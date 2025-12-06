# Claude Code のセットアップ

> 開発マシンに Claude Code をインストール、認証し、使用を開始します。

## システム要件

* **オペレーティングシステム**: macOS 10.15+、Ubuntu 20.04+/Debian 10+、または Windows 10+（WSL 1、WSL 2、または Git for Windows を使用）
* **ハードウェア**: 4GB 以上の RAM
* **ソフトウェア**: [Node.js 18+](https://nodejs.org/en/download)（NPM インストールの場合のみ必須）
* **ネットワーク**: 認証と AI 処理に必要なインターネット接続
* **シェル**: Bash、Zsh、Fish で最適に動作
* **場所**: [Anthropic がサポートしている国](https://www.anthropic.com/supported-countries)

### 追加の依存関係

* **ripgrep**: 通常は Claude Code に含まれています。検索機能が失敗する場合は、[検索のトラブルシューティング](/ja/troubleshooting#search-and-discovery-issues)を参照してください。

## 標準インストール

To install Claude Code, use one of the following methods:

<Tabs>
  <Tab title="Native Install (Recommended)">
    **Homebrew (macOS, Linux):**

    ```sh  theme={null}
    brew install --cask claude-code
    ```

    **macOS, Linux, WSL:**

    ```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Windows PowerShell:**

    ```powershell  theme={null}
    irm https://claude.ai/install.ps1 | iex
    ```

    **Windows CMD:**

    ```batch  theme={null}
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```
  </Tab>

  <Tab title="NPM">
    If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):

    ```sh  theme={null}
    npm install -g @anthropic-ai/claude-code
    ```
  </Tab>
</Tabs>

<Note>
  一部のユーザーは改善されたインストール方法に自動的に移行される場合があります。
</Note>

インストールプロセスが完了した後、プロジェクトに移動して Claude Code を起動します：

```bash  theme={null}
cd your-awesome-project
claude
```

Claude Code は以下の認証オプションを提供しています：

1. **Claude Console**: デフォルトオプション。Claude Console を通じて接続し、OAuth プロセスを完了します。[console.anthropic.com](https://console.anthropic.com) でのアクティブな課金が必要です。「Claude Code」ワークスペースが使用状況の追跡とコスト管理のために自動的に作成されます。Claude Code ワークスペース用の API キーを作成することはできません。これは Claude Code の使用専用です。
2. **Claude App（Pro または Max プラン付き）**: Claude の [Pro または Max プラン](https://claude.com/pricing)にサブスクライブして、Claude Code とウェブインターフェースの両方を含む統一されたサブスクリプションを取得します。同じ価格ポイントでより多くの価値を得ながら、1 か所でアカウントを管理します。Claude.ai アカウントでログインします。起動時に、サブスクリプションタイプに一致するオプションを選択します。
3. **エンタープライズプラットフォーム**: 既存のクラウドインフラストラクチャを使用したエンタープライズデプロイメント用に、Claude Code を [Amazon Bedrock または Google Vertex AI](/ja/third-party-integrations) を使用するように構成します。

<Note>
  Claude Code は認証情報を安全に保存します。詳細については、[認証情報管理](/ja/iam#credential-management)を参照してください。
</Note>

## Windows セットアップ

**オプション 1: WSL 内の Claude Code**

* WSL 1 と WSL 2 の両方がサポートされています

**オプション 2: Git Bash を使用したネイティブ Windows 上の Claude Code**

* [Git for Windows](https://git-scm.com/downloads/win) が必要です
* ポータブル Git インストールの場合、`bash.exe` へのパスを指定します：
  ```powershell  theme={null}
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  ```

## 代替インストール方法

Claude Code は異なる環境に対応するための複数のインストール方法を提供しています。

インストール中に問題が発生した場合は、[トラブルシューティングガイド](/ja/troubleshooting#linux-permission-issues)を参照してください。

<Tip>
  インストール後に `claude doctor` を実行して、インストールタイプとバージョンを確認します。
</Tip>

### ネイティブインストールオプション

ネイティブインストールは推奨される方法であり、いくつかの利点があります：

* 1 つの自己完結型実行可能ファイル
* Node.js の依存関係なし
* 改善された自動更新プログラムの安定性

Claude Code の既存のインストールがある場合は、`claude install` を使用してネイティブバイナリインストールに移行します。

ネイティブインストーラーを使用した高度なインストールオプションの場合：

**macOS、Linux、WSL:**

```bash  theme={null}
# 安定版をインストール（デフォルト）
curl -fsSL https://claude.ai/install.sh | bash

# 最新版をインストール
curl -fsSL https://claude.ai/install.sh | bash -s latest

# 特定のバージョン番号をインストール
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

<Note>
  **Alpine Linux およびその他の musl/uClibc ベースのディストリビューション**: ネイティブビルドでは、`libgcc`、`libstdc++`、および `ripgrep` をインストールする必要があります。インストール（Alpine: `apk add libgcc libstdc++ ripgrep`）し、`USE_BUILTIN_RIPGREP=0` を設定します。
</Note>

<Note>
  Homebrew 経由でインストールされた Claude Code は、`DISABLE_AUTOUPDATER` 環境変数で明示的に無効にされない限り、brew ディレクトリの外で自動更新されます（[自動更新](#auto-updates)セクションを参照）。
</Note>

**Windows PowerShell:**

```powershell  theme={null}
# 安定版をインストール（デフォルト）
irm https://claude.ai/install.ps1 | iex

# 最新版をインストール
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest

# 特定のバージョン番号をインストール
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
```

**Windows CMD:**

```batch  theme={null}
REM 安定版をインストール（デフォルト）
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

REM 最新版をインストール
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd latest && del install.cmd

REM 特定のバージョン番号をインストール
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
```

<Tip>
  インストール前に、古いエイリアスまたはシンボリックリンクを削除してください。
</Tip>

### NPM インストール

NPM が推奨または必須の環境の場合：

```sh  theme={null}
npm install -g @anthropic-ai/claude-code
```

<Warning>
  `sudo npm install -g` を使用しないでください。これはパーミッション問題とセキュリティリスクにつながる可能性があります。
  パーミッションエラーが発生した場合は、[Claude Code の構成](/ja/troubleshooting#linux-permission-issues)で推奨されるソリューションを参照してください。
</Warning>

## AWS または GCP で実行

デフォルトでは、Claude Code は Claude API を使用します。

AWS または GCP で Claude Code を実行する方法の詳細については、[サードパーティ統合](/ja/third-party-integrations)を参照してください。

## Claude Code を更新

### 自動更新

Claude Code は最新の機能とセキュリティ修正を確保するために、自動的に自身を最新の状態に保ちます。

* **更新チェック**: 起動時と実行中に定期的に実行されます
* **更新プロセス**: バックグラウンドで自動的にダウンロードおよびインストールされます
* **通知**: 更新がインストールされたときに通知が表示されます
* **更新の適用**: 更新は Claude Code を次に起動したときに有効になります

**自動更新を無効にする:**

シェルまたは [settings.json ファイル](/ja/settings)で `DISABLE_AUTOUPDATER` 環境変数を設定します：

```bash  theme={null}
export DISABLE_AUTOUPDATER=1
```

### 手動で更新

```bash  theme={null}
claude update
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt