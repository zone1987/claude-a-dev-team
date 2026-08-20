# sw-sales-channel-defaults-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | `null` | no |  |
| propertyName | `any` | — | yes |  |
| propertyLabel | `any` | — | yes |  |
| defaultPropertyName | `any` | — | yes |  |
| defaultPropertyLabel | `any` | — | yes |  |
| propertyNameInDomain | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| criteria | `any` | — | no |  |
| disabledTooltipMessage | `any` | `''` | no |  |
| shouldShowActiveState | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `updateCollection` | |
| `getNotInCollection` | |
| `addItem` | |
| `removeItem` | |
| `getDomainUsingValue` | |
| `updateDefault` | |
| `isDisabledItem` | |
| `getActiveIconColor` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `propertyCollection` | |
| `defaultId` | |
| `propertyEntityName` | |
| `propertyNameKebabCase` | |
| `multiSelectClass` | |
| `singleSelectClass` | |
| `defaultsValueError` | |
| `labelProperty` | |
| `showClearableButtonForDefault` | |

## Examples

### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-defaults-select
    v-if="!isProductComparison"
    :sales-channel="salesChannel"
    property-name="countries"
    :property-label="$tc('sw-sales-channel.detail.labelInputCountries')"
    :help-text="$tc('sw-sales-channel.detail.countryMultiSelectHelpText')"
    default-property-name="countryId"
    :criteria="countryCriteria"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :default-property-label="$tc('sw-sales-channel.detail.labelInputDefaultCountry')"
    :disabled-tooltip-message="$tc('sw-sales-channel.detail.tooltipDisabledCountry')"
    should-show-active-state
/>
{% endblock %}

```

### Example 2
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-defaults-select
    v-if="!isProductComparison"
    :sales-channel="salesChannel"
    property-name="paymentMethods"
    :criteria="paymentMethodCriteria"
    :property-label="$tc('sw-sales-channel.detail.labelInputPaymentMethods')"
    default-property-name="paymentMethodId"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :default-property-label="$tc('sw-sales-channel.detail.labelInputDefaultPaymentMethod')"
    :disabled-tooltip-message="$tc('sw-sales-channel.detail.tooltipDisabledPaymentMethod')"
    should-show-active-state
/>
{% endblock %}

{% block sw_sales_channel_detail_base_disabled_shipping_methods_warning %}
```
