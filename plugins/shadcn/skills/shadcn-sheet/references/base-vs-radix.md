# Sheet — Base vs Radix

Both variants build on their respective Dialog primitives.

## Dependency

| Variant  | Primitive                          |
| -------- | ---------------------------------- |
| Radix    | `Dialog` from `radix-ui`           |
| Base UI  | `Dialog` from `@base-ui/react/dialog` |

## Key differences

| Aspect                  | new-york-v4 (Radix)                               | base variant (Base UI)                                |
| ----------------------- | ------------------------------------------------- | ----------------------------------------------------- |
| Overlay component       | `SheetPrimitive.Overlay`                          | `SheetPrimitive.Backdrop`                             |
| Content component       | `SheetPrimitive.Content`                          | `SheetPrimitive.Popup` with `data-side={side}`        |
| Overlay animation       | `data-[state=open/closed]` attributes             | `data-starting-style` / `data-ending-style` CSS attrs |
| Content animation       | Slide animation via `data-[state]` + Tailwind     | Translate animation via `data-starting/ending-style` |
| Side prop               | Applied via Tailwind ternary in `className`       | Passed as `data-side={side}` attribute to Popup       |
| Close button            | Renders `XIcon` lucide icon directly              | Uses `IconPlaceholder` (theme-switchable)             |
| Close button styling    | `absolute top-4 right-4 rounded-xs opacity-70`   | Uses `Button` component with `variant="ghost" size="icon-sm"` |
| Header padding          | `gap-1.5 p-4`                                     | `cn-sheet-header flex flex-col` (CSS token driven)    |

## Source files

- `registry/new-york-v4/ui/sheet.tsx`
- `registry/bases/base/ui/sheet.tsx`
