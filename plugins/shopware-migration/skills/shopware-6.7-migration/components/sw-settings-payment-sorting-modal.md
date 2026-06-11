# sw-settings-payment-sorting-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| paymentMethods | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| modal-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `applyChanges` | |
| `onSort` | |
| `isShopwareDefaultPaymentMethod` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `paymentMethodRepository` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-settings-payment/page/sw-settings-payment-overview/sw-settings-payment-overview.html.twig`
```twig
        <sw-settings-payment-sorting-modal
            v-if="showSortingModal"
            :payment-methods="paymentMethods"
            @modal-close="showSortingModal = false"
            @modal-save="loadPaymentMethods"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
