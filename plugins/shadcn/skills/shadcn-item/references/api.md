# Item — API Reference

## Composition

```text
ItemGroup
└── Item
    ├── ItemHeader
    ├── ItemMedia
    ├── ItemContent
    │   ├── ItemTitle
    │   └── ItemDescription
    ├── ItemActions
    └── ItemFooter
```

## Item vs Field

Use `Field` for form inputs (checkbox, input, radio, select).
Use `Item` for displaying content (title, description, actions).

## Item

The main flex container.

| Prop      | Type                                | Default     | Description                        |
| --------- | ----------------------------------- | ----------- | ---------------------------------- |
| `variant` | `"default" \| "outline" \| "muted"` | `"default"` | Visual style                       |
| `size`    | `"default" \| "sm"`                 | `"default"` | Spacing/padding                    |
| `asChild` | `boolean`                           | `false`     | Render as child element (e.g. `<a>`) |

## ItemGroup

Wraps multiple `Item` elements in a `role="list"` container.

```tsx
<ItemGroup>
  <Item />
  <Item />
</ItemGroup>
```

## ItemSeparator

Horizontal separator between items in a group.

```tsx
<ItemGroup>
  <Item />
  <ItemSeparator />
  <Item />
</ItemGroup>
```

## ItemMedia

Displays media (icon, image, avatar) beside the content.

| Prop      | Type                             | Default     | Description        |
| --------- | -------------------------------- | ----------- | ------------------ |
| `variant` | `"default" \| "icon" \| "image"` | `"default"` | Media display mode |

- `"icon"` — 32px bordered box, auto-sizes SVGs to 16px
- `"image"` — 40px clipped box, `object-cover` images

## ItemContent

Flex column wrapping title and description. Takes `flex: 1`.

## ItemTitle

Bold title text, `text-sm font-medium`.

## ItemDescription

Muted description, `text-sm text-muted-foreground`, clamps to 2 lines.

## ItemActions

Horizontal flex container for buttons/icons, `flex items-center gap-2`.

## ItemHeader

Full-width header row (`basis-full`) above the main item content.

## ItemFooter

Full-width footer row (`basis-full`) below the main item content.

---
Source: `content/docs/components/base/item.mdx`
