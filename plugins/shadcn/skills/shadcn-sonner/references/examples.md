# Sonner — Examples

## Demo (basic toast with description and action)

`registry/new-york-v4/examples/sonner-demo.tsx`

```tsx
"use client"

import { toast } from "sonner"

import { Button } from "@/registry/new-york-v4/ui/button"

export default function SonnerDemo() {
  return (
    <Button
      variant="outline"
      onClick={() =>
        toast("Event has been created", {
          description: "Sunday, December 03, 2023 at 9:00 AM",
          action: {
            label: "Undo",
            onClick: () => console.log("Undo"),
          },
        })
      }
    >
      Show Toast
    </Button>
  )
}
```

## Types (all toast variants)

`registry/new-york-v4/examples/sonner-types.tsx`

```tsx
"use client"

import { toast } from "sonner"

import { Button } from "@/registry/new-york-v4/ui/button"

export default function SonnerTypes() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button variant="outline" onClick={() => toast("Event has been created")}>
        Default
      </Button>
      <Button
        variant="outline"
        onClick={() => toast.success("Event has been created")}
      >
        Success
      </Button>
      <Button
        variant="outline"
        onClick={() =>
          toast.info("Be at the area 10 minutes before the event time")
        }
      >
        Info
      </Button>
      <Button
        variant="outline"
        onClick={() =>
          toast.warning("Event start time cannot be earlier than 8am")
        }
      >
        Warning
      </Button>
      <Button
        variant="outline"
        onClick={() => toast.error("Event has not been created")}
      >
        Error
      </Button>
      <Button
        variant="outline"
        onClick={() => {
          toast.promise<{ name: string }>(
            () =>
              new Promise((resolve) =>
                setTimeout(() => resolve({ name: "Event" }), 2000)
              ),
            {
              loading: "Loading...",
              success: (data) => `${data.name} has been created`,
              error: "Error",
            }
          )
        }}
      >
        Promise
      </Button>
    </div>
  )
}
```

## Source files

- `registry/new-york-v4/examples/sonner-demo.tsx`
- `registry/new-york-v4/examples/sonner-types.tsx`
