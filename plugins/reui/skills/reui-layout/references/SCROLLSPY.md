# Scrollspy

Custom Shadcn Scrollspy for React and Tailwind CSS. Dynamically highlights navigation to indicate
current visible section in viewport during page scroll.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (1 total)](#examples-1-total)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/scrollspy
```

## Import

```tsx
import { Scrollspy } from "@/components/reui/scrollspy"
```

## Usage

```tsx
<Scrollspy targetRef={containerRef}>
  <a href="#section-1" data-scrollspy-anchor="section-1">Section 1</a>
  <a href="#section-2" data-scrollspy-anchor="section-2">Section 2</a>
</Scrollspy>

<div ref={containerRef}>
  <div id="section-1">Content 1</div>
  <div id="section-2">Content 2</div>
</div>
```

## Examples (1 total)

### Horizontal

```tsx
"use client"

import { useRef } from "react"
import { Scrollspy } from "@/components/reui/scrollspy"
import { Button } from "@/components/ui/button"
import { ScrollArea } from "@/components/ui/scroll-area"

export function Pattern() {
  const parentRef = useRef<HTMLDivElement>(null)
  const nav = [
    { id: "section-6", label: "Section 1" },
    { id: "section-7", label: "Section 2" },
    { id: "section-8", label: "Section 3" },
    { id: "section-9", label: "Section 4" },
    { id: "section-10", label: "Section 5" },
  ]

  return (
    <div className="w-full space-y-5">
      <div className="flex w-full gap-2">
        <Scrollspy offset={50} targetRef={parentRef} className="flex gap-2.5">
          {nav.map((item) => (
            <Button
              key={item.id}
              variant="outline"
              data-scrollspy-anchor={item.id}
              className="data-[active=true]:bg-primary data-[active=true]:text-primary-foreground"
            >
              {item.label}
            </Button>
          ))}
        </Scrollspy>
      </div>
      <div className="w-full" ref={parentRef}>
        <ScrollArea className="h-[400px] grow">
          <div className="space-y-8">
            {nav.map((item) => (
              <div key={item.id} id={item.id} className="space-y-2.5">
                <h3 className="text-foreground text-base">{item.label}</h3>
                <div className="bg-muted rounded-2xl h-[350px]"></div>
              </div>
            ))}
          </div>
        </ScrollArea>
      </div>
    </div>
  )
}
```

A second, vertical variant of the same pattern is also shown upstream (nav column at fixed width
`w-[150px]` beside a `grow` scroll area) — same props, `offset={50}` and `targetRef={parentRef}`, just
laid out with `flex-col` instead of horizontally.

## API Reference

### Scrollspy

The main component that wraps the navigation links and manages the scroll spying logic.

| Prop | Type | Default | Description |
|---|---|---|---|
| `targetRef` | `RefObject` | `window` | The scrollable container to monitor. |
| `onUpdate` | `(id: string) => void` | `-` | Callback fired when the active section changes. |
| `offset` | `number` | `0` | Global pixel offset from the top when calculating active sections. |
| `smooth` | `boolean` | `true` | Whether to use smooth scrolling when clicking on anchors. |
| `history` | `boolean` | `true` | Whether to update the URL hash when the active section changes. |
| `dataAttribute` | `string` | `"scrollspy"` | The prefix for data attributes (e.g., `data-scrollspy-anchor`). |
| `className` | `string` | `-` | Additional CSS classes for the wrapper. |

### Data Attributes

Navigation links within `Scrollspy` should use these attributes to connect to sections:

| Attribute | Description |
|---|---|
| `data-scrollspy-anchor` | Required. The ID of the target section (without the `#`). |
| `data-scrollspy-offset` | Optional. Overrides the global `offset` for this specific link. |

The component adds `data-active="true"` to the link element when its corresponding section is
active.

## Base UI vs Radix UI

The Base UI and Radix UI pages are textually identical apart from the "Free Components" marketing
sentence. Import path (`@/components/reui/scrollspy`), installation command, the Horizontal example,
and the full API Reference (props and data attributes) are unchanged between builds — `Scrollspy` has
no dependency on either primitive library.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI. For this specific component the distinction is immaterial.

## Source

- Base UI: `docs/components/base/scrollspy` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/scrollspy` — mirror captured 2026-09-04.
