# sw-product-stream-modal-preview

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filters | `any` | — | yes |  |
| defaultLimit | `any` | `25` | no |  |
| defaultSorting | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |
| `onSalesChannelChange` | |
| `loadEntityData` | |
| `loadSalesChannels` | |
| `mapFiltersForSearch` | |
| `closeModal` | |
| `getPriceForDefaultCurrency` | |
| `onPageChange` | |
| `loadSalesChannelById` | |
| `isNotEqualToAnyType` | |
| `addRandomSort` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `salesChannelCriteria` | |
| `previewCriteria` | |
| `previewSelectionCriteria` | |
| `productColumns` | |
| `currencyFilter` | |
| `stockColorVariantFilter` | |

## Examples

### Example 1
Source: `sw-cms/elements/product-slider/config/sw-cms-el-config-product-slider.html.twig`
```twig
<sw-product-stream-modal-preview
    v-if="showProductStreamPreview"
    :filters="productStream.apiFilter"
    :default-limit="element.config.productStreamLimit.value"
    :default-sorting="element.config.productStreamSorting.value"
    @modal-close="onCloseProductStreamModal"
/>

<sw-container
    columns="1fr 1fr"
    gap="30px"
>
    {% block sw_cms_element_product_slider_config_content_product_stream_sorting %}
    <sw-cms-inherit-wrapper
        field="productStreamSorting"
```

### Example 2
Source: `sw-product/component/sw-product-cross-selling-form/sw-product-cross-selling-form.html.twig`
```twig
        <sw-product-stream-modal-preview
            v-if="showModalPreview"
            ref="modalPreview"
            :filters="productStreamFilterTree"
            @modal-close="closeModalPreview"
        />
        {% endblock %}
    </div>
</mt-card>
{% endblock %}

{% block sw_product_detail_cross_selling_form_modal_delete %}
<sw-modal
    v-if="showDeleteModal"
    variant="small"
```

### Example 3
Source: `sw-product-stream/page/sw-product-stream-detail/sw-product-stream-detail.html.twig`
```twig
                <sw-product-stream-modal-preview
                    v-if="showModalPreview"
                    ref="modalPreview"
                    :filters="productStreamFiltersTree"
                    @modal-close="closeModalPreview"
                />
                {% endblock %}

                {% block sw_prouct_stream_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-product-stream-detail-custom-field-sets"
                    :large="true"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                >
```
