# sw-product-image

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaId | `any` | — | yes |  |
| isSpatial | `any` | `false` | no |  |
| isArReady | `any` | `false` | no |  |
| isCover | `any` | `false` | no |  |
| isPlaceholder | `any` | `false` | no |  |
| showCoverLabel | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-product-image-cover | — | |
| sw-product-image-delete | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productImageClasses` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-media-form/sw-product-media-form.html.twig`
```twig
            <sw-product-image
                v-for="mediaItem in mediaItems"
                :key="mediaItem.id"
                v-draggable="{ dragGroup: 'product-media', data: mediaItem, onDragEnter: onMediaItemDragSort }"
                v-droppable="{ dragGroup: 'product-media', data: mediaItem }"
                :is-cover="isCover(mediaItem)"
                :is-spatial="isSpatial(mediaItem)"
                :is-ar-ready="isArReady(mediaItem)"
                :is-placeholder="mediaItem.isPlaceholder"
                :media-id="mediaItem.mediaId"
                :show-cover-label="showCoverLabel"
                @sw-product-image-delete="removeFile(mediaItem)"
                @sw-product-image-cover="markMediaAsCover(mediaItem)"
            />
            {% endblock %}
```
