# Crawl Claude Code Docs Workflow

Claude Code の[公式ドキュメント](https://code.claude.com/docs/en/)を自動的にクロールし、  
Markdown ファイルとしてリポジトリに保存するためのワークフローです。

## 概要

このプロジェクトは、Claude Code の公式ドキュメントを定期的に取得し、マークダウンファイルとして保存＋変更を追跡するためのツールです。  
GitHub Actions を使用して毎日自動実行され、ドキュメントの更新を検出すると自動的にリポジトリにコミットします。

## 機能

- `https://code.claude.com/docs/en/` 配下の全ページを自動巡回
- 各ページの Markdown ファイルを取得して保存
- ファイルの変更検出（ハッシュ比較）
- GitHub Actions による自動実行（毎日 JST 03:00）

## セットアップ

### 必要なもの

- Python 3.11 以上
- [uv](https://github.com/astral-sh/uv)（推奨）

### インストール

```bash
# リポジトリのクローン
git clone https://github.com/is0383kk/Crawl-Claude-Code-Docs-Workflow.git
cd Crawl-Claude-Code-Docs-Workflow

# 依存関係のインストール（uv使用）
uv sync
```

## 使い方

### ローカルでの実行

```bash
# スクリプトの実行
uv run crawl_claude_code_docs.py
```

実行すると、`claude-code-docs/` ディレクトリ配下に Markdown ファイルが保存されます。

### GitHub Actions での実行

- **自動実行**: 毎日 JST 03:00 に自動的に実行されます
- **手動実行**: GitHub Actions の UI から「Sync Claude Code docs (en)」ワークフローを手動で実行できます

## プロジェクト構造

```
.
├── .github/
│   └── workflow/
│       └── sync-claude-docs.yml  # GitHub Actionsワークフロー
├── claude-code-docs/             # クロールしたドキュメント（自動生成）
├── crawl_claude_code_docs.py     # メインスクリプト
├── pyproject.toml                # プロジェクト設定
├── uv.lock                       # 依存関係のロック
└── README.md                     # このファイル
```
