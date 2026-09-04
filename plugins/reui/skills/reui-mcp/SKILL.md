---
name: reui-mcp
description: The ReUI MCP server at mcp.reui.io: its tools, OAuth and reui_pat_ tokens, and the free plan's 100 calls/day. Use when an mcp__reui__ tool fails or ReUI MCP access is set up.
---

# The ReUI MCP server

`https://mcp.reui.io`, Streamable HTTP. It does discovery and guidance — scored search, inline
component APIs, page planning, validation. It never serves source: the shadcn CLI installs, and the
licence key lives there, not here.

Every request carries a credential; there is no anonymous access.

## The budget that decides how you call it

**The free plan allows 100 tool calls per day.** Spend them deliberately:

- One `search` per intent, with hints (`type`, `component`, `category`, `features`, `free`) — never
  a second search for the same thing.
- **One batched `get_component`** over the whole `componentsUsed` array, never one call per name.
  Often skippable entirely: a search result's `componentDigests` already carries a compact API
  contract per component.
- `compose_page` once before a whole page, instead of a search per section.
- Never `list_*` to browse — that is for a taxonomy the user explicitly asked to explore.

A Pro or Ultimate licence removes the limit. Upstream documents no other rate limit.

## When it stops answering

The plugin's `PostToolUseFailure` hook fires on any `mcp__reui__*` failure and names the cause, but
the decision is the same either way: **stop calling the MCP and use the local references.** They
carry the registry and the component APIs offline —
[reui-registry](../reui-registry/SKILL.md), [reui-blocks](../reui-blocks/SKILL.md),
[reui-data](../reui-data/SKILL.md), [reui-forms](../reui-forms/SKILL.md),
[reui-layout](../reui-layout/SKILL.md), [reui-setup](../reui-setup/SKILL.md).

The shadcn CLI is unaffected by an MCP outage:

```bash
npx shadcn@latest search @reui -q "kanban board"
npx shadcn@latest add @reui/c-kanban-1 --yes
```

## Reference map

- **[TOOLS.md](references/TOOLS.md)**: every tool, what it returns, and when to reach for it.
- **[AUTHENTICATION.md](references/AUTHENTICATION.md)**: the OAuth flow, personal `reui_pat_` tokens,
  lifetimes, and the dead-connection state that retries can never recover.
- **[HEADLESS-CI.md](references/HEADLESS-CI.md)**: tokens as Bearer headers, the required `accept`
  header, and the smoke test.
- **[TROUBLESHOOTING.md](references/TROUBLESHOOTING.md)**: every documented failure — 401 in both its
  forms, the 429 daily limit, hangs, and a sign-in that appears to work but still 401s.
- **[CLIENT-SETUP.md](references/CLIENT-SETUP.md)**: the exact command or config per client, all 15.

## Claude Code

```bash
claude mcp add --transport http reui https://mcp.reui.io
```

Then `/mcp` and sign in, or `claude mcp login reui` from the shell (`--no-browser` on a machine
without one). `claude mcp list` should report `reui ✔ Connected`.

This plugin ships `.mcp.json` with that server already declared, so the connection needs only the
sign-in.

**A configured `Authorization` header always wins over the OAuth credential.** If sign-in appears to
succeed and every call still 401s, look for a header on the `reui` entry: the two are alternatives,
not layers.

## Source

[MCP Server](https://reui.io/docs/mcp), [Agent Skills](https://reui.io/docs/agent-skills) and the
per-client guides under `https://reui.io/docs/`, mirrored 2026-09-04.
