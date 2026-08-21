# Alert — API Reference

## Composition

```
Alert
├── Icon (optional svg)
├── AlertTitle
├── AlertDescription
└── AlertAction (Base UI only by default)
```

## Alert

| Prop | Type | Default |
|------|------|---------|
| `variant` | `"default" \| "destructive"` | `"default"` |
| `className` | `string` | — |

The grid layout auto-adjusts when an SVG icon is a direct child.

## AlertTitle

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## AlertDescription

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## AlertAction (Base UI version)

Positioned absolutely in top-right corner.

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## data-slot values

- `data-slot="alert"`
- `data-slot="alert-title"`
- `data-slot="alert-description"`
- `data-slot="alert-action"` (Base UI)

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/base/alert.mdx`
