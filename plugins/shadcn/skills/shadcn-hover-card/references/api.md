# HoverCard — API Reference

## Composition Tree

```text
HoverCard
├── HoverCardTrigger
└── HoverCardContent
```

## Basic Usage

```tsx
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"

<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```

## Sub-component Props

### HoverCard

Wraps `HoverCardPrimitive.Root`.

| Prop              | Type                      | Default | Description                              |
| ----------------- | ------------------------- | ------- | ---------------------------------------- |
| `open`            | `boolean`                 | –       | Controlled open state                    |
| `defaultOpen`     | `boolean`                 | `false` | Uncontrolled default                     |
| `onOpenChange`    | `(open: boolean) => void` | –       | Called when open state changes           |
| `openDelay`       | `number`                  | `700`   | Delay (ms) before opening on hover       |
| `closeDelay`      | `number`                  | `300`   | Delay (ms) before closing after unhover  |

### HoverCardTrigger

Wraps `HoverCardPrimitive.Trigger`. Accepts `asChild`.

| Prop      | Type      | Default | Description             |
| --------- | --------- | ------- | ----------------------- |
| `asChild` | `boolean` | `false` | Render as child element |

### HoverCardContent

Rendered inside a portal. Default width: `w-64`.

| Prop          | Type                                          | Default    | Description                    |
| ------------- | --------------------------------------------- | ---------- | ------------------------------ |
| `align`       | `"start" \| "center" \| "end"`               | `"center"` | Horizontal alignment           |
| `side`        | `"top" \| "right" \| "bottom" \| "left"`     | –          | Preferred side                 |
| `sideOffset`  | `number`                                      | `4`        | Distance from trigger (px)     |
| `className`   | `string`                                      | –          | Additional CSS classes         |

## Trigger Delays

Control open/close timing on the `HoverCard` root:

```tsx
<HoverCard openDelay={100} closeDelay={200}>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>Content</HoverCardContent>
</HoverCard>
```

## Positioning

```tsx
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent side="top" align="start">
    Content
  </HoverCardContent>
</HoverCard>
```

---

_Source: `apps/v4/content/docs/components/base/hover-card.mdx`, `apps/v4/registry/new-york-v4/ui/hover-card.tsx`_
