# Phone Input

Custom Shadcn Phone Input for React and Tailwind CSS. A phone number input component with country
selection and validation.

Free component — no licence key required.

Upstream note: "We used the [react-phone-number-input] library to create this component."

This is a thin upstream page: installation, one usage line, one example (Size), and a compact API
Reference. Nothing further is padded in below.

## Installation

```
pnpm dlx shadcn@latest add @reui/phone-input
```

## Import

```tsx
import { PhoneInput } from "@/components/reui/phone-input"
```

## Usage

```tsx
<PhoneInput
  placeholder="Enter phone number"
  defaultCountry="US"
  value={value}
  onChange={setValue}
/>
```

## Examples (1 total)

### Size

```tsx
import { PhoneInput } from "@/components/reui/phone-input"

export function Pattern() {
  return (
    <PhoneInput
      variant="sm"
      placeholder="Enter phone number"
      defaultCountry="NL"
      value="+31612345678"
    />
  )
}
```

## API Reference

### PhoneInput

The main component for entering phone numbers with country selection.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | `-` | The current phone number value in E.164 format. |
| `onChange` | `(value: string) => void` | `-` | Callback fired when the value changes. |
| `variant` | `"sm" \| "default" \| "lg"` | `"default"` | The vertical size of the input and country selector. |
| `popupClassName` | `string` | `-` | Additional CSS classes for the country selection dropdown. |
| `defaultCountry` | `Country` | `-` | The default country selected if no value is provided. |
| `placeholder` | `string` | `-` | Placeholder text for the phone number input. |
| `className` | `string` | `-` | Additional CSS classes for the root container. |
| `disabled` | `boolean` | `false` | Whether the input and country selector are disabled. |

`Country` is not defined on this page; it is the country-code type from `react-phone-number-input`.

### External Props

This component also accepts all props from the `react-phone-number-input` library (linked upstream,
not itself enumerated on this page).

```tsx
import { PhoneInput } from "@/components/reui/phone-input"

export function Pattern() {
  return <PhoneInput placeholder="Enter phone number" />
}
```

## Base UI vs Radix UI

The Base UI and Radix UI pages are textually identical apart from the "Free Components" marketing
sentence. Import path (`@/components/reui/phone-input`), installation command, the Size example, and
the full API Reference table are unchanged between builds.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI.

## Source

- Base UI: `docs/components/base/phone-input` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/phone-input` — mirror captured 2026-09-04.
