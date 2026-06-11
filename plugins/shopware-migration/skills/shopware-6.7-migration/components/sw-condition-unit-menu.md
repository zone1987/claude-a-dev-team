# sw-condition-unit-menu

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | — | yes |  |
| value | `null \| null` | — | no |  |
| visibleValue | `null \| null` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| set-default-unit | — | |
| change-unit | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onUnitChange` | |
| `getConvertedValue` | |
| `isSelected` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `defaultUnit` | |
| `unitSnippet` | |
| `unitOptions` | |

## Examples

### Basic Usage
```twig
<sw-condition-unit-menu
    type="..."
>
    <!-- content -->
</sw-condition-unit-menu>
```
