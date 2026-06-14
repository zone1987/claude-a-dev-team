# InputGroup — API Reference

## Composition Tree

```text
InputGroup
├── InputGroupInput or InputGroupTextarea
├── InputGroupAddon (align="inline-start" — default, placed before input visually)
├── InputGroupAddon (align="inline-end" — placed after input visually)
└── InputGroupAddon (align="block-start" or "block-end" — for Textarea)
    ├── InputGroupButton
    ├── InputGroupText
    └── (icons, Kbd, Separator, Tooltip, DropdownMenu, etc.)
```

> **Important:** Always place `InputGroupAddon` **after** `InputGroupInput`/`InputGroupTextarea` in the DOM for correct focus management. Use the `align` prop to position it visually.

## Basic Usage

```tsx
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"

<InputGroup>
  <InputGroupInput placeholder="Search..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

## Sub-component Props

### InputGroup

Main container with unified border, focus ring, and error state.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### InputGroupAddon

Displays icons, text, buttons, or other content.

| Prop        | Type                                                              | Default          | Description                                              |
| ----------- | ----------------------------------------------------------------- | ---------------- | -------------------------------------------------------- |
| `align`     | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` | Visual position of the addon                             |
| `className` | `string`                                                          | –                | Additional CSS classes                                   |

**Alignment rules:**
- `inline-start` / `inline-end` → use with `InputGroupInput`
- `block-start` / `block-end` → use with `InputGroupTextarea`

Clicking the addon (on non-button elements) automatically focuses the inner input.

### InputGroupButton

Compact button sized for inside an input group.

| Prop        | Type                                                                         | Default   | Description                     |
| ----------- | ---------------------------------------------------------------------------- | --------- | ------------------------------- |
| `size`      | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"`                                    | `"xs"`    | Button size variant             |
| `variant`   | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"ghost"` | Button visual variant           |
| `type`      | `"button" \| "submit" \| "reset"`                                            | `"button"` | Default prevents form submit   |
| `className` | `string`                                                                     | –         | Additional CSS classes          |

### InputGroupText

Inline text/icon label inside an addon (not interactive).

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### InputGroupInput

Drop-in replacement for `<Input />` inside an `InputGroup`. Removes border and focuses through the group.

| Prop        | Type     | Default | Description                  |
| ----------- | -------- | ------- | ---------------------------- |
| All `<input>` props forwarded | | | |
| `className` | `string` | –       | Additional CSS classes        |

### InputGroupTextarea

Drop-in replacement for `<Textarea />` inside an `InputGroup`. Auto-resizes, no border.

| Prop        | Type     | Default | Description                  |
| ----------- | -------- | ------- | ---------------------------- |
| All `<textarea>` props forwarded | | | |
| `className` | `string` | –       | Additional CSS classes        |

## Custom Input

Add `data-slot="input-group-control"` to any custom input to participate in focus state management:

```tsx
<InputGroup>
  <CustomInput data-slot="input-group-control" />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

---

_Source: `apps/v4/content/docs/components/base/input-group.mdx`, `apps/v4/registry/new-york-v4/ui/input-group.tsx`_
