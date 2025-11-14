# 一般的なワークフロー

> Claude Codeを使用した一般的なワークフローについて学びます。

このドキュメント内の各タスクには、明確な指示、コマンド例、およびClaudeコードを最大限に活用するためのベストプラクティスが含まれています。

## 新しいコードベースを理解する

### コードベースの概要をすばやく取得する

新しいプロジェクトに参加したばかりで、その構造をすばやく理解する必要があるとします。

<Steps>
  <Step title="プロジェクトルートディレクトリに移動する">
    ```bash  theme={null}
    cd /path/to/project 
    ```
  </Step>

  <Step title="Claude Codeを開始する">
    ```bash  theme={null}
    claude 
    ```
  </Step>

  <Step title="高レベルの概要をリクエストする">
    ```
    > give me an overview of this codebase 
    ```
  </Step>

  <Step title="特定のコンポーネントをさらに詳しく調べる">
    ```
    > explain the main architecture patterns used here 
    ```

    ```
    > what are the key data models?
    ```

    ```
    > how is authentication handled?
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * 広い質問から始めて、特定の領域に絞り込んでいきます
  * プロジェクトで使用されているコーディング規約とパターンについて尋ねます
  * プロジェクト固有の用語の用語集をリクエストします
</Tip>

### 関連するコードを見つける

特定の機能または機能に関連するコードを見つける必要があるとします。

<Steps>
  <Step title="Claudeに関連ファイルを見つけるよう依頼する">
    ```
    > find the files that handle user authentication 
    ```
  </Step>

  <Step title="コンポーネントがどのように相互作用するかについてのコンテキストを取得する">
    ```
    > how do these authentication files work together? 
    ```
  </Step>

  <Step title="実行フローを理解する">
    ```
    > trace the login process from front-end to database 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * 探しているものについて具体的にしてください
  * プロジェクトのドメイン言語を使用します
</Tip>

***

## バグを効率的に修正する

エラーメッセージが表示され、そのソースを見つけて修正する必要があるとします。

<Steps>
  <Step title="エラーをClaudeと共有する">
    ```
    > I'm seeing an error when I run npm test 
    ```
  </Step>

  <Step title="修正の推奨事項をリクエストする">
    ```
    > suggest a few ways to fix the @ts-ignore in user.ts 
    ```
  </Step>

  <Step title="修正を適用する">
    ```
    > update user.ts to add the null check you suggested 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * Claudeに問題を再現するコマンドとスタックトレースを伝えます
  * エラーを再現するための手順を記載します
  * エラーが断続的か一貫しているかをClaudeに知らせます
</Tip>

***

## コードをリファクタリングする

古いコードを更新して、最新のパターンとプラクティスを使用する必要があるとします。

<Steps>
  <Step title="リファクタリング用のレガシーコードを特定する">
    ```
    > find deprecated API usage in our codebase 
    ```
  </Step>

  <Step title="リファクタリングの推奨事項を取得する">
    ```
    > suggest how to refactor utils.js to use modern JavaScript features 
    ```
  </Step>

  <Step title="変更を安全に適用する">
    ```
    > refactor utils.js to use ES2024 features while maintaining the same behavior 
    ```
  </Step>

  <Step title="リファクタリングを検証する">
    ```
    > run tests for the refactored code 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * Claudeに最新のアプローチの利点を説明するよう依頼します
  * 必要に応じて、変更が後方互換性を維持することをリクエストします
  * リファクタリングは小さくテスト可能な増分で実行します
</Tip>

***

## 特化したサブエージェントを使用する

特化したAIサブエージェントを使用して、特定のタスクをより効果的に処理したいとします。

<Steps>
  <Step title="利用可能なサブエージェントを表示する">
    ```
    > /agents
    ```

    これにより、すべての利用可能なサブエージェントが表示され、新しいものを作成できます。
  </Step>

  <Step title="サブエージェントを自動的に使用する">
    Claude Codeは、特化したサブエージェントに適切なタスクを自動的に委譲します：

    ```
    > review my recent code changes for security issues
    ```

    ```
    > run all tests and fix any failures
    ```
  </Step>

  <Step title="特定のサブエージェントを明示的にリクエストする">
    ```
    > use the code-reviewer subagent to check the auth module
    ```

    ```
    > have the debugger subagent investigate why users can't log in
    ```
  </Step>

  <Step title="ワークフロー用のカスタムサブエージェントを作成する">
    ```
    > /agents
    ```

    次に、「新しいサブエージェントを作成」を選択し、プロンプトに従って以下を定義します：

    * サブエージェントタイプ（例：`api-designer`、`performance-optimizer`）
    * 使用する時期
    * アクセスできるツール
    * その特化したシステムプロンプト
  </Step>
