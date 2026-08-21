# sw-media-media-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-rename-success | — | |
| media-item-play | — | |
| media-item-delete | — | |
| media-folder-move | — | |
| media-item-replaced | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeName` | |
| `handleErrorMessage` | |
| `rejectRenaming` | |
| `onBlur` | |
| `emitPlayEvent` | |
| `copyItemLink` | |
| `openModalDelete` | |
| `closeModalDelete` | |
| `emitItemDeleted` | |
| `openModalReplace` | |
| `closeModalReplace` | |
| `openModalMove` | |
| `closeModalMove` | |
| `onMediaItemMoved` | |
| `emitRefreshMediaLibrary` | |
| `runAppAction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `locale` | |
| `defaultContextMenuClass` | |
| `mediaNameFilter` | |
| `dateFilter` | |
| `fileSizeFilter` | |
| `extensionSdkButtons` | |

## Examples

### Example 1
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
                    <sw-media-media-item
                        v-for="upload in uploads"
                        :key="`sw-media-modal-v2-upload-${upload.id}`"
                        :item="upload"
                        :show-context-menu-button="false"
                        :show-selection-indicator="allowMultiSelect"
                        :allow-multi-select="allowMultiSelect"
                        :selected="checkMediaItem(upload)"
                        :editable="false"
                        :is-list="compact"
                        @media-item-selection-remove="onMediaRemoveSelected"
                        @media-item-selection-add="onMediaAddSelected"
                        @media-item-click="onMediaItemSelect"
                    />
                </sw-media-grid>
```
