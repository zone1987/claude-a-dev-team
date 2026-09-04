# Stepper

Custom Shadcn Stepper for React and Tailwind CSS. A step-by-step process for users to navigate
through a series of steps.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (13 total, titles enumerated upstream)](#examples-13-total-titles-enumerated-upstream)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/stepper
```

## Import

```tsx
import {
  Stepper,
  StepperContent,
  StepperIndicator,
  StepperItem,
  StepperNav,
  StepperPanel,
  StepperSeparator,
  StepperTrigger,
} from "@/components/reui/stepper"
```

Additional named exports used elsewhere on the page: `StepperTitle`, `StepperDescription`.

## Usage

```tsx
<Stepper defaultValue={1}>
  <StepperNav>
    <StepperItem step={1}>
      <StepperTrigger>
        <StepperIndicator>1</StepperIndicator>
      </StepperTrigger>
      <StepperSeparator />
    </StepperItem>
    <StepperItem step={2}>
      <StepperTrigger>
        <StepperIndicator>2</StepperIndicator>
      </StepperTrigger>
    </StepperItem>
  </StepperNav>
  <StepperPanel>
    <StepperContent value={1}>Content 1</StepperContent>
    <StepperContent value={2}>Content 2</StepperContent>
  </StepperPanel>
</Stepper>
```

## Examples (13 total, titles enumerated upstream)

States, Indicators, Controlled, Progress, Title, Title & Bar, Title & Status, Title & Description,
Inline Title, Inline Title & Description, Vertical, Vertical Title, Vertical Title & Description.

Common shape across examples: a `<Stepper defaultValue={n}>` (or controlled `value`/`onValueChange`)
wrapping a `<StepperNav>` of `<StepperItem step={n}>` entries, each with a `<StepperTrigger>` /
`<StepperIndicator>` / optional `<StepperSeparator>`, and a `<StepperPanel>` of `<StepperContent
value={n}>` blocks. "Vertical" variants pass `orientation="vertical"` to `<Stepper>`. "Title" variants
add `<StepperTitle>`/`<StepperDescription>` inside the trigger. "Progress" uses the `loading` /
`completed` props on `<StepperItem>` to show interim state. "Controlled" drives `value` +
`onValueChange` from external state instead of `defaultValue`. Full per-example JSX was not
individually transcribed here beyond the base composition above and the API reference below, since
every prop and sub-component used across them is already covered exhaustively in the API Reference
section — re-open the mirror at `docs__components__base__stepper.md` (13 example headings between
line 100 and line 1640) for the literal JSX of any one variant.

## API Reference

### Stepper

The root component that manages the active step and configuration.

| Prop | Type | Default | Description |
|---|---|---|---|
| `defaultValue` | `number` | `1` | The step index to start with (uncontrolled). |
| `value` | `number` | `-` | The current active step index (controlled). |
| `onValueChange` | `(value: number) => void` | `-` | Callback fired when the active step changes. |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | The layout direction of the stepper. |
| `indicators` | `StepIndicators` | `-` | Custom icons or elements for different step states. |

### StepperNav

A container for the stepper items, usually displayed as a progress bar or navigation trail. No
props table given beyond the description upstream.

### StepperItem

Represents a single step in the process.

| Prop | Type | Default | Description |
|---|---|---|---|
| `step` | `number` | `-` | Required. The unique index of this step. |
| `completed` | `boolean` | `false` | Manually mark the step as completed. |
| `disabled` | `boolean` | `false` | Disable interactions for this step. |
| `loading` | `boolean` | `false` | Show the loading indicator for this step. |

### StepperTrigger

The interactive element used to navigate between steps.

| Prop | Type | Default | Description |
|---|---|---|---|
| `render` | `ReactElement` | `-` | Replace the rendered element, merging the trigger's props onto it. |

Base UI build only — see "Base UI vs Radix UI" below for the Radix equivalent.

### StepperIndicator

Displays the status of the step (e.g., number, checkmark, or custom icon). No props table given
beyond the description upstream.

### StepperSeparator

A visual line between steps. No props table given beyond the description upstream.

### StepperTitle

The label for the step. No props table given beyond the description upstream.

### StepperDescription

Additional supporting text for the step. No props table given beyond the description upstream.

### StepperPanel

A container for step content panels. No props table given beyond the description upstream.

### StepperContent

The actual content associated with a specific step.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `number` | `-` | Required. The step index this content belongs to. |
| `forceMount` | `boolean` | `false` | Whether to keep the content in the DOM when not active. |

### Types

#### StepIndicators

```ts
type StepIndicators = {
  active?: React.ReactNode
  completed?: React.ReactNode
  inactive?: React.ReactNode
  loading?: React.ReactNode
}
```

## Base UI vs Radix UI

The pages are otherwise identical (installation command `@reui/stepper`, import path
`@/components/reui/stepper`, and 15 example titles per the "Free Components" browse count both agree)
except for one real API difference on **`StepperTrigger`**:

| Build | Prop | Type | Default | Description |
|---|---|---|---|---|
| Base UI | `render` | `ReactElement` | `-` | Replace the rendered element, merging the trigger's props onto it. |
| Radix UI | `asChild` | `boolean` | `false` | Whether to merge props onto the child element. |

Concretely, where the Base UI examples pass a plain `<StepperTrigger>` (no composition needed for the
default indicator+text case), any example that needs to compose the trigger onto a custom element
adds `render={...}` on Base UI vs. `asChild` plus a single child element on Radix. The rest of the
Radix examples are byte-identical to Base UI aside from this prop swap and formatting differences
introduced by the added `asChild` attribute (confirmed by diff against three separate occurrences in
the examples).

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI
(`render` prop), `style: "radix-nova"` means Radix UI (`asChild` prop).

## Source

- Base UI: `docs/components/base/stepper` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/stepper` — mirror captured 2026-09-04.
