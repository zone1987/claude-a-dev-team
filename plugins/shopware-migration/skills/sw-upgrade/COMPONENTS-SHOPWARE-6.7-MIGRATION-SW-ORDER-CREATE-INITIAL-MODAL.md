# sw-order-create-initial-modal

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `onCloseModal` | |
| `onPreviewOrder` | |
| `onSaveItem` | |
| `addPromotionCodes` | |
| `updatePromotion` | |
| `onRemoveItems` | |
| `updateAutoPromotionToggle` | |
| `updateShippingCost` | |
| `updateOrderContext` | |
| `disableAutoAppliedPromotions` | |
| `modifyShippingCost` | |
| `cancelCart` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelId` | |
| `salesChannelContext` | |
| `currency` | |
| `cart` | |
| `customer` | |
| `isCustomerActive` | |
| `promotionCodeItems` | |
| `cartDelivery` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-initial/sw-order-create-initial.html.twig`
```twig
    <sw-order-create-initial-modal
        v-if="routeCustomerReady"
        @modal-close="onCloseCreateModal"
        @order-preview="onPreviewOrder"
    />
    <sw-loader v-else />
</div>
{% endblock %}

```
