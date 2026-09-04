# Installation

Step-by-step guide to add ReUI to a shadcn project. See PREREQUISITES.md before starting, and
REGISTRY-CONFIG.md / LICENSE-SETUP.md for the registry and license mechanics referenced here.

## Contents

- [1. Setup ReUI Registry](#1-setup-reui-registry)
- [2. License key for premium items (summary)](#2-license-key-for-premium-items-summary)
- [Free component install command (from the Registry page)](#free-component-install-command-from-the-registry-page)
- [Components: CLI vs manual](#components-cli-vs-manual)
- [Base UI and Radix UI support](#base-ui-and-radix-ui-support)
- [AI-enhanced workflow (as stated on Get Started / Introduction)](#ai-enhanced-workflow-as-stated-on-get-started-introduction)
- [Source](#source)

## 1. Setup ReUI Registry

Add the ReUI registry namespace to `components.json` and set the component library and style.

```json
{
  ...
  "style": "base-nova",
  ...
  "registries": {
    "@reui": "https://reui.io/r/{style}/{name}.json"
  }
}
```

The `style` field selects the primitive/style family (e.g. `base-nova` for Base UI, or the
`radix-nova` equivalent for Radix UI — see RTL.md, which names both `base-nova` and
`radix-nova` as the style families the shadcn CLI supports). The `{style}` and `{name}`
placeholders in the registry URL are resolved by the shadcn CLI from `components.json` and the
requested item name.

Free `c-*` components can be installed with this config **as-is** — no license key needed.

Some free `c-*` installs also pull shared `@reui/*` primitives (e.g. `@reui/alert`,
`@reui/data-grid`) as registry dependencies. Those supporting registry items remain publicly
accessible, so the free component install flow keeps working without a license.

To install paid blocks, icons, or templates, switch the registry entry to the authenticated
object form (see REGISTRY-CONFIG.md) and send the `REUI_LICENSE_KEY` as a Bearer header.

## 2. License key for premium items (summary)

If premium blocks, icons, or templates will be installed with the shadcn CLI, add a license key
once and keep using the same `@reui` namespace. Full walkthrough: LICENSE-SETUP.md.

### 2a. Add the license key

Create or update `.env.local` in the project root:

```
REUI_LICENSE_KEY=your-license-key-here
```

### 2b. Switch the registry to the authenticated form

Keep the same namespace, add the authorization header to `components.json`:

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

### 2c. Install premium registry items

```
npx shadcn@latest add @reui/banner-1
npx shadcn@latest add @reui/icons/default/solid/all
```

Free `c-*` components keep working with the authenticated config too — no second registry
namespace is needed.

## Free component install command (from the Registry page)

Free examples use the `c-*` naming pattern and install without a license key. Package-manager
forms (pnpm/npm/yarn/bun tabs shown on the docs site):

```
pnpm dlx shadcn@latest add @reui/c-alert-1
```

The npm/yarn/bun equivalents follow the same shadcn CLI `add` invocation with the same
`@reui/<name>` argument; the source page shows a pnpm/npm/yarn/bun tab group but the mirrored
markdown only captured the pnpm form as literal text for this example. The premium install
examples above (`npx shadcn@latest add @reui/banner-1`) show the npx/npm form explicitly. Use
whichever package manager runner the project already uses with `shadcn@latest add <item>`.

## Components: CLI vs manual

Components can be integrated either via the shadcn CLI for automation, or by manual
installation for full control. Both methods support the entire collection of Component Docs and
Components.

## Base UI and Radix UI support

ReUI is primitive-agnostic: Base UI and Radix UI versions exist for each registry entry
(components, examples, and blocks), so the same catalog fits new projects and existing
codebases regardless of which primitive library they use.

## AI-enhanced workflow (as stated on Get Started / Introduction)

- **llms.txt** — a structured map of the documentation and architecture, optimized for AI
  agents.
- **Copy Markdown** — every page includes a Copy Markdown feature to feed documentation or code
  directly into AI-driven workflows.
- The free MCP server at `mcp.reui.io` works with any MCP-capable agent after a quick account
  sign-in, and exposes 18 tools (see the reui-mcp skill's TOOLS.md) covering scored search, real
  component APIs, page composition, and prop validation.
- Free Agent Skills teach the ReUI workflow on top of the MCP server: find the right item,
  install it with the shadcn CLI, read the actual API, and adapt by reuse.

## Source

https://reui.io/docs/get-started, https://reui.io/docs/registry, https://reui.io/docs — mirrored 2026-09-04.
