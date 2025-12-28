# Claude Code 公式ドキュメント概要

このファイルは `claude-code-docs/` 配下の各マークダウンファイルの概要をまとめたものです。
Claude Code の使い方を調べる際に、どのドキュメントを参照したらよいかを判断するために使用します。

---

## claude-code-docs/amazon-bedrock.md

Amazon Bedrock を使用して Claude Code を実行する方法を説明。AWS 環境での認証、IAM ロール、API キー、クロスアカウントアクセス、リージョン設定などを含む。

## claude-code-docs/analytics.md

Claude Code の使用状況とコストを追跡・監視するためのアナリティクス機能。OpenTelemetry メトリクス、カスタムエクスポーター、動的ヘッダーの設定方法を説明。

## claude-code-docs/checkpointing.md

Claude Code のチェックポイント機能の説明。会話の特定のポイントへの保存・復元、チェックポイントの作成・削除・リストアップ方法を含む。

## claude-code-docs/chrome.md

Chrome 拡張機能を使用して Claude Code とブラウザを統合する方法。スクリーンショット撮影、URL の共有、Web 開発ワークフローへの統合方法を説明。

## claude-code-docs/claude-code-on-the-web.md

Web ブラウザから Claude Code を使用する方法。クラウド実行、非同期タスク、GitHub 統合、ネットワークアクセス制御などを含む。

## claude-code-docs/cli-reference.md

Claude Code CLI の完全なコマンドラインリファレンス。すべての CLI フラグ、オプション、使用例を含む。

## claude-code-docs/common-workflows.md

Claude Code を使用した一般的なワークフローとタスク。コードレビュー、デバッグ、テスト、リファクタリング、ドキュメント作成などの手順を説明。

## claude-code-docs/costs.md

Claude Code の使用にかかるコストの理解と管理。トークン使用量、プロンプトキャッシング、コスト最適化のベストプラクティスを説明。

## claude-code-docs/data-usage.md

Claude Code によるデータの使用方法とプライバシーポリシー。データの保存、処理、保持期間、ユーザーの権利を説明。

## claude-code-docs/desktop.md

Claude Code のデスクトップアプリケーションの使用方法。インストール、設定、機能の説明を含む。

## claude-code-docs/devcontainer.md

開発コンテナ（devcontainer）で Claude Code を使用する方法。VS Code Dev Containers、Docker、分離環境での設定を説明。

## claude-code-docs/discover-plugins.md

Claude Code のプラグインマーケットプレイスでプラグインを発見・インストールする方法。プラグインの検索、評価、インストール手順を説明。

## claude-code-docs/github-actions.md

GitHub Actions で Claude Code を使用する方法。CI/CD パイプライン、自動化、GitHub アプリの設定を説明。

## claude-code-docs/gitlab-ci-cd.md

GitLab CI/CD で Claude Code を統合する方法。パイプライン設定、認証、自動化ワークフローを説明。

## claude-code-docs/google-vertex-ai.md

Google Vertex AI を使用して Claude Code を実行する方法。GCP 認証、プロジェクト設定、リージョン設定を説明。

## claude-code-docs/headless.md

ヘッドレスモード（非インタラクティブモード）で Claude Code を使用する方法。自動化スクリプト、CI/CD 統合、バッチ処理を説明。

## claude-code-docs/hooks-guide.md

Claude Code フックのガイド。フックの作成、設定、使用方法を含む包括的なチュートリアル。

## claude-code-docs/hooks.md

Claude Code のフック機能の概要。ツールイベント時にカスタムコマンドを実行する方法を説明。

## claude-code-docs/iam.md

Identity and Access Management（IAM）の設定。権限、アクセス制御、エンタープライズ管理設定を説明。

## claude-code-docs/interactive-mode.md

Claude Code のインタラクティブモードの使用方法。キーボードショートカット、入力モード、インタラクティブ機能を説明。

## claude-code-docs/jetbrains.md

JetBrains IDE（IntelliJ、PyCharm など）で Claude Code を使用する方法。プラグインのインストール、設定、統合を説明。

## claude-code-docs/legal-and-compliance.md

Claude Code の法的およびコンプライアンス情報。利用規約、プライバシーポリシー、データ保護規制を説明。

## claude-code-docs/llm-gateway.md

