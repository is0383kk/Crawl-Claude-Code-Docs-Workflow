# ウェブ上の Claude Code

> セキュアなクラウドインフラストラクチャ上で Claude Code タスクを非同期に実行します

<Note>
  Claude Code on the web は現在リサーチプレビュー中です。
</Note>

## Claude Code on the web とは何ですか？

Claude Code on the web により、開発者は Claude アプリから Claude Code を開始できます。これは以下に最適です：

* **質問への回答**: コードアーキテクチャと機能の実装方法について質問する
* **バグ修正と定型タスク**: 頻繁な操舵が不要な明確に定義されたタスク
* **並列作業**: 複数のバグ修正を並列で処理する
* **ローカルマシンにないリポジトリ**: ローカルにチェックアウトしていないコードで作業する
* **バックエンド変更**: Claude Code がテストを書き、その後そのテストに合格するコードを書く場合

Claude Code は Claude iOS アプリでも利用可能です。これは以下に最適です：

* **移動中**: 通勤中やノートパソコンから離れている間にタスクを開始する
* **監視**: エージェントの作業の軌跡を監視し、操舵する

開発者は Claude アプリから Claude Code セッションをターミナルに移動して、タスクをローカルで続行することもできます。

## Claude Code on the web は誰が使用できますか？

Claude Code on the web はリサーチプレビューで以下に利用可能です：

* **Pro ユーザー**
* **Max ユーザー**

Team および Enterprise プレミアムシートユーザーへの提供は近日予定です。

## はじめに

