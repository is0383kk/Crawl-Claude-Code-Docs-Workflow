#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
複数の公式ドキュメントサイトを巡回し、対応する .md を取得してリポジトリ配下に保存します。
- https://code.claude.com/docs/en/ -> claude-code-docs/
- https://docs.openclaw.ai/        -> openclaw-docs/
各ページは URL 末尾に .md を付けることでマークダウンとして取得できます。
"""

import hashlib
import logging
import pathlib
import re
import time
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

TIMEOUT = 120
SLEEP_SEC = 0.5
HEADERS = {
    "User-Agent": "DocsSyncBot/1.0 (+https://github.com/is0383kk/Crawl-Claude-Code-Docs-Workflow)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


@dataclass
class CrawlTarget:
    base: str
    start_path: str
    output_root: pathlib.Path


TARGETS = [
    CrawlTarget(
        base="https://code.claude.com",
        start_path="/docs/en/",
        output_root=pathlib.Path("claude-code-docs"),
    ),
    CrawlTarget(
        base="https://docs.openclaw.ai",
        start_path="/",
        output_root=pathlib.Path("openclaw-docs"),
    ),
]


def is_target_path(url: str, target: CrawlTarget) -> bool:
    try:
        p = urlparse(url)
        if p.netloc and p.netloc != urlparse(target.base).netloc:
            return False
        path = p.path or ""
        return path.startswith(target.start_path)
    except Exception:
        return False


def to_output_path(path: str, target: CrawlTarget) -> Optional[pathlib.Path]:
    path = path.rstrip("/")
    start_stripped = target.start_path.rstrip("/")

    # ルートは保存しない
    if not path or path == start_stripped:
        return None

    # 末尾 .md を除去（念のため）
    path = re.sub(r"\.md$", "", path)

    # start_path プレフィックスを落として相対パス化
    if path.startswith(target.start_path):
        rel = path[len(target.start_path):]
    elif path.startswith(start_stripped):
        rel = path[len(start_stripped):].lstrip("/")
    else:
        rel = path.lstrip("/")

    if not rel:
        return None

    return target.output_root / f"{rel}.md"


def ensure_parent_dir(p: pathlib.Path):
    p.parent.mkdir(parents=True, exist_ok=True)


def write_if_changed(filepath: pathlib.Path, content: bytes) -> bool:
    ensure_parent_dir(filepath)
    new_hash = hashlib.sha256(content).hexdigest().encode()
    if filepath.exists():
        old = filepath.read_bytes()
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


def collect_paths(target: CrawlTarget) -> set[str]:
    """start_path 以下の HTML を辿って内部リンクのパス集合を作る。"""
    start_url = urljoin(target.base, target.start_path)
    seen = set()
    queue = [start_url]

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
                if not is_target_path(href, target):
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
    paths = set(urlparse(u).path for u in seen if is_target_path(u, target))
    return paths


def fetch_markdown_for_path(path: str, target: CrawlTarget) -> tuple[int, bytes | None]:
    # 末尾に .md を付けて取得
    md_url = urljoin(target.base, path.rstrip("/") + ".md")
    r = fetch(md_url)
    if r.status_code == 200 and "text/markdown" in r.headers.get("Content-Type", ""):
        return r.status_code, r.content
    return r.status_code, None


def crawl_target(target: CrawlTarget) -> tuple[int, int, int]:
    start_url = urljoin(target.base, target.start_path)
    logging.info(f"Collecting paths under {start_url} ...")
    paths = sorted(collect_paths(target))
    logging.info(f"Found {len(paths)} html paths.")

    target.output_root.mkdir(parents=True, exist_ok=True)

    changed = skipped = failed = 0

    for path in paths:
        outpath = to_output_path(path, target)
        if outpath is None:
            logging.info(f"Skip root path (no file): {path}")
            continue

        try:
            status, content = fetch_markdown_for_path(path, target)
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

    return changed, skipped, failed


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    total_changed = total_skipped = total_failed = 0

    for target in TARGETS:
        logging.info(f"=== Crawling: {target.base}{target.start_path} -> {target.output_root} ===")
        c, s, f = crawl_target(target)
        total_changed += c
        total_skipped += s
        total_failed += f
        logging.info(f"  changed={c}, unchanged={s}, failed={f}")

    logging.info(f"All done. changed={total_changed}, unchanged={total_skipped}, failed={total_failed}")


if __name__ == "__main__":
    main()
