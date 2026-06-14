# Alert Dialog — Base UI vs Radix UI

## Dependency

| | Radix UI | Base UI |
|---|---|---|
| Package | `radix-ui` | `@base-ui/react` |
| Import | `AlertDialog from "radix-ui"` | `from "@base-ui/react/alert-dialog"` |

## Component mapping

| Radix UI | Base UI |
|----------|---------|
| `AlertDialogPrimitive.Overlay` | `AlertDialogPrimitive.Backdrop` |
| `AlertDialogPrimitive.Content` | `AlertDialogPrimitive.Popup` |
| `AlertDialogPrimitive.Cancel` | `AlertDialogPrimitive.Close` |

## Trigger

- Radix: `asChild` prop
- Base UI: `render` prop

## AlertDialogAction

- Radix: wraps `Button` with `asChild` around `AlertDialogPrimitive.Action`
- Base UI: `Button` component directly with data-slot

## AlertDialogCancel

- Radix: `Button asChild` around `AlertDialogPrimitive.Cancel`
- Base UI: `AlertDialogPrimitive.Close` with `render={<Button />}`

## Animation

- Radix: `data-[state=open]:animate-in data-[state=closed]:animate-out`
- Base UI: CSS custom classes `cn-alert-dialog-*`

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/alert-dialog.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/alert-dialog.tsx`
