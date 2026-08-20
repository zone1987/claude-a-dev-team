# sw-maintain-currencies-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencies | `any` | — | no |  |
| prices | `any` | — | yes |  |
| defaultPrice | `any` | — | yes |  |
| taxRate | `any` | — | yes |  |
| hideListPrices | `any` | `false` | no |  |
| hideRegulationPrices | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-prices | — | |
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCurrencies` | |
| `updateCurrencyCollectionFromCurrencies` | |
| `sortCurrencies` | |
| `convertPrice` | |
| `isCurrencyInherited` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `onCancel` | |
| `onApply` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `maintainCurrencyColumns` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-price-form/sw-product-price-form.html.twig`
```twig
    <sw-maintain-currencies-modal
        v-if="displayMaintainCurrencies"
        variant="full"
        :currencies="currencies"
        :prices="product.price"
        :default-price="defaultPrice"
        :tax-rate="productTaxRate"
        :disabled="!allowEdit || undefined"
        @modal-close="onMaintainCurrenciesClose"
        @update-prices="updatePrices"
    />
    {% endblock %}
</div>
{% endblock %}

```
