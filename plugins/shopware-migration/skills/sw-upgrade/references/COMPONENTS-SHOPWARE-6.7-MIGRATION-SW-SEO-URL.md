# sw-seo-url

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannelId | `any` | `null` | no |  |
| urls | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |
| hasDefaultTemplate | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| resultLimit | `any` | `25` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| seo-additional | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-change-sales-channel | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initSalesChannelCollection` | |
| `initSeoUrlCollection` | |
| `clearDefaultSeoUrls` | |
| `refreshCurrentSeoUrl` | |
| `onSalesChannelChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlCollection` | |
| `currentSeoUrl` | |
| `defaultSeoUrl` | |
| `seoUrlRepository` | |
| `salesChannelRepository` | |
| `isHeadlessSalesChannel` | |
| `seoUrlHelptext` | |
| `hasAdditionalSeoSlot` | |
| `allowInput` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-seo/sw-category-detail-seo.html.twig`
```twig
    <sw-seo-url
        v-if="category.seoUrls"
        :is-loading="isLoading"
        :has-default-template="false"
        :disabled="!acl.can('category.editor')"
        :urls="category.seoUrls"
    />
    {% endblock %}

</div>
{% endblock %}

```

### Example 2
Source: `sw-product/view/sw-product-detail-seo/sw-product-detail-seo.html.twig`
```twig
<sw-seo-url
    v-if="product.seoUrls"
    :has-default-template="false"
    :disabled="!acl.can('product.editor')"
    :urls="product.seoUrls"
    @on-change-sales-channel="onChangeSalesChannel"
>
    {% block sw_product_detail_seo_urls_content %}
    <template #seo-additional="props">
        {% block sw_product_detail_seo_urls_content_seo_additional %}
        <sw-inherit-wrapper
            v-if="product.mainCategories"
            v-model:value="productMainCategory"
            :has-parent="!!parentProduct.id && !!props.currentSalesChannelId && product.categories.length === 0"
            :label="$tc('sw-seo-url.labelMainCategory')"
```

### Example 3
Source: `sw-settings-seo/page/sw-settings-seo/sw-settings-seo.html.twig`
```twig
<sw-seo-url-template-card ref="seoUrlTemplateCard" />
```
