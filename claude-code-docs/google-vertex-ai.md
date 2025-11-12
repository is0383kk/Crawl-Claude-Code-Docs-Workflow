# Google Vertex AI上のClaude Code

> Google Vertex AIを通じたClaude Codeの設定方法について学びます。セットアップ、IAM設定、トラブルシューティングを含みます。

## 前提条件

Vertex AIでClaude Codeを設定する前に、以下を確認してください：

* 請求が有効になっているGoogle Cloud Platform（GCP）アカウント
* Vertex AI APIが有効になっているGCPプロジェクト
* 目的のClaudeモデルへのアクセス（例：Claude Sonnet 4.5）
* Google Cloud SDK（`gcloud`）がインストールおよび設定されていること
* 目的のGCPリージョンに割り当てられたクォータ

## リージョン設定

Claude CodeはVertex AI [グローバル](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai)とリージョナルエンドポイントの両方で使用できます。

<Note>
  Vertex AIは、すべてのリージョンでClaude Codeのデフォルトモデルをサポートしていない場合があります。[サポートされているリージョンまたはモデル](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#genai-partner-models)に切り替える必要がある場合があります。
</Note>

<Note>
  Vertex AIは、グローバルエンドポイントでClaude Codeのデフォルトモデルをサポートしていない場合があります。リージョナルエンドポイントまたは[サポートされているモデル](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#supported_models)に切り替える必要がある場合があります。
</Note>

## セットアップ

### 1. Vertex AI APIを有効にする

GCPプロジェクトでVertex AI APIを有効にします：

```bash  theme={null}
# プロジェクトIDを設定
gcloud config set project YOUR-PROJECT-ID

# Vertex AI APIを有効にする
gcloud services enable aiplatform.googleapis.com
```

### 2. モデルアクセスをリクエストする

Vertex AIでClaudeモデルへのアクセスをリクエストします：

1. [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)に移動します
2. 「Claude」モデルを検索します
3. 目的のClaudeモデル（例：Claude Sonnet 4.5）へのアクセスをリクエストします
4. 承認を待ちます（24～48時間かかる場合があります）

### 3. GCP認証情報を設定する

Claude Codeは標準的なGoogle Cloud認証を使用します。

詳細については、[Google Cloud認証ドキュメント](https://cloud.google.com/docs/authentication)を参照してください。

<Note>
  認証時に、Claude Codeは`ANTHROPIC_VERTEX_PROJECT_ID`環境変数からプロジェクトIDを自動的に使用します。これをオーバーライドするには、`GCLOUD_PROJECT`、`GOOGLE_CLOUD_PROJECT`、または`GOOGLE_APPLICATION_CREDENTIALS`のいずれかの環境変数を設定します。
</Note>

### 4. Claude Codeを設定する

以下の環境変数を設定します：

```bash  theme={null}
# Vertex AI統合を有効にする
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=global
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# オプション：必要に応じてプロンプトキャッシングを無効にする
export DISABLE_PROMPT_CACHING=1

# CLOUD_ML_REGION=globalの場合、サポートされていないモデルのリージョンをオーバーライドする
export VERTEX_REGION_CLAUDE_3_5_HAIKU=us-east5

# オプション：他の特定のモデルのリージョンをオーバーライドする
export VERTEX_REGION_CLAUDE_3_5_SONNET=us-east5
export VERTEX_REGION_CLAUDE_3_7_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_0_OPUS=europe-west1
export VERTEX_REGION_CLAUDE_4_0_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_1_OPUS=europe-west1
```

<Note>
  [プロンプトキャッシング](https://docs.claude.com/ja/docs/build-with-claude/prompt-caching)は、`cache_control`エフェメラルフラグを指定すると自動的にサポートされます。これを無効にするには、`DISABLE_PROMPT_CACHING=1`を設定します。レート制限を高くするには、Google Cloudサポートに連絡してください。
</Note>

<Note>
  Vertex AIを使用する場合、Google Cloud認証情報を通じて認証が処理されるため、`/login`および`/logout`コマンドは無効になります。
</Note>

### 5. モデル設定

Claude CodeはVertex AIに対して以下のデフォルトモデルを使用します：

| モデルタイプ   | デフォルト値                       |
| :------- | :--------------------------- |
| プライマリモデル | `claude-sonnet-4-5@20250929` |
| 小型/高速モデル | `claude-haiku-4-5@20251001`  |

<Note>
  Vertex AIユーザーの場合、Claude CodeはHaiku 3.5からHaiku 4.5に自動的にアップグレードされません。新しいHaikuモデルに手動で切り替えるには、`ANTHROPIC_DEFAULT_HAIKU_MODEL`環境変数をフルモデル名に設定します（例：`claude-haiku-4-5@20251001`）。
</Note>

モデルをカスタマイズするには：

```bash  theme={null}
export ANTHROPIC_MODEL='claude-opus-4-1@20250805'
export ANTHROPIC_SMALL_FAST_MODEL='claude-haiku-4-5@20251001'
```

## IAM設定

必要なIAMパーミッションを割り当てます：

`roles/aiplatform.user`ロールには必要なパーミッションが含まれています：

* `aiplatform.endpoints.predict` - モデル呼び出しとトークンカウントに必要

より制限的なパーミッションの場合は、上記のパーミッションのみを持つカスタムロールを作成します。

詳細については、[Vertex IAMドキュメント](https://cloud.google.com/vertex-ai/docs/general/access-control)を参照してください。

<Note>
  コスト追跡とアクセス制御を簡素化するために、Claude Code用の専用GCPプロジェクトを作成することをお勧めします。
</Note>

## 1Mトークンコンテキストウィンドウ

Claude Sonnet 4およびSonnet 4.5は、Vertex AIで[1Mトークンコンテキストウィンドウ](https://docs.claude.com/ja/docs/build-with-claude/context-windows#1m-token-context-window)をサポートしています。

<Note>
  1Mトークンコンテキストウィンドウは現在ベータ版です。拡張コンテキストウィンドウを使用するには、Vertex AIリクエストに`context-1m-2025-08-07`ベータヘッダーを含めます。
</Note>

## トラブルシューティング

クォータの問題が発生した場合：

* [Cloud Console](https://cloud.google.com/docs/quotas/view-manage)を通じて現在のクォータを確認するか、クォータ増加をリクエストします

「モデルが見つかりません」404エラーが発生した場合：

* [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)でモデルが有効になっていることを確認します
* 指定されたリージョンへのアクセス権があることを確認します
* `CLOUD_ML_REGION=global`を使用している場合、[Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)の「サポートされている機能」でモデルがグローバルエンドポイントをサポートしていることを確認します。グローバルエンドポイントをサポートしていないモデルの場合は、以下のいずれかを実行します：
  * `ANTHROPIC_MODEL`または`ANTHROPIC_SMALL_FAST_MODEL`を通じてサポートされているモデルを指定するか、
  * `VERTEX_REGION_<MODEL_NAME>`環境変数を使用してリージョナルエンドポイントを設定します

429エラーが発生した場合：

* リージョナルエンドポイントの場合、プライマリモデルと小型/高速モデルが選択されたリージョンでサポートされていることを確認します
* より良い可用性のために`CLOUD_ML_REGION=global`への切り替えを検討します

## 追加リソース

* [Vertex AIドキュメント](https://cloud.google.com/vertex-ai/docs)
* [Vertex AI価格](https://cloud.google.com/vertex-ai/pricing)
* [Vertex AIクォータと制限](https://cloud.google.com/vertex-ai/docs/quotas)
