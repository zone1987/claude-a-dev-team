# Card — API Reference

## Composition

```text
Card
├── CardHeader
│   ├── CardTitle
│   ├── CardDescription
│   └── CardAction
├── CardContent
└── CardFooter
```

## Usage

```tsx
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
```

```tsx
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
    <CardAction>Card Action</CardAction>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
```

## Sub-Component Props

### Card

The root container for card content.

| Prop        | Type                | Default     |
| ----------- | ------------------- | ----------- |
| `size`      | `"default" \| "sm"` | `"default"` |
| `className` | `string`            | -           |

### CardHeader

Used for a title, description, and optional action. Uses CSS container queries (`@container/card-header`) to layout the optional `CardAction` in the top-right corner.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardTitle

The card title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardDescription

Helper text under the title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardAction

Places content in the top-right of the header (e.g. a button or badge). When present, `CardHeader` automatically switches to a two-column grid layout.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardContent

Main card body.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CardFooter

Actions and secondary content at the bottom of the card.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

## Spacing Customization

Use the `--card-spacing` CSS variable to control spacing between sections and the inset of card parts:

```tsx
<Card className="[--card-spacing:--spacing(6)]">...</Card>
```

Use negative margins to make content go edge-to-edge:

```tsx
<CardContent className="-mx-(--card-spacing)">...</CardContent>
```

## Changelog — Spacing Variable Migration

If upgrading from a previous version, replace hard-coded gap/padding values with `--card-spacing`:

```diff
// Card root
-  "group/card flex flex-col gap-4 overflow-hidden rounded-xl bg-card py-4 ..."
+  "group/card flex flex-col gap-(--card-spacing) overflow-hidden rounded-xl bg-card py-(--card-spacing) ... [--card-spacing:--spacing(4)] ..."

// CardHeader
-  "... px-4 group-data-[size=sm]/card:px-3 ... [.border-b]:pb-4 ..."
+  "... px-(--card-spacing) ... [.border-b]:pb-(--card-spacing)"

// CardContent
-  "px-4 group-data-[size=sm]/card:px-3"
+  "px-(--card-spacing)"

// CardFooter
-  "... p-4 group-data-[size=sm]/card:p-3"
+  "... p-(--card-spacing)"
```

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/card.mdx`_
