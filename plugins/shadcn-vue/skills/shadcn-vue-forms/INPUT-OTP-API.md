# InputOTP — API

Base documentation: https://vue-input-otp.vercel.app/

## Sub-components

| Component | Description |
|---|---|
| `InputOTP` | Root wrapper (OTPInput from vue-input-otp) |
| `InputOTPGroup` | Groups related slots |
| `InputOTPSlot` | Single input cell (renders character + caret) |
| `InputOTPSeparator` | Separator between groups (default: MinusIcon) |

## InputOTP (root)

Forwards all `OTPInputProps` from vue-input-otp.

| Prop | Type | Default | Description |
|---|---|---|---|
| `maxlength` | `number` | - | Maximum characters (required) |
| `modelValue` / `v-model` | `string` | - | Controlled value |
| `pattern` | `string \| RegExp` | - | Allowed characters (e.g. `REGEXP_ONLY_DIGITS_AND_CHARS`) |
| `disabled` | `boolean` | `false` | Disables all slots |
| `class` | `string` | - | CSS classes for the container |

| Emit | Description |
|---|---|
| `update:modelValue` | Value changed |
| `complete` | All slots filled |

## InputOTPSlot

| Prop | Type | Default | Description |
|---|---|---|---|
| `index` | `number` | - | Position within the OTP (0-based, required) |
| `class` | `string` | - | Additional CSS classes |
| `aria-invalid` | `boolean` | - | Enable error styling |

The slot automatically renders `slot?.char` from the OTP context and shows a blinking caret when `slot?.hasFakeCaret` is active.

## Pattern constants (vue-input-otp)

```ts
import { REGEXP_ONLY_DIGITS, REGEXP_ONLY_CHARS, REGEXP_ONLY_DIGITS_AND_CHARS } from 'vue-input-otp'
```

| Constant | Pattern |
|---|---|
| `REGEXP_ONLY_DIGITS` | Digits only (0-9) |
| `REGEXP_ONLY_CHARS` | Letters only (A-Z) |
| `REGEXP_ONLY_DIGITS_AND_CHARS` | Digits and letters |
