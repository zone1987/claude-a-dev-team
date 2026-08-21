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

- [TABLE-INSTALLATION.md](TABLE-INSTALLATION.md) — CLI & manual setup
- [TABLE-SOURCE.md](TABLE-SOURCE.md) — Complete component source
- [TABLE-API.md](TABLE-API.md) — Sub-component props
- [TABLE-EXAMPLES.md](TABLE-EXAMPLES.md) — All examples
