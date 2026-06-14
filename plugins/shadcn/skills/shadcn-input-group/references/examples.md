# InputGroup — Examples

## Example 1 — Demo (Multi-pattern Showcase)

Search with result count, URL with tooltip button, chat textarea with controls.

```tsx
import { IconCheck, IconInfoCircle, IconPlus } from "@tabler/icons-react"
import { ArrowUpIcon, Search } from "lucide-react"

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/registry/new-york-v4/ui/input-group"
import { Separator } from "@/registry/new-york-v4/ui/separator"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/registry/new-york-v4/ui/tooltip"

export default function InputGroupDemo() {
  return (
    <div className="grid w-full max-w-sm gap-6">
      {/* Search with result count */}
      <InputGroup>
        <InputGroupInput placeholder="Search..." />
        <InputGroupAddon>
          <Search />
        </InputGroupAddon>
        <InputGroupAddon align="inline-end">12 results</InputGroupAddon>
      </InputGroup>

      {/* URL input with tooltip */}
      <InputGroup>
        <InputGroupInput placeholder="example.com" className="pl-1!" />
        <InputGroupAddon>
          <InputGroupText>https://</InputGroupText>
        </InputGroupAddon>
        <InputGroupAddon align="inline-end">
          <Tooltip>
            <TooltipTrigger asChild>
              <InputGroupButton className="rounded-full" size="icon-xs">
                <IconInfoCircle />
              </InputGroupButton>
            </TooltipTrigger>
            <TooltipContent>This is content in a tooltip.</TooltipContent>
          </Tooltip>
        </InputGroupAddon>
      </InputGroup>

      {/* Chat textarea with block-end toolbar */}
      <InputGroup>
        <InputGroupTextarea placeholder="Ask, Search or Chat..." />
        <InputGroupAddon align="block-end">
          <InputGroupButton
            variant="outline"
            className="rounded-full"
            size="icon-xs"
          >
            <IconPlus />
          </InputGroupButton>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <InputGroupButton variant="ghost">Auto</InputGroupButton>
            </DropdownMenuTrigger>
            <DropdownMenuContent
              side="top"
              align="start"
              className="[--radius:0.95rem]"
            >
              <DropdownMenuItem>Auto</DropdownMenuItem>
              <DropdownMenuItem>Agent</DropdownMenuItem>
              <DropdownMenuItem>Manual</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <InputGroupText className="ml-auto">52% used</InputGroupText>
          <Separator orientation="vertical" className="h-4!" />
          <InputGroupButton
            variant="default"
            className="rounded-full"
            size="icon-xs"
            disabled
          >
            <ArrowUpIcon />
            <span className="sr-only">Send</span>
          </InputGroupButton>
        </InputGroupAddon>
      </InputGroup>

      {/* Verified badge */}
      <InputGroup>
        <InputGroupInput placeholder="@shadcn" />
        <InputGroupAddon align="inline-end">
          <div className="flex size-4 items-center justify-center rounded-full bg-primary text-primary-foreground">
            <IconCheck className="size-3" />
          </div>
        </InputGroupAddon>
      </InputGroup>
    </div>
  )
}
```

## Example 2 — Simple Icon Start

```tsx
import { SearchIcon } from "lucide-react"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
} from "@/components/ui/input-group"

<InputGroup>
  <InputGroupInput placeholder="Search..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

## Example 3 — Text Prefix + Icon End

```tsx
import { InfoIcon } from "lucide-react"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
} from "@/components/ui/input-group"

<InputGroup>
  <InputGroupInput placeholder="yourdomain.com" className="pl-1!" />
  <InputGroupAddon>
    <InputGroupText>https://</InputGroupText>
  </InputGroupAddon>
  <InputGroupAddon align="inline-end">
    <InputGroupButton size="icon-xs">
      <InfoIcon />
    </InputGroupButton>
  </InputGroupAddon>
</InputGroup>
```

## Example 4 — Textarea with Block-end Submit Button

```tsx
import { ArrowUpIcon } from "lucide-react"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupTextarea,
} from "@/components/ui/input-group"

<InputGroup>
  <InputGroupTextarea placeholder="Type a message..." />
  <InputGroupAddon align="block-end">
    <InputGroupButton
      variant="default"
      size="icon-xs"
      className="ml-auto rounded-full"
    >
      <ArrowUpIcon />
      <span className="sr-only">Send</span>
    </InputGroupButton>
  </InputGroupAddon>
</InputGroup>
```

---

_Source: `apps/v4/registry/new-york-v4/examples/input-group-demo.tsx`, `apps/v4/registry/new-york-v4/examples/input-group-button.tsx`, `apps/v4/content/docs/components/base/input-group.mdx`_
