# License Setup

Configure a ReUI license key for premium registry installs.

Use this guide to install premium ReUI registry items with the shadcn CLI. Free components do
not require a license key; premium blocks, icons, and templates do.

## Contents

- [Your license key](#your-license-key)
- [CLI installation (recommended path)](#cli-installation-recommended-path)
- [Monorepo (Turborepo)](#monorepo-turborepo)
- [Manual copy & paste](#manual-copy-paste)
- [Related guides](#related-guides)
- [Source](#source)

## Your license key

The license key comes from the ReUI account (Account → Licenses). The docs page states: "You
need to be logged in to see your license key."

## CLI installation (recommended path)

### Prerequisites

- A React project with shadcn/ui initialized
- Node.js 18 or newer
- A `components.json` file in the project root

### 1. Add the license key

`.env.local` in the project root:

```
REUI_LICENSE_KEY=your-license-key-here
```

### 2. Point components.json at the authenticated @reui registry

```json
{
  "registries": {
    "@reui": {
      "url": "https://reui.io/r/{style}/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REUI_LICENSE_KEY}"
      }
    }
  }
}
```

The shadcn CLI expands `${REUI_LICENSE_KEY}` from the environment, so leave it as a variable
here.

**A ReUI MCP server entry is a separate config with its own rules**, and substitution syntax
differs by client:
- Claude Code expands `${VAR}` in `.mcp.json`
- Cursor only understands the `env:` prefix (`${env:NAME}`)
- Codex reads the value from `bearer_token_env_var`
- Antigravity's `mcp_config.json` documents no substitution at all — the real token must be
  pasted in there

Check the specific agent's guide before copying this `components.json` line into an MCP config.
Create an MCP personal token at Account → MCP (see the reui-mcp skill's AUTHENTICATION.md).

### 3. Install registry items

```
pnpm dlx shadcn@latest add @reui/c-data-grid-1
```

Free components continue to work with the authenticated config, so no second registry namespace
is needed.

## Monorepo (Turborepo)

Installing into a shared package (e.g. `packages/ui`) works the same way, with three things to
get right. All three follow from one rule: **the CLI reads `components.json` and `.env.local`
from the directory it runs in, and looks nowhere else.**

### Put components.json in the package, not the repo root

Every workspace needs its own `components.json`; the `@reui` registry block belongs in the one
installed from:

`packages/ui/components.json`
```json
{
  "aliases": {
    "components": "@workspace/ui/components",
    "ui": "@workspace/ui/components",
    "lib": "@workspace/ui/lib",
    "hooks": "@workspace/ui/hooks",
    "utils": "@workspace/ui/lib/utils"
  },
  "registries": {
    "@reui": {
      "url": "https://reui.io/r/{style}/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REUI_LICENSE_KEY}"
      }
    }
  }
}
```

The `aliases` are what land the files in `packages/ui` instead of in an app.

### Keep the key next to it

The CLI loads `.env.local` from the directory it runs in and does not walk up to parent
folders, so a key kept only in the repo root's `.env.local` is never seen. That produces the
error `Registry "@reui" requires the following environment variables`, which stops before any
request is made:

`packages/ui/.env.local`
```
REUI_LICENSE_KEY=your-license-key-here
```

### Run the install from the package

```
cd packages/ui
npx shadcn@latest add @reui/c-data-grid-1
```

Or stay at the repo root and point the CLI at the package (this is what the CLI suggests itself
when run from the root):

```
pnpm dlx shadcn@latest add -c packages/ui @reui/c-data-grid-1
```

Running from a directory whose `components.json` has no `@reui` block (the root, or an app) is
the other way this fails: the CLI falls back to shadcn's public directory entry for `@reui`,
which carries no license header, so reui.io answers `You are not authorized to access the item`
even though the key is set.

Consuming apps import as usual and need no license key of their own:

```ts
import { DataGrid } from "@workspace/ui/components/data-grid"
```

Prefer shadcn's own monorepo layout where installs run from `apps/web`? That works too: put the
same `registries` block and `.env.local` in `apps/web` instead. The `ui` alias still lands the
files in `packages/ui`.

**Passing the key from shell/CI env through a `turbo` task:** Turborepo 2 defaults to strict
environment mode, which hands a task only the variables declared in `turbo.json`, so add
`REUI_LICENSE_KEY` to `globalEnv` there. With the key in `packages/ui/.env.local` this does not
apply: the CLI reads that file itself, inside the task.

## Manual copy & paste

An alternative to the CLI: browse and copy code directly.
- Browse premium sections in Blocks
- Browse premium icon packs in Icons
- See plan details in Pricing (see PLANS.md)

## Related guides

- Get Started (INSTALLATION.md)
- Registry (REGISTRY-CONFIG.md)

## Source

https://reui.io/docs/license-setup — mirrored 2026-09-04.
