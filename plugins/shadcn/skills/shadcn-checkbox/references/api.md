# Checkbox — API Reference

## Usage

```tsx
import { Checkbox } from "@/components/ui/checkbox"
```

```tsx
<Checkbox />
```

## Props

The `Checkbox` component forwards all props to `Radix UI Checkbox.Root`.

| Prop              | Type                                        | Default | Description                                     |
| ----------------- | ------------------------------------------- | ------- | ----------------------------------------------- |
| `checked`         | `boolean \| "indeterminate"`                | -       | Controlled checked state                        |
| `defaultChecked`  | `boolean \| "indeterminate"`                | -       | Uncontrolled initial checked state              |
| `onCheckedChange` | `(checked: boolean \| "indeterminate") => void` | -   | Callback when checked state changes             |
| `disabled`        | `boolean`                                   | `false` | Prevents interaction                            |
| `required`        | `boolean`                                   | `false` | Marks as required in form contexts              |
| `name`            | `string`                                    | -       | Name for form submission                        |
| `value`           | `string`                                    | `"on"`  | Value for form submission                       |
| `aria-invalid`    | `boolean`                                   | -       | Shows destructive/invalid styling               |
| `className`       | `string`                                    | -       |                                                 |

## Checked State

```tsx
// Uncontrolled
<Checkbox defaultChecked />

// Controlled
import * as React from "react"

export function Example() {
  const [checked, setChecked] = React.useState(false)
  return <Checkbox checked={checked} onCheckedChange={setChecked} />
}
```

## Invalid State

Set `aria-invalid` on the checkbox to show destructive/invalid styling:

```tsx
<Checkbox aria-invalid />
```

## Disabled State

```tsx
<Checkbox disabled />
```

## Indeterminate State

```tsx
<Checkbox checked="indeterminate" />
```

## With Label

```tsx
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"

<div className="flex items-center gap-3">
  <Checkbox id="terms" />
  <Label htmlFor="terms">Accept terms and conditions</Label>
</div>
```

## Radix UI API Reference

See https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference for the complete Radix UI API.

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/checkbox.mdx`_
