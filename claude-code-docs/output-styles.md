# 出力スタイル

> ソフトウェアエンジニアリング以外の用途にClaudeコードを適応させる

出力スタイルを使用すると、Claude Codeをあらゆるタイプのエージェントとして使用しながら、ローカルスクリプトの実行、ファイルの読み書き、TODOの追跡などのコア機能を保持できます。

## 組み込み出力スタイル

Claude Codeの**デフォルト**出力スタイルは既存のシステムプロンプトであり、ソフトウェアエンジニアリングタスクを効率的に完了するのに役立つように設計されています。

コードベースとClaudeの動作方法を教えることに焦点を当てた、2つの追加の組み込み出力スタイルがあります：

* **説明的（Explanatory）**: ソフトウェアエンジニアリングタスクの完了を支援しながら、教育的な「インサイト」を提供します。実装の選択肢とコードベースのパターンを理解するのに役立ちます。

* **学習（Learning）**: 協調的な学習型モードで、Claude Codeはコーディング中に「インサイト」を共有するだけでなく、小さな戦略的なコードの一部を自分で実装するよう求めます。Claude Codeは実装するためにコード内に`TODO(human)`マーカーを追加します。

## 出力スタイルの仕組み

出力スタイルはClaude Codeのシステムプロンプトを直接変更します。

* デフォルト以外の出力スタイルは、コード生成と効率的な出力に固有の指示を除外します。これは通常Claude Codeに組み込まれています（簡潔に応答し、テストでコードを検証するなど）。
* 代わりに、これらの出力スタイルにはシステムプロンプトに追加されたカスタム指示があります。

## 出力スタイルを変更する

以下のいずれかを実行できます：

* `/output-style`を実行してメニューにアクセスし、出力スタイルを選択します（これは`/config`メニューからもアクセスできます）

* `/output-style [style]`（例：`/output-style explanatory`）を実行して、スタイルに直接切り替えます

これらの変更は[ローカルプロジェクトレベル](/ja/settings)に適用され、`.claude/settings.local.json`に保存されます。

## カスタム出力スタイルを作成する

Claudeの助けを借りて新しい出力スタイルを設定するには、
`/output-style:new I want an output style that ...`を実行します

デフォルトでは、`/output-style:new`を通じて作成された出力スタイルはユーザーレベルで`~/.claude/output-styles`にマークダウンファイルとして保存され、プロジェクト全体で使用できます。これらは以下の構造を持ちます：

```markdown  theme={null}
---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]
```

また、独自の出力スタイルマークダウンファイルを作成し、ユーザーレベル（`~/.claude/output-styles`）またはプロジェクトレベル（`.claude/output-styles`）のいずれかに保存することもできます。

## 関連機能との比較

### 出力スタイル対CLAUDE.md対--append-system-prompt

出力スタイルはClaude Codeのデフォルトシステムプロンプトのソフトウェアエンジニアリング固有の部分を完全に「オフ」にします。CLAUDE.mdも`--append-system-prompt`もClaude Codeのデフォルトシステムプロンプトを編集しません。CLAUDE.mdはコンテンツをユーザーメッセージとして追加します。これはClaude Codeのデフォルトシステムプロンプトの\_後に\_続きます。`--append-system-prompt`はコンテンツをシステムプロンプトに追加します。

### 出力スタイル対[エージェント](/ja/sub-agents)

出力スタイルはメインエージェントループに直接影響し、システムプロンプトのみに影響します。エージェントは特定のタスクを処理するために呼び出され、使用するモデル、利用可能なツール、エージェントを使用する時期に関するコンテキストなどの追加設定を含めることができます。

### 出力スタイル対[カスタムスラッシュコマンド](/ja/slash-commands)

出力スタイルを「保存されたシステムプロンプト」と考え、カスタムスラッシュコマンドを「保存されたプロンプト」と考えることができます。


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt