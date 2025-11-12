#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code 日本語ドキュメント (https://code.claude.com/docs/ja/) を巡回し、
対応する .md を取得してリポジトリの docs/ 配下に保存します。
- 例: https://code.claude.com/docs/ja/sub-agents  -> docs/ja/sub-agents.md
- 例: https://code.claude.com/docs/ja/            -> docs/ja/index.md
"""

import hashlib
import logging
import pathlib
import re
import time
from typing import Optional
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE = "https://code.claude.com"
START_PATH = "/docs/ja/"
START_URL = urljoin(BASE, START_PATH)
OUTPUT_ROOT = pathlib.Path("claude-code-docs")
TIMEOUT = 120
SLEEP_SEC = 0.5
HEADERS = {
    "User-Agent": "DocsSyncBot/1.0 (+https://github.com/is0383kk/Crawl-Claude-Code-Docs-Workflow)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


# 収集対象: /docs/ja/ 以下（クエリ・フラグメントは除外）
def is_target_path(url: str) -> bool:
    try:
        p = urlparse(url)
        if p.netloc and p.netloc != urlparse(BASE).netloc:
            return False
        path = p.path or ""
        return path.startswith("/docs/ja/")
    except Exception:
        return False


# 出力ファイルパス: /docs/ja/foo -> docs/ja/foo.md
def to_output_path(path: str) -> Optional[pathlib.Path]:
    path = path.rstrip("/")

    # ルートは保存しない
    if path in ("/docs/ja", "/docs/ja/"):
        return None

    # 末尾 .md を除去（念のため）
    path = re.sub(r"\.md$", "", path)

    # /docs/ja/ のプレフィックスを落として相対パス化
    if path.startswith("/docs/ja/"):
        rel = path[len("/docs/ja/") :]
    elif path.startswith("/docs/"):
        # 念のためのフォールバック（将来他言語を取りたい場合など）
        rel = path[len("/docs/") :]
    else:
        # ここに来るのは通常想定外
        rel = path.lstrip("/")

    return OUTPUT_ROOT / f"{rel}.md"


def ensure_parent_dir(p: pathlib.Path):
    p.parent.mkdir(parents=True, exist_ok=True)


def write_if_changed(filepath: pathlib.Path, content: bytes) -> bool:
    ensure_parent_dir(filepath)
    new_hash = hashlib.sha256(content).hexdigest().encode()
    if filepath.exists():
        old = filepath.read_bytes()
        # 既存ファイルのハッシュをコメント行として最終行に入れていない前提で比較
        if hashlib.sha256(old).hexdigest().encode() == new_hash:
            return False
    filepath.write_bytes(content)
    return True


def fetch(url: str) -> requests.Response:
    return requests.get(url, headers=HEADERS, timeout=TIMEOUT)


def normalize_href(href: str, base: str) -> str:
    # フラグメントとクエリを落とす
    href, _frag = urldefrag(href)
    return urljoin(base, href)


def collect_paths() -> set[str]:
    """/docs/ja/ 以下のHTMLを辿って内部リンクのパス集合を作る。"""
    seen = set()
    queue = [START_URL]

    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)

        try:
            r = fetch(url)
            if r.status_code != 200 or "text/html" not in r.headers.get(
                "Content-Type", ""
            ):
                continue
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.select("a[href]"):
                href = normalize_href(str(a["href"]), url)
                if not is_target_path(href):
                    continue
                p = urlparse(href)
                # HTMLページ（.md 直リンクは巡回対象に含めない）
                if p.path.endswith(".md"):
                    href = href[:-3]
                if href not in seen and href not in queue:
                    queue.append(href)
            time.sleep(SLEEP_SEC)
        except Exception as e:
            logging.warning(f"collect error: {url} -> {e}")
            continue

    # 収集したURLからパスのみ抽出
    paths = set(urlparse(u).path for u in seen if is_target_path(u))
    return paths


def fetch_markdown_for_path(path: str) -> tuple[int, bytes | None]:
    if path.rstrip("/") in ("/docs/ja", "/docs/ja/"):
        md_url = urljoin(BASE, "/docs/ja.md")  # 一応試す（多くは404）
        r = fetch(md_url)
        if r.status_code == 200 and "text/markdown" in r.headers.get(
            "Content-Type", ""
        ):
            return r.status_code, r.content
        # ルートは通常、個別 .md 化されていない想定。代替としてHTML→簡易Headerを付けて保存
        r = fetch(START_URL)
        if r.status_code == 200:
            fallback = f"# Claude Code ドキュメント（日本語トップ）\n\n元URL: {START_URL}\n".encode(
                "utf-8"
            )
            return 200, fallback
        return r.status_code, None

    # 通常は「末尾に .md を付ける」
    md_url = urljoin(BASE, path.rstrip("/") + ".md")
    r = fetch(md_url)
    if r.status_code == 200 and "text/markdown" in r.headers.get("Content-Type", ""):
        return r.status_code, r.content
    return r.status_code, None


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    logging.info("Collecting paths under /docs/ja/ ...")
    paths = sorted(collect_paths())
    logging.info(f"Found {len(paths)} html paths.")

    changed = 0
    skipped = 0
    failed = 0

    for path in paths:
        outpath = to_output_path(path)
        if outpath is None:
            logging.info(f"Skip root path (no file): {path}")
            continue

        try:
            status, content = fetch_markdown_for_path(path)
            if status == 200 and content:
                if write_if_changed(outpath, content):
                    changed += 1
                    logging.info(f"Saved: {outpath}")
                else:
                    skipped += 1
                    logging.info(f"Unchanged: {outpath}")
            else:
                failed += 1
                logging.warning(f"Markdown not available ({status}): {path}")
        except Exception as e:
            failed += 1
            logging.warning(f"Error on {path}: {e}")
        time.sleep(SLEEP_SEC)

    logging.info(f"Done. changed={changed}, unchanged={skipped}, failed={failed}")


if __name__ == "__main__":
    main()
