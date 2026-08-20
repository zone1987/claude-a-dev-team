# sw-media-list-selection-item-v2

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| hideActions | `any` | `false` | no |  |
| hideTooltip | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |
| item-remove | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isPlaceholder` | |
| `productImageClasses` | |
| `sourceId` | |

## Examples

### Example 1
Source: `sw-cms/elements/image-gallery/component/sw-cms-el-image-gallery.html.twig`
```twig
            <sw-media-list-selection-item-v2
                v-if="index < galleryLimit"
                :item="sliderItem.media"
                :class="activeMediaClass(sliderItem.media)"
                hide-actions
                hide-tooltip
                @click="onChangeGalleryImage(sliderItem.media, index)"
            />
        </template>
        {% endblock %}
    </div>
</template>

<template v-else>
    {% block sw_cms_element_image_gallery_empty %}
```
