# sw-media-base-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| isList | `any` | `false` | no |  |
| showSelectionIndicator | `any` | `false` | no |  |
| showContextMenuButton | `any` | `true` | no |  |
| selected | `any` | `false` | no |  |
| editable | `any` | `true` | no |  |
| allowMultiSelect | `any` | `true` | no |  |
| truncateRight | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |
| allowDelete | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| preview | — | |
| name | — | |
| metadata | — | |
| context-menu | — | |
| modal-windows | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-click | — | |
| media-item-selection-add | — | |
| media-item-selection-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `handleItemClick` | |
| `isSelectionIndicatorClicked` | |
| `onClickedItem` | |
| `selectItem` | |
| `removeFromSelection` | |
| `startInlineEdit` | |
| `endInlineEdit` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaItemClasses` | |
| `mediaNameContainerClasses` | |
| `listSelected` | |
| `selectionIndicatorClasses` | |
| `isLoading` | |
| `isSpatial` | |

## Examples

### Basic Usage
```twig
<sw-media-base-item
    item="..."
>
    <!-- content -->
</sw-media-base-item>
```
