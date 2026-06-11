# sw-one-to-many-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| collection | `any` | — | yes |  |
| localMode | `any` | `true` | no |  |
| dataSource | `null \| null` | — | no |  |
| allowDelete | `any` | `true` | no |  |
| tooltipDelete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| more-actions | — | |
| delete-action | item: item | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| load-finish | — | |
| delete-item-failed | — | |
| items-delete-finish | — | |
| column-sort | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `applyResult` | |
| `save` | |
| `revert` | |
| `load` | |
| `deleteItem` | |
| `deleteItems` | |
| `deleteItemsFinish` | |
| `sort` | |
| `paginate` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-one-to-many-grid
    ref="countryStateGrid"
    class="sw-settings-country-state-list__content"
    :is-loading="countryStateLoading"
    :collection="country.states"
    :full-page="undefined"
    :local-mode="country.isNew()"
    :columns="stateColumns"
    :allow-delete="acl.can('country.editor')"
    :tooltip-delete="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('country.editor'),
        showOnDisabledElements: true
    }"
    @selection-change="countryStateSelectionChanged"
```

### Example 2
Source: `sw-property/component/sw-property-option-list/sw-property-option-list.html.twig`
```twig
<sw-one-to-many-grid
    ref="grid"
    :is-loading="isLoading"
    :collection="propertyGroup.options"
    :columns="getGroupColumns()"
    :full-page="false"
    :local-mode="false"
    :allow-inline-edit="allowInlineEdit"
    :sort-by="sortBy"
    :sort-direction="sortDirection"
    @load-finish="checkEmptyState"
    @selection-change="onGridSelectionChanged"
>
    <template #column-name="{ item, isInlineEdit }">
        <template v-if="isInlineEdit">
```

### Example 3
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-discount-type/sw-promotion-v2-settings-discount-type.html.twig`
```twig
<sw-one-to-many-grid
    :collection="discount.promotionDiscountPrices"
    :local-mode="true"
    :columns="currencyPriceColumns"
    :show-selection="false"
    :show-actions="!acl.can('promotion.editor')"
>

    {% block sw_promotion_v2_settings_discount_type_advanced_prices_modal_grid_column_name %}
    <template #column-currency.translated.name="{ item }">
        <p class="sw-promotion-v2-settings-discounts-type__advances-prices-column-name">
            {{ item.currency.translated.name }}
        </p>
    </template>
    {% endblock %}
```

### Example 4
Source: `sw-promotion-v2/component/sw-promotion-discount-component/sw-promotion-discount-component.html.twig`
```twig
<sw-one-to-many-grid
    :collection="discount.promotionDiscountPrices"
    :local-mode="true"
    :columns="currencyPriceColumns"
    :show-selection="false"
    :is-loading="isLoading"
    :show-actions="!isEditingDisabled"
>

    <template #column-currency.translated.name="{ item }">
        <p>{{ item.currency.translated.name }}</p>
    </template>

    <template #column-price="{ item }">
        <mt-number-field
```

### Example 5
Source: `sw-promotion-v2/component/promotion-codes/sw-promotion-v2-individual-codes-behavior/sw-promotion-v2-individual-codes-behavior.html.twig`
```twig
<sw-one-to-many-grid
    ref="individualCodesGrid"
    class="sw-promotion-v2-individual-codes-behavior__grid"
    :is-loading="isGridLoading"
    :collection="promotion.individualCodes"
    :columns="codeColumns"
    :local-mode="false"
    sort-by="code"
    sort-direction="ASC"
    @selection-change="onSelectionChange"
    @items-delete-finish="$emit('delete-finish')"
>

    {% block sw_promotion_v2_individual_codes_behavior_grid_redeemed %}
    <template #column-payload="{ item }">
```
