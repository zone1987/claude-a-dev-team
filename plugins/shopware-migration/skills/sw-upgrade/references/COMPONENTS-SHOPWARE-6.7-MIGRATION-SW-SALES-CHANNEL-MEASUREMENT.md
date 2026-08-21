# sw-sales-channel-measurement

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| labelUnitSystem | `any` | — | no |  |
| labelLengthUnit | `any` | — | no |  |
| labelWeightUnit | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| measurement-system-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onMeasurementSystemChange` | |
| `formatUnitLabel` | |
| `getDefaultMeasurementSystems` | |
| `getUnitOptionsByType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `measurementSystemRepository` | |
| `measurementSystemCriteria` | |
| `unitSystemLabel` | |
| `dimensionUnitLabel` | |
| `weightUnitLabel` | |
| `measurementUnits` | |
| `measurementSystemOptions` | |
| `lengthUnitOptions` | |
| `weightUnitOptions` | |
| `defaultLengthUnit` | |
| `defaultWeightUnit` | |
| `measurementUnitSystemError` | |
| `measurementLengthUnitError` | |
| `measurementWeightUnitError` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig`
```twig
<sw-sales-channel-measurement
    :sales-channel="currentDomain"
    :label-unit-system="$tc('sw-sales-channel.detail.measurementSystem.labelUnitSystem')"
    :label-length-unit="$tc('sw-sales-channel.detail.measurementSystem.labelLengthUnit')"
    :label-weight-unit="$tc('sw-sales-channel.detail.measurementSystem.labelWeightUnit')"
/>

{% block sw_sales_channel_detail_domains_hreflang %}
<sw-radio-field
    v-model:value="currentDomain.hreflangUseOnlyLocale"
    :label="$tc('sw-sales-channel.detail.hreflang.domainSettings.label')"
    identification="hreflang"
    :options="hreflangLocalisationOptions"
/>
{% endblock %}
```

### Example 2
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-sales-channel-measurement
        v-if="!isProductComparison"
        :sales-channel="salesChannel"
        :label-unit-system="$tc('sw-sales-channel.detail.measurementSystem.labelDefaultUnitSystem')"
        :label-length-unit="$tc('sw-sales-channel.detail.measurementSystem.labelDefaultLengthUnit')"
        :label-weight-unit="$tc('sw-sales-channel.detail.measurementSystem.labelDefaultWeightUnit')"
    />
</mt-card>
{% endblock %}

{% block sw_sales_channel_shipping_payment %}
<mt-card
    v-if="salesChannel"
    position-identifier="sw-sales-channel-detail-base-shipping-payment"
    :is-loading="isLoading"
```
