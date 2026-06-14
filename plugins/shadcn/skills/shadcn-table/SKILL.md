---
name: shadcn-table
description: >
  shadcn/ui Table component — responsive data table, Table, TableHeader, TableBody,
  TableFooter, TableRow, TableHead, TableCell, TableCaption, Tabelle, Datentabelle,
  shadcn table, HTML table component, data table
---

# shadcn/ui Table

A responsive table component built on native HTML table elements with styled sub-components.
No external primitive dependency — pure HTML with Tailwind styling.

## Quick Reference

- **Install**: `npx shadcn@latest add table`
- **Deps**: none (no external primitive)
- **Exports**: `Table`, `TableHeader`, `TableBody`, `TableFooter`, `TableRow`, `TableHead`, `TableCell`, `TableCaption`
- **Advanced**: Combine with @tanstack/react-table for sorting, filtering, pagination — see [Data Table](/docs/components/data-table)

## Composition

```text
Table
├── TableCaption
├── TableHeader
│   └── TableRow
│       └── TableHead (multiple)
├── TableBody
│   └── TableRow (multiple)
│       └── TableCell (multiple)
└── TableFooter
    └── TableRow
```

## Reference files

- [installation.md](references/installation.md) — CLI & manual setup
- [source.md](references/source.md) — Complete component source
- [api.md](references/api.md) — Sub-component props
- [examples.md](references/examples.md) — All examples
