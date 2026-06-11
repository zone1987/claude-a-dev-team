# sw-product-seo-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `fetchVariants` | |
| `getItemName` | |
| `onSearch` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `hasParent` | |
| `hasVariants` | |
| `variantCriteria` | |
| `isCanonicalUrlSelectLoading` | |
| `variantsWithResetOption` | |
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `productKeywordsError` | |
| `productMetaDescriptionError` | |
| `productMetaTitleError` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-seo/sw-product-detail-seo.html.twig`
```twig
    <sw-product-seo-form
        ref="seoForm"
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_seo_urls %}
<sw-seo-url
    v-if="product.seoUrls"
    :has-default-template="false"
    :disabled="!acl.can('product.editor')"
    :urls="product.seoUrls"
    @on-change-sales-channel="onChangeSalesChannel"
```
