# エンタープライズネットワーク構成

> プロキシサーバー、カスタム認証局（CA）、および相互トランスポートレイヤーセキュリティ（mTLS）認証を使用して、エンタープライズ環境向けにClaude Codeを構成します。

Claude Codeは、環境変数を通じてさまざまなエンタープライズネットワークおよびセキュリティ構成をサポートしています。これには、企業プロキシサーバーを通じたトラフィックのルーティング、カスタム認証局（CA）の信頼、およびセキュリティ強化のための相互トランスポートレイヤーセキュリティ（mTLS）証明書による認証が含まれます。

<Note>
  このページに表示されているすべての環境変数は、[`settings.json`](/ja/settings)でも構成できます。
</Note>

## プロキシ構成

### 環境変数

Claude Codeは標準的なプロキシ環境変数に対応しています：

```bash  theme={null}
# HTTPSプロキシ（推奨）
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTPプロキシ（HTTPSが利用できない場合）
export HTTP_PROXY=http://proxy.example.com:8080

# 特定のリクエストのプロキシをバイパス - スペース区切り形式
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# 特定のリクエストのプロキシをバイパス - カンマ区切り形式
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# すべてのリクエストのプロキシをバイパス
export NO_PROXY="*"
```

<Note>
  Claude CodeはSOCKSプロキシをサポートしていません。
</Note>

### 基本認証

プロキシが基本認証を必要とする場合は、プロキシURLに認証情報を含めます：

```bash  theme={null}
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

<Warning>
  スクリプトにパスワードをハードコーディングすることは避けてください。代わりに環境変数またはセキュアな認証情報ストレージを使用してください。
</Warning>

<Tip>
  高度な認証（NTLM、Kerberosなど）が必要なプロキシの場合は、認証方法をサポートするLLMゲートウェイサービスの使用を検討してください。
</Tip>

## カスタムCA証明書

エンタープライズ環境がHTTPS接続用のカスタムCAを使用している場合（プロキシ経由であるか直接API アクセスであるかを問わず）、Claude Codeをそれらを信頼するように構成します：

```bash  theme={null}
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

## mTLS認証

クライアント証明書認証を必要とするエンタープライズ環境の場合：

```bash  theme={null}
# 認証用のクライアント証明書
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# クライアント秘密鍵
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# オプション：暗号化された秘密鍵のパスフレーズ
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```

## ネットワークアクセス要件

Claude Codeは以下のURLへのアクセスが必要です：

* `api.anthropic.com` - Claude APIエンドポイント
* `claude.ai` - WebFetchセーフガード
* `statsig.anthropic.com` - テレメトリーとメトリクス
* `sentry.io` - エラー報告

これらのURLがプロキシ構成とファイアウォールルールでホワイトリストに登録されていることを確認してください。これは、特にコンテナ化された環境または制限されたネットワーク環境でClaude Codeを使用する場合に重要です。

## 追加リソース

* [Claude Code設定](/ja/settings)
* [環境変数リファレンス](/ja/settings#environment-variables)
* [トラブルシューティングガイド](/ja/troubleshooting)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt