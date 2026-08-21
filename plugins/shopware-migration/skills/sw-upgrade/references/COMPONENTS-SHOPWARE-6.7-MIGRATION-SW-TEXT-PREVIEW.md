# sw-text-preview

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | — | yes |  |
| maximumLength | `any` | — | yes |  |
| modalTitle | `any` | `''` | no |  |
| maximumNewLines | `any` | `0` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `openModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `shortenedText` | |
| `fullText` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-customer-comment/sw-order-customer-comment.html.twig`
```twig
    <sw-text-preview
        :text="customerComment"
        :modal-title="$tc('sw-order.detailCustomerComment.title')"
        :maximum-length="750"
        :maximum-new-lines="5"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```
