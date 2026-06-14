# Collapsible — API Reference

## Composition

```text
Collapsible
├── CollapsibleTrigger
└── CollapsibleContent
```

## Usage

```tsx
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
```

```tsx
<Collapsible>
  <CollapsibleTrigger>Can I use this in my project?</CollapsibleTrigger>
  <CollapsibleContent>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </CollapsibleContent>
</Collapsible>
```

## Sub-Component Props

### Collapsible (Root)

Wraps `Radix UI Collapsible.Root`.

| Prop           | Type                      | Default | Description                                 |
| -------------- | ------------------------- | ------- | ------------------------------------------- |
| `open`         | `boolean`                 | -       | Controlled open state                       |
| `defaultOpen`  | `boolean`                 | `false` | Uncontrolled initial open state             |
| `onOpenChange` | `(open: boolean) => void` | -       | Callback when open state changes            |
| `disabled`     | `boolean`                 | `false` | Prevents interaction                        |
| `className`    | `string`                  | -       |                                             |

### CollapsibleTrigger

The button/element that toggles the collapsible. Wraps `Radix UI Collapsible.CollapsibleTrigger`.

| Prop        | Type     | Default | Description                           |
| ----------- | -------- | ------- | ------------------------------------- |
| `asChild`   | `boolean`| `false` | Merge props onto immediate child      |
| `className` | `string` | -       |                                       |

### CollapsibleContent

The panel that shows/hides. Wraps `Radix UI Collapsible.CollapsibleContent`.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

## Controlled State

```tsx
import * as React from "react"

export function Example() {
  const [open, setOpen] = React.useState(false)

  return (
    <Collapsible open={open} onOpenChange={setOpen}>
      <CollapsibleTrigger>Toggle</CollapsibleTrigger>
      <CollapsibleContent>Content</CollapsibleContent>
    </Collapsible>
  )
}
```

## Radix UI API Reference

See https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference for the complete Radix UI API.

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/collapsible.mdx`_
