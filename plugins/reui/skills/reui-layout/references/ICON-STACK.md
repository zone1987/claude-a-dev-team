# Icon Stack

Custom Shadcn Icon Stack for React and Tailwind CSS. Shadcn Icon Stack for isometric icons, layered
icon illustrations, and empty-state visuals.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (5 total)](#examples-5-total)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/icon-stack
```

## Import

```tsx
import { InboxIcon } from "lucide-react"
import { IconStack } from "@/components/reui/icon-stack"
```

## Usage

```tsx
<IconStack aria-hidden="true">
  <InboxIcon className="size-4" />
</IconStack>
```

`IconStack` is a shadcn-compatible ReUI primitive for building layered isometric icons and compact
isometric illustrations. Use it for empty states, onboarding steps, feature cards, dashboard status
panels, and small UI moments that need more depth than a flat icon.

The main preview shows the basic shadcn icon stack pattern: a layered SVG stack with one centered
icon. Style the inner icon or custom content directly with its own `className`; the stack only
provides the isometric artwork and overlay position. Keep meaningful labels in surrounding copy and
mark purely decorative stacks with `aria-hidden="true"`.

## Examples (5 total)

### Sizes

```tsx
import { IconStack } from "@/components/reui/icon-stack"
import { ArchiveIcon, LayersIcon, PackageIcon } from "lucide-react"

const sizes = [
  { label: "Small", className: "h-16 w-14", icon: <ArchiveIcon className="size-3.5" /> },
  { label: "Default", className: "h-20 w-18", icon: <PackageIcon className="size-4" /> },
  { label: "Large", className: "h-28 w-24", icon: <LayersIcon className="size-6" /> },
]

export function Pattern() {
  return (
    <div className="flex flex-wrap items-end justify-center gap-8">
      {sizes.map((item) => (
        <div key={item.label} className="flex flex-col items-center gap-2">
          <IconStack aria-hidden="true" className={item.className}>
            {item.icon}
          </IconStack>
          <span className="text-muted-foreground text-sm">{item.label}</span>
        </div>
      ))}
    </div>
  )
}
```

### Colors

```tsx
import { IconStack } from "@/components/reui/icon-stack"
import { SparklesIcon } from "lucide-react"

const stacks = [
  { label: "Neutral", className: "text-foreground", iconClassName: "text-muted-foreground" },
  { label: "Primary", className: "text-primary", iconClassName: "text-primary" },
  { label: "Success", className: "text-success", iconClassName: "text-success" },
  { label: "Warning", className: "text-warning", iconClassName: "text-warning" },
]

export function Pattern() {
  return (
    <div className="flex flex-wrap items-end justify-center gap-7">
      {stacks.map((item) => (
        <div key={item.label} className="flex flex-col items-center gap-2">
          <IconStack aria-hidden="true" className={item.className}>
            <SparklesIcon className={`size-4 ${item.iconClassName}`} />
          </IconStack>
          <span className="text-muted-foreground text-sm">{item.label}</span>
        </div>
      ))}
    </div>
  )
}
```

Note: the `Colors` example uses the `text-success` and `text-warning` utility classes directly (the
extended semantic tokens also used by Alert and Badge — see
`skills/reui-theming/references/TOKENS.md`), confirming `IconStack` inherits color purely via
`currentColor`/`text-*` on its wrapper, with no `variant` prop of its own.

### Icon Badge

```tsx
import { IconStack } from "@/components/reui/icon-stack"
import { CheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <div className="flex items-center justify-center">
      <IconStack aria-hidden="true" className="text-primary h-24 w-22">
        <span className="bg-background text-primary flex size-8 items-center justify-center rounded-full border shadow-xs">
          <CheckIcon className="size-4" />
        </span>
      </IconStack>
    </div>
  )
}
```

### Empty State Illustration

```tsx
import { IconStack } from "@/components/reui/icon-stack"
import { Button } from "@/components/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
import { DatabaseIcon, InboxIcon, UserPlusIcon } from "lucide-react"

export function Pattern() {
  return (
    <div className="flex items-center justify-center p-4">
      <Empty className="max-w-md py-10">
        <EmptyHeader>
          <EmptyMedia>
            <IconStack aria-hidden="true" className="text-primary h-24 w-22">
              <InboxIcon className="text-primary size-5" />
            </IconStack>
          </EmptyMedia>
          <EmptyTitle>Workspace is ready</EmptyTitle>
          <EmptyDescription>
            Invite teammates or connect a data source to start filling this view.
          </EmptyDescription>
        </EmptyHeader>
        <EmptyContent className="flex-row justify-center gap-2">
          <Button size="sm">
            <UserPlusIcon data-icon="inline-start" />
            Invite team
          </Button>
          <Button variant="outline" size="sm">
            <DatabaseIcon data-icon="inline-start" />
            Connect source
          </Button>
        </EmptyContent>
      </Empty>
    </div>
  )
}
```

### Item Media

```tsx
import { IconStack } from "@/components/reui/icon-stack"
import { Item, ItemContent, ItemDescription, ItemMedia, ItemTitle } from "@/components/ui/item"
import { PackageIcon } from "lucide-react"

export function Pattern() {
  return (
    <div className="mx-auto flex w-full max-w-md items-center justify-center p-4">
      <Item variant="outline" className="max-w-sm">
        <ItemMedia>
          <IconStack aria-hidden="true" className="text-primary h-12 w-11">
            <PackageIcon className="text-primary size-3" />
          </IconStack>
        </ItemMedia>
        <ItemContent>
          <ItemTitle>Registry package ready</ItemTitle>
          <ItemDescription>Use IconStack as rich media inside compact shadcn items.</ItemDescription>
        </ItemContent>
      </Item>
    </div>
  )
}
```

## API Reference

### IconStack

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Controls the outer wrapper size, color, and layout. |
| `children` | `React.ReactNode` | `-` | Renders optional decorative content inside the stack. |

All native `div` props are supported.

## Base UI vs Radix UI

The Base UI and Radix UI pages are textually identical apart from the "Free Components" marketing
sentence. Import path (`@/components/reui/icon-stack`), installation command, all five examples, and
the two-row API Reference table are unchanged between builds — `IconStack` renders a plain `div` with
no Base UI or Radix UI primitive dependency.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI. For this specific component the distinction is immaterial.

## Source

- Base UI: `docs/components/base/icon-stack` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/icon-stack` — mirror captured 2026-09-04.
