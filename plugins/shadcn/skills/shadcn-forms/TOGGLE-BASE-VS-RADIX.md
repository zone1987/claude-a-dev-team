# Toggle — new-york-v4 vs Radix Base

Both variants use the same Radix UI Toggle primitive from `radix-ui` and export `Toggle` and `toggleVariants`.

## new-york-v4

Full Tailwind utility classes baked into `toggleVariants`:

- Colors and backgrounds: `bg-transparent`, `hover:bg-muted`, `hover:text-muted-foreground`
- Active/pressed state: `data-[state=on]:bg-accent data-[state=on]:text-accent-foreground`
- Focus ring: `focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50`
- Outline variant: `border border-input bg-transparent shadow-xs hover:bg-accent hover:text-accent-foreground`
- Aria-invalid styling: `aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40`
- Typography: `text-sm font-medium`
- Transitions: `transition-[color,box-shadow]`

Variant classes are concrete Tailwind classes. Sizing:

| Size | Classes |
|------|---------|
| `default` | `h-9 min-w-9 px-2` |
| `sm` | `h-8 min-w-8 px-1.5` |
| `lg` | `h-10 min-w-10 px-2.5` |

## Radix Base

Marker/semantic CSS class names instead of Tailwind utilities:

- Base class: `cn-toggle group/toggle`
- Variant classes: `cn-toggle-variant-default`, `cn-toggle-variant-outline`
- Size classes: `cn-toggle-size-default`, `cn-toggle-size-sm`, `cn-toggle-size-lg`

Only structural and state-agnostic Tailwind classes are included (`inline-flex`, `items-center`, `justify-center`, `whitespace-nowrap`, `outline-none`, `hover:bg-muted`, `focus-visible:ring-[3px]`, `disabled:pointer-events-none`, `disabled:opacity-50`).

Colors, borders, shadows, active state (`data-[state=on]`), and sizing are defined via design system CSS variables resolved through the `cn-*` marker classes. This makes the base variant suitable for theming and design system integration without coupling to specific Tailwind color tokens.

## toggleVariants re-use

`toggleVariants` is exported from both versions and is consumed internally by `ToggleGroup` to ensure consistent variant and size handling across both components.

```tsx
// ToggleGroup uses toggleVariants from the same toggle module
import { toggleVariants } from "@/components/ui/toggle"
```
