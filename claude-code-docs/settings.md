# Claude Code 設定

> Claude Code をグローバル設定とプロジェクトレベルの設定、および環境変数で構成します。

Claude Code は、ニーズに合わせて動作を構成するためのさまざまな設定を提供します。インタラクティブ REPL を使用する際に `/config` コマンドを実行することで Claude Code を構成できます。これにより、ステータス情報を表示し、構成オプションを変更できるタブ付き設定インターフェースが開きます。

## 設定ファイル

`settings.json` ファイルは、階層的な設定を通じて Claude Code を構成するための公式メカニズムです。

* **ユーザー設定**は `~/.claude/settings.json` で定義され、すべてのプロジェクトに適用されます。
* **プロジェクト設定**はプロジェクトディレクトリに保存されます。
  * `.claude/settings.json` はソース管理にチェックインされ、チームと共有される設定用です。
  * `.claude/settings.local.json` はチェックインされない設定用で、個人的な設定と実験に役立ちます。Claude Code は作成時に `.claude/settings.local.json` を無視するように git を構成します。
* Claude Code のエンタープライズデプロイメントの場合、**エンタープライズ管理ポリシー設定**もサポートしています。これらはユーザー設定とプロジェクト設定より優先されます。システム管理者は以下にポリシーをデプロイできます。
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Linux と WSL: `/etc/claude-code/managed-settings.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-settings.json`
* エンタープライズデプロイメントは、ユーザーが構成したサーバーをオーバーライドする**管理 MCP サーバー**も構成できます。[エンタープライズ MCP 構成](/ja/mcp#enterprise-mcp-configuration)を参照してください。
  * macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
  * Linux と WSL: `/etc/claude-code/managed-mcp.json`
  * Windows: `C:\ProgramData\ClaudeCode\managed-mcp.json`

```JSON Example settings.json theme={null}
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  }
}
```

### 利用可能な設定

`settings.json` は多くのオプションをサポートしています。

| キー                           | 説明                                                                                                                                                                                   | 例                                                           |
| :--------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `apiKeyHelper`               | 認証値を生成するために `/bin/sh` で実行されるカスタムスクリプト。この値は `X-Api-Key` および `Authorization: Bearer` ヘッダーとしてモデルリクエストに送信されます                                                                            | `/bin/generate_temp_api_key.sh`                             |
| `cleanupPeriodDays`          | この期間より長く非アクティブなセッションは起動時に削除されます。`0` に設定すると、すべてのセッションが即座に削除されます。（デフォルト: 30 日）                                                                                                         | `20`                                                        |
| `env`                        | すべてのセッションに適用される環境変数                                                                                                                                                                  | `{"FOO": "bar"}`                                            |
| `includeCoAuthoredBy`        | git コミットとプルリクエストに `co-authored-by Claude` のバイラインを含めるかどうか（デフォルト: `true`）                                                                                                              | `false`                                                     |
| `permissions`                | 権限の構造については以下の表を参照してください。                                                                                                                                                             |                                                             |
| `hooks`                      | ツール実行の前後に実行するカスタムコマンドを構成します。[hooks ドキュメント](/ja/hooks)を参照してください。                                                                                                                      | `{"PreToolUse": {"Bash": "echo 'Running command...'"}}`     |
| `disableAllHooks`            | すべての [hooks](/ja/hooks) を無効にします。                                                                                                                                                     | `true`                                                      |
| `model`                      | Claude Code に使用するデフォルトモデルをオーバーライドします。                                                                                                                                                | `"claude-sonnet-4-5-20250929"`                              |
| `statusLine`                 | コンテキストを表示するカスタムステータスラインを構成します。[statusLine ドキュメント](/ja/statusline)を参照してください。                                                                                                          | `{"type": "command", "command": "~/.claude/statusline.sh"}` |
| `outputStyle`                | システムプロンプトを調整する出力スタイルを構成します。[出力スタイルドキュメント](/ja/output-styles)を参照してください。                                                                                                               | `"Explanatory"`                                             |
| `forceLoginMethod`           | `claudeai` を使用して Claude.ai アカウントへのログインを制限するか、`console` を使用して Claude Console（API 使用量課金）アカウントへのログインを制限します。                                                                             | `claudeai`                                                  |
| `forceLoginOrgUUID`          | ログイン中に自動的に選択する組織の UUID を指定し、組織選択ステップをバイパスします。`forceLoginMethod` が設定されている必要があります。                                                                                                     | `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`                    |
| `enableAllProjectMcpServers` | プロジェクト `.mcp.json` ファイルで定義されたすべての MCP サーバーを自動的に承認します。                                                                                                                                | `true`                                                      |
| `enabledMcpjsonServers`      | `.mcp.json` ファイルから承認する特定の MCP サーバーのリスト                                                                                                                                               | `["memory", "github"]`                                      |
| `disabledMcpjsonServers`     | `.mcp.json` ファイルから拒否する特定の MCP サーバーのリスト                                                                                                                                               | `["filesystem"]`                                            |
| `useEnterpriseMcpConfigOnly` | managed-settings.json で設定された場合、MCP サーバーを managed-mcp.json で定義されたもののみに制限します。[エンタープライズ MCP 構成](/ja/mcp#enterprise-mcp-configuration)を参照してください。                                         | `true`                                                      |
| `allowedMcpServers`          | managed-settings.json で設定された場合、ユーザーが構成できる MCP サーバーのホワイトリスト。未定義 = 制限なし、空配列 = ロックダウン。すべてのスコープに適用されます。ブロックリストが優先されます。[エンタープライズ MCP 構成](/ja/mcp#enterprise-mcp-configuration)を参照してください。  | `[{ "serverName": "github" }]`                              |
| `deniedMcpServers`           | managed-settings.json で設定された場合、明示的にブロックされた MCP サーバーのブロックリスト。エンタープライズサーバーを含むすべてのスコープに適用されます。ブロックリストはホワイトリストより優先されます。[エンタープライズ MCP 構成](/ja/mcp#enterprise-mcp-configuration)を参照してください。 | `[{ "serverName": "filesystem" }]`                          |
| `awsAuthRefresh`             | `.aws` ディレクトリを変更するカスタムスクリプト（[高度な認証情報構成](/ja/amazon-bedrock#advanced-credential-configuration)を参照）                                                                                    | `aws sso login --profile myprofile`                         |
| `awsCredentialExport`        | AWS 認証情報を含む JSON を出力するカスタムスクリプト（[高度な認証情報構成](/ja/amazon-bedrock#advanced-credential-configuration)を参照）                                                                                | `/bin/generate_aws_grant.sh`                                |

### 権限設定

| キー                             | 説明                                                                                                                                                                                                   | 例                                                                      |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| `allow`                        | ツール使用を許可する[権限ルール](/ja/iam#configuring-permissions)の配列。**注:** Bash ルールはプレフィックスマッチングを使用し、正規表現ではありません。                                                                                                  | `[ "Bash(git diff:*)" ]`                                               |
| `ask`                          | ツール使用時に確認を求める[権限ルール](/ja/iam#configuring-permissions)の配列。                                                                                                                                            | `[ "Bash(git push:*)" ]`                                               |
| `deny`                         | ツール使用を拒否する[権限ルール](/ja/iam#configuring-permissions)の配列。これを使用して、Claude Code アクセスから機密ファイルを除外することもできます。**注:** Bash パターンはプレフィックスマッチであり、バイパスできます（[Bash 権限の制限](/ja/iam#tool-specific-permission-rules)を参照）。 | `[ "WebFetch", "Bash(curl:*)", "Read(./.env)", "Read(./secrets/**)" ]` |
| `additionalDirectories`        | Claude がアクセスできる追加の[作業ディレクトリ](/ja/iam#working-directories)                                                                                                                                            | `[ "../docs/" ]`                                                       |
| `defaultMode`                  | Claude Code を開く際のデフォルト[権限モード](/ja/iam#permission-modes)                                                                                                                                              | `"acceptEdits"`                                                        |
| `disableBypassPermissionsMode` | `"disable"` に設定して `bypassPermissions` モードの有効化を防止します。これにより `--dangerously-skip-permissions` コマンドラインフラグが無効になります。[管理ポリシー設定](/ja/iam#enterprise-managed-policy-settings)を参照してください。                       | `"disable"`                                                            |

### サンドボックス設定

高度なサンドボックス動作を構成します。サンドボックスは bash コマンドをファイルシステムとネットワークから分離します。詳細は[サンドボックス](/ja/sandboxing)を参照してください。

**ファイルシステムとネットワークの制限**は、これらのサンドボックス設定ではなく、Read、Edit、および WebFetch 権限ルールを通じて構成されます。

| キー                          | 説明                                                                                                                                                                                                                                  | 例                         |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| `enabled`                   | bash サンドボックスを有効にします（macOS/Linux のみ）。デフォルト: false                                                                                                                                                                                    | `true`                    |
| `autoAllowBashIfSandboxed`  | サンドボックス化されている場合、bash コマンドを自動承認します。デフォルト: true                                                                                                                                                                                       | `true`                    |
| `excludedCommands`          | サンドボックスの外で実行すべきコマンド                                                                                                                                                                                                                 | `["git", "docker"]`       |
| `allowUnsandboxedCommands`  | `dangerouslyDisableSandbox` パラメータを通じてコマンドをサンドボックスの外で実行することを許可します。`false` に設定すると、`dangerouslyDisableSandbox` エスケープハッチは完全に無効になり、すべてのコマンドはサンドボックス化されるか `excludedCommands` に含まれる必要があります。厳密なサンドボックス化を必要とするエンタープライズポリシーに役立ちます。デフォルト: true | `false`                   |
| `network.allowUnixSockets`  | サンドボックスでアクセス可能な Unix ソケットパス（SSH エージェント用など）                                                                                                                                                                                          | `["~/.ssh/agent-socket"]` |
| `network.allowLocalBinding` | localhost ポートへのバインドを許可します（MacOS のみ）。デフォルト: false                                                                                                                                                                                    | `true`                    |
| `network.httpProxyPort`     | 独自のプロキシを使用する場合に使用される HTTP プロキシポート。指定されない場合、Claude は独自のプロキシを実行します。                                                                                                                                                                   | `8080`                    |
| `network.socksProxyPort`    | 独自のプロキシを使用する場合に使用される SOCKS5 プロキシポート。指定されない場合、Claude は独自のプロキシを実行します。                                                                                                                                                                 | `8081`                    |
| `enableWeakerNestedSandbox` | 非特権 Docker 環境用の弱いサンドボックスを有効にします（Linux のみ）。**セキュリティが低下します。** デフォルト: false                                                                                                                                                            | `true`                    |

**構成例:**

```json  theme={null}
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker"],
    "network": {
      "allowUnixSockets": [
        "/var/run/docker.sock"
      ],
      "allowLocalBinding": true
    }
  },
  "permissions": {
    "deny": [
      "Read(.envrc)",
      "Read(~/.aws/**)"
    ]
  }
}
```

**ファイルシステムアクセス**は Read/Edit 権限を通じて制御されます。

* Read 拒否ルールはサンドボックス内のファイル読み取りをブロックします。
* Edit 許可ルールはファイル書き込みを許可します（デフォルトに加えて、例えば現在の作業ディレクトリ）。
* Edit 拒否ルールは許可されたパス内の書き込みをブロックします。

**ネットワークアクセス**は WebFetch 権限を通じて制御されます。

* WebFetch 許可ルールはネットワークドメインを許可します。
* WebFetch 拒否ルールはネットワークドメインをブロックします。

### 設定の優先順位

設定は優先順位の順序（高から低）で適用されます。

1. **エンタープライズ管理ポリシー** (`managed-settings.json`)
   * IT/DevOps によってデプロイされます。
   * オーバーライドできません。

2. **コマンドラインの引数**
   * 特定のセッションの一時的なオーバーライド

3. **ローカルプロジェクト設定** (`.claude/settings.local.json`)
   * 個人的なプロジェクト固有の設定

4. **共有プロジェクト設定** (`.claude/settings.json`)
   * ソース管理内のチーム共有プロジェクト設定

5. **ユーザー設定** (`~/.claude/settings.json`)
   * 個人的なグローバル設定

この階層により、エンタープライズセキュリティポリシーが常に適用されながら、チームと個人が自分の経験をカスタマイズできるようになります。

### 構成システムに関する重要なポイント

* **メモリファイル (CLAUDE.md)**: Claude が起動時にロードする指示とコンテキストを含みます。
* **設定ファイル (JSON)**: 権限、環境変数、およびツール動作を構成します。
* **スラッシュコマンド**: セッション中に `/command-name` で呼び出すことができるカスタムコマンド。
* **MCP サーバー**: 追加のツールと統合で Claude Code を拡張します。
* **優先順位**: 高レベルの構成（エンタープライズ）は低レベルのもの（ユーザー/プロジェクト）をオーバーライドします。
* **継承**: 設定はマージされ、より具体的な設定がより広い設定に追加またはオーバーライドされます。

### システムプロンプトの可用性

<Note>
  claude.ai とは異なり、Claude Code の内部システムプロンプトはこのウェブサイトに公開していません。CLAUDE.md ファイルまたは `--append-system-prompt` を使用して、Claude Code の動作にカスタム指示を追加してください。
</Note>

### 機密ファイルの除外

Claude Code が機密情報（API キー、シークレット、環境ファイルなど）を含むファイルにアクセスするのを防ぐには、`.claude/settings.json` ファイルで `permissions.deny` 設定を使用します。

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./build)"
    ]
  }
}
```

これは非推奨の `ignorePatterns` 構成に代わるものです。これらのパターンに一致するファイルは Claude Code に完全に見えなくなり、機密データの偶発的な公開を防ぎます。

## サブエージェント構成

Claude Code は、ユーザーレベルとプロジェクトレベルの両方で構成できるカスタム AI サブエージェントをサポートしています。これらのサブエージェントは YAML フロントマターを持つ Markdown ファイルとして保存されます。

* **ユーザーサブエージェント**: `~/.claude/agents/` - すべてのプロジェクトで利用可能
* **プロジェクトサブエージェント**: `.claude/agents/` - プロジェクト固有で、チームと共有できます。

サブエージェントファイルは、カスタムプロンプトとツール権限を持つ特殊な AI アシスタントを定義します。サブエージェントの作成と使用の詳細については、[サブエージェントドキュメント](/ja/sub-agents)を参照してください。

## プラグイン構成

Claude Code はプラグインシステムをサポートしており、カスタムコマンド、エージェント、フック、および MCP サーバーで機能を拡張できます。プラグインはマーケットプレイスを通じて配布され、ユーザーレベルとリポジトリレベルの両方で構成できます。

### プラグイン設定

`settings.json` のプラグイン関連設定:

```json  theme={null}
{
  "enabledPlugins": {
    "formatter@company-tools": true,
    "deployer@company-tools": true,
    "analyzer@security-plugins": false
  },
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": "github",
      "repo": "company/claude-plugins"
    }
  }
}
```

#### `enabledPlugins`

どのプラグインが有効かを制御します。形式: `"plugin-name@marketplace-name": true/false`

**スコープ**:

* **ユーザー設定** (`~/.claude/settings.json`): 個人的なプラグイン設定
* **プロジェクト設定** (`.claude/settings.json`): チームと共有されるプロジェクト固有のプラグイン
* **ローカル設定** (`.claude/settings.local.json`): マシンごとのオーバーライド（コミットされない）

**例**:

```json  theme={null}
{
  "enabledPlugins": {
    "code-formatter@team-tools": true,
    "deployment-tools@team-tools": true,
    "experimental-features@personal": false
  }
}
```

#### `extraKnownMarketplaces`

リポジトリで利用可能にすべき追加マーケットプレイスを定義します。通常、リポジトリレベルの設定で使用され、チームメンバーが必要なプラグインソースにアクセスできるようにします。

**リポジトリが `extraKnownMarketplaces` を含む場合**:

1. チームメンバーはフォルダを信頼するときにマーケットプレイスをインストールするよう促されます。
2. チームメンバーはそのマーケットプレイスからプラグインをインストールするよう促されます。
3. ユーザーは不要なマーケットプレイスまたはプラグインをスキップできます（ユーザー設定に保存されます）。
4. インストールは信頼境界を尊重し、明示的な同意が必要です。

**例**:

```json  theme={null}
{
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": {
        "source": "github",
        "repo": "company-org/claude-plugins"
      }
    },
    "security-plugins": {
      "source": {
        "source": "git",
        "url": "https://git.company.com/security/plugins.git"
      }
    }
  }
}
```

**マーケットプレイスソースタイプ**:

* `github`: GitHub リポジトリ（`repo` を使用）
* `git`: 任意の git URL（`url` を使用）
* `directory`: ローカルファイルシステムパス（`path` を使用、開発のみ）

### プラグインの管理

`/plugin` コマンドを使用してプラグインを対話的に管理します。

* マーケットプレイスから利用可能なプラグインを参照
* プラグインをインストール/アンインストール
* プラグインを有効/無効
* プラグインの詳細を表示（提供されるコマンド、エージェント、フック）
* マーケットプレイスを追加/削除

プラグインシステムの詳細については、[プラグインドキュメント](/ja/plugins)を参照してください。

## 環境変数

Claude Code は、その動作を制御するために以下の環境変数をサポートしています。

<Note>
  すべての環境変数は [`settings.json`](#available-settings) でも構成できます。これは各セッションの環境変数を自動的に設定したり、チーム全体または組織全体に環境変数のセットをロールアウトする方法として役立ちます。
</Note>

| 変数                                         | 目的                                                                                                                                                                                                                                                                       |
| :----------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ANTHROPIC_API_KEY`                        | `X-Api-Key` ヘッダーとして送信される API キー、通常は Claude SDK 用（インタラクティブ使用の場合は `/login` を実行）                                                                                                                                                                                            |
| `ANTHROPIC_AUTH_TOKEN`                     | `Authorization` ヘッダーのカスタム値（ここで設定した値には `Bearer ` が付加されます）                                                                                                                                                                                                                 |
| `ANTHROPIC_CUSTOM_HEADERS`                 | リクエストに追加したいカスタムヘッダー（`Name: Value` 形式）                                                                                                                                                                                                                                    |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL`            | [モデル構成](/ja/model-config#environment-variables)を参照                                                                                                                                                                                                                       |
| `ANTHROPIC_DEFAULT_OPUS_MODEL`             | [モデル構成](/ja/model-config#environment-variables)を参照                                                                                                                                                                                                                       |
| `ANTHROPIC_DEFAULT_SONNET_MODEL`           | [モデル構成](/ja/model-config#environment-variables)を参照                                                                                                                                                                                                                       |
| `ANTHROPIC_MODEL`                          | 使用するモデル設定の名前（[モデル構成](/ja/model-config#environment-variables)を参照）                                                                                                                                                                                                         |
| `ANTHROPIC_SMALL_FAST_MODEL`               | \[非推奨] [バックグラウンドタスク用 Haiku クラスモデル](/ja/costs)の名前                                                                                                                                                                                                                         |
| `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION`    | Bedrock を使用する場合、Haiku クラスモデルの AWS リージョンをオーバーライド                                                                                                                                                                                                                          |
| `AWS_BEARER_TOKEN_BEDROCK`                 | 認証用 Bedrock API キー（[Bedrock API キー](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/)を参照）                                                                                                                           |
| `BASH_DEFAULT_TIMEOUT_MS`                  | 長時間実行される bash コマンドのデフォルトタイムアウト                                                                                                                                                                                                                                           |
| `BASH_MAX_OUTPUT_LENGTH`                   | 中央で切り詰められる前の bash 出力の最大文字数                                                                                                                                                                                                                                               |
| `BASH_MAX_TIMEOUT_MS`                      | モデルが長時間実行される bash コマンドに設定できる最大タイムアウト                                                                                                                                                                                                                                     |
| `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` | 各 Bash コマンド後に元の作業ディレクトリに戻る                                                                                                                                                                                                                                               |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`        | 認証情報をリフレッシュすべき間隔（ミリ秒）（`apiKeyHelper` を使用する場合）                                                                                                                                                                                                                            |
| `CLAUDE_CODE_CLIENT_CERT`                  | mTLS 認証用のクライアント証明書ファイルへのパス                                                                                                                                                                                                                                               |
| `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`        | 暗号化された CLAUDE\_CODE\_CLIENT\_KEY のパスフレーズ（オプション）                                                                                                                                                                                                                          |
| `CLAUDE_CODE_CLIENT_KEY`                   | mTLS 認証用のクライアント秘密鍵ファイルへのパス                                                                                                                                                                                                                                               |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | `DISABLE_AUTOUPDATER`、`DISABLE_BUG_COMMAND`、`DISABLE_ERROR_REPORTING`、および `DISABLE_TELEMETRY` の設定と同等                                                                                                                                                                     |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE`       | `1` に設定して、会話コンテキストに基づく自動ターミナルタイトル更新を無効にする                                                                                                                                                                                                                                |
| `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL`        | IDE 拡張機能の自動インストールをスキップ                                                                                                                                                                                                                                                   |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS`            | ほとんどのリクエストの最大出力トークン数を設定                                                                                                                                                                                                                                                  |
| `CLAUDE_CODE_SHELL_PREFIX`                 | すべての bash コマンドをラップするコマンドプレフィックス（例：ログ記録や監査用）。例：`/path/to/logger.sh` は `/path/to/logger.sh <コマンド>` として実行されます                                                                                                                                                               |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH`            | Bedrock の AWS 認証をスキップ（例えば LLM ゲートウェイを使用する場合）                                                                                                                                                                                                                             |
| `CLAUDE_CODE_SKIP_VERTEX_AUTH`             | Vertex の Google 認証をスキップ（例えば LLM ゲートウェイを使用する場合）                                                                                                                                                                                                                           |
| `CLAUDE_CODE_SUBAGENT_MODEL`               | [モデル構成](/ja/model-config)を参照                                                                                                                                                                                                                                             |
| `CLAUDE_CODE_USE_BEDROCK`                  | [Bedrock](/ja/amazon-bedrock) を使用                                                                                                                                                                                                                                        |
| `CLAUDE_CODE_USE_VERTEX`                   | [Vertex](/ja/google-vertex-ai) を使用                                                                                                                                                                                                                                       |
| `DISABLE_AUTOUPDATER`                      | `1` に設定して自動更新を無効にします。これは `autoUpdates` 構成設定より優先されます。                                                                                                                                                                                                                     |
| `DISABLE_BUG_COMMAND`                      | `1` に設定して `/bug` コマンドを無効にする                                                                                                                                                                                                                                              |
| `DISABLE_COST_WARNINGS`                    | `1` に設定してコスト警告メッセージを無効にする                                                                                                                                                                                                                                                |
| `DISABLE_ERROR_REPORTING`                  | `1` に設定して Sentry エラーレポートをオプトアウト                                                                                                                                                                                                                                          |
| `DISABLE_NON_ESSENTIAL_MODEL_CALLS`        | `1` に設定してフレーバーテキストなどの非重要パスのモデル呼び出しを無効にする                                                                                                                                                                                                                                 |
| `DISABLE_PROMPT_CACHING`                   | `1` に設定してすべてのモデルのプロンプトキャッシングを無効にします（モデルごとの設定より優先）                                                                                                                                                                                                                        |
| `DISABLE_PROMPT_CACHING_HAIKU`             | `1` に設定して Haiku モデルのプロンプトキャッシングを無効にする                                                                                                                                                                                                                                    |
| `DISABLE_PROMPT_CACHING_OPUS`              | `1` に設定して Opus モデルのプロンプトキャッシングを無効にする                                                                                                                                                                                                                                     |
| `DISABLE_PROMPT_CACHING_SONNET`            | `1` に設定して Sonnet モデルのプロンプトキャッシングを無効にする                                                                                                                                                                                                                                   |
| `DISABLE_TELEMETRY`                        | `1` に設定して Statsig テレメトリをオプトアウト（Statsig イベントにはコード、ファイルパス、bash コマンドなどのユーザーデータは含まれないことに注意）                                                                                                                                                                                  |
| `HTTP_PROXY`                               | ネットワーク接続用の HTTP プロキシサーバーを指定                                                                                                                                                                                                                                              |
| `HTTPS_PROXY`                              | ネットワーク接続用の HTTPS プロキシサーバーを指定                                                                                                                                                                                                                                             |
| `MAX_MCP_OUTPUT_TOKENS`                    | MCP ツール応答で許可される最大トークン数。Claude Code は出力が 10,000 トークンを超える場合に警告を表示します（デフォルト: 25000）                                                                                                                                                                                         |
| `MAX_THINKING_TOKENS`                      | [拡張思考](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)を有効にし、思考プロセスのトークン予算を設定します。拡張思考は複雑な推論とコーディングタスクのパフォーマンスを向上させますが、[プロンプトキャッシング効率](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#caching-with-thinking-blocks)に影響します。デフォルトで無効。 |
| `MCP_TIMEOUT`                              | MCP サーバー起動のタイムアウト（ミリ秒）                                                                                                                                                                                                                                                   |
| `MCP_TOOL_TIMEOUT`                         | MCP ツール実行のタイムアウト（ミリ秒）                                                                                                                                                                                                                                                    |
| `NO_PROXY`                                 | リクエストが直接発行されるドメインと IP のリスト（プロキシをバイパス）                                                                                                                                                                                                                                    |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET`           | [SlashCommand ツール](/ja/slash-commands#slashcommand-tool)に表示されるスラッシュコマンドメタデータの最大文字数（デフォルト: 15000）                                                                                                                                                                         |
| `USE_BUILTIN_RIPGREP`                      | `0` に設定して Claude Code に含まれる `rg` の代わりにシステムインストール済みの `rg` を使用                                                                                                                                                                                                             |
| `VERTEX_REGION_CLAUDE_3_5_HAIKU`           | Vertex AI を使用する場合、Claude 3.5 Haiku のリージョンをオーバーライド                                                                                                                                                                                                                        |
| `VERTEX_REGION_CLAUDE_3_7_SONNET`          | Vertex AI を使用する場合、Claude 3.7 Sonnet のリージョンをオーバーライド                                                                                                                                                                                                                       |
| `VERTEX_REGION_CLAUDE_4_0_OPUS`            | Vertex AI を使用する場合、Claude 4.0 Opus のリージョンをオーバーライド                                                                                                                                                                                                                         |
| `VERTEX_REGION_CLAUDE_4_0_SONNET`          | Vertex AI を使用する場合、Claude 4.0 Sonnet のリージョンをオーバーライド                                                                                                                                                                                                                       |
| `VERTEX_REGION_CLAUDE_4_1_OPUS`            | Vertex AI を使用する場合、Claude 4.1 Opus のリージョンをオーバーライド                                                                                                                                                                                                                         |

## Claude が利用できるツール

Claude Code は、コードベースを理解および変更するのに役立つ強力なツールのセットにアクセスできます。

| ツール              | 説明                                                       | 権限が必要 |
| :--------------- | :------------------------------------------------------- | :---- |
| **Bash**         | 環境でシェルコマンドを実行                                            | はい    |
| **Edit**         | 特定のファイルに対象を絞った編集を行う                                      | はい    |
| **Glob**         | パターンマッチングに基づいてファイルを検索                                    | いいえ   |
| **Grep**         | ファイルコンテンツ内のパターンを検索                                       | いいえ   |
| **NotebookEdit** | Jupyter ノートブックセルを変更                                      | はい    |
| **NotebookRead** | Jupyter ノートブックコンテンツを読み取って表示                              | いいえ   |
| **Read**         | ファイルのコンテンツを読み取る                                          | いいえ   |
| **SlashCommand** | [カスタムスラッシュコマンド](/ja/slash-commands#slashcommand-tool)を実行 | はい    |
| **Task**         | 複雑なマルチステップタスクを処理するサブエージェントを実行                            | いいえ   |
| **TodoWrite**    | 構造化されたタスクリストを作成および管理                                     | いいえ   |
| **WebFetch**     | 指定された URL からコンテンツを取得                                     | はい    |
| **WebSearch**    | ドメインフィルタリング付きで Web 検索を実行                                 | はい    |
| **Write**        | ファイルを作成または上書き                                            | はい    |

権限ルールは `/allowed-tools` を使用するか、[権限設定](/ja/settings#available-settings)で構成できます。[ツール固有の権限ルール](/ja/iam#tool-specific-permission-rules)も参照してください。

### フックでツールを拡張

[Claude Code フック](/ja/hooks-guide)を使用して、任意のツール実行の前後にカスタムコマンドを実行できます。

たとえば、Claude が Python ファイルを変更した後に Python フォーマッターを自動的に実行したり、特定のパスへの Write 操作をブロックして本番構成ファイルの変更を防止したりできます。

## 関連項目

* [Identity and Access Management](/ja/iam#configuring-permissions) - Claude Code の権限システムについて学ぶ
* [IAM とアクセス制御](/ja/iam#enterprise-managed-policy-settings) - エンタープライズポリシー管理
* [トラブルシューティング](/ja/troubleshooting#auto-updater-issues) - 一般的な構成の問題の解決策


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt