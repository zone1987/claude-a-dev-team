# Scroll Area — Base vs Radix

## Dependency

| Variant  | Package                   |
| -------- | ------------------------- |
| Radix    | `radix-ui`                |
| Base UI  | `@base-ui/react`          |

## Key differences

| Aspect                       | new-york-v4 (Radix)                                          | base variant (Base UI)                                          |
| ---------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| Root import                  | `import { ScrollArea as ScrollAreaPrimitive } from "radix-ui"` | `import { ScrollArea as ScrollAreaPrimitive } from "@base-ui/react/scroll-area"` |
| Scrollbar component          | `ScrollAreaPrimitive.ScrollAreaScrollbar`                    | `ScrollAreaPrimitive.Scrollbar`                                 |
| Thumb component              | `ScrollAreaPrimitive.ScrollAreaThumb`                        | `ScrollAreaPrimitive.Thumb`                                     |
| Orientation tracking         | Controlled via CSS conditional classes                       | Adds `data-orientation={orientation}` attribute                 |
| ScrollBar thumb shape        | `rounded-full`                                               | No `rounded-full` (styled via theme token)                      |
| CSS class prefixes           | No `cn-` prefix                                              | `cn-scroll-area`, `cn-scroll-area-viewport`, etc.               |

## API compatibility

The exported `ScrollArea` and `ScrollBar` components have the same props in both variants.
The main difference is the underlying primitive library.

## Source files

- `registry/new-york-v4/ui/scroll-area.tsx`
- `registry/bases/base/ui/scroll-area.tsx`
- `registry/bases/radix/ui/scroll-area.tsx`
