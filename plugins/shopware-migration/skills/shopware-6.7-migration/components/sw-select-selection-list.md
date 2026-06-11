# sw-select-selection-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selections | `any` | — | no |  |
| labelProperty | `any` | `'label'` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| enableSearch | `any` | `true` | no |  |
| invisibleCount | `any` | `0` | no |  |
| size | `any` | `null` | no |  |
| alwaysShowPlaceholder | `any` | `false` | no |  |
| placeholder | `any` | `''` | no |  |
| isLoading | `any` | `false` | no |  |
| searchTerm | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| hideLabels | `any` | `false` | no |  |
| inputLabel | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selected-option | — | |
| label-property | — | |
| invisible-count | — | |
| input | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| total-count-click | — | |
| search-term-change | — | |
| last-item-delete | — | |
| key-down-enter | — | |
| item-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isSelectionDisabled` | |
| `onClickInvisibleCount` | |
| `onSearchTermChange` | |
| `onKeyDownDelete` | |
| `onKeyDownEnter` | |
| `onClickDismiss` | |
| `focus` | |
| `blur` | |
| `select` | |
| `getFocusEl` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `showPlaceholder` | |

## Examples

### Basic Usage
```twig
<sw-select-selection-list>
    <!-- content -->
</sw-select-selection-list>
```
