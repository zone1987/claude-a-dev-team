# Progress — Examples

## Demo

Animated progress bar that transitions from 13% to 66% on mount.

```tsx
"use client"

import * as React from "react"
import { Progress } from "@/components/ui/progress"

export default function ProgressDemo() {
  const [progress, setProgress] = React.useState(13)

  React.useEffect(() => {
    const timer = setTimeout(() => setProgress(66), 500)
    return () => clearTimeout(timer)
  }, [])

  return <Progress value={progress} className="w-[60%]" />
}
```

## Static Value

Simple progress bar at a fixed value.

```tsx
import { Progress } from "@/components/ui/progress"

export default function ProgressStatic() {
  return <Progress value={40} className="w-full max-w-sm" />
}
```

## With Label (Base UI variant)

Progress bar with a text label and percentage value using Base UI's extended sub-components.

```tsx
import {
  Progress,
  ProgressLabel,
  ProgressValue,
} from "@/components/ui/progress"

export default function ProgressLabel() {
  return (
    <Progress value={56} className="w-full max-w-sm">
      <ProgressLabel>Upload progress</ProgressLabel>
      <ProgressValue />
    </Progress>
  )
}
```

## Controlled (slider-driven)

A progress bar value controlled by a slider input.

```tsx
"use client"

import { useState } from "react"
import { Progress } from "@/components/ui/progress"
import { Slider } from "@/components/ui/slider"

export default function ProgressControlled() {
  const [value, setValue] = useState([33])

  return (
    <div className="flex w-full max-w-sm flex-col gap-4">
      <Progress value={value[0]} />
      <Slider
        value={value}
        onValueChange={setValue}
        min={0}
        max={100}
        step={1}
      />
    </div>
  )
}
```

---
Source: `registry/new-york-v4/examples/progress-demo.tsx`
