# sw-order-create-options

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotionCodes | `any` | — | yes |  |
| disabledAutoPromotion | `any` | — | yes |  |
| context | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `updateSameAsBillingAddressToggle` | |
| `createdComponent` | |
| `validatePromotions` | |
| `onToggleAutoPromotion` | |
| `changePromotionCodes` | |
| `updateCartContext` | |
| `updateOrderContext` | |
| `loadCart` | |
| `onChangeShippingCost` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelId` | |
| `salesChannelCriteria` | |
| `shippingMethodCriteria` | |
| `paymentMethodCriteria` | |
| `customer` | |
| `currency` | |
| `cart` | |
| `cartDelivery` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
                <sw-order-create-options
                    v-show="active === 'options'"
                    :disabled="!customer || undefined"
                    :disabled-auto-promotion="disabledAutoPromotion"
                    :promotion-codes="promotionCodes"
                    :context="context"
                    @promotions-change="updatePromotion"
                    @auto-promotion-toggle="updateAutoPromotionToggle"
                    @shipping-cost-change="updateShippingCost"
                />
                {% endblock %}
            </div>
            {% endblock %}
        </template>
    </sw-tabs>
```
