# Dialog — Base UI vs. Radix UI

| Aspect                  | new-york-v4 (Radix UI)                          | Base UI                                          |
| ----------------------- | ----------------------------------------------- | ------------------------------------------------ |
| Dependency              | `radix-ui`                                      | `@base-ui/react`                                 |
| Import                  | `from "radix-ui"` (Dialog)                      | `from "@base-ui/react/dialog"`                   |
| Overlay component       | `DialogPrimitive.Overlay`                       | `DialogPrimitive.Backdrop`                       |
| Content component       | `DialogPrimitive.Content`                       | `DialogPrimitive.Popup`                          |
| Close button render     | JSX child with `asChild`                        | `render` prop on `DialogPrimitive.Close`         |
| Close icon              | `XIcon` (lucide-react)                          | `IconPlaceholder` (theme-agnostic multi-lib)     |
| Styling approach        | Tailwind utility classes with animations        | `cn-dialog-*` CSS token classes                  |
| Overlay animation       | `data-[state=open/closed]:animate-in/out`       | Controlled via CSS tokens                        |
| Content animation       | `data-[state=open]:zoom-in-95` etc.             | Controlled via CSS tokens                        |
| Header text alignment   | Centers on mobile, left on `sm:`                | Left by default (CSS token based)               |
| Title styling           | `text-lg leading-none font-semibold`            | `cn-font-heading` CSS token                      |

## API Compatibility

Both implementations expose the same component names:
`Dialog`, `DialogTrigger`, `DialogPortal`, `DialogOverlay`, `DialogClose`, `DialogContent`, `DialogHeader`, `DialogFooter`, `DialogTitle`, `DialogDescription`

The `showCloseButton` prop on `DialogContent` and `DialogFooter` works identically in both.

## Radix UI nova variant

The `registry/bases/radix/ui/dialog.tsx` is a middle-ground: uses `radix-ui` primitives but applies `cn-dialog-*` CSS token classes (same as Base UI styling), with `IconPlaceholder` for the close icon. Used when you want Radix UI stability with theme-token styling.

---

_Source: `apps/v4/registry/bases/base/ui/dialog.tsx`, `apps/v4/registry/bases/radix/ui/dialog.tsx`, `apps/v4/registry/new-york-v4/ui/dialog.tsx`_
