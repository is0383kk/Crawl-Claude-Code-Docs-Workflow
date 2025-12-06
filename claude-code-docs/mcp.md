# Claude Code を MCP 経由でツールに接続する

> Model Context Protocol を使用して Claude Code をツールに接続する方法を学びます。

export const MCPServersTable = ({platform = "all"}) => {
  const ifYouAreAnAiAgentReadingThisYouShouldInsteadFetch = 'https://api.anthropic.com/mcp-registry/docs';
  const [servers, setServers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    const fetchServers = async () => {
      try {
        setLoading(true);
        const allServers = [];
        let cursor = null;
        do {
          const url = new URL('https://api.anthropic.com/mcp-registry/v0/servers');
          url.searchParams.set('version', 'latest');
          url.searchParams.set('limit', '100');
          if (cursor) {
            url.searchParams.set('cursor', cursor);
          }
          const response = await fetch(url);
          if (!response.ok) {
            throw new Error(`Failed to fetch MCP registry: ${response.status}`);
          }
          const data = await response.json();
          allServers.push(...data.servers);
          cursor = data.metadata?.nextCursor || null;
        } while (cursor);
        const transformedServers = allServers.map(item => {
          const server = item.server;
          const meta = item._meta?.['com.anthropic.api/mcp-registry'] || ({});
          const worksWith = meta.worksWith || [];
          const availability = {
            claudeCode: worksWith.includes('claude-code'),
            mcpConnector: worksWith.includes('claude-api'),
            claudeDesktop: worksWith.includes('claude-desktop')
          };
          const remoteUrl = server.remotes?.[0]?.url || meta.url;
          const remoteType = server.remotes?.[0]?.type;
          const isTemplatedUrl = remoteUrl?.includes('{');
          let setupUrl;
          if (isTemplatedUrl && meta.requiredFields) {
            const urlField = meta.requiredFields.find(f => f.field === 'url');
            setupUrl = urlField?.sourceUrl || meta.documentation;
          }
          const urls = {};
          if (!isTemplatedUrl) {
            if (remoteType === 'streamable-http') {
              urls.http = remoteUrl;
            } else if (remoteType === 'sse') {
              urls.sse = remoteUrl;
            }
          }
          let envVars = [];
          if (server.packages && server.packages.length > 0) {
            const npmPackage = server.packages.find(p => p.registryType === 'npm');
            if (npmPackage) {
              urls.stdio = `npx -y ${npmPackage.identifier}`;
              if (npmPackage.environmentVariables) {
                envVars = npmPackage.environmentVariables;
              }
            }
          }
          return {
            name: meta.displayName || server.title || server.name,
            description: meta.oneLiner || server.description,
            documentation: meta.documentation,
            urls: urls,
            envVars: envVars,
            availability: availability,
            customCommands: meta.claudeCodeCopyText ? {
              claudeCode: meta.claudeCodeCopyText
            } : undefined,
            setupUrl: setupUrl
          };
        });
        setServers(transformedServers);
        setError(null);
      } catch (err) {
        setError(err.message);
        console.error('Error fetching MCP registry:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchServers();
  }, []);
  const generateClaudeCodeCommand = server => {
    if (server.customCommands && server.customCommands.claudeCode) {
      return server.customCommands.claudeCode;
    }
    const serverSlug = server.name.toLowerCase().replace(/[^a-z0-9]/g, '-');
    if (server.urls.http) {
      return `claude mcp add ${serverSlug} --transport http ${server.urls.http}`;
    }
    if (server.urls.sse) {
      return `claude mcp add ${serverSlug} --transport sse ${server.urls.sse}`;
    }
    if (server.urls.stdio) {
      const envFlags = server.envVars && server.envVars.length > 0 ? server.envVars.map(v => `--env ${v.name}=YOUR_${v.name}`).join(' ') : '';
      const baseCommand = `claude mcp add ${serverSlug} --transport stdio`;
      return envFlags ? `${baseCommand} ${envFlags} -- ${server.urls.stdio}` : `${baseCommand} -- ${server.urls.stdio}`;
    }
    return null;
  };
  if (loading) {
    return <div>Loading MCP servers...</div>;
  }
  if (error) {
    return <div>Error loading MCP servers: {error}</div>;
  }
  const filteredServers = servers.filter(server => {
    if (platform === "claudeCode") {
      return server.availability.claudeCode;
    } else if (platform === "mcpConnector") {
      return server.availability.mcpConnector;
    } else if (platform === "claudeDesktop") {
      return server.availability.claudeDesktop;
    } else if (platform === "all") {
      return true;
    } else {
      throw new Error(`Unknown platform: ${platform}`);
    }
  });
  return <>
      <style jsx>{`
        .cards-container {
          display: grid;
          gap: 1rem;
          margin-bottom: 2rem;
        }
        .server-card {
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 6px;
          padding: 1rem;
        }
        .command-row {
          display: flex;
          align-items: center;
          gap: 0.25rem;
        }
        .command-row code {
          font-size: 0.75rem;
          overflow-x: auto;
        }
      `}</style>

      <div className="cards-container">
        {filteredServers.map(server => {
    const claudeCodeCommand = generateClaudeCodeCommand(server);
    const mcpUrl = server.urls.http || server.urls.sse;
    const commandToShow = platform === "claudeCode" ? claudeCodeCommand : mcpUrl;
    return <div key={server.name} className="server-card">
              <div>
                {server.documentation ? <a href={server.documentation}>
                    <strong>{server.name}</strong>
                  </a> : <strong>{server.name}</strong>}
              </div>

              <p style={{
      margin: '0.5rem 0',
      fontSize: '0.9rem'
    }}>
                {server.description}
              </p>

              {server.setupUrl && <p style={{
      margin: '0.25rem 0',
      fontSize: '0.8rem',
      fontStyle: 'italic',
      opacity: 0.7
    }}>
                  Requires user-specific URL.{' '}
                  <a href={server.setupUrl} style={{
      textDecoration: 'underline'
    }}>
                    Get your URL here
                  </a>.
                </p>}

              {commandToShow && !server.setupUrl && <>
                <p style={{
      display: 'block',
      fontSize: '0.75rem',
      fontWeight: 500,
      minWidth: 'fit-content',
      marginTop: '0.5rem',
      marginBottom: 0
    }}>
                  {platform === "claudeCode" ? "Command" : "URL"}
                </p>
                <div className="command-row">
                  <code>
                    {commandToShow}
                  </code>
                </div>
              </>}
            </div>;
  })}
      </div>
    </>;
};

Claude Code は、AI ツール統合のためのオープンソース標準である [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) を通じて、数百の外部ツールとデータソースに接続できます。MCP サーバーは Claude Code にツール、データベース、API へのアクセスを提供します。

## MCP でできること

MCP サーバーが接続されている場合、Claude Code に以下のことを依頼できます：

* **イシュー トラッカーから機能を実装する**: 「JIRA イシュー ENG-4521 に記載されている機能を追加し、GitHub に PR を作成してください。」
* **監視データを分析する**: 「Sentry と Statsig をチェックして、ENG-4521 に記載されている機能の使用状況を確認してください。」
* **データベースをクエリする**: 「Postgres データベースに基づいて、ENG-4521 機能を使用した 10 人のランダムなユーザーのメール アドレスを検索してください。」
* **デザインを統合する**: 「Slack に投稿された新しい Figma デザインに基づいて、標準メール テンプレートを更新してください。」
* **ワークフローを自動化する**: 「新機能に関するフィードバック セッションにこれら 10 人のユーザーを招待する Gmail ドラフトを作成してください。」

## 人気のある MCP サーバー

Claude Code に接続できる一般的に使用される MCP サーバーをいくつか紹介します：

<Warning>
  サードパーティの MCP サーバーは自己責任で使用してください - Anthropic はこれらすべてのサーバーの正確性またはセキュリティを検証していません。
  インストールする MCP サーバーを信頼していることを確認してください。
  信頼されていないコンテンツを取得する可能性のある MCP サーバーを使用する場合は特に注意してください。これらはプロンプト インジェクション リスクにさらされる可能性があります。
</Warning>

<MCPServersTable platform="claudeCode" />

<Note>
  **特定の統合が必要ですか？** [GitHub で数百以上の MCP サーバーを検索](https://github.com/modelcontextprotocol/servers)するか、[MCP SDK](https://modelcontextprotocol.io/quickstart/server) を使用して独自のサーバーを構築してください。
</Note>

## MCP サーバーのインストール

MCP サーバーは、ニーズに応じて 3 つの異なる方法で構成できます：

### オプション 1: リモート HTTP サーバーを追加する

HTTP サーバーは、リモート MCP サーバーに接続するための推奨オプションです。これはクラウドベースのサービスに対して最も広くサポートされているトランスポートです。

```bash  theme={null}
# 基本的な構文
claude mcp add --transport http <name> <url>

# 実際の例: Notion に接続する
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Bearer トークンを使用した例
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### オプション 2: リモート SSE サーバーを追加する

<Warning>
  SSE (Server-Sent Events) トランスポートは非推奨です。利用可能な場合は、代わりに HTTP サーバーを使用してください。
</Warning>

```bash  theme={null}
# 基本的な構文
claude mcp add --transport sse <name> <url>

# 実際の例: Asana に接続する
claude mcp add --transport sse asana https://mcp.asana.com/sse

# 認証ヘッダーを使用した例
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"
```

### オプション 3: ローカル stdio サーバーを追加する

Stdio サーバーはマシン上のローカル プロセスとして実行されます。システムへの直接アクセスまたはカスタム スクリプトが必要なツールに最適です。

```bash  theme={null}
# 基本的な構文
claude mcp add --transport stdio <name> <command> [args...]

# 実際の例: Airtable サーバーを追加する
claude mcp add --transport stdio airtable --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server
```

<Note>
  **「--」パラメータについて：**
  `--`（ダブル ダッシュ）は Claude 独自の CLI フラグを MCP サーバーに渡されるコマンドと引数から分離します。`--` の前のすべてはオプション（`--env`、`--scope` など）で、`--` の後のすべてが MCP サーバーを実行するための実際のコマンドです。

  例：

  * `claude mcp add --transport stdio myserver -- npx server` → `npx server` を実行します
  * `claude mcp add --transport stdio myserver --env KEY=value -- python server.py --port 8080` → 環境に `KEY=value` を設定して `python server.py --port 8080` を実行します

  これにより、Claude のフラグとサーバーのフラグ間の競合が防止されます。
</Note>

### サーバーの管理

設定後、これらのコマンドで MCP サーバーを管理できます：

```bash  theme={null}
# すべての設定済みサーバーをリストする
claude mcp list

# 特定のサーバーの詳細を取得する
claude mcp get github

# サーバーを削除する
claude mcp remove github

# (Claude Code 内) サーバーのステータスを確認する
/mcp
```

<Tip>
  ヒント：

  * `--scope` フラグを使用して、設定の保存場所を指定します：
    * `local`（デフォルト）: 現在のプロジェクト内のあなただけが利用可能（古いバージョンでは `project` と呼ばれていました）
    * `project`: `.mcp.json` ファイルを通じてプロジェクト内のすべてのユーザーと共有
    * `user`: すべてのプロジェクト全体であなたが利用可能（古いバージョンでは `global` と呼ばれていました）
  * `--env` フラグで環境変数を設定します（例：`--env KEY=value`）
  * MCP\_TIMEOUT 環境変数を使用して MCP サーバーのスタートアップ タイムアウトを構成します（例：`MCP_TIMEOUT=10000 claude` は 10 秒のタイムアウトを設定します）
  * Claude Code は MCP ツール出力が 10,000 トークンを超える場合に警告を表示します。この制限を増やすには、`MAX_MCP_OUTPUT_TOKENS` 環境変数を設定します（例：`MAX_MCP_OUTPUT_TOKENS=50000`）
  * `/mcp` を使用して、OAuth 2.0 認証が必要なリモート サーバーで認証します
</Tip>

<Warning>
  **Windows ユーザー**: ネイティブ Windows（WSL ではない）では、`npx` を使用するローカル MCP サーバーは適切な実行を確保するために `cmd /c` ラッパーが必要です。

  ```bash  theme={null}
  # これにより command="cmd" が作成され、Windows が実行できます
  claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
  ```

  `cmd /c` ラッパーがない場合、Windows は `npx` を直接実行できないため、「Connection closed」エラーが発生します。（`--` パラメータの説明については、上記のメモを参照してください。）
</Warning>

### プラグイン提供の MCP サーバー

[プラグイン](/ja/plugins)は MCP サーバーをバンドルでき、プラグインが有効になると自動的にツールと統合を提供します。プラグイン MCP サーバーはユーザー設定サーバーと同じように機能します。

**プラグイン MCP サーバーの仕組み**：

* プラグインはプラグイン ルートの `.mcp.json` または `plugin.json` 内でインラインで MCP サーバーを定義します
* プラグインが有効になると、その MCP サーバーが自動的に起動します
* プラグイン MCP ツールは手動で設定された MCP ツールと一緒に表示されます
* プラグイン サーバーはプラグイン インストール経由で管理されます（`/mcp` コマンドではありません）

**プラグイン MCP 設定の例**：

プラグイン ルートの `.mcp.json` 内：

```json  theme={null}
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```

または `plugin.json` 内でインライン：

```json  theme={null}
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```

**プラグイン MCP 機能**：

* **自動ライフサイクル**: プラグインが有効になるとサーバーが起動しますが、MCP サーバーの変更（有効化または無効化）を適用するには Claude Code を再起動する必要があります
* **環境変数**: プラグイン相対パスに `${CLAUDE_PLUGIN_ROOT}` を使用します
* **ユーザー環境アクセス**: 手動で設定されたサーバーと同じ環境変数へのアクセス
* **複数のトランスポート タイプ**: stdio、SSE、HTTP トランスポートをサポート（トランスポート サポートはサーバーによって異なる場合があります）

**プラグイン MCP サーバーの表示**：

```bash  theme={null}
# Claude Code 内で、プラグインのものを含むすべての MCP サーバーを表示します
/mcp
```

プラグイン サーバーはプラグインから来ていることを示すインジケーター付きでリストに表示されます。

**プラグイン MCP サーバーの利点**：

* **バンドル配布**: ツールとサーバーが一緒にパッケージ化されます
* **自動セットアップ**: 手動の MCP 設定は不要です
* **チーム一貫性**: プラグインがインストールされると、すべてのユーザーが同じツールを取得します

プラグインで MCP サーバーをバンドルする方法の詳細については、[プラグイン コンポーネント リファレンス](/ja/plugins-reference#mcp-servers)を参照してください。

## MCP インストール スコープ

MCP サーバーは 3 つの異なるスコープ レベルで設定でき、それぞれがサーバーのアクセス可能性と共有を管理するための異なる目的に役立ちます。これらのスコープを理解することで、特定のニーズに合わせてサーバーを設定する最適な方法を決定できます。

### ローカル スコープ

ローカル スコープ サーバーはデフォルトの設定レベルを表し、プロジェクト固有のユーザー設定に保存されます。これらのサーバーはあなたにのみプライベートで、現在のプロジェクト ディレクトリ内で作業する場合にのみアクセス可能です。このスコープは、個人開発サーバー、実験的な設定、または共有すべきでない機密認証情報を含むサーバーに最適です。

```bash  theme={null}
# ローカル スコープ サーバーを追加する（デフォルト）
claude mcp add --transport http stripe https://mcp.stripe.com

# ローカル スコープを明示的に指定する
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

### プロジェクト スコープ

プロジェクト スコープ サーバーは、プロジェクトのルート ディレクトリにある `.mcp.json` ファイルに設定を保存することで、チーム コラボレーションを実現します。このファイルはバージョン管理にチェックインされるように設計されており、すべてのチーム メンバーが同じ MCP ツールとサービスにアクセスできることを保証します。プロジェクト スコープ サーバーを追加すると、Claude Code は自動的にこのファイルを作成または更新し、適切な設定構造を使用します。

```bash  theme={null}
# プロジェクト スコープ サーバーを追加する
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp
```

結果の `.mcp.json` ファイルは標準化された形式に従います：

```json  theme={null}
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

セキュリティ上の理由から、Claude Code は `.mcp.json` ファイルからプロジェクト スコープ サーバーを使用する前に承認を求めます。これらの承認選択をリセットする必要がある場合は、`claude mcp reset-project-choices` コマンドを使用してください。

### ユーザー スコープ

ユーザー スコープ サーバーはクロスプロジェクト アクセスを提供し、マシン上のすべてのプロジェクト全体で利用可能にしながら、ユーザー アカウントにプライベートのままにします。このスコープは、個人ユーティリティ サーバー、開発ツール、または異なるプロジェクト全体で頻繁に使用するサービスに適しています。

```bash  theme={null}
# ユーザー サーバーを追加する
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### 適切なスコープの選択

以下に基づいてスコープを選択します：

* **ローカル スコープ**: 個人サーバー、実験的な設定、または 1 つのプロジェクトに固有の機密認証情報
* **プロジェクト スコープ**: チーム共有サーバー、プロジェクト固有のツール、またはコラボレーションに必要なサービス
* **ユーザー スコープ**: 複数のプロジェクト全体で必要な個人ユーティリティ、開発ツール、または頻繁に使用されるサービス

### スコープ階層と優先順位

MCP サーバー設定は明確な優先順位階層に従います。同じ名前のサーバーが複数のスコープに存在する場合、システムはローカル スコープ サーバーを最初に優先し、次にプロジェクト スコープ サーバー、最後にユーザー スコープ サーバーを優先することで競合を解決します。この設計により、個人設定が必要に応じて共有設定をオーバーライドできることが保証されます。

### `.mcp.json` での環境変数展開

Claude Code は `.mcp.json` ファイルでの環境変数展開をサポートしており、チームが設定を共有しながら、マシン固有のパスと API キーなどの機密値の柔軟性を維持できます。

**サポートされている構文：**

* `${VAR}` - 環境変数 `VAR` の値に展開されます
* `${VAR:-default}` - `VAR` が設定されている場合は展開され、そうでない場合は `default` を使用します

**展開場所：**
環境変数は以下で展開できます：

* `command` - サーバー実行可能ファイルのパス
* `args` - コマンドライン引数
* `env` - サーバーに渡される環境変数
* `url` - HTTP サーバー タイプの場合
* `headers` - HTTP サーバー認証の場合

**変数展開を使用した例：**

```json  theme={null}
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

必要な環境変数が設定されておらず、デフォルト値がない場合、Claude Code は設定の解析に失敗します。

## 実践的な例

{/* ### 例: Playwright でブラウザ テストを自動化する

  ```bash
  # 1. Playwright MCP サーバーを追加する
  claude mcp add --transport stdio playwright -- npx -y @playwright/mcp@latest

  # 2. ブラウザ テストを作成して実行する
  > "Test if the login flow works with test@example.com"
  > "Take a screenshot of the checkout page on mobile"
  > "Verify that the search feature returns results"
  ``` */}

### 例: Sentry でエラーを監視する

```bash  theme={null}
# 1. Sentry MCP サーバーを追加する
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 2. /mcp を使用して Sentry アカウントで認証する
> /mcp

# 3. 本番環境の問題をデバッグする
> "What are the most common errors in the last 24 hours?"
> "Show me the stack trace for error ID abc123"
> "Which deployment introduced these new errors?"
```

### 例: コード レビュー用に GitHub に接続する

```bash  theme={null}
# 1. GitHub MCP サーバーを追加する
claude mcp add --transport http github https://api.githubcopilot.com/mcp/

# 2. Claude Code で必要に応じて認証する
> /mcp
# GitHub の「認証」を選択します

# 3. これで Claude に GitHub で作業するよう依頼できます
> "Review PR #456 and suggest improvements"
> "Create a new issue for the bug we just found"
> "Show me all open PRs assigned to me"
```

### 例: PostgreSQL データベースをクエリする

```bash  theme={null}
# 1. 接続文字列を使用してデータベース サーバーを追加する
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"

# 2. データベースを自然にクエリする
> "What's our total revenue this month?"
> "Show me the schema for the orders table"
> "Find customers who haven't made a purchase in 90 days"
```

## リモート MCP サーバーで認証する

多くのクラウドベースの MCP サーバーは認証が必要です。Claude Code は安全な接続のために OAuth 2.0 をサポートしています。

<Steps>
  <Step title="認証が必要なサーバーを追加する">
    例：

    ```bash  theme={null}
    claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
    ```
  </Step>

  <Step title="Claude Code 内で /mcp コマンドを使用する">
    Claude Code で、コマンドを使用します：

    ```
    > /mcp
    ```

    次に、ブラウザのステップに従ってログインします。
  </Step>
</Steps>

<Tip>
  ヒント：

  * 認証トークンは安全に保存され、自動的に更新されます
  * `/mcp` メニューで「Clear authentication」を使用してアクセスを取り消します
  * ブラウザが自動的に開かない場合は、提供された URL をコピーします
  * OAuth 認証は HTTP サーバーで機能します
</Tip>

## JSON 設定から MCP サーバーを追加する

MCP サーバーの JSON 設定がある場合は、直接追加できます：

<Steps>
  <Step title="JSON から MCP サーバーを追加する">
    ```bash  theme={null}
    # 基本的な構文
    claude mcp add-json <name> '<json>'

    # 例: JSON 設定を使用して HTTP サーバーを追加する
    claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

    # 例: JSON 設定を使用して stdio サーバーを追加する
    claude mcp add-json local-weather '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'
    ```
  </Step>

  <Step title="サーバーが追加されたことを確認する">
    ```bash  theme={null}
    claude mcp get weather-api
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * JSON がシェルで適切にエスケープされていることを確認してください
  * JSON は MCP サーバー設定スキーマに準拠する必要があります
  * `--scope user` を使用して、プロジェクト固有のサーバーではなく、ユーザー設定にサーバーを追加できます
</Tip>

## Claude Desktop から MCP サーバーをインポートする

Claude Desktop で MCP サーバーを既に設定している場合は、それらをインポートできます：

<Steps>
  <Step title="Claude Desktop からサーバーをインポートする">
    ```bash  theme={null}
    # 基本的な構文 
    claude mcp add-from-claude-desktop 
    ```
  </Step>

  <Step title="インポートするサーバーを選択する">
    コマンドを実行した後、インポートするサーバーを選択できるインタラクティブ ダイアログが表示されます。
  </Step>

  <Step title="サーバーがインポートされたことを確認する">
    ```bash  theme={null}
    claude mcp list 
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * この機能は macOS と Windows Subsystem for Linux (WSL) でのみ機能します
  * これらのプラットフォームの標準的な場所から Claude Desktop 設定ファイルを読み取ります
  * `--scope user` フラグを使用して、ユーザー設定にサーバーを追加します
  * インポートされたサーバーは Claude Desktop と同じ名前を持ちます
  * 同じ名前のサーバーが既に存在する場合、数値サフィックスが付けられます（例：`server_1`）
</Tip>

## Claude Code を MCP サーバーとして使用する

Claude Code 自体を MCP サーバーとして使用でき、他のアプリケーションがそれに接続できます：

```bash  theme={null}
# Claude を stdio MCP サーバーとして起動する
claude mcp serve
```

これを Claude Desktop で使用するには、この設定を claude\_desktop\_config.json に追加します：

```json  theme={null}
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

<Warning>
  **実行可能ファイル パスの設定**: `command` フィールドは Claude Code 実行可能ファイルを参照する必要があります。`claude` コマンドがシステムの PATH にない場合は、実行可能ファイルへの完全なパスを指定する必要があります。

  完全なパスを見つけるには：

  ```bash  theme={null}
  which claude
  ```

  次に、設定で完全なパスを使用します：

  ```json  theme={null}
  {
    "mcpServers": {
      "claude-code": {
        "type": "stdio",
        "command": "/full/path/to/claude",
        "args": ["mcp", "serve"],
        "env": {}
      }
    }
  }
  ```

  正しい実行可能ファイル パスがない場合、`spawn claude ENOENT` などのエラーが発生します。
</Warning>

<Tip>
  ヒント：

  * サーバーは View、Edit、LS などの Claude のツールへのアクセスを提供します
  * Claude Desktop で、Claude にディレクトリ内のファイルを読み取り、編集などを行うよう依頼してみてください。
  * この MCP サーバーは単に Claude Code のツールを MCP クライアントに公開しているため、独自のクライアントは個々のツール呼び出しのユーザー確認を実装する責任があります。
</Tip>

## MCP 出力制限と警告

MCP ツールが大きな出力を生成する場合、Claude Code はトークン使用量を管理して会話コンテキストを圧倒しないようにするのに役立ちます：

* **出力警告しきい値**: Claude Code は MCP ツール出力が 10,000 トークンを超える場合に警告を表示します
* **設定可能な制限**: `MAX_MCP_OUTPUT_TOKENS` 環境変数を使用して、許可される最大 MCP 出力トークンを調整できます
* **デフォルト制限**: デフォルトの最大値は 25,000 トークンです

大きな出力を生成するツールの制限を増やすには：

```bash  theme={null}
# MCP ツール出力の制限を高くする
export MAX_MCP_OUTPUT_TOKENS=50000
claude
```

これは特に以下を行う MCP サーバーで作業する場合に便利です：

* 大規模なデータセットまたはデータベースをクエリする
* 詳細なレポートまたはドキュメントを生成する
* 広範なログ ファイルまたはデバッグ情報を処理する

<Warning>
  特定の MCP サーバーで出力警告が頻繁に発生する場合は、制限を増やすか、サーバーをページネーションまたはフィルタリング応答するように設定することを検討してください。
</Warning>

## MCP リソースを使用する

MCP サーバーはリソースを公開でき、ファイルを参照する方法と同様に @ メンションを使用して参照できます。

### MCP リソースを参照する

<Steps>
  <Step title="利用可能なリソースをリストする">
    プロンプトで `@` を入力して、接続されているすべての MCP サーバーから利用可能なリソースを表示します。リソースはオートコンプリート メニューのファイルと一緒に表示されます。
  </Step>

  <Step title="特定のリソースを参照する">
    `@server:protocol://resource/path` 形式を使用してリソースを参照します：

    ```
    > Can you analyze @github:issue://123 and suggest a fix?
    ```

    ```
    > Please review the API documentation at @docs:file://api/authentication
    ```
  </Step>

  <Step title="複数のリソース参照">
    1 つのプロンプトで複数のリソースを参照できます：

    ```
    > Compare @postgres:schema://users with @docs:file://database/user-model
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * リソースは参照されるときに自動的に取得され、添付ファイルとして含まれます
  * リソース パスは @ メンション オートコンプリートでファジー検索可能です
  * Claude Code は、サーバーがサポートしている場合、MCP リソースをリストおよび読み取るツールを自動的に提供します
  * リソースには、MCP サーバーが提供するあらゆるタイプのコンテンツ（テキスト、JSON、構造化データなど）を含めることができます
</Tip>

## MCP プロンプトをスラッシュ コマンドとして使用する

MCP サーバーはプロンプトを公開でき、Claude Code でスラッシュ コマンドとして利用可能になります。

### MCP プロンプトを実行する

<Steps>
  <Step title="利用可能なプロンプトを発見する">
    `/` を入力して、MCP サーバーからのプロンプトを含むすべての利用可能なコマンドを表示します。MCP プロンプトは `/mcp__servername__promptname` 形式で表示されます。
  </Step>

  <Step title="引数なしでプロンプトを実行する">
    ```
    > /mcp__github__list_prs
    ```
  </Step>

  <Step title="引数を使用してプロンプトを実行する">
    多くのプロンプトは引数を受け入れます。コマンドの後にスペース区切りで渡します：

    ```
    > /mcp__github__pr_review 456
    ```

    ```
    > /mcp__jira__create_issue "Bug in login flow" high
    ```
  </Step>
</Steps>

<Tip>
  ヒント：

  * MCP プロンプトは接続されているサーバーから動的に発見されます
  * 引数はプロンプトの定義されたパラメータに基づいて解析されます
  * プロンプト結果は会話に直接挿入されます
  * サーバーとプロンプト名は正規化されます（スペースはアンダースコアになります）
</Tip>

## エンタープライズ MCP 設定

MCP サーバーの一元管理が必要な組織の場合、Claude Code はエンタープライズ管理の MCP 設定をサポートしています。これにより、IT 管理者は以下のことができます：

* **従業員がアクセスできる MCP サーバーを制御する**: 組織全体で承認された MCP サーバーの標準化されたセットをデプロイします
* **不正な MCP サーバーを防止する**: オプションで、ユーザーが独自の MCP サーバーを追加することを制限します
* **MCP を完全に無効にする**: 必要に応じて MCP 機能を完全に削除します

### エンタープライズ MCP 設定のセットアップ

システム管理者は、管理設定ファイルと一緒にエンタープライズ MCP 設定ファイルをデプロイできます：

* **macOS**: `/Library/Application Support/ClaudeCode/managed-mcp.json`
* **Windows**: `C:\ProgramData\ClaudeCode\managed-mcp.json`
* **Linux**: `/etc/claude-code/managed-mcp.json`

`managed-mcp.json` ファイルは標準の `.mcp.json` ファイルと同じ形式を使用します：

```json  theme={null}
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"],
      "env": {
        "COMPANY_API_URL": "https://internal.company.com"
      }
    }
  }
}
```

### 許可リストと拒否リストで MCP サーバーを制限する

エンタープライズ管理サーバーの提供に加えて、管理者は `managed-settings.json` ファイルの `allowedMcpServers` と `deniedMcpServers` を使用して、ユーザーが設定できる MCP サーバーを制御できます：

* **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
* **Windows**: `C:\ProgramData\ClaudeCode\managed-settings.json`
* **Linux**: `/etc/claude-code/managed-settings.json`

```json  theme={null}
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "sentry" },
    { "serverName": "company-internal" }
  ],
  "deniedMcpServers": [
    { "serverName": "filesystem" }
  ]
}
```

**許可リスト動作（`allowedMcpServers`）**：

* `undefined`（デフォルト）: 制限なし - ユーザーは任意の MCP サーバーを設定できます
* 空の配列 `[]`: 完全なロックダウン - ユーザーは MCP サーバーを設定できません
* サーバー名のリスト: ユーザーは指定されたサーバーのみを設定できます

**拒否リスト動作（`deniedMcpServers`）**：

* `undefined`（デフォルト）: サーバーはブロックされません
* 空の配列 `[]`: サーバーはブロックされません
* サーバー名のリスト: 指定されたサーバーはすべてのスコープ全体で明示的にブロックされます

**重要な注意**：

* これらの制限はすべてのスコープに適用されます：ユーザー、プロジェクト、ローカル、および `managed-mcp.json` からのエンタープライズ サーバーでも
* **拒否リストは絶対的な優先順位を持ちます**: サーバーが両方のリストに表示される場合、ブロックされます

<Note>
  **エンタープライズ設定の優先順位**: エンタープライズ MCP 設定は最高の優先順位を持ち、ユーザー、ローカル、またはプロジェクト設定でオーバーライドすることはできません。
</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt