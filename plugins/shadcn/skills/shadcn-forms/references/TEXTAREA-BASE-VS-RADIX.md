# Textarea — new-york-v4 vs. Radix Base

Both variants wrap a native `<textarea>` element directly. There is no external
Radix UI primitive involved — `Textarea` is a plain HTML element with Tailwind
class names applied via `cn()`.

## new-york-v4 (fully styled)

**File**: `registry/new-york-v4/ui/textarea.tsx`

Includes all visual styles out of the box:

- `rounded-md border border-input` — standard input border
- `bg-transparent` / `dark:bg-input/30` — background with dark mode variant
- `px-3 py-2 text-base md:text-sm` — padding and responsive font size
- `shadow-xs` — subtle box shadow
- `transition-[color,box-shadow]` — smooth transitions
- `outline-none` — removes default browser outline
- `placeholder:text-muted-foreground` — muted placeholder color
- `focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50` — accessible focus ring
- `disabled:cursor-not-allowed disabled:opacity-50` — disabled state
- `aria-invalid:border-destructive aria-invalid:ring-destructive/20` — validation error state (light mode)
- `dark:aria-invalid:ring-destructive/40` — validation error state (dark mode)
- `field-sizing-content min-h-16` — auto-resize with minimum height

This variant is ready to use in any shadcn/ui project without additional CSS.

## Radix base (minimal / unstyled)

**File**: `registry/bases/radix/ui/textarea.tsx`

Contains only structural and accessibility styles:

- `cn-textarea` — hook class for design system overrides
- `field-sizing-content min-h-16 w-full` — structural sizing
- `outline-none` — removes default browser outline
- `placeholder:text-muted-foreground` — minimal placeholder tint
- `disabled:cursor-not-allowed disabled:opacity-50` — disabled state

No border, background, shadow, focus ring, or error styles are applied.
This variant is intended for use in custom design systems where all visual
styles are applied via the `cn-textarea` class or a CSS layer.

## When to use which

| Scenario | Variant |
|----------|---------|
| Standard shadcn/ui project | new-york-v4 |
| Design system with own CSS tokens/themes | Radix base |
| Rapid prototyping | new-york-v4 |
| Headless / fully custom styling | Radix base |
