# Button Group — API Reference

## Composition

```
ButtonGroup
├── Button or Input or Select
├── ButtonGroupSeparator
└── ButtonGroupText

# Nested groups with gaps:
ButtonGroup
├── ButtonGroup (inner group A)
└── ButtonGroup (inner group B)
```

## ButtonGroup

| Prop | Type | Default |
|------|------|---------|
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` |
| `className` | `string` | — |
| `aria-label` | `string` | Recommended for accessibility |

Has `role="group"`.

## ButtonGroupSeparator

Visual divider between buttons (no border for `outline` variant buttons
needed — they have borders already).

| Prop | Type | Default |
|------|------|---------|
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` |
| `className` | `string` | — |

## ButtonGroupText

Static text or label inside the group.

| Prop | Type | Default |
|------|------|---------|
| `asChild` (Radix) | `boolean` | `false` |
| `render` (Base) | render prop | — |
| `className` | `string` | — |

## ButtonGroup vs ToggleGroup

- `ButtonGroup` — for buttons that perform actions
- `ToggleGroup` — for buttons that toggle state

## Accessibility

```tsx
<ButtonGroup aria-label="Text formatting">
  <Button>Bold</Button>
  <Button>Italic</Button>
</ButtonGroup>
```

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/button-group.mdx`