</Steps>

<Tip>
  ヒント：

  * チームで共有するために、`.claude/agents/`にプロジェクト固有のサブエージェントを作成します
  * 自動委譲を有効にするために、説明的な`description`フィールドを使用します
  * 各サブエージェントが実際に必要とするツールアクセスのみに制限します
  * 詳細な例については、[サブエージェントドキュメント](/ja/sub-agents)を確認してください
</Tip>

***

## プランモードを使用して安全なコード分析を行う

プランモードは、読み取り専用操作でコードベースを分析することでプランを作成するようClaudeに指示します。これは、コードベースの探索、複雑な変更の計画、またはコードの安全なレビューに最適です。

### プランモードを使用する場合

* **マルチステップ実装**：機能が多くのファイルへの編集を必要とする場合
* **コード探索**：何かを変更する前にコードベースを徹底的に調査したい場合
* **インタラクティブ開発**：Claudeとの方向性について反復したい場合

### プランモードの使用方法

**セッション中にプランモードをオンにする**

**Shift+Tab**を使用してセッション中にプランモードに切り替えることができます。

通常モードの場合、**Shift+Tab**は最初にオートアクセプトモードに切り替わります。これはターミナルの下部に`⏵⏵ accept edits on`で示されます。その後の**Shift+Tab**はプランモードに切り替わります。これは`⏸ plan mode on`で示されます。

**プランモードで新しいセッションを開始する**

プランモードで新しいセッションを開始するには、`--permission-mode plan`フラグを使用します：

```bash  theme={null}
claude --permission-mode plan
```

**プランモードで「ヘッドレス」クエリを実行する**

`-p`を使用してプランモードでクエリを直接実行することもできます（つまり、[「ヘッドレスモード」](/ja/headless)で）：

```bash  theme={null}
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

### 例：複雑なリファクタリングの計画

```bash  theme={null}
claude --permission-mode plan
```

```
> I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Claudeは現在の実装を分析し、包括的なプランを作成します。フォローアップで改善します：

```
> What about backward compatibility?
> How should we handle database migration?
```

### プランモードをデフォルトとして設定する

```json  theme={null}
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

詳細な設定オプションについては、[設定ドキュメント](/ja/settings#available-settings)を参照してください。

***

## テストを使用する

カバーされていないコードのテストを追加する必要があるとします。

<Steps>
  <Step title="テストされていないコードを特定する">
    ```
    > find functions in NotificationsService.swift that are not covered by tests 
    ```
  </Step>

  <Step title="テストスキャフォルディングを生成する">
    ```
    > add tests for the notification service 
    ```
  </Step>

  <Step title="意味のあるテストケースを追加する">
    ```
    > add test cases for edge conditions in the notification service 
    ```
  </Step>

  <Step title="テストを実行して検証する">
    ```
    > run the new tests and fix any failures 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * エッジケースとエラー条件をカバーするテストをリクエストします
  * 必要に応じて、ユニットテストと統合テストの両方をリクエストします
  * Claudeにテスト戦略を説明させます
</Tip>

***

## プルリクエストを作成する

変更に対して、よく文書化されたプルリクエストを作成する必要があるとします。

<Steps>
  <Step title="変更を要約する">
    ```
    > summarize the changes I've made to the authentication module 
    ```
  </Step>

  <Step title="Claudeを使用してPRを生成する">
    ```
    > create a pr 
    ```
  </Step>

  <Step title="レビューと改善">
    ```
    > enhance the PR description with more context about the security improvements 
    ```
  </Step>

  <Step title="テストの詳細を追加する">
    ```
    > add information about how these changes were tested 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * Claudeに直接PRを作成するよう依頼します
  * 送信する前にClaudeが生成したPRをレビューします
  * Claudeに潜在的なリスクまたは考慮事項を強調するよう依頼します
</Tip>

## ドキュメントを処理する

コードのドキュメントを追加または更新する必要があるとします。

<Steps>
  <Step title="文書化されていないコードを特定する">
    ```
    > find functions without proper JSDoc comments in the auth module 
    ```
  </Step>

  <Step title="ドキュメントを生成する">
    ```
    > add JSDoc comments to the undocumented functions in auth.js 
    ```
  </Step>

  <Step title="レビューと改善">
    ```
    > improve the generated documentation with more context and examples 
    ```
  </Step>

  <Step title="ドキュメントを検証する">
    ```
    > check if the documentation follows our project standards 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * 必要なドキュメントスタイルを指定します（JSDoc、docstringsなど）
  * ドキュメント内の例をリクエストします
  * パブリックAPI、インターフェース、および複雑なロジックのドキュメントをリクエストします
