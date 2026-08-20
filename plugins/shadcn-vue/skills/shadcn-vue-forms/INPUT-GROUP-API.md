# InputGroup — API

## Sub-components

| Component | Description |
|---|---|
| `InputGroup` | Root container, controls focus and error state via has-[...] |
| `InputGroupAddon` | Addon area (icon, text, button), automatically focuses the input on click |
| `InputGroupInput` | Input replacement with `data-slot="input-group-control"` |
| `InputGroupTextarea` | Textarea replacement with `data-slot="input-group-control"` |
| `InputGroupButton` | Button inside an addon (ghost, xs by default) |
| `InputGroupText` | Text span for static labels in the addon |

## InputGroupAddon

| Prop | Type | Default | Description |
|---|---|---|---|
| `align` | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` | Position of the addon |
| `class` | `string` | - | - |

### Alignments

| Value | Usage | Placement |
|---|---|---|
| `inline-start` | For `InputGroupInput` | Left/leading, `order-first` |
| `inline-end` | For `InputGroupInput` | Right/trailing, `order-last` |
| `block-start` | For `InputGroupTextarea` | Top, `order-first`, `w-full` |
| `block-end` | For `InputGroupTextarea` | Bottom, `order-last`, `w-full` |

Important: place the addon AFTER the input in DOM order (CSS `order` controls the visual order). This keeps the tab order correct.

## InputGroupButton

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"` | `"xs"` | Button size |
| `variant` | `ButtonVariants["variant"]` | `"ghost"` | Button variant |
| `class` | `string` | - | - |

## Custom Input

Add `data-slot="input-group-control"` to your own input elements to get focus-state handling:

```vue
<InputGroup>
  <textarea
    data-slot="input-group-control"
    class="flex field-sizing-content min-h-16 w-full resize-none rounded-md bg-transparent px-3 py-2.5 text-base outline-none md:text-sm"
    placeholder="Autoresize textarea..."
  />
  <InputGroupAddon align="block-end">
    <InputGroupButton class="ml-auto" size="sm" variant="default">Submit</InputGroupButton>
  </InputGroupAddon>
</InputGroup>
```
