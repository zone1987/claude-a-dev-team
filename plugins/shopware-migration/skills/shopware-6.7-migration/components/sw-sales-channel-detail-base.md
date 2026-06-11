# sw-sales-channel-detail-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| productExport | `any` | — | yes |  |
| storefrontSalesChannelCriteria | `any` | — | no |  |
| customFieldSets | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| productComparisonAccessUrl | `any` | `''` | no |  |
| templateOptions | `any` | — | no |  |
| showTemplateModal | `any` | `false` | no |  |
| templateName | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| template-selected | — | |
| template-modal-close | — | |
| template-modal-confirm | — | |
| invalid-file-name | — | |
| valid-file-name | — | |
| access-key-changed | — | |
| domain-changed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onGenerateKeys` | |
| `onGenerateProductExportKey` | |
| `onToggleActive` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `deleteSalesChannel` | |
| `extractFkInfo` | |
| `copyToClipboard` | |
| `onStorefrontSelectionChange` | |
| `onStorefrontDomainSelectionChange` | |
| `loadStorefrontDomains` | |
| `onChangeFileName` | |
| `onChangeFileNameDebounce` | |
| `changeInterval` | |
| `createCategoryCollections` | |
| `createCategoriesCollection` | |
| `onMainSelectionAdd` | |
| `onMainSelectionRemove` | |
| `onFooterSelectionAdd` | |
| `onFooterSelectionRemove` | |
| `onServiceSelectionAdd` | |
| `onServiceSelectionRemove` | |
| `buildDisabledPaymentAlert` | |
| `buildDisabledShippingAlert` | |
| `buildUnservedLanguagesAlert` | |
| `isFavorite` | |
| `validateMaintenanceIpCidr` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `secretAccessKeyFieldType` | |
| `isStorefront` | |
| `isDomainAware` | |
| `salesChannelRepository` | |
| `isProductComparison` | |
| `isHeadlessSalesChannel` | |
| `storefrontSalesChannelDomainCriteria` | |
| `storefrontSalesChannelCurrencyCriteria` | |
| `paymentMethodCriteria` | |
| `countryCriteria` | |
| `languageCriteria` | |
| `disabledCountries` | |
| `disabledCountryVariant` | |
| `disabledPaymentMethods` | |
| `disabledPaymentMethodVariant` | |
| `disabledShippingMethods` | |
| `disabledShippingMethodVariant` | |
| `unservedLanguages` | |
| `unservedLanguageVariant` | |
| `storefrontDomainsLoaded` | |
| `domainRepository` | |
| `globalDomainRepository` | |
| `productExportRepository` | |
| `mainNavigationCriteria` | |
| `getIntervalOptions` | |
| `getFileFormatOptions` | |
| `getEncodingOptions` | |
| `invalidFileNameError` | |
| `helpTextTaxCalculation` | |
| `taxCalculationTypeOptions` | |
| `maintenanceIpAllowlist` | |
| `salesChannelNameError` | |
| `salesChannelCustomerGroupIdError` | |
| `salesChannelNavigationCategoryIdError` | |
| `productExportProductStreamIdError` | |
| `productExportEncodingError` | |
| `productExportFileNameError` | |
| `productExportFileFormatError` | |
| `productExportStorefrontSalesChannelIdError` | |
| `productExportSalesChannelDomainIdError` | |
| `productExportCurrencyIdError` | |
| `categoryRepository` | |
| `mainCategoryCriteria` | |
| `footerCategoryCriteria` | |
| `serviceCategoryCriteria` | |
| `mainCategories` | |
| `footerCategories` | |
| `serviceCategories` | |
| `navigationCategoryPlaceholder` | |
| `footerCategoryPlaceholder` | |
| `serviceCategoryPlaceholder` | |
| `salesChannelFavoritesService` | |
| `currencyCriteria` | |
| `shippingMethodCriteria` | |
| `productStreamCriteria` | |
| `dateFilter` | |
| `cliCommand` | |
| `templateSelectOptions` | |

## Examples

### Basic Usage
```twig
<sw-sales-channel-detail-base
    salesChannel="..."
    productExport="..."
>
    <!-- content -->
</sw-sales-channel-detail-base>
```
