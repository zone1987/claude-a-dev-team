# Card — API Reference

## Composition

```text
Card
├── CardHeader
│   ├── CardTitle
│   ├── CardDescription
│   └── CardAction        (optional, positions itself to top-right via CSS grid)
├── CardContent
└── CardFooter
```

## Sub-components

All sub-components are pure layout primitives. They accept a single `class`
prop for Tailwind overrides and expose a default `<slot />`.

| Component          | Element | data-slot          | Default classes (abbreviated)                                   |
| ------------------ | ------- | ------------------ | --------------------------------------------------------------- |
| `Card`             | `div`   | `card`             | `bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm` |
| `CardHeader`       | `div`   | `card-header`      | `@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6` + conditional grid-cols when `CardAction` is present |
| `CardTitle`        | `h3`    | `card-title`       | `leading-none font-semibold`                                    |
| `CardDescription`  | `p`     | `card-description` | `text-muted-foreground text-sm`                                 |
| `CardAction`       | `div`   | `card-action`      | `col-start-2 row-span-2 row-start-1 self-start justify-self-end` |
| `CardContent`      | `div`   | `card-content`     | `px-6`                                                          |
| `CardFooter`       | `div`   | `card-footer`      | `flex items-center px-6 [.border-t]:pt-6`                       |

## Props (all components)

| Prop    | Type                      | Default     | Description                        |
| ------- | ------------------------- | ----------- | ---------------------------------- |
| `class` | `HTMLAttributes["class"]` | `undefined` | Additional Tailwind classes to merge via `cn()` |

## Slots (all components)

| Slot      | Description                  |
| --------- | ---------------------------- |
| `default` | Any content passed as children |

## Notes

- `CardAction` uses CSS grid positioning (`col-start-2 row-span-2 row-start-1`)
  to anchor itself to the top-right of `CardHeader`. `CardHeader` automatically
  switches to a two-column grid (`grid-cols-[1fr_auto]`) when a `CardAction`
  with `data-slot="card-action"` is present
  (`has-data-[slot=card-action]:grid-cols-[1fr_auto]`).
- `CardFooter` has a conditional top-padding rule `[.border-t]:pt-6` — add
  `class="border-t"` to get the spacing when using a top border.
- `CardHeader` has a conditional bottom-padding rule `[.border-b]:pb-6` — add
  `class="border-b"` to get the spacing when using a bottom border.
- No dependency on reka-ui. Pure layout components.

---
Source: `registry/new-york-v4/ui/card/`
