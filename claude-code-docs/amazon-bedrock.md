# Amazon Bedrock上のClaude Code

> Amazon Bedrockを通じたClaude Codeの設定、セットアップ、IAM設定、トラブルシューティングについて学びます。

## 前提条件

Bedrockを使用してClaude Codeを設定する前に、以下を確認してください：

* Bedrockアクセスが有効になっているAWSアカウント
* Bedrock内の目的のClaudeモデル（例：Claude Sonnet 4.5）へのアクセス
* AWS CLIがインストールおよび設定されている（オプション - 認証情報を取得する別のメカニズムがない場合のみ必要）
* 適切なIAMパーミッション

## セットアップ

### 1. ユースケースの詳細を送信

Anthropicモデルの初回ユーザーは、モデルを呼び出す前にユースケースの詳細を送信する必要があります。これはアカウントごとに1回行われます。

1. 適切なIAMパーミッションがあることを確認してください（以下を参照）
2. [Amazon Bedrockコンソール](https://console.aws.amazon.com/bedrock/)に移動します
3. **Chat/Text playground**を選択します
4. Anthropicモデルを選択すると、ユースケースフォームに入力するよう求められます

### 2. AWS認証情報を設定

Claude Codeはデフォルトの AWS SDK認証情報チェーンを使用します。以下のいずれかの方法を使用して認証情報を設定します：

**オプションA：AWS CLI設定**

```bash  theme={null}
aws configure
```

**オプションB：環境変数（アクセスキー）**

```bash  theme={null}
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```

**オプションC：環境変数（SSOプロファイル）**

```bash  theme={null}
aws sso login --profile=<your-profile-name>

export AWS_PROFILE=your-profile-name
```

**オプションD：Bedrock APIキー**

```bash  theme={null}
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key
```

Bedrock APIキーは、完全なAWS認証情報を必要としない、より簡単な認証方法を提供します。[Bedrock APIキーについて詳しく学ぶ](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/)。

#### 高度な認証情報設定

Claude Codeは、AWS SSOおよび企業IDプロバイダーの自動認証情報更新をサポートしています。これらの設定をClaude Codeの設定ファイルに追加します（ファイルの場所については[設定](/ja/settings)を参照）。

Claude Codeが AWS認証情報の有効期限が切れていることを検出した場合（ローカルのタイムスタンプに基づくか、Bedrockが認証情報エラーを返した場合）、設定された`awsAuthRefresh`および/または`awsCredentialExport`コマンドを自動的に実行して、リクエストを再試行する前に新しい認証情報を取得します。

##### 設定例

```json  theme={null}
{
  "awsAuthRefresh": "aws sso login --profile myprofile",
  "env": {
    "AWS_PROFILE": "myprofile"
  }
}
```

##### 設定の説明

**`awsAuthRefresh`**：`.aws`ディレクトリを変更するコマンド（例：認証情報、SSOキャッシュ、または設定ファイルの更新）に使用します。出力はユーザーに表示されます（ただしユーザー入力はサポートされていません）。CLIがブラウザに入力するコードを表示するブラウザベースの認証フローに適しています。

**`awsCredentialExport`**：`.aws`を変更できず、認証情報を直接返す必要がある場合にのみ使用します。出力は静かにキャプチャされます（ユーザーに表示されません）。コマンドは次の形式でJSONを出力する必要があります：

```json  theme={null}
{
  "Credentials": {
    "AccessKeyId": "value",
    "SecretAccessKey": "value",
    "SessionToken": "value"
  }
}
```

### 3. Claude Codeを設定

Bedrockを有効にするには、以下の環境変数を設定します：

```bash  theme={null}
# Bedrock統合を有効にする
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1  # または希望するリージョン

# オプション：小型/高速モデル（Haiku）のリージョンをオーバーライド
export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION=us-west-2
```

Claude CodeのBedrockを有効にする場合、以下に注意してください：

* `AWS_REGION`は必須の環境変数です。Claude Codeはこの設定について`.aws`設定ファイルから読み込みません。
* Bedrockを使用する場合、`/login`および`/logout`コマンドは無効になります。認証はAWS認証情報を通じて処理されるためです。
* 他のプロセスに漏らしたくない`AWS_PROFILE`などの環境変数に対して、設定ファイルを使用できます。詳細については[設定](/ja/settings)を参照してください。

### 4. モデル設定

Claude CodeはBedrockに対してこれらのデフォルトモデルを使用します：

| モデルタイプ   | デフォルト値                                             |
| :------- | :------------------------------------------------- |
| プライマリモデル | `global.anthropic.claude-sonnet-4-5-20250929-v1:0` |
| 小型/高速モデル | `us.anthropic.claude-haiku-4-5-20251001-v1:0`      |

<Note>
  Bedrockユーザーの場合、Claude CodeはHaiku 3.5からHaiku 4.5に自動的にアップグレードされません。新しいHaikuモデルに手動で切り替えるには、`ANTHROPIC_DEFAULT_HAIKU_MODEL`環境変数をフルモデル名に設定します（例：`us.anthropic.claude-haiku-4-5-20251001-v1:0`）。
</Note>

モデルをカスタマイズするには、以下のいずれかの方法を使用します：

```bash  theme={null}
# 推論プロファイルIDを使用
export ANTHROPIC_MODEL='global.anthropic.claude-sonnet-4-5-20250929-v1:0'
export ANTHROPIC_SMALL_FAST_MODEL='us.anthropic.claude-haiku-4-5-20251001-v1:0'

# アプリケーション推論プロファイルARNを使用
export ANTHROPIC_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-model-id'

# オプション：必要に応じてプロンプトキャッシングを無効にする
export DISABLE_PROMPT_CACHING=1
```

<Note>
  [プロンプトキャッシング](https://docs.claude.com/ja/docs/build-with-claude/prompt-caching)はすべてのリージョンで利用できない場合があります
</Note>

### 5. 出力トークン設定

Amazon BedrockでClaude Codeを使用する場合、以下のトークン設定をお勧めします：

```bash  theme={null}
# Bedrockの推奨出力トークン設定
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
export MAX_THINKING_TOKENS=1024
```

**これらの値の理由：**

* **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096`**：Bedrockのバーンダウンスロットリングロジックは、max\_tokenペナルティの最小値として4096トークンを設定します。これを低く設定してもコストは削減されませんが、長いツール使用を切り落とし、Claude Codeエージェントループが永続的に失敗する可能性があります。Claude Codeは通常、拡張思考なしで4096出力トークン未満を使用しますが、重要なファイル作成またはWriteツール使用を含むタスクにはこのヘッドルームが必要な場合があります。

* **`MAX_THINKING_TOKENS=1024`**：これは、ツール使用応答を切り落とさずに拡張思考のためのスペースを提供しながら、焦点を絞った推論チェーンを維持します。このバランスは、特にコーディングタスクに対して常に有用とは限らない軌跡の変更を防ぐのに役立ちます。

## IAM設定

Claude Codeに必要なパーミッションを持つIAMポリシーを作成します：

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowModelAndInferenceProfileAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListInferenceProfiles"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*:*:application-inference-profile/*",
        "arn:aws:bedrock:*:*:foundation-model/*"
      ]
    },
    {
      "Sid": "AllowMarketplaceSubscription",
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:ViewSubscriptions",
        "aws-marketplace:Subscribe"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:CalledViaLast": "bedrock.amazonaws.com"
        }
      }
    }
  ]
}
```

より制限的なパーミッションの場合、リソースを特定の推論プロファイルARNに制限できます。

詳細については、[Bedrock IAMドキュメント](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)を参照してください。

<Note>
  コスト追跡とアクセス制御を簡素化するために、Claude Code用に専用のAWSアカウントを作成することをお勧めします。
</Note>

## トラブルシューティング

リージョンの問題が発生した場合：

* モデルの可用性を確認：`aws bedrock list-inference-profiles --region your-region`
* サポートされているリージョンに切り替え：`export AWS_REGION=us-east-1`
* クロスリージョンアクセスのために推論プロファイルの使用を検討してください

「オンデマンドスループットはサポートされていません」というエラーが表示される場合：

* モデルを[推論プロファイル](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)IDとして指定します

Claude CodeはBedrock [Invoke API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)を使用し、Converse APIはサポートしていません。

## 追加リソース

* [Bedrockドキュメント](https://docs.aws.amazon.com/bedrock/)
* [Bedrockの価格](https://aws.amazon.com/bedrock/pricing/)
* [Bedrock推論プロファイル](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
* [Amazon Bedrock上のClaude Code：クイックセットアップガイド](https://community.aws/content/2tXkZKrZzlrlu0KfH8gST5Dkppq/claude-code-on-amazon-bedrock-quick-setup-guide)
* [Claude Codeモニタリング実装（Bedrock）](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/MONITORING.md)
