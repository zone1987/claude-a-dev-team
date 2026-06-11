# sw-order-nested-line-items-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| lineItem | `any` | — | yes |  |
| order | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `enrichNestedLineItems` | |
| `naturalSort` | |
| `onCloseModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `lineItemRepository` | |
| `modalTitle` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-line-items-grid/sw-order-line-items-grid.html.twig`
```twig
    <sw-order-nested-line-items-modal
        v-if="nestedLineItemsModal"
        :line-item="nestedLineItemsModal"
        :order="order"
        @modal-close="closeNestedLineItemsModal"
    />
    {% endblock %}

</sw-container>
{% endblock %}

```
