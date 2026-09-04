---
name: reui-layout
description: Full APIs of the ReUI layout primitives: kanban, sortable, timeline, frame, alert, badge, scrollspy, icon-stack, icon-tile. Use when building with @reui/kanban or @reui/sortable.
---

# ReUI layout and display primitives

Structure, ordering and status components. All **free** — no licence key — installed with
`npx shadcn@latest add @reui/<name> --yes`.

## Read your build first

`components.json` → `style`: `base-nova` → Base UI, `radix-nova` → Radix UI. Write against that
build's API; the CLI installs the right variant on its own. Each file records the real difference in
its **Base UI vs Radix UI** section.

## Alert and badge carry extended tokens

ReUI's `alert` and `badge` use semantic tokens plain shadcn/ui does not define — `--success`,
`--info`, `--warning`, `--invert` and their foreground pairs. A project that never defines them
renders these variants with the wrong colours. The values are in
[reui-theming/TOKENS.md](../reui-theming/references/TOKENS.md).

## Reference map

- **[KANBAN.md](references/KANBAN.md)**: drag-and-drop board across customizable columns.
- **[SORTABLE.md](references/SORTABLE.md)**: drag-and-drop reordering — vertical, grid and nested.
- **[TIMELINE.md](references/TIMELINE.md)**: events in chronological order.
- **[FRAME.md](references/FRAME.md)**: related content in a structured frame.
- **[ALERT.md](references/ALERT.md)**: callouts, with the variant-to-token mapping.
- **[BADGE.md](references/BADGE.md)**: status and count indicators, with the variant-to-token mapping.
- **[SCROLLSPY.md](references/SCROLLSPY.md)**: highlights navigation for the section in view.
- **[ICON-STACK.md](references/ICON-STACK.md)**: layered and isometric icon illustrations.
- **[ICON-TILE.md](references/ICON-TILE.md)**: an icon on a consistent square surface.

## Source

Distilled from `https://reui.io/docs/components/base/<name>` and its `radix` twin, mirrored
2026-09-04.
