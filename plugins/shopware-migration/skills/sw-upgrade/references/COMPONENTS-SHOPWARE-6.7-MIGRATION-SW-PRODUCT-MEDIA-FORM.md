# sw-product-media-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| isInherited | `any` | `false` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-open | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCreated` | |
| `onOpenMedia` | |
| `updateColumnCount` | |
| `getPlaceholderCount` | |
| `createPlaceholderMedia` | |
| `buildProductMedia` | |
| `successfulUpload` | |
| `createMediaAssociation` | |
| `onUploadFailed` | |
| `removeCover` | |
| `isCover` | |
| `isSpatial` | |
| `isArReady` | |
| `removeFile` | |
| `markMediaAsCover` | |
| `onDropMedia` | |
| `onMediaItemDragSort` | |
| `updateMediaItemPositions` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `mediaItems` | |
| `cover` | |
| `isStoreLoading` | |
| `isLoading` | |
| `productMediaRepository` | |
| `mediaRepository` | |
| `productMedia` | |
| `productMediaStore` | |
| `gridAutoRows` | |
| `currentCoverID` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
            <sw-product-media-form
                v-if="mediaFormVisible"
                :key="isInherited"
                :product-id="isInherited ? parentProduct.id : product.id"
                :is-inherited="isInherited"
                :disabled="isInherited || !acl.can('product.editor')"
                @media-open="onOpenMediaModal"
            />
            {% endblock %}

        </mt-card>
        {% endblock %}

    </template>
</sw-inherit-wrapper>
```
