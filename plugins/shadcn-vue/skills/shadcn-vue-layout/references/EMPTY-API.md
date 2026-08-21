# Empty — API

## Sub-components

| Component | Description |
|---|---|
| `Empty` | Root container (centered, flex-col, border-dashed optional) |
| `EmptyHeader` | Area for media, title, description |
| `EmptyMedia` | Media area (icon, avatar, image) |
| `EmptyTitle` | Title of the empty state |
| `EmptyDescription` | Description / help text |
| `EmptyContent` | Area for actions (buttons, input etc.) |

## Empty

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | - | E.g. `border` for outline, `bg-muted` for background |

Default classes: `flex min-w-0 flex-1 flex-col items-center justify-center gap-6 text-balance rounded-lg border-dashed p-6 text-center md:p-12`

## EmptyMedia

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `"default" \| "icon"` | `"default"` | Display variant |
| `class` | `string` | - | - |

### Variants

| Variant | Classes |
|---|---|
| `default` | `bg-transparent` — for images/avatars |
| `icon` | `bg-muted text-foreground size-10 rounded-lg` — for icons |

## All other components

All accept only `class: string`. No further props.

| Component | Base styling |
|---|---|
| `EmptyHeader` | `flex max-w-sm flex-col items-center gap-2 text-center` |
| `EmptyTitle` | `text-lg font-medium tracking-tight` |
| `EmptyDescription` | `text-muted-foreground text-sm/relaxed` + link styling |
| `EmptyContent` | `flex w-full min-w-0 max-w-sm flex-col items-center gap-4` |
