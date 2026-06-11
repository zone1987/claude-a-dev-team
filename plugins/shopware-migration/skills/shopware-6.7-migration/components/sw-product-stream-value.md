# sw-product-stream-value

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| condition | `any` | — | yes |  |
| fieldName | `any` | `null` | no |  |
| definition | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-label-property | — | |
| result-item | — | |
| result-description-property | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| empty-change | — | |
| type-change | — | |
| boolean-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeType` | |
| `getConditionType` | |
| `getRangeType` | |
| `getParameters` | |
| `getParameterName` | |
| `getParameterType` | |
| `setBooleanValue` | |
| `setSearchTerm` | |
| `onSelectCollapsed` | |
| `getCategoryBreadcrumb` | |
| `isEntityCustomField` | |
| `getCustomFieldEntityName` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `repository` | |
| `entityCustomFieldRepository` | |
| `componentClasses` | |
| `growthClass` | |
| `disabledClass` | |
| `actualCondition` | |
| `isMultiSelectValue` | |
| `filterType` | |
| `fieldDefinition` | |
| `operators` | |
| `relativeTimeOperators` | |
| `productStateOptions` | |
| `productTypeOptions` | |
| `fieldType` | |
| `booleanOptions` | |
| `reversedEmptyOptions` | |
| `multiValue` | |
| `inputComponent` | |
| `currentParameter` | |
| `gte` | |
| `lte` | |
| `operator` | |
| `emptyValue` | |
| `stringValue` | |
| `context` | |
| `productCriteria` | |
| `propertyCriteria` | |
| `visibilitiesCriteria` | |
| `resultCriteria` | |
| `customFieldCriteria` | |
| `visibilitiesLabelCallback` | |
| `isProductEntity` | |

## Examples

### Example 1
Source: `sw-product-stream/component/sw-product-stream-filter/sw-product-stream-filter.html.twig`
```twig
    <sw-product-stream-value
        v-bind="{ condition, ...lastField }"
        :disabled="!acl.can('product_stream.editor') || undefined"
        @type-change="changeType"
        @boolean-change="changeBooleanValue"
        @empty-change="changeEmptyValue"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_product_stream_filter_field_actions %}
<sw-context-button
    v-tooltip="getNoPermissionsTooltip('product_stream.editor', false)"
    class="sw-product-stream-filter__context-button"
```
