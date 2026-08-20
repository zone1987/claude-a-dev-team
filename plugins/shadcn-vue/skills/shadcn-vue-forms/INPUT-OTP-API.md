# InputOTP — API

Basis-Dokumentation: https://vue-input-otp.vercel.app/

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `InputOTP` | Root-Wrapper (OTPInput von vue-input-otp) |
| `InputOTPGroup` | Gruppiert zusammenhaengende Slots |
| `InputOTPSlot` | Einzelne Eingabezelle (zeigt Zeichen + Caret) |
| `InputOTPSeparator` | Trenner zwischen Gruppen (Standard: MinusIcon) |

## InputOTP (Root)

Leitet alle `OTPInputProps` von vue-input-otp weiter.

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `maxlength` | `number` | - | Maximale Zeichen (Pflicht) |
| `modelValue` / `v-model` | `string` | - | Kontrollierter Wert |
| `pattern` | `string \| RegExp` | - | Erlaubte Zeichen (z.B. `REGEXP_ONLY_DIGITS_AND_CHARS`) |
| `disabled` | `boolean` | `false` | Deaktiviert alle Slots |
| `class` | `string` | - | CSS-Klassen fuer den Container |

| Emit | Beschreibung |
|---|---|
| `update:modelValue` | Wert geaendert |
| `complete` | Alle Slots ausgefuellt |

## InputOTPSlot

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `index` | `number` | - | Position im OTP (0-basiert, Pflicht) |
| `class` | `string` | - | Zusaetzliche CSS-Klassen |
| `aria-invalid` | `boolean` | - | Fehler-Styling aktivieren |

Das Slot zeigt automatisch `slot?.char` aus dem OTP-Context und rendert einen blinkenden Caret wenn `slot?.hasFakeCaret` aktiv ist.

## Pattern-Konstanten (vue-input-otp)

```ts
import { REGEXP_ONLY_DIGITS, REGEXP_ONLY_CHARS, REGEXP_ONLY_DIGITS_AND_CHARS } from 'vue-input-otp'
```

| Konstante | Muster |
|---|---|
| `REGEXP_ONLY_DIGITS` | Nur Ziffern (0-9) |
| `REGEXP_ONLY_CHARS` | Nur Buchstaben (A-Z) |
| `REGEXP_ONLY_DIGITS_AND_CHARS` | Ziffern und Buchstaben |
