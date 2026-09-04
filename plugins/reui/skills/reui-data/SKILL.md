---
name: reui-data
description: Full APIs of the ReUI data primitives: data-grid, filters, cascader, gantt, event-calendar, tree, date-selector, code-block. Use when building with @reui/data-grid or @reui/filters.
---

# ReUI data components

The primitives shadcn/ui does not solve. All **free** — no licence key — and all installed with
`npx shadcn@latest add @reui/<name> --yes`.

Never hand-roll one of these. A bespoke `<table>` where `@reui/data-grid` fits, or a hand-built
board instead of the real component, is the failure this plugin exists to prevent.

## Read your build first

`components.json` → `style` decides which API your code must target: `base-nova` → Base UI,
`radix-nova` → Radix UI. The CLI installs the matching variant on its own — never pass a style. For
most components the two differ only in import paths; where they differ in props, each reference
file says so in its **Base UI vs Radix UI** section.

## Where the API comes from

1. **The MCP**, when it answers: one **batched** `get_component` over every name the item uses, then
   `get_examples` to install a real composition and copy it.
2. **These reference files**, when it cannot — quota spent, signed out, offline.
3. **The files the install added**, which outrank both for what is actually available right now.

Never write a prop you have not read in one of the three.

## Reference map

- **[DATA-GRID.md](references/DATA-GRID.md)**: TanStack Table v9 grid — sorting, filtering,
  pagination, row and column virtualization, drag-and-drop, row pinning, tree rows, cell selection
  with clipboard, inline editing, i18n —
  with [DATA-GRID-EXAMPLE.md](references/DATA-GRID-EXAMPLE.md) as the worked composition.
- **[FILTERS.md](references/FILTERS.md)**: the stepped filter builder — nested attributes, popover
  value editors, the boolean query tree —
  with [FILTERS-API.md](references/FILTERS-API.md) as the exhaustive API (349 prop rows, every
  sub-component, type, i18n key, hook, keyboard and accessibility contract) and
  [FILTERS-EXAMPLES.md](references/FILTERS-EXAMPLES.md) as the six worked sources.
- **[CASCADER.md](references/CASCADER.md)**: nested multi-level combobox with drill-down,
  breadcrumbs, search and custom rows.
- **[GANTT.md](references/GANTT.md)**: split tree and timeline panes, day-to-year scales, zoom, drag
  and resize scheduling, progress and summary rollups —
  with [GANTT-EXAMPLES.md](references/GANTT-EXAMPLES.md) as the worked compositions.
- **[EVENT-CALENDAR.md](references/EVENT-CALENDAR.md)**: month, week, day, N-day and agenda views,
  drag-and-drop scheduling, recurring events, time zones, the external CRUD contract —
  with [EVENT-CALENDAR-EXAMPLE.md](references/EVENT-CALENDAR-EXAMPLE.md) as the worked composition.
- **[TREE.md](references/TREE.md)**: hierarchical tree with selection and expansion.
- **[DATE-SELECTOR.md](references/DATE-SELECTOR.md)**: period types, filter modes, display options.
- **[CODE-BLOCK.md](references/CODE-BLOCK.md)**: Shiki highlighting, streaming, diffs, folding and
  per-line interaction for AI and agent UIs —
  with [CODE-BLOCK-EXAMPLES.md](references/CODE-BLOCK-EXAMPLES.md) as the worked compositions.

The examples that show real composition are the free `c-*` items — `c-data-grid-3`, `c-kanban-1` and
the rest are listed in
[reui-registry/EXAMPLES-FREE.md](../reui-registry/references/EXAMPLES-FREE.md).

## Source

Distilled from `https://reui.io/docs/components/base/<name>` and its `radix` twin, mirrored
2026-09-04.
