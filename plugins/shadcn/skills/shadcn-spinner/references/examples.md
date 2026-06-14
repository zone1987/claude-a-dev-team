# Spinner — Examples

## Basic (standalone)

`registry/new-york-v4/examples/spinner-basic.tsx`

```tsx
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerBasic() {
  return (
    <div className="flex flex-col items-center justify-center gap-8">
      <Spinner />
    </div>
  )
}
```

## Demo (in item context)

`registry/new-york-v4/examples/spinner-demo.tsx`

```tsx
import {
  Item,
  ItemContent,
  ItemMedia,
  ItemTitle,
} from "@/registry/new-york-v4/ui/item"
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerDemo() {
  return (
    <div className="flex w-full max-w-xs flex-col gap-4 [--radius:1rem]">
      <Item variant="muted">
        <ItemMedia>
          <Spinner />
        </ItemMedia>
        <ItemContent>
          <ItemTitle className="line-clamp-1">Processing payment...</ItemTitle>
        </ItemContent>
        <ItemContent className="flex-none justify-end">
          <span className="text-sm tabular-nums">$100.00</span>
        </ItemContent>
      </Item>
    </div>
  )
}
```

## Size variants

`registry/new-york-v4/examples/spinner-size.tsx`

```tsx
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerSize() {
  return (
    <div className="flex items-center gap-6">
      <Spinner className="size-3" />
      <Spinner className="size-4" />
      <Spinner className="size-6" />
      <Spinner className="size-8" />
    </div>
  )
}
```

## In a Button (loading state)

`registry/new-york-v4/examples/spinner-button.tsx`

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerButton() {
  return (
    <div className="flex flex-col items-center gap-4">
      <Button disabled size="sm">
        <Spinner />
        Loading...
      </Button>
      <Button variant="outline" disabled size="sm">
        <Spinner />
        Please wait
      </Button>
      <Button variant="secondary" disabled size="sm">
        <Spinner />
        Processing
      </Button>
    </div>
  )
}
```

## In a Badge

`registry/new-york-v4/examples/spinner-badge.tsx`

```tsx
import { Badge } from "@/registry/new-york-v4/ui/badge"
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerBadge() {
  return (
    <div className="flex items-center gap-4 [--radius:1.2rem]">
      <Badge>
        <Spinner />
        Syncing
      </Badge>
      <Badge variant="secondary">
        <Spinner />
        Updating
      </Badge>
      <Badge variant="outline">
        <Spinner />
        Processing
      </Badge>
    </div>
  )
}
```

## Color variants

`registry/new-york-v4/examples/spinner-color.tsx`

```tsx
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerColor() {
  return (
    <div className="flex items-center gap-6">
      <Spinner className="size-6 text-red-500" />
      <Spinner className="size-6 text-green-500" />
      <Spinner className="size-6 text-blue-500" />
      <Spinner className="size-6 text-yellow-500" />
      <Spinner className="size-6 text-purple-500" />
    </div>
  )
}
```

## Custom icon

`registry/new-york-v4/examples/spinner-custom.tsx`

```tsx
import { LoaderIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <LoaderIcon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export default function SpinnerCustom() {
  return (
    <div className="flex items-center gap-4">
      <Spinner />
    </div>
  )
}
```

## In an Input Group

`registry/new-york-v4/examples/spinner-input-group.tsx`

```tsx
import { ArrowUpIcon } from "lucide-react"

import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupTextarea,
} from "@/registry/new-york-v4/ui/input-group"
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerInputGroup() {
  return (
    <div className="flex w-full max-w-md flex-col gap-4">
      <InputGroup>
        <InputGroupInput placeholder="Send a message..." disabled />
        <InputGroupAddon align="inline-end">
          <Spinner />
        </InputGroupAddon>
      </InputGroup>
      <InputGroup>
        <InputGroupTextarea placeholder="Send a message..." disabled />
        <InputGroupAddon align="block-end">
          <Spinner /> Validating...
          <InputGroupButton className="ml-auto" variant="default">
            <ArrowUpIcon />
            <span className="sr-only">Send</span>
          </InputGroupButton>
        </InputGroupAddon>
      </InputGroup>
    </div>
  )
}
```

## In an Empty state

`registry/new-york-v4/examples/spinner-empty.tsx`

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/registry/new-york-v4/ui/empty"
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerEmpty() {
  return (
    <Empty className="w-full">
      <EmptyHeader>
        <EmptyMedia variant="icon">
          <Spinner />
        </EmptyMedia>
        <EmptyTitle>Processing your request</EmptyTitle>
        <EmptyDescription>
          Please wait while we process your request. Do not refresh the page.
        </EmptyDescription>
      </EmptyHeader>
      <EmptyContent>
        <Button variant="outline" size="sm">
          Cancel
        </Button>
      </EmptyContent>
    </Empty>
  )
}
```

## In an Item with progress

`registry/new-york-v4/examples/spinner-item.tsx`

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemFooter,
  ItemMedia,
  ItemTitle,
} from "@/registry/new-york-v4/ui/item"
import { Progress } from "@/registry/new-york-v4/ui/progress"
import { Spinner } from "@/registry/new-york-v4/ui/spinner"

export default function SpinnerItem() {
  return (
    <div className="flex w-full max-w-md flex-col gap-4 [--radius:1rem]">
      <Item variant="outline">
        <ItemMedia variant="icon">
          <Spinner />
        </ItemMedia>
        <ItemContent>
          <ItemTitle>Downloading...</ItemTitle>
          <ItemDescription>129 MB / 1000 MB</ItemDescription>
        </ItemContent>
        <ItemActions className="hidden sm:flex">
          <Button variant="outline" size="sm">
            Cancel
          </Button>
        </ItemActions>
        <ItemFooter>
          <Progress value={75} />
        </ItemFooter>
      </Item>
    </div>
  )
}
```

## Source files

- `registry/new-york-v4/examples/spinner-basic.tsx`
- `registry/new-york-v4/examples/spinner-demo.tsx`
- `registry/new-york-v4/examples/spinner-size.tsx`
- `registry/new-york-v4/examples/spinner-button.tsx`
- `registry/new-york-v4/examples/spinner-badge.tsx`
- `registry/new-york-v4/examples/spinner-color.tsx`
- `registry/new-york-v4/examples/spinner-custom.tsx`
- `registry/new-york-v4/examples/spinner-input-group.tsx`
- `registry/new-york-v4/examples/spinner-empty.tsx`
- `registry/new-york-v4/examples/spinner-item.tsx`
