# sw-boolean-filter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

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
| `value` | |
| `options` | |

## Examples

### Basic Usage
```twig
<sw-boolean-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-boolean-filter>
```
