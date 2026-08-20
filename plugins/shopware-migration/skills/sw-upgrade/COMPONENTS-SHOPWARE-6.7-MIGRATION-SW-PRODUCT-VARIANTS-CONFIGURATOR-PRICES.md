# sw-product-variants-configurator-prices

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `mountedComponent` | |
| `loadCurrencies` | |
| `getOptionsForGroup` | |
| `resetSurcharges` | |
| `getCurrencyOfOption` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currencyRepository` | |
| `currenciesList` | |
| `optionColumns` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
    <sw-product-variants-configurator-prices
        v-if="activeTab == 'prices'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

    {% block sw_product_modal_variant_generation_main_configurator_restrictions %}
    <sw-product-variants-configurator-restrictions
        v-if="activeTab == 'restrictions'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
```
