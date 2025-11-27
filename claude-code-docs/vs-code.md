# Visual Studio Code

> ネイティブ拡張機能またはCLI統合を通じてVisual Studio CodeでClaude Codeを使用します

<img src="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=300652d5678c63905e6b0ea9e50835f8" alt="Claude Code VS Code拡張機能インターフェース" data-og-width="2500" width="2500" data-og-height="1155" height="1155" data-path="images/vs-code-extension-interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=280&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=87630c671517a3d52e9aee627041696e 280w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=560&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=716b093879204beec8d952649ef75292 560w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=840&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=c1525d1a01513acd9d83d8b5a8fe2fc8 840w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=1100&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=1d90021d58bbb51f871efec13af955c3 1100w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=1650&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=7babdd25440099886f193cfa99af88ae 1650w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/vs-code-extension-interface.jpg?w=2500&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=08c92eedfb56fe61a61e480fb63784b6 2500w" />

## VS Code拡張機能（ベータ版）

ベータ版で利用可能なVS Code拡張機能により、IDEに直接統合されたネイティブグラフィカルインターフェースを通じて、Claudeの変更をリアルタイムで確認できます。VS Code拡張機能により、ターミナルよりもビジュアルインターフェースを好むユーザーがClaude Codeにアクセスして操作しやすくなります。

### 機能

VS Code拡張機能は以下を提供します：

* **ネイティブIDE体験**: Sparkアイコンでアクセスできる専用Claude Codeサイドバーパネル
* **編集機能付きプランモード**: Claudeのプランを受け入れる前に確認および編集
* **自動受け入れ編集モード**: Claudeの変更が行われると自動的に適用
* **ファイル管理**: @メンション機能でファイルを参照するか、システムファイルピッカーを使用してファイルと画像を添付
* **MCPサーバー使用**: CLIを通じて設定されたModel Context Protocolサーバーを使用
* **会話履歴**: 過去の会話への簡単なアクセス
* **複数セッション**: 複数のClaude Codeセッションを同時に実行
* **キーボードショートカット**: CLIのほとんどのショートカットをサポート
* **スラッシュコマンド**: 拡張機能内でほとんどのCLIスラッシュコマンドに直接アクセス

### 要件

* VS Code 1.98.0以上

### インストール

[Visual Studio Code拡張機能マーケットプレイス](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)から拡張機能をダウンロードしてインストールします。

### 動作方法

インストール後、VS Codeインターフェースを通じてClaude Codeの使用を開始できます：

1. エディターのサイドバーのSparkアイコンをクリックしてClaude Codeパネルを開く
2. ターミナルで行うのと同じ方法でClaude Codeにプロンプトを入力
3. Claudeがコードを分析し、変更を提案するのを監視
4. インターフェース内で直接編集を確認して受け入れ
   * **ヒント**: サイドバーをドラッグして広げてインラインdiffを表示し、クリックして展開して詳細を確認

### サードパーティプロバイダーの使用（VertexおよびBedrock）

VS Code拡張機能は、Amazon BedrockやGoogle Vertex AIなどのサードパーティプロバイダーでClaude Codeを使用することをサポートしています。これらのプロバイダーで設定されている場合、拡張機能はログインを求めません。サードパーティプロバイダーを使用するには、VS Code拡張機能設定で環境変数を設定します：

1. VS Code設定を開く
2. 「Claude Code: Environment Variables」を検索
3. 必要な環境変数を追加

#### 環境変数

| 変数                            | 説明                     | 必須              | 例                                                |
| :---------------------------- | :--------------------- | :-------------- | :----------------------------------------------- |
| `CLAUDE_CODE_USE_BEDROCK`     | Amazon Bedrock統合を有効化   | Bedrockの場合は必須   | `"1"` または `"true"`                               |
| `CLAUDE_CODE_USE_VERTEX`      | Google Vertex AI統合を有効化 | Vertex AIの場合は必須 | `"1"` または `"true"`                               |
| `ANTHROPIC_API_KEY`           | サードパーティアクセス用APIキー      | 必須              | `"your-api-key"`                                 |
| `AWS_REGION`                  | Bedrock用AWSリージョン       |                 | `"us-east-2"`                                    |
| `AWS_PROFILE`                 | Bedrock認証用AWSプロファイル    |                 | `"your-profile"`                                 |
| `CLOUD_ML_REGION`             | Vertex AI用リージョン        |                 | `"global"` または `"us-east5"`                      |
| `ANTHROPIC_VERTEX_PROJECT_ID` | Vertex AI用GCPプロジェクトID  |                 | `"your-project-id"`                              |
| `ANTHROPIC_MODEL`             | プライマリモデルをオーバーライド       | モデルIDをオーバーライド   | `"us.anthropic.claude-sonnet-4-5-20250929-v1:0"` |
| `ANTHROPIC_SMALL_FAST_MODEL`  | 小型/高速モデルをオーバーライド       | オプション           | `"us.anthropic.claude-3-5-haiku-20241022-v1:0"`  |
| `CLAUDE_CODE_SKIP_AUTH_LOGIN` | すべてのログインプロンプトを無効化      | オプション           | `"1"` または `"true"`                               |

