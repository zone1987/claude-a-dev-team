# Kbd — API reference

## Kbd

Renders as a native `<kbd>` HTML element. No reka-ui primitive.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

### Slots

| Slot | Description |
|---|---|
| default | Text or SVG icon of the key |

### Styling
- Background: `bg-muted`
- Text: `text-muted-foreground`
- Size: `h-5 min-w-5 text-xs`
- Inside `[data-slot=tooltip-content]`: transparent background (automatic)

---

## KbdGroup

Also renders as `<kbd>`, grouping multiple `Kbd` elements with `gap-1`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

### Slots

| Slot | Description |
|---|---|
| default | Multiple `<Kbd>` components |

---

## Note
`Kbd` and `KbdGroup` have no reka-ui base — they are pure Tailwind CSS wrappers.
