# Number Field

Custom Shadcn Number Field for React and Tailwind CSS. A numeric input element with increment and
decrement buttons, and a scrub area.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [API Reference](#api-reference)
- [Usage](#usage)
- [Examples (3 total)](#examples-3-total)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/number-field
```

## Import

```tsx
import {
  NumberField,
  NumberFieldDecrement,
  NumberFieldGroup,
  NumberFieldIncrement,
  NumberFieldInput,
  NumberFieldScrubArea,
} from "@/components/ui/number-field"
```

Note: the "Usage" heading on the docs page shows the import resolving to
`"@/components/ui/number-field"` while the example code blocks (below) import from
`"@/components/reui/number-field"`. Both paths are attested verbatim in the mirror; the page does not
explain the discrepancy. Treat `@/components/reui/number-field` as the one actually used in the worked
examples.

## API Reference

reui.io does not document Number Field's props itself. Both the Base UI build page
(`docs/components/base/number-field`) and the Radix UI build page (`docs/components/radix/number-field`)
carry an "API Reference" badge, and on **both** pages that badge links to the same URL:
`https://base-ui.com/react/components/number-field#api-reference`. Radix UI's own primitives
documentation (radix-ui.com) has **no `number-field` component page at all** — its 29-component index
(`primitives/docs/overview/introduction`, checked 2026-09-04) lists none. ReUI's "Radix UI" build of
Number Field is therefore documented against the same Base UI primitive as the "Base UI" build; there
is no separate Radix-primitives table to report.

Every table below is copied verbatim from `https://base-ui.com/react/components/number-field` (its
markdown twin at `.../number-field.md`, "API reference" section), retrieved 2026-09-04. Column values
that are exact TypeScript unions are kept exact; multi-sentence descriptions keep every sentence.
Where the upstream default column shows `-`, that is upstream's own way of saying no default is
documented, not an omission by this file. This component has **no documented CSS variables** upstream.

### Root

Groups all parts of the number field and manages its state. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `name` | `string` | - | Identifies the field when a form is submitted. |
| `defaultValue` | `number` | - | The uncontrolled value of the field when it's initially rendered. To render a controlled number field, use the `value` prop instead. |
| `value` | `number \| null` | - | The raw numeric value of the field. |
| `onValueChange` | `(value: number \| null, eventDetails: NumberField.Root.ChangeEventDetails) => void` | - | Callback fired when the number value changes. The `eventDetails.reason` indicates what triggered the change: `'input-change'` for parseable typing or programmatic text updates; `'input-clear'` when the field becomes empty; `'input-blur'` when formatting (and clamping, if enabled) occurs on blur; `'input-paste'` for paste interactions; `'keyboard'` for arrow-key/Home/End stepping (typing digits uses `'input-change'`/`'input-clear'`); `'increment-press'` / `'decrement-press'` for button presses on the increment and decrement controls; `'wheel'` for wheel-based scrubbing; `'scrub'` for scrub area drags. |
| `onValueCommitted` | `(value: number \| null, eventDetails: NumberField.Root.CommitEventDetails) => void` | - | Callback function that is fired when the value is committed. It runs later than `onValueChange`, when: the input is blurred after typing a value; the pointer is released after scrubbing or pressing the increment/decrement buttons. It runs simultaneously with `onValueChange` when interacting with the keyboard or the mouse wheel. **Warning**: this is a generic event, not a change event. |
| `allowOutOfRange` | `boolean` | `false` | When true, direct text entry may be outside the `min`/`max` range without clamping, so native range underflow/overflow validation can occur. Step-based interactions (keyboard arrows, buttons, wheel, scrub) still clamp. |
| `form` | `string` | - | Identifies the form that owns the hidden input. Useful when the number field is rendered outside the form. |
| `locale` | `Intl.LocalesArgument` | - | The locale of the input element. Defaults to the user's runtime locale. |
| `snapOnStep` | `boolean` | `false` | Whether the value should snap to the nearest step when incrementing or decrementing. |
| `step` | `number \| 'any'` | `1` | Amount to increment and decrement with the buttons and arrow keys, or to scrub with pointer movement in the scrub area. To always enable step validation on form submission, specify the `min` prop explicitly in conjunction with this prop. Specify `step="any"` to always disable step validation; interactive stepping then uses a base amount of `1`, while the alt and shift keys still step by `smallStep` and `largeStep`. |
| `smallStep` | `number` | `0.1` | The small step value of the input element when incrementing while the alt key is held. Snaps to multiples of this value when `snapOnStep` is enabled. |
| `largeStep` | `number` | `10` | The large step value of the input element when incrementing while the shift key is held. Snaps to multiples of this value when `snapOnStep` is enabled. |
| `min` | `number` | - | The minimum value of the input element. |
| `max` | `number` | - | The maximum value of the input element. |
| `allowWheelScrub` | `boolean` | `false` | Whether to allow the user to scrub the input value with the mouse wheel while focused and hovering over the input. |
| `format` | `Intl.NumberFormatOptions` | - | Options to format the input value. |
| `disabled` | `boolean` | `false` | Whether the component should ignore user interaction. |
| `readOnly` | `boolean` | `false` | Whether the user should be unable to change the field value. |
| `required` | `boolean` | `false` | Whether the user must enter a value before submitting a form. |
| `inputRef` | `React.Ref<HTMLInputElement>` | - | A ref to access the hidden input element. |
| `id` | `string` | - | The id of the input element. |
| `className` | `string \| ((state: NumberField.Root.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.Root.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: NumberField.Root.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Root data attributes**: `data-disabled` (present when the number field is disabled) ·
`data-readonly` (present when the number field is readonly) · `data-required` (present when the
number field is required) · `data-valid` (present when the number field is in a valid state, when
wrapped in `Field.Root`) · `data-invalid` (present when the number field is in an invalid state, when
wrapped in `Field.Root`) · `data-dirty` (present when the number field's value has changed, when
wrapped in `Field.Root`) · `data-touched` (present when the number field has been touched, when
wrapped in `Field.Root`) · `data-filled` (present when the number field is filled, when wrapped in
`Field.Root`) · `data-focused` (present when the number field is focused, when wrapped in
`Field.Root`) · `data-scrubbing` (present while scrubbing).

Every other part below (`Input`, `Group`, `ScrubArea`, `ScrubAreaCursor`, `Decrement`, `Increment`)
documents the exact same 10 data attributes as Root upstream — repeated per part in the tables below
because that is how the upstream page lists them, not merged, so nothing in the per-part attribute
list is silently assumed from Root.

**Root.State** (all fields, exactly as documented):

```typescript
type NumberFieldRootState = {
  /** The raw numeric value of the field. */
  value: number | null;
  /** The formatted string value presented in the input element. */
  inputValue: string;
  /** Whether the user must enter a value before submitting a form. */
  required: boolean;
  /** Whether the component should ignore user interaction. */
  disabled: boolean;
  /** Whether the user should be unable to change the field value. */
  readOnly: boolean;
  /** Whether the user is currently scrubbing the field. */
  scrubbing: boolean;
  /** Whether the field has been touched. */
  touched: boolean;
  /** Whether the field value has changed from its initial value. */
  dirty: boolean;
  /** Whether the field is valid. */
  valid: boolean | null;
  /** Whether the field has a value. */
  filled: boolean;
  /** Whether the field is focused. */
  focused: boolean;
};
```

**Root.ChangeEventReason**: `'input-change' | 'input-clear' | 'input-blur' | 'input-paste' | 'keyboard' | 'increment-press' | 'decrement-press' | 'wheel' | 'scrub' | 'none'`.

**Root.CommitEventReason**: `'input-blur' | 'input-clear' | 'keyboard' | 'increment-press' | 'decrement-press' | 'wheel' | 'scrub' | 'none'`.

### Input

The native input control in the number field. Renders an `<input>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `aria-roledescription` | `string` | `'Number field'` | A user-friendly description of the input's role for assistive tech. This is a role description, not an accessible name — use `Field.Label` or `aria-label` to name the control. |
| `className` | `string \| ((state: NumberField.Input.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.Input.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: React.DetailedHTMLProps<React.InputHTMLAttributes<HTMLInputElement>, HTMLInputElement>, state: NumberField.Input.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Input data attributes**: same 10 as Root — `data-disabled`, `data-readonly`, `data-required`,
`data-valid`, `data-invalid`, `data-dirty`, `data-touched`, `data-filled`, `data-focused`,
`data-scrubbing`.

### Group

Groups the input with the increment and decrement buttons. Renders a `<div>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: NumberField.Group.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.Group.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: NumberField.Group.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Group data attributes**: same 10 as Root.

### ScrubArea

An interactive area where the user can click and drag to change the field value. Renders a `<span>`
element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `direction` | `'horizontal' \| 'vertical'` | `'horizontal'` | Cursor movement direction in the scrub area. |
| `pixelSensitivity` | `number` | `2` | Determines how many pixels the cursor must move before the value changes. A higher value will make scrubbing less sensitive. |
| `teleportDistance` | `number` | - | If specified, determines the distance that the cursor may move from the center of the scrub area before it will loop back around. |
| `className` | `string \| ((state: NumberField.ScrubArea.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.ScrubArea.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: NumberField.ScrubArea.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**ScrubArea data attributes**: same 10 as Root.

### ScrubAreaCursor

A custom element to display instead of the native cursor while using the scrub area. Renders a
`<span>` element. Upstream note: "This component uses the [Pointer Lock
API](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API), which may prompt the browser
to display a related notification. It is disabled in Safari to avoid a layout shift that this
notification causes there."

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string \| ((state: NumberField.ScrubAreaCursor.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.ScrubAreaCursor.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: NumberField.ScrubAreaCursor.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**ScrubAreaCursor data attributes**: same 10 as Root.

### Decrement

A stepper button that decreases the field value when clicked. Renders a `<button>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `nativeButton` | `boolean` | `true` | Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `false` if the rendered element is not a button (for example, `<div>`). |
| `className` | `string \| ((state: NumberField.Decrement.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.Decrement.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: NumberField.Decrement.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Decrement data attributes**: same 10 as Root.

### Increment

A stepper button that increases the field value when clicked. Renders a `<button>` element.

| Prop | Type | Default | Description |
|---|---|---|---|
| `nativeButton` | `boolean` | `true` | Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `false` if the rendered element is not a button (for example, `<div>`). |
| `className` | `string \| ((state: NumberField.Increment.State) => string \| undefined)` | - | CSS class applied to the element, or a function that returns a class based on the component's state. |
| `style` | `React.CSSProperties \| ((state: NumberField.Increment.State) => React.CSSProperties \| undefined)` | - | Style applied to the element, or a function that returns a style object based on the component's state. |
| `render` | `ReactElement \| ((props: HTMLProps, state: NumberField.Increment.State) => ReactElement)` | - | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render. |

**Increment data attributes**: same 10 as Root.

### External types referenced above

```typescript
type Direction = -1 | 1;
```

### ReUI additions

These props appear in ReUI's own example code (`@/components/reui/number-field`) on the reui.io page
but are **not** part of the Base UI `NumberField` API reference above. They are attested only by usage
in example code, with no upstream type or default:

- `size` (on `NumberField`) — seen with `"sm"` and `"lg"` values in examples; no upstream enum,
  default, or full value list documented. A third, unlabelled default size is implied but never named.
- `label` (on `NumberFieldScrubArea`) — seen as a plain string in examples (`"Amount"`, `"Small"`,
  `"Large"`, `"Quantity"`); not part of the Base UI `ScrubArea` prop table above.
- `variant` — not observed in any example read for this file. Listed in the task's earlier findings
  as a ReUI addition; this pass found no occurrence of it in the mirrored example code, so it is
  reported here as unconfirmed rather than dropped silently.

`defaultValue`, `min`, and `max` all exist on `NumberField.Root` in the Base UI table above — they are
not ReUI additions. `className` on any part is the native Base UI `className` prop documented per-part
above, also not a ReUI addition.
## Usage

```tsx
<NumberField defaultValue={0}>
  <NumberFieldScrubArea label="Quantity" />
  <NumberFieldGroup>
    <NumberFieldDecrement />
    <NumberFieldInput />
    <NumberFieldIncrement />
  </NumberFieldGroup>
</NumberField>
```

## Examples (3 total)

### Size

```tsx
import {
  NumberField,
  NumberFieldDecrement,
  NumberFieldGroup,
  NumberFieldIncrement,
  NumberFieldInput,
  NumberFieldScrubArea,
} from "@/components/reui/number-field"

export function Pattern() {
  return (
    <div className="w-full max-w-48">
      <NumberField defaultValue={5} min={0} max={100}>
        <NumberFieldScrubArea label="Amount" />
        <NumberFieldGroup>
          <NumberFieldDecrement />
          <NumberFieldInput />
          <NumberFieldIncrement />
        </NumberFieldGroup>
      </NumberField>
    </div>
  )
}
```

`size="sm"` and `size="lg"` variants are shown identically, with `<NumberField defaultValue={5} min={0} max={100} size="sm">`
and `size="lg"` respectively, and matching `label="Small"` / `label="Large"` on `NumberFieldScrubArea`.

### With Action Buttons

Same composition as Size, no distinguishing props beyond the base example — the upstream title
implies a variant but the captured code block for this section is identical in structure to the Size
example.

### With Extended Message

```tsx
import {
  NumberField,
  NumberFieldDecrement,
  NumberFieldGroup,
  NumberFieldIncrement,
  NumberFieldInput,
  NumberFieldScrubArea,
} from "@/components/reui/number-field"

export function Pattern() {
  return (
    <div className="w-full max-w-48">
      <NumberField defaultValue={5} min={0} max={100}>
        <NumberFieldScrubArea label="Amount" />
        <NumberFieldGroup>
          <NumberFieldInput className="text-left" />
          <NumberFieldDecrement className="rounded-none!" />
          <NumberFieldIncrement />
        </NumberFieldGroup>
      </NumberField>
    </div>
  )
}
```

## Base UI vs Radix UI

The Base UI and Radix UI pages are textually identical apart from the "Free Components" marketing
sentence ("Base UI primitives from `@base-ui/react`" vs. "the Radix UI implementation with accessible
primitives from the Radix stack"). Import path, installation command, and all three example bodies are
unchanged between builds.

**The "API Reference" link is also identical between builds**: on both `docs/components/base/number-field`
and `docs/components/radix/number-field`, the badge points at
`https://base-ui.com/react/components/number-field#api-reference`. Radix UI Primitives (radix-ui.com)
has no `number-field` component to link to — see the [API Reference](#api-reference) section above.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI.

## Source

- reui.io, Base UI build: `docs/components/base/number-field` — mirror captured 2026-09-04.
- reui.io, Radix UI build: `docs/components/radix/number-field` — mirror captured 2026-09-04. Its own
  "API Reference" link resolves to the same Base UI URL as the Base UI build (verified 2026-09-04).
- Primitive library for the API Reference section (both builds): Base UI,
  [`https://base-ui.com/react/components/number-field`](https://base-ui.com/react/components/number-field)
  (markdown twin `.../number-field.md`, "API reference" section) — retrieved 2026-09-04.
- Checked and found to have no counterpart: Radix UI Primitives component index at
  [`https://www.radix-ui.com/primitives/docs/overview/introduction`](https://www.radix-ui.com/primitives/docs/overview/introduction)
  lists 29 components, none named `number-field` — checked 2026-09-04.
