# Avatar — API Reference

## Composition

```
Avatar
├── AvatarImage
├── AvatarFallback
└── AvatarBadge

AvatarGroup
├── Avatar ...
└── AvatarGroupCount
```

## Avatar

| Prop | Type | Default |
|------|------|---------|
| `size` | `"default" \| "sm" \| "lg"` | `"default"` |
| `className` | `string` | — |

Sizes: `sm`=24px, `default`=32px, `lg`=40px.

## AvatarImage

| Prop | Type | Notes |
|------|------|-------|
| `src` | `string` | Image URL |
| `alt` | `string` | Alt text |
| `className` | `string` | — |

## AvatarFallback

| Prop | Type | Notes |
|------|------|-------|
| `className` | `string` | — |
| `children` | `ReactNode` | Initials or icon |

## AvatarBadge

Positioned at bottom-right. Size scales with `Avatar` size.

| Prop | Type | Notes |
|------|------|-------|
| `className` | `string` | Override color: `className="bg-green-600"` |
| `children` | `ReactNode` | Optional icon |

## AvatarGroup

| Prop | Type | Notes |
|------|------|-------|
| `className` | `string` | — |

Applies negative space-x-2 and ring to children.

## AvatarGroupCount

| Prop | Type | Notes |
|------|------|-------|
| `className` | `string` | — |
| `children` | `ReactNode` | "+5" text or icon |

## data-slot values

- `data-slot="avatar"`, `avatar-image`, `avatar-fallback`, `avatar-badge`,
  `avatar-group`, `avatar-group-count`

## External API docs

- Radix UI: https://www.radix-ui.com/primitives/docs/components/avatar#api-reference
- Base UI: https://base-ui.com/react/components/avatar#api-reference

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/avatar.mdx`
