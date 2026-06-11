# sw-bulk-edit-product

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-bulk-edit-modal-cancel | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setRouteMetaModule` | |
| `setBulkEditProductValue` | |
| `getParentProduct` | |
| `loadDefaultCurrency` | |
| `defineBulkEditData` | |
| `loadBulkEditData` | |
| `loadCustomFieldSets` | |
| `loadTaxes` | |
| `productTaxRate` | |
| `loadCurrencies` | |
| `definePricesBulkEdit` | |
| `setProductPrice` | |
| `onChangePrices` | |
| `onCustomFieldsChange` | |
| `onProcessData` | |
| `processListPrice` | |
| `processRegulationPrice` | |
| `openModal` | |
| `onSave` | |
| `savePreferenceUnits` | |
| `closeModal` | |
| `onChangeLanguage` | |
| `loadRules` | |
| `loadPreferenceUnits` | |
| `onRuleChange` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `setProductSearchKeywords` | |
| `setProductAssociation` | |
| `onUpdateDefaultUnit` | |
| `convertWidth` | |
| `convertHeight` | |
| `convertLength` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `taxes` | |
| `defaultCurrency` | |
| `defaultPrice` | |
| `selectedIds` | |
| `customFieldSetRepository` | |
| `currencyRepository` | |
| `taxRepository` | |
| `productRepository` | |
| `hasSelectedChanges` | |
| `customFieldSetCriteria` | |
| `taxCriteria` | |
| `productCriteria` | |
| `isChild` | |
| `restrictedFields` | |
| `generalFormFields` | |
| `pricesFormFields` | |
| `advancedPricesFormFields` | |
| `propertyFormFields` | |
| `deliverabilityFormFields` | |
| `assignmentFormFields` | |
| `mediaFormFields` | |
| `labellingFormFields` | |
| `seoFormFields` | |
| `measuresPackagingFields` | |
| `sellingPackagingFields` | |
| `essentialCharacteristicsFormFields` | |
| `ruleRepository` | |
| `priceRepository` | |
| `ruleCriteria` | |
| `priceRuleGroups` | |
| `hasPreferenceUnitsChanged` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-bulk-edit-product-media-form
        :disabled="disabled || undefined"
        @media-open="showMediaModal = true"
    />
    {% endblock %}

    {% block sw_bulk_edit_product_media_modal %}
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
```
