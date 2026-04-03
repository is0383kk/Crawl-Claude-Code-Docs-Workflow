> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Provider Quickstart

# Model Providers

OpenClaw can use many LLM providers. Pick one, authenticate, then set the default
model as `provider/model`.

## Quick start (two steps)

1. Authenticate with the provider (usually via `openclaw onboard`).
2. Set the default model:

```json5  theme={"theme":{"light":"min-light","dark":"min-dark"}}
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },
}
```

## Supported providers (starter set)

* [Anthropic (API + Claude Code CLI)](/providers/anthropic)
* [Amazon Bedrock](/providers/bedrock)
* [Cloudflare AI Gateway](/providers/cloudflare-ai-gateway)
* [GLM models](/providers/glm)
* [MiniMax](/providers/minimax)
* [Mistral](/providers/mistral)
* [Moonshot AI (Kimi + Kimi Coding)](/providers/moonshot)
* [OpenAI (API + Codex)](/providers/openai)
* [OpenCode (Zen + Go)](/providers/opencode)
* [OpenRouter](/providers/openrouter)
* [Qianfan](/providers/qianfan)
* [StepFun](/providers/stepfun)
* [Synthetic](/providers/synthetic)
* [Vercel AI Gateway](/providers/vercel-ai-gateway)
* [Venice (Venice AI)](/providers/venice)
* [xAI](/providers/xai)
* [Z.AI](/providers/zai)

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration,
see [Model providers](/concepts/model-providers).


Built with [Mintlify](https://mintlify.com).