# sw-price-preview

> Shopware Administration component.

## Computed Properties

| Name | Description |
|------|-------------|
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
    <sw-price-preview
        :value="item.price ? item.price : []"
        :default-price="productEntity.price[0]"
        :tax-rate="productEntity.tax"
        :currency="currency"
    />
</template>
{% endblock %}

{% block sw_product_variant_modal_bulk_edit_modal_column_stock %}
<template #column-stock="{ item }">
    {{ item.stock }}
    <sw-color-badge :variant="stockColorVariantFilter(item.stock)" />
</template>
{% endblock %}
```

### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
        <sw-price-preview
            :value="item.price ? item.price : []"
            :default-price="productEntity.price[0]"
            :tax-rate="productEntity.tax"
            :currency="currency"
        />
    </template>
</template>
{% endblock %}

{% block sw_product_variant_modal_body_grid_column_stock %}
<template #column-stock="{item, isInlineEdit}">

    {% block sw_product_variant_modal_body_grid_column_stock_inline_edit %}
    <mt-number-field
```

### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
        <sw-price-preview
            :key="`else-price-field-${currency.isoCode}`"
            :value="item.price ? item.price : []"
            :default-price="getDefaultPriceForVariant(item, currency)"
            :tax-rate="productTaxRate"
            :currency="currency"
        />
        {% endblock %}
    </template>
    {% endblock %}

</template>
{% endblock %}

{% block sw_product_variants_overview_data_grid_column_stock %}
```

### Example 4
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-price-preview
        :key="`else-price-field-${currency.isoCode}`"
        :value="item.price ? item.price : []"
        :default-price="getDefaultPriceForVariant(item, currency)"
        :tax-rate="productTaxRate"
        :currency="currency"
    />
</template>
{% endblock %}

{% block sw_product_variants_overview_bulk_edit_modal_column_media %}
<template #column-media="{ item }">
    <sw-inheritance-switch
        class="sw-product-variants-overview_media__inherited-icon"
        :is-inherited="isMediaFieldInherited(item)"
```
