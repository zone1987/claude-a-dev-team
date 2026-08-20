# Popover — API Reference

## Popover (Root)

Built on reka-ui `PopoverRoot`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | `boolean` | — | Controlled open state |
| `defaultOpen` | `boolean` | `false` | Uncontrolled initial state |
| `modal` | `boolean` | `false` | Modal mode (focus trap) |

### Emits

| Event | Type | Description |
|---|---|---|
| `update:open` | `boolean` | Fires on open/close |

### Slot Props

```ts
// v-slot="{ open }"
```

---

## PopoverTrigger

Built on reka-ui `PopoverTrigger`. No styling of its own.

### Props

| Prop | Type | Description |
|---|---|---|
| `asChild` | `boolean` | Renders the child as the trigger |
| All `PopoverTriggerProps` | — | Forwarded |

---

## PopoverContent

Built on reka-ui `PopoverContent`, rendered inside `PopoverPortal`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `align` | `"start" \| "center" \| "end"` | `"center"` | Horizontal alignment |
| `sideOffset` | `number` | `4` | Distance from the trigger (px) |
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Preferred side |
| `alignOffset` | `number` | — | Offset along the alignment axis |
| `avoidCollisions` | `boolean` | `true` | Flips on viewport collision |
| `collisionBoundary` | `Element \| null \| Array` | — | Collision boundaries |
| `collisionPadding` | `number \| Partial<Record<Side, number>>` | `0` | Padding for the collision check |
| `sticky` | `"partial" \| "always"` | `"partial"` | Stickiness |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### Animations
Are controlled via `data-[state]` and `data-[side]`:
- `data-[state=open]`: fade-in + zoom-in-95
- `data-[state=closed]`: fade-out + zoom-out-95
- `data-[side=*]`: slide-in-from-*

---

## PopoverAnchor

Decouples the anchor from the trigger. Allows positioning the popover relative to another element.

### Props

| Prop | Type | Description |
|---|---|---|
| All `PopoverAnchorProps` | — | Forwarded |

---

## reka-ui Reference
- https://reka-ui.com/docs/components/popover
