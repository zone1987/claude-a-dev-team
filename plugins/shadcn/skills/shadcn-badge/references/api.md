# Badge — API Reference

## Badge

| Prop | Type | Default |
|------|------|---------|
| `variant` | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `asChild` (Radix) | `boolean` | `false` |
| `render` (Base) | render prop | — |
| `className` | `string` | — |

## badgeVariants export

Use to apply badge styling to non-Badge elements:

```tsx
import { badgeVariants } from "@/components/ui/badge"

<a className={badgeVariants({ variant: "outline" })}>Link Badge</a>
```

## Variants

| Variant | Description |
|---------|-------------|
| `default` | Primary color background |
| `secondary` | Secondary color background |
| `destructive` | Red/error background |
| `outline` | Border only |
| `ghost` | Transparent, hover effect |
| `link` | Text link style |

## Icons inside Badge

```tsx
<Badge>
  <CheckIcon data-icon="inline-start" />
  Verified
</Badge>
```

Use `data-icon="inline-start"` or `data-icon="inline-end"` for proper spacing.

## data-slot values

- `data-slot="badge"`
- `data-variant="<variant>"`

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/badge.mdx`
