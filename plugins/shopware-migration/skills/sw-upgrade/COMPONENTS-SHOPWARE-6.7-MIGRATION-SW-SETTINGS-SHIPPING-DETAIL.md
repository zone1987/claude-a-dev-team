# sw-settings-shipping-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| shippingMethodId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSaveRule` | |
| `loadCurrencies` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onSave` | |
| `onError` | |
| `filterIncompletePrices` | |
| `getIncompletePrices` | |
| `onCancel` | |
| `setMediaItem` | |
| `onDropMedia` | |
| `setMediaFromSidebar` | |
| `onUnlinkLogo` | |
| `openMediaSidebar` | |
| `sortCurrencies` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `currencies` | |
| `restrictedRuleIds` | |
| `shippingMethodNameError` | |
| `shippingMethodTechnicalNameError` | |
| `shippingMethodDeliveryTimeIdError` | |
| `shippingMethodAvailabilityRuleIdError` | |
| `identifier` | |
| `shippingMethodRepository` | |
| `shippingMethodPricesRepository` | |
| `currencyRepository` | |
| `isNewShippingMethod` | |
| `mediaRepository` | |
| `deliveryTimeRepository` | |
| `deliveryTimeCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `ruleFilter` | |
| `shippingMethodCriteria` | |
| `showCustomFields` | |

## Examples

### Basic Usage
```twig
<sw-settings-shipping-detail>
    <!-- content -->
</sw-settings-shipping-detail>
```
