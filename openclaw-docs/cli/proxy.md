> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# proxy

# `openclaw proxy`

Run the local explicit debug proxy and inspect captured traffic.

This is a debugging command for transport-level investigation. It can start a
local proxy, run a child command with capture enabled, list capture sessions,
query common traffic patterns, read captured blobs, and purge local capture
data.

## Commands

```bash theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw proxy start [--host <host>] [--port <port>]
openclaw proxy run [--host <host>] [--port <port>] -- <cmd...>
openclaw proxy coverage
openclaw proxy sessions [--limit <count>]
openclaw proxy query --preset <name> [--session <id>]
openclaw proxy blob --id <blobId>
openclaw proxy purge
```

## Query presets

`openclaw proxy query --preset <name>` accepts:

* `double-sends`
* `retry-storms`
* `cache-busting`
* `ws-duplicate-frames`
* `missing-ack`
* `error-bursts`

## Notes

* `start` defaults to `127.0.0.1` unless `--host` is set.
* `run` starts a local debug proxy and then runs the command after `--`.
* Captures are local debugging data; use `openclaw proxy purge` when finished.
