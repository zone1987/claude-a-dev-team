# sw-sales-channel-config

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| domain | `any` | `''` | no |  |
| value | `any` | — | no |  |
| criteria | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| select | — | |
| content | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| salesChannelChanged | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `readAll` | |
| `onInput` | |
| `save` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `actualConfigData` | |
| `salesChannelRepository` | |

## Examples

### Basic Usage
```twig
<sw-sales-channel-config>
    <!-- content -->
</sw-sales-channel-config>
```
