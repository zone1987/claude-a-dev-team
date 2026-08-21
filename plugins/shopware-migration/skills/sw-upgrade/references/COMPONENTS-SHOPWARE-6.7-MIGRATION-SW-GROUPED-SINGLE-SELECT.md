# sw-grouped-single-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| groups | `any` | — | yes |  |
| groupIdProperty | `any` | `'id'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-group | — | |
| result-item | — | |
| result-label-property | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getGroupClasses` | |
| `getGroupLabel` | |
| `shouldShowGroupTitle` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-grouped-single-select
    class="sw-flow-sequence-action__selection-action"
    size="small"
    value=""
    :placeholder="$tc('sw-flow.actions.placeholderSelectAction')"
    :options="actionOptions"
    :groups="groups"
    :popover-classes="['sw-flow-sequence-action__popover']"
    :error="fieldError"
    :disabled="isUnknownTrigger"
    @update:value="openDynamicModal"
>
    <template #result-item="{ item, index, labelProperty, highlightSearchTerm, isSelected, setValue, getKey }">
        <sw-select-result
            v-tooltip="{
```
