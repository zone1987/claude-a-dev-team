# Drawer — API Reference

## Composition Tree

```text
Drawer
├── DrawerTrigger
└── DrawerContent
    ├── DrawerHeader
    │   ├── DrawerTitle
    │   └── DrawerDescription
    └── DrawerFooter
```

## Sub-component Props

### Drawer

Wraps `DrawerPrimitive.Root` (Vaul).

| Prop              | Type                         | Default      | Description                                  |
| ----------------- | ---------------------------- | ------------ | -------------------------------------------- |
| `open`            | `boolean`                    | –            | Controlled open state                        |
| `onOpenChange`    | `(open: boolean) => void`    | –            | Called when open state changes               |
| `direction`       | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Side the drawer slides from     |
| `modal`           | `boolean`                    | `true`       | Whether interaction outside closes drawer    |
| `dismissible`     | `boolean`                    | `true`       | Whether user can drag/swipe to close         |
| `snapPoints`      | `(string \| number)[]`       | –            | Vaul snap points                             |

### DrawerTrigger

Wraps `DrawerPrimitive.Trigger`. Accepts `asChild`.

### DrawerContent

Renders portal + overlay + content panel. The grab handle (drag indicator) is rendered automatically for `direction="bottom"`.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### DrawerHeader

`<div>` wrapper. Text is centered for `top`/`bottom` drawers, left-aligned for `left`/`right`.

### DrawerFooter

`<div>` wrapper with `mt-auto` — pushes footer to the bottom of a flex column.

### DrawerTitle

Wraps `DrawerPrimitive.Title`. Required for accessibility.

### DrawerDescription

Wraps `DrawerPrimitive.Description`. Renders muted helper text.

### DrawerClose

Wraps `DrawerPrimitive.Close`. Use `asChild` for custom close buttons.

## Direction-specific Styling

The `DrawerContent` component uses `data-[vaul-drawer-direction=*]` selectors:

| Direction | Behavior                                             |
| --------- | ---------------------------------------------------- |
| `bottom`  | Full width, slides from bottom, shows drag handle   |
| `top`     | Full width, slides from top, centered header text   |
| `right`   | 75% width (max `sm`), slides from right              |
| `left`    | 75% width (max `sm`), slides from left               |

---

_Source: `apps/v4/content/docs/components/base/drawer.mdx`, `apps/v4/registry/new-york-v4/ui/drawer.tsx`_
