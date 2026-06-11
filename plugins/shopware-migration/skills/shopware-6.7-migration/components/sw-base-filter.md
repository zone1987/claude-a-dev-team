# sw-base-filter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| showResetButton | `any` | — | yes |  |
| active | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-reset | — | |

## Methods

| Method | Description |
|--------|-------------|
| `resetFilter` | |

## Examples

### Basic Usage
```twig
<sw-base-filter
    title="..."
    showResetButton="..."
    active="..."
>
    <!-- content -->
</sw-base-filter>
```
