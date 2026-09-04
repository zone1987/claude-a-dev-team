# Rating

Custom Shadcn Rating for React and Tailwind CSS. A customizable star rating component that supports
read-only display and interactive input modes.

Free component — no licence key required.

This is a thin upstream page: installation, one usage line, four examples, and a compact API
Reference. Nothing further is padded in below.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (4 total)](#examples-4-total)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/rating
```

## Import

```tsx
import { Rating } from "@/components/reui/rating"
```

## Usage

```tsx
<Rating rating={4.5} showValue editable />
```

## Examples (4 total)

### Decimal

```tsx
import { Rating } from "@/components/reui/rating"

export function Pattern() {
  return <Rating rating={3.5} />
}
```

### Show Value

```tsx
import { Rating } from "@/components/reui/rating"

export function Pattern() {
  return <Rating rating={4.5} showValue={true} />
}
```

### Editable

```tsx
"use client"

import { useState } from "react"
import { Rating } from "@/components/reui/rating"
import { toast } from "sonner"

export function Pattern() {
  const [productRating, setProductRating] = useState(0)

  const handleRatingChange = (rating: number) => {
    setProductRating(rating)
    toast.success("Rated {rating} out of 5", {
      description: `Rated ${rating} out of 5`,
    })
  }

  return (
    <div className="space-y-8">
      <Rating
        rating={productRating}
        editable={true}
        onRatingChange={handleRatingChange}
        showValue={true}
      />
    </div>
  )
}
```

### Size

```tsx
import { Rating } from "@/components/reui/rating"

export function Pattern() {
  return (
    <div className="flex flex-col items-center gap-4">
      <Rating rating={4} size="sm" />
      <Rating rating={4} />
      <Rating rating={4} size="lg" />
    </div>
  )
}
```

## API Reference

### Rating

The main component for displaying and editing star ratings.

| Prop | Type | Default | Description |
|---|---|---|---|
| `rating` | `number` | `-` | Required. The current rating value. Supports decimal values for partial stars. |
| `maxRating` | `number` | `5` | Total number of stars to display. |
| `size` | `"sm" \| "default" \| "lg"` | `"md"` | The size of the stars and spacing. Note: upstream default literal is `"md"`, though the enum itself lists `"default"` rather than `"md"` — stated exactly as the page has it, not reconciled. |
| `showValue` | `boolean` | `false` | Whether to show the numeric rating value next to the stars. |
| `editable` | `boolean` | `false` | Whether the rating can be changed by clicking on stars. |
| `onRatingChange` | `(rating: number) => void` | `-` | Callback fired when a star is clicked (if `editable` is true). |
| `starClassName` | `string` | `-` | Additional CSS classes for the numeric value container. |
| `className` | `string` | `-` | Additional CSS classes for the root container. |

```tsx
import { Rating } from "@/components/reui/rating"

export function Pattern() {
  return <Rating rating={4} />
}
```

## Base UI vs Radix UI

The Base UI and Radix UI pages are textually identical apart from the "Free Components" marketing
sentence. Import path (`@/components/reui/rating`), installation command, all four examples, and the
full API Reference table are unchanged between builds.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI.

## Source

- Base UI: `docs/components/base/rating` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/rating` — mirror captured 2026-09-04.
