# sw-price-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| allowModal | `any` | `false` | no |  |
| defaultPrice | `any` | — | no |  |
| hideListPrices | `any` | `false` | no |  |
| taxRate | `any` | — | no |  |
| currency | `any` | — | yes |  |
| validation | `any` | `null` | no |  |
| label | `any` | `true` | no |  |
| compact | `any` | `false` | no |  |
| error | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| disableSuffix | `any` | `false` | no |  |
| grossLabel | `any` | `null` | no |  |
| netLabel | `any` | `null` | no |  |
| name | `any` | `null` | no |  |
| allowEmpty | `any` | `false` | no |  |
| inherited | `any` | — | no |  |
| grossHelpText | `any` | `null` | no |  |
| netHelpText | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| price-lock-change | — | |
| price-calculate | — | |
| price-gross-change | — | |
| price-net-change | — | |
| calculating | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onLockSwitch` | |
| `onEndsWithDecimalSeparator` | |
| `onPriceGrossInputChange` | |
| `onPriceNetInputChange` | |
| `onPriceGrossChange` | |
| `onPriceNetChange` | |
| `convertNetToGross` | |
| `convertGrossToNet` | |
| `requestTaxValue` | |
| `convertPrice` | |
| `keymonitor` | |
| `onCloseModal` | |
| `onPriceGrossChangeDebounce` | |
| `onPriceNetChangeDebounce` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `calculatePriceApiService` | |
| `priceForCurrency` | |
| `attributesWithoutListeners` | |
| `isInherited` | |
| `isDisabled` | |
| `labelGross` | |
| `labelNet` | |
| `grossError` | |
| `netError` | |
| `grossFieldName` | |
| `netFieldName` | |

## Examples

### Example 1
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
    <!--<sw-price-field
        v-else-if="type === 'json_object'"
        class="sw-custom-entity-input-field__price"
        :value="currentValue"
        :label="label"
        :placeholder="placeholder"
        :help-text="helpText"
        @change="onChange"
    />-->

    <!-- ToDo NEXT-22874 - Remove after Debug -->

    <mt-text-field
        v-else
        class="sw-custom-entity-input-field__undefined"
```

### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
        <sw-price-field
            :value="item.price ? item.price : []"
            :default-price="productEntity.price[0]"
            :tax-rate="productEntity.tax"
            :label="false"
            :compact="true"
            :disable-suffix="true"
            enable-inheritance
            :currency="currency"
        />
    </template>

    <template v-else>
        <sw-inheritance-switch
            :is-inherited="item.price === null"
```

### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-price-field
        :value="item.price ? item.price : []"
        :default-price="getDefaultPriceForVariant(item, currency)"
        :tax-rate="productTaxRate"
        :label="false"
        :compact="compact"
        enable-inheritance
        :currency="currency"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_product_variants_overview_data_grid_column_price_preview %}
<template v-else>
```

### Example 4
Source: `sw-product/view/sw-product-detail-context-prices/sw-product-detail-context-prices.html.twig`
```twig
        <sw-price-field
            :value="item.price"
            :default-price="findDefaultPriceOfRule(item)"
            :tax-rate="productTaxRate"
            :label="false"
            :compact="compact"
            :name="`${item.ruleId}-${currency.isoCode}-${item.quantityStart}`"
            :currency="currency"
            :disabled="!acl.can('product.editor')"
        />
    {% endblock %}
    </div>
</template>

<template v-if="showListPrices[priceGroup.ruleId] !== false">
```
