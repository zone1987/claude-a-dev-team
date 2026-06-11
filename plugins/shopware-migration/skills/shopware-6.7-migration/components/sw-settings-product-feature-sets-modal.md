# sw-settings-product-feature-sets-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productFeatureSet | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchCustomFields` | |
| `onSearchPropertyGroups` | |
| `onClickNext` | |
| `getProductInformationList` | |
| `getCustomFieldList` | |
| `getPropertyList` | |
| `getList` | |
| `getFeaturesIds` | |
| `onChangeOption` | |
| `checkIfReferencePriceIsSelected` | |
| `onConfirm` | |
| `setFeatures` | |
| `setFeatureSelection` | |
| `applySelectionsToActiveGrid` | |
| `getPropertyGroupColumns` | |
| `getCustomFieldColumns` | |
| `getProductInformationColumns` | |
| `paginateCustomFieldGrid` | |
| `paginatePropertyGroupGrid` | |
| `readCustomFieldLabel` | |
| `getCurrentSelection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productFeatureSetRepository` | |
| `customFieldsRepository` | |
| `propertyGroupsRepository` | |
| `productFeatureSetCriteria` | |
| `customFieldCriteria` | |
| `propertyGroupCriteria` | |
| `referencePriceSelected` | |
| `propertyGroupColumns` | |
| `customFieldColumns` | |
| `productInformationColumns` | |
| `checkIfReferencePriceSelected` | |
| `settingOptions` | |
| `customFieldTotal` | |
| `propertyGroupTotal` | |
| `addButtonDisabled` | |

## Examples

### Example 1
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-values-card/sw-settings-product-feature-sets-values-card.html.twig`
```twig
    <sw-settings-product-feature-sets-modal
        v-if="showModal"
        :product-feature-set="productFeatureSet"
        @modal-close="onModalClose"
    />
    {% endblock %}

</mt-card>
{% endblock %}

```
