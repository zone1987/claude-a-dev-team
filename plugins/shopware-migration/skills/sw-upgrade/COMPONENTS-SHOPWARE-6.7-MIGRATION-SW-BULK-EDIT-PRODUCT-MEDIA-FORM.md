# sw-bulk-edit-product-media-form

> Shopware Administration component.

## Examples

### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-bulk-edit-product-media-form
        :disabled="disabled || undefined"
        @media-open="showMediaModal = true"
    />
    {% endblock %}

    {% block sw_bulk_edit_product_media_modal %}
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
```
