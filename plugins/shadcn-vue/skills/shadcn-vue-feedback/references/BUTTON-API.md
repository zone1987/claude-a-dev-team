# Button — API Reference

## Props

### Variant

| Value | Visual |
|---|---|
| `default` | Solid primary background |
| `destructive` | Red/destructive background, white text |
| `outline` | Border, transparent background, accent hover |
| `secondary` | Muted secondary background |
| `ghost` | No background, accent hover |
| `link` | Text-only, underline on hover |

Default: `"default"`

### Size

| Value | Dimensions | Notes |
|---|---|---|
| `default` | h-9, px-4 py-2 | Standard |
| `sm` | h-8, px-3 | Compact, smaller gap |
| `lg` | h-10, px-6 | Large |
| `icon` | size-9 (36×36px) | Square, icon-only |
| `icon-sm` | size-8 (32×32px) | Small square |
| `icon-lg` | size-10 (40×40px) | Large square |

Default: `"default"`

### Full Props Table

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"default"` | Visual style variant |
| `size` | `"default" \| "sm" \| "lg" \| "icon" \| "icon-sm" \| "icon-lg"` | `"default"` | Size preset |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes merged via `cn()` |
| `as` | `string \| Component` | `"button"` | HTML element or component to render as |
| `asChild` | `boolean` | `false` | Merge props/events onto the direct child element |

`as` and `asChild` are inherited from reka-ui's `PrimitiveProps`.

## Data Attributes

The component renders the following data attributes for CSS targeting:

| Attribute | Value |
|---|---|
| `data-slot` | `"button"` (always) |
| `data-variant` | Current variant value (e.g. `"default"`, `"destructive"`) |
| `data-size` | Current size value (e.g. `"default"`, `"icon"`) |

## `buttonVariants` standalone export

The CVA helper is exported separately for use outside the component, e.g. to style a `<RouterLink>` that should look like a button without `asChild`:

```ts
import { buttonVariants } from "@/components/ui/button"

// In a template:
// :class="buttonVariants({ variant: 'outline', size: 'sm' })"
```

```vue
<RouterLink :class="buttonVariants({ variant: 'outline' })" to="/settings">
  Settings
</RouterLink>
```
