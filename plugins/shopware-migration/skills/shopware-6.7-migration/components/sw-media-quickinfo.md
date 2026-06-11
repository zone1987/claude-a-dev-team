# sw-media-quickinfo

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| editable | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-rename-success | — | |
| media-item-replaced | — | |
| update:item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchSpatialItemConfig` | |
| `buildAugmentedRealityTooltip` | |
| `loadCustomFieldSets` | |
| `onSave` | |
| `onSaveCustomFields` | |
| `saveFinish` | |
| `copyLinkToClipboard` | |
| `onSubmitTitle` | |
| `onSubmitAltText` | |
| `onChangeFileName` | |
| `handleErrorMessage` | |
| `openModalReplace` | |
| `closeModalReplace` | |
| `emitRefreshMediaLibrary` | |
| `quickActionClasses` | |
| `onRemoveFileNameError` | |
| `toggleAR` | |
| `changeARPlacement` | |
| `runAppAction` | |
| `openModelEditorModal` | |
| `closeModelEditorModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `isMediaObject` | |
| `fileSize` | |
| `createdAt` | |
| `fileNameClasses` | |
| `isSpatial` | |
| `extensionSdkButtons` | |
| `isPlayable` | |
| `showUnsupportedFormatWarning` | |
| `canManageVideoCover` | |
| `editorTooltip` | |
| `deleterTooltip` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
        <sw-media-quickinfo-metadata-item
            class="sw-media-quickinfo-metadata-name"
            :class="nameItemClasses"
            :label-name="$tc('sw-media.sidebar.metadata.name')"
            :truncated="false"
        >
            <sw-confirm-field
                v-if="editable"
                ref="inlineEditFieldName"
                :disabled="!acl.can('media.creator')"
                compact
                :value="mediaFolder.name"
                :error="mediaFolderNameError"
                @input="onChangeFolderName"
            />
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-name"
    :class="fileNameClasses"
    :label-name="$t('sw-media.sidebar.metadata.name')"
    :truncated="false"
>

    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        class="sw-media-quickinfo-metadata-name"
        :disabled="!acl.can('media.editor')"
        compact
        :value="item.fileName"
        :error="fileNameError"
```

### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-alt-field"
    :label-name="$t('sw-media.sidebar.metadata.title')"
    :truncated="false"
>
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldTitle"
        :disabled="!acl.can('media.editor')"
        compact
        :placeholder="placeholder(item, 'title', $t('sw-media.sidebar.metadata.title'))"
        :value="item.title"
        @input="onSubmitTitle"
    />
    <template v-else>
```

### Example 4
Source: `sw-media/component/sidebar/sw-media-sidebar/sw-media-sidebar.html.twig`
```twig
<sw-media-quickinfo
    v-if="isSingleFile && firstEntity.getEntityName() === 'media'"
    :item="firstEntity"
    :editable="editable"
    v-bind="filteredAttributes"
    @update:item="onFirstItemUpdated"
/>

<sw-media-folder-info
    v-else-if="isSingleFile && firstEntity.getEntityName() === 'media_folder'"
    :media-folder="firstEntity"
    :editable="editable"
    v-bind="filteredAttributes"
/>

```
