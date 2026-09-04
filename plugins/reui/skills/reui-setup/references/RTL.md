# RTL (Right-to-Left)

How right-to-left support works in ReUI, what the shadcn CLI converts automatically, and what
must be checked manually.

## Contents

- [Overview](#overview)
- [What the CLI converts](#what-the-cli-converts)
- [What the CLI cannot convert](#what-the-cli-cannot-convert)
- [Where ReUI stands today](#where-reui-stands-today)
- [Checklist for an RTL app](#checklist-for-an-rtl-app)
- [Further reading (named by upstream)](#further-reading-named-by-upstream)
- [Source](#source)

## Overview

ReUI is a standard shadcn registry. It ships the same style families the shadcn CLI supports
(`base-nova`, `radix-nova`, and the rest), so everything the CLI does for RTL on shadcn's own
components, it does identically for ReUI components, blocks, and Motion Icons. **There is no
ReUI-specific RTL mode** to enable and nothing to configure beyond the standard shadcn setup.

Set RTL up once, following the official shadcn/ui RTL documentation — that page is the source of
truth for the `components.json` flag, the `DirectionProvider`, and the framework-specific wiring
for Next.js, Vite, and TanStack Start. This ReUI page only covers what is specific to ReUI.

## What the CLI converts

With RTL enabled in `components.json`, the shadcn CLI rewrites physical Tailwind utilities into
logical ones as code is written into the project. This applies to anything installed from a
registry, ReUI included:

| Category | Physical → Logical |
|---|---|
| Positioning | `left-*` and `right-*` → `start-*` and `end-*` |
| Spacing | `ml-*`, `mr-*`, `pl-*`, `pr-*` → `ms-*`, `me-*`, `ps-*`, `pe-*` |
| Text alignment | `text-left` and `text-right` → `text-start` and `text-end` |
| Borders and radii | `border-l`, `rounded-r` and friends → their `-s` / `-e` equivalents |
| Directional animations | `slide-in-from-right` → `slide-in-from-end` |

This is why ReUI source does not need to be written in logical properties: conversion happens at
install time, on the copy that lands in the repository.

**Existing projects need one migration pass.** Automatic conversion applies to projects created
with `shadcn create` on the new style families. If ReUI was added to an older project, run
`pnpm dlx shadcn@latest migrate rtl [path]` over the installed files once, then keep RTL enabled
so later installs are converted as they arrive.

## What the CLI cannot convert

Class conversion is mechanical and only half of RTL. The other half is behavior, and no CLI can
infer it:

- **Drag and drop.** Pointer deltas are signed. A grid, Kanban, or Gantt that reorders on a
  positive x delta needs that sign flipped under RTL.
- **Scroll position.** Horizontal scroll origin differs in RTL, affecting virtualized grids,
  timelines, and anything that restores a saved `scrollLeft`.
- **Charts.** Axis placement and series direction come from the charting library's own
  configuration, not from Tailwind classes.
- **Icons that encode direction.** Chevrons and arrows need `rtl:rotate-180`; a check mark or a
  spinner must not be flipped.
- **Content order.** Whether a sidebar belongs on the start or end edge is a product decision,
  not a styling one.

## Where ReUI stands today

Stated plainly by upstream, not softened here:

- **Primitives** are written predominantly with logical properties already, so they degrade well
  before any conversion runs. Exceptions with real geometry: the **Data Grid table** and the
  **Gantt drag layer**, both of which compute positions in JavaScript — the first places to check
  if something reads wrong.
- **Blocks** are presentational compositions on those primitives and shadcn components, authored
  the way shadcn's own examples are (physical utilities in places); the CLI's RTL transform
  converts them on install. Because a block is layout rather than logic, class conversion covers
  most of what a block needs.
- **Not yet done, budget for it.** No RTL preview toggle on block pages, no RTL test suite, no
  per-block certification list exists. The interactive primitives — **Data Grid, Gantt, Event
  Calendar, Kanban, Filters, App Shell** — have not been formally verified in RTL, and those are
  exactly where the behavioral issues above live. For an Arabic-first or Hebrew-first product:
  treat static blocks as low-risk, and plan a review pass over the interactive ones — verify
  column order, sidebar edge, drag direction, horizontal scroll, and chart axes against your own
  designs.
- Upstream invites reports: "Tell us the block or primitive and what breaks."

## Checklist for an RTL app

1. **Enable RTL in shadcn.** Follow the shadcn RTL guide: set the flag in `components.json`, add
   the `DirectionProvider` for the framework. Do this **before** installing ReUI items so they
   are converted on the way in.
2. **Install ReUI items as usual** — nothing changes in the command:
   ```
   pnpm dlx shadcn@latest add @reui/c-data-grid-30
   ```
   The registry is the same; the CLI applies the RTL transform to what it writes.
3. **Review interactive surfaces.** For each Data Grid, Gantt, Event Calendar, Kanban, or Filters
   instance, check the five behaviors class conversion cannot reach: column order, drag
   direction, horizontal scroll, chart axes, and any icon that points somewhere.
4. **Flip only the icons that mean direction.** Add `rtl:rotate-180` to chevrons, arrows, and
   carets. Leave symbolic icons alone.

## Further reading (named by upstream)

- shadcn/ui RTL documentation — setup, the `DirectionProvider`, the full conversion list, and
  known caveats.
- Styling — ReUI's extended token system, stated to be direction-independent (see the
  reui-theming skill's TOKENS.md).

## Source

https://reui.io/docs/rtl — mirrored 2026-09-04.
