# sw-product-download-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| isInherited | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-open | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onOpenMedia` | |
| `getFileSize` | |
| `getFileName` | |
| `createdAt` | |
| `onRemoveDownload` | |
| `successfulUpload` | |
| `createDownloadAssociation` | |
| `onUploadFailed` | |
| `removeFile` | |
| `updateMediaItemPositions` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `isStoreLoading` | |
| `isLoading` | |
| `productDownloadRepository` | |
| `productDownloads` | |
| `mediaRepository` | |
| `error` | |
| `hasError` | |
| `swFieldClasses` | |
| `fileAccept` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
    <sw-product-download-form
        v-if="mediaFormVisible"
        :product-id="product.id"
        :label="$tc('sw-product.detailBase.downloadsLabel')"
        :disabled="!acl.can('product.editor')"
        required
        @media-open="onOpenDownloadMediaModal"
    />
</mt-card>

{% block sw_product_detail_base_price_card %}
<mt-card
    v-show="showProductCard('prices')"
    class="sw-product-detail-base__prices"
    position-identifier="sw-product-detail-base-prices"
```
