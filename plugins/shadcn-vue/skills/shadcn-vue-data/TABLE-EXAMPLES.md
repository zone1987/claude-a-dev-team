# Examples

## Contents

- [Basic](#basic)
- [With Footer](#with-footer)
- [Simple](#simple)
- [With Badges](#with-badges)
- [With Actions](#with-actions)

## Basic

Invoice table with caption.

```vue
<!-- TableBasic.vue -->
<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

const invoices = [
  { invoice: "INV001", paymentStatus: "Paid", totalAmount: "$250.00", paymentMethod: "Credit Card" },
  { invoice: "INV002", paymentStatus: "Pending", totalAmount: "$150.00", paymentMethod: "PayPal" },
  { invoice: "INV003", paymentStatus: "Unpaid", totalAmount: "$350.00", paymentMethod: "Bank Transfer" },
]
</script>

<template>
  <Table>
    <TableCaption>A list of your recent invoices.</TableCaption>
    <TableHeader>
      <TableRow>
        <TableHead class="w-[100px]">Invoice</TableHead>
        <TableHead>Status</TableHead>
        <TableHead>Method</TableHead>
        <TableHead class="text-right">Amount</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="invoice in invoices" :key="invoice.invoice">
        <TableCell class="font-medium">{{ invoice.invoice }}</TableCell>
        <TableCell>{{ invoice.paymentStatus }}</TableCell>
        <TableCell>{{ invoice.paymentMethod }}</TableCell>
        <TableCell class="text-right">{{ invoice.totalAmount }}</TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
```

## With Footer

Table with totals row in footer.

```vue
<!-- TableWithFooter.vue -->
<script setup lang="ts">
import {
  Table, TableBody, TableCaption, TableCell,
  TableFooter, TableHead, TableHeader, TableRow,
} from "@/components/ui/table"

const invoices = [
  { invoice: "INV001", paymentStatus: "Paid", totalAmount: "$250.00", paymentMethod: "Credit Card" },
  { invoice: "INV002", paymentStatus: "Pending", totalAmount: "$150.00", paymentMethod: "PayPal" },
  { invoice: "INV003", paymentStatus: "Unpaid", totalAmount: "$350.00", paymentMethod: "Bank Transfer" },
]
</script>

<template>
  <Table>
    <TableCaption>A list of your recent invoices.</TableCaption>
    <TableHeader>
      <TableRow>
        <TableHead class="w-[100px]">Invoice</TableHead>
        <TableHead>Status</TableHead>
        <TableHead>Method</TableHead>
        <TableHead class="text-right">Amount</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="invoice in invoices" :key="invoice.invoice">
        <TableCell class="font-medium">{{ invoice.invoice }}</TableCell>
        <TableCell>{{ invoice.paymentStatus }}</TableCell>
        <TableCell>{{ invoice.paymentMethod }}</TableCell>
        <TableCell class="text-right">{{ invoice.totalAmount }}</TableCell>
      </TableRow>
    </TableBody>
    <TableFooter>
      <TableRow>
        <TableCell colspan="3">Total</TableCell>
        <TableCell class="text-right">$2,500.00</TableCell>
      </TableRow>
    </TableFooter>
  </Table>
</template>
```

## Simple

Minimal users table without caption.

```vue
<!-- TableSimple.vue -->
<script setup lang="ts">
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table"
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Name</TableHead>
        <TableHead>Email</TableHead>
        <TableHead class="text-right">Role</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow>
        <TableCell class="font-medium">Sarah Chen</TableCell>
        <TableCell>sarah.chen@acme.com</TableCell>
        <TableCell class="text-right">Admin</TableCell>
      </TableRow>
      <TableRow>
        <TableCell class="font-medium">Marc Rodriguez</TableCell>
        <TableCell>marcus.rodriguez@acme.com</TableCell>
        <TableCell class="text-right">User</TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
```

## With Badges

Table using inline badge-style spans for status and priority.

```vue
<!-- TableWithBadges.vue -->
<script setup lang="ts">
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table"
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Task</TableHead>
        <TableHead>Status</TableHead>
        <TableHead class="text-right">Priority</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow>
        <TableCell class="font-medium">Design homepage</TableCell>
        <TableCell>
          <span class="inline-flex items-center rounded-full bg-green-500/10 px-2 py-1 text-xs font-medium text-green-700 dark:text-green-400">
            Completed
          </span>
        </TableCell>
        <TableCell class="text-right">
          <span class="inline-flex items-center rounded-full bg-blue-500/10 px-2 py-1 text-xs font-medium text-blue-700 dark:text-blue-400">
            High
          </span>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
```

## With Actions

Table with per-row dropdown menus.

```vue
<!-- TableWithActions.vue -->
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem,
  DropdownMenuSeparator, DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table"
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Product</TableHead>
        <TableHead>Price</TableHead>
        <TableHead class="text-right">Actions</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow>
        <TableCell class="font-medium">Wireless Mouse</TableCell>
        <TableCell>$29.99</TableCell>
        <TableCell class="text-right">
          <DropdownMenu>
            <DropdownMenuTrigger :as-child="true">
              <Button variant="ghost" size="icon" class="size-8">...</Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuItem>Edit</DropdownMenuItem>
              <DropdownMenuItem>Duplicate</DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem variant="destructive">Delete</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
```

Sources:
- `registry/bases/reka/examples/table/TableBasic.vue`
- `registry/bases/reka/examples/table/TableWithFooter.vue`
- `registry/bases/reka/examples/table/TableSimple.vue`
- `registry/bases/reka/examples/table/TableWithBadges.vue`
- `registry/bases/reka/examples/table/TableWithActions.vue`
- `registry/bases/reka/examples/table/TableWithSelect.vue`
- `registry/bases/reka/examples/table/TableWithInput.vue`
- `registry/bases/reka/examples/table/data.ts`
