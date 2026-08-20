# sw-custom-field-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentCustomField | `any` | — | yes |  |
| set | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| custom-field-edit-cancel | — | |
| custom-field-edit-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCancel` | |
| `onSave` | |
| `createNameNotUniqueNotification` | |
| `createEntityTypeRequiredNotification` | |
| `applyTypeConfiguration` | |
| `getCartExposeTooltipConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `locales` | |
| `canSave` | |
| `renderComponentName` | |
| `modalTitle` | |
| `labelSaveButton` | |
| `isProductCustomField` | |
| `ruleConditionRepository` | |
| `customFieldTypeOptions` | |
| `currentCustomFieldNameError` | |

## Examples

### Example 1
Source: `sw-settings-custom-field/component/sw-custom-field-list/sw-custom-field-list.html.twig`
```twig
<sw-custom-field-detail
    v-if="currentCustomField"
    :set="set"
    :current-custom-field="currentCustomField"
    @custom-field-edit-save="onSaveCustomField"
    @custom-field-edit-cancel="onCancelCustomField"
/>
{% endblock %}

{% block sw_custom_field_list_custom_field_delete %}
<sw-modal
    v-if="deleteCustomField"
    :title="$tc('sw-settings-custom-field.customField.list.titleDeleteAction', {}, deleteCustomField.length)"
    variant="small"
    @modal-close="onCancelDeleteCustomField"
```
