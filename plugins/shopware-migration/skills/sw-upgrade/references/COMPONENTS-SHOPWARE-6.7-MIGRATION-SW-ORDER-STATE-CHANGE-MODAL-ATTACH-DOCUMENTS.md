# sw-order-state-change-modal-attach-documents

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-confirm | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |

## Examples

### Example 1
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
