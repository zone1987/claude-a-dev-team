# sw-media-library

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selection | `any` | — | yes |  |
| folderId | `any` | `null` | no |  |
| pendingUploads | `any` | — | no |  |
| limit | `any` | `25` | no | Valid: `1`, `5`, `25`, `50`, `100`, `500` |
| term | `any` | `''` | no |  |
| compact | `any` | `false` | no |  |
| editable | `any` | `false` | no |  |
| allowMultiSelect | `any` | `true` | no |  |
| allowCreateFolder | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:selection | — | |
| media-folder-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `refreshList` | |
| `isValidTerm` | |
| `loadNextItems` | |
| `mapFolderSorting` | |
| `isLoaderDone` | |
| `loadItems` | |
| `nextMedia` | |
| `nextFolders` | |
| `fetchAssociatedFolders` | |
| `goToParentFolder` | |
| `clearSelection` | |
| `injectItem` | |
| `injectMedia` | |
| `createFolder` | |
| `removeNewFolder` | |
| `refreshItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `shouldDisplayEmptyState` | |
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaFolderConfigurationRepository` | |
| `selectableItems` | |
| `rootFolder` | |
| `gridPresentation` | |
| `showItemsAsList` | |
| `showLoadMoreButton` | |
| `nextMediaCriteria` | |
| `nextFoldersCriteria` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-media/page/sw-media-index/sw-media-index.html.twig`
```twig
    <sw-media-library
        ref="mediaLibrary"
        v-model:selection="selectedItems"
        class="sw-media-index__media-library"
        :folder-id="routeFolderId"
        :pending-uploads="uploads"
        :term="term"
        editable
        @media-folder-change="updateRoute"
    />
    {% endblock %}

    {% block sw_media_index_sidebar %}
    <sw-media-sidebar
        :items="selectedItems"
```

### Example 2
Source: `sw-media/component/sw-media-save-modal/sw-media-save-modal.html.twig`
```twig
    <sw-media-library
        ref="mediaLibrary"
        :selection="[]"
        :folder-id="folderId"
        :compact="compact"
        :disabled="isLoading"
        allow-create-folder
        :allow-multi-select="false"
        @media-folder-change="folderId = $event"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_media_save_modal_modal_footer %}
```

### Example 3
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
    <sw-media-library
        ref="mediaLibrary"
        :selection="selection"
        :folder-id="folderId"
        :term="term"
        :compact="compact"
        :allow-multi-select="allowMultiSelect"
        @update:selection="selection = $event"
        @media-folder-change="folderId = $event"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_media_modal_v2_tab_content_upload %}
```
