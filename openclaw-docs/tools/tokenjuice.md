> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tokenjuice

`tokenjuice` is an optional bundled plugin that compacts noisy `exec` and `bash`
tool results after the command has already run.

It changes the returned `tool_result`, not the command itself. Tokenjuice does
not rewrite shell input, rerun commands, or change exit codes.

Today this applies to Pi embedded runs, where tokenjuice hooks the embedded
`tool_result` path and trims the output that goes back into the session.

## Enable the plugin

Fast path:

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw config set plugins.entries.tokenjuice.enabled true
```

Equivalent:

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw plugins enable tokenjuice
```

OpenClaw already ships the plugin. There is no separate `plugins install`
or `tokenjuice install openclaw` step.

If you prefer editing config directly:

```json5 theme={"theme":{"light":"min-light","dark":"min-dark"}}
{
  plugins: {
    entries: {
      tokenjuice: {
        enabled: true,
      },
    },
  },
}
```

## What tokenjuice changes

* Compacts noisy `exec` and `bash` results before they are fed back into the session.
* Keeps the original command execution untouched.
* Preserves exact file-content reads and other commands that tokenjuice should leave raw.
* Stays opt-in: disable the plugin if you want verbatim output everywhere.

## Verify it is working

1. Enable the plugin.
2. Start a session that can call `exec`.
3. Run a noisy command such as `git status`.
4. Check that the returned tool result is shorter and more structured than the raw shell output.

## Disable the plugin

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw config set plugins.entries.tokenjuice.enabled false
```

Or:

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw plugins disable tokenjuice
```

## Related

* [Exec tool](/tools/exec)
* [Thinking levels](/tools/thinking)
* [Context engine](/concepts/context-engine)
