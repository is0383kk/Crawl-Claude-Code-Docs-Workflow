# アイデンティティとアクセス管理

> Claude Codeの組織内でのユーザー認証、認可、アクセス制御を設定する方法を学びます。

## 認証方法

Claude Codeのセットアップには、Anthropicモデルへのアクセスが必要です。チームの場合、Claude Codeアクセスを次の3つの方法のいずれかで設定できます：

* Claude API（Claude Consoleを経由）
* Amazon Bedrock
* Google Vertex AI

### Claude API認証

**Claude APIを経由してチーム向けにClaude Codeアクセスを設定するには：**

1. 既存のClaude Consoleアカウントを使用するか、新しいClaude Consoleアカウントを作成します
2. 以下のいずれかの方法でユーザーを追加できます：
   * Console内からユーザーを一括招待します（Console -> Settings -> Members -> Invite）
   * [SSOを設定する](https://support.claude.com/en/articles/10280258-setting-up-single-sign-on-on-the-api-console)
3. ユーザーを招待する際、ユーザーは以下のいずれかのロールが必要です：
   * 「Claude Code」ロールはユーザーがClaude Code APIキーのみを作成できることを意味します
   * 「Developer」ロールはユーザーがあらゆる種類のAPIキーを作成できることを意味します
4. 招待されたユーザーは以下の手順を完了する必要があります：
   * Console招待を受け入れます
   * [システム要件を確認する](/ja/setup#system-requirements)
   * [Claude Codeをインストールする](/ja/setup#installation)
   * Consoleアカウント認証情報でログインします

### クラウドプロバイダー認証

**BedrockまたはVertexを経由してチーム向けにClaude Codeアクセスを設定するには：**

1. [Bedrockドキュメント](/ja/amazon-bedrock)または[Vertexドキュメント](/ja/google-vertex-ai)に従います
2. 環境変数とクラウド認証情報を生成するための指示をユーザーに配布します。[ここで設定を管理する方法について詳しく読む](/ja/settings)。
3. ユーザーは[Claude Codeをインストール](/ja/setup#installation)できます

## アクセス制御と権限

エージェントが実行できることを正確に指定できるきめ細かい権限をサポートしています（例：テストの実行、linterの実行）。また、実行できないことも指定できます（例：クラウドインフラストラクチャの更新）。これらの権限設定はバージョン管理にチェックインでき、組織内のすべての開発者に配布できるほか、個々の開発者がカスタマイズできます。

### 権限システム

Claude Codeは、パワーとセーフティのバランスを取るために、段階的な権限システムを使用しています：

| ツールタイプ   | 例                | 承認が必要 | 「はい、今後は聞かない」の動作         |
| :------- | :--------------- | :---- | :---------------------- |
| 読み取り専用   | ファイル読み取り、LS、Grep | いいえ   | N/A                     |
| Bashコマンド | シェル実行            | はい    | プロジェクトディレクトリとコマンドごとに永続的 |
| ファイル変更   | ファイルの編集/書き込み     | はい    | セッション終了まで               |

### 権限の設定

`/permissions`を使用してClaude Codeのツール権限を表示および管理できます。このUIはすべての権限ルールと、それらが取得されるsettings.jsonファイルをリストします。

* **Allow**ルールは、Claude Codeが指定されたツールをさらなる手動承認なしで使用できるようにします。
* **Ask**ルールは、Claude Codeが指定されたツールを使用しようとするたびにユーザーに確認を求めます。Askルールはallowルールより優先されます。
* **Deny**ルールは、Claude Codeが指定されたツールを使用することを防止します。Denyルールはallowルールとaskルールより優先されます。
* **追加ディレクトリ**は、Claude のファイルアクセスを初期作業ディレクトリを超えたディレクトリに拡張します。
* **デフォルトモード**は、新しいリクエストに遭遇したときのClaudeの権限動作を制御します。

権限ルールは以下の形式を使用します：`Tool`または`Tool(optional-specifier)`

ツール名だけのルールは、そのツールの任意の使用に一致します。たとえば、allowルールのリストに`Bash`を追加すると、Claude Codeはユーザー承認を必要とせずにBashツールを使用できるようになります。

#### 権限モード

Claude Codeは、[設定ファイル](/ja/settings#settings-files)で`defaultMode`として設定できるいくつかの権限モードをサポートしています：

| モード                 | 説明                                                 |
| :------------------ | :------------------------------------------------- |
| `default`           | 標準動作 - 各ツールの最初の使用時に権限を求めます                         |
| `acceptEdits`       | セッション中のファイル編集権限を自動的に受け入れます                         |
| `plan`              | プランモード - Claudeはファイルを分析できますが、ファイルの変更やコマンドの実行はできません |
| `bypassPermissions` | すべての権限プロンプトをスキップします（安全な環境が必要 - 下記の警告を参照）           |

#### 作業ディレクトリ

デフォルトでは、Claudeは起動されたディレクトリ内のファイルにアクセスできます。このアクセスを拡張できます：

* **起動時**：`--add-dir <path>` CLIオプションを使用します
* **セッション中**：`/add-dir`スラッシュコマンドを使用します
* **永続的な設定**：[設定ファイル](/ja/settings#settings-files)の`additionalDirectories`に追加します

追加ディレクトリ内のファイルは、元の作業ディレクトリと同じ権限ルールに従います。プロンプトなしで読み取り可能になり、ファイル編集権限は現在の権限モードに従います。

#### ツール固有の権限ルール

一部のツールはより細かい権限制御をサポートしています：

**Bash**

* `Bash(npm run build)` 正確なBashコマンド`npm run build`に一致します
* `Bash(npm run test:*)` `npm run test`で始まるBashコマンドに一致します
* `Bash(curl http://site.com/:*)` `curl http://site.com/`で正確に始まるcurlコマンドに一致します

<Tip>
  Claude Codeはシェルオペレータ（`&&`など）を認識しているため、`Bash(safe-cmd:*)`のようなプレフィックスマッチルールは、`safe-cmd && other-cmd`コマンドを実行する権限を与えません
</Tip>

<Warning>
  Bash権限パターンの重要な制限事項：

  1. このツールは**プレフィックスマッチ**を使用し、正規表現またはglobパターンではありません
  2. ワイルカード`:*`はパターンの末尾でのみ機能し、任意の継続にマッチします
  3. `Bash(curl http://github.com/:*)`のようなパターンは多くの方法でバイパスできます：
     * URLの前のオプション：`curl -X GET http://github.com/...`はマッチしません
     * 異なるプロトコル：`curl https://github.com/...`はマッチしません
     * リダイレクト：`curl -L http://bit.ly/xyz`（githubにリダイレクト）
     * 変数：`URL=http://github.com && curl $URL`はマッチしません
     * 余分なスペース：`curl  http://github.com`はマッチしません

  より信頼性の高いURLフィルタリングについては、以下を検討してください：

  * `WebFetch(domain:github.com)`権限でWebFetchツールを使用する
  * CLAUDE.mdを経由してClaude Codeに許可されたcurlパターンについて指示する
  * カスタム権限検証のためのフックを使用する
</Warning>

**Read & Edit**

`Edit`ルールはファイルを編集するすべての組み込みツールに適用されます。Claudeは、Grep、Glob、LSなどのファイルを読み取るすべての組み込みツールに`Read`ルールを適用するためにベストエフォートを試みます。

Read & Editルールは両方とも[gitignore](https://git-scm.com/docs/gitignore)仕様に従い、4つの異なるパターンタイプがあります：

| パターン              | 意味                     | 例                                | マッチ                                |
| ----------------- | ---------------------- | -------------------------------- | ---------------------------------- |
| `//path`          | ファイルシステムルートからの**絶対**パス | `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**`          |
| `~/path`          | **ホーム**ディレクトリからのパス     | `Read(~/Documents/*.pdf)`        | `/Users/alice/Documents/*.pdf`     |
| `/path`           | **設定ファイルに相対的な**パス      | `Edit(/src/**/*.ts)`             | `<settings file path>/src/**/*.ts` |
| `path`または`./path` | **現在のディレクトリに相対的な**パス   | `Read(*.env)`                    | `<cwd>/*.env`                      |

<Warning>
  `/Users/alice/file`のようなパターンは絶対パスではなく、設定ファイルに相対的です。絶対パスには`//Users/alice/file`を使用してください。
</Warning>

* `Edit(/docs/**)` - `<project>/docs/`での編集（`/docs/`ではありません！）
* `Read(~/.zshrc)` - ホームディレクトリの`.zshrc`を読み取ります
* `Edit(//tmp/scratch.txt)` - 絶対パス`/tmp/scratch.txt`を編集します
* `Read(src/**)` - `<current-directory>/src/`から読み取ります

**WebFetch**

* `WebFetch(domain:example.com)` example.comへのフェッチリクエストにマッチします

**MCP**

* `mcp__puppeteer` `puppeteer`サーバーが提供するあらゆるツールにマッチします（Claude Codeで設定された名前）
* `mcp__puppeteer__puppeteer_navigate` `puppeteer`サーバーが提供する`puppeteer_navigate`ツールにマッチします

<Warning>
  他の権限タイプとは異なり、MCP権限はワイルカード（`*`）をサポートしていません。

  MCPサーバーからすべてのツールを承認するには：

  * ✅ 使用：`mcp__github`（すべてのGitHubツールを承認）
  * ❌ 使用しないでください：`mcp__github__*`（ワイルカードはサポートされていません）

  特定のツールのみを承認するには、各ツールをリストします：

  * ✅ 使用：`mcp__github__get_issue`
  * ✅ 使用：`mcp__github__list_issues`
</Warning>

### フックを使用した追加の権限制御

[Claude Codeフック](/ja/hooks-guide)は、実行時に権限評価を実行するカスタムシェルコマンドを登録する方法を提供します。Claude Codeがツール呼び出しを行うと、PreToolUseフックは権限システムが実行される前に実行され、フック出力は権限システムの代わりにツール呼び出しを承認または拒否するかどうかを決定できます。

### エンタープライズ管理ポリシー設定

Claude Codeのエンタープライズデプロイメントの場合、ユーザーおよびプロジェクト設定より優先されるエンタープライズ管理ポリシー設定をサポートしています。これにより、システム管理者はユーザーがオーバーライドできないセキュリティポリシーを実施できます。

システム管理者は以下にポリシーをデプロイできます：

* macOS：`/Library/Application Support/ClaudeCode/managed-settings.json`
* LinuxおよびWSL：`/etc/claude-code/managed-settings.json`
* Windows：`C:\ProgramData\ClaudeCode\managed-settings.json`

これらのポリシーファイルは通常の[設定ファイル](/ja/settings#settings-files)と同じ形式に従いますが、ユーザーまたはプロジェクト設定によってオーバーライドできません。これにより、組織全体で一貫したセキュリティポリシーが確保されます。

### 設定の優先順位

複数の設定ソースが存在する場合、以下の順序（優先度が高い順から低い順）で適用されます：

1. エンタープライズポリシー
2. コマンドラインオプション
3. ローカルプロジェクト設定（`.claude/settings.local.json`）
4. 共有プロジェクト設定（`.claude/settings.json`）
5. ユーザー設定（`~/.claude/settings.json`）

この階層により、組織のポリシーが常に実施されながら、プロジェクトおよびユーザーレベルで適切な柔軟性が許可されます。

## 認証情報管理

Claude Codeは認証認証情報を安全に管理します：

* **保存場所**：macOSでは、APIキー、OAuthトークン、およびその他の認証情報は暗号化されたmacOS Keychainに保存されます。
* **サポートされている認証タイプ**：Claude.ai認証情報、Claude API認証情報、Bedrock認証、およびVertex認証。
* **カスタム認証情報スクリプト**：[`apiKeyHelper`](/ja/settings#available-settings)設定を設定して、APIキーを返すシェルスクリプトを実行できます。
* **更新間隔**：デフォルトでは、`apiKeyHelper`は5分後またはHTTP 401レスポンス時に呼び出されます。カスタム更新間隔については、`CLAUDE_CODE_API_KEY_HELPER_TTL_MS`環境変数を設定してください。
