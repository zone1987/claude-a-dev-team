# Badge

Custom Shadcn Badge for React and Tailwind CSS. Badges are used to highlight items, notify users, or
display statuses.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (21 total)](#examples-21-total)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/badge
```

## Import

```tsx
import { Badge } from "@/components/reui/badge"
```

## Usage

```tsx
<Badge>Badge</Badge>
```

## Examples (21 total)

### Secondary

```tsx
import { Badge } from "@/components/reui/badge"

export function Pattern() {
  return <Badge variant="secondary">Badge</Badge>
}
```

### Destructive

```tsx
<Badge variant="destructive">Badge</Badge>
```

### Success

```tsx
<Badge variant="success">Badge</Badge>
```

### Info

```tsx
<Badge variant="info">Badge</Badge>
```

### Warning

```tsx
<Badge variant="warning">Badge</Badge>
```

### Outline

```tsx
<Badge variant="outline">Badge</Badge>
```

### Primary Outline

```tsx
<Badge variant="primary-outline">Badge</Badge>
```

### Destructive Outline

```tsx
<Badge variant="destructive-outline">Badge</Badge>
```

### Info Outline

```tsx
<Badge variant="info-outline">Badge</Badge>
```

### Success Outline

```tsx
<Badge variant="success-outline">Badge</Badge>
```

### Warning Outline

```tsx
<Badge variant="warning-outline">Badge</Badge>
```

### Primary Light

```tsx
<Badge variant="primary-light">Badge</Badge>
```

### Destructive Light

```tsx
<Badge variant="destructive-light">Badge</Badge>
```

### Success Light

```tsx
<Badge variant="success-light">Badge</Badge>
```

### Info Light

```tsx
<Badge variant="info-light">Badge</Badge>
```

### Warning Light

```tsx
<Badge variant="warning-light">Badge</Badge>
```

### Size

```tsx
import { Badge } from "@/components/reui/badge"

export function Pattern() {
  return (
    <div className="flex items-center gap-2.5">
      <Badge size="sm">Small</Badge>
      <Badge size="default">Default</Badge>
      <Badge size="lg">Large</Badge>
    </div>
  )
}
```

### Full Radius

```tsx
import { Badge } from "@/components/reui/badge"

export function Pattern() {
  return (
    <div className="flex flex-col items-center justify-center gap-6">
      <div className="flex items-center gap-2.5">
        <Badge size="sm" radius="full">3</Badge>
        <Badge size="default" radius="full">3</Badge>
        <Badge size="lg" radius="full">3</Badge>
      </div>
      <div className="flex items-center gap-2.5">
        <Badge size="sm" radius="full">New</Badge>
        <Badge radius="full">New</Badge>
        <Badge size="lg" radius="full">New</Badge>
      </div>
      <div className="flex items-center gap-2.5">
        <Badge size="sm" radius="full" variant="outline">New</Badge>
        <Badge radius="full" variant="secondary">New</Badge>
        <Badge size="lg" radius="full" variant="success-light">New</Badge>
      </div>
    </div>
  )
}
```

### With Icon

```tsx
import { Badge } from "@/components/reui/badge"
import { CheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <Badge variant="outline">
      <CheckIcon />
      Badge
    </Badge>
  )
}
```

### With Icon Button

```tsx
import { Badge } from "@/components/reui/badge"
import { Button } from "@/components/ui/button"
import { XIcon } from "lucide-react"

export function Pattern() {
  return (
    <Badge variant="outline" className="gap-0.5">
      Badge
      <Button variant="ghost" size="icon" className="size-3 hover:bg-transparent">
        <XIcon />
      </Button>
    </Badge>
  )
}
```

### With Dot

```tsx
import { Badge } from "@/components/reui/badge"

export function Pattern() {
  return (
    <Badge variant="info-light">
      <span className="ms-0.25 size-1.25 rounded-full! bg-[currentColor]" />{" "}
      Badge
    </Badge>
  )
}
```

### With Link

```tsx
import { Badge } from "@/components/reui/badge"

export function Pattern() {
  return (
    <Badge variant="outline" render={<a href="#" />}>
      Badge
    </Badge>
  )
}
```

`render` here is the Base UI composition prop — see "Base UI vs Radix UI" below for the Radix
equivalent (`asChild`).

## API Reference

This component follows the same API design as the Badge component from shadcn/ui. The key
difference is that it uses extended color tokens — `--success`, `--info`, `--warning`, and
`--invert` — for badge variants instead of utility classes. This approach enables consistent,
reusable state variants across the project without relying on custom Tailwind color utilities.

```tsx
<Badge variant="success-light" size="sm">
  Success
