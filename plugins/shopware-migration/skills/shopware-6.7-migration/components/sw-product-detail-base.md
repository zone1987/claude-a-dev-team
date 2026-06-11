# sw-product-detail-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `showProductCard` | |
| `getMediaDefaultFolderId` | |
| `mediaRemoveInheritanceFunction` | |
| `mediaRestoreInheritanceFunction` | |
| `onOpenMediaModal` | |
| `onCloseMediaModal` | |
| `onOpenDownloadMediaModal` | |
| `onCloseDownloadMediaModal` | |
| `onAddMedia` | |
| `addMedia` | |
| `isSpatial` | |
| `isExistingMedia` | |
| `setMediaAsCover` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `customFieldSets` | |
| `loading` | |
| `isLoading` | |
| `showModeSetting` | |
| `productStates` | |
| `productType` | |
| `isDownloadCardVisible` | |
| `mediaFormVisible` | |
| `productMediaRepository` | |
| `mediaDefaultFolderRepository` | |
| `mediaDefaultFolderCriteria` | |

## Examples

### Basic Usage
```twig
<sw-product-detail-base>
    <!-- content -->
</sw-product-detail-base>
```
