# Data Table — API Reference

TanStack Table docs: https://tanstack.com/table/v8/docs

---

## Installation imports

```ts
import {
  FlexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getExpandedRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useVueTable,
} from '@tanstack/vue-table'
```

---

## useVueTable options

| Option                    | Type / Import           | Description                          |
| :------------------------ | :---------------------- | :----------------------------------- |
| `data`                    | getter `() => TData[]`  | Reactive data array                  |
| `columns`                 | `ColumnDef<TData>[]`    | Column definitions                   |
| `getCoreRowModel`         | `getCoreRowModel()`     | Required base row model              |
| `getPaginationRowModel`   | `getPaginationRowModel()` | Enables pagination              |
| `getSortedRowModel`       | `getSortedRowModel()`   | Enables column sorting               |
| `getFilteredRowModel`     | `getFilteredRowModel()` | Enables column filtering             |
| `getExpandedRowModel`     | `getExpandedRowModel()` | Enables row expanding                |
| `onSortingChange`         | `(u) => valueUpdater(u, sorting)` | Sync sorting state      |
| `onColumnFiltersChange`   | `(u) => valueUpdater(u, columnFilters)` | Sync filters    |
| `onColumnVisibilityChange`| `(u) => valueUpdater(u, columnVisibility)` | Sync visibility |
| `onRowSelectionChange`    | `(u) => valueUpdater(u, rowSelection)` | Sync selection    |
| `onExpandedChange`        | `(u) => valueUpdater(u, expanded)` | Sync expanded state      |
| `state`                   | object with getters     | Reflect Vue refs back to table       |

**Note:** Use getter syntax `get data() { return props.data }` to keep
reactivity working with TanStack Table.

---

## State refs

```ts
const sorting = ref<SortingState>([])
const columnFilters = ref<ColumnFiltersState>([])
const columnVisibility = ref<VisibilityState>({})
const rowSelection = ref({})
const expanded = ref<ExpandedState>({})
```

---

## ColumnDef shape

```ts
interface ColumnDef<TData> {
  id?: string               // required if no accessorKey
  accessorKey?: keyof TData // dot-notation supported
  header?: string | (ctx) => VNode
  cell?: (ctx) => VNode
  enableSorting?: boolean   // default true
  enableHiding?: boolean    // default true
  enableColumnFilter?: boolean
}
```

---

## table instance methods

| Method                           | Description                              |
| :------------------------------- | :--------------------------------------- |
| `table.getHeaderGroups()`        | Array of header group objects            |
| `table.getRowModel().rows`       | Current page rows                        |
| `table.getAllColumns()`          | All columns including hidden             |
| `table.getColumn(id)`           | Get column by id                         |
| `table.getCanPreviousPage()`     | Boolean                                  |
| `table.getCanNextPage()`         | Boolean                                  |
| `table.previousPage()`           | Go to previous page                      |
| `table.nextPage()`               | Go to next page                          |
| `table.setPageIndex(n)`          | Jump to page n                           |
| `table.getPageCount()`           | Total page count                         |
| `table.getState()`               | Current table state                      |
| `table.getFilteredRowModel()`    | All filtered rows (not paginated)        |
| `table.getFilteredSelectedRowModel()` | Selected rows from filtered set   |
| `table.getIsAllPageRowsSelected()` | Boolean                                |
| `table.toggleAllPageRowsSelected(bool)` | Select/deselect all on page     |
| `table.setPageSize(n)`           | Change page size                         |

---

## Row methods

| Method                    | Description                                |
| :------------------------ | :----------------------------------------- |
| `row.original`            | Original data object                       |
| `row.getValue(key)`       | Typed cell value                           |
| `row.getIsSelected()`     | Boolean                                    |
| `row.toggleSelected(bool)` | Select/deselect row                       |
| `row.getIsExpanded()`     | Boolean                                    |
| `row.toggleExpanded()`    | Toggle row expanded                        |
| `row.getVisibleCells()`   | Visible cells for this row                 |
| `row.getAllCells()`        | All cells (for colspan on expand)          |

---

## Column methods

| Method                         | Description                             |
| :----------------------------- | :-------------------------------------- |
| `column.getFilterValue()`      | Current filter value                    |
| `column.setFilterValue(v)`     | Set filter value                        |
| `column.getIsSorted()`         | `'asc' | 'desc' | false`                |
| `column.toggleSorting(desc?)`  | Toggle sort direction                   |
| `column.getCanSort()`          | Boolean                                 |
| `column.getCanHide()`          | Boolean                                 |
| `column.getIsVisible()`        | Boolean                                 |
| `column.toggleVisibility(bool)`| Show/hide column                        |

---

## valueUpdater utility

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

---

## FlexRender

Renders either a string/VNode or a render function as a Vue template.

```vue
<FlexRender
  v-if="!header.isPlaceholder"
  :render="header.column.columnDef.header"
  :props="header.getContext()"
/>
```

---

## Cell Formatting example (currency)

```ts
{
  accessorKey: 'amount',
  header: () => h('div', { class: 'text-right' }, 'Amount'),
  cell: ({ row }) => {
    const amount = Number.parseFloat(row.getValue('amount'))
    const formatted = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(amount)
    return h('div', { class: 'text-right font-medium' }, formatted)
  },
}
```
