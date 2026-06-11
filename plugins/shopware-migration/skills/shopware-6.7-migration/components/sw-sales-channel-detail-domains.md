# sw-sales-channel-detail-domains

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| disableEdit | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `sortColumns` | |
| `unicodeUriFilter` | |
| `localSortDomains` | |
| `getSortValue` | |
| `onInput` | |
| `verifyUrl` | |
| `domainExistsLocal` | |
| `isOriginalUrl` | |
| `domainExistsInDatabase` | |
| `setCurrentDomainBackup` | |
| `resetCurrentDomainToBackup` | |
| `setInitialCurrency` | |
| `setInitialLanguage` | |
| `setInitialMeasurementUnits` | |
| `onClickOpenCreateDomainModal` | |
| `onClickAddNewDomain` | |
| `onClickEditDomain` | |
| `onCloseCreateDomainModal` | |
| `onClickDeleteDomain` | |
| `onConfirmDeleteDomain` | |
| `onCloseDeleteDomainModal` | |
| `onLanguageSelect` | |
| `onCurrencySelect` | |
| `onOptionSelect` | |
| `getDomainColumns` | |
| `getMeasurementName` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `domainRepository` | |
| `currentDomainModalTitle` | |
| `currentDomainModalButtonText` | |
| `snippetSetCriteria` | |
| `salesChannelFilterCriteria` | |
| `currencyCriteria` | |
| `hreflangLocalisationOptions` | |
| `disabled` | |
| `sortedDomains` | |
| `measurementSystemRepository` | |
| `measurementSystemCriteria` | |

## Examples

### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-detail-domains
    v-if="salesChannel && isDomainAware"
    :sales-channel="salesChannel"
    :disable-edit="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_general_input_product_comparison_storefront %}
<mt-card
    v-if="salesChannel && isProductComparison"
    position-identifier="sw-sales-channel-detail-base-general-input-product-comparison-storefront"
    :is-loading="isLoading"
    :title="$tc('sw-sales-channel.detail.productComparison.storefront')"
>
```
