# sw-order-state-change-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| technicalName | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-leave | — | |
| page-leave-confirm | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onDocsConfirm` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-details-state-card/sw-order-details-state-card.html.twig`
```twig
        <sw-order-state-change-modal
            v-if="showStateChangeModal"
            :order="order"
            :is-loading="isLoading"
            :technical-name="''"
            @page-leave="onLeaveModalClose"
            @page-leave-confirm="onLeaveModalConfirm"
        />
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_order_state_change_card_divider %}
    <hr class="sw-order-detail-state-card__divider">
    {% endblock %}
```

### Example 2
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
<sw-order-state-change-modal
    v-if="showModal"
    :order="order"
    :is-loading="isLoading"
    :technical-name="technicalName"
    @page-leave="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}
{% block sw_order_state_history_card_container %}
<sw-container
    columns="repeat(auto-fit, minmax(250px, 1fr))"
    gap="30px 30px"
>
    {% block sw_order_state_history_card_transaction %}
```

### Example 3
Source: `sw-order/component/sw-order-general-info/sw-order-general-info.html.twig`
```twig
<sw-order-state-change-modal
    v-if="showModal"
    :order="order"
    :is-loading="isLoading"
    :technical-name="''"
    @page-leave="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}

{% block sw_order_detail_base_general_info_order_states %}
<div class="sw-order-general-info__order-states">
    {% block sw_order_detail_base_general_info_order_states_payment %}
    <div
        v-if="transaction"
```

### Example 4
Source: `sw-order/component/sw-order-state-change-modal/sw-order-state-change-modal.html.twig`
```twig
    <sw-order-state-change-modal-attach-documents
        :order="order"
        :is-loading="isLoading"
        @on-confirm="onDocsConfirm"
    />
    {% endblock %}
</sw-modal>
{% endblock %}

```
