# sw-media-folder-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaFolder | `any` | — | yes |  |
| editable | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-folder-renamed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeFolderName` | |
| `quickActionClasses` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `createdAt` | |
| `mediaFolderNameError` | |
| `nameItemClasses` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-sidebar/sw-media-sidebar.html.twig`
```twig
    <sw-media-folder-info
        v-else-if="isSingleFile && firstEntity.getEntityName() === 'media_folder'"
        :media-folder="firstEntity"
        :editable="editable"
        v-bind="filteredAttributes"
    />

    <sw-media-quickinfo-multiple
        v-else-if="isMultipleFile"
        :editable="editable"
        :items="items"
        v-bind="filteredAttributes"
    />

    <sw-media-folder-info
```
