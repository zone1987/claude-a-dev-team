# Tooltip — Examples

## Basic (`tooltip-demo.tsx`)

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/registry/new-york-v4/ui/tooltip"

export default function TooltipDemo() {
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <Button variant="outline">Hover</Button>
      </TooltipTrigger>
      <TooltipContent>
        <p>Add to library</p>
      </TooltipContent>
    </Tooltip>
  )
}
```

## Side Position

Use the `side` prop on `TooltipContent` to change where the tooltip appears:

```tsx
<Tooltip>
  <TooltipTrigger asChild>
    <Button variant="outline">Bottom</Button>
  </TooltipTrigger>
  <TooltipContent side="bottom">
    <p>Appears below</p>
  </TooltipContent>
</Tooltip>
```

Available values: `"top"` (default), `"right"`, `"bottom"`, `"left"`.

## With Keyboard Shortcut

```tsx
<Tooltip>
  <TooltipTrigger asChild>
    <Button variant="outline">Save</Button>
  </TooltipTrigger>
  <TooltipContent>
    <p>
      Save file{" "}
      <kbd className="ml-1 rounded bg-muted px-1 font-mono text-[10px]">
        Ctrl+S
      </kbd>
    </p>
  </TooltipContent>
</Tooltip>
```

## Disabled Button Tooltip

Disabled elements do not fire mouse events, so the tooltip trigger must be wrapped
in a `<span>` to receive the hover events:

```tsx
<Tooltip>
  <TooltipTrigger asChild>
    <span>
      <Button disabled>Disabled</Button>
    </span>
  </TooltipTrigger>
  <TooltipContent>This action is unavailable</TooltipContent>
</Tooltip>
```

## Controlled Open State

```tsx
const [open, setOpen] = React.useState(false)

<Tooltip open={open} onOpenChange={setOpen}>
  <TooltipTrigger asChild>
    <Button onClick={() => setOpen(true)}>Click to open</Button>
  </TooltipTrigger>
  <TooltipContent>
    <p>Controlled tooltip</p>
  </TooltipContent>
</Tooltip>
```

## Custom Delay

Override the provider delay for a single tooltip:

```tsx
<Tooltip delayDuration={500}>
  <TooltipTrigger asChild>
    <Button variant="ghost">Slow tooltip</Button>
  </TooltipTrigger>
  <TooltipContent>
    <p>Shows after 500ms</p>
  </TooltipContent>
</Tooltip>
```
