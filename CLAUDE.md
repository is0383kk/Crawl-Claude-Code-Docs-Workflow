# Claude Code 公式ドキュメント概要

このファイルは `claude-code-docs/` 配下の各マークダウンファイルの概要をまとめたものです。
Claude Code の使い方を調べる際に、どのドキュメントを参照したらよいかを判断するために使用します。

---

## claude-code-docs/agent-teams.md

複数の Claude Code セッションをチームとして協調動作させる方法（実験的機能）。チームリードとチームメイトが共有タスクリストと直接メッセージングで連携する仕組みを説明。

## claude-code-docs/amazon-bedrock.md

Amazon Bedrock を使用して Claude Code を実行する方法を説明。AWS 環境での認証、IAM ロール、API キー、クロスアカウントアクセス、リージョン設定などを含む。

## claude-code-docs/analytics.md

Claude Code の使用状況とコストを追跡・監視するためのアナリティクス機能。OpenTelemetry メトリクス、カスタムエクスポーター、動的ヘッダーの設定方法を説明。

## claude-code-docs/authentication.md

Claude Code のログインと認証設定方法。個人ユーザー（Claude.ai）から Teams/Enterprise（Console、クラウドプロバイダー）まで対応する各種認証方式とクレデンシャル管理を説明。

## claude-code-docs/azure-ai-foundry.md

Microsoft Azure AI Foundry を使用して Claude Code を実行する方法。API キー認証または Entra ID 認証の設定、モデルバージョンのピン留め、RBAC 設定を説明。

## claude-code-docs/best-practices.md

Claude Code を効果的に使用するためのベストプラクティス。コンテキスト管理、効果的なプロンプト作成、環境設定（CLAUDE.md・フック・スキル）、自動化・スケールアップの方法を説明。

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

## claude-code-docs/desktop-quickstart.md

Claude Code デスクトップアプリのクイックスタートガイド。インストール手順から最初のセッション開始まで、差分ビュー・並列セッション・スケジュールタスクなど主要機能の紹介を含む。

## claude-code-docs/devcontainer.md

開発コンテナ（devcontainer）で Claude Code を使用する方法。VS Code Dev Containers、Docker、分離環境での設定を説明。

## claude-code-docs/discover-plugins.md

Claude Code のプラグインマーケットプレイスでプラグインを発見・インストールする方法。プラグインの検索、評価、インストール手順を説明。

## claude-code-docs/fast-mode.md

Claude Opus 4.6 のファストモード機能。2.5倍高速な応答を実現する `/fast` コマンドでのトグル方法、コストとのトレードオフ、適切な使用シナリオ、組織向けの管理設定を説明。

## claude-code-docs/features-overview.md

Claude Code の各拡張機能（CLAUDE.md、Skills、MCP、サブエージェント、エージェントチーム、フック、プラグイン）の概要。各機能の役割・使い分けの基準・コンテキストコストを説明。

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

## claude-code-docs/how-claude-code-works.md

Claude Code のエージェントループと動作原理。コンテキスト収集・アクション実行・結果検証のループ、組み込みツール（ファイル操作・検索・実行・Web など）、セッション管理、チェックポイントの仕組みを説明。

## claude-code-docs/iam.md

Identity and Access Management（IAM）の設定。権限、アクセス制御、エンタープライズ管理設定を説明。

## claude-code-docs/ide-integrations.md

VS Code での Claude Code 拡張機能の詳細な使用方法。インストール、@-メンション参照、プランモード、キーボードショートカット、MCP サーバー設定、サードパーティプロバイダー統合を説明。

## claude-code-docs/interactive-mode.md

Claude Code のインタラクティブモードの使用方法。キーボードショートカット、入力モード、インタラクティブ機能を説明。

## claude-code-docs/jetbrains.md

JetBrains IDE（IntelliJ、PyCharm など）で Claude Code を使用する方法。プラグインのインストール、設定、統合を説明。

## claude-code-docs/keybindings.md

Claude Code のキーボードショートカットのカスタマイズ方法。`/keybindings` コマンドで設定ファイルを作成・編集し、コンテキスト別のバインディング、利用可能なアクション一覧、キーストローク記法、バインディング解除の方法を説明。

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

## claude-code-docs/permissions.md

Claude Code の権限システムと細かい許可ルールの設定方法。ツール種別ごとの allow/ask/deny ルール、パーミッションモード（default/acceptEdits/plan/bypassPermissions）、組織向けの管理設定を説明。

## claude-code-docs/plugin-marketplaces.md

プラグインマーケットプレイスの管理と使用方法。マーケットプレイスの追加、プラグインの発見、エンタープライズ制限を説明。

## claude-code-docs/plugins-reference.md

プラグイン開発者向けの技術リファレンス。プラグインの構造、API、コンポーネント、配布方法を説明。

## claude-code-docs/plugins.md

Claude Code プラグインシステムの概要。プラグインのインストール、設定、管理方法を説明。

## claude-code-docs/quickstart.md

Claude Code のクイックスタートガイド。インストールから最初のタスクまでのステップバイステップの手順を提供。

## claude-code-docs/remote-control.md

ローカルの Claude Code セッションをブラウザやモバイルアプリからリモート操作する方法。セッションの開始・接続、セキュリティモデル、Claude Code on the web との違いを説明。

## claude-code-docs/sandboxing.md

Claude Code のサンドボックス機能。ファイルシステムとネットワーク分離による安全なエージェント実行を説明。

## claude-code-docs/scheduled-tasks.md

Claude Code セッション内でプロンプトを定期実行するスケジュールタスク機能。`/loop` コマンドによる繰り返し実行、一度きりのリマインダー設定、cron 式の使用方法を説明。

## claude-code-docs/security.md

Claude Code のセキュリティ機能とベストプラクティス。プロンプトインジェクション保護、権限システム、データ保護を説明。

## claude-code-docs/server-managed-settings.md

組織管理者が Web インターフェースから Claude Code の設定を一元管理するサーバー管理設定（パブリックベータ）。MDM 不要で Teams/Enterprise に設定を配布する方法とセキュリティ考慮事項を説明。

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

## claude-code-docs/terminal-guide.md

ターミナル初心者向けの Claude Code インストールガイド。macOS/Linux および Windows（PowerShell）での Claude Code セットアップ手順をステップバイステップで説明。

## claude-code-docs/third-party-integrations.md

サードパーティプロバイダーとの統合。Amazon Bedrock、Google Vertex AI、Microsoft Foundry のデプロイオプションを説明。

## claude-code-docs/troubleshooting.md

Claude Code の一般的な問題のトラブルシューティング。インストール、権限、認証、パフォーマンスの問題の解決方法を説明。

## claude-code-docs/vs-code.md

VS Code で Claude Code 拡張機能を使用する方法。インストール、設定、インライン差分、キーボードショートカットを説明。

## claude-code-docs/zero-data-retention.md

Claude for Enterprise における Zero Data Retention（ZDR）機能の説明。ZDR の適用範囲（対象・対象外）、ZDR 有効時に無効化される機能、リクエスト方法を説明。
