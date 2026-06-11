# sw-media-modal-replace

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemToReplace | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-replace-modal-close | — | |
| media-replace-modal-item-replaced | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onNewUpload` | |
| `emitCloseReplaceModal` | |
| `replaceMediaItem` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-modal-replace
    v-if="showModalReplace"
    :item-to-replace="item"
    @media-replace-modal-item-replaced="emitRefreshMediaLibrary"
    @media-replace-modal-close="closeModalReplace"
/>
{% endblock %}

{% block sw_media_quickinfo_modal_delete %}
<sw-media-modal-delete
    v-if="showModalDelete"
    :items-to-delete="[item]"
    @media-delete-modal-close="closeModalDelete"
    @media-delete-modal-items-delete="deleteSelectedItems"
/>
```
