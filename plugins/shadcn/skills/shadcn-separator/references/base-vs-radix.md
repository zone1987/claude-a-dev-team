# Separator — Base vs Radix

## Dependency

| Variant  | Package          |
| -------- | ---------------- |
| Radix    | `radix-ui`       |
| Base UI  | `@base-ui/react` |

## Key differences

| Aspect                  | new-york-v4 (Radix)                            | base variant (Base UI)                        |
| ----------------------- | ---------------------------------------------- | --------------------------------------------- |
| Import                  | `import { Separator as SeparatorPrimitive } from "radix-ui"` | `import { Separator as SeparatorPrimitive } from "@base-ui/react/separator"` |
| Component type          | `SeparatorPrimitive.Root` (has `.Root`)        | `SeparatorPrimitive` (directly callable)      |
| `decorative` prop       | Supported (hides from a11y tree when true)     | Not available                                 |
| Orientation CSS selectors | `data-[orientation=horizontal]:`             | `data-horizontal:` / `data-vertical:`         |
| Vertical sizing         | `data-[orientation=vertical]:h-full`           | `data-vertical:self-stretch` (flex-based)     |

## Source files

- `registry/new-york-v4/ui/separator.tsx`
- `registry/bases/base/ui/separator.tsx`