</Tip>

***

## 画像を使用する

コードベース内の画像を使用する必要があり、Claudeが画像コンテンツの分析を支援することを望むとします。

<Steps>
  <Step title="会話に画像を追加する">
    次のいずれかの方法を使用できます：

    1. Claude Codeウィンドウに画像をドラッグアンドドロップします
    2. 画像をコピーしてCLIにctrl+vで貼り付けます（cmd+vは使用しないでください）
    3. 画像パスをClaudeに提供します。例：「この画像を分析してください：/path/to/your/image.png」
  </Step>

  <Step title="Claudeに画像を分析するよう依頼する">
    ```
    > What does this image show?
    ```

    ```
    > Describe the UI elements in this screenshot
    ```

    ```
    > Are there any problematic elements in this diagram?
    ```
  </Step>

  <Step title="コンテキストに画像を使用する">
    ```
    > Here's a screenshot of the error. What's causing it?
    ```

    ```
    > This is our current database schema. How should we modify it for the new feature?
    ```
  </Step>

  <Step title="ビジュアルコンテンツからコード提案を取得する">
    ```
    > Generate CSS to match this design mockup
    ```

    ```
    > What HTML structure would recreate this component?
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * テキストの説明が不明確または面倒な場合は、画像を使用します
  * より良いコンテキストのために、エラー、UIデザイン、または図のスクリーンショットを含めます
  * 会話で複数の画像を使用できます
  * 画像分析は、図、スクリーンショット、モックアップなどで機能します
</Tip>

***

## ファイルとディレクトリを参照する

@を使用して、Claudeが読み込むのを待たずにファイルまたはディレクトリをすばやく含めます。

<Steps>
  <Step title="単一ファイルを参照する">
    ```
    > Explain the logic in @src/utils/auth.js
    ```

    これにより、ファイルの完全な内容が会話に含まれます。
  </Step>

  <Step title="ディレクトリを参照する">
    ```
    > What's the structure of @src/components?
    ```

    これにより、ファイル情報を含むディレクトリリストが提供されます。
  </Step>

  <Step title="MCPリソースを参照する">
    ```
    > Show me the data from @github:repos/owner/repo/issues
    ```

    これにより、@server:resourceの形式を使用して接続されたMCPサーバーからデータを取得します。詳細については、[MCPリソース](/ja/mcp#use-mcp-resources)を参照してください。
  </Step>
</Steps>

<Tip>
  ヒント：

  * ファイルパスは相対パスまたは絶対パスです
  * @ファイル参照は、ファイルのディレクトリと親ディレクトリにCLAUDE.mdを追加します
  * ディレクトリ参照はファイルリストを表示し、内容は表示しません
  * 単一のメッセージで複数のファイルを参照できます（例：「@file1.jsと@file2.js」）
</Tip>

***

## 拡張思考を使用する

複雑なアーキテクチャの決定、難しいバグ、または深い推論が必要なマルチステップ実装の計画に取り組んでいるとします。

<Note>
  [拡張思考](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)はClaudeコードではデフォルトで無効になっています。`Tab`を使用して思考をオンに切り替えるか、「think」または「think hard」などのプロンプトを使用してオンデマンドで有効にできます。また、設定で[`MAX_THINKING_TOKENS`環境変数](/ja/settings#environment-variables)を設定することで、永続的に有効にすることもできます。
</Note>

<Steps>
  <Step title="コンテキストを提供し、Claudeに考えるよう依頼する">
    ```
    > I need to implement a new authentication system using OAuth2 for our API. Think deeply about the best approach for implementing this in our codebase.
    ```

    Claudeはコードベースから関連情報を収集し、
    拡張思考を使用します。これはインターフェースに表示されます。
  </Step>

  <Step title="フォローアップのプロンプトで思考を改善する">
    ```
    > think about potential security vulnerabilities in this approach 
    ```

    ```
    > think hard about edge cases we should handle 
    ```
  </Step>
</Steps>

<Tip>
  拡張思考から最大の価値を得るためのヒント：

  [拡張思考](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)は、以下のような複雑なタスクに最も価値があります：

  * 複雑なアーキテクチャの変更を計画する
  * 複雑な問題をデバッグする
  * 新機能の実装計画を作成する
  * 複雑なコードベースを理解する
  * 異なるアプローチ間のトレードオフを評価する

  セッション中に`Tab`を使用して思考をオンとオフに切り替えます。

  思考をリクエストする方法は、思考の深さのレベルが異なります：

  * 「think」は基本的な拡張思考をトリガーします
  * 「keep hard」、「think more」、「think a lot」、「think longer」などの強化フレーズは、より深い思考をトリガーします

  拡張思考プロンプトのヒントについては、[拡張思考のヒント](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)を参照してください。
</Tip>

<Note>
  Claudeは、その思考プロセスをレスポンスの上にイタリック体の灰色のテキストとして表示します。
</Note>

***

## 前の会話を再開する

Claude Codeでタスクに取り組んでいて、後のセッションで中断したところから続ける必要があるとします。

Claude Codeは、前の会話を再開するための2つのオプションを提供します：

* `--continue`で最新の会話を自動的に続ける
* `--resume`で会話ピッカーを表示する

<Steps>
  <Step title="最新の会話を続ける">
    ```bash  theme={null}
    claude --continue
    ```

    これにより、プロンプトなしで最新の会話がすぐに再開されます。
  </Step>

  <Step title="非対話モードで続ける">
    ```bash  theme={null}
    claude --continue --print "Continue with my task"
    ```

    `--continue`で`--print`を使用して、最新の会話を非対話モードで再開します。これはスクリプトまたは自動化に最適です。
  </Step>

  <Step title="会話ピッカーを表示する">
    ```bash  theme={null}
    claude --resume
    ```

    これにより、以下を表示するクリーンなリストビューを含むインタラクティブな会話セレクターが表示されます：

    * セッション要約（または初期プロンプト）
    * メタデータ：経過時間、メッセージ数、およびgitブランチ

    矢印キーを使用してナビゲートし、Enterキーを押して会話を選択します。Escキーを押して終了します。
  </Step>
</Steps>

<Tip>
  ヒント：

  * 会話履歴はマシンにローカルに保存されます
  * 最新の会話にすばやくアクセスするには`--continue`を使用します
  * 特定の過去の会話を選択する必要がある場合は`--resume`を使用します
  * 再開すると、続行する前に会話履歴全体が表示されます
  * 再開された会話は、元の会話と同じモデルと設定で開始されます

  動作方法：

  1. **会話ストレージ**：すべての会話は、完全なメッセージ履歴を含めてローカルに自動保存されます
  2. **メッセージ逆シリアル化**：再開時に、コンテキストを維持するために会話履歴全体が復元されます
  3. **ツール状態**：前の会話からのツール使用と結果が保持されます
  4. **コンテキスト復元**：会話は、以前のコンテキストがすべて保持された状態で再開されます

  例：

  ```bash  theme={null}
  # 最新の会話を続ける
  claude --continue

  # 特定のプロンプトで最新の会話を続ける
  claude --continue --print "Show me our progress"

  # 会話ピッカーを表示する
  claude --resume

  # 非対話モードで最新の会話を続ける
  claude --continue --print "Run the tests again"
  ```
</Tip>

***

## Gitワークツリーを使用して並列Claude Codeセッションを実行する

複数のタスクに同時に取り組む必要があり、Claude Codeインスタンス間で完全なコード分離が必要なとします。

<Steps>
  <Step title="Gitワークツリーを理解する">
    Gitワークツリーを使用すると、同じリポジトリから複数のブランチを別々のディレクトリにチェックアウトできます。各ワークツリーは、Git履歴を共有しながら、独自の作業ディレクトリを持ちます。詳細については、[公式Gitワークツリー
    ドキュメント](https://git-scm.com/docs/git-worktree)を参照してください。
  </Step>

  <Step title="新しいワークツリーを作成する">
    ```bash  theme={null}
    # 新しいブランチで新しいワークツリーを作成する
    git worktree add ../project-feature-a -b feature-a

    # または既存のブランチでワークツリーを作成する
    git worktree add ../project-bugfix bugfix-123
    ```

    これにより、リポジトリの個別の作業コピーを含む新しいディレクトリが作成されます。
  </Step>

  <Step title="各ワークツリーでClaudeコードを実行する">
    ```bash  theme={null}
    # ワークツリーに移動する
    cd ../project-feature-a

    # この分離された環境でClaudeコードを実行する
    claude
    ```
  </Step>

  <Step title="別のワークツリーでClaudeを実行する">
    ```bash  theme={null}
    cd ../project-bugfix
    claude
    ```
  </Step>

  <Step title="ワークツリーを管理する">
    ```bash  theme={null}
    # すべてのワークツリーをリストする
    git worktree list

    # 完了したワークツリーを削除する
    git worktree remove ../project-feature-a
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * 各ワークツリーは独立したファイル状態を持ち、並列Claude Codeセッションに最適です
  * 1つのワークツリーで行われた変更は他に影響を与えず、Claudeインスタンスが相互に干渉するのを防ぎます
  * すべてのワークツリーは同じGit履歴とリモート接続を共有します
  * 長時間実行されるタスクの場合、1つのワークツリーでClaudeが作業している間に、別のワークツリーで開発を続けることができます
  * 各ワークツリーが何のタスク用かを簡単に識別するために、説明的なディレクトリ名を使用します
  * 各新しいワークツリーでプロジェクトの設定に従って開発環境を初期化することを忘れないでください。スタックによっては、以下が含まれる場合があります：
    * JavaScriptプロジェクト：依存関係のインストール（`npm install`、`yarn`）を実行する
    * Pythonプロジェクト：仮想環境を設定するか、パッケージマネージャーでインストールする
    * その他の言語：プロジェクトの標準的なセットアッププロセスに従う
