---
name: shadcn-mcp
description: shadcn MCP-Server — AI-Assistenten durchsuchen/installieren Registry-Items per natürlicher Sprache; dieses Plugin liefert den MCP mit. Trigger: shadcn mcp, shadcn mcp server, npx shadcn mcp, mcp registry, install component via mcp.
---

# shadcn-mcp

shadcn MCP server: lets AI assistants browse, search and install registry
items using natural language. The plugin ships this MCP — activate it per
the instructions below.

## References

- [setup.md](references/setup.md) — Init commands for all clients, .mcp.json config
- [registries.md](references/registries.md) — Configuring additional registries in components.json
- [registry-dev.md](references/registry-dev.md) — Making your own registry MCP-compatible

## Quick setup (Claude Code)

```bash
npx shadcn@latest mcp init --client claude
```

This writes `.mcp.json` to the project root:

```json
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    }
  }
}
```

Restart Claude Code, then run `/mcp` to verify `shadcn` shows as `Connected`.

## Other clients

| Client    | Command                                           | Config file                   |
|-----------|---------------------------------------------------|-------------------------------|
| Cursor    | `npx shadcn@latest mcp init --client cursor`      | `.cursor/mcp.json`            |
| VS Code   | `npx shadcn@latest mcp init --client vscode`      | `.vscode/mcp.json`            |
| OpenCode  | `npx shadcn@latest mcp init --client opencode`    | auto                          |
| Codex     | `npx shadcn@latest mcp init --client codex`       | manual `~/.codex/config.toml` |

### Codex config.toml (manual)

```toml
[mcp_servers.shadcn]
command = "npx"
args = ["shadcn@latest", "mcp"]
```

## VS Code mcp.json format

```json
{
  "servers": {
    "shadcn": { "command": "npx", "args": ["shadcn@latest", "mcp"] }
  }
}
```

## Example prompts after setup

- "Show me all available components in the shadcn registry"
- "Add the button, dialog and card components to my project"
- "Create a contact form using components from the shadcn registry"
- "Install @internal/auth-form"
- "Build a landing page using hero and features from the acme registry"

Source: (root)/mcp.mdx, registry/mcp.mdx
