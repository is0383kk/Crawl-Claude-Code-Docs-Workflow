> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# flows

# `openclaw flows`

Inspect and manage [ClawFlow](/automation/clawflow) jobs.

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw flows list
openclaw flows show <lookup>
openclaw flows cancel <lookup>
```

## Commands

### `flows list`

List tracked flows and their task counts.

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw flows list
openclaw flows list --status blocked
openclaw flows list --json
```

### `flows show`

Show one flow by flow id or owner session key.

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw flows show <lookup>
openclaw flows show <lookup> --json
```

The output includes the flow status, current step, wait target, blocked summary when present, stored output keys, and linked tasks.

### `flows cancel`

Cancel a flow and any active child tasks.

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw flows cancel <lookup>
```

## Related

* [ClawFlow](/automation/clawflow) — job-level orchestration above tasks
* [Background Tasks](/automation/tasks) — detached work ledger
* [CLI reference](/cli/index) — full command tree


Built with [Mintlify](https://mintlify.com).