# Tabs — API Reference

## Tabs (Root)

Extends `React.ComponentProps<typeof TabsPrimitive.Root>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultValue` | `string` | — | Default active tab value (uncontrolled) |
| `value` | `string` | — | Controlled active tab value |
| `onValueChange` | `(value: string) => void` | — | Callback fired when the active tab changes |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Layout direction; affects flex direction and trigger sizing |
| `dir` | `"ltr" \| "rtl"` | — | Text direction for RTL support |
| `activationMode` | `"automatic" \| "manual"` | `"automatic"` | `"automatic"` activates on focus; `"manual"` requires Enter/Space |
| `className` | `string` | — | Additional CSS classes |

## TabsList

Extends `React.ComponentProps<typeof TabsPrimitive.List>` and `VariantProps<typeof tabsListVariants>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `"default" \| "line"` | `"default"` | Visual style: `"default"` renders a pill/card background; `"line"` renders an underline-only indicator |
| `className` | `string` | — | Additional CSS classes |

## TabsTrigger

Extends `React.ComponentProps<typeof TabsPrimitive.Trigger>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `string` | required | Unique identifier matching a `TabsContent` value |
| `disabled` | `boolean` | `false` | Disables the trigger; pointer events blocked, opacity reduced |
| `className` | `string` | — | Additional CSS classes |

## TabsContent

Extends `React.ComponentProps<typeof TabsPrimitive.Content>`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `string` | required | Matches the corresponding `TabsTrigger` value |
| `forceMount` | `boolean` | — | When `true`, content is always mounted in the DOM regardless of active state (useful for animations) |
| `className` | `string` | — | Additional CSS classes |

## tabsListVariants

CVA variant helper exported for custom use.

```ts
const tabsListVariants = cva("...", {
  variants: {
    variant: {
      default: "bg-muted",
      line: "gap-1 bg-transparent",
    },
  },
  defaultVariants: {
    variant: "default",
  },
})
```

Use when building custom TabsList-like wrappers that need the same variant logic.
