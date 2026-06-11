# sw-product-variants-overview

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productEntity | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |
| productStates | `any` | — | no |  |
| productType | `any` | `'all'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| generator-open | — | |
| delivery-open | — | |
| variants-finish-update | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `removeFile` | |
| `mediaExists` | |
| `successfulUpload` | |
| `getDownloadsSource` | |
| `getList` | |
| `buildSearchQuery` | |
| `getFilterOptions` | |
| `resetFilterOptions` | |
| `filterOptionChecked` | |
| `getFilterCriteria` | |
| `getOptionsForGroup` | |
| `isPriceFieldInherited` | |
| `isActiveFieldInherited` | |
| `isMediaFieldInherited` | |
| `onInheritanceRestore` | |
| `onActiveInheritanceRestore` | |
| `onActiveInheritanceRemove` | |
| `onInheritanceRemove` | |
| `onMediaInheritanceRestore` | |
| `onMediaInheritanceRemove` | |
| `getDefaultPriceForVariant` | |
| `onVariationDelete` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `canVariantBeDeleted` | |
| `onOptionEdit` | |
| `isPriceEditing` | |
| `toggleBulkEditModal` | |
| `onEditItems` | |
| `onClickBulkDelete` | |
| `variantIsDigital` | |
| `updateVariantListingConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `currencies` | |
| `taxes` | |
| `variants` | |
| `isLoading` | |
| `defaultPrice` | |
| `defaultCurrency` | |
| `productTaxRate` | |
| `productRepository` | |
| `productMediaRepository` | |
| `mediaRepository` | |
| `productDownloadRepository` | |
| `variantColumns` | |
| `currencyColumns` | |
| `canBeDeletedCriteria` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
<sw-product-variants-overview
    v-if="product.id"
    v-show="variantListHasContent && !isLoading"
    ref="generatedVariants"
    :product-states="currentProductStates"
    :product-type="currentProductType"
    :groups="groups"
    :selected-groups="configSettingGroups"
    :product-entity="productEntity"
    @variants-finish-update="updateVariantListHasContent"
    @generator-open="openModal('variantGeneration')"
    @delivery-open="openModal('deliveryModal')"
/>
{% endblock %}

```
