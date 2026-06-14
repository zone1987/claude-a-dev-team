# Button — API Reference

## Button

| Prop | Type | Default |
|------|------|---------|
| `variant` | see variants | `"default"` |
| `size` | see sizes | `"default"` |
| `asChild` (Radix) | `boolean` | `false` |
| `className` | `string` | — |

## Variants

| Variant | Description |
|---------|-------------|
| `default` | Primary filled |
| `outline` | Border, transparent bg |
| `secondary` | Secondary color |
| `ghost` | Transparent, hover bg |
| `destructive` | Red/error |
| `link` | Underline link style |

## Sizes

| Size | Height | Notes |
|------|--------|-------|
| `default` | 36px | Standard |
| `xs` | 24px | Extra small |
| `sm` | 32px | Small |
| `lg` | 40px | Large |
| `icon` | 36x36px | Square icon button |
| `icon-xs` | 24x24px | — |
| `icon-sm` | 32x32px | — |
| `icon-lg` | 40x40px | — |

## buttonVariants export

Apply button styling to non-Button elements (links etc.):

```tsx
import { buttonVariants } from "@/components/ui/button"

<a href="/login" className={buttonVariants({ variant: "outline" })}>
  Login
</a>
```

## asChild pattern (Radix)

```tsx
<Button asChild>
  <Link href="/login">Login</Link>
</Button>
```

## Base UI note

Do NOT use `<Button render={<a />}>` for links — Base UI always adds
`role="button"` which overrides the link semantics. Use `buttonVariants`
with a plain `<a>` tag instead.

## data-slot values

- `data-slot="button"`
- `data-variant="<variant>"`
- `data-size="<size>"`

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/button.mdx`
