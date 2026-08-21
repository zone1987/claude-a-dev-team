# API Reference

The `Skeleton` component has no reka-ui dependency. It is a simple styled div.

## Skeleton

| Prop | Type | Default | Description |
|---|---|---|---|
| class | string | — | Additional CSS classes for sizing and shaping |

## Base Classes

The component applies these classes by default:

- `animate-pulse` — CSS pulse animation
- `rounded-md` — medium border radius
- `bg-primary/10` — 10% opacity primary color background

## data-slot Attributes

| Component | data-slot value |
|---|---|
| Skeleton | skeleton |

## Customization

Override with the `class` prop:

```vue
<!-- Circular (avatar) -->
<Skeleton class="size-10 rounded-full" />

<!-- Wide bar -->
<Skeleton class="h-4 w-full" />

<!-- Partial width -->
<Skeleton class="h-4 w-3/4" />

<!-- Square -->
<Skeleton class="aspect-square w-full" />

<!-- Input-sized -->
<Skeleton class="h-10 w-full" />

<!-- Button-sized -->
<Skeleton class="h-9 w-24" />
```
