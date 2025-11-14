# Claude Code GitHub Actions

> Claude Code GitHub Actionsを開発ワークフローに統合する方法について学びます

Claude Code GitHub Actionsは、GitHub ワークフローにAI駆動の自動化をもたらします。任意のPRまたはissueで`@claude`と言及するだけで、Claudeはコードを分析し、プルリクエストを作成し、機能を実装し、バグを修正できます。すべてプロジェクトの標準に従いながら。

<Note>
  Claude Code GitHub Actionsは[Claude Code SDK](/ja/sdk)の上に構築されており、Claude Codeのプログラマティック統合をアプリケーションに有効にします。SDKを使用して、GitHub Actions以外のカスタム自動化ワークフローを構築できます。
</Note>

## Claude Code GitHub Actionsを使用する理由は何ですか？

* **インスタントPR作成**: 必要なものを説明すると、Claudeは必要なすべての変更を含む完全なPRを作成します
* **自動コード実装**: issueを単一のコマンドで動作するコードに変換します
* **標準に従う**: Claudeは`CLAUDE.md`ガイドラインと既存のコードパターンを尊重します
* **シンプルなセットアップ**: インストーラーとAPIキーで数分で開始できます
* **デフォルトで安全**: コードはGithubのランナーに留まります

## Claudeは何ができますか？

Claude Codeは、コードの操作方法を変える強力なGitHub Actionを提供します：

### Claude Code Action

このGitHub Actionにより、GitHub Actionsワークフロー内でClaude Codeを実行できます。これを使用して、Claude Code上に任意のカスタムワークフローを構築できます。

