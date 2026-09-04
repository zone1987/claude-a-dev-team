# Client Setup

One section per supported client (15 total), each with its exact connect command/config. Shared
endpoint everywhere: `https://mcp.reui.io`, Streamable HTTP. Shared "Build with ReUI" prompts
(identical wording on every client page) are listed once at the end rather than per client.
Headless/CI variants and the full troubleshooting tables live in HEADLESS-CI.md and
TROUBLESHOOTING.md; unlock-premium steps (`.env.local` + `components.json`) are the same shape
described in the reui-setup skill's LICENSE-SETUP.md and are only noted here where a client adds
something client-specific.

## Contents

- [Claude (Claude Code and Claude Desktop)](#claude-claude-code-and-claude-desktop)
- [Codex](#codex)
- [Cursor](#cursor)
- [Grok (Grok Build / xAI CLI)](#grok-grok-build-xai-cli)
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
- [Shared "Build with ReUI" prompts](#shared-build-with-reui-prompts)
- [Unlock premium items — shared shape (every client page)](#unlock-premium-items-shared-shape-every-client-page)
- [Source](#source)

## Claude (Claude Code and Claude Desktop)

Two setups differ only in how the server is added.

**Claude Code (CLI):**
```
claude mcp add --transport http reui https://mcp.reui.io
```
Sign in: `/mcp` inside Claude Code, select `reui`, approve "Sign in with ReUI" in the browser.
Claude Code discovers the sign-in from the `WWW-Authenticate` header ReUI returns — nothing to
configure. Or from the shell without a session: `claude mcp login reui`. Add `--no-browser` on a
machine with no browser (e.g. SSH) — Claude Code prints the authorization URL to open elsewhere,
then asks for the redirect URL to be pasted back.

Confirm: `claude mcp list` — `reui` should report `✔ Connected`. `! Needs authentication` = sign-in
did not finish. `✘ Failed to connect` = Claude Code could not reach the server at all.

Install the ReUI skill: `curl -fsSL https://mcp.reui.io/install | node -` (drops a ReUI skill
file into the project).

`${REUI_LICENSE_KEY}` works in both `components.json` and `.mcp.json`, for two different reasons:
the shadcn CLI expands it in the former; Claude Code itself expands `${VAR}` and
`${VAR:-default}` in a server's `url`/`headers` in `.mcp.json` — which is why the ReUI installer
writes `Authorization: Bearer ${REUI_LICENSE_KEY}` into the MCP config instead of the raw key.
When the variable is unset, Claude Code warns in `claude mcp list` and sends the literal
`${REUI_LICENSE_KEY}` text (401). This exact substitution behavior does not carry over to Cursor,
OpenCode, or Zed configs.

**Claude Desktop:** setup differs only in how the server is added (per the page's tab structure);
the mirrored markdown captures the CLI tab's content only — the Claude Desktop tab's distinct UI
steps are not present as separate text in this mirror (same endpoint and sign-in flow apply per
the page's framing).

## Codex

```
codex mcp add reui --url https://mcp.reui.io
```
Confirm: `codex mcp list` (entry lands in `~/.codex/config.toml`; a trusted project can scope it
via `.codex/config.toml`). In the Codex TUI, `/mcp` shows the same list live.

Sign in: `codex mcp login reui` (opens "Sign in with ReUI" in the browser).

Install the ReUI skill: `curl -fsSL https://mcp.reui.io/install | node -`.

## Cursor

One-click "Add to Cursor" button, or manually in `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "reui": {
      "url": "https://mcp.reui.io"
    }
  }
}
```
A remote server needs no `type` field — Cursor infers Streamable HTTP from `url`. Use
`~/.cursor/mcp.json` to make ReUI available in every project.

Sign in: first tool call opens a browser "Sign in with ReUI" prompt.

Install the ReUI skill: `curl -fsSL https://mcp.reui.io/install | node -`.

Troubleshooting home: Cursor's MCP servers live under **Customize** in the sidebar.

## Grok (Grok Build / xAI CLI)

```
grok mcp add --transport http reui https://mcp.reui.io
```
Writes to `~/.grok/config.toml`:
```toml
[mcp_servers.reui]
url = "https://mcp.reui.io"
```
Sign in: browser flow triggers on first use. Or start it manually: `/mcps` → select `reui` →
press `i` to authenticate. Grok stores tokens in `~/.grok/mcp_credentials.json`.

The ReUI skill rides entirely on the MCP here — nothing to install by default; ask Grok to call
`get_agent_skill`. Optional local copy: project mode `curl -fsSL https://mcp.reui.io/install |
node -` (writes to `<project>/.claude/skills/reui` and `<project>/.agents/skills/reui` — Grok
reads Claude Code's skills, MCP entries, and instruction files with no configuration). Global
mode: `curl -fsSL https://mcp.reui.io/install | REUI_GLOBAL=1 node -` (writes to
`~/.claude/skills/reui` and `~/.agents/skills/reui`). Caveats: the installer adds a `reui` entry
to Codex's `~/.codex/config.toml` in **both** modes; global mode additionally merges one into
`~/.claude.json`. Each run **replaces** the managed `reui` skill directory outright — local edits
inside it do not survive an update.

## Conductor

Conductor runs Claude Code, Codex, Cursor, and OpenCode in parallel, each in its own git
worktree. **Conductor has no MCP config format of its own** — it uses whatever the underlying
agent already loads for that session, so ReUI is configured for that agent, and Conductor picks
it up.

Add ReUI to the repository root (works for Claude Code sessions, since Claude Code reads
`.mcp.json` from the project root, and a repo with one there gives every Claude Code session
those servers):

`.mcp.json`
```json
{
  "mcpServers": {
    "reui": {
      "type": "http",
      "url": "https://mcp.reui.io"
    }
  }
}
```
**Commit it** — since every workspace is a checkout of the repo, committing is what makes ReUI
show up in workspaces created later, not just the current one.

Running Codex sessions instead: Codex reads `~/.codex/config.toml` or `.codex/config.toml`.
Cursor Composer reads the project-level `.cursor/mcp.json` from that workspace checkout. Entry
shape is equivalent to the respective client's own guide.

Sign-in is the underlying agent's, not Conductor's own.

Confirm: Conductor shows MCP server status in the chat composer; an MCP status dialog has a
Refresh status option — use it after editing the config, do not assume a running session reloaded
it.

Install the ReUI skill from the repository root: `curl -fsSL https://mcp.reui.io/install | node -`
— writes `.claude/skills/reui` and `.agents/skills/reui` into the project, which should be
committed for the same reason as `.mcp.json`. The installer also adds a `reui` entry to
`~/.codex/config.toml` on the machine running it. The same workflow is also available at runtime
via `get_agent_skill`, so nothing breaks if the install step is skipped.

## v0

Click **Add MCP** (available from MCP Connections settings or the prompt form in a chat):
```
Name:           reui
URL:            https://mcp.reui.io
Authentication: OAuth
```
v0 offers four auth kinds: No Auth, Custom Headers, Bearer Token, OAuth. Pick **OAuth** — ReUI
supports OAuth 2.0, nothing to paste. Sign in: browser "Sign in with ReUI" prompt.

Prefer a token to a browser sign-in: choose **Bearer Token** in the same form, paste a personal
token from Account → MCP. Paste the token value itself — v0 sends exactly what is typed, so an
`${...}` placeholder arrives as literal text (401).

The ReUI skill rides on the MCP — nothing to install; v0 can call `get_agent_skill`.

Since v0 runs in the cloud, apply the premium-unlock `.env.local`/`components.json` steps inside
the v0 project it is building, not on the local machine.

## Lovable

Custom MCP servers are available on every Lovable plan. Open **Connectors** → stay on **All**,
scroll to the bottom **Custom** card labeled "MCP" ("Connect your own MCP"):
```
Server name:    reui
Server URL:     https://mcp.reui.io
Authentication: OAuth (default)
```
Leave Authentication on OAuth (default), click **Add & authorize** (opens "Sign in with ReUI").

A chat connector only gives Lovable context while it builds: it is never part of the published
app, and app visitors can never reach it.

The ReUI skill rides on the MCP — nothing to install; `get_agent_skill` on demand.

Since Lovable builds on the shadcn/ui model (Vite + React), connect GitHub first and apply the
premium-unlock steps in the synced repo, where the Agent runs the CLI.

Token alternative: same form, "Bearer token or API key" instead of OAuth (default); paste the
token alone — `reui_pat_...`, no `Authorization:` prefix, no `${...}` placeholder.

## Replit

MCP servers live on the account, not inside a single Repl — one setup covers every project. At
`replit.com/integrations` → **MCP Servers for Replit Agent** → **+ Add MCP server**. ReUI is not
in Replit's pre-listed catalog, so add it by URL:
```
Display name:    reui
MCP Server URL:  https://mcp.reui.io
```
Click **Test & save** — Replit sees ReUI asks for authorization and walks through "Sign in with
ReUI" (registers itself automatically, no client ID to create). Once saved, tools are available
across all projects.

The ReUI skill rides on the MCP — nothing separate to install; `get_agent_skill` on demand.

Replit runs a full Linux workspace, so the Agent installs items with the shadcn CLI directly in
the Replit shell. The license key can go in `.env.local`, or in the **Secrets** pane as
`REUI_LICENSE_KEY` (Replit encrypts it and exposes it as an env var — the better home for a key
not wanted in the repo).

Token alternative: **Advanced settings** in the add-server dialog, custom header (see
HEADLESS-CI.md).

## Bolt

Click the plus icon in the chatbox → **Connectors** → **Manage connectors** (same page under
Settings → Connectors) → **Custom MCP server**:
```
Name: ReUI
URL: https://mcp.reui.io
Transport type: HTTP
Authentication: MCP OAuth
```
Click **Connect** — "Connected" status in the upper right confirms setup. MCP OAuth means Bolt
runs a sign-in flow. Connectors are added at the account level and must be **enabled per
project**: open the project, plus icon → Connectors → toggle ReUI on (or select "Auto-enable for
all projects" when adding the connector).

Bolt is a hosted builder — cannot run a local installer. The ReUI tools carry their own usage
guidance; Bolt can call `get_agent_skill`.

Apply premium-unlock steps inside the Bolt project itself, so files live in the workspace Bolt
wires the UI into.

## OpenCode

`opencode.json` in the project root:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "reui": {
      "type": "remote",
      "url": "https://mcp.reui.io",
      "enabled": true
    }
  }
}
```
The ReUI installer writes the URL spelled out in full as `https://mcp.reui.io/api/mcp` (the short
form above rewrites to it — use whichever). OpenCode handles OAuth for remote MCP servers on its
own; if it does not prompt, start manually: `opencode mcp auth reui`. `opencode mcp list` shows
what is registered.

Pick one auth method, not both: the config above deliberately has no `headers` block for the
OAuth path.

Install the ReUI skill: `curl -fsSL https://mcp.reui.io/install | node -`.

## VS Code

`.vscode/mcp.json` in the workspace:
```json
{
  "servers": {
    "reui": {
      "type": "http",
      "url": "https://mcp.reui.io"
    }
  }
}
```
Note: top-level key is **`servers`**, not `mcpServers`. A remote server needs `"type": "http"`.
For every workspace instead: **MCP: Open User Configuration** from the Command Palette, add the
same entry there. **MCP: Add Server** offers a guided flow instead of hand-editing JSON.

Sign in: first tool call opens a browser "Sign in with ReUI" tab. VS Code registers itself with
ReUI dynamically — no `oauth` block or client ID needed in the entry.

The ReUI skill rides on the MCP — no separate install; `get_agent_skill` on demand.

Troubleshooting home: **MCP: List Servers** from the Command Palette, or the server's context
menu under "MCP SERVERS - INSTALLED" in the Extensions view.

## GitHub Copilot

Three surfaces documented, each with its own config:

**VS Code:** identical `.vscode/mcp.json` shape to the VS Code section above, or **MCP: Add
Server** from the Command Palette (choose Workspace or Global). Then open Chat in **Agent mode**
so Copilot can call the ReUI tools. VS Code first asks to confirm the server is trusted.
Organization policy: on Copilot Business/Enterprise, MCP servers must be enabled by an admin in
Copilot policy first.

**Copilot CLI:** examples write `${VAR}` in `~/.copilot/mcp-config.json`, though "the docs never
state the behaviour outright" (upstream's own hedge).

**JetBrains, Eclipse, Xcode:** their own `mcp.json`, with no documented variable support.

Install the ReUI skill: `curl -fsSL https://mcp.reui.io/install | node -` — writes to
`.claude/skills/reui` and `.agents/skills/reui`, both read by VS Code Copilot as project skills
(alongside `.github/skills`). If a surface does not read those folders, the same workflow ships
with the server via `get_agent_skill`.

## Kilo Code

Settings → MCP → **Add Server** → **Remote** server type, or edit the config file directly:
`~/.config/kilo/kilo.jsonc` (every project) or `kilo.jsonc` in the project root / `.kilo/kilo.jsonc`
(scoped to one):
```json
{
  "mcp": {
    "reui": {
      "type": "remote",
      "url": "https://mcp.reui.io",
      "enabled": true
    }
  }
}
```
Two things that catch people out: the top-level key is **`mcp`**, not `mcpServers`; a remote
server needs **`"type": "remote"`**, not `http`. Either wrong and the entry never connects.

Sign in: Kilo Code handles OAuth 2.0 for remote servers itself, starts the flow automatically on
connect — no client id/secret/token needed. The `oauth` key exists to turn this off (`"oauth":
false`) for servers authenticating another way; leave it out for ReUI.

Confirm: Settings → MCP shows `reui` listed and enabled; same panel enables/disables without
deleting, edits the entry, or removes it entirely.

**Skip the one-line installer used by other clients** — it writes `.claude/skills` /
`.agents/skills`, which Kilo Code does not read. Kilo Code's instruction files are `AGENTS.md`,
`CLAUDE.md`, and `CONTEXT.md`, discovered at the project root and parent directories, plus
`~/.config/kilo/AGENTS.md` globally. To keep the workflow on disk, paste it into `AGENTS.md`
rather than running the installer. At runtime, ask Kilo Code to call `get_agent_skill`.

## Zed

Settings JSON, add a context server:
```json
{
  "context_servers": {
    "reui": {
      "url": "https://mcp.reui.io"
    }
  }
}
```
A `url` is all a remote entry needs (`command`, `args`, `env` are for local stdio servers only).
UI alternative: Settings > AI > MCP Servers → Add Server → Add Remote Server → paste the URL.

Sign in: leave the entry as a bare `url` and Zed runs the standard MCP OAuth flow — browser tab
opens "Sign in with ReUI" on the first tool call.

The ReUI skill rides on the MCP — `get_agent_skill` on demand, nothing to install.

Troubleshooting home: Settings > AI > MCP Servers (the `agent: open settings` action also opens
it).

## Antigravity

Kept in `mcp_config.json`, at `~/.gemini/config/mcp_config.json` (every workspace) or
`.agents/mcp_config.json` (one workspace):
```json
{
  "mcpServers": {
    "reui": {
      "serverUrl": "https://mcp.reui.io"
    }
  }
}
```
**Remote servers must use `serverUrl`** — Antigravity does not support the `url` or `httpUrl`
keys other clients use; the wrong key never connects. Reachable from the app too: Antigravity 2.0
→ Settings → Customizations → Installed MCP Servers; IDE → `...` at the top of the agent side
panel → MCP Servers; CLI → `/mcp` opens the interactive MCP Manager. Custom servers like ReUI are
added by editing the file above regardless of entry point.

Sign in: ReUI supports dynamic client registration, so no client id/secret is needed. Open Agent
Settings (`Cmd+,` macOS / `Ctrl+,` Windows/Linux) → Customizations tab → **Authenticate** next to
`reui` → approve "Sign in with ReUI" in the browser → paste the authorization code back into
Antigravity. Antigravity stores tokens in `~/.gemini/antigravity/mcp_oauth_tokens.json` and
refreshes them automatically.

Install the ReUI skill: `curl -fsSL https://mcp.reui.io/install | node -` — writes to
`.agents/skills/reui`, exactly where Antigravity looks for workspace skills. `get_agent_skill` at
runtime works too if the install step is skipped.

## Shared "Build with ReUI" prompts

These four example prompts appear verbatim on every one of the 15 client pages, after setup:

```
Use ReUI to scaffold an admin app - the app-shell with a collapsible sidebar and top bar, and a dashboard page with stat cards and a chart.
```
```
Add a data-grid of orders with sorting, column filters, pagination, and row selection, wired to my /api/orders endpoint.
```
```
Build a multi-step "create project" wizard with the ReUI stepper and form components, with validation on each step.
```
```
Add a kanban board for support tickets with drag and drop, grouped by status, and a filters bar above it.
```

## Unlock premium items — shared shape (every client page)

Free items (the 20 components and every `c-*` example — note: this figure is stated as "20" on
every client page, one less than the "21 ReUI Primitives" figure stated on the Introduction and
Pricing pages; both numbers are reproduced exactly as each source states them) install with no
license. To unlock premium blocks, icons, and templates: get a Pro or Ultimate license (see the
reui-setup skill's PLANS.md) — one license unlocks the whole premium registry and removes the
daily MCP request limit. Then:
1. Add `REUI_LICENSE_KEY=your-license-key-here` to `.env.local` at the project root.
2. Add the authenticated `@reui` registry block to `components.json` (see the reui-setup skill's
   REGISTRY-CONFIG.md).

Client-specific caveats on this shared step are captured inline in each client's section above
(e.g. v0 and Lovable's "apply inside the cloud project", Conductor's "`.env.local` is normally
gitignored so it does not travel to new worktrees automatically").

## Source

https://reui.io/docs/claude, /codex, /cursor, /grok, /conductor, /v0, /lovable, /replit, /bolt,
/opencode, /vscode, /github-copilot, /kilo-code, /zed, /antigravity — mirrored 2026-09-04.
