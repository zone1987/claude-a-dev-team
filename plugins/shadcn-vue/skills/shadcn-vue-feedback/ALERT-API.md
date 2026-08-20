# Alert — API Reference

## Anatomy

```vue
<Alert variant="default">
  <!-- optional: SVG icon here -->
  <AlertTitle>Title</AlertTitle>
  <AlertDescription>Description text.</AlertDescription>
</Alert>
```

The grid layout automatically detects an SVG child via `has-[>svg]` and switches from
single-column to two-column (icon + text) layout.

## alertVariants (CVA)

```ts
alertVariants({ variant: "default" | "destructive" })
```

Base classes:
- `relative w-full rounded-lg border px-4 py-3 text-sm`
- Grid: `grid has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] grid-cols-[0_1fr]`
- SVG: `[&>svg]:size-4 [&>svg]:translate-y-0.5 [&>svg]:text-current`

## Alert

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `"default" \| "destructive"` | `"default"` | Visual style variant |
| `class` | `string` | — | Additional CSS classes |

**Attributes:** `role="alert"` is always set.

**Slots:** default — place icon (SVG), AlertTitle, AlertDescription in any combination

## AlertTitle

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

Classes: `col-start-2 line-clamp-1 min-h-4 font-medium tracking-tight`

## AlertDescription

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional CSS classes |

Classes: `text-muted-foreground col-start-2 text-sm [&_p]:leading-relaxed`

---
Source: `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/alert/`
