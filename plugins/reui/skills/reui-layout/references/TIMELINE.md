# Timeline

Custom Shadcn Timeline for React and Tailwind CSS. A visual representation of events in chronological
order.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (9 titled on the Base UI page)](#examples-9-titled-on-the-base-ui-page)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/timeline
```

## Import

```tsx
import {
  Timeline,
  TimelineContent,
  TimelineDate,
  TimelineHeader,
  TimelineIndicator,
  TimelineItem,
  TimelineSeparator,
  TimelineTitle,
} from "@/components/reui/timeline"
```

## Usage

```tsx
<Timeline>
  <TimelineItem step={1}>
    <TimelineHeader>
      <TimelineDate>March 2024</TimelineDate>
      <TimelineTitle>Project Initialized</TimelineTitle>
    </TimelineHeader>
    <TimelineIndicator />
    <TimelineSeparator />
    <TimelineContent>
      Successfully set up the project repository and initial architecture.
    </TimelineContent>
  </TimelineItem>
</Timeline>
```

## Examples (9 titled on the Base UI page)

With Left-Aligned Dates, With Custom Indicators, With Icons, Alternating Layout, Horizontal
Orientation, Horizontal with Top Indicators, Customized Timeline, Compact Roadmap, Activity Feed.

Only the section titles and the root "View Code" markers were present in the mirror for these nine
sections (the expanded JSX bodies were collapsed behind client-rendered "View Code" toggles that this
fetch did not expand). What is attested for all of them: they compose `Timeline` with `orientation`
("vertical" default, "horizontal" for the two Horizontal examples per the API Reference below), and
the sub-components listed in Import. The page also states: "This primitive also powers ready-made
ReUI Pro blocks: complete timeline sections... Preview all 9 Shadcn Timeline Pro blocks in the ReUI
blocks gallery" (Pro blocks are out of scope).

## API Reference

### Timeline

The root component for the timeline.

| Prop | Type | Default | Description |
|---|---|---|---|
| `defaultValue` | `number` | `1` | The initial active step. |
| `value` | `number` | `-` | The current active step (controlled). |
| `onValueChange` | `(value: number) => void` | `-` | Callback fired when the active step changes. |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` | The layout orientation of the timeline. |

### TimelineItem

A single item in the timeline.

| Prop | Type | Default | Description |
|---|---|---|---|
| `step` | `number` | `-` | Required. The step number for this item. |

### TimelineDate

The date or time label for a timeline item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the date label. |

### TimelineTitle

The title for a timeline item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the title. |

### TimelineIndicator

The visual indicator (usually a dot) for a timeline item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the indicator. |

### TimelineSeparator

The line connecting timeline indicators.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the separator line. |

### TimelineHeader

A container for the date and title.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the header container. |

### TimelineContent

The main descriptive content for a timeline item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the content container. |

## Base UI vs Radix UI

The API Reference table and root usage are identical between builds. Two real differences:

1. **Import path changes**, like Sortable and Badge:

   | Build | Install | Import |
   |---|---|---|
   | Base UI | `pnpm dlx shadcn@latest add @reui/timeline` | `@/components/reui/timeline` |
   | Radix UI | `pnpm dlx shadcn@latest add @reui/r-timeline` | `@/components/reui/r-timeline` |

2. **The example set differs.** The Radix UI page swaps two example titles for different ones and
   reorders the rest: Base UI has "Horizontal Orientation" (5th) and "Customized Timeline" /
   "Compact Roadmap" / "Activity Feed" as its last three; Radix UI instead has "Pipeline Steps" (in
   the position Base UI uses for "Horizontal Orientation" in the top-of-page teaser) and "Dot
   Indicators" replacing "Horizontal with Top Indicators" in the on-page nav order, and does not
   list "Activity Feed" at all in its "On This Page" outline. This is a difference in which worked
   examples are shown, not in the component's API — no prop, type, or default differs. One
   formatting-only code diff was also observed inside the shared "Horizontal Orientation" example: Base
   UI writes `group-data-open/collapsible:rotate-90`; Radix UI writes
   `group-data-[state=open]/collapsible:rotate-90` for the same chevron rotation — a Base UI vs.
   Radix data-attribute naming difference (`data-open` vs. `data-state="open"`), not a prop
   difference.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI
(`@reui/timeline`), `style: "radix-nova"` means Radix UI (`@reui/r-timeline`).

## Source

- Base UI: `docs/components/base/timeline` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/timeline` — mirror captured 2026-09-04.
