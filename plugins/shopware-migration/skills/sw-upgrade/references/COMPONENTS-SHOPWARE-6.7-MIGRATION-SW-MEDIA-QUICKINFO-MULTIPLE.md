# sw-media-quickinfo-multiple

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| editable | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-selection-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onRemoveItemFromSelection` | |
| `quickActionClassesDelete` | |
| `quickActionClasses` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `itemsIsAvailable` | |
| `getFileSize` | |
| `getFileSizeLabel` | |
| `hasFolder` | |
| `hasMedia` | |
| `isPrivate` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-sidebar/sw-media-sidebar.html.twig`
```twig
        <sw-media-quickinfo-multiple
            v-else-if="isMultipleFile"
            :editable="editable"
            :items="items"
            v-bind="filteredAttributes"
        />

        <sw-media-folder-info
            v-else-if="currentFolder"
            :media-folder="currentFolder"
            :editable="editable"
            v-bind="filteredAttributes"
            @media-folder-renamed="onMediaFolderRenamed"
        />

```
