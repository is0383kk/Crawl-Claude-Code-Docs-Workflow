# データ使用

> Anthropicの Claude のデータ使用ポリシーについて学習します

## データポリシー

### データトレーニングポリシー

**コンシューマーユーザー（Free、Pro、Max プラン）**:
2025年8月28日から、将来の Claude モデルの改善に使用するためにデータを使用することを許可するかどうかを選択できるようになります。

この設定がオンの場合、Free、Pro、Max アカウントからのデータを使用して新しいモデルをトレーニングします（これらのアカウントから Claude Code を使用する場合を含む）。

* 現在のユーザーの場合、今すぐ設定を選択でき、選択は直ちに有効になります。
  この設定は Claude の新規または再開されたチャットおよびコーディングセッションにのみ適用されます。追加のアクティビティがない以前のチャットはモデルトレーニングに使用されません。
* 2025年10月8日までに選択を行う必要があります。
  新規ユーザーの場合、サインアップ処理中にモデルトレーニングの設定を選択できます。
  プライバシー設定でいつでも選択を変更できます。

**商用ユーザー**:（Team および Enterprise プラン、API、サードパーティプラットフォーム、Claude Gov）既存のポリシーを維持します：Anthropic は、顧客がモデル改善のためにデータを提供することを選択した場合を除き、商用条件下で Claude Code に送信されたコードまたはプロンプトを使用して生成モデルをトレーニングしません（例：[Developer Partner Program](https://support.claude.com/en/articles/11174108-about-the-development-partner-program)）。

### Development Partner Program

[Development Partner Program](https://support.claude.com/en/articles/11174108-about-the-development-partner-program) などを通じてトレーニング用の資料を提供する方法に明示的にオプトインした場合、提供された資料を使用してモデルをトレーニングする場合があります。組織管理者は、組織の Development Partner Program に明示的にオプトインできます。このプログラムは Anthropic ファーストパーティ API でのみ利用可能であり、Bedrock または Vertex ユーザーは利用できないことに注意してください。

### `/bug` コマンドを使用したフィードバック

`/bug` コマンドを使用して Claude Code に関するフィードバックを送信することを選択した場合、製品とサービスを改善するためにフィードバックを使用する場合があります。`/bug` を通じて共有されたトランスクリプトは5年間保持されます。

### セッション品質調査

Claude Code で「Claude はこのセッションでどのように機能していますか？」というプロンプトが表示される場合、この調査に応答する（「却下」を選択する場合を含む）と、数値評価（1、2、3、または却下）のみが記録されます。この調査の一部として、会話トランスクリプト、入力、出力、またはその他のセッションデータを収集または保存しません。サムズアップ/ダウンフィードバックまたは `/bug` レポートとは異なり、このセッション品質調査は単純な製品満足度メトリックです。この調査への応答は、データトレーニング設定に影響を与えず、AI モデルをトレーニングするために使用することはできません。

### データ保持

Anthropic は、アカウントタイプと設定に基づいて Claude Code データを保持します。

**コンシューマーユーザー（Free、Pro、Max プラン）**:

* モデル改善のためのデータ使用を許可するユーザー：モデル開発とセキュリティ改善をサポートするための5年間の保持期間
* モデル改善のためのデータ使用を許可しないユーザー：30日間の保持期間
* プライバシー設定は [claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls) でいつでも変更できます。

**商用ユーザー（Team、Enterprise、API）**:

* 標準：30日間の保持期間
* ゼロデータ保持：適切に構成された API キーで利用可能 - Claude Code はサーバーにチャットトランスクリプトを保持しません
* ローカルキャッシング：Claude Code クライアントはセッション再開を有効にするために最大30日間ローカルにセッションを保存できます（構成可能）

[Privacy Center](https://privacy.anthropic.com/) でデータ保持慣行の詳細を確認してください。

詳細については、[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms)（Team、Enterprise、API ユーザー向け）または [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)（Free、Pro、Max ユーザー向け）および [Privacy Policy](https://www.anthropic.com/legal/privacy) を確認してください。

## データフローと依存関係

<img src="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=4672f138596e864633b4b7c7ae4ae812" alt="Claude Code データフロー図" data-og-width="1597" width="1597" data-og-height="1285" height="1285" data-path="images/claude-code-data-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=280&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=5d9bdaf7ea50fc38dc01bbde7b952835 280w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=560&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=525736e5860ac9f262de4b40c9c68a0e 560w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=840&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=5262f9d1a1d0cffb0d5944e49b2d72be 840w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=1100&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=ec74e6b2f87b667f6d0e2278c20944de 1100w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=1650&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=05f11b1d061b6ddbb69969d4e535547a 1650w, https://mintcdn.com/claude-code/-YhHHmtSxwr7W8gy/images/claude-code-data-flow.png?w=2500&fit=max&auto=format&n=-YhHHmtSxwr7W8gy&q=85&s=9b9cce0fb5989bd1d27f143825be73ff 2500w" />

Claude Code は [NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code) からインストールされます。Claude Code はローカルで実行されます。LLM と相互作用するために、Claude Code はネットワーク経由でデータを送信します。このデータには、すべてのユーザープロンプトとモデル出力が含まれます。データは転送中に TLS で暗号化され、保存時には暗号化されません。Claude Code はほとんどの一般的な VPN および LLM プロキシと互換性があります。

Claude Code は Anthropic の API 上に構築されています。API のセキュリティ制御（API ロギング手順を含む）に関する詳細については、[Anthropic Trust Center](https://trust.anthropic.com) で提供されるコンプライアンスアーティファクトを参照してください。

### クラウド実行

<Note>
  上記のデータフロー図と説明は、マシンでローカルに実行されている Claude Code CLI に適用されます。Web 上の Claude Code を使用したクラウドベースのセッションについては、以下のセクションを参照してください。
</Note>

[Web 上の Claude Code](/ja/claude-code-on-the-web) を使用する場合、セッションはローカルではなく Anthropic 管理の仮想マシンで実行されます。クラウド環境では：

* **コードストレージ**：リポジトリは分離された VM にクローンされ、セッション完了後に自動的に削除されます
* **認証情報**：GitHub 認証はセキュアプロキシを通じて処理されます。GitHub 認証情報はサンドボックスに入りません
* **ネットワークトラフィック**：すべてのアウトバウンドトラフィックはセキュリティプロキシを通じて監査ログと不正使用防止のために送信されます
* **データ保持**：コードとセッションデータはアカウントタイプの保持および使用ポリシーに従います
* **セッションデータ**：プロンプト、コード変更、出力はローカル Claude Code 使用と同じデータポリシーに従います

クラウド実行のセキュリティ詳細については、[Security](/ja/security#cloud-execution-security) を参照してください。

## テレメトリサービス

Claude Code はユーザーのマシンから Statsig サービスに接続して、レイテンシ、信頼性、使用パターンなどの運用メトリックをログに記録します。このログには、コードまたはファイルパスは含まれません。データは転送中に TLS を使用して暗号化され、保存時に 256 ビット AES 暗号化を使用して暗号化されます。[Statsig セキュリティドキュメント](https://www.statsig.com/trust/security) で詳細を確認してください。Statsig テレメトリをオプトアウトするには、`DISABLE_TELEMETRY` 環境変数を設定してください。

Claude Code はユーザーのマシンから Sentry に接続して、運用エラーログを記録します。データは転送中に TLS を使用して暗号化され、保存時に 256 ビット AES 暗号化を使用して暗号化されます。[Sentry セキュリティドキュメント](https://sentry.io/security/) で詳細を確認してください。エラーログをオプトアウトするには、`DISABLE_ERROR_REPORTING` 環境変数を設定してください。

ユーザーが `/bug` コマンドを実行すると、コードを含む完全な会話履歴のコピーが Anthropic に送信されます。データは転送中および保存時に暗号化されます。オプションで、GitHub の公開リポジトリに GitHub の問題が作成されます。バグレポートをオプトアウトするには、`DISABLE_BUG_COMMAND` 環境変数を設定してください。

## API プロバイダー別のデフォルト動作

デフォルトでは、Bedrock または Vertex を使用する場合、すべての非必須トラフィック（エラーレポート、テレメトリ、バグレポート機能を含む）を無効にします。`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` 環境変数を設定することで、これらすべてを一度にオプトアウトすることもできます。完全なデフォルト動作は以下の通りです：

| サービス                        | Claude API                                         | Vertex API                                             | Bedrock API                                             |
| --------------------------- | -------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------- |
| **Statsig（メトリック）**          | デフォルトオン。<br />`DISABLE_TELEMETRY=1` で無効にします。       | デフォルトオフ。<br />`CLAUDE_CODE_USE_VERTEX` は 1 である必要があります。 | デフォルトオフ。<br />`CLAUDE_CODE_USE_BEDROCK` は 1 である必要があります。 |
| **Sentry（エラー）**             | デフォルトオン。<br />`DISABLE_ERROR_REPORTING=1` で無効にします。 | デフォルトオフ。<br />`CLAUDE_CODE_USE_VERTEX` は 1 である必要があります。 | デフォルトオフ。<br />`CLAUDE_CODE_USE_BEDROCK` は 1 である必要があります。 |
| **Claude API（`/bug` レポート）** | デフォルトオン。<br />`DISABLE_BUG_COMMAND=1` で無効にします。     | デフォルトオフ。<br />`CLAUDE_CODE_USE_VERTEX` は 1 である必要があります。 | デフォルトオフ。<br />`CLAUDE_CODE_USE_BEDROCK` は 1 である必要があります。 |

すべての環境変数は `settings.json` にチェックインできます（[詳細を確認](/ja/settings)）。


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt