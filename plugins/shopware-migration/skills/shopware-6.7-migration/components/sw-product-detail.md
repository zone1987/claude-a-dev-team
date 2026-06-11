# sw-product-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productId | `any` | `null` | no |  |
| creationStates | `any` | `null` | no |  |
| creationType | `any` | `'physical'` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initState` | |
| `initAdvancedModeSettings` | |
| `createUserModeSetting` | |
| `getAdvancedModeDefaultSetting` | |
| `getAdvancedModeSetting` | |
| `saveAdvancedMode` | |
| `onChangeSetting` | |
| `changeModeSettings` | |
| `onChangeSettingItem` | |
| `loadState` | |
| `loadAll` | |
| `createState` | |
| `adjustProductAccordingToType` | |
| `loadProduct` | |
| `getDefaultPurchasePrices` | |
| `loadParentProduct` | |
| `loadCurrencies` | |
| `loadTaxes` | |
| `getDefaultTaxRate` | |
| `loadAttributeSet` | |
| `loadDefaultFeatureSet` | |
| `getDefaultSalesChannels` | |
| `fetchSalesChannelByIds` | |
| `createProductVisibilityEntity` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `saveFinish` | |
| `onSave` | |
| `customValidate` | |
| `validateProductPrices` | |
| `validatePrices` | |
| `onSaveFinished` | |
| `onCancel` | |
| `saveProduct` | |
| `removeMediaItem` | |
| `onCoverChange` | |
| `getInheritTitle` | |
| `onDuplicate` | |
| `onDuplicateFinish` | |
| `validateProductPurchase` | |
| `getCmsPageOverrides` | |
| `deleteSpecifcKeys` | |
| `loadLanguage` | |
| `initProductMeasurementUnits` | |
| `getPreferredMeasurementUnits` | |
| `savePreferenceUnits` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `localMode` | |
| `advancedModeSetting` | |
| `modeSettings` | |
| `isLoading` | |
| `isChild` | |
| `defaultCurrency` | |
| `getDefaultFeatureSet` | |
| `showModeSetting` | |
| `advanceModeEnabled` | |
| `productStates` | |
| `productType` | |
| `swProductDetailBaseError` | |
| `swProductDetailCrossSellingError` | |
| `identifier` | |
| `productTitle` | |
| `productRepository` | |
| `propertyRepository` | |
| `syncRepository` | |
| `currencyRepository` | |
| `taxRepository` | |
| `customFieldSetRepository` | |
| `salesChannelRepository` | |
| `productVisibilityRepository` | |
| `mediaRepository` | |
| `featureSetRepository` | |
| `currentUser` | |
| `userModeSettingsRepository` | |
| `userModeSettingsCriteria` | |
| `productCriteria` | |
| `customFieldSetCriteria` | |
| `defaultFeatureSetCriteria` | |
| `taxCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `getModeSettingGeneralTab` | |
| `getModeSettingSpecificationsTab` | |
| `showAdvanceModeSetting` | |
| `cmsPageState` | |
| `currentPage` | |
| `languageRepository` | |
| `language` | |
| `translateFields` | |
| `ignoreFieldsValidation` | |
| `productApiContext` | |
| `lengthUnit` | |
| `weightUnit` | |
| `measurementUnitsChanged` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <sw-product-detail-context-prices
            :is-set-default-price="true"
            :can-set-loading-rules="false"
        />

        {% block sw_bulk_edit_product_content_advanced_prices_modal_footer %}
        <template #modal-footer>
            <slot name="sw-bulk-edit-modal-cancel">
                <mt-button
                    size="small"
                    variant="secondary"
                    @click="displayAdvancePricesModal = false"
                >
                    {{ $tc('global.default.close') }}
                </mt-button>
```
