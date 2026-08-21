# sw-order-create-details-footer

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cart | `any` | — | yes |  |
| customer | `any` | `null` | no |  |
| isCustomerActive | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `updateContext` | |
| `updateOrderContext` | |
| `updateCustomerContext` | |
| `getCart` | |
| `getCurrency` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `context` | |
| `salesChannelId` | |
| `salesChannelCriteria` | |
| `paymentMethodCriteria` | |
| `currencyRepository` | |
| `currentCurrencyId` | |
| `defaultSalesChannel` | |
| `isCartTokenAvailable` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
                <sw-order-create-details-footer
                    :customer="customer"
                    :is-customer-active="isCustomerActive"
                    :cart="cart"
                    @loading-change="updateLoading"
                />
                {% endblock %}
            </sw-card-section>
        </sw-container>
    </template>
</mt-card>
{% endblock %}

{% block sw_order_create_base_line_items_card %}
<mt-card
```
