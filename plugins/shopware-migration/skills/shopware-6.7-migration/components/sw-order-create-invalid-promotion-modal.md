# sw-order-create-invalid-promotion-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| confirm | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `onConfirm` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `invalidPromotionCodes` | |

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
