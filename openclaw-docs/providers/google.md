> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google (Gemini)

# Google (Gemini)

The Google plugin provides access to Gemini models through Google AI Studio, plus
image generation, media understanding (image/audio/video), and web search via
Gemini Grounding.

* Provider: `google`
* Auth: `GEMINI_API_KEY` or `GOOGLE_API_KEY`
* API: Google Gemini API

## Quick start

1. Set the API key:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw onboard --auth-choice gemini-api-key
```

2. Set a default model:

```json5  theme={"theme":{"light":"min-light","dark":"min-dark"}}
{
  agents: {
    defaults: {
      model: { primary: "google/gemini-3.1-pro-preview" },
    },
  },
}
```

## Non-interactive example

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw onboard --non-interactive \
  --mode local \
  --auth-choice gemini-api-key \
  --gemini-api-key "$GEMINI_API_KEY"
```

## Capabilities

| Capability             | Supported         |
| ---------------------- | ----------------- |
| Chat completions       | Yes               |
| Image generation       | Yes               |
| Image understanding    | Yes               |
| Audio transcription    | Yes               |
| Video understanding    | Yes               |
| Web search (Grounding) | Yes               |
| Thinking/reasoning     | Yes (Gemini 3.1+) |

## Direct Gemini cache reuse

For direct Gemini API runs (`api: "google-generative-ai"`), OpenClaw now
passes a configured `cachedContent` handle through to Gemini requests.

* Configure per-model or global params with either
  `cachedContent` or legacy `cached_content`
* If both are present, `cachedContent` wins
* Example value: `cachedContents/prebuilt-context`
* Gemini cache-hit usage is normalized into OpenClaw `cacheRead` from
  upstream `cachedContentTokenCount`

Example:

```json5  theme={"theme":{"light":"min-light","dark":"min-dark"}}
{
  agents: {
    defaults: {
      models: {
        "google/gemini-2.5-pro": {
          params: {
            cachedContent: "cachedContents/prebuilt-context",
          },
        },
      },
    },
  },
}
```

## Image generation

The bundled `google` image-generation provider defaults to
`google/gemini-3.1-flash-image-preview`.

* Also supports `google/gemini-3-pro-image-preview`
* Generate: up to 4 images per request
* Edit mode: enabled, up to 5 input images
* Geometry controls: `size`, `aspectRatio`, and `resolution`

Image generation, media understanding, and Gemini Grounding all stay on the
`google` provider id.

## Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `GEMINI_API_KEY`
is available to that process (for example, in `~/.openclaw/.env` or via
`env.shellEnv`).


Built with [Mintlify](https://mintlify.com).