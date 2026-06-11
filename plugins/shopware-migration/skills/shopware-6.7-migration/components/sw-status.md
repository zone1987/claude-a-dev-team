# sw-status

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| color | `any` | `'green'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `statusClass` | |

## Examples

### Example 1
Source: `sw-sales-channel/page/sw-sales-channel-list/sw-sales-channel-list.html.twig`
```twig
<sw-status color="orange">
    {{ $tc('sw-sales-channel.list.status.maintenance') }}
</sw-status>
```

### Example 2
Source: `sw-sales-channel/page/sw-sales-channel-list/sw-sales-channel-list.html.twig`
```twig
<sw-status color="green">
    {{ $tc('sw-sales-channel.list.status.online') }}
</sw-status>
```

### Example 3
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<sw-status
    :color="serviceStatus"
>
    {{ $t(statusText) }}
</sw-status>
```