</Tip>

***

## Claudeをunixスタイルのユーティリティとして使用する

### 検証プロセスにClaudeを追加する

Claude Codeをリンターまたはコードレビュアーとして使用したいとします。

**ビルドスクリプトにClaudeを追加する：**

```json  theme={null}
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}
```

<Tip>
  ヒント：

  * CI/CDパイプラインで自動コードレビューにClaudeを使用します
  * プロンプトをカスタマイズして、プロジェクトに関連する特定の問題をチェックします
  * 異なるタイプの検証用に複数のスクリプトを作成することを検討してください
</Tip>

### パイプイン、パイプアウト

Claudeにデータをパイプインし、構造化された形式でデータを取得したいとします。

**Claudeを通じてデータをパイプする：**

```bash  theme={null}
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

<Tip>
  ヒント：

  * パイプを使用してClaudeを既存のシェルスクリプトに統合します
  * 他のUnixツールと組み合わせて、強力なワークフローを実現します
  * 構造化された出力に`--output-format`を使用することを検討してください
</Tip>

### 出力形式を制御する

特にClaudeコードをスクリプトまたは他のツールに統合する場合、Claudeの出力が特定の形式である必要があるとします。

<Steps>
  <Step title="テキスト形式を使用する（デフォルト）">
    ```bash  theme={null}
    cat data.txt | claude -p 'summarize this data' --output-format text > summary.txt
    ```

    これにより、Claudeのプレーンテキストレスポンスのみが出力されます（デフォルトの動作）。
  </Step>

  <Step title="JSON形式を使用する">
    ```bash  theme={null}
    cat code.py | claude -p 'analyze this code for bugs' --output-format json > analysis.json
    ```

    これにより、コストと期間を含むメタデータを含むメッセージのJSON配列が出力されます。
  </Step>

  <Step title="ストリーミングJSON形式を使用する">
    ```bash  theme={null}
    cat log.txt | claude -p 'parse this log file for errors' --output-format stream-json
    ```

    これにより、Claudeがリクエストを処理するときにリアルタイムでJSONオブジェクトのシリーズが出力されます。各メッセージは有効なJSONオブジェクトですが、連結された場合、全体の出力は有効なJSONではありません。
  </Step>
</Steps>

<Tip>
  ヒント：

  * Claudeのレスポンスだけが必要な単純な統合には`--output-format text`を使用します
  * 完全な会話ログが必要な場合は`--output-format json`を使用します
  * 各会話ターンのリアルタイム出力には`--output-format stream-json`を使用します
</Tip>

***

## カスタムスラッシュコマンドを作成する

Claude Codeは、特定のプロンプトまたはタスクをすばやく実行するために作成できるカスタムスラッシュコマンドをサポートしています。

詳細については、[スラッシュコマンド](/ja/slash-commands)リファレンスページを参照してください。

### プロジェクト固有のコマンドを作成する

すべてのチームメンバーが使用できるプロジェクト用の再利用可能なスラッシュコマンドを作成したいとします。

<Steps>
  <Step title="プロジェクトにコマンドディレクトリを作成する">
    ```bash  theme={null}
    mkdir -p .claude/commands
    ```
  </Step>

  <Step title="各コマンド用にMarkdownファイルを作成する">
    ```bash  theme={null}
    echo "Analyze the performance of this code and suggest three specific optimizations:" > .claude/commands/optimize.md 
    ```
  </Step>

  <Step title="Claude Codeでカスタムコマンドを使用する">
    ```
    > /optimize 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * コマンド名はファイル名から派生します（例：`optimize.md`は`/optimize`になります）
  * コマンドをサブディレクトリに整理できます（例：`.claude/commands/frontend/component.md`は説明に「(project:frontend)」が表示される`/component`を作成します）
  * プロジェクトコマンドは、リポジトリをクローンするすべてのユーザーが利用できます
  * Markdownファイルの内容は、コマンドが呼び出されたときにClaudeに送信されるプロンプトになります
