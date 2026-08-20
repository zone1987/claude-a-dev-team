# sw-notification-center-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| notification | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| center-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isNotificationFromSameDay` | |
| `onDelete` | |
| `handleAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `itemHeaderClass` | |
| `notificationActions` | |

## Examples

### Basic Usage
```twig
<sw-notification-center-item
    notification="..."
>
    <!-- content -->
</sw-notification-center-item>
```
