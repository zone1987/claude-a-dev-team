# Dialog — API Reference

## Composition Tree

```text
Dialog
├── DialogTrigger
└── DialogContent
    ├── DialogHeader
    │   ├── DialogTitle
    │   └── DialogDescription
    └── DialogFooter
```

## Basic Usage

```tsx
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you absolutely sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

## Sub-component Props

### Dialog

Wraps `DialogPrimitive.Root`. All Radix UI Dialog Root props are forwarded.

| Prop           | Type                      | Default     | Description                        |
| -------------- | ------------------------- | ----------- | ---------------------------------- |
| `open`         | `boolean`                 | –           | Controlled open state              |
| `defaultOpen`  | `boolean`                 | `false`     | Uncontrolled default open state    |
| `onOpenChange` | `(open: boolean) => void` | –           | Called when open state changes     |
| `modal`        | `boolean`                 | `true`      | Whether dialog is modal            |

### DialogTrigger

Wraps `DialogPrimitive.Trigger`. Accepts `asChild` to render a custom element.

| Prop      | Type      | Default | Description                    |
| --------- | --------- | ------- | ------------------------------ |
| `asChild` | `boolean` | `false` | Render as child element        |

### DialogContent

Renders overlay + popup. Includes close button by default.

| Prop              | Type      | Default | Description                         |
| ----------------- | --------- | ------- | ----------------------------------- |
| `showCloseButton` | `boolean` | `true`  | Show/hide the X close button        |
| `className`       | `string`  | –       | Additional CSS classes              |
| All Radix Content props are forwarded (e.g. `onOpenAutoFocus`, `onCloseAutoFocus`, `onInteractOutside`) | | | |

### DialogHeader

Plain `<div>` wrapper with flex-col layout. Centers text on mobile, left-aligns on `sm:`.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### DialogFooter

Plain `<div>` wrapper. Stack vertically on mobile, row on `sm:`. Optional built-in Close button.

| Prop              | Type      | Default | Description                             |
| ----------------- | --------- | ------- | --------------------------------------- |
| `showCloseButton` | `boolean` | `false` | Renders a `DialogClose` "Close" button  |
| `className`       | `string`  | –       | Additional CSS classes                  |

### DialogTitle

Wraps `DialogPrimitive.Title`. Required for accessibility.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### DialogDescription

Wraps `DialogPrimitive.Description`. Renders muted helper text below the title.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### DialogClose

Wraps `DialogPrimitive.Close`. Use `asChild` to render custom close buttons.

| Prop      | Type      | Default | Description             |
| --------- | --------- | ------- | ----------------------- |
| `asChild` | `boolean` | `false` | Render as child element |

### DialogOverlay

Semi-transparent backdrop. Automatically included inside `DialogContent`.

### DialogPortal

Renders dialog outside the DOM tree. Automatically included inside `DialogContent`.

---

_Source: `apps/v4/content/docs/components/base/dialog.mdx`, `apps/v4/content/docs/components/radix/dialog.mdx`_
