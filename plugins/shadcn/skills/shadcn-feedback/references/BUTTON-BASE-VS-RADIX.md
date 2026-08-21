# Button — Base UI vs Radix UI

## Underlying primitive

| | Radix UI | Base UI |
|---|---|---|
| Primitive | `Slot.Root` from `radix-ui` (for asChild) | `ButtonPrimitive` from `@base-ui/react/button` |
| Base element | `<button>` | Base UI Button always has `role="button"` |

## asChild vs render

| | Radix UI | Base UI |
|---|---|---|
| Polymorphic | `asChild` boolean | Standard `render` / children pattern |
| Link pattern | `<Button asChild><Link href="/" />` | Use `buttonVariants` + plain `<a>` |

## IMPORTANT: Links with Base UI

Base UI `Button` always applies `role="button"`, which overrides the
semantic link role on `<a>` elements. For navigation links:

```tsx
// Radix: OK
<Button asChild>
  <Link href="/">Home</Link>
</Button>

// Base UI: WRONG - role="button" overrides link semantics
<Button render={<a href="/" />}>Home</Button>

// Base UI: CORRECT
<a href="/" className={buttonVariants({ variant: "outline" })}>
  Home
</a>
```

## Style approach

- Radix: Full Tailwind classes inline in CVA
- Base: `cn-button-variant-*` and `cn-button-size-*` CSS tokens (theme-driven)

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/button.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/button.tsx`