</Badge>
```

```tsx
<Badge variant="outline" radius="full">
  Pill
</Badge>
```

### Props

| Prop | Type |
|---|---|
| `variant` | `"default" \| "secondary" \| "destructive" \| "outline" \| "info" \| "success" \| "warning" \| "invert"` |
| `variant` (Outline) | `"primary-outline" \| "warning-outline" \| "success-outline" \| "info-outline" \| "destructive-outline" \| "invert-outline"` |
| `variant` (Light) | `"primary-light" \| "warning-light" \| "success-light" \| "info-light" \| "destructive-light" \| "invert-light"` |
| `size` | `"default" \| "xs" \| "sm" \| "lg" \| "xl"` |
| `radius` | `"default"` (active style radius) \| `"full"` (`rounded-full`) |

The upstream Props table gives only types (rendered as three separate `variant` rows to keep the
base/outline/light families visually distinct on the docs page); no default and no per-row
description beyond the two sentences above the table are stated for any of these rows. Treat
defaults and descriptions here as unstated upstream, except for `radius` where the table cell itself
states the two behaviours inline.

### All variant values (union of the three rows above, 20 total)

`default`, `secondary`, `destructive`, `outline`, `info`, `success`, `warning`, `invert`,
`primary-outline`, `warning-outline`, `success-outline`, `info-outline`, `destructive-outline`,
`invert-outline`, `primary-light`, `warning-light`, `success-light`, `info-light`,
`destructive-light`, `invert-light`.

Note: `invert-outline` and `invert-light` are listed in the Props table's enum on both the Base UI
and Radix UI pages, but only `invert-light` has its own worked example — and only on the Radix UI
page (see "Base UI vs Radix UI" below). Neither page has a worked example for `invert` (plain),
`invert-outline`, or `primary` (plain, un-suffixed) — those three enum values are attested by the
Props table only, not by an example.

### Variant-to-token map

| `variant` family | Token used |
|---|---|
| `default`, `secondary`, `destructive`, `outline` | shadcn/ui defaults (no extended token) |
| `info`, `info-outline`, `info-light` | `--info` / `--info-foreground` |
| `success`, `success-outline`, `success-light` | `--success` / `--success-foreground` |
| `warning`, `warning-outline`, `warning-light` | `--warning` / `--warning-foreground` |
| `invert`, `invert-outline`, `invert-light` | `--invert` / `--invert-foreground` |
| `primary-outline`, `primary-light` | primary token family (shadcn `--primary`), not one of the four extended semantic tokens |

This page does not itself enumerate the light/dark values of `--success`, `--info`, `--warning`,
`--invert`, or their `-foreground` pairs — see `skills/reui-theming/references/TOKENS.md` for the
distilled light and dark values of these tokens (shared with Alert).

## Base UI vs Radix UI

Two real differences beyond the "Free Components" marketing sentence:

1. **Import path changes**, like Sortable and Timeline:

   | Build | Install | Import |
   |---|---|---|
   | Base UI | `pnpm dlx shadcn@latest add @reui/badge` | `@/components/reui/badge` |
   | Radix UI | `pnpm dlx shadcn@latest add @reui/r-badge` | `@/components/reui/r-badge` |

2. **The Radix UI page has one extra worked example the Base UI page lacks: "Invert Light"**
   (`<Badge variant="invert-light">Badge</Badge>`), inserted after "Warning Light" and before
   "Size" in its on-page outline. The Base UI page's Props table already lists `invert-light` as a
   valid `variant` value, so this is a missing *example*, not a missing *variant* — the prop itself
   is documented identically on both pages.

3. **Composition prop**: the "With Link" example uses `render={<a href="#" />}` on Base UI vs.
   `asChild` with a nested `<a href="#">Badge</a>` child on Radix UI — the same `render`-prop vs.
   `asChild` pattern seen on Stepper, Kanban, and Icon Tile.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI
(`@reui/badge`, `render` composition), `style: "radix-nova"` means Radix UI (`@reui/r-badge`,
`asChild` composition).

## Source

- Base UI: `docs/components/base/badge` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/badge` — mirror captured 2026-09-04.
