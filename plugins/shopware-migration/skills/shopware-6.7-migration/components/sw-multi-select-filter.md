# sw-multi-select-filter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-update | — | |
| filter-reset | — | |

## Methods

| Method | Description |
|--------|-------------|
| `changeValue` | |
| `resetFilter` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isEntityMultiSelect` | |
| `labelProperty` | |
| `values` | |

## Examples

### Basic Usage
```twig
<sw-multi-select-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-multi-select-filter>
```
