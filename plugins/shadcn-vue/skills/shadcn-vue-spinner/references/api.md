# API Reference

## Spinner Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Additional Tailwind CSS classes |

## HTML Attributes

The component renders as `<svg>` via `Loader2Icon` with:
- `role="status"` for accessibility
- `aria-label="Loading"` for screen readers
- Default size `size-4` (1rem x 1rem) via Tailwind

## Customization

### Size

Use Tailwind `size-*` utility:

```vue
<Spinner class="size-6" />   <!-- 24px -->
<Spinner class="size-8" />   <!-- 32px -->
```

### Color

Use Tailwind `text-*` utility:

```vue
<Spinner class="text-primary" />
<Spinner class="text-destructive" />
<Spinner class="text-muted-foreground" />
```

### Custom Icon

Replace `Loader2Icon` in `Spinner.vue` with any other icon component.

## data-icon Attribute

When used inside buttons or badges, set `data-icon="inline-start"` to
apply correct spacing:

```vue
<Button>
  <Spinner data-icon="inline-start" /> Submit
</Button>
```
