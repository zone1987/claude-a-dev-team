# Alert Dialog — API Reference

## Composition

```
AlertDialog
├── AlertDialogTrigger
└── AlertDialogContent (size="default"|"sm")
    ├── AlertDialogHeader
    │   ├── AlertDialogMedia (optional)
    │   ├── AlertDialogTitle
    │   └── AlertDialogDescription
    └── AlertDialogFooter
        ├── AlertDialogCancel
        └── AlertDialogAction
```

## AlertDialog

Root — no visible output. Controls open state.

## AlertDialogTrigger

| Prop | Type | Notes |
|------|------|-------|
| `asChild` (Radix) | `boolean` | Render trigger as child |
| `render` (Base) | render prop | Base UI render pattern |

## AlertDialogContent

| Prop | Type | Default |
|------|------|---------|
| `size` | `"default" \| "sm"` | `"default"` |
| `className` | `string` | — |

`size="sm"` → max-w-xs, grid footer layout.  
`size="default"` → sm:max-w-lg, row footer layout.

## AlertDialogAction

| Prop | Type | Default |
|------|------|---------|
| `variant` | Button variant | `"default"` |
| `size` | Button size | `"default"` |

## AlertDialogCancel

| Prop | Type | Default |
|------|------|---------|
| `variant` | Button variant | `"outline"` |
| `size` | Button size | `"default"` |

## External API docs

- Radix UI: https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference
- Base UI: https://base-ui.com/react/components/alert-dialog#api-reference

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/alert-dialog.mdx`
