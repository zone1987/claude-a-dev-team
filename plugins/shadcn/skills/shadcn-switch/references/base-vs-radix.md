# Switch — Base UI vs Radix Primitive

shadcn/ui provides three variants of the Switch component, each backed by a different primitive. This document explains the differences so you can choose the right one.

## Summary

| | new-york-v4 (Radix) | Radix base | Base UI |
|---|---|---|---|
| Primitive package | `radix-ui` | `radix-ui` | `@base-ui/react` |
| Import path | `radix-ui` (Switch) | `radix-ui` (Switch) | `@base-ui/react/switch` |
| Styling approach | Inline Tailwind utilities | External CSS tokens | External CSS tokens |
| `data-state` attribute | `checked` / `unchecked` | `checked` / `unchecked` | — |
| `data-disabled` attribute | — | — | present when disabled |
| Props type source | `React.ComponentProps<typeof SwitchPrimitive.Root>` | `React.ComponentProps<typeof SwitchPrimitive.Root>` | `SwitchPrimitive.Root.Props` |
| Touch target expansion | No | `after:absolute after:-inset-x-3 after:-inset-y-2` | `after:absolute after:-inset-x-3 after:-inset-y-2` |
| Recommended for | Tailwind-first projects using shadcn CLI | Design systems with CSS tokens | Design systems with CSS tokens using Base UI |

## Primitive differences

### Radix UI (`radix-ui`)

- Mature, battle-tested accessibility primitive.
- State is surfaced via `data-state="checked"` and `data-state="unchecked"` on the root element.
- Disabled state uses the HTML `disabled` attribute and `data-disabled`.
- Well-documented, large community.

### Base UI (`@base-ui/react`)

- Newer, actively developed successor spirit to Radix UI (some of the same authors).
- State attributes use `data-checked` and `data-unchecked` rather than `data-state`.
- Disabled state is surfaced as `data-disabled` (no HTML `disabled` attribute by default on the button).
- Designed for headless use without imposing DOM structure; the thumb element is a first-class sub-component.
- Smaller ecosystem but growing.

## When to choose each

**Use new-york-v4 (Radix)** when:
- You are starting a new project with `npx shadcn@latest add switch`.
- You want all styles to live in Tailwind utilities — no external stylesheet required.
- You prefer maximum compatibility with the full shadcn/ui ecosystem.

**Use Radix base** when:
- You are building or extending a design system that uses CSS custom properties / design tokens.
- You want Radix semantics (`data-state`) but prefer to apply styles externally.
- You are migrating an existing Radix-based component library.

**Use Base UI** when:
- You are specifically adopting `@base-ui/react` across your component library.
- You want the latest primitive API and are comfortable with a newer ecosystem.
- You need `data-disabled` instead of HTML `disabled` for certain CSS patterns.

## Data attribute comparison

```tsx
// Radix / new-york-v4: state via data-state
<button
  role="switch"
  data-state="checked"     // or "unchecked"
  data-slot="switch"
  data-size="default"
/>

// Base UI: state via data-checked / data-unchecked
<button
  role="switch"
  data-checked             // present when checked
  data-slot="switch"
  data-size="default"
  data-disabled            // present when disabled
/>
```

## CSS targeting

```css
/* new-york-v4 / Radix base */
[data-slot="switch"][data-state="checked"] { /* checked styles */ }
[data-slot="switch"][data-state="unchecked"] { /* unchecked styles */ }
[data-slot="switch-thumb"][data-state="checked"] { /* thumb checked */ }

/* Base UI */
[data-slot="switch"][data-checked] { /* checked styles */ }
[data-slot="switch"][data-disabled] { /* disabled styles */ }
[data-slot="switch-thumb"] { /* thumb styles */ }
```
