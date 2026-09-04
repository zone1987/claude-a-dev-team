# Headless and CI

For any environment that can never show an approval screen (CI job, remote shell over SSH,
container, cron task): skip OAuth, use a personal token (`reui_pat_...`) from **Account → MCP**
as a Bearer header. Shared mechanics (creation, lifetimes, the 20-token limit, why a header
always overrides OAuth) are in AUTHENTICATION.md. This file has the exact per-client commands and
config shapes.

## Contents

- [Claude Code](#claude-code)
- [Codex](#codex)
- [Cursor](#cursor)
- [Grok (Grok Build)](#grok-grok-build)
- [Conductor](#conductor)
- [v0](#v0)
- [Lovable](#lovable)
- [Replit](#replit)
- [Bolt](#bolt)
- [OpenCode](#opencode)
- [VS Code](#vs-code)
- [GitHub Copilot](#github-copilot)
- [Kilo Code](#kilo-code)
- [Zed](#zed)
- [Antigravity](#antigravity)
- [Source](#source)

## Claude Code

```
claude mcp add --transport http reui https://mcp.reui.io \
  --header "Authorization: Bearer reui_pat_your_token_here"
```

In a committed config, let Claude Code substitute the env var instead (it expands `${VAR}` in
`.mcp.json`):

```json
{
  "mcpServers": {
    "reui": {
      "type": "http",
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer ${REUI_MCP_TOKEN}"
      }
    }
  }
}
```

Once a header is set, that is the credential used — no fallback to the browser flow. A bad or
lapsed token shows as a failed connection, not a sign-in prompt.

## Codex

```
codex mcp add reui --url https://mcp.reui.io \
  --bearer-token-env-var REUI_LICENSE_KEY
```

Writes to `~/.codex/config.toml`:

```toml
[mcp_servers.reui]
url = "https://mcp.reui.io"
bearer_token_env_var = "REUI_LICENSE_KEY"
```

Then `export REUI_LICENSE_KEY=<your token or license key>` in the shell profile. Codex also
accepts `http_headers` (static) and `env_http_headers` (sourced from environment), but
`bearer_token_env_var` is the shortest correct route. Do not paste the `${REUI_LICENSE_KEY}` form
from `components.json` into `http_headers` — that placeholder is expanded by the shadcn CLI, not
by Codex; a static header does not expand it, and it reaches the server as literal text (401). A
bearer token configured this way replaces `codex mcp login`, not adds to it.

## Cursor

Cursor interpolates `${env:NAME}` inside `headers`:

```json
{
  "mcpServers": {
    "reui": {
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer ${env:REUI_LICENSE_KEY}"
      }
    }
  }
}
```

Then `export REUI_LICENSE_KEY=<your token or license key>` in the shell profile. Pasting the
literal `reui_pat_...` value works too, only in a file not committed.

## Grok (Grok Build)

```
grok mcp add --transport http reui https://mcp.reui.io \
  --header "Authorization: Bearer reui_pat_your_token_here"
```

Grok expands `${VAR}` and `${VAR:-default}` inside `url`, `command`, `args`, `env`, and `headers`:

```toml
[mcp_servers.reui]
url = "https://mcp.reui.io"
headers = { Authorization = "Bearer ${REUI_MCP_TOKEN}" }
```

For non-interactive runs specifically: `grok -p`, cron jobs, pipelines.

## Conductor

Sign-in belongs to the underlying agent. For fanning out across many parallel workspaces at
once, a token is "the more predictable option, since it authenticates from the config itself
rather than through a browser prompt per session." Claude Code path shown (commit-safe because
`${VAR}` is expanded):

```json
{
  "mcpServers": {
    "reui": {
      "type": "http",
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer ${REUI_MCP_TOKEN}"
      }
    }
  }
}
```

Export `REUI_MCP_TOKEN` in the environment Conductor launches agents from. This is the one form
safe to commit in `.mcp.json`, which matters here specifically because that file is inherited by
every workspace worktree. If the variable is unset, Claude Code sends the literal
`${REUI_MCP_TOKEN}` text and ReUI rejects it with 401. Parallel workspaces **share one ReUI
account** — several agents running at once draw down the same daily allowance (relevant to the
429 free-tier limit; see TROUBLESHOOTING.md).

## v0

v0 itself always runs in a browser (OAuth is the normal path). When provisioning chats through
the v0 Platform API instead:

```bash
curl -X POST https://api.v0.dev/v1/mcp-servers \
  -H "Authorization: Bearer $V0_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "reui",
    "url": "https://mcp.reui.io",
    "auth": { "type": "bearer", "token": "reui_pat_your_token_here" }
  }'
```

Or via the `v0-sdk` package:

```ts
import { v0 } from 'v0-sdk';

await v0.mcpServers.create({
  name: 'reui',
  url: 'https://mcp.reui.io',
  auth: { type: 'bearer', token: process.env.REUI_MCP_TOKEN! },
});
```

## Lovable

No headless/CI mode of its own (browser product). The connector form's auth-type selector offers
"Bearer token or API key" as an alternative to OAuth (default): create a personal token at
Account → MCP, paste the token value alone — just `reui_pat_...`, no `Authorization:` prefix, no
`${...}` placeholder (sent exactly as written) — then click Add server.

## Replit

For an unattended setup with nobody to approve a browser prompt: create a token, open **Advanced
settings** in the add-server dialog, define a custom header:

```
Header name:  Authorization
Header value: Bearer reui_pat_your_token_here
```

Replit sends the headers defined with every MCP request. Paste the token itself, not an
environment variable reference — the value is sent exactly as written.

## Bolt

No documented headless path with a personal token — Bolt's "API key" auth option's header is
undocumented by Bolt, so upstream states it cannot promise a ReUI token works through it. Use the
"MCP OAuth" sign-in flow instead (Bolt has a browser).

## OpenCode

Skip OAuth; create a token; pass as an `Authorization: Bearer` header:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "reui": {
      "type": "remote",
      "url": "https://mcp.reui.io",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer reui_pat_your_token_here"
      }
    }
  }
}
```

Prefer OpenCode's own environment syntax on this path, `Bearer {env:REUI_LICENSE_KEY}` (resolved
before the request goes out, keeps the secret out of a committed file). Pick one authentication
method, not both: a `headers.Authorization` entry is sent on every request, including after a
browser sign-in, so it takes precedence.

## VS Code

```json
{
  "servers": {
    "reui": {
      "type": "http",
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer reui_pat_your_token_here"
      }
    }
  }
}
```

Since `.vscode/mcp.json` is usually committed, prefer an input variable over a pasted secret — VS
Code prompts for the value the first time the server starts and stores it securely afterwards:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "reui-token",
      "description": "ReUI personal token (reui_pat_...)",
      "password": true
    }
  ],
  "servers": {
    "reui": {
      "type": "http",
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer ${input:reui-token}"
      }
    }
  }
}
```

## GitHub Copilot

VS Code surface: identical to the VS Code section above (`.vscode/mcp.json`). Organization
policy note: on a Copilot Business or Copilot Enterprise plan, MCP servers must be enabled by an
admin in Copilot policy before any MCP server, ReUI included, will connect. JetBrains, Eclipse,
Xcode `mcp.json` has no documented variable support — paste the real token there and keep the
file out of version control. Copilot CLI examples use `~/.copilot/mcp-config.json` with `${VAR}`
in their own examples, though "the docs never state the behaviour outright."

## Kilo Code

```json
{
  "mcp": {
    "reui": {
      "type": "remote",
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer reui_pat_your_token_here"
      },
      "enabled": true,
      "timeout": 15000
    }
  }
}
```

Kilo Code's docs document no variable substitution for this file — paste the real token, keep the
file out of version control. `timeout` is optional, in milliseconds.

## Zed

```json
{
  "context_servers": {
    "reui": {
      "url": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer reui_pat_your_token_here"
      }
    }
  }
}
```

Paste the real token — Zed has no placeholder syntax in `settings.json`. Adding this header also
switches the browser flow off: Zed only prompts to sign in when a remote server has no
`Authorization` header configured.

## Antigravity

```json
{
  "mcpServers": {
    "reui": {
      "serverUrl": "https://mcp.reui.io",
      "headers": {
        "Authorization": "Bearer reui_pat_your_token_here"
      }
    }
  }
}
```

Paste the token itself — Antigravity documents no variable substitution for `mcp_config.json`.

## Source

https://reui.io/docs/claude, /codex, /cursor, /grok, /conductor, /v0, /lovable, /replit, /bolt,
/opencode, /vscode, /github-copilot, /kilo-code, /zed, /antigravity — mirrored 2026-09-04.
