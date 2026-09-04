# Troubleshooting

Every documented error and symptom, with the fix stated by upstream. Common pattern across all
clients: **most hiccups are a stale browser sign-in, fixed by reconnecting. The one exception is
a personal token, which cannot be re-authenticated — it has to be replaced.** A configured
`Authorization` header always overrides stored OAuth (see AUTHENTICATION.md) — this is the root
cause of the recurring "sign-in appears to work but every call still 401s" symptom below.

## Contents

- [Rate limits and quotas](#rate-limits-and-quotas)
- [401 — two distinct causes, always distinguished by the response body](#401-two-distinct-causes-always-distinguished-by-the-response-body)
- ["Sign-in appears to work but every call still 401s"](#sign-in-appears-to-work-but-every-call-still-401s)
- ["Every ReUI call fails and nothing asks you to sign in"](#every-reui-call-fails-and-nothing-asks-you-to-sign-in)
- [Tools missing, greyed out, or "not connected"](#tools-missing-greyed-out-or-not-connected)
- [Requests hang or the session drops mid-build](#requests-hang-or-the-session-drops-mid-build)
- [Per-client quick reference](#per-client-quick-reference)
- [Client-specific extra symptoms](#client-specific-extra-symptoms)
- [Token lifetime, restated](#token-lifetime-restated)
- [Gaps](#gaps)
- [Source](#source)

## Rate limits and quotas

- **429 "daily limit reached"** — the free-tier limit of **100 tool calls per day** has been hit.
  Fix: sign in with a Pro/Ultimate ReUI license for unlimited access, or wait for the next day.
  Stated identically on every client page. Conductor adds: parallel workspaces share one ReUI
  account, so several agents running at once draw down the same daily allowance.
- No other rate limit (e.g. a per-IP requests-per-minute cap, or a distinct 403 status) is
  documented on any page in scope for this distillation. If such a limit exists, it is not stated
  anywhere in the mirrored source and is intentionally **not** invented here — see the Gaps note
  at the end of this file.

## 401 — two distinct causes, always distinguished by the response body

Every client page draws the same two-way split:

1. **401 from a stale/expired browser (OAuth) sign-in.** Fix: reconnect / re-authenticate through
   that client's own sign-in action (see the per-client entries below). Re-authenticating fixes
   this case.
2. **401 from a personal token (headless/CI) that has expired or been revoked.**
   Re-authenticating (OAuth) does **not** fix this — a personal token has no refresh. The token
   must be replaced: create a new one at Account → MCP and update the header/env var/CI secret.

**The 401 response body itself names which of the two it is** — stated verbatim on nearly every
client page ("The 401 body names which of the two it was").

## "Sign-in appears to work but every call still 401s"

Root cause on every client: a configured credential (an `Authorization` header, a bearer-token
flag, a pasted API key) is sent on **every** request and **overrides** the OAuth credential the
sign-in flow just stored. The two are alternatives, not layers. Fix: remove the header/credential
entirely to use the browser sign-in path, or keep the header and stop expecting OAuth
re-authentication to matter while it is present.

## "Every ReUI call fails and nothing asks you to sign in"

The stored OAuth connection is **dead** (revoked, expired, or invalidated after a suspicious
token reuse), and the client is silently retrying a credential that can never work again.
**Account → MCP shows the connection as Disconnected** when this is the state. Fix: reconnect the
same way as the relevant 401 fix; retrying without signing in again cannot recover it. Stated
identically on every client page.

## Tools missing, greyed out, or "not connected"

The server did not finish connecting. Fix is client-specific (see per-client table below), but
the pattern is always: re-authenticate/reconnect, then restart the client.

## Requests hang or the session drops mid-build

Long sessions can lose the connection. Fix: reconnect/re-authenticate (client-specific action)
and retry the last prompt. Claude Code: `/mcp` and re-authenticate. Codex: `codex mcp login
reui`. Cursor: reconnect from Customize (Output panel → MCP Logs for the underlying error). Grok:
press `r` in `/mcps`. v0/Lovable/Replit/Bolt: reconnect from their respective connection UI. Zed:
Settings > AI > MCP Servers, re-authenticate. Kilo Code: toggle `reui` off/on (raising `timeout`
helps on a slow network). Antigravity: refresh the MCP servers list. VS Code/GitHub Copilot: `MCP:
List Servers`, restart `reui` (Show Output for the server log).

## Per-client quick reference

| Client | "Not connected" fix | 401 (OAuth) fix | 401 (token) fix | Reconnect action |
|---|---|---|---|---|
| Claude Code | `/mcp`, re-authenticate `reui` | `/mcp`, re-authenticate | replace token, update `.mcp.json` header | `claude mcp list` shows `✔ Connected` / `! Needs authentication` / `✘ Failed to connect` |
| Codex | `codex mcp login reui`, restart | `codex mcp login reui` | replace token, update env var/CI secret | `codex mcp list`, or `/mcp` in TUI |
| Cursor | open Customize, sign in `reui` again, restart | open Customize, sign in again | replace token, update header/env var | Output panel → MCP Logs |
| Grok | `/mcps`, toggle on with `Space`, press `r`, restart | `/mcps`, select `reui`, press `i` | replace token, update header | `grok mcp doctor reui` reports connection status |
| Conductor | Refresh status in MCP status dialog; confirm `.mcp.json` at repo root of that workspace's checkout | re-authenticate in underlying agent | replace token; check `REUI_MCP_TOKEN` set in Conductor's launch environment | MCP status dialog, Refresh status |
| v0 | reopen MCP Connections, reconnect, authorize, restart | reconnect, authorize again | replace token, update connection | Tools listed but nothing runs: v0 gates tool calls behind a permission mode — approve the call or switch Ask → Auto |
| Lovable | Connectors, remove & re-add `reui`, authorize, restart | remove & re-add, authorize | replace token, paste in again | "No Custom MCP card in Connectors": on Business/Enterprise an admin must re-enable Custom MCP |
| Replit | MCP settings, Test & save on `reui`, authorize, restart | Test & save, authorize | replace token, update header value | — |
| Bolt | Connectors, confirm ReUI toggled on for this project; else reconnect via Manage connectors | reconnect, authorize | (no documented token path — see HEADLESS-CI.md) | "Some tools missing but others work": tools can be deselected per connector — Manage connectors → ReUI → ⋯ → Edit |
| OpenCode | `opencode mcp auth reui`, restart | `opencode mcp auth reui` (if it keeps failing, `opencode mcp logout reui` first) | replace token, update header/env var | See `needs_auth` special case below |
| VS Code | `MCP: List Servers`, select `reui`, restart, sign in | disconnect account, start server again | replace token, update header/CI secret | Also via server's context menu under "MCP SERVERS - INSTALLED" |
| GitHub Copilot | VS Code: `MCP: List Servers`, restart `reui`. CLI: `/mcp`, check server enabled | VS Code: `MCP: List Servers`, re-authenticate | replace token, update header (CLI, JetBrains, Eclipse, Xcode, CI) | Confirm org MCP policy is enabled on Business/Enterprise |
| Kilo Code | confirm entry under `mcp` key with `"type": "remote"`, toggled on, reload window | disable/re-enable `reui` in Settings → MCP | replace token, paste into header | — |
| Zed | Settings > AI > MCP Servers, re-authenticate, restart | Settings > AI > MCP Servers, re-authenticate | replace token, header value (re-authenticate not offered while header set) | `agent: open settings` action also opens this panel |
| Antigravity | confirm entry uses `serverUrl` (not `url`/`httpUrl`), save, refresh list, restart | Agent Settings → Customizations → Authenticate `reui` | replace token, paste into header | — |

## Client-specific extra symptoms

- **OpenCode — `Unexpected status: needs_auth`, often with a `saveDiscoveryState()` /
  `discoveryState()` warning above it.** Not a ReUI-side failure; re-running the auth command will
  not clear it. `needs_auth` is OpenCode's own status string; the warning comes from its MCP SDK,
  mid-upgrade — OpenCode's OAuth provider has not implemented the SDK's newer discovery-state
  methods yet, so browser sign-in can succeed while the CLI still reports itself unauthenticated.
  Fix: update OpenCode first (actively being fixed upstream). If still stuck: skip the browser
  flow entirely, remove any stored OAuth credential, use a personal token via the `headers`
  config instead (does not touch OAuth, works today).
- **Claude Code — a configured header vs `/mcp`.** `/mcp` renews the browser sign-in, not the
  `Authorization` header a job sends; Claude Code reports a rejected header as a **failed
  connection**, not a fallback to OAuth.
- **v0 — tools listed but nothing runs.** v0 gates MCP tool calls behind a permission mode (Ask /
  Auto); approve the call when asked, or switch to Auto.
- **Lovable — admin-disabled custom MCP.** On Business/Enterprise workspaces an admin can turn
  off custom MCP servers as a category; ask them to re-enable it in connector admin settings.
- **Bolt — no documented token header.** Its "API key" auth form does not document which header
  it sends the key in, so upstream states a ReUI token is not guaranteed to work through it — use
  MCP OAuth instead.

## Token lifetime, restated

Applies everywhere a personal token is used: default **90 days**; **30, 60, 90, 180 days**
offered, plus **No expiry**. Nothing warns before expiry (no email, no grace period) — the token
simply starts returning 401. Existing tokens keep whatever lifetime they were issued with.

## Gaps

The task brief that scoped this distillation named "403", "429 incl. the free limit of 100 tool
calls/day", "120 req/min per IP", and "hangs" as facts to extract. Searched every in-scope page
(`docs__mcp.md`, `mcp.md`, and all 15 client pages): **no page states a 403 status code, and no
page states a 120-requests-per-minute-per-IP limit.** Both were checked with a full-text search
across the mirror and are absent. Only the 429 "100 tool calls/day" free-tier limit is documented
(captured above). This gap is reported rather than papered over — if these limits exist, they are
not present in the mirrored source at
`/private/tmp/.../reui-mirror/md/` as of the 2026-09-04 mirror.

## Source

https://reui.io/docs/mcp, https://reui.io/docs/claude, /codex, /cursor, /grok, /conductor, /v0,
/lovable, /replit, /bolt, /opencode, /vscode, /github-copilot, /kilo-code, /zed, /antigravity —
mirrored 2026-09-04.
