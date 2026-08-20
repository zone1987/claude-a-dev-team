# Data Table — Installation

## Required Dependencies

1. Add the `Table` component:

```bash
npx shadcn@latest add table
```

2. Install TanStack Table:

```bash
npm install @tanstack/react-table
```

## Project Structure

The recommended file layout for a data table feature:

```txt
app
└── payments
    ├── columns.tsx     (client component — column definitions)
    ├── data-table.tsx  (client component — DataTable component)
    └── page.tsx        (server component — fetch data + render)
```

## Links

- TanStack Table docs: https://tanstack.com/table/v8/docs/introduction
- TanStack Table headless UI: https://tanstack.com/table/v8/docs/introduction#what-is-headless-ui

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/data-table.mdx`_
