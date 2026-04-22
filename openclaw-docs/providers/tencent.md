> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tencent Cloud (TokenHub)

# Tencent Cloud (TokenHub)

The Tencent Cloud provider gives access to Tencent Hy models via the TokenHub
endpoint (`tencent-tokenhub`).

The provider uses an OpenAI-compatible API.

## Quick start

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw onboard --auth-choice tokenhub-api-key
```

## Non-interactive example

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw onboard --non-interactive \
  --mode local \
  --auth-choice tokenhub-api-key \
  --tokenhub-api-key "$TOKENHUB_API_KEY" \
  --skip-health \
  --accept-risk
```

## Providers and endpoints

| Provider           | Endpoint                      | Use case                |
| ------------------ | ----------------------------- | ----------------------- |
| `tencent-tokenhub` | `tokenhub.tencentmaas.com/v1` | Hy via Tencent TokenHub |

## Available models

### tencent-tokenhub

* **hy3-preview** — Hy3 preview (256K context, reasoning, default)

## Notes

* TokenHub model refs use `tencent-tokenhub/<modelId>`.
* Override pricing and context metadata in `models.providers` if needed.

## Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `TOKENHUB_API_KEY`
is available to that process (for example, in `~/.openclaw/.env` or via
`env.shellEnv`).

## Related documentation

* [OpenClaw Configuration](/configuration)
* [Model Providers](/concepts/model-providers)
* [Tencent TokenHub](https://cloud.tencent.com/document/product/1823/130050)
