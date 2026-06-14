# NativeSelect — Examples

## Demo

Basic native select with status options.

```tsx
import {
  NativeSelect,
  NativeSelectOption,
} from "@/components/ui/native-select"

export default function NativeSelectDemo() {
  return (
    <NativeSelect>
      <NativeSelectOption value="">Select status</NativeSelectOption>
      <NativeSelectOption value="todo">Todo</NativeSelectOption>
      <NativeSelectOption value="in-progress">In Progress</NativeSelectOption>
      <NativeSelectOption value="done">Done</NativeSelectOption>
      <NativeSelectOption value="cancelled">Cancelled</NativeSelectOption>
    </NativeSelect>
  )
}
```

## Groups

`NativeSelectOptGroup` organizes options into labeled categories.

```tsx
import {
  NativeSelect,
  NativeSelectOptGroup,
  NativeSelectOption,
} from "@/components/ui/native-select"

export default function NativeSelectGroups() {
  return (
    <NativeSelect>
      <NativeSelectOption value="">Select department</NativeSelectOption>
      <NativeSelectOptGroup label="Engineering">
        <NativeSelectOption value="frontend">Frontend</NativeSelectOption>
        <NativeSelectOption value="backend">Backend</NativeSelectOption>
        <NativeSelectOption value="devops">DevOps</NativeSelectOption>
      </NativeSelectOptGroup>
      <NativeSelectOptGroup label="Sales">
        <NativeSelectOption value="sales-rep">Sales Rep</NativeSelectOption>
        <NativeSelectOption value="account-manager">Account Manager</NativeSelectOption>
        <NativeSelectOption value="sales-director">Sales Director</NativeSelectOption>
      </NativeSelectOptGroup>
      <NativeSelectOptGroup label="Operations">
        <NativeSelectOption value="support">Customer Support</NativeSelectOption>
        <NativeSelectOption value="product-manager">Product Manager</NativeSelectOption>
        <NativeSelectOption value="ops-manager">Operations Manager</NativeSelectOption>
      </NativeSelectOptGroup>
    </NativeSelect>
  )
}
```

## Disabled

The `disabled` prop grays out the entire select via `has-[select:disabled]:opacity-50` on the wrapper.

```tsx
import {
  NativeSelect,
  NativeSelectOption,
} from "@/components/ui/native-select"

export default function NativeSelectDisabled() {
  return (
    <NativeSelect disabled>
      <NativeSelectOption value="">Select priority</NativeSelectOption>
      <NativeSelectOption value="low">Low</NativeSelectOption>
      <NativeSelectOption value="medium">Medium</NativeSelectOption>
      <NativeSelectOption value="high">High</NativeSelectOption>
      <NativeSelectOption value="critical">Critical</NativeSelectOption>
    </NativeSelect>
  )
}
```

## Invalid

Use `aria-invalid="true"` to display the destructive border and ring for validation errors.

```tsx
import {
  NativeSelect,
  NativeSelectOption,
} from "@/components/ui/native-select"

export default function NativeSelectInvalid() {
  return (
    <NativeSelect aria-invalid="true">
      <NativeSelectOption value="">Select role</NativeSelectOption>
      <NativeSelectOption value="admin">Admin</NativeSelectOption>
      <NativeSelectOption value="editor">Editor</NativeSelectOption>
      <NativeSelectOption value="viewer">Viewer</NativeSelectOption>
      <NativeSelectOption value="guest">Guest</NativeSelectOption>
    </NativeSelect>
  )
}
```

---
Source: `registry/new-york-v4/examples/native-select-*.tsx`
