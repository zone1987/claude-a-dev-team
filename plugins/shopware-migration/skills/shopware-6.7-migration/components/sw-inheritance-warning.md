# sw-inheritance-warning

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | yes |  |

## Examples

### Example 1
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
<sw-inheritance-warning
    v-if="isChild"
    :name="$tc('sw-product.general.inheritanceModuleName')"
/>
{% endblock %}

{% block sw_product_detail_content_tabs %}
<sw-tabs
    v-if="productId"
    class="sw-product-detail-page__tabs"
    position-identifier="sw-product-detail"
>
    {% block sw_product_detail_content_tabs_general %}
    <sw-tabs-item
        class="sw-product-detail__tab-general"
```
