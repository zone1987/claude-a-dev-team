# Data Table — Installation

The Data Table is a guide pattern — not a single installable component.
It uses the `<Table />` component from shadcn-vue plus TanStack Table.

## Step 1: Add the Table component

```bash
npx shadcn-vue@latest add table
```

## Step 2: Install TanStack Table

```bash
npm install @tanstack/vue-table
```

## File structure (recommended)

```
components/
  payments/
    columns.ts          — ColumnDef definitions
    data-table.vue      — <DataTable /> component
    data-table-dropdown.vue  — Row actions dropdown
app.vue                 — Fetch data + render table
```

## valueUpdater utility

TanStack Table state changes use an `Updater<T>` — either a direct value
or a function `(prev: T) => T`. Add this helper to your `lib/utils.ts`:

```ts
import type { Updater } from '@tanstack/vue-table'
import type { Ref } from 'vue'

export function valueUpdater<T extends Updater<any>>(
  updaterOrValue: T,
  ref: Ref,
) {
  ref.value = typeof updaterOrValue === 'function'
    ? updaterOrValue(ref.value)
    : updaterOrValue
}
```

## Prerequisites: data shape

```ts
interface Payment {
  id: string
  amount: number
  status: 'pending' | 'processing' | 'success' | 'failed'
  email: string
}

export const payments: Payment[] = [
  { id: '728ed52f', amount: 100, status: 'pending',
    email: 'm@example.com' },
  { id: '489e1d42', amount: 125, status: 'processing',
    email: 'example@gmail.com' },
  // ...
]
```

## Source location

Documentation: `apps/v4/content/docs/components/data-table.md`
(data-table has no `ui/` directory — it is a guide-only composite)
