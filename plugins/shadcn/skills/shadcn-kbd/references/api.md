# Kbd — API Reference

## Composition

```text
Kbd
KbdGroup
├── Kbd
└── Kbd
```

## Kbd

Renders a `<kbd>` element styled as a keyboard key badge.

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | `""`    | Additional CSS classes |

Inherits all native `<kbd>` props.

### Tooltip context

When placed inside a `[data-slot=tooltip-content]` ancestor, the background automatically adapts to remain visible on dark tooltip backgrounds.

```tsx
import { Kbd } from "@/components/ui/kbd"

<Kbd>Ctrl</Kbd>
<Kbd>⌘</Kbd>
<Kbd>⏎</Kbd>
```

## KbdGroup

Renders a `<kbd>` wrapper that displays multiple `Kbd` elements inline with spacing.

| Prop        | Type     | Default | Description            |
| ----------- | -------- | ------- | ---------------------- |
| `className` | `string` | `""`    | Additional CSS classes |

```tsx
import { Kbd, KbdGroup } from "@/components/ui/kbd"

<KbdGroup>
  <Kbd>Ctrl</Kbd>
  <Kbd>B</Kbd>
</KbdGroup>
```

---
Source: `content/docs/components/base/kbd.mdx`
