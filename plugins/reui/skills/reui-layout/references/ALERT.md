# Alert

Custom Shadcn Alert for React and Tailwind CSS. Displays a callout for user attention, such as a
success message, warning, or error.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (10 total)](#examples-10-total)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/alert
```

## Import

```tsx
import {
  Alert,
  AlertAction,
  AlertDescription,
  AlertTitle,
} from "@/components/reui/alert"
```

## Usage

```tsx
<Alert>
  <ShieldCheckIcon />
  <AlertTitle>Security Update</AlertTitle>
  <AlertDescription>Update your password and enable 2FA.</AlertDescription>
  <AlertAction>
    <Button variant="outline" size="xs">
      Dismiss
    </Button>
    <Button size="xs">Update</Button>
  </AlertAction>
</Alert>
```

## Examples (10 total)

### With Icon

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { CircleCheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert>
      <CircleCheckIcon />
      <AlertTitle>Alert!</AlertTitle>
      <AlertDescription>This is an alert with icon, title and description.</AlertDescription>
    </Alert>
  )
}
```

### With Action Buttons

```tsx
import { Alert, AlertAction, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { Button } from "@/components/ui/button"
import { ShieldCheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert>
      <ShieldCheckIcon />
      <AlertTitle>Security Update</AlertTitle>
      <AlertDescription>Update your password and enable 2FA.</AlertDescription>
      <AlertAction>
        <Button variant="outline" size="xs">Dismiss</Button>
        <Button size="xs">Update</Button>
      </AlertAction>
    </Alert>
  )
}
```

### With Extended Message

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { CircleAlertIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert variant="destructive">
      <CircleAlertIcon />
      <AlertTitle>Payment Failed</AlertTitle>
      <AlertDescription>
        <p>Please check your payment details:</p>
        <ul className="mt-1 list-inside list-disc space-y-0.5 text-sm">
          <li>Card number and expiry</li>
          <li>Billing address</li>
          <li>Available funds</li>
        </ul>
      </AlertDescription>
    </Alert>
  )
}
```

### With Title and Action Buttons

```tsx
import { Alert, AlertAction, AlertTitle } from "@/components/reui/alert"
import { Button } from "@/components/ui/button"
import { ShieldCheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert>
      <ShieldCheckIcon />
      <AlertTitle>Update your password and enable 2FA.</AlertTitle>
      <AlertAction>
        <Button variant="outline" size="xs">Dismiss</Button>
        <Button size="xs">Update</Button>
      </AlertAction>
    </Alert>
  )
}
```

Note: this example uses `AlertTitle` without an `AlertDescription` — the title alone carries the
message.

### With Description and Action Buttons

```tsx
import { Alert, AlertAction, AlertDescription } from "@/components/reui/alert"
import { Button } from "@/components/ui/button"
import { ShieldCheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert>
      <ShieldCheckIcon />
      <AlertDescription>Update your password and enable 2FA.</AlertDescription>
      <AlertAction>
        <Button variant="outline" size="xs">Dismiss</Button>
        <Button size="xs">Update</Button>
      </AlertAction>
    </Alert>
  )
}
```

Note: the mirror image of "With Title and Action Buttons" — `AlertDescription` without `AlertTitle`.

### Info Alert

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { CircleAlertIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert variant="info">
      <CircleAlertIcon />
      <AlertTitle>Info! Something important</AlertTitle>
      <AlertDescription>This is an important message. Please read it carefully.</AlertDescription>
    </Alert>
  )
}
```

### Success Alert

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { CircleCheckIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert variant="success">
      <CircleCheckIcon />
      <AlertTitle>Success! All good</AlertTitle>
      <AlertDescription>Everything is working as expected. You can continue with your task.</AlertDescription>
    </Alert>
  )
}
```

### Warning Alert

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { AlertTriangleIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert variant="warning">
      <AlertTriangleIcon />
      <AlertTitle>Warning! Something is wrong</AlertTitle>
      <AlertDescription>Please check your settings. If the problem persists, contact support.</AlertDescription>
    </Alert>
  )
}
```

### Destructive Alert

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { CircleAlertIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert variant="destructive">
      <CircleAlertIcon />
      <AlertTitle>Error! Something went wrong</AlertTitle>
      <AlertDescription>Please try again. If the problem persists, contact support.</AlertDescription>
    </Alert>
  )
}
```

### Invert Alert

```tsx
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { CircleAlertIcon } from "lucide-react"

export function Pattern() {
  return (
    <Alert variant="invert">
      <CircleAlertIcon className="text-success" />
      <AlertTitle>Notification! All good</AlertTitle>
      <AlertDescription>This is a notification alert with a title and description.</AlertDescription>
    </Alert>
  )
}
```

Note: the icon color is set explicitly with `text-success` here — `variant="invert"` itself does not
tint the icon, only the alert surface/text.

## API Reference

This component follows the same API design as the Alert component from shadcn/ui. The key
difference is that it uses extended color tokens — `--success`, `--info`, `--warning`, and
`--invert` — for alert variants instead of utility classes. This approach enables consistent,
reusable state variants across the project without relying on custom Tailwind color utilities.

```tsx
<Alert variant="success">
  <AlertTitle>Success</AlertTitle>
  <AlertDescription>This is a success alert</AlertDescription>
</Alert>
```

### Props

| Prop | Type |
|---|---|
| `variant` | `"default" \| "destructive" \| "info" \| "success" \| "warning" \| "invert"` |

The upstream Props table for Alert gives only `variant`'s type — no default, and no per-row
description beyond the sentence above the table. No default value is stated on this page for
`variant`; shadcn/ui convention is `"default"`, but that is not asserted here, so treat it as
unstated upstream.

### Variant-to-token map

| `variant` | Token used |
|---|---|
| `default` | shadcn/ui default (no extended token) |
| `destructive` | shadcn/ui `destructive` (no extended token) |
| `info` | `--info` / `--info-foreground` |
| `success` | `--success` / `--success-foreground` |
| `warning` | `--warning` / `--warning-foreground` |
| `invert` | `--invert` / `--invert-foreground` |

This page does not itself enumerate the light/dark values of `--success`, `--info`, `--warning`,
`--invert`, or their `-foreground` pairs — see `skills/reui-theming/references/TOKENS.md` for the
distilled light and dark values of these tokens (they are shared across Alert and Badge, and are
what makes both differ from plain shadcn/ui).

## Base UI vs Radix UI

Installation command and import path are unchanged between builds (`@reui/alert`,
`@/components/reui/alert`), and the Props table and variant-to-token map above are identical. The
only diffs found by full-file comparison are the "Free Components" marketing sentence (Base UI: "use
Base UI primitives and composable components"; Radix UI: "follow accessible roles from the Radix
stack") and markdown-rendering artifacts around the top usage snippet with no code difference.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI.

## Source

- Base UI: `docs/components/base/alert` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/alert` — mirror captured 2026-09-04.