詳細なセットアップ手順と追加の設定オプションについては、以下を参照してください：

* [Amazon Bedrock上のClaude Code](/ja/amazon-bedrock)
* [Google Vertex AI上のClaude Code](/ja/google-vertex-ai)

### まだ実装されていない機能

VS Code拡張機能では以下の機能はまだ利用できません：

* **完全なMCPサーバー設定**: [MCPサーバーをCLIを通じて設定](/ja/mcp)する必要があり、その後拡張機能がそれらを使用します
* **サブエージェント設定**: [CLIを通じてサブエージェントを設定](/ja/sub-agents)してVS Codeで使用
* **チェックポイント**: 特定のポイントで会話状態を保存および復元
* **高度なショートカット**:
  * `#` ショートカットでメモリに追加
  * `!` ショートカットでbashコマンドを直接実行
* **タブ補完**: タブキーでファイルパス補完

これらの機能は今後のアップデートで追加予定です。

## セキュリティに関する考慮事項

Claude CodeがVS Codeで自動編集権限を有効にして実行される場合、IDEによって自動的に実行される可能性があるIDE設定ファイルを変更できる可能性があります。これにより、自動編集モードでClaude Codeを実行するリスクが増加し、bash実行のためのClaude Codeの権限プロンプトをバイパスできる可能性があります。

VS Codeで実行する場合は、以下を検討してください：

* 信頼されていないワークスペースに対して[VS Code制限モード](https://code.visualstudio.com/docs/editor/workspace-trust#_restricted-mode)を有効化
* 編集の手動承認モードを使用
* Claudeが信頼されたプロンプトでのみ使用されることを確認するために特に注意を払う

## レガシーCLI統合

リリースした最初のVS Code統合により、ターミナルで実行されているClaude CodeがIDEと相互作用できます。これは選択コンテキスト共有（現在の選択/タブが自動的にClaude Codeと共有される）、ターミナルの代わりにIDEでのdiff表示、ファイル参照ショートカット（MacではCmd+Option+K、Windows/LinuxではAlt+Ctrl+Kを使用して@File#L1-99のようなファイル参照を挿入）、および自動診断共有（lintおよび構文エラー）を提供します。

レガシー統合は、VS Codeの統合ターミナルから`claude`を実行すると自動インストールされます。ターミナルから`claude`を実行するだけで、すべての機能がアクティブになります。外部ターミナルの場合は、`/ide`コマンドを使用してClaude CodeをVS Codeインスタンスに接続します。設定するには、`claude`を実行し、`/config`を入力し、diffツールを`auto`に設定して自動IDE検出を行います。

拡張機能とCLI統合の両方がVisual Studio Code、Cursor、Windsurf、およびVSCodiumで機能します。

## トラブルシューティング

### 拡張機能がインストールされない

* VS Codeの互換バージョン（1.85.0以上）があることを確認
* VS Codeが拡張機能をインストールする権限があることを確認
* マーケットプレイスウェブサイトから直接インストールしてみる

### レガシー統合が機能しない

* VS Codeの統合ターミナルからClaude Codeを実行していることを確認
* IDE変種用のCLIがインストールされていることを確認：
  * VS Code: `code` コマンドが利用可能である必要があります
  * Cursor: `cursor` コマンドが利用可能である必要があります
  * Windsurf: `windsurf` コマンドが利用可能である必要があります
  * VSCodium: `codium` コマンドが利用可能である必要があります
* コマンドがインストールされていない場合：
  1. `Cmd+Shift+P`（Mac）または`Ctrl+Shift+P`（Windows/Linux）でコマンドパレットを開く
  2. 「Shell Command: Install 'code' command in PATH」（またはIDE用の同等のコマンド）を検索

追加のヘルプについては、[トラブルシューティングガイド](/ja/troubleshooting)を参照してください。


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt