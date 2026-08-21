# sw-multi-snippet-drag-and-drop

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| totalLines | `any` | — | yes |  |
| linePosition | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| dragConfig | `any` | — | no |  |
| dropConfig | `any` | — | no |  |
| getLabelProperty | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selected-option | — | |
| label-property | — | |
| input | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onDragStart` | |
| `onDragEnter` | |
| `onDrop` | |
| `isSelectionDisabled` | |
| `onClickDismiss` | |
| `addNewLineAt` | |
| `moveToNewPosition` | |
| `onDelete` | |
| `openModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `errorObject` | |
| `mergedDragConfig` | |
| `mergedDropConfig` | |
| `isMaxLines` | |
| `isMinLines` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
    <sw-multi-snippet-drag-and-drop
        v-for="(snippet, index) in addressFormat"
        :key="index"
        v-droppable="{ data: { snippet, index }, dragGroup: 'sw-multi-snippet' }"
        v-draggable="{ ...dragConf, data: { snippet, index }}"
        :value="snippet"
        :line-position="index"
        :get-label-property="getLabelProperty"
        :total-lines="addressFormat.length"
        @update:value="change"
        @drop-end="onDropEnd"
        @position-move="moveToNewPosition"
        @add-new-line="addNewLineAt"
        @open-snippet-modal="openSnippetModal"
    />
```
