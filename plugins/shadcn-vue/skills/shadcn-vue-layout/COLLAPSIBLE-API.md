# Collapsible — API

The `Collapsible` component wraps reka-ui `CollapsibleRoot`. `CollapsibleTrigger` and `CollapsibleContent` wrap their reka-ui counterparts.

## Collapsible (root)

### Props

All `CollapsibleRootProps` from reka-ui are accepted:

| Prop          | Type      | Default | Description                                     |
| ------------- | --------- | ------- | ----------------------------------------------- |
| `open`        | `boolean` | —       | Controlled open state                           |
| `defaultOpen` | `boolean` | `false` | Initial open state (uncontrolled)               |
| `disabled`    | `boolean` | `false` | Prevents the collapsible from being toggled     |

### Emits

| Event         | Payload   | Description                          |
| ------------- | --------- | ------------------------------------ |
| `update:open` | `boolean` | Fired when the open state changes    |

### v-model

```vue
<Collapsible v-model:open="isOpen">
  ...
</Collapsible>
```

## CollapsibleTrigger

Wraps `CollapsibleTriggerProps`. Accepts `asChild` (boolean) to render as the child element instead of a `<button>`.

```vue
<CollapsibleTrigger :as-child="true">
  <Button variant="ghost">Toggle</Button>
</CollapsibleTrigger>
```

## CollapsibleContent

Wraps `CollapsibleContentProps`. The content is automatically shown/hidden based on the root's open state and supports CSS-based animations via `data-state` (`open` | `closed`).

```vue
<CollapsibleContent class="mt-2">
  <p>Expanded content</p>
</CollapsibleContent>
```

## Full reka-ui API reference

https://reka-ui.com/docs/components/collapsible#api-reference
