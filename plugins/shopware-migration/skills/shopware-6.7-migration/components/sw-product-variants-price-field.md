# sw-product-variants-price-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| price | `any` | — | yes |  |
| taxRate | `any` | `null` | no |  |
| currency | `any` | — | yes |  |
| readonly | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| price-lock-change | — | |
| change | — | |
| price-calculate | — | |
| price-gross-change | — | |
| price-net-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onLockSwitch` | |
| `onPriceGrossChange` | |
| `onPriceGrossChangeDebounce` | |
| `onPriceNetChange` | |
| `onPriceNetChangeDebounce` | |
| `convertNetToGross` | |
| `convertGrossToNet` | |
| `requestTaxValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `calculatePriceApiService` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-variants-configurator/sw-product-variants-configurator-prices/sw-product-variants-configurator-prices.html.twig`
```twig
                    <sw-product-variants-price-field
                        :price="getCurrencyOfOption(item, currency.id)"
                        :tax-rate="product.taxId"
                        :currency="currency"
                        compact
                    />
                </template>
                {% endblock %}

                {% block sw_product_variants_configurator_prices_actions %}
                <template
                    #actions="{ item }"
                >
                    {% block sw_product_variants_configurator_prices_actions_items %}
                    <sw-context-menu-item
```
