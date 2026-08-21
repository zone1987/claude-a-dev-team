# sw-select-option

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| index | `any` | — | yes |  |
| item | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| selected | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `registerEvents` | |
| `removeEvents` | |
| `emitActiveResultPosition` | |
| `onClicked` | |
| `checkActiveState` | |
| `selectOptionOnEnter` | |
| `isInSelections` | |
| `onMouseEnter` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |

## Examples

### Basic Usage
```twig
<sw-select-option
    index="..."
    item="..."
>
    <!-- content -->
</sw-select-option>
```
