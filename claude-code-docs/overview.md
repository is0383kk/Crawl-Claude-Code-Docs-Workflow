# Claude Code 概要

> Claude Code について学びましょう。Anthropic のエージェント型コーディングツールで、ターミナルで動作し、アイデアをこれまで以上に速くコードに変えるのに役立ちます。

## 30秒で始める

前提条件:

* [Claude.ai](https://claude.ai) (推奨) または [Claude Console](https://console.anthropic.com/) アカウント

**Claude Code をインストール:**

<Tabs>
  <Tab title="macOS/Linux">
    ```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```
  </Tab>

  <Tab title="Homebrew">
    ```bash  theme={null}
    brew install --cask claude-code
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell  theme={null}
    irm https://claude.ai/install.ps1 | iex
    ```
  </Tab>

  <Tab title="NPM">
    ```bash  theme={null}
    npm install -g @anthropic-ai/claude-code
    ```

    [Node.js 18+](https://nodejs.org/en/download/) が必要です
  </Tab>
</Tabs>

**Claude Code の使用を開始:**

```bash  theme={null}
cd your-project
claude
```

初回使用時にログインするよう促されます。これだけです! [クイックスタート (5分) に進む →](/ja/quickstart)

<Tip>
  インストールオプションについては [高度なセットアップ](/ja/setup) を、問題が発生した場合は [トラブルシューティング](/ja/troubleshooting) を参照してください。
</Tip>

<Note>
  **新しい VS Code 拡張機能 (ベータ版)**: グラフィカルインターフェースをお好みですか? 新しい [VS Code 拡張機能](/ja/vs-code) は、ターミナルの知識を必要とせずに、使いやすいネイティブ IDE エクスペリエンスを提供します。マーケットプレイスからインストールして、サイドバーで Claude を使用してコーディングを開始するだけです。
</Note>

## Claude Code があなたのためにすること

* **説明からフィーチャーを構築**: Claude に平易な英語で何を構築したいかを伝えます。計画を立て、コードを書き、それが機能することを確認します。
* **バグをデバッグして修正**: バグを説明するか、エラーメッセージを貼り付けます。Claude Code はコードベースを分析し、問題を特定し、修正を実装します。
* **任意のコードベースをナビゲート**: チームのコードベースについて何でも質問し、思慮深い回答を得ます。Claude Code はプロジェクト全体の構造を認識し、ウェブから最新情報を見つけることができ、[MCP](/ja/mcp) を使用すると Google Drive、Figma、Slack などの外部データソースから取得できます。
* **退屈なタスクを自動化**: 厄介な lint の問題を修正し、マージコンフリクトを解決し、リリースノートを作成します。開発者マシンから単一のコマンドで、または CI で自動的にすべてを実行します。

## 開発者が Claude Code を愛する理由

* **ターミナルで動作**: 別のチャットウィンドウではありません。別の IDE ではありません。Claude Code はあなたが既に作業している場所で、既に愛用しているツールで、あなたに会います。
* **アクションを実行**: Claude Code はファイルを直接編集し、コマンドを実行し、コミットを作成できます。もっと必要ですか? [MCP](/ja/mcp) を使用すると、Claude は Google Drive のデザインドキュメントを読み、Jira のチケットを更新したり、*あなたの* カスタム開発者ツーリングを使用したりできます。
* **Unix 哲学**: Claude Code は構成可能でスクリプト化可能です。`tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *が動作します*。CI は `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"` を実行できます。
* **エンタープライズ対応**: Claude API を使用するか、AWS または GCP でホストします。エンタープライズグレードの [セキュリティ](/ja/security)、[プライバシー](/ja/data-usage)、および [コンプライアンス](https://trust.anthropic.com/) が組み込まれています。

## 次のステップ

<CardGroup>
  <Card title="クイックスタート" icon="rocket" href="/ja/quickstart">
    実践的な例で Claude Code の動作を確認してください
  </Card>

  <Card title="一般的なワークフロー" icon="graduation-cap" href="/ja/common-workflows">
    一般的なワークフローのステップバイステップガイド
  </Card>

  <Card title="トラブルシューティング" icon="wrench" href="/ja/troubleshooting">
    Claude Code の一般的な問題の解決策
  </Card>

  <Card title="IDE セットアップ" icon="laptop" href="/ja/vs-code">
    IDE に Claude Code を追加
  </Card>
</CardGroup>

## 追加リソース

<CardGroup>
  <Card title="Agent SDK で構築" icon="code-branch" href="https://docs.claude.com/en/docs/agent-sdk/overview">
    Claude Agent SDK でカスタム AI エージェントを作成
  </Card>

  <Card title="AWS または GCP でホスト" icon="cloud" href="/ja/third-party-integrations">
    Amazon Bedrock または Google Vertex AI で Claude Code を構成
  </Card>

  <Card title="設定" icon="gear" href="/ja/settings">
    ワークフローに合わせて Claude Code をカスタマイズ
  </Card>

  <Card title="コマンド" icon="terminal" href="/ja/cli-reference">
    CLI コマンドとコントロールについて学ぶ
  </Card>

  <Card title="リファレンス実装" icon="code" href="https://github.com/anthropics/claude-code/tree/main/.devcontainer">
    開発コンテナリファレンス実装をクローン
  </Card>

  <Card title="セキュリティ" icon="shield" href="/ja/security">
    Claude Code のセーフガードと安全な使用のベストプラクティスを発見
  </Card>

  <Card title="プライバシーとデータ使用" icon="lock" href="/ja/data-usage">
    Claude Code がデータをどのように処理するかを理解
  </Card>
</CardGroup>
