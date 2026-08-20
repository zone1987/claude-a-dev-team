# sw-data-grid-settings

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| columns | `any` | — | yes |  |
| compact | `any` | `false` | yes |  |
| previews | `any` | `false` | yes |  |
| enablePreviews | `any` | `false` | yes |  |
| disabled | `any` | `false` | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additionalSettings | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-compact-mode | — | |
| change-preview-images | — | |
| change-column-visibility | — | |
| change-column-order | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeCompactMode` | |
| `onChangePreviews` | |
| `onChangeColumnVisibility` | |
| `onClickChangeColumnOrderUp` | |
| `onClickChangeColumnOrderDown` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `contextMenuClasses` | |

## Examples

### Basic Usage
```twig
<sw-data-grid-settings
    columns="..."
    compact="..."
    previews="..."
>
    <!-- content -->
</sw-data-grid-settings>
```