1. [claude.ai/code](https://claude.ai/code) にアクセスします
2. GitHub アカウントを接続します
3. リポジトリに Claude GitHub アプリをインストールします
4. デフォルト環境を選択します
5. コーディングタスクを送信します
6. 変更を確認し、GitHub でプルリクエストを作成します

## 仕組み

Claude Code on the web でタスクを開始すると：

1. **リポジトリのクローン**: リポジトリが Anthropic 管理の仮想マシンにクローンされます
2. **環境セットアップ**: Claude がコードを含むセキュアなクラウド環境を準備します
3. **ネットワーク構成**: インターネットアクセスが設定に基づいて構成されます
4. **タスク実行**: Claude がコードを分析し、変更を加え、テストを実行し、その作業を確認します
5. **完了**: 完了時に通知され、変更を含むプルリクエストを作成できます
6. **結果**: 変更がブランチにプッシュされ、プルリクエスト作成の準備ができます

## ウェブとターミナル間でのタスク移動

### ウェブからターミナルへ

ウェブでタスクを開始した後：

1. 「Open in CLI」ボタンをクリックします
2. コマンドをコピーしてリポジトリのチェックアウトでターミナルで実行します
3. 既存のローカル変更はスタッシュされ、リモートセッションが読み込まれます
4. ローカルで作業を続行します

## クラウド環境

### デフォルトイメージ

一般的なツールチェーンと言語エコシステムがプリインストールされた汎用イメージを構築・保守しています。このイメージには以下が含まれます：

* 人気のあるプログラミング言語とランタイム
* 一般的なビルドツールとパッケージマネージャー
* テストフレームワークとリンター

#### 利用可能なツールの確認

環境にプリインストールされているものを確認するには、Claude Code に以下を実行するよう依頼します：

```bash  theme={null}
check-tools
```

このコマンドは以下を表示します：

* プログラミング言語とそのバージョン
* 利用可能なパッケージマネージャー
* インストールされた開発ツール

#### 言語固有のセットアップ

汎用イメージには以下の事前構成環境が含まれます：

* **Python**: pip、poetry、および一般的な科学ライブラリを備えた Python 3.x
* **Node.js**: npm、yarn、および pnpm を備えた最新 LTS バージョン
* **Java**: Maven と Gradle を備えた OpenJDK
* **Go**: モジュールサポート付きの最新安定版
* **Rust**: cargo を備えた Rust ツールチェーン
* **C++**: GCC および Clang コンパイラ

### 環境構成

Claude Code on the web でセッションを開始すると、内部で以下が発生します：

1. **環境準備**: リポジトリをクローンし、初期化用に構成された Claude フックを実行します。リポジトリは GitHub リポジトリのデフォルトブランチでクローンされます。特定のブランチをチェックアウトしたい場合は、プロンプトで指定できます。

2. **ネットワーク構成**: エージェント用のインターネットアクセスを構成します。インターネットアクセスはデフォルトで制限されていますが、ニーズに基づいて環境をインターネットなしまたは完全なインターネットアクセスを持つように構成できます。

3. **Claude Code 実行**: Claude Code が実行されてタスクを完了し、コードを書き、テストを実行し、その作業を確認します。ウェブインターフェース経由でセッション全体を通じて Claude をガイドし、操舵できます。Claude は `CLAUDE.md` で定義したコンテキストを尊重します。

4. **結果**: Claude が作業を完了すると、ブランチをリモートにプッシュします。ブランチのプルリクエストを作成できるようになります。

<Note>
  Claude は環境で利用可能なターミナルと CLI ツールを完全に通じて動作します。汎用イメージにプリインストールされたツールと、フックまたは依存関係管理を通じてインストールする追加ツールを使用します。
</Note>

**新しい環境を追加するには：** 現在の環境を選択して環境セレクターを開き、「Add environment」を選択します。これにより、環境名、ネットワークアクセスレベル、および設定したい環境変数を指定できるダイアログが開きます。

**既存の環境を更新するには：** 現在の環境を選択し、環境名の右側にある設定ボタンを選択します。これにより、環境名、ネットワークアクセス、および環境変数を更新できるダイアログが開きます。

<Note>
  環境変数は [`.env` 形式](https://www.dotenv.org/) でキーと値のペアとして指定する必要があります。例えば：

  ```
  API_KEY=your_api_key
  DEBUG=true
  ```
</Note>

### 依存関係管理

[SessionStart フック](/ja/hooks#sessionstart) を使用して自動依存関係インストールを構成します。これはリポジトリの `.claude/settings.json` ファイルで構成できます：

```json  theme={null}
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/install_pkgs.sh"
          }
        ]
      }
    ]
  }
}
```

`scripts/install_pkgs.sh` に対応するスクリプトを作成します：

```bash  theme={null}
#!/bin/bash
npm install
pip install -r requirements.txt
exit 0
```

実行可能にします：`chmod +x scripts/install_pkgs.sh`

#### ローカル対リモート実行

デフォルトでは、すべてのフックはローカルとリモート（ウェブ）環境の両方で実行されます。フックを 1 つの環境でのみ実行するには、フックスクリプトで `CLAUDE_CODE_REMOTE` 環境変数を確認します。

```bash  theme={null}
#!/bin/bash

# 例：リモート環境でのみ実行
if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  exit 0
fi

npm install
pip install -r requirements.txt
```

#### 環境変数の永続化

SessionStart フックは、`CLAUDE_ENV_FILE` 環境変数で指定されたファイルに書き込むことで、後続の bash コマンド用に環境変数を永続化できます。詳細については、フック参照の [SessionStart フック](/ja/hooks#sessionstart) を参照してください。

## ネットワークアクセスとセキュリティ

### ネットワークポリシー

#### GitHub プロキシ

セキュリティのため、すべての GitHub 操作は、すべての git インタラクションを透過的に処理する専用プロキシサービスを通じて行われます。サンドボックス内では、git クライアントはカスタムビルドのスコープ付き認証情報を使用して認証します。このプロキシは：

* GitHub 認証をセキュアに管理します - git クライアントはサンドボックス内のスコープ付き認証情報を使用し、プロキシはこれを検証して実際の GitHub 認証トークンに変換します
* 安全性のため git プッシュ操作を現在のワーキングブランチに制限します
* セキュリティ境界を維持しながらシームレスなクローン、フェッチ、PR 操作を有効にします

#### セキュリティプロキシ

環境はセキュリティと不正使用防止のため HTTP/HTTPS ネットワークプロキシの背後で実行されます。すべてのアウトバウンドインターネットトラフィックはこのプロキシを通じて渡され、以下を提供します：

* 悪意のあるリクエストからの保護
* レート制限と不正使用防止
* 強化されたセキュリティのためのコンテンツフィルタリング

### アクセスレベル

デフォルトでは、ネットワークアクセスは [許可リストドメイン](#default-allowed-domains) に制限されています。

カスタムネットワークアクセスを構成でき、ネットワークアクセスを無効にすることもできます。

### デフォルト許可ドメイン

「Limited」ネットワークアクセスを使用する場合、以下のドメインはデフォルトで許可されます：

#### Anthropic サービス

* api.anthropic.com
* statsig.anthropic.com
* claude.ai

#### バージョン管理

* github.com
* [www.github.com](http://www.github.com)
* api.github.com
* raw\.githubusercontent.com
* objects.githubusercontent.com
* codeload.github.com
* avatars.githubusercontent.com
* camo.githubusercontent.com
* gist.github.com
* gitlab.com
* [www.gitlab.com](http://www.gitlab.com)
* registry.gitlab.com
* bitbucket.org
* [www.bitbucket.org](http://www.bitbucket.org)
* api.bitbucket.org

#### コンテナレジストリ

* registry-1.docker.io
* auth.docker.io
* index.docker.io
* hub.docker.com
* [www.docker.com](http://www.docker.com)
* production.cloudflare.docker.com
* download.docker.com
* \*.gcr.io
* ghcr.io
* mcr.microsoft.com
* \*.data.mcr.microsoft.com

#### クラウドプラットフォーム

* cloud.google.com
* accounts.google.com
* gcloud.google.com
* \*.googleapis.com
* storage.googleapis.com
* compute.googleapis.com
* container.googleapis.com
* azure.com
* portal.azure.com
* microsoft.com
* [www.microsoft.com](http://www.microsoft.com)
* \*.microsoftonline.com
* packages.microsoft.com
* dotnet.microsoft.com
* dot.net
* visualstudio.com
* dev.azure.com
* oracle.com
* [www.oracle.com](http://www.oracle.com)
* java.com
* [www.java.com](http://www.java.com)
* java.net
* [www.java.net](http://www.java.net)
* download.oracle.com
* yum.oracle.com

#### パッケージマネージャー - JavaScript/Node

* registry.npmjs.org
* [www.npmjs.com](http://www.npmjs.com)
* [www.npmjs.org](http://www.npmjs.org)
* npmjs.com
* npmjs.org
* yarnpkg.com
* registry.yarnpkg.com

#### パッケージマネージャー - Python

* pypi.org
* [www.pypi.org](http://www.pypi.org)
* files.pythonhosted.org
* pythonhosted.org
* test.pypi.org
* pypi.python.org
* pypa.io
* [www.pypa.io](http://www.pypa.io)

#### パッケージマネージャー - Ruby

* rubygems.org
* [www.rubygems.org](http://www.rubygems.org)
* api.rubygems.org
* index.rubygems.org
* ruby-lang.org
* [www.ruby-lang.org](http://www.ruby-lang.org)
* rubyforge.org
* [www.rubyforge.org](http://www.rubyforge.org)
* rubyonrails.org
* [www.rubyonrails.org](http://www.rubyonrails.org)
* rvm.io
* get.rvm.io

#### パッケージマネージャー - Rust

* crates.io
* [www.crates.io](http://www.crates.io)
* static.crates.io
* rustup.rs
* static.rust-lang.org
* [www.rust-lang.org](http://www.rust-lang.org)

#### パッケージマネージャー - Go

* proxy.golang.org
* sum.golang.org
* index.golang.org
* golang.org
* [www.golang.org](http://www.golang.org)
* goproxy.io
* pkg.go.dev

#### パッケージマネージャー - JVM

* maven.org
* repo.maven.org
* central.maven.org
* repo1.maven.org
* jcenter.bintray.com
* gradle.org
* [www.gradle.org](http://www.gradle.org)
* services.gradle.org
* spring.io
* repo.spring.io

#### パッケージマネージャー - その他の言語

* packagist.org (PHP Composer)
* [www.packagist.org](http://www.packagist.org)
* repo.packagist.org
* nuget.org (.NET NuGet)
* [www.nuget.org](http://www.nuget.org)
* api.nuget.org
* pub.dev (Dart/Flutter)
* api.pub.dev
* hex.pm (Elixir/Erlang)
* [www.hex.pm](http://www.hex.pm)
* cpan.org (Perl CPAN)
* [www.cpan.org](http://www.cpan.org)
* metacpan.org
* [www.metacpan.org](http://www.metacpan.org)
* api.metacpan.org
* cocoapods.org (iOS/macOS)
* [www.cocoapods.org](http://www.cocoapods.org)
* cdn.cocoapods.org
* haskell.org
* [www.haskell.org](http://www.haskell.org)
* hackage.haskell.org
* swift.org
* [www.swift.org](http://www.swift.org)

#### Linux ディストリビューション

* archive.ubuntu.com
* security.ubuntu.com
* ubuntu.com
* [www.ubuntu.com](http://www.ubuntu.com)
* \*.ubuntu.com
* ppa.launchpad.net
* launchpad.net
* [www.launchpad.net](http://www.launchpad.net)

#### 開発ツール & プラットフォーム

* dl.k8s.io (Kubernetes)
* pkgs.k8s.io
* k8s.io
* [www.k8s.io](http://www.k8s.io)
* releases.hashicorp.com (HashiCorp)
* apt.releases.hashicorp.com
* rpm.releases.hashicorp.com
* archive.releases.hashicorp.com
* hashicorp.com
* [www.hashicorp.com](http://www.hashicorp.com)
* repo.anaconda.com (Anaconda/Conda)
* conda.anaconda.org
* anaconda.org
* [www.anaconda.com](http://www.anaconda.com)
* anaconda.com
* continuum.io
* apache.org (Apache)
* [www.apache.org](http://www.apache.org)
* archive.apache.org
* downloads.apache.org
* eclipse.org (Eclipse)
* [www.eclipse.org](http://www.eclipse.org)
* download.eclipse.org
* nodejs.org (Node.js)
* [www.nodejs.org](http://www.nodejs.org)

#### クラウドサービス & 監視

* statsig.com
* [www.statsig.com](http://www.statsig.com)
* api.statsig.com
* \*.sentry.io

#### コンテンツ配信 & ミラー

* \*.sourceforge.net
* packagecloud.io
* \*.packagecloud.io

#### スキーマ & 構成

* json-schema.org
* [www.json-schema.org](http://www.json-schema.org)
* json.schemastore.org
* [www.schemastore.org](http://www.schemastore.org)

<Note>
  `*` でマークされたドメインはワイルドカードサブドメインマッチングを示します。例えば、`*.gcr.io` は `gcr.io` のすべてのサブドメインへのアクセスを許可します。
</Note>

### カスタマイズされたネットワークアクセスのセキュリティベストプラクティス

1. **最小権限の原則**: 必要な最小限のネットワークアクセスのみを有効にします
2. **定期的に監査**: 許可されたドメインを定期的に確認します
3. **HTTPS を使用**: HTTP エンドポイントより HTTPS エンドポイントを常に優先します

## セキュリティと分離

Claude Code on the web は強力なセキュリティ保証を提供します：

* **分離された仮想マシン**: 各セッションは分離された Anthropic 管理の VM で実行されます
* **ネットワークアクセス制御**: ネットワークアクセスはデフォルトで制限され、無効にできます

<Note>
  ネットワークアクセスが無効な状態で実行する場合、Claude Code は Anthropic API と通信することが許可されており、これにより分離された Claude Code VM からデータが出ることがあります。
</Note>

* **認証情報保護**: 機密認証情報（git 認証情報や署名キーなど）はサンドボックス内の Claude Code と一緒にありません。認証はスコープ付き認証情報を使用したセキュアプロキシを通じて処理されます
* **セキュア分析**: コードは PR を作成する前に分離された VM 内で分析および変更されます

## 価格とレート制限

Claude Code on the web は、アカウント内のすべての他の Claude および Claude Code 使用とレート制限を共有します。複数のタスクを並列で実行すると、レート制限をより多く消費します。

## 制限事項

* **リポジトリ認証**: ウェブからローカルへセッションを移動できるのは、同じアカウントに認証されている場合のみです
* **プラットフォーム制限**: Claude Code on the web は GitHub でホストされているコードでのみ機能します。GitLab およびその他の非 GitHub リポジトリはクラウドセッションで使用できません

## ベストプラクティス

1. **Claude Code フックを使用**: [sessionStart フック](/ja/hooks#sessionstart) を構成して環境セットアップと依存関係インストールを自動化します。
2. **要件を文書化**: `CLAUDE.md` ファイルで依存関係とコマンドを明確に指定します。`AGENTS.md` ファイルがある場合は、`@AGENTS.md` を使用して `CLAUDE.md` でソースすることで、単一の情報源を維持できます。

## 関連リソース

* [フック構成](/ja/hooks)
* [設定リファレンス](/ja/settings)
* [セキュリティ](/ja/security)
* [データ使用](/ja/data-usage)
