# Aspect Ratio — Base UI vs Radix UI

## Implementation difference

| | Radix UI | Base UI |
|---|---|---|
| Technique | Radix `AspectRatio.Root` (padding-top trick internally) | Pure CSS `aspect-(--ratio)` with CSS custom property |
| Props | Same as Radix Root | `ratio: number` prop (explicit) |
| SSR | Radix handles it | CSS-based, no JS needed |

## API difference

Radix version passes `ratio` through to the Radix primitive directly.
Base version sets `--ratio` CSS variable and uses `aspect-(--ratio)` class.

```tsx
// Both look the same at usage:
<AspectRatio ratio={16 / 9}>
  <img ... />
</AspectRatio>
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/aspect-ratio.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/aspect-ratio.tsx`