[リポジトリを表示 →](https://github.com/anthropics/claude-code-action)

## セットアップ

## クイックセットアップ

このアクションをセットアップする最も簡単な方法は、ターミナルのClaude Codeを使用することです。claudeを開いて`/install-github-app`を実行するだけです。

このコマンドは、GitHubアプリと必要なシークレットのセットアップをガイドします。

<Note>
  * GitHubアプリをインストールしてシークレットを追加するには、リポジトリ管理者である必要があります
  * GitHubアプリは、Contents、Issues、およびPull requestsの読み取り＆書き込み権限をリクエストします
  * このクイックスタート方法は、直接Claude APIユーザーのみが利用できます。AWS BedrocまたはGoogle Vertex AIを使用している場合は、[AWS Bedrock＆Google Vertex AIで使用する](#using-with-aws-bedrock-%26-google-vertex-ai)セクションを参照してください。
</Note>

## 手動セットアップ

`/install-github-app`コマンドが失敗した場合、または手動セットアップを希望する場合は、以下の手動セットアップ手順に従ってください：

1. **Claude GitHubアプリをリポジトリにインストール**: [https://github.com/apps/claude](https://github.com/apps/claude)

   Claude GitHubアプリには、以下のリポジトリ権限が必要です：

   * **Contents**: 読み取り＆書き込み（リポジトリファイルを変更するため）
   * **Issues**: 読み取り＆書き込み（issueに応答するため）
   * **Pull requests**: 読み取り＆書き込み（PRを作成して変更をプッシュするため）

   セキュリティと権限の詳細については、[セキュリティドキュメント](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)を参照してください。
2. **ANTHROPIC\_API\_KEYをリポジトリシークレットに追加** ([GitHub Actionsでシークレットを使用する方法を学ぶ](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions))
3. **ワークフローファイルをコピー** [examples/claude.yml](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml)からリポジトリの`.github/workflows/`へ

<Tip>
  クイックスタートまたは手動セットアップのいずれかを完了した後、issueまたはPRコメントで`@claude`をタグ付けしてアクションをテストしてください！
</Tip>

## ベータ版からのアップグレード

<Warning>
  Claude Code GitHub Actions v1.0は、ベータ版からv1.0にアップグレードするためにワークフローファイルを更新する必要がある破壊的な変更を導入します。
</Warning>

現在Claude Code GitHub Actionsのベータ版を使用している場合は、ワークフローをGA版を使用するように更新することをお勧めします。新しいバージョンは、自動モード検出などの強力な新機能を追加しながら、設定を簡素化します。

### 重要な変更

すべてのベータユーザーは、アップグレードするためにワークフローファイルに以下の変更を加える必要があります：

1. **アクションバージョンを更新**: `@beta`を`@v1`に変更
2. **モード設定を削除**: `mode: "tag"`または`mode: "agent"`を削除（現在は自動検出）
3. **プロンプト入力を更新**: `direct_prompt`を`prompt`に置き換え
4. **CLIオプションを移動**: `max_turns`、`model`、`custom_instructions`などを`claude_args`に変換

### 破壊的な変更リファレンス

| 古いベータ入力               | 新しいv1.0入力                        |
| --------------------- | -------------------------------- |
| `mode`                | *(削除 - 自動検出)*                    |
| `direct_prompt`       | `prompt`                         |
| `override_prompt`     | `prompt`（GitHubの変数付き）            |
| `custom_instructions` | `claude_args: --system-prompt`   |
| `max_turns`           | `claude_args: --max-turns`       |
| `model`               | `claude_args: --model`           |
| `allowed_tools`       | `claude_args: --allowedTools`    |
| `disallowed_tools`    | `claude_args: --disallowedTools` |
| `claude_env`          | `settings` JSON形式                |

### ビフォー・アフター例

**ベータ版:**

```yaml  theme={null}
- uses: anthropics/claude-code-action@beta
  with:
    mode: "tag"
    direct_prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    custom_instructions: "Follow our coding standards"
    max_turns: "10"
    model: "claude-sonnet-4-5-20250929"
```

**GA版（v1.0）:**

```yaml  theme={null}
- uses: anthropics/claude-code-action@v1
  with:
    prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    claude_args: |
      --system-prompt "Follow our coding standards"
      --max-turns 10
      --model claude-sonnet-4-5-20250929
```

<Tip>
  アクションは、設定に基づいて、インタラクティブモード（`@claude`メンションに応答）または自動化モード（プロンプト付きで即座に実行）で実行するかどうかを自動的に検出します。
</Tip>

## ユースケース例

Claude Code GitHub Actionsは、さまざまなタスクに役立ちます。[examplesディレクトリ](https://github.com/anthropics/claude-code-action/tree/main/examples)には、異なるシナリオ用の使用可能なワークフローが含まれています。

### 基本的なワークフロー

```yaml  theme={null}
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # Responds to @claude mentions in comments
```

### スラッシュコマンドの使用

```yaml  theme={null}
name: Code Review
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "/review"
          claude_args: "--max-turns 5"
```

### プロンプトを使用したカスタム自動化

```yaml  theme={null}
name: Daily Report
on:
  schedule:
    - cron: "0 9 * * *"
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "Generate a summary of yesterday's commits and open issues"
          claude_args: "--model claude-opus-4-1-20250805"
```

### 一般的なユースケース

issueまたはPRコメント内：

```
@claude implement this feature based on the issue description
@claude how should I implement user authentication for this endpoint?
@claude fix the TypeError in the user dashboard component
```

Claudeは自動的にコンテキストを分析し、適切に応答します。

## ベストプラクティス

### CLAUDE.md設定

リポジトリルートに`CLAUDE.md`ファイルを作成して、コードスタイルガイドライン、レビュー基準、プロジェクト固有のルール、および推奨パターンを定義します。このファイルは、Claudeのプロジェクト標準の理解をガイドします。

### セキュリティに関する考慮事項

<Warning>APIキーをリポジトリに直接コミットしないでください！</Warning>

権限、認証、およびベストプラクティスを含む包括的なセキュリティガイダンスについては、[Claude Code Actionセキュリティドキュメント](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)を参照してください。

常にAPIキーにGitHub Secretsを使用してください：

* APIキーを`ANTHROPIC_API_KEY`という名前のリポジトリシークレットとして追加
* ワークフローで参照：`anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}`
* アクション権限を必要なものだけに制限
* マージ前にClaudeの提案を確認

ワークフローファイルにAPIキーを直接ハードコーディングするのではなく、常にGitHub Secrets（例：`${{ secrets.ANTHROPIC_API_KEY }}`）を使用してください。

### パフォーマンスの最適化

issueテンプレートを使用してコンテキストを提供し、`CLAUDE.md`を簡潔で焦点を絞ったものに保ち、ワークフローに適切なタイムアウトを設定します。

### CI コスト

Claude Code GitHub Actionsを使用する場合、関連するコストに注意してください：

**GitHub Actionsコスト：**

* Claude Codeはgithub ホストランナーで実行され、GitHub Actionsの分を消費します
* 詳細な価格設定と分の制限については、[GitHubの請求ドキュメント](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)を参照してください

**APIコスト：**

* 各Claude相互作用は、プロンプトと応答の長さに基づいてAPIトークンを消費します
* トークン使用量は、タスクの複雑さとコードベースのサイズによって異なります
* 現在のトークンレートについては、[Claudeの価格ページ](https://claude.com/platform/api)を参照してください

**コスト最適化のヒント：**

* 特定の`@claude`コマンドを使用して、不要なAPI呼び出しを減らします
* `claude_args`で適切な`--max-turns`を設定して、過度な反復を防ぎます
* ワークフローレベルのタイムアウトを設定して、暴走ジョブを回避します
* GitHubの同時実行制御を使用して、並列実行を制限することを検討してください

## 設定例

Claude Code Action v1は、統一されたパラメータで設定を簡素化します：

```yaml  theme={null}
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    prompt: "Your instructions here" # Optional
    claude_args: "--max-turns 5" # Optional CLI arguments
```

主な機能：

* **統一されたプロンプトインターフェース** - すべての指示に`prompt`を使用
* **スラッシュコマンド** - `/review`や`/fix`などの事前構築されたプロンプト
* **CLIパススルー** - `claude_args`経由のClaude Code CLIの任意の引数
* **柔軟なトリガー** - 任意のGitHubイベントで動作

完全なワークフローファイルについては、[examplesディレクトリ](https://github.com/anthropics/claude-code-action/tree/main/examples)を参照してください。

<Tip>
  issueまたはPRコメントに応答する場合、Claudeは自動的に@claudeメンションに応答します。その他のイベントの場合は、`prompt`パラメータを使用して指示を提供します。
</Tip>

## AWS Bedrock＆Google Vertex AIで使用する

エンタープライズ環境では、Claude Code GitHub Actionsを独自のクラウドインフラストラクチャで使用できます。このアプローチにより、データレジデンシーと請求を制御しながら、同じ機能を維持できます。

### 前提条件

クラウドプロバイダーでClaude Code GitHub Actionsをセットアップする前に、以下が必要です：

#### Google Cloud Vertex AIの場合：

1. Vertex AIが有効になっているGoogle Cloudプロジェクト
2. GitHub Actionsに設定されたWorkload Identity Federation
3. 必要な権限を持つサービスアカウント
4. GitHubアプリ（推奨）またはデフォルトのGITHUB\_TOKENを使用

#### AWS Bedrockの場合：

1. Amazon Bedrockが有効になっているAWSアカウント
2. AWSで設定されたGitHub OIDCアイデンティティプロバイダー
3. Bedrock権限を持つIAMロール
4. GitHubアプリ（推奨）またはデフォルトのGITHUB\_TOKENを使用

<Steps>
  <Step title="カスタムGitHubアプリを作成（3Pプロバイダーに推奨）">
    Vertex AIやBedrockなどの3Pプロバイダーを使用する場合、最適な制御とセキュリティのために、独自のGitHubアプリを作成することをお勧めします：

    1. [https://github.com/settings/apps/newにアクセス](https://github.com/settings/apps/newにアクセス)
    2. 基本情報を入力：
       * **GitHub App name**: 一意の名前を選択（例：「YourOrg Claude Assistant」）
       * **Homepage URL**: 組織のウェブサイトまたはリポジトリURL
    3. アプリ設定を設定：
       * **Webhooks**: 「Active」をチェック解除（この統合には不要）
    4. 必要な権限を設定：
       * **Repository permissions**:
         * Contents: Read & Write
         * Issues: Read & Write
         * Pull requests: Read & Write
    5. 「Create GitHub App」をクリック
    6. 作成後、「Generate a private key」をクリックしてダウンロードした`.pem`ファイルを保存
    7. アプリ設定ページからアプリIDをメモ
    8. アプリをリポジトリにインストール：
       * アプリの設定ページから、左側のサイドバーの「Install App」をクリック
       * アカウントまたは組織を選択
       * 「Only select repositories」を選択して特定のリポジトリを選択
       * 「Install」をクリック
    9. プライベートキーをリポジトリシークレットとして追加：
       * リポジトリの設定 → シークレットと変数 → アクションに移動
       * `.pem`ファイルの内容を含む`APP_PRIVATE_KEY`という名前の新しいシークレットを作成
    10. アプリIDをシークレットとして追加：

    * GitHubアプリのIDを含む`APP_ID`という名前の新しいシークレットを作成

    <Note>
      このアプリは、[actions/create-github-app-token](https://github.com/actions/create-github-app-token)アクションで使用され、ワークフロー内で認証トークンを生成します。
    </Note>

    **Claude APIの場合またはGithubアプリをセットアップしたくない場合の代替案**: 公式Anthropicアプリを使用：

    1. [https://github.com/apps/claudeからインストール](https://github.com/apps/claudeからインストール)
    2. 認証に追加の設定は不要
  </Step>

  <Step title="クラウドプロバイダー認証を設定">
    クラウドプロバイダーを選択し、安全な認証をセットアップ：

    <AccordionGroup>
      <Accordion title="AWS Bedrock">
        **認証情報を保存せずに、GitHub ActionsがAWSに安全に認証できるようにAWSを設定します。**

        > **セキュリティに関する注意**: リポジトリ固有の設定を使用し、最小限の必要な権限のみを付与します。

        **必要なセットアップ**:

        1. **Amazon Bedrockを有効化**:
           * Amazon Bedrockでのクラウドモデルへのアクセスをリクエスト
           * クロスリージョンモデルの場合、すべての必要なリージョンでアクセスをリクエスト

        2. **GitHub OIDCアイデンティティプロバイダーをセットアップ**:
           * プロバイダーURL: `https://token.actions.githubusercontent.com`
           * オーディエンス: `sts.amazonaws.com`

        3. **GitHub Actions用のIAMロールを作成**:
           * 信頼されたエンティティタイプ: Web identity
           * アイデンティティプロバイダー: `token.actions.githubusercontent.com`
           * 権限: `AmazonBedrockFullAccess`ポリシー
           * 特定のリポジトリの信頼ポリシーを設定

        **必要な値**:

        セットアップ後、以下が必要です：

        * **AWS\_ROLE\_TO\_ASSUME**: 作成したIAMロールのARN

        <Tip>
          OIDCは、認証情報が一時的で自動的にローテーションされるため、静的なAWSアクセスキーを使用するよりも安全です。
        </Tip>

        詳細なOIDCセットアップ手順については、[AWSドキュメント](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)を参照してください。
      </Accordion>

      <Accordion title="Google Vertex AI">
        **認証情報を保存せずに、GitHub ActionsがGoogle Cloudに安全に認証できるようにGoogle Cloudを設定します。**

        > **セキュリティに関する注意**: リポジトリ固有の設定を使用し、最小限の必要な権限のみを付与します。

        **必要なセットアップ**:

        1. **Google Cloudプロジェクトで APIを有効化**:
           * IAM Credentials API
           * Security Token Service (STS) API
           * Vertex AI API

        2. **Workload Identity Federationリソースを作成**:
           * Workload Identity Poolを作成
           * 以下を含むGitHub OIDCプロバイダーを追加：
             * Issuer: `https://token.actions.githubusercontent.com`
             * リポジトリと所有者の属性マッピング
             * **セキュリティ推奨**: リポジトリ固有の属性条件を使用

        3. **サービスアカウントを作成**:
           * `Vertex AI User`ロールのみを付与
           * **セキュリティ推奨**: リポジトリごとに専用のサービスアカウントを作成

        4. **IAMバインディングを設定**:
           * Workload Identity Poolがサービスアカウントをなりすまし可能にする
           * **セキュリティ推奨**: リポジトリ固有のプリンシパルセットを使用

        **必要な値**:

        セットアップ後、以下が必要です：

        * **GCP\_WORKLOAD\_IDENTITY\_PROVIDER**: 完全なプロバイダーリソース名
        * **GCP\_SERVICE\_ACCOUNT**: サービスアカウントのメールアドレス

        <Tip>
          Workload Identity Federationは、ダウンロード可能なサービスアカウントキーの必要性を排除し、セキュリティを向上させます。
        </Tip>

        詳細なセットアップ手順については、[Google Cloud Workload Identity Federationドキュメント](https://cloud.google.com/iam/docs/workload-identity-federation)を参照してください。
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="必要なシークレットを追加">
    リポジトリに以下のシークレットを追加（設定 → シークレットと変数 → アクション）：

    #### Claude API（直接）の場合：

    1. **API認証の場合**:
       * `ANTHROPIC_API_KEY`: [console.anthropic.com](https://console.anthropic.com)からのClaude APIキー

    2. **GitHubアプリの場合（独自のアプリを使用している場合）**:
       * `APP_ID`: GitHubアプリのID
       * `APP_PRIVATE_KEY`: プライベートキー（.pem）の内容

    #### Google Cloud Vertex AIの場合

    1. **GCP認証の場合**:
       * `GCP_WORKLOAD_IDENTITY_PROVIDER`
       * `GCP_SERVICE_ACCOUNT`

    2. **GitHubアプリの場合（独自のアプリを使用している場合）**:
       * `APP_ID`: GitHubアプリのID
       * `APP_PRIVATE_KEY`: プライベートキー（.pem）の内容

    #### AWS Bedrockの場合

    1. **AWS認証の場合**:
       * `AWS_ROLE_TO_ASSUME`

    2. **GitHubアプリの場合（独自のアプリを使用している場合）**:
       * `APP_ID`: GitHubアプリのID
       * `APP_PRIVATE_KEY`: プライベートキー（.pem）の内容
  </Step>

  <Step title="ワークフローファイルを作成">
    クラウドプロバイダーと統合するGitHub Actionsワークフローファイルを作成します。以下の例は、AWS BedrocとGoogle Vertex AIの両方の完全な設定を示しています：

    <AccordionGroup>
      <Accordion title="AWS Bedrockワークフロー">
        **前提条件：**

        * AWS Bedrockアクセスが有効で、Claudeモデルの権限がある
        * GitHubがAWSのOIDCアイデンティティプロバイダーとして設定されている
        * GitHub Actionsを信頼するBedrock権限を持つIAMロール

        **必要なGitHubシークレット：**

        | シークレット名              | 説明                      |
        | -------------------- | ----------------------- |
        | `AWS_ROLE_TO_ASSUME` | Bedrockアクセス用のIAMロールのARN |
        | `APP_ID`             | GitHubアプリID（アプリ設定から）    |
        | `APP_PRIVATE_KEY`    | GitHubアプリ用に生成したプライベートキー |

        ```yaml  theme={null}
        name: Claude PR Action

        permissions:
          contents: write
          pull-requests: write
          issues: write
          id-token: write

        on:
          issue_comment:
            types: [created]
          pull_request_review_comment:
            types: [created]
          issues:
            types: [opened, assigned]

        jobs:
          claude-pr:
            if: |
              (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
            runs-on: ubuntu-latest
            env:
              AWS_REGION: us-west-2
            steps:
              - name: Checkout repository
                uses: actions/checkout@v4

              - name: Generate GitHub App token
                id: app-token
                uses: actions/create-github-app-token@v2
                with:
                  app-id: ${{ secrets.APP_ID }}
                  private-key: ${{ secrets.APP_PRIVATE_KEY }}

              - name: Configure AWS Credentials (OIDC)
                uses: aws-actions/configure-aws-credentials@v4
                with:
                  role-to-assume: ${{ secrets.AWS_ROLE_TO_ASSUME }}
                  aws-region: us-west-2

              - uses: anthropics/claude-code-action@v1
                with:
                  github_token: ${{ steps.app-token.outputs.token }}
                  use_bedrock: "true"
                  claude_args: '--model us.anthropic.claude-sonnet-4-5-20250929-v1:0 --max-turns 10'
        ```

        <Tip>
          BedrockのモデルID形式には、リージョンプレフィックス（例：`us.anthropic.claude...`）とバージョンサフィックスが含まれます。
        </Tip>
      </Accordion>

      <Accordion title="Google Vertex AIワークフロー">
        **前提条件：**

        * GCPプロジェクトでVertex AI APIが有効
        * GitHubに設定されたWorkload Identity Federation
        * Vertex AI権限を持つサービスアカウント

        **必要なGitHubシークレット：**

        | シークレット名                          | 説明                              |
        | -------------------------------- | ------------------------------- |
        | `GCP_WORKLOAD_IDENTITY_PROVIDER` | Workload identity providerリソース名 |
        | `GCP_SERVICE_ACCOUNT`            | Vertex AIアクセス権を持つサービスアカウントメール   |
        | `APP_ID`                         | GitHubアプリID（アプリ設定から）            |
        | `APP_PRIVATE_KEY`                | GitHubアプリ用に生成したプライベートキー         |

        ```yaml  theme={null}
        name: Claude PR Action

        permissions:
          contents: write
          pull-requests: write
          issues: write
          id-token: write

        on:
          issue_comment:
            types: [created]
          pull_request_review_comment:
            types: [created]
          issues:
            types: [opened, assigned]

        jobs:
          claude-pr:
            if: |
              (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
              (github.event_name == 'issues' && contains(github.event.issue.body, '@claude'))
            runs-on: ubuntu-latest
            steps:
              - name: Checkout repository
                uses: actions/checkout@v4

              - name: Generate GitHub App token
                id: app-token
                uses: actions/create-github-app-token@v2
                with:
                  app-id: ${{ secrets.APP_ID }}
                  private-key: ${{ secrets.APP_PRIVATE_KEY }}

              - name: Authenticate to Google Cloud
                id: auth
                uses: google-github-actions/auth@v2
                with:
                  workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
                  service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

              - uses: anthropics/claude-code-action@v1
                with:
                  github_token: ${{ steps.app-token.outputs.token }}
                  trigger_phrase: "@claude"
                  use_vertex: "true"
                  claude_args: '--model claude-sonnet-4@20250514 --max-turns 10'
                env:
                  ANTHROPIC_VERTEX_PROJECT_ID: ${{ steps.auth.outputs.project_id }}
                  CLOUD_ML_REGION: us-east5
                  VERTEX_REGION_CLAUDE_3_7_SONNET: us-east5
        ```

        <Tip>
          プロジェクトIDはGoogle Cloud認証ステップから自動的に取得されるため、ハードコーディングする必要はありません。
        </Tip>
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>

## トラブルシューティング

### Claudeが@claudeコマンドに応答しない

GitHubアプリが正しくインストールされていることを確認し、ワークフローが有効になっていることを確認し、APIキーがリポジトリシークレットに設定されていることを確認し、コメントに`@claude`が含まれていることを確認します（`/claude`ではなく）。

### CIがClaudeのコミットで実行されない

GitHub Appまたはカスタムアプリを使用していることを確認（Actionsユーザーではなく）、ワークフロートリガーに必要なイベントが含まれていることを確認し、アプリ権限にCIトリガーが含まれていることを確認します。

### 認証エラー

APIキーが有効で十分な権限があることを確認します。Bedrock/Vertexの場合は、認証情報の設定を確認し、シークレットがワークフロー内で正しく名前付けされていることを確認します。

## 高度な設定

### アクションパラメータ

Claude Code Action v1は、簡素化された設定を使用します：

| パラメータ               | 説明                                 | 必須     |
| ------------------- | ---------------------------------- | ------ |
| `prompt`            | Claude用の指示（テキストまたはスラッシュコマンド）       | いいえ\*  |
| `claude_args`       | Claude Codeに渡されるCLI引数              | いいえ    |
| `anthropic_api_key` | Claude APIキー                       | はい\*\* |
| `github_token`      | API アクセス用のGitHubトークン               | いいえ    |
| `trigger_phrase`    | カスタムトリガーフレーズ（デフォルト：「@claude」）      | いいえ    |
| `use_bedrock`       | Claude APIの代わりにAWS Bedrockを使用      | いいえ    |
| `use_vertex`        | Claude APIの代わりにGoogle Vertex AIを使用 | いいえ    |

\*プロンプトはオプションです - issueまたはPRコメントで省略した場合、Claudeはトリガーフレーズに応答します\
\*\*直接Claude APIに必須、Bedrock/Vertexには不要

#### claude\_argsの使用

`claude_args`パラメータは、任意のClaude Code CLIの引数を受け入れます：

```yaml  theme={null}
claude_args: "--max-turns 5 --model claude-sonnet-4-5-20250929 --mcp-config /path/to/config.json"
```

一般的な引数：

* `--max-turns`: 最大会話ターン数（デフォルト：10）
* `--model`: 使用するモデル（例：`claude-sonnet-4-5-20250929`）
* `--mcp-config`: MCPの設定へのパス
* `--allowed-tools`: 許可されたツールのカンマ区切りリスト
* `--debug`: デバッグ出力を有効化

### 代替統合方法

`/install-github-app`コマンドが推奨されるアプローチですが、以下も可能です：

* **カスタムGitHubアプリ**: ブランド化されたユーザー名またはカスタム認証フローが必要な組織向け。必要な権限（contents、issues、pull requests）を持つ独自のGitHubアプリを作成し、actions/create-github-app-tokenアクションを使用してワークフロー内でトークンを生成します。
* **手動GitHub Actions**: 最大の柔軟性のための直接ワークフロー設定
* **MCP設定**: Model Context Protocolサーバーの動的読み込み

詳細なガイドについては、[Claude Code Actionドキュメント](https://github.com/anthropics/claude-code-action/blob/main/docs)を参照してください。認証、セキュリティ、および高度な設定に関する詳細ガイドがあります。

### Claudeの動作をカスタマイズ

Claudeの動作は2つの方法で設定できます：

1. **CLAUDE.md**: リポジトリのルートに`CLAUDE.md`ファイルを作成して、コーディング標準、レビュー基準、およびプロジェクト固有のルールを定義します。Claudeは、PRを作成してリクエストに応答する際に、これらのガイドラインに従います。詳細については、[メモリドキュメント](/ja/memory)を確認してください。
2. **カスタムプロンプト**: ワークフローファイルの`prompt`パラメータを使用して、ワークフロー固有の指示を提供します。これにより、異なるワークフローまたはタスク用にClaudeの動作をカスタマイズできます。

Claudeは、PRを作成してリクエストに応答する際に、これらのガイドラインに従います。
