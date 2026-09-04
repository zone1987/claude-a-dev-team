---
name: reui-registry
description: Which ReUI registry items install free and which need a Pro or Ultimate licence, with every primitive, example and block by name. Use when the request names ReUI, @reui or REUI_LICENSE_KEY.
---

# The ReUI registry

ReUI is a shadcn-compatible registry reached through one namespace, `@reui`. Everything installs
with the shadcn CLI; the licence is checked by the server at install time, not by the CLI.

**Ask the MCP first.** `mcp__reui__search` answers against the live registry and returns an install
command, a preview URL and the components an item uses. The reference files below are the fallback
for when it cannot answer — a spent free quota, an expired sign-in, no network.

## The one rule that decides everything

An item's name tells you what it costs:

| Name shape | Tier | Licence at install |
|---|---|---|
| `@reui/c-<component>-<n>` | free example (1,105) | none |
| `@reui/<component>` | free primitive (23, 81 files) | none |
| anything else — `app-shell-3`, `hero-11`, `solution-crm-2` | premium block (533) | **Pro** |
| `@reui/icons/<default\|animated>/<style>/<name>` | icon (638) | **Ultimate** |
| a full-page template (14) | template | **Ultimate** |

A premium install without `REUI_LICENSE_KEY` **and** the authenticated registry form fails with a
401 after resolving dependencies. Check both before proposing one — see
[reui-setup](../reui-setup/SKILL.md).

## Reference map

- **[FREE-VS-PREMIUM.md](references/FREE-VS-PREMIUM.md)**: the tier table with exact counts, the six
  premium groups, and how to read a tier off a name. Generated from `registry.json`.
- **[PRIMITIVES.md](references/PRIMITIVES.md)**: all 77 `registry:ui` items and 4 hooks with their
  npm and `@reui` dependencies, grouped into the families you install.
- **[EXAMPLES-FREE.md](references/EXAMPLES-FREE.md)**: all 1,105 free `c-*` examples across 74
  families, by name.
- Premium blocks live in [reui-blocks](../reui-blocks/SKILL.md).

## Without the MCP

The shadcn CLI reaches the same registry directly:

```bash
npx shadcn@latest search @reui -q "data grid"
npx shadcn@latest add @reui/c-data-grid-3 --yes
```

No scoring and no inline API, but the install path is unchanged. `https://reui.io/llms.txt` is the
upstream index of every category.

## Source

Generated from [`https://reui.io/r/registry.json`](https://reui.io/r/registry.json),
sha256 `a598d3b8b544a0fa1fc834d7a590b2b04642c080890c46790c7a5df5e1ea239f`, 1,719 items, mirrored
2026-09-04. Counts cross-checked against [`https://reui.io/llms.txt`](https://reui.io/llms.txt).
