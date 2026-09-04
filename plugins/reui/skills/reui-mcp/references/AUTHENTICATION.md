# Authentication

Every ReUI MCP request carries a credential — **there is no anonymous access**. Which kind to use
comes down to one question: can this machine open a browser?

## Contents

- [OAuth (browser-capable clients)](#oauth-browser-capable-clients)
- [Personal tokens (headless / no-browser clients)](#personal-tokens-headless-no-browser-clients)
- [A configured Authorization header always overrides OAuth](#a-configured-authorization-header-always-overrides-oauth)
- [Placeholder / variable substitution differs by client — this is the #1 cross-client footgun](#placeholder-variable-substitution-differs-by-client-this-is-the-1-cross-client-footgun)
- [Source](#source)

## OAuth (browser-capable clients)

This is the path almost everyone takes; nothing gets pasted anywhere.

1. The agent connects and receives a `401` whose `WWW-Authenticate` header points at ReUI's
   discovery documents.
2. The agent registers itself — ReUI supports **dynamic client registration**, so there is no
   client id or secret to create manually.
3. The agent opens the "Sign in with ReUI" approval in the browser, over **PKCE**.
4. Approve once; the agent stores the tokens and refreshes them on its own from then on.
5. A free ReUI account is created in that flow if one does not already exist.
6. Every connection can be reviewed or revoked later at **Account → MCP**.

### If the agent gets stuck signed out

An OAuth connection can stop working permanently for any of these reasons:
- it was revoked
- its 60-day refresh token lapsed
- its stored token was invalidated for safety after a suspicious reuse

From then on every refresh answers `invalid_grant`, and many agents quietly retry that forever
instead of asking for a fresh sign-in — so the only visible symptom is ReUI tools that stopped
working. The stored credential is dead; no amount of retrying revives it.

**Fix:** make the agent sign in again — either its own reconnect/sign-in action, or by removing
and re-adding the ReUI MCP server, which triggers a fresh browser approval. **Account → MCP**
shows the connection as **Disconnected** when this is the state.

## Personal tokens (headless / no-browser clients)

Some environments can never show an approval screen: CI, a remote shell over SSH, a container, a
cron task. Skip OAuth and carry a personal token instead.

### Create the token

- Go to **Account → MCP** and create a personal token.
- Format: `reui_pat_...`
- Shown **once**, at creation. ReUI stores only a hash of it — a lost token must be replaced, not
  recovered.
- **Up to 20 active tokens** may be held at once — enough to give each pipeline or machine its
  own.

### Send it as a Bearer header

```
Authorization: Bearer reui_pat_...
```

In an MCP client config this is a `headers` entry on the ReUI server; in a script it is one `-H`
flag.

Smoke test:

```bash
curl -sS https://mcp.reui.io \
  -H 'content-type: application/json' \
  -H 'accept: application/json, text/event-stream' \
  -H "authorization: Bearer $REUI_MCP_TOKEN" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl","version":"0.0.0"}}}'
```

The `accept` header is **not decoration**: MCP's Streamable HTTP transport requires the client to
list both `application/json` and `text/event-stream`, and this server answers a POST with an SSE
stream — a request that omits it fails. A working token returns `200` with the JSON-RPC result
delivered as an SSE event; a bad one returns `401` with a `WWW-Authenticate` header and a
JSON-RPC error naming the actual problem (expired, revoked, or an unexpanded placeholder).

### Lifetimes and silent expiry

- Default lifetime: **90 days**.
- Offered lifetimes: **30, 60, 90, 180 days**, or **No expiry** (for pipelines that genuinely
  cannot rotate).
- **Nothing warns before expiry.** No expiry email, no grace period — the first sign is usually a
  green pipeline turning red.
- On expiry the token returns `401` and must be **replaced, not re-authenticated** — a personal
  token has no refresh, so signing in again does nothing for it.
- Create a new one at Account → MCP and update the secret.
- A revocation from Account → MCP "takes effect at the server within about half a minute."

### Store it in a CI secret

Treat the token like a password: it authenticates as the account holder and carries their plan.
Put it in the CI provider's secret store, read it from the environment at run time. Never commit
it to a config file that lands in the repository. Prefer one token per pipeline so a single leak
can be revoked without taking down the rest.

## A configured Authorization header always overrides OAuth

This is stated per-client throughout CLIENT-SETUP.md, and generally on the MCP overview page: a
credential configured directly on the server entry (a `headers.Authorization` line, a bearer
token flag, etc.) is sent on **every** request and **takes precedence over any stored OAuth
credential**. The two are alternatives, not layers — configuring both means the header always
wins, so re-authenticating via the browser flow silently cannot take effect while a header is
present. Remove the header entirely to use the browser sign-in path.

## Placeholder / variable substitution differs by client — this is the #1 cross-client footgun

Whether `${VAR}` (or similar) in an MCP config is expanded into the real secret, or sent to the
server as **literal text** (causing a 401), depends entirely on the client. This is separate from
`components.json`, which the shadcn CLI always expands `${REUI_LICENSE_KEY}` from — the MCP
config is a different file with different (or no) substitution rules. Per client (see
CLIENT-SETUP.md for each client's exact syntax and file):

| Client | MCP config substitution |
|---|---|
| Claude Code | Expands `${VAR}` and `${VAR:-default}` in a server's `url` and `headers`, in `.mcp.json`. |
| Cursor | Only understands the `env:` prefix: `${env:NAME}`. A bare `${REUI_LICENSE_KEY}` is sent as literal text and 401s. |
| Codex | No placeholder syntax in `config.toml`; instead names the variable via `bearer_token_env_var` (or `env_http_headers`). Never paste the `${REUI_LICENSE_KEY}` form into `http_headers` — that is a static header, not expanded. |
| Grok (Grok Build) | Expands `${VAR}` and `${VAR:-default}` inside `url`, `command`, `args`, `env`, and `headers`. |
| VS Code | Its own `${input:...}` (prompts once, stores securely) and `${env:...}` syntax — unrelated to `${REUI_LICENSE_KEY}`. |
| OpenCode | Its own `{env:NAME}` syntax (different braces than `${...}`), e.g. `Bearer {env:REUI_LICENSE_KEY}`. The `${REUI_LICENSE_KEY}` form from `components.json` is *not* expanded by OpenCode and passes through literally. |
| Kilo Code | Documents **no** variable substitution for `kilo.jsonc` — paste the real token, keep the file out of version control. |
| Zed | **No** placeholder syntax in `settings.json` — paste the real token. |
| Antigravity | Documents **no** substitution for `mcp_config.json` — its own examples use literal header values. |
| v0 | The MCP connection form sends exactly what is typed — no environment placeholder support; paste the real `reui_pat_...` value, or use the built-in OAuth/Bearer Token auth-type selector instead. |
| Lovable | The connector form does not expand anything — paste the real token via the "Bearer token or API key" auth-type option. |
| Replit | The MCP header field does not expand anything — paste the real token in Advanced settings. |
| Bolt | No documented header for its "API key" option at all — upstream says "we cannot promise a ReUI token works through it," recommends the OAuth sign-in flow ("MCP OAuth") instead. |
| GitHub Copilot | VS Code surface: prefer `${input:...}`/`${env:...}`. Copilot CLI (`~/.copilot/mcp-config.json`) writes `${VAR}` in its own examples but "the docs never state the behaviour outright" (upstream's own uncertainty, stated as such). JetBrains/Eclipse/Xcode `mcp.json`: no documented variable support — paste the real token. |
| Conductor | Delegates entirely to the underlying agent's config (Claude Code `.mcp.json`, Codex `config.toml`, or Cursor `.cursor/mcp.json`) — same rules as that agent. |

## Source

https://reui.io/docs/mcp, and each client page in CLIENT-SETUP.md — mirrored 2026-09-04.
