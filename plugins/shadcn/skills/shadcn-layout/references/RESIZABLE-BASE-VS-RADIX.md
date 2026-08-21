# Resizable — Base vs Radix

Both variants wrap `react-resizable-panels` v4 and use the same shadcn/ui API.

## Key differences

| Aspect               | new-york-v4 (Radix/default)                      | base variant                                  |
| -------------------- | ------------------------------------------------- | --------------------------------------------- |
| Import path          | `import { GripVerticalIcon } from "lucide-react"` | No Lucide icon import                         |
| `withHandle` icon    | Renders `GripVerticalIcon` inside a styled `div`  | Renders `<div className="cn-resizable-handle-icon z-10 flex shrink-0" />` (styled by theme) |
| CSS class prefixes   | No `cn-` prefix                                   | `cn-resizable-panel-group`, `cn-resizable-handle` prefixes |
| `ring-offset`        | `focus-visible:ring-offset-1`                     | `ring-offset-background` utility              |
| Peer dependency      | `react-resizable-panels`                          | `react-resizable-panels` (same)               |

## Recommendation

Use the `new-york-v4` / Radix source when adding to a standard shadcn/ui project.
Use the `base` variant when building on Base UI or in a design-system context with CSS token-based theming.

## Source files

- `registry/new-york-v4/ui/resizable.tsx`
- `registry/bases/base/ui/resizable.tsx`
- `registry/bases/radix/ui/resizable.tsx`