</Tip>

### \$ARGUMENTSでコマンド引数を追加する

ユーザーからの追加入力を受け入れることができる柔軟なスラッシュコマンドを作成したいとします。

<Steps>
  <Step title="$ARGUMENTSプレースホルダーを含むコマンドファイルを作成する">
    ```bash  theme={null}
    echo 'Find and fix issue #$ARGUMENTS. Follow these steps: 1.
    Understand the issue described in the ticket 2. Locate the relevant code in
    our codebase 3. Implement a solution that addresses the root cause 4. Add
    appropriate tests 5. Prepare a concise PR description' >
    .claude/commands/fix-issue.md 
    ```
  </Step>

  <Step title="問題番号を指定してコマンドを使用する">
    Claude Codeセッションでコマンドを引数と共に使用します。

    ```
    > /fix-issue 123 
    ```

    これにより、プロンプト内の\$ARGUMENTSが「123」に置き換えられます。
  </Step>
</Steps>

<Tip>
  ヒント：

  * \$ARGUMENTSプレースホルダーは、コマンドに続くテキストに置き換えられます
  * \$ARGUMENTSをコマンドテンプレート内の任意の場所に配置できます
  * その他の有用なアプリケーション：特定の関数のテストケースの生成、コンポーネントのドキュメント作成、特定のファイルのコードレビュー、または指定された言語へのコンテンツの翻訳
