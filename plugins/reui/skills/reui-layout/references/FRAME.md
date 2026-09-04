# Frame

Custom Shadcn Frame for React and Tailwind CSS. Displays related content in a structured frame.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (6 titled upstream)](#examples-6-titled-upstream)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/frame
```

## Import

```tsx
import {
  Frame,
  FrameDescription,
  FrameFooter,
  FrameHeader,
  FramePanel,
  FrameTitle,
} from "@/components/reui/frame"
```

## Usage

```tsx
<Frame>
  <FramePanel>
    <FrameHeader>
      <FrameTitle>Frame Title</FrameTitle>
      <FrameDescription>Frame Description</FrameDescription>
    </FrameHeader>
    <div className="p-5">Frame Content</div>
    <FrameFooter>Frame Footer</FrameFooter>
  </FramePanel>
</Frame>
```

### Customizing Radius

You can customize the border radius of the frame and its panels using the `--frame-radius` CSS
variable.

```tsx
<Frame className="[--frame-radius:var(--radius-lg)]">
  <FramePanel>...</FramePanel>
</Frame>
```

## Examples (6 titled upstream)

With Separated Panels, With Stacked Panels, With Dense Panels, Without Outer Border, Custom Spacing,
Custom Radius. The mirror captured these section headings and the shared root API below; the
individual JSX bodies for these six were not each independently transcribed since every prop and
sub-component they exercise (`variant`, `spacing`, `stacked`, `dense`, and the `--frame-radius` /
`--frame-panel-radius` CSS variables) is already covered exhaustively by the API Reference and
"Customizing Radius" sections above/below — e.g. "With Stacked Panels" is inferred to pass
`stacked` on `<Frame>`, "With Dense Panels" to pass `dense`, per their prop descriptions.

## API Reference

### Frame

The root container for one or more frame panels.

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "ghost"` | `"default"` | The visual style of the frame container. |
| `spacing` | `"sm" \| "default" \| "lg"` | `"default"` | The internal padding of the frame and margin between panels. |
| `stacked` | `boolean` | `false` | If true, removes margins between panels and connects them vertically with shared borders. |
| `dense` | `boolean` | `false` | If true, removes padding on the panel. |
| `className` | `string` | `-` | Additional CSS classes for the container. |

### CSS Variables

| Variable | Default | Description |
|---|---|---|
| `--frame-radius` | `var(--radius-xl)` | The outer border radius of the frame. Panels derive their radius from it, so this is the single knob to adjust. |
| `--frame-panel-radius` | `calc(var(--frame-radius) - var(--frame-px) - 1px)` | The inner panel radius, reduced from `--frame-radius` so panel corners nest concentrically inside the frame. |

### FramePanel

A card-like container within the frame that holds header, content, and footer.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the panel. |

### FrameHeader

A container for the title and description, with default padding.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the header. |

### FrameTitle

Heading for the frame panel.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the title. |

### FrameDescription

Supporting text for the frame panel.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the description. |

### FrameFooter

A container for actions or additional information at the bottom of the panel.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the footer. |

## Base UI vs Radix UI

Installation command and import path are unchanged between builds (`@reui/frame`,
`@/components/reui/frame`), and the full API Reference table above is identical. The only diffs found
by full-file comparison are the "Free Components" marketing sentence and one cosmetic text change in
an example heading (`"Section title 2"` in Base UI vs. `"Section title"` in Radix UI) — not a prop or
behavioural difference.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI.

## Source

- Base UI: `docs/components/base/frame` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/frame` — mirror captured 2026-09-04.
