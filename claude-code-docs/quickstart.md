# クイックスタート

> Claude Codeへようこそ！

このクイックスタートガイドを使用すれば、わずか数分でAI搭載のコーディング支援を使用できるようになります。最後には、一般的な開発タスクにClaude Codeを使用する方法を理解できるようになります。

## 始める前に

以下のものを用意してください：

* ターミナルまたはコマンドプロンプトを開いた状態
* 作業するコードプロジェクト
* [Claude.ai](https://claude.ai)（推奨）または[Claude Console](https://console.anthropic.com/)アカウント

## ステップ1：Claude Codeをインストール

To install Claude Code, use one of the following methods:

<Tabs>
  <Tab title="Native Install (Recommended)">
    **Homebrew (macOS, Linux):**

    ```sh  theme={null}
    brew install --cask claude-code
    ```

    **macOS, Linux, WSL:**

    ```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Windows PowerShell:**

    ```powershell  theme={null}
    irm https://claude.ai/install.ps1 | iex
    ```

    **Windows CMD:**

    ```batch  theme={null}
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```
  </Tab>

  <Tab title="NPM">
    If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):

    ```sh  theme={null}
    npm install -g @anthropic-ai/claude-code
    ```
  </Tab>
</Tabs>

## ステップ2：アカウントにログイン

Claude Codeを使用するにはアカウントが必要です。`claude`コマンドでインタラクティブセッションを開始すると、ログインが必要になります：

```bash  theme={null}
claude
# 初回使用時にログインするよう促されます
```

```bash  theme={null}
/login
# プロンプトに従ってアカウントでログインします
```

以下のいずれかのアカウントタイプでログインできます：

* [Claude.ai](https://claude.ai)（サブスクリプションプラン - 推奨）
* [Claude Console](https://console.anthropic.com/)（プリペイドクレジット付きAPIアクセス）

ログイン後、認証情報が保存され、再度ログインする必要はありません。

<Note>
  Claude ConsoleアカウントでClaude Codeを初めて認証すると、「Claude Code」というワークスペースが自動的に作成されます。このワークスペースは、組織内のすべてのClaude Code使用に対する一元化されたコスト追跡と管理を提供します。
</Note>

<Note>
  同じメールアドレスの下に両方のアカウントタイプを持つことができます。再度ログインする必要がある場合またはアカウントを切り替える場合は、Claude Code内で`/login`コマンドを使用してください。
</Note>

## ステップ3：最初のセッションを開始

任意のプロジェクトディレクトリでターミナルを開き、Claude Codeを開始します：

```bash  theme={null}
cd /path/to/your/project
claude
```

セッション情報、最近の会話、最新の更新が表示されたClaude Codeウェルカムスクリーンが表示されます。利用可能なコマンドについては`/help`を入力するか、前の会話を続行するには`/resume`を入力してください。

<Tip>
  ログイン後（ステップ2）、認証情報がシステムに保存されます。詳細については、[認証情報管理](/ja/iam#credential-management)を参照してください。
</Tip>

## ステップ4：最初の質問をする

コードベースを理解することから始めましょう。以下のコマンドのいずれかを試してください：

```
> what does this project do?
```

Claudeはファイルを分析し、概要を提供します。より具体的な質問をすることもできます：

```
> what technologies does this project use?
```

```
> where is the main entry point?
```

```
> explain the folder structure
```

Claude自身の機能について質問することもできます：

```
> what can Claude Code do?
```

```
> how do I use slash commands in Claude Code?
```

```
> can Claude Code work with Docker?
```

<Note>
  Claude Codeは必要に応じてファイルを読み込みます。コンテキストを手動で追加する必要はありません。Claudeは独自のドキュメントにアクセスでき、その機能と機能について質問に答えることができます。
</Note>

## ステップ5：最初のコード変更を行う

次に、Claude Codeに実際のコーディングを行わせましょう。簡単なタスクを試してください：

```
> add a hello world function to the main file
```

Claude Codeは以下を実行します：

1. 適切なファイルを見つける
2. 提案された変更を表示する
3. 承認を求める
4. 編集を行う

<Note>
  Claude Codeは常にファイルを変更する前に許可を求めます。個別の変更を承認するか、セッション中に「すべて受け入れる」モードを有効にすることができます。
</Note>

## ステップ6：Claude CodeでGitを使用

Claude Codeはgit操作を会話型にします：

```
> what files have I changed?
```

```
> commit my changes with a descriptive message
```

より複雑なGit操作を促すこともできます：

```
> create a new branch called feature/quickstart
```

```
> show me the last 5 commits
```

```
> help me resolve merge conflicts
```

## ステップ7：バグを修正するか機能を追加

Claudeはデバッグと機能実装に精通しています。

自然言語で実現したいことを説明してください：

```
> add input validation to the user registration form
```

または既存の問題を修正してください：

```
> there's a bug where users can submit empty forms - fix it
```

Claude Codeは以下を実行します：

* 関連するコードを見つける
* コンテキストを理解する
* ソリューションを実装する
* 利用可能な場合はテストを実行する

## ステップ8：その他の一般的なワークフローを試す

Claudeと連携する方法はいくつかあります：

**コードをリファクタリング**

```
> refactor the authentication module to use async/await instead of callbacks
```

**テストを作成**

```
> write unit tests for the calculator functions
```

**ドキュメントを更新**

```
> update the README with installation instructions
```

**コードレビュー**

```
> review my changes and suggest improvements
```

<Tip>
  **覚えておいてください**：Claude Codeはあなたのペアプログラマーです。有能な同僚と話すように話しかけてください。実現したいことを説明すれば、それを達成するのに役立ちます。
</Tip>

## 必須コマンド

日常的に使用する最も重要なコマンドは以下の通りです：

| コマンド                | 機能                | 例                                   |
| ------------------- | ----------------- | ----------------------------------- |
| `claude`            | インタラクティブモードを開始    | `claude`                            |
| `claude "task"`     | 1回限りのタスクを実行       | `claude "fix the build error"`      |
| `claude -p "query"` | 1回限りのクエリを実行してから終了 | `claude -p "explain this function"` |
| `claude -c`         | 最新の会話を続行          | `claude -c`                         |
| `claude -r`         | 前の会話を再開           | `claude -r`                         |
| `claude commit`     | Gitコミットを作成        | `claude commit`                     |
| `/clear`            | 会話履歴をクリア          | `> /clear`                          |
| `/help`             | 利用可能なコマンドを表示      | `> /help`                           |
| `exit` または Ctrl+C   | Claude Codeを終了    | `> exit`                            |

完全なコマンドリストについては、[CLIリファレンス](/ja/cli-reference)を参照してください。

## 初心者向けのプロのヒント

<AccordionGroup>
  <Accordion title="リクエストを具体的にする">
    代わりに：「バグを修正して」

    試してください：「ユーザーが間違った認証情報を入力した後に空白の画面が表示されるログインバグを修正してください」
  </Accordion>

  <Accordion title="段階的な指示を使用">
    複雑なタスクをステップに分割します：

    ```
    > 1. create a new database table for user profiles
    ```

    ```
    > 2. create an API endpoint to get and update user profiles
    ```

    ```
    > 3. build a webpage that allows users to see and edit their information
    ```
  </Accordion>

  <Accordion title="Claudeに最初に探索させる">
    変更を加える前に、Claudeにコードを理解させます：

    ```
    > analyze the database schema
    ```

    ```
    > build a dashboard showing products that are most frequently returned by our UK customers
    ```
  </Accordion>

  <Accordion title="ショートカットで時間を節約">
    * `?`を押してすべての利用可能なキーボードショートカットを表示
    * タブをコマンド補完に使用
    * ↑を押してコマンド履歴を表示
    * `/`を入力してすべてのスラッシュコマンドを表示
  </Accordion>
</AccordionGroup>

## 次は何ですか？

基本を学習したので、より高度な機能を探索してください：

<CardGroup cols={3}>
  <Card title="一般的なワークフロー" icon="graduation-cap" href="/ja/common-workflows">
    一般的なタスクのステップバイステップガイド
  </Card>

  <Card title="CLIリファレンス" icon="terminal" href="/ja/cli-reference">
    すべてのコマンドとオプションをマスター
  </Card>

  <Card title="設定" icon="gear" href="/ja/settings">
    Claude Codeをワークフローに合わせてカスタマイズ
  </Card>

  <Card title="ウェブ上のClaude Code" icon="cloud" href="/ja/claude-code-on-the-web">
    クラウドでタスクを非同期に実行
  </Card>
</CardGroup>

## ヘルプを取得

* **Claude Code内**：`/help`を入力するか、「how do I...」と質問してください
* **ドキュメント**：ここにいます！他のガイドを参照してください
* **コミュニティ**：[Discord](https://www.anthropic.com/discord)に参加してヒントとサポートを受けてください


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt