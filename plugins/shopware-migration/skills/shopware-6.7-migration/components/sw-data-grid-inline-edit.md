# sw-data-grid-inline-edit

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| column | `any` | — | yes |  |
| value | `any` | — | yes |  |
| compact | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitInput` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `inputFieldSize` | |

## Examples

### Basic Usage
```twig
<sw-data-grid-inline-edit
    column="..."
    value="..."
>
    <!-- content -->
</sw-data-grid-inline-edit>
```
