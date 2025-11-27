# LLM gateway設定

> Claude CodeをLLM gatewayソリューションで設定する方法を学びます。LiteLLMセットアップ、認証方法、使用状況追跡やバジェット管理などのエンタープライズ機能を含みます。

LLM gatewayは、Claude CodeとモデルプロバイダーとのCentralized proxyレイヤーを提供し、以下を提供します：

* **Centralized authentication** - API キー管理の単一ポイント
* **使用状況追跡** - チームとプロジェクト全体の使用状況を監視
* **コスト管理** - バジェットとレート制限を実装
* **監査ログ** - コンプライアンスのためにすべてのモデルインタラクションを追跡
* **モデルルーティング** - コード変更なしでプロバイダー間を切り替え

## LiteLLM設定

<Note>
  LiteLLMはサードパーティのプロキシサービスです。Anthropicは、LiteLLMのセキュリティまたは機能を承認、保守、または監査していません。このガイドは情報提供目的で提供されており、古くなる可能性があります。自由裁量で使用してください。
</Note>

### 前提条件

* Claude Codeが最新バージョンに更新されている
* LiteLLM Proxy Serverがデプロイされてアクセス可能
* 選択したプロバイダーを通じてClaudeモデルにアクセス可能

### 基本的なLiteLLMセットアップ

**Claude Codeを設定**：

#### 認証方法

##### 静的APIキー

固定APIキーを使用した最もシンプルな方法：

```bash  theme={null}
# 環境変数で設定
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key

# またはClaude Code設定で
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}
```

この値は`Authorization`ヘッダーとして送信されます。

##### ヘルパーを使用した動的APIキー

キーのローテーションまたはユーザーごとの認証の場合：

1. APIキーヘルパースクリプトを作成：

```bash  theme={null}
#!/bin/bash
# ~/bin/get-litellm-key.sh

# 例：vaultからキーを取得
vault kv get -field=api_key secret/litellm/claude-code

# 例：JWTトークンを生成
jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'
```

2. ヘルパーを使用するようにClaude Code設定を構成：

```json  theme={null}
{
  "apiKeyHelper": "~/bin/get-litellm-key.sh"
}
```

3. トークンリフレッシュ間隔を設定：

```bash  theme={null}
# 1時間ごとにリフレッシュ（3600000 ms）
export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000
```

この値は`Authorization`および`X-Api-Key`ヘッダーとして送信されます。`apiKeyHelper`は`ANTHROPIC_AUTH_TOKEN`または`ANTHROPIC_API_KEY`より優先度が低いです。

#### 統合エンドポイント（推奨）

LiteLLMの[Anthropic形式エンドポイント](https://docs.litellm.ai/docs/anthropic_unified)を使用：

```bash  theme={null}
export ANTHROPIC_BASE_URL=https://litellm-server:4000
```

**パススルーエンドポイントに対する統合エンドポイントの利点：**

* ロードバランシング
* フェイルオーバー
* コスト追跡とエンドユーザー追跡の一貫したサポート

#### プロバイダー固有のパススルーエンドポイント（代替）

##### LiteLLMを通じたClaude API

[パススルーエンドポイント](https://docs.litellm.ai/docs/pass_through/anthropic_completion)を使用：

```bash  theme={null}
export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic
```

##### LiteLLMを通じたAmazon Bedrock

[パススルーエンドポイント](https://docs.litellm.ai/docs/pass_through/bedrock)を使用：

```bash  theme={null}
export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
```

##### LiteLLMを通じたGoogle Vertex AI

[パススルーエンドポイント](https://docs.litellm.ai/docs/pass_through/vertex_ai)を使用：

```bash  theme={null}
export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
```

### モデル選択

デフォルトでは、モデルは[モデル設定](/ja/third-party-integrations#model-configuration)で指定されたものを使用します。

LiteLLMでカスタムモデル名を設定した場合は、前述の環境変数をそれらのカスタム名に設定してください。

詳細については、[LiteLLMドキュメント](https://docs.litellm.ai/)を参照してください。

## 追加リソース

* [LiteLLMドキュメント](https://docs.litellm.ai/)
* [Claude Code設定](/ja/settings)
* [エンタープライズネットワーク設定](/ja/network-config)
* [サードパーティ統合の概要](/ja/third-party-integrations)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt