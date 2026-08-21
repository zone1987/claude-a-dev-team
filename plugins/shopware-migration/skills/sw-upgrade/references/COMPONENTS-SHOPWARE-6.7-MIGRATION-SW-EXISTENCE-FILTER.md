# sw-existence-filter

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
| `filterOptions` | |

## Examples

### Basic Usage
```twig
<sw-existence-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-existence-filter>
```
