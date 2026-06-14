# MCP Server Setup by Client

## Quick setup (CLI)

```bash
# Claude Code
npx shadcn@latest mcp init --client claude

# Cursor
npx shadcn@latest mcp init --client cursor

# VS Code (GitHub Copilot)
npx shadcn@latest mcp init --client vscode

# OpenCode
npx shadcn@latest mcp init --client opencode

# Codex (manual config required)
npx shadcn@latest mcp init --client codex
```

## Manual configuration per client

### Claude Code — `.mcp.json`

```json title=".mcp.json"
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

After adding: restart Claude Code, run `/mcp` to verify `Connected` status.

### Cursor — `.cursor/mcp.json`

```json title=".cursor/mcp.json"
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

After adding: enable the shadcn MCP server in Cursor Settings.

### VS Code — `.vscode/mcp.json`

```json title=".vscode/mcp.json"
{
  "servers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

After adding: open `.vscode/mcp.json` and click **Start** next to shadcn.

### Codex — `~/.codex/config.toml` (MANUAL — CLI cannot write this)

```toml title="~/.codex/config.toml"
[mcp_servers.shadcn]
command = "npx"
args = ["shadcn@latest", "mcp"]
```

Restart Codex after adding.

### OpenCode

Handled automatically by `mcp init --client opencode`.

## Troubleshooting

| Symptom                        | Fix                                                        |
|--------------------------------|------------------------------------------------------------|
| MCP not responding             | Restart client after config change                         |
| `No tools or prompts` message  | Run `npx clear-npx-cache`, re-enable server                |
| Registry access fails          | Check `components.json` URL, env vars, namespace syntax    |
| Installation fails             | Verify `components.json` exists, check write permissions   |

Cursor logs: View → Output → `MCP: project-*`

Source: (root)/mcp.mdx
