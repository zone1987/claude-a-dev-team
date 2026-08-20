# sw-list-price-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| price | `any` | — | yes |  |
| purchasePrices | `any` | — | no |  |
| defaultPrice | `any` | — | no |  |
| label | `any` | `true` | no |  |
| taxRate | `any` | — | yes |  |
| currency | `any` | — | yes |  |
| compact | `any` | `false` | no |  |
| error | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| enableInheritance | `any` | `false` | no |  |
| disableSuffix | `any` | `false` | no |  |
| vertical | `any` | `false` | no |  |
| hideListPrices | `any` | `false` | no |  |
| hidePurchasePrices | `any` | `false` | no |  |
| hideRegulationPrices | `any` | `false` | no |  |
| showSettingPrice | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `listPriceChanged` | |
| `regulationPriceChanged` | |
| `convertPrice` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `priceForCurrency` | |
| `listPrice` | |
| `regulationPrice` | |
| `defaultListPrice` | |
| `defaultRegulationPrice` | |
| `isInherited` | |
| `listPriceHelpText` | |
| `regulationPriceHelpText` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-price-form/sw-product-price-form.html.twig`
```twig
            <sw-list-price-field
                vertical
                :price="currentValue.price"
                :purchase-prices="currentValue.purchasePrices"
                :tax-rate="productTaxRate"
                :disabled="isInherited || !allowEdit || undefined"
                :error="productPriceError ? productPriceError[0] : null"
                :currency="defaultCurrency"
                :show-setting-price="showModeSetting"
            />
        </template>
    </sw-inherit-wrapper>
    {% endblock %}

</sw-container>
```

### Example 2
Source: `sw-product/view/sw-product-detail-context-prices/sw-product-detail-context-prices.html.twig`
```twig
                <sw-list-price-field
                    :price="item.price"
                    :default-price="findDefaultPriceOfRule(item)"
                    :vertical="true"
                    :tax-rate="productTaxRate"
                    :label="false"
                    :compact="compact"
                    :disabled="!acl.can('product.editor')"
                    :currency="currency"
                    hide-purchase-prices
                />
            </div>
        </template>
    </template>
{% endblock %}
```
