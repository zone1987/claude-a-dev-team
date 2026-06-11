# sw-media-preview-v2

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |
| showControls | `any` | `false` | no |  |
| autoplay | `any` | `false` | no |  |
| transparency | `any` | `true` | no |  |
| useThumbnails | `any` | `true` | no |  |
| hideTooltip | `any` | `true` | no |  |
| mediaIsPrivate | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |
| media-preview-play | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `mountedComponent` | |
| `fetchSourceIfNecessary` | |
| `onPlayClick` | |
| `getDataUrlFromFile` | |
| `reloadMediaElement` | |
| `removeUrlPreview` | |
| `showEvent` | |
| `onMediaLibraryItemUpdated` | |
| `getCurrentMediaId` | |
| `ensureVideoCoverMedia` | |
| `getVideoCoverMediaId` | |
| `buildSourceSet` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaPreviewClasses` | |
| `transparencyClass` | |
| `canBeTransparent` | |
| `mimeType` | |
| `mimeTypeGroup` | |
| `isPlayable` | |
| `showUnsupportedFormatWarning` | |
| `isIcon` | |
| `placeholderIcon` | |
| `placeholderIconPath` | |
| `lockIsVisible` | |
| `previewUrl` | |
| `isUrl` | |
| `isFile` | |
| `isRelativePath` | |
| `alt` | |
| `mediaName` | |
| `mediaNameFilter` | |
| `assetFilter` | |
| `sourceSet` | |
| `videoCoverMedia` | |
| `videoCoverPoster` | |
| `hasVideoCover` | |
| `videoPreloadValue` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
                <sw-media-preview-v2
                    class="sw-media-quickinfo__media-preview"
                    :source="item.id"
                    :show-controls="true"
                    :use-thumbnails="false"
                />
            </template>
            {% endblock %}
        </div>
    </template>
    {% endblock %}
</sw-media-collapse>
{% endblock %}

{% block sw_media_quickinfo_metadata %}
```

### Example 2
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
<sw-media-preview-v2 :source="item.cover ? item.cover.media : null" />
```

### Example 3
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
<sw-media-preview-v2 :source="getItemMedia(item)" />
```

### Example 4
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
<sw-media-preview-v2 :source="getItemMedia(item)" />
```

### Example 5
Source: `sw-product/component/sw-product-media-form/sw-product-media-form.html.twig`
```twig
            <sw-media-preview-v2
                :key="cover ? cover.media?.url : product.cover.media?.url"
                class="sw-product-media-form__cover-image"
                :source="cover ? cover.mediaId : product.cover.mediaId"
            />
            {% endblock %}
            <span>{{ $tc('sw-product.mediaForm.coverSubline') }}</span>
        </div>
    </div>
    <div
        v-else
        class="sw-product-media-form__cover-image is--placeholder"
    >
        {{ $tc('sw-product.mediaForm.coverSubline') }}
    </div>
```