LLM ゲートウェイを使用した Claude Code のデプロイ。集中管理、使用状況追跡、予算管理、監査ログを説明。

## claude-code-docs/mcp.md

Model Context Protocol (MCP) サーバーの設定と使用方法。外部ツールやデータソースへの接続を説明。

## claude-code-docs/memory.md

Claude Code のメモリ管理。CLAUDE.md ファイルを使用したセッション間での指示とコンテキストの保持方法を説明。

## claude-code-docs/microsoft-foundry.md

Microsoft Foundry (Azure) を使用して Claude Code を実行する方法。API キー認証、Entra ID 認証、Azure 請求を説明。

## claude-code-docs/model-config.md

Claude Code のモデル設定。モデルの選択、カスタム設定、環境変数によるモデル指定を説明。

## claude-code-docs/monitoring-usage.md

Claude Code の使用状況の監視。OpenTelemetry メトリクス、ログ、監査追跡を説明。

## claude-code-docs/network-config.md

企業ネットワーク環境での Claude Code の設定。プロキシサーバー、SSL/TLS 要件、証明書設定を説明。

## claude-code-docs/output-styles.md

Claude Code の出力スタイルのカスタマイズ。システムプロンプトの調整、応答形式、コミュニケーションスタイルを説明。

## claude-code-docs/overview.md

Claude Code の概要と主要機能の紹介。製品の全体像、主要な機能、使い始め方を説明。

## claude-code-docs/plugin-marketplaces.md

プラグインマーケットプレイスの管理と使用方法。マーケットプレイスの追加、プラグインの発見、エンタープライズ制限を説明。

## claude-code-docs/plugins-reference.md

プラグイン開発者向けの技術リファレンス。プラグインの構造、API、コンポーネント、配布方法を説明。

## claude-code-docs/plugins.md

Claude Code プラグインシステムの概要。プラグインのインストール、設定、管理方法を説明。

## claude-code-docs/quickstart.md

Claude Code のクイックスタートガイド。インストールから最初のタスクまでのステップバイステップの手順を提供。

## claude-code-docs/sandboxing.md

Claude Code のサンドボックス機能。ファイルシステムとネットワーク分離による安全なエージェント実行を説明。

## claude-code-docs/security.md

Claude Code のセキュリティ機能とベストプラクティス。プロンプトインジェクション保護、権限システム、データ保護を説明。

## claude-code-docs/settings.md

Claude Code の設定システム。グローバル設定、プロジェクト設定、環境変数、スコープの説明を含む。

## claude-code-docs/setup.md

Claude Code のセットアップと初期設定。インストール方法、認証、システム要件を説明。

## claude-code-docs/skills.md

Agent Skills の作成と使用方法。スキルの定義、設定、管理、トラブルシューティングを説明。

## claude-code-docs/slack.md

Slack ワークスペースから Claude Code を使用する方法。Slack での Claude メンション、自動ルーティング、GitHub 統合、リポジトリ選択、セッション管理を説明。

## claude-code-docs/slash-commands.md

Claude Code のスラッシュコマンド。組み込みコマンド、カスタムコマンド、MCP コマンド、プラグインコマンドを説明。

## claude-code-docs/statusline.md

Claude Code のステータスライン設定。カスタムステータスラインの作成、JSON 入力構造、サンプルスクリプトを説明。

## claude-code-docs/sub-agents.md

サブエージェントの作成と使用方法。専門化された AI アシスタント、タスク特化型ワークフロー、コンテキスト管理を説明。

## claude-code-docs/terminal-config.md

Claude Code のターミナル設定の最適化。テーマ設定、改行入力、通知設定、大規模入力の取り扱い、Vim モードなどのターミナルカスタマイズ方法を説明。

## claude-code-docs/third-party-integrations.md

サードパーティプロバイダーとの統合。Amazon Bedrock、Google Vertex AI、Microsoft Foundry のデプロイオプションを説明。

## claude-code-docs/troubleshooting.md

Claude Code の一般的な問題のトラブルシューティング。インストール、権限、認証、パフォーマンスの問題の解決方法を説明。

## claude-code-docs/vs-code.md

VS Code で Claude Code 拡張機能を使用する方法。インストール、設定、インライン差分、キーボードショートカットを説明。
