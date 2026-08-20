# Skeleton — API Reference

## Skeleton

Renders a `<div>` with pulse animation.

| Prop        | Type     | Default | Description                                                 |
| ----------- | -------- | ------- | ----------------------------------------------------------- |
| `className` | `string` | —       | Override or extend classes. Use `h-*`, `w-*`, `rounded-*`  |

All other `div` HTML attributes are forwarded.

`data-slot="skeleton"`

## Default styles

- `animate-pulse` — CSS pulse animation
- `rounded-md` — medium border radius
- `bg-accent` — uses `--accent` color token

## Common class overrides

| Use case            | Classes                                |
| ------------------- | -------------------------------------- |
| Circle avatar       | `h-12 w-12 rounded-full`               |
| Text line           | `h-4 w-[250px]`                        |
| Short text line     | `h-4 w-[200px]`                        |
| Card image area     | `h-[125px] w-[250px] rounded-xl`       |
| Full width block    | `h-4 w-full`                           |
| Button shape        | `h-9 w-24 rounded-md`                  |

## Source files

- `registry/new-york-v4/ui/skeleton.tsx`
