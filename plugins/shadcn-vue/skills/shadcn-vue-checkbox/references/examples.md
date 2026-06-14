# Checkbox — Examples

## 1. Basic

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="Basic">
    <Field orientation="horizontal">
      <Checkbox id="terms" />
      <FieldLabel html-for="terms">
        Accept terms and conditions
      </FieldLabel>
    </Field>
  </Example>
</template>
```

## 2. Disabled

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="Disabled">
    <Field orientation="horizontal">
      <Checkbox id="toggle" disabled />
      <FieldLabel html-for="toggle">
        Enable notifications
      </FieldLabel>
    </Field>
  </Example>
</template>
```

## 3. With Description

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldLabel,
} from "@/registry/bases/reka/ui/field"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="With Description">
    <Field orientation="horizontal">
      <Checkbox id="terms-2" :default-checked="true" />
      <FieldContent>
        <FieldLabel html-for="terms-2">
          Accept terms and conditions
        </FieldLabel>
        <FieldDescription>
          By clicking this checkbox, you agree to the terms and conditions.
        </FieldDescription>
      </FieldContent>
    </Field>
  </Example>
</template>
```

## 4. Invalid

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="Invalid">
    <Field orientation="horizontal" data-invalid>
      <Checkbox id="terms-3" aria-invalid />
      <FieldLabel html-for="terms-3">
        Accept terms and conditions
      </FieldLabel>
    </Field>
  </Example>
</template>
```

## 5. Group

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="Group">
    <Field>
      <FieldLabel>Show these items on the desktop:</FieldLabel>
      <Field orientation="horizontal">
        <Checkbox id="finder-pref-9k2-hard-disks-ljj" />
        <FieldLabel html-for="finder-pref-9k2-hard-disks-ljj" class="font-normal">
          Hard disks
        </FieldLabel>
      </Field>
      <Field orientation="horizontal">
        <Checkbox id="finder-pref-9k2-external-disks-1yg" />
        <FieldLabel html-for="finder-pref-9k2-external-disks-1yg" class="font-normal">
          External disks
        </FieldLabel>
      </Field>
      <Field orientation="horizontal">
        <Checkbox id="finder-pref-9k2-cds-dvds-fzt" />
        <FieldLabel html-for="finder-pref-9k2-cds-dvds-fzt" class="font-normal">
          CDs, DVDs, and iPods
        </FieldLabel>
      </Field>
      <Field orientation="horizontal">
        <Checkbox id="finder-pref-9k2-connected-servers-6l2" />
        <FieldLabel html-for="finder-pref-9k2-connected-servers-6l2" class="font-normal">
          Connected servers
        </FieldLabel>
      </Field>
    </Field>
  </Example>
</template>
```

## 6. With Title (FieldGroup + FieldTitle)

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldTitle,
} from "@/registry/bases/reka/ui/field"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="With Title">
    <FieldGroup>
      <FieldLabel html-for="toggle-2">
        <Field orientation="horizontal">
          <Checkbox id="toggle-2" :default-checked="true" />
          <FieldContent>
            <FieldTitle>Enable notifications</FieldTitle>
            <FieldDescription>
              You can enable or disable notifications at any time.
            </FieldDescription>
          </FieldContent>
        </Field>
      </FieldLabel>
      <FieldLabel html-for="toggle-4">
        <Field orientation="horizontal" data-disabled>
          <Checkbox id="toggle-4" disabled />
          <FieldContent>
            <FieldTitle>Enable notifications</FieldTitle>
            <FieldDescription>
              You can enable or disable notifications at any time.
            </FieldDescription>
          </FieldContent>
        </Field>
      </FieldLabel>
    </FieldGroup>
  </Example>
</template>
```

## 7. In Table (reactive row selection)

```vue
<script setup lang="ts">
import { computed, ref } from "vue"
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/registry/bases/reka/ui/table"
import { Example } from "~/registry/bases/reka/components/example"

const tableData = [
  { id: "1", name: "Sarah Chen", email: "sarah.chen@example.com", role: "Admin" },
  { id: "2", name: "Marcus Rodriguez", email: "marcus.rodriguez@example.com", role: "User" },
  { id: "3", name: "Priya Patel", email: "priya.patel@example.com", role: "User" },
  { id: "4", name: "David Kim", email: "david.kim@example.com", role: "Editor" },
]

const selectedRows = ref<Set<string>>(new Set(["1"]))

const selectAll = computed(() => selectedRows.value.size === tableData.length)

function handleSelectAll(checked: boolean) {
  if (checked) {
    selectedRows.value = new Set(tableData.map(row => row.id))
  }
  else {
    selectedRows.value = new Set()
  }
}

function handleSelectRow(id: string, checked: boolean) {
  const newSelected = new Set(selectedRows.value)
  if (checked) {
    newSelected.add(id)
  }
  else {
    newSelected.delete(id)
  }
  selectedRows.value = newSelected
}
</script>

<template>
  <Example title="In Table">
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead class="w-8">
            <Checkbox
              id="select-all"
              :checked="selectAll"
              @update:checked="handleSelectAll"
            />
          </TableHead>
          <TableHead>Name</TableHead>
          <TableHead>Email</TableHead>
          <TableHead>Role</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <TableRow
          v-for="row in tableData"
          :key="row.id"
          :data-state="selectedRows.has(row.id) ? 'selected' : undefined"
        >
          <TableCell>
            <Checkbox
              :id="`row-${row.id}`"
              :checked="selectedRows.has(row.id)"
              @update:checked="(checked: boolean | 'indeterminate') => handleSelectRow(row.id, checked === true)"
            />
          </TableCell>
          <TableCell class="font-medium">
            {{ row.name }}
          </TableCell>
          <TableCell>{{ row.email }}</TableCell>
          <TableCell>{{ row.role }}</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  </Example>
</template>
```
