# Empty — API Reference

## Composition Tree

```text
Empty
├── EmptyHeader
│   ├── EmptyMedia
│   ├── EmptyTitle
│   └── EmptyDescription
└── EmptyContent
```

## Sub-component Props

### Empty

Main container. Flex column, centered, `text-balance`.

| Prop        | Type     | Default | Description                        |
| ----------- | -------- | ------- | ---------------------------------- |
| `className` | `string` | –       | Add `border border-dashed` for outline style |

### EmptyHeader

Wraps media, title, and description in a centered flex column (max-w-sm).

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### EmptyMedia

Displays the icon, image, or avatar. Uses CVA variants.

| Prop        | Type                    | Default     | Description                              |
| ----------- | ----------------------- | ----------- | ---------------------------------------- |
| `variant`   | `"default" \| "icon"`  | `"default"` | `icon` renders a 40px rounded bg-muted box |
| `className` | `string`                | –           | Additional CSS classes                   |

**Variant details:**
- `default` — transparent background, use for avatars and images
- `icon` — `size-10` rounded-lg `bg-muted`, auto-sizes SVG to 24px (`size-6`)

```tsx
{/* Icon variant */}
<EmptyMedia variant="icon">
  <FolderIcon />
</EmptyMedia>

{/* Avatar variant (default) */}
<EmptyMedia>
  <Avatar className="size-12">
    <AvatarImage src="..." />
    <AvatarFallback>AB</AvatarFallback>
  </Avatar>
</EmptyMedia>
```

### EmptyTitle

Title text with `text-lg font-medium tracking-tight`.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### EmptyDescription

Muted helper text. Inline `<a>` links are automatically styled with underline.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

### EmptyContent

Action area below the header. Centered flex column.

| Prop        | Type     | Default | Description          |
| ----------- | -------- | ------- | -------------------- |
| `className` | `string` | –       | Additional CSS classes |

---

_Source: `apps/v4/content/docs/components/base/empty.mdx`_
