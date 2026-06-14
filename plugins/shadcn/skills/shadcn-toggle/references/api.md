# Toggle — API Reference

Toggle extends Radix `TogglePrimitive.Root` props plus `toggleVariants` options:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `"default" \| "outline"` | `"default"` | Visual style |
| `size` | `"default" \| "sm" \| "lg"` | `"default"` | Size of the toggle |
| `pressed` | `boolean` | — | Controlled pressed state |
| `defaultPressed` | `boolean` | — | Uncontrolled default pressed |
| `onPressedChange` | `(pressed: boolean) => void` | — | Callback on press change |
| `disabled` | `boolean` | `false` | Disables the toggle |
| `aria-label` | `string` | — | Required for icon-only toggles |
| `className` | `string` | — | Additional CSS classes |
| `asChild` | `boolean` | `false` | Merge with child element |

## toggleVariants export

`toggleVariants` is also exported for use in custom components:

```tsx
import { toggleVariants } from "@/components/ui/toggle"
// Used by ToggleGroup internally
```
