# sw-product-detail-context-prices

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isSetDefaultPrice | `any` | `false` | no |  |
| canSetLoadingRules | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `sortCurrencies` | |
| `onRuleChange` | |
| `onAddNewPriceGroup` | |
| `onPriceGroupDelete` | |
| `onPriceGroupDuplicate` | |
| `onPriceRuleDelete` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `isPriceFieldInherited` | |
| `convertPrice` | |
| `findRuleById` | |
| `findPricesByRuleId` | |
| `findDefaultPriceOfRule` | |
| `onQuantityEndChange` | |
| `createPriceRule` | |
| `canCreatePriceRule` | |
| `duplicatePriceRule` | |
| `getPriceRuleGroupClass` | |
| `restoreInheritance` | |
| `removeInheritance` | |
| `onChangeShowListPrices` | |
| `getStartQuantityTooltip` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `taxes` | |
| `currencies` | |
| `isLoading` | |
| `defaultCurrency` | |
| `defaultPrice` | |
| `productTaxRate` | |
| `isChild` | |
| `priceRepository` | |
| `ruleRepository` | |
| `priceRuleGroups` | |
| `priceRuleGroupsExists` | |
| `canAddPriceRule` | |
| `emptyPriceRuleExists` | |
| `isLoaded` | |
| `currencyColumns` | |
| `pricesColumns` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <sw-product-detail-context-prices
            :is-set-default-price="true"
            :can-set-loading-rules="false"
        />

        {% block sw_bulk_edit_product_content_advanced_prices_modal_footer %}
        <template #modal-footer>
            <slot name="sw-bulk-edit-modal-cancel">
                <mt-button
                    size="small"
                    variant="secondary"
                    @click="displayAdvancePricesModal = false"
                >
                    {{ $tc('global.default.close') }}
                </mt-button>
```
