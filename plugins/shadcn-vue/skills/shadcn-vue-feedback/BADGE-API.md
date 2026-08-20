# Badge — API Reference

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "secondary" \| "destructive" \| "outline"` | `"default"` | Visual style variant |
| `class` | `HTMLAttributes["class"]` | `undefined` | Additional CSS classes merged via `cn()` |
| `as` | `string \| Component` | `"div"` | HTML tag or component to render as (from `PrimitiveProps`) |
| `asChild` | `boolean` | `false` | Merge props and slot content onto the child element instead of rendering a wrapper (from `PrimitiveProps`) |

## Variants

| Variant | Background | Text | Border | Hover (link context) |
|---|---|---|---|---|
| `default` | `bg-primary` | `text-primary-foreground` | transparent | `bg-primary/90` |
| `secondary` | `bg-secondary` | `text-secondary-foreground` | transparent | `bg-secondary/90` |
| `destructive` | `bg-destructive` (60% opacity in dark) | `text-white` | transparent | `bg-destructive/90` |
| `outline` | transparent | `text-foreground` | `border` (default ring color) | `bg-accent` / `text-accent-foreground` |

> Hover styles (`[a&]:hover:*`) only apply when the badge is rendered as or inside an `<a>` element.

## Inherited Primitive Props

`Badge` extends `PrimitiveProps` from `reka-ui`, so it accepts all `Primitive` props:

| Prop | Type | Description |
|---|---|---|
| `as` | `AsTag \| Component` | The element or component to render |
| `asChild` | `boolean` | Merge slot content into the child component |

See [reka-ui Primitive docs](https://reka-ui.com/docs/utilities/primitive) for full details.

## Using `badgeVariants` directly

`badgeVariants` is a standalone CVA function exported from `index.ts`. Use it to apply badge styles without the Vue component:

```ts
import { badgeVariants } from "@/components/ui/badge"

// Generates the full class string for the destructive variant
const classes = badgeVariants({ variant: "destructive" })
```

This is useful when:
- Rendering badges inside a `v-for` with dynamic tag types
- Applying badge styles to third-party components that accept a `class` prop
- Server-side rendering without Vue component overhead

## Slots

| Slot | Description |
|---|---|
| `default` | Badge content — text, icons, or any inline elements |

## Emits

No custom emits. Native DOM events pass through via `Primitive`.

## CSS Custom Properties / Tokens Used

The component relies on these Tailwind CSS design tokens (defined in your CSS/theme):

- `--primary` / `--primary-foreground`
- `--secondary` / `--secondary-foreground`
- `--destructive`
- `--accent` / `--accent-foreground`
- `--foreground`
- `--ring`

## `as` vs `asChild`

**`as` prop** — renders a different HTML tag:

```vue
<Badge as="span" variant="secondary">Label</Badge>
<!-- renders: <span class="...badge classes...">Label</span> -->
```

**`asChild` prop** — merges all badge props onto the single child element:

```vue
<Badge asChild variant="default">
  <a href="/new">New</a>
</Badge>
<!-- renders: <a href="/new" class="...badge classes...">New</a> -->
```

Use `asChild` when you need the badge to be a real `<a>` (for accessibility and hover styles) while keeping the badge styling logic in the `Badge` component.
