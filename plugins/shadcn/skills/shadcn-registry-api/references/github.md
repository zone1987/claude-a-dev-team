# GitHub Registries

Any public GitHub repository can become a registry by adding `registry.json`
at the root.

## Install syntax

```bash
npx shadcn@latest add <owner>/<repo>/<item>
npx shadcn@latest add acme/toolkit/project-conventions
```

Item names containing `/` are resolved as registry item names, not file paths.
Addresses ending in `.json` are treated as file paths.

## Requirements

- Public `github.com` repository
- `registry.json` at the repository root
- Valid `registry.json` and `registry-item.json` schemas
- Referenced source files must exist in the repo

Private repos and GitHub Enterprise are NOT supported via GitHub addresses.
Use a namespace with authentication for those.

## Setup

1. Create `registry.json` at repo root.
2. Define items with `"type": "registry:item"` and `"target"` on every file.
3. Commit and push.

```json title="registry.json"
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme-toolkit",
  "homepage": "https://github.com/acme/toolkit",
  "items": [
    {
      "name": "project-conventions",
      "type": "registry:item",
      "title": "Project Conventions",
      "description": "Shared editor settings and agent instructions.",
      "files": [
        {
          "path": "AGENTS.md",
          "type": "registry:file",
          "target": "~/AGENTS.md"
        },
        {
          "path": ".editorconfig",
          "type": "registry:file",
          "target": "~/.editorconfig"
        }
      ]
    }
  ]
}
```

## Refs (#ref)

Install from a branch, tag, or commit SHA:

```bash
npx shadcn@latest add acme/toolkit/conventions#main
npx shadcn@latest add acme/toolkit/conventions#v1.0.0
npx shadcn@latest add acme/toolkit/conventions#c0ffee254729296a45d6691db565cf707a3fef5d
```

Refs can contain slashes. Omitting `#ref` uses the default branch.
Full 40-character SHAs are used directly (no Git needed).

## Same-repository dependencies

Use full GitHub item addresses for same-repo deps (NOT bare names):

```json
{
  "registryDependencies": [
    "acme/toolkit/agent-rules",
    "acme/toolkit/tsconfig#v1.0.0"
  ]
}
```

Bare names like `button` resolve to the official shadcn/ui registry.
Refs are not inherited — pin each dep separately.

## External registry dependencies

```json
{
  "registryDependencies": [
    "@acme/tsconfig",
    "contoso/devtools/prettier-config"
  ]
}
```

## Organize with include

```json title="registry.json"
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme-toolkit",
  "homepage": "https://github.com/acme/toolkit",
  "include": ["config/registry.json", "rules/registry.json"]
}
```

File paths in included files are relative to the including `registry.json`.

## Useful commands

```bash
# List all items
npx shadcn@latest list acme/toolkit

# Search
npx shadcn@latest search acme/toolkit -q conventions

# Validate
npx shadcn@latest registry validate acme/toolkit
npx shadcn@latest registry validate acme/toolkit#v1.0.0

# View item payload
npx shadcn@latest view acme/toolkit/project-conventions

# Dry run (preview without writing)
npx shadcn@latest add acme/toolkit/project-conventions --dry-run

# Show diff before installing
npx shadcn@latest add acme/toolkit/project-conventions --diff
```

## What you can distribute

Components, helpers/utilities, design system packages, feature kits, agent
workflows (`AGENTS.md`, `.cursor/rules/*`, `.claude/commands/*`), project
conventions, codemods, testing setup, CI workflows, GitHub templates, and
MCP configuration (`.mcp.json`, `.cursor/mcp.json`).

Source: registry/github.mdx
