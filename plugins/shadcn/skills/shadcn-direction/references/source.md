# Direction — Full Source Code

## new-york-v4 (Radix UI)

```tsx
"use client"

import * as React from "react"
import { Direction } from "radix-ui"

function DirectionProvider({
  dir,
  direction,
  children,
}: React.ComponentProps<typeof Direction.DirectionProvider> & {
  direction?: React.ComponentProps<typeof Direction.DirectionProvider>["dir"]
}) {
  return (
    <Direction.DirectionProvider dir={direction ?? dir}>
      {children}
    </Direction.DirectionProvider>
  )
}

const useDirection = Direction.useDirection

export { DirectionProvider, useDirection }
```

## Base UI variant

```tsx
"use client"

export {
  DirectionProvider,
  useDirection,
} from "@base-ui/react/direction-provider"
```

The Base UI variant is a direct re-export — no wrapper component needed.

---

_Source: `apps/v4/registry/new-york-v4/ui/direction.tsx`, `apps/v4/registry/bases/base/ui/direction.tsx`_
