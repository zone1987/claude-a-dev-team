# sw-promotion-discount-component

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | yes |  |
| discount | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| discount-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onDiscountScopeChanged` | |
| `onDiscountTypeChanged` | |
| `onDiscountValueChanged` | |
| `onMaxValueChanged` | |
| `onClickAdvancedPrices` | |
| `recalculatePrices` | |
| `calculatePrice` | |
| `clearAdvancedPrices` | |
| `isMemberOfCollection` | |
| `onCloseAdvancedPricesModal` | |
| `onShowDeleteModal` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `loadSetGroups` | |
| `loadSorters` | |
| `loadPickers` | |
| `loadRestrictedRules` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `advancedPricesRepo` | |
| `repositoryGroups` | |
| `currencyRepository` | |
| `ruleFilter` | |
| `currencyPriceColumns` | |
| `scopes` | |
| `types` | |
| `valueSuffix` | |
| `maxValueSuffix` | |
| `showMaxValueSettings` | |
| `showAbsoluteAdvancedPricesSettings` | |
| `showMaxValueAdvancedPrices` | |
| `maxValueAdvancedPricesTooltip` | |
| `isEditingDisabled` | |
| `displayAdvancedRuleOption` | |
| `graduationSorters` | |
| `graduationPickers` | |
| `isSetGroup` | |
| `isSet` | |
| `graduationAppliers` | |
| `graduationCounts` | |
| `isPickingModeVisible` | |
| `isMaxUsageVisible` | |
| `promotionDiscountSnippet` | |
| `fieldScopeOptions` | |
| `applyCountOptions` | |
| `maxCountOptions` | |
| `sorterOptions` | |
| `pickerOptions` | |
| `discountTypeOptions` | |

## Examples

### Example 1
Source: `sw-promotion-v2/view/sw-promotion-detail-discounts/sw-promotion-detail-discounts.html.twig`
```twig
        <sw-promotion-discount-component
            v-for="discount in discounts"
            :key="discount.id"
            :promotion="promotion"
            :discount="discount"
            @discount-delete="deleteDiscount"
        />
        {% endblock %}
    </ul>
    {% endblock %}
</div>
{% endblock %}

```
