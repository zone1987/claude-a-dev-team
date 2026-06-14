# InputOTP — API Reference

## Composition Tree

```text
InputOTP
├── InputOTPGroup
│   ├── InputOTPSlot (index=0)
│   ├── InputOTPSlot (index=1)
│   └── InputOTPSlot (index=2)
├── InputOTPSeparator
├── InputOTPGroup
│   ├── InputOTPSlot (index=3)
│   ├── InputOTPSlot (index=4)
│   └── InputOTPSlot (index=5)
├── InputOTPSeparator
└── InputOTPGroup
    ├── InputOTPSlot (index=6)
    └── InputOTPSlot (index=7)
```

## Basic Usage

```tsx
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"

<InputOTP maxLength={6}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
    <InputOTPSlot index={2} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={3} />
    <InputOTPSlot index={4} />
    <InputOTPSlot index={5} />
  </InputOTPGroup>
</InputOTP>
```

## Sub-component Props

### InputOTP

Wraps `OTPInput` from `input-otp`. Renders as an invisible input that manages all slot state.

| Prop                 | Type                          | Default | Description                                         |
| -------------------- | ----------------------------- | ------- | --------------------------------------------------- |
| `maxLength`          | `number`                      | –       | **Required.** Total number of character slots        |
| `value`              | `string`                      | –       | Controlled value                                    |
| `onChange`           | `(value: string) => void`     | –       | Called on value change                              |
| `pattern`            | `string \| RegExp`            | –       | Restricts allowed characters (see pattern constants) |
| `disabled`           | `boolean`                     | `false` | Disables all slots                                  |
| `containerClassName` | `string`                      | –       | CSS classes on the outer container div              |
| `className`          | `string`                      | –       | CSS classes on the hidden input element             |
| `onComplete`         | `(value: string) => void`     | –       | Called when all slots are filled                    |
| `autoFocus`          | `boolean`                     | `false` | Auto-focuses on mount                               |

### InputOTPGroup

Groups consecutive slots into a connected visual unit.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### InputOTPSlot

Renders a single character slot. Reads state from `OTPInputContext`.

| Prop        | Type     | Default | Description                                      |
| ----------- | -------- | ------- | ------------------------------------------------ |
| `index`     | `number` | –       | **Required.** 0-based position of this slot      |
| `className` | `string` | –       | Additional CSS classes                           |

States handled automatically:
- `data-active` — current cursor position
- `aria-invalid` — error state
- `hasFakeCaret` — animated blinking cursor when active and empty

### InputOTPSeparator

Visual separator between groups. Renders a `MinusIcon`.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |
| `children`  | `ReactNode` | `<MinusIcon />` | Custom separator content |

## Pattern Constants (from `input-otp`)

```tsx
import {
  REGEXP_ONLY_DIGITS,          // /^\d+$/
  REGEXP_ONLY_CHARS,           // /^[a-zA-Z]+$/
  REGEXP_ONLY_DIGITS_AND_CHARS, // /^[a-zA-Z0-9]+$/
} from "input-otp"
```

```tsx
<InputOTP maxLength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
  ...
</InputOTP>
```

## Error State

Add `aria-invalid` to `InputOTPSlot` components:

```tsx
<InputOTPGroup>
  <InputOTPSlot index={0} aria-invalid />
  <InputOTPSlot index={1} aria-invalid />
  <InputOTPSlot index={2} aria-invalid />
</InputOTPGroup>
```

---

_Source: `apps/v4/content/docs/components/base/input-otp.mdx`, `apps/v4/registry/new-york-v4/ui/input-otp.tsx`_
