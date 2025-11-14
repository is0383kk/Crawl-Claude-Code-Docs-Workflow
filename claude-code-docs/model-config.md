# モデル設定

> Claude Codeのモデル設定について学習します。`opusplan`などのモデルエイリアスを含みます

## 利用可能なモデル

Claude Codeの`model`設定では、以下のいずれかを設定できます：

* **モデルエイリアス**
* 完全な\*\*[モデル名](https://docs.claude.com/ja/docs/about-claude/models/overview#model-names)\*\*
* Bedrockの場合、ARN

### モデルエイリアス

モデルエイリアスは、正確なバージョン番号を覚えることなくモデル設定を選択するための便利な方法を提供します：

| モデルエイリアス         | 動作                                                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **`default`**    | アカウントタイプに応じた推奨モデル設定                                                                                                                    |
| **`sonnet`**     | 日常的なコーディングタスク用に最新のSonnetモデル（現在Sonnet 4.5）を使用                                                                                           |
| **`opus`**       | 特殊な複雑な推論タスク用にOpusモデル（現在Opus 4.1）を使用                                                                                                    |
| **`haiku`**      | シンプルなタスク用に高速で効率的なHaikuモデルを使用                                                                                                           |
| **`sonnet[1m]`** | 長いセッション用に[100万トークンコンテキストウィンドウ](https://docs.claude.com/ja/docs/build-with-claude/context-windows#1m-token-context-window)を備えたSonnetを使用 |
| **`opusplan`**   | プランモード中は`opus`を使用し、実行時に`sonnet`に切り替わる特別なモード                                                                                            |

### モデルの設定

モデルは優先度順に複数の方法で設定できます：

1. **セッション中** - `/model <alias|name>`を使用してセッション中にモデルを切り替える
2. **起動時** - `claude --model <alias|name>`で起動
3. **環境変数** - `ANTHROPIC_MODEL=<alias|name>`を設定
4. **設定** - `model`フィールドを使用して設定ファイルで永続的に設定

使用例：

```bash  theme={null}
# Opusで起動
claude --model opus

# セッション中にSonnetに切り替え
/model sonnet
```

設定ファイルの例：

```
{
    "permissions": {
        ...
    },
    "model": "opus"
}
```

## 特別なモデルの動作

### `default`モデル設定

`default`の動作はアカウントタイプに依存します。

特定のMaxユーザーの場合、Opusの使用量閾値に達するとClaude Codeは自動的にSonnetにフォールバックします。

### `opusplan`モデル設定

`opusplan`モデルエイリアスは自動化されたハイブリッドアプローチを提供します：

* **プランモード** - 複雑な推論とアーキテクチャ決定用にOpusを使用
* **実行モード** - コード生成と実装用に自動的にSonnetに切り替わり

これにより両方の長所が得られます：プランニング用のOpusの優れた推論能力と、実行用のSonnetの効率性です。

### \[1m]による拡張コンテキスト

Console/APIユーザーの場合、完全なモデル名に`[1m]`サフィックスを追加して、[100万トークンコンテキストウィンドウ](https://docs.claude.com/ja/docs/build-with-claude/context-windows#1m-token-context-window)を有効にできます。

```bash  theme={null}
# [1m]サフィックス付きの完全なモデル名を使用する例
/model anthropic.claude-sonnet-4-5-20250929-v1:0[1m]
```

注：拡張コンテキストモデルは[異なる価格設定](https://docs.claude.com/ja/docs/about-claude/pricing#long-context-pricing)があります。

## 現在のモデルを確認する

現在使用しているモデルは複数の方法で確認できます：

1. [ステータスライン](/ja/statusline)内（設定されている場合）
2. `/status`内。アカウント情報も表示されます。

## 環境変数

以下の環境変数を使用できます。これらは完全な**モデル名**である必要があり、エイリアスがマップするモデル名を制御します。

| 環境変数                             | 説明                                                                  |
| -------------------------------- | ------------------------------------------------------------------- |
| `ANTHROPIC_DEFAULT_OPUS_MODEL`   | `opus`用に使用するモデル、またはプランモードがアクティブな場合の`opusplan`用                      |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | `sonnet`用に使用するモデル、またはプランモードがアクティブでない場合の`opusplan`用                  |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL`  | `haiku`用に使用するモデル、または[バックグラウンド機能](/ja/costs#background-token-usage)用 |
| `CLAUDE_CODE_SUBAGENT_MODEL`     | [サブエージェント](/ja/sub-agents)用に使用するモデル                                 |

注：`ANTHROPIC_SMALL_FAST_MODEL`は非推奨です。`ANTHROPIC_DEFAULT_HAIKU_MODEL`を使用してください。

### プロンプトキャッシング設定

Claude Codeは[プロンプトキャッシング](https://docs.claude.com/ja/docs/build-with-claude/prompt-caching)を自動的に使用してパフォーマンスを最適化し、コストを削減します。プロンプトキャッシングをグローバルに、または特定のモデルティア用に無効にできます：

| 環境変数                            | 説明                                              |
| ------------------------------- | ----------------------------------------------- |
| `DISABLE_PROMPT_CACHING`        | すべてのモデルのプロンプトキャッシングを無効にするには`1`に設定（モデル固有の設定より優先） |
| `DISABLE_PROMPT_CACHING_HAIKU`  | Haikuモデルのみのプロンプトキャッシングを無効にするには`1`に設定            |
| `DISABLE_PROMPT_CACHING_SONNET` | Sonnetモデルのみのプロンプトキャッシングを無効にするには`1`に設定           |
| `DISABLE_PROMPT_CACHING_OPUS`   | Opusモデルのみのプロンプトキャッシングを無効にするには`1`に設定             |

これらの環境変数は、プロンプトキャッシング動作に対する細かい制御を提供します。グローバルな`DISABLE_PROMPT_CACHING`設定はモデル固有の設定より優先され、必要に応じてすべてのキャッシングを迅速に無効にできます。モデル固有の設定は、特定のモデルをデバッグする場合や、異なるキャッシング実装を持つ可能性があるクラウドプロバイダーと連携する場合など、選択的な制御に役立ちます。
