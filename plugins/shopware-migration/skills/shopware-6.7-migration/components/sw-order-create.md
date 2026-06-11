# sw-order-create

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `redirectToOrderList` | |
| `saveFinish` | |
| `onSaveOrder` | |
| `fetchPaymentMethodName` | |
| `onCancelOrder` | |
| `showError` | |
| `openInvalidCodeModal` | |
| `closeInvalidCodeModal` | |
| `removeInvalidCode` | |
| `onRemindPaymentModalClose` | |
| `onRemindCustomer` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customer` | |
| `cart` | |
| `invalidPromotionCodes` | |
| `isSaveOrderValid` | |
| `orderValidateErrorMessage` | |
| `paymentMethodRepository` | |
| `showInitialModal` | |

## Examples

### Example 1
Source: `sw-order/page/sw-order-create/sw-order-create.html.twig`
```twig
<sw-order-create-invalid-promotion-modal
    v-if="showInvalidCodeModal"
    @confirm="removeInvalidCode"
    @close="closeInvalidCodeModal"
/>
{% endblock %}

{% block sw_order_create_remind_payment_modal %}
<sw-modal
    v-if="showRemindPaymentModal"
    class="sw-order-create__remind-payment-modal"
    :title="$tc('sw-order.create.remindPaymentModal.title')"
    :is-loading="remindPaymentModalLoading"
    @modal-close="onRemindPaymentModalClose"
>
```

### Example 2
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

### Example 3
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
    <sw-order-create-general-info
        :cart="cart"
        :context="context"
        :is-loading="isLoading"
    />
</mt-card>

<sw-extension-component-section
    position-identifier="sw-order-create-base-line-items__before"
/>

<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
```

### Example 4
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
    :is-loading="isLoading"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    @close="onClosePromotionModal"
    @save="onSavePromotionModal"
/>
{% endblock %}

{% block sw_order_create_details_payment %}
<mt-card
    class="sw-order-create-details__payment"
    position-identifier="sw-order-create-details-payment"
    :title="$tc('sw-order.createBase.detailsTab.labelTransactionCard')"
```

### Example 5
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-create-address-modal
    v-if="showAddressModal"
    :address="address"
    :add-address-modal-title="addAddressModalTitle"
    :edit-address-modal-title="editAddressModalTitle"
    :customer="customer"
    :cart="cart"
    @close-modal="closeModal"
    @set-customer-address="setCustomerAddress"
/>
{% endblock %}

{% block sw_order_create_promotion_modal %}
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
```
