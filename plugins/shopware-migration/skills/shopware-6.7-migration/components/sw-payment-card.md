# sw-payment-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| paymentMethod | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| set-payment-active | — | |

## Methods

| Method | Description |
|--------|-------------|
| `setPaymentMethodActive` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `previewUrl` | |

## Examples

### Example 1
Source: `sw-settings-payment/page/sw-settings-payment-overview/sw-settings-payment-overview.html.twig`
```twig
            <sw-payment-card
                :key="`default-${card.id}`"
                :payment-method="card.paymentMethod"
                @set-payment-active="togglePaymentMethodActive"
            />
            {% endblock %}
        </template>

    </template>
    {% endblock %}

    {% block sw_settings_payment_overview_empty_state %}
    <mt-empty-state
        v-if="isEmpty"
        :icon="$route.meta.$module.icon"
```
