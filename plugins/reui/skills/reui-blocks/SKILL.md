---
name: reui-blocks
description: The 533 premium ReUI blocks by group, plus icons and templates: what each composes and which licence it needs. Use when the request names a ReUI block or @reui/icons.
---

# Premium ReUI blocks

A block is a full page or section composed from ReUI primitives and shadcn components. All 533 need
a **Pro or Ultimate** licence at install; icons and templates need **Ultimate**.

**Ask the MCP first.** `mcp__reui__compose_page` turns a whole-page intent into ordered sections,
each matched to the best block — use it before searching block by block. `mcp__reui__search` handles
single sections. The references below are the fallback when the MCP cannot answer.

## Before installing any of these

Both halves must be in place or the install fails with a 401:

1. `REUI_LICENSE_KEY` in `.env.local` (or the environment).
2. The `@reui` entry in `components.json` in its **authenticated object form**, carrying
   `"Authorization": "Bearer ${REUI_LICENSE_KEY}"`.

The plain string form installs free items only. Full walkthrough:
[reui-setup/LICENSE-SETUP.md](../reui-setup/references/LICENSE-SETUP.md).

## The six groups

| Group | Blocks | Reference |
|---|---|---|
| Application | 292 | [BLOCKS-APPLICATION.md](references/BLOCKS-APPLICATION.md) |
| eCommerce | 87 | [BLOCKS-ECOMMERCE.md](references/BLOCKS-ECOMMERCE.md) |
| Solutions | 65 | [BLOCKS-SOLUTIONS.md](references/BLOCKS-SOLUTIONS.md) |
| Marketing | 40 | [BLOCKS-MARKETING.md](references/BLOCKS-MARKETING.md) |
| Data Grid | 37 | [BLOCKS-DATA-GRID.md](references/BLOCKS-DATA-GRID.md) |
| AI & Agents | 12 | [BLOCKS-AI-AGENTS.md](references/BLOCKS-AI-AGENTS.md) |

Each entry carries the block's title, its description, the `@reui` primitives it composes and its npm
dependencies — enough to judge a fit and to know what an install pulls in.
[BLOCKS-PREMIUM.md](references/BLOCKS-PREMIUM.md) is the index across all six.

## Adapt, do not redesign

A block arrives already themed against your semantic tokens. After `add`: read the installed files,
keep the composition, swap the demo data for real data, fix icon imports, and leave the styling to
the theme. Output that looks generic means the design was reused too little, not that it needs
restyling.

- **[ADAPTING.md](references/ADAPTING.md)**: reuse-first — preserve the design, reuse a block's own
  elements, wire real data, and never invent an API.
- **[CRAFT.md](references/CRAFT.md)**: the bar an adaptation has to hold — hierarchy, deliberate
  density, the empty, loading and error states, responsive, restrained motion, and the AI tells that
  give a generated surface away.
- **[QUALITY-GATES.md](references/QUALITY-GATES.md)**: the done gate — security, accessibility and
  scroll mechanics. Clear every item, and run the MCP `get_audit_checklist` when it is reachable.
- **[ICONS.md](references/ICONS.md)**: portable icons and the `iconLibrary` import mappings, plus
  the Motion Icon install paths.

## Icons and templates (Ultimate)

- Icons: 638 in 4 styles, 2,552 variants. Static `@reui/icons/default/<style>/<name>`, hover-animated
  `@reui/icons/animated/<style>/<name>`. `mcp__reui__search_icons` batches up to 24 concepts per call.
- Templates: 14 full-page templates.

Neither is served in `registry.json` — `/r/icons.json` answers 401 without a licence — so no offline
name list exists for them here. The MCP or reui.io is the only index.

## Source

Generated from [`https://reui.io/r/registry.json`](https://reui.io/r/registry.json),
sha256 `a598d3b8b544a0fa1fc834d7a590b2b04642c080890c46790c7a5df5e1ea239f`, mirrored 2026-09-04.
Icon and template counts from [`https://reui.io/llms.txt`](https://reui.io/llms.txt).
