# Select — Base vs Radix

## Dependency

| Variant  | Package          |
| -------- | ---------------- |
| Radix    | `radix-ui`       |
| Base UI  | `@base-ui/react` |

## Key structural differences

| Aspect                  | new-york-v4 (Radix)                            | base variant (Base UI)                              |
| ----------------------- | ---------------------------------------------- | --------------------------------------------------- |
| Root                    | `SelectPrimitive.Root`                         | `SelectPrimitive.Root` (re-exported directly as `Select`) |
| Trigger icon            | `ChevronDownIcon` from lucide-react            | `IconPlaceholder` (theme-switchable icon)           |
| Dropdown positioning    | `position="item-aligned"` or `"popper"` prop  | `alignItemWithTrigger` boolean prop (default `true`) |
| Content wrapper         | `SelectPrimitive.Portal > Content > Viewport` | `Portal > Positioner > Popup > List`                |
| Scroll arrows           | `ScrollUpButton` / `ScrollDownButton`          | `ScrollUpArrow` / `ScrollDownArrow`                 |
| Item indicator position | `absolute right-2` inside item                | Separate `ItemIndicator` component with `render` prop |
| ItemText                | `SelectPrimitive.ItemText`                     | `SelectPrimitive.ItemText` with `className`         |
| Disabled state attr     | `data-[disabled]`                              | `data-disabled`                                     |

## Positioning comparison

**Radix** — `SelectContent position` prop:
- `"item-aligned"` (default): dropdown overlaps trigger, selected item shows on top
- `"popper"`: standard dropdown that appears below/above trigger edge

**Base UI** — `SelectContent alignItemWithTrigger` prop:
- `true` (default): same as `item-aligned`
- `false`: same as `popper`

## Source files

- `registry/new-york-v4/ui/select.tsx`
- `registry/bases/base/ui/select.tsx`
