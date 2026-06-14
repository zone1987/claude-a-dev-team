# Toggle — Examples

## toggle-demo.tsx

```tsx
import { BookmarkIcon } from "lucide-react"

import { Toggle } from "@/registry/new-york-v4/ui/toggle"

export default function ToggleDemo() {
  return (
    <Toggle
      aria-label="Toggle bookmark"
      size="sm"
      variant="outline"
      className="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-blue-500 data-[state=on]:*:[svg]:stroke-blue-500"
    >
      <BookmarkIcon />
      Bookmark
    </Toggle>
  )
}
```

## toggle-outline.tsx

```tsx
import { Italic } from "lucide-react"

import { Toggle } from "@/registry/new-york-v4/ui/toggle"

export default function ToggleOutline() {
  return (
    <Toggle variant="outline" aria-label="Toggle italic">
      <Italic />
    </Toggle>
  )
}
```

## toggle-with-text.tsx

```tsx
import { Italic } from "lucide-react"

import { Toggle } from "@/registry/new-york-v4/ui/toggle"

export default function ToggleWithText() {
  return (
    <Toggle aria-label="Toggle italic">
      <Italic />
      Italic
    </Toggle>
  )
}
```

## toggle-sm.tsx

```tsx
import { Italic } from "lucide-react"

import { Toggle } from "@/registry/new-york-v4/ui/toggle"

export default function ToggleSm() {
  return (
    <Toggle size="sm" aria-label="Toggle italic">
      <Italic />
    </Toggle>
  )
}
```

## toggle-lg.tsx

```tsx
import { Italic } from "lucide-react"

import { Toggle } from "@/registry/new-york-v4/ui/toggle"

export default function ToggleLg() {
  return (
    <Toggle size="lg" aria-label="Toggle italic">
      <Italic />
    </Toggle>
  )
}
```

## toggle-disabled.tsx

```tsx
import { Underline } from "lucide-react"

import { Toggle } from "@/registry/new-york-v4/ui/toggle"

export default function ToggleDisabled() {
  return (
    <Toggle aria-label="Toggle italic" disabled>
      <Underline className="h-4 w-4" />
    </Toggle>
  )
}
```
