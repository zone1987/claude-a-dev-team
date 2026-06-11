# sw-order-line-items-grid-sales-channel

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannelId | `any` | `''` | yes |  |
| cart | `any` | — | yes |  |
| currency | `any` | — | yes |  |
| isCustomerActive | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| title | `any` | `''` | no |  |
| positionIdentifier | `any` | `'sw-order-line-items-grid-sales-channel'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| footer | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-save-item | — | |
| on-remove-items | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `createNewOrderLineItem` | |
| `initLineItem` | |
| `onInsertExistingItem` | |
| `onInsertBlankItem` | |
| `onInsertCreditItem` | |
| `onSelectionChanged` | |
| `onDeleteSelectedItems` | |
| `onDeleteItem` | |
| `itemCreatedFromProduct` | |
| `onSearchTermChange` | |
| `isCreditItem` | |
| `isProductItem` | |
| `getMinItemPrice` | |
| `isPromotionItem` | |
| `isAutoPromotionItem` | |
| `showTaxValue` | |
| `checkItemPrice` | |
| `tooltipTaxDetail` | |
| `hasMultipleTaxes` | |
| `changeItemQuantity` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `orderLineItemRepository` | |
| `cartLineItems` | |
| `lineItemTypes` | |
| `isCartTokenAvailable` | |
| `isAddNewItemButtonDisabled` | |
| `taxStatus` | |
| `unitPriceLabel` | |
| `getLineItemColumns` | |
| `assetFilter` | |
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
                <sw-order-line-items-grid-sales-channel
                    v-show="active === 'products'"
                    :is-loading="isProductGridLoading"
                    :sales-channel-id="salesChannelId"
                    :cart="cart"
                    :currency="currency"
                    :is-customer-active="isCustomerActive"
                    @on-save-item="onSaveItem"
                    @on-remove-items="onRemoveItems"
                />
                {% endblock %}

                {% block sw_order_create_modal_tabs_content_options %}
                <sw-order-create-options
                    v-show="active === 'options'"
```

### Example 2
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
    :title="$tc('sw-order.createBase.generalTab.labelLineItemsCard')"
    editable
    :cart="cart"
    :currency="currency"
    :sales-channel-id="context.salesChannel.id"
    :is-customer-active="isCustomerActive"
    @on-save-item="onSaveItem"
    @on-remove-items="onRemoveItems"
>

    <template #footer>
```

### Example 3
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-line-items-grid-sales-channel
    ref="sw-order-line-item-grid-sales-channel"
    :cart="cart"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    :is-loading="isLoading"
    :is-customer-active="isCustomerActive"
    editable
    @on-save-item="onSaveItem"
    @on-remove-items="onRemoveItems"
/>
{% endblock %}

{% block sw_order_create_base_line_items_summary %}
<sw-card-section
```
