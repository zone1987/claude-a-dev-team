# Sonner — API Reference

Full API: https://sonner.emilkowal.ski/getting-started

## Toaster component props

The `Toaster` component accepts all `ToasterProps` from the `sonner` package:

| Prop                | Type                                                                  | Default         | Description                                       |
| ------------------- | --------------------------------------------------------------------- | --------------- | ------------------------------------------------- |
| `theme`             | `"light" \| "dark" \| "system"`                                      | auto (useTheme) | Color theme (auto-detected from `next-themes`)    |
| `position`          | `"top-left" \| "top-center" \| "top-right" \| "bottom-left" \| "bottom-center" \| "bottom-right"` | `"bottom-right"` | Position of toasts |
| `expand`            | `boolean`                                                             | `false`         | Whether toasts expand vertically                  |
| `richColors`        | `boolean`                                                             | `false`         | Use rich semantic colors for type variants        |
| `duration`          | `number`                                                              | `4000`          | Default toast duration in ms                      |
| `visibleToasts`     | `number`                                                              | `3`             | Max visible toasts at once                        |
| `closeButton`       | `boolean`                                                             | `false`         | Show close button on toasts                       |
| `toastOptions`      | `ToastClassnames`                                                     | —               | Default options for all toasts                    |
| `icons`             | `IconsConfig`                                                         | Lucide set      | Override toast icons                              |
| `offset`            | `string \| number`                                                    | `32px`          | Offset from screen edge                           |
| `dir`               | `"ltr" \| "rtl" \| "auto"`                                          | `"auto"`        | Text direction                                    |

## CSS Variables (injected by shadcn/ui Toaster)

| Variable           | Value                        |
| ------------------ | ---------------------------- |
| `--normal-bg`      | `var(--popover)`             |
| `--normal-text`    | `var(--popover-foreground)`  |
| `--normal-border`  | `var(--border)`              |
| `--border-radius`  | `var(--radius)`              |

## toast() API

```tsx
import { toast } from "sonner"

toast("Message")                          // default
toast.success("Success message")          // success (green)
toast.error("Error message")              // error (red)
toast.warning("Warning message")          // warning (yellow)
toast.info("Info message")                // info (blue)
toast.loading("Loading...")               // loading spinner
toast.promise(promise, { loading, success, error })  // promise-based
toast.dismiss(id)                         // dismiss by id
toast.dismiss()                           // dismiss all
```

## toast() options

```tsx
toast("Message", {
  description: "Optional description",
  action: {
    label: "Undo",
    onClick: () => {},
  },
  cancel: {
    label: "Cancel",
    onClick: () => {},
  },
  duration: 5000,
  id: "unique-id",
  onDismiss: (t) => {},
  onAutoClose: (t) => {},
})
```

## Source files

- `registry/new-york-v4/ui/sonner.tsx`
