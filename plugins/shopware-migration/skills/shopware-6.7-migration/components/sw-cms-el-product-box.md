# sw-cms-el-product-box

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `displaySkeleton` | |
| `mediaUrl` | |
| `altTag` | |
| `displayModeClass` | |
| `verticalAlignStyle` | |
| `assetFilter` | |
| `truncateFilter` | |
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-cms/elements/product-listing/component/sw-cms-el-product-listing.html.twig`
```twig
    <sw-cms-el-product-box
        v-for="index in demoProductCount"
        :key="index"
        :element="getProduct(index)"
    />
</div>

<div class="sw-cms-el-product-listing__pagination">
    <div class="sw-cms-el-product-listing__pagination-entry">
        <mt-icon
            name="regular-chevron-left-xxs"
            size="20px"
        />
    </div>

```

### Example 2
Source: `sw-cms/elements/cross-selling/component/sw-cms-el-cross-selling.html.twig`
```twig
        <sw-cms-el-product-box
            v-for="index in sliderBoxLimit"
            :key="index"
            :element="demoProductElement"
        />
        {% endblock %}
    </template>

    <template v-else>
        {% block sw_cms_element_cross_selling_products %}
        <template
            v-for="(crossSelling, index) in crossSellingProducts"
            :key="index"
        >
            <sw-cms-el-product-box
```

### Example 3
Source: `sw-cms/elements/product-slider/component/sw-cms-el-product-slider.html.twig`
```twig
        <sw-cms-el-product-box
            v-for="index in sliderBoxLimit"
            :key="index"
            :element="demoProductElement"
        />
        {% endblock %}
    </template>

    <template v-else>
        {% block sw_cms_element_product_slider_products %}
        <template
            v-for="(product, index) in element.data.products"
            :key="index"
        >
            <sw-cms-el-product-box
```