</Tip>

### 個人用スラッシュコマンドを作成する

すべてのプロジェクトで機能する個人用スラッシュコマンドを作成したいとします。

<Steps>
  <Step title="ホームフォルダにコマンドディレクトリを作成する">
    ```bash  theme={null}
    mkdir -p ~/.claude/commands 
    ```
  </Step>

  <Step title="各コマンド用にMarkdownファイルを作成する">
    ```bash  theme={null}
    echo "Review this code for security vulnerabilities, focusing on:" >
    ~/.claude/commands/security-review.md 
    ```
  </Step>

  <Step title="個人用カスタムコマンドを使用する">
    ```
    > /security-review 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * 個人用コマンドは、`/help`でリストされるときに説明に「(user)」が表示されます
  * 個人用コマンドはあなただけが利用でき、チームと共有されません
  * 個人用コマンドはすべてのプロジェクトで機能します
  * これらを使用して、異なるコードベース全体で一貫したワークフローを実現できます
</Tip>

***

## Claudeの機能について尋ねる

Claudeは、ドキュメントへの組み込みアクセスを持ち、独自の機能と制限について質問に答えることができます。

### 質問例

```
> can Claude Code create pull requests?
```

```
> how does Claude Code handle permissions?
```

```
> what slash commands are available?
```

```
> how do I use MCP with Claude Code?
```

```
> how do I configure Claude Code for Amazon Bedrock?
```

```
> what are the limitations of Claude Code?
```

<Note>
  Claudeは、これらの質問に対してドキュメントベースの回答を提供します。実行可能な例とハンズオンデモンストレーションについては、上記の特定のワークフローセクションを参照してください。
</Note>

<Tip>
  ヒント：

  * Claudeは、使用しているバージョンに関係なく、常に最新のClaudeコードドキュメントにアクセスできます
  * 詳細な回答を得るために、具体的な質問をします
  * Claudeは、MCP統合、エンタープライズ構成、高度なワークフローなどの複雑な機能を説明できます
</Tip>

***

## 次のステップ

<Card title="Claude Codeリファレンス実装" icon="code" href="https://github.com/anthropics/claude-code/tree/main/.devcontainer">
  開発コンテナリファレンス実装をクローンします。
</Card>
