# sw-image-preview-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaItems | `any` | — | yes |  |
| activeItemId | `any` | `''` | no |  |
| zoomSteps | `any` | `5` | no |  |
| itemPerPage | `any` | `10` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `afterComponentsMounted` | |
| `updatedComponent` | |
| `beforeDestroyComponent` | |
| `destroyedComponent` | |
| `buttonClass` | |
| `getActiveImage` | |
| `loadImage` | |
| `onClickClose` | |
| `onClickZoomIn` | |
| `onClickZoomOut` | |
| `onClickReset` | |
| `onImageSliderChange` | |
| `onThumbnailSliderChange` | |
| `setTransition` | |
| `updateTransform` | |
| `setActionButtonState` | |
| `onMouseWheel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `images` | |
| `maxZoomValue` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-variants-media-upload/sw-product-variants-media-upload.html.twig`
```twig
    <sw-image-preview-modal
        v-if="showPreviewModal"
        :active-item-id="activeItemId"
        :media-items="mediaSource"
        @modal-close="onClosePreviewModal"
    />
    {% endblock %}
</div>
{% endblock %}

```
