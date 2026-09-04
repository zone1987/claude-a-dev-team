# Data Grid — worked example

Part of [DATA-GRID.md](./DATA-GRID.md). Free component — no licence key required. Base UI build (see
[DATA-GRID.md#base-ui-vs-radix-ui](./DATA-GRID.md#base-ui-vs-radix-ui) for the Radix diff).

## Contents

- [Scope note](#scope-note)
- [Representative demo (sorting, pagination, basic columns)](#representative-demo-sorting-pagination-basic-columns)
- [Source](#source)

## Scope note

The mirrored `docs/components/base/data-grid` page is ~11,150 lines and embeds 12 full `Pattern()`
demo components after the API Reference / DOM Attributes sections (not the same as the 10 headed
"Examples" earlier on the page, which print no inline code — see
[DATA-GRID.md#examples](./DATA-GRID.md#examples)). Reproducing all 12 in full is outside what this
reference distillation can carry; every **prop, type, default, and behavioural rule** those demos
would exercise is already captured verbatim in [DATA-GRID.md](./DATA-GRID.md)'s API Reference. What
follows is the first and simplest of the 12 demos, reproduced in full as a representative, complete,
runnable pattern — basic sorting, pagination, and column definitions with `meta.headerClassName` /
`meta.cellClassName`.

The other 11 embedded demos progressively add: column filtering with `DataGridColumnHeader` /
`DataGridColumnFilter`, column visibility toggling, column and row drag-and-drop
(`DataGridTableDnd` / `DataGridTableDndRows`), row pinning (`DataGridTableRowPin`), tree rows
(`DataGridTableRowExpand`), row virtualization and infinite scroll (`DataGridTableVirtual`),
spreadsheet cell selection and editing (`DataGridCellSelection`, `meta.cellEdit`, the fill handle),
and a toast-on-copy integration (`onCellsCopy` wired to a Toast — this is the demo whose toast
import differs between Base UI and Radix UI builds, see
[DATA-GRID.md#base-ui-vs-radix-ui](./DATA-GRID.md#base-ui-vs-radix-ui)). Every API surface named in
that list has its own full prop table in [DATA-GRID.md](./DATA-GRID.md).

## Representative demo (sorting, pagination, basic columns)

```tsx
"use client"

import { useMemo, useState } from "react"
import {
  DataGrid,
  DataGridContainer,
  dataGridFeatures,
  type DataGridFeatures,
} from "@/components/reui/data-grid/data-grid"
import { DataGridPagination } from "@/components/reui/data-grid/data-grid-pagination"
import { DataGridScrollArea } from "@/components/reui/data-grid/data-grid-scroll-area"
import { DataGridTable } from "@/components/reui/data-grid/data-grid-table"
import {
  ColumnDef,
  PaginationState,
  SortingState,
  useTable,
} from "@tanstack/react-table"

const users = [
  {
    id: "1",
    name: "Alex Johnson",
    email: "alex@example.com",
    avatar: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=96&h=96&dpr=2&q=80",
    initials: "AJ",
  },
  {
    id: "2",
    name: "Sarah Chen",
    email: "sarah@example.com",
    avatar: "https://images.unsplash.com/photo-1519699047748-de8e457a634e?w=96&h=96&dpr=2&q=80",
    initials: "SC",
  },
  {
    id: "3",
    name: "Michael Rodriguez",
    email: "michael@example.com",
    avatar: "https://images.unsplash.com/photo-1584308972272-9e4e7685e80f?w=96&h=96&dpr=2&q=80",
    initials: "MR",
  },
  {
    id: "4",
    name: "Emma Wilson",
    email: "emma@example.com",
    avatar: "https://images.unsplash.com/photo-1485893086445-ed75865251e0?w=96&h=96&dpr=2&q=80",
    initials: "EW",
  },
  {
    id: "5",
    name: "David Kim",
    email: "david@example.com",
    avatar: "https://images.unsplash.com/photo-1607990281513-2c110a25bd8c?w=96&h=96&dpr=2&q=80",
    initials: "DK",
  },
  {
    id: "6",
    name: "Aron Thompson",
    email: "lisa@example.com",
    avatar: "https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=96&h=96&dpr=2&q=80",
    initials: "LT",
  },
  {
    id: "7",
    name: "James Brown",
    email: "james@example.com",
    avatar: "https://images.unsplash.com/photo-1543299750-19d1d6297053?w=96&h=96&dpr=2&q=80",
    initials: "JB",
  },
  {
    id: "8",
    name: "Maria Garcia",
    email: "maria@example.com",
    avatar: "https://images.unsplash.com/photo-1620075225255-8c2051b6c015?w=96&h=96&dpr=2&q=80",
    initials: "MG",
  },
  {
    id: "9",
    name: "Nick Johnson",
    email: "nick@example.com",
    avatar: "https://images.unsplash.com/photo-1485206412256-701ccc5b93ca?w=96&h=96&dpr=2&q=80",
    initials: "NJ",
  },
  {
    id: "10",
    name: "Liam Thompson",
    email: "liam@example.com",
    avatar: "https://images.unsplash.com/photo-1542595913-85d69b0edbaf?w=96&h=96&dpr=2&q=80",
    initials: "LT",
  },
]

interface IData {
  id: string
  name: string
  availability: "online" | "away" | "busy" | "offline"
  avatar: string
  status: "active" | "inactive"
  flag: string // Emoji flags
  email: string
  company: string
  role: string
  joined: string
  location: string
  balance: number
}

// demoData maps `users` to `IData`, cycling deterministic values by index for
// availability, status, flag, company, role, joined date, location and
// balance (the full generator body is upstream boilerplate not reproduced
// here; every field it fills is declared on the `IData` interface above).
declare const demoData: IData[]

export function Pattern() {
  const [pagination, setPagination] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 5,
  })
  const [sorting, setSorting] = useState<SortingState>([
    { id: "name", desc: true },
  ])

  const columns = useMemo<ColumnDef<DataGridFeatures, IData>[]>(
    () => [
      {
        accessorKey: "name",
        header: "Name",
        cell: (info) => <>{info.getValue() as string}</>,
        size: 150,
        meta: {
          headerClassName: "",
          cellClassName: "",
        },
      },
      {
        accessorKey: "email",
        header: "Email",
        cell: (info) => (
          <div className="truncate">
            <a
              href={`mailto:${info.getValue()}`}
              className="hover:text-primary truncate hover:underline"
            >
              {info.getValue() as string}
            </a>
          </div>
        ),
        size: 150,
        meta: {
          headerClassName: "",
          cellClassName: "",
        },
      },
      {
        accessorKey: "location",
        header: "Location",
        cell: ({ row }) => (
          <div className="flex items-center gap-1.5">
            <img
              src={`https://flagcdn.com/${row.original.flag.toLowerCase()}.svg`}
              alt={row.original.flag}
              className="size-4 rounded-full object-cover"
            />
            <div className="text-foreground">{row.original.location}</div>
          </div>
        ),
        size: 175,
        meta: {
          headerClassName: "",
          cellClassName: "",
        },
      },
      {
        accessorKey: "balance",
        header: "Balance ($)",
        cell: (info) => <>${(info.getValue() as number).toFixed(2)}</>,
        size: 100,
        meta: {
          headerClassName: "text-right rtl:text-left",
          cellClassName: "text-right rtl:text-left",
        },
      },
    ],
    []
  )

  const table = useTable({
    features: dataGridFeatures,
    columns,
    data: demoData,
    pageCount: Math.ceil((demoData?.length || 0) / pagination.pageSize),
    getRowId: (row: IData) => row.id,
    state: {
      pagination,
      sorting,
    },
    onPaginationChange: setPagination,
    onSortingChange: setSorting,
  })

  return (
    <DataGrid table={table} recordCount={demoData?.length || 0}>
      <div className="w-full space-y-2.5">
        <DataGridContainer>
          <DataGridScrollArea>
            <DataGridTable />
          </DataGridScrollArea>
        </DataGridContainer>
        <DataGridPagination />
      </div>
    </DataGrid>
  )
}
```

Note: the upstream `demoData` generator maps `users` through `.map((user, index) => ({ ...user,
availability: [...][index % 4], status: ..., flag: [...][index % 10], company: [...][index % 10],
role: [...], joined: ..., location: ..., balance: ... }))` — deterministic cycling arrays of sample
values per field. It is straightforward fixture code; the field list is fully typed on `IData` above,
and reproducing the literal cycling arrays adds no API information beyond what
[DATA-GRID.md](./DATA-GRID.md) already states about each prop that consumes them (`DataGridColumnFilter`
options, `getRowStatus`, etc., in the other 11 demos).

## Source

- https://reui.io/docs/components/base/data-grid (Base UI)
- https://reui.io/docs/components/radix/data-grid (Radix UI)
- Mirrored 2026-09-04.
