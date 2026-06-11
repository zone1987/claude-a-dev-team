# sw-order-line-items-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| context | `any` | — | yes |  |
| editable | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-edit | — | |
| existing-item-edit | — | |
| item-cancel | — | |
| item-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `createNewOrderLineItem` | |
| `onInsertBlankItem` | |
| `onInsertExistingItem` | |
| `onInsertCreditItem` | |
| `onSelectionChanged` | |
| `onDeleteSelectedItems` | |
| `onDeleteItem` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `itemCreatedFromProduct` | |
| `onSearchTermChange` | |
| `isCreditItem` | |
| `isProductItem` | |
| `isPromotionItem` | |
| `isContainerItem` | |
| `getMinItemPrice` | |
| `showTaxValue` | |
| `checkItemPrice` | |
| `tooltipTaxDetail` | |
| `openNestedLineItemsModal` | |
| `closeNestedLineItemsModal` | |
| `hasChildren` | |
| `hasMultipleTaxes` | |
| `updateItemQuantity` | |
| `refreshChildrenQuantity` | |
| `showTaxRulesInlineEdit` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `canCreateDiscounts` | |
| `orderLineItemRepository` | |
| `orderLineItems` | |
| `lineItemTypes` | |
| `taxStatus` | |
| `unitPriceLabel` | |
| `getLineItemColumns` | |
| `salesChannelId` | |
| `isProductNumberColumnVisible` | |
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

### Example 4
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
<sw-order-line-items-grid
    ref="sw-order-line-item-grid"
    :order="order"
    :context="versionContext"
    :editable="acl.can('order.editor')"
    @item-delete="recalculateAndReload"
    @item-edit="recalculateAndReload"
    @existing-item-edit="saveAndRecalculate"
    @item-cancel="recalculateAndReload"
/>
{% endblock %}

{% block sw_order_detail_general_line_items_summary %}
<sw-card-section
    divider="top"
```
