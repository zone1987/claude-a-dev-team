# Registry Configuration

How the ReUI shadcn registry works and how `components.json` is configured.

## Single namespace

The ReUI Registry uses a single `@reui` namespace for free `c-*` components, paid blocks, paid
icons, and paid templates. The shadcn CLI resolves the full alias suffix into the registry URL,
so everything installs from one namespace and ReUI handles access rules server-side.

## Plain string form (free items only)

```json
{
  "registries": {
    "@reui": "https://reui.io/r/{style}/{name}.json"
  }
}
```

## Authenticated object form (required for premium items)

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

The shadcn CLI expands `${REUI_LICENSE_KEY}` from the environment (`.env.local`) when reading
`components.json`. This is CLI-side expansion only — it has no relationship to how any given MCP
client expands (or does not expand) placeholders in its own MCP config file. See the reui-mcp
skill's AUTHENTICATION.md for the per-client differences on that separate config.

Free items keep working under the authenticated config too, so a second registry namespace is
never needed.

## Free components

Free component examples use the `c-*` naming pattern and install without a license key:

```
pnpm dlx shadcn@latest add @reui/c-alert-1
```

Some free `c-*` items pull shared `@reui/*` primitives (such as `@reui/alert` or
`@reui/data-grid`) as registry dependencies. Those supporting files remain publicly accessible,
so free component installs keep working even without a license.

## Paid blocks, icons, and templates

Premium blocks, icons, and templates use the same `@reui` namespace but require a valid license
key (see LICENSE-SETUP.md and PLANS.md for what unlocks them).

Steps:
1. Add the license key to `.env.local`: `REUI_LICENSE_KEY=your-license-key`
2. Change the registry entry to the authenticated object form (above).
3. Install premium items from the same namespace:

```
pnpm dlx shadcn@latest add @reui/banner-1
npx shadcn@latest add @reui/icons/default/solid/all
```

## Monorepo (Turborepo) — where components.json and .env.local must live

Covered in full in LICENSE-SETUP.md's Monorepo section; summarized here because it is a registry
config fact:

The shadcn CLI reads `components.json` and `.env.local` only from the directory it is run in —
it does not walk up to parent directories. In a Turborepo-style monorepo:

- Put `components.json` (with the `@reui` registries block and correct `aliases`) in the
  **package** you install into (e.g. `packages/ui/components.json`), not the repo root.
- Put `.env.local` with `REUI_LICENSE_KEY` **next to that `components.json`** — a key only in the
  repo root's `.env.local` is never seen and produces:
  `Registry "@reui" requires the following environment variables` (fails before any request is
  made).
- Run the install from that package directory, or from the repo root with `-c <path>`:
  `pnpm dlx shadcn@latest add -c packages/ui @reui/c-data-grid-1`.
- Running the install from a directory whose `components.json` has no `@reui` block (root, or an
  app) makes the CLI fall back to shadcn's public directory entry for `@reui`, which carries no
  license header — reui.io then answers `You are not authorized to access the item` even though
  the key is set elsewhere.
- Passing the key via CI/shell env through a Turborepo `turbo` task: Turborepo 2 defaults to
  strict environment mode, so a task only receives variables declared in `turbo.json`'s
  `globalEnv`; add `REUI_LICENSE_KEY` there if using this path. This does not apply when the key
  lives in `packages/ui/.env.local`, since the CLI reads that file itself, inside the task.

Full detail (including apps/web-style monorepo layout) is in LICENSE-SETUP.md.

## Source

https://reui.io/docs/registry, https://reui.io/docs/license-setup — mirrored 2026-09-04.
