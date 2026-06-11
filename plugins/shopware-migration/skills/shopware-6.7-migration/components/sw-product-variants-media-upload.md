# sw-product-variants-media-upload

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |
| parentProduct | `any` | — | yes |  |
| isInherited | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getMediaDefaultFolderId` | |
| `isCover` | |
| `markMediaAsCover` | |
| `removeMedia` | |
| `onAddMedia` | |
| `addMedia` | |
| `isExistingMedia` | |
| `onUploadMediaSuccessful` | |
| `isReplacedMedia` | |
| `onUploadMediaFailed` | |
| `previewMedia` | |
| `onClosePreviewModal` | |
| `updateMediaItemPositions` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productMediaRepository` | |
| `product` | |
| `mediaSource` | |
| `cover` | |
| `coverImageSource` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
            <sw-product-variants-media-upload
                :source="item"
                :upload-tag="item.id"
                :is-inherited="isMediaFieldInherited(item)"
                :parent-product="productEntity"
                disabled
            />
        </template>
        {% endblock %}
    </sw-bulk-edit-modal>
</template>
{% endblock %}

{% block sw_product_variant_modal_body_grid_column_name %}
<template #column-name="{item, isInlineEdit}">
```

### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
    <sw-product-variants-media-upload
        :source="item"
        :upload-tag="item.id"
        :is-inherited="isMediaFieldInherited(item)"
        :disabled="isInlineEdit ? isMediaFieldInherited(item) : true"
        :parent-product="productEntity"
    />
    {% endblock %}
    {% endblock %}
</template>
{% endblock %}

{% block sw_product_variant_modal_body_grid_actions %}
<template #actions="{item}">

```

### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-product-variants-media-upload
        :source="item"
        :upload-tag="item.id"
        :is-inherited="isMediaFieldInherited(item)"
        :disabled="isInlineEdit ? isMediaFieldInherited(item) : true"
        :parent-product="product"
    />
    {% endblock %}
    {% endblock %}
</template>
{% endblock %}

<template #column-downloads="{item, isInlineEdit, compact}">
    <sw-upload-listener
        :upload-tag="item.productNumber"
```

### Example 4
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-product-variants-media-upload
        :source="item"
        :upload-tag="item.id"
        :is-inherited="isMediaFieldInherited(item)"
        :parent-product="product"
        disabled
    />
</template>
{% endblock %}

<template #column-downloads="{item, isInlineEdit, compact}">
    <sw-upload-listener
        :upload-tag="item.productNumber"
        auto-upload
        @media-upload-finish="(event) => successfulUpload(event, item)"
```
