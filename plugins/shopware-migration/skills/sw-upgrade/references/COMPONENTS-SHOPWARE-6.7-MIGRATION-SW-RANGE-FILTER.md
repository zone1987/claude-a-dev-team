# sw-range-filter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| property | `any` | — | yes |  |
| isShowDivider | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| from-field | — | |
| divider | — | |
| to-field | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-update | — | |

## Methods

| Method | Description |
|--------|-------------|
| `updateFilter` | |

## Examples

### Basic Usage
```twig
<sw-range-filter
    value="..."
    property="..."
>
    <!-- content -->
</sw-range-filter>
```
