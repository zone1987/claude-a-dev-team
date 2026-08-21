# Spinner — API Reference

## Spinner

Renders an SVG icon (`Loader2Icon` from lucide-react) with `animate-spin`.

| Prop        | Type     | Default                  | Description                                               |
| ----------- | -------- | ------------------------ | --------------------------------------------------------- |
| `className` | `string` | —                        | Override or extend classes (use `size-*`, `text-*`)       |
| `role`      | `string` | `"status"` (pre-set)     | ARIA role — already set, do not override without reason   |
| `aria-label`| `string` | `"Loading"` (pre-set)    | ARIA label — already set                                  |

All other SVG HTML attributes are forwarded.

## Default styles

- `size-4` — 1rem (16px) width and height
- `animate-spin` — continuous 360° rotation animation
- Inherits `currentColor` from parent (controllable via `text-*` classes)

## Size variants

Use Tailwind `size-*` utility to change size:

```tsx
<Spinner className="size-3" />   {/* 12px */}
<Spinner className="size-4" />   {/* 16px — default */}
<Spinner className="size-6" />   {/* 24px */}
<Spinner className="size-8" />   {/* 32px */}
```

## Color variants

Use Tailwind `text-*` utility:

```tsx
<Spinner className="text-primary" />
<Spinner className="text-muted-foreground" />
<Spinner className="text-red-500" />
```

## Source files

- `registry/new-york-v4/ui/spinner.tsx`
