# Button Group — Examples

## Demo (email toolbar with nested groups)

```tsx
"use client"

import * as React from "react"
import {
  ArchiveIcon, ArrowLeftIcon, CalendarPlusIcon, ClockIcon,
  ListFilterIcon, MailCheckIcon, MoreHorizontalIcon, TagIcon, Trash2Icon,
} from "lucide-react"
import { Button } from "@/registry/new-york-v4/ui/button"
import { ButtonGroup } from "@/registry/new-york-v4/ui/button-group"
import { DropdownMenu, DropdownMenuContent, DropdownMenuGroup,
  DropdownMenuItem, DropdownMenuTrigger } from "@/registry/new-york-v4/ui/dropdown-menu"

export default function ButtonGroupDemo() {
  return (
    <ButtonGroup>
      <ButtonGroup className="hidden sm:flex">
        <Button variant="outline" size="icon" aria-label="Go Back">
          <ArrowLeftIcon />
        </Button>
      </ButtonGroup>
      <ButtonGroup>
        <Button variant="outline">Archive</Button>
        <Button variant="outline">Report</Button>
      </ButtonGroup>
      <ButtonGroup>
        <Button variant="outline">Snooze</Button>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" size="icon" aria-label="More Options">
              <MoreHorizontalIcon />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" className="w-52">
            <DropdownMenuGroup>
              <DropdownMenuItem><MailCheckIcon /> Mark as Read</DropdownMenuItem>
              <DropdownMenuItem><ArchiveIcon /> Archive</DropdownMenuItem>
            </DropdownMenuGroup>
          </DropdownMenuContent>
        </DropdownMenu>
      </ButtonGroup>
    </ButtonGroup>
  )
}
```

## Orientation (vertical)

```tsx
import { MinusIcon, PlusIcon } from "lucide-react"

<ButtonGroup orientation="vertical" aria-label="Media controls" className="h-fit">
  <Button variant="outline" size="icon"><PlusIcon /></Button>
  <Button variant="outline" size="icon"><MinusIcon /></Button>
</ButtonGroup>
```

## Separator (split button)

```tsx
import { ButtonGroup, ButtonGroupSeparator } from "@/components/ui/button-group"

<ButtonGroup>
  <Button variant="secondary">Button</Button>
  <ButtonGroupSeparator />
  <Button size="icon" variant="secondary">
    <PlusIcon />
  </Button>
</ButtonGroup>
```

## With input

```tsx
import { SearchIcon } from "lucide-react"
import { Input } from "@/components/ui/input"

<ButtonGroup>
  <Input placeholder="Search..." />
  <Button variant="outline" aria-label="Search">
    <SearchIcon />
  </Button>
</ButtonGroup>
```

## With dropdown (split button pattern)

```tsx
<ButtonGroup>
  <Button variant="outline">Follow</Button>
  <DropdownMenu>
    <DropdownMenuTrigger asChild>
      <Button variant="outline" className="pl-2!">
        <ChevronDownIcon />
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end">
      <DropdownMenuItem>Mute Conversation</DropdownMenuItem>
      <DropdownMenuItem>Block User</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</ButtonGroup>
```

## With select

```tsx
<ButtonGroup>
  <ButtonGroup>
    <Select value={currency} onValueChange={setCurrency}>
      <SelectTrigger className="font-mono">{currency}</SelectTrigger>
      <SelectContent className="min-w-24">
        {/* items */}
      </SelectContent>
    </Select>
    <Input placeholder="10.00" />
  </ButtonGroup>
  <ButtonGroup>
    <Button size="icon" variant="outline"><ArrowRightIcon /></Button>
  </ButtonGroup>
</ButtonGroup>
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-demo.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-orientation.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-separator.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-split.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-input.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-dropdown.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-select.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-size.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-nested.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-group-popover.tsx`
