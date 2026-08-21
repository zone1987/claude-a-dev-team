# sw-cms-el-config-image-gallery

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `initGalleryItems` | |
| `initConfig` | |
| `updateColumnWidth` | |
| `onOpenMediaModal` | |
| `onCloseMediaModal` | |
| `onImageUpload` | |
| `getMediaItem` | |
| `onItemRemove` | |
| `onMediaSelectionChange` | |
| `updateMediaDataValue` | |
| `onItemSort` | |
| `onChangeMinHeight` | |
| `onChangeDisplayMode` | |
| `onChangeUseFetchPriorityOnFirstItem` | |
| `emitUpdateEl` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `uploadTag` | |
| `defaultFolderName` | |
| `sliderItems` | |
| `sliderItemsConfigValue` | |
| `gridAutoRows` | |
| `isProductPage` | |
| `displayModeValueOptions` | |
| `verticalAlignValueOptions` | |
| `navigationArrowsValueOptions` | |
| `navigationDotsValueOptions` | |
| `galleryPositionValueOptions` | |

## Examples

### Basic Usage
```twig
<sw-cms-el-config-image-gallery>
    <!-- content -->
</sw-cms-el-config-image-gallery>
```
