# sw-media-modal-move

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemsToMove | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-move-modal-close | — | |
| media-move-modal-items-move | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `closeMoveModal` | |
| `isNotPartOfItemsToMove` | |
| `updateParentFolder` | |
| `fetchParentFolder` | |
| `onSelection` | |
| `_moveSelection` | |
| `moveSelection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaNameFilter` | |
| `targetFolderId` | |
| `rootFolderName` | |
| `isMoveDisabled` | |
| `startFolderId` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="[mediaFolder]"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
    {% endblock %}

    {% block sw_media_folder_info_modal_delete %}
    <sw-media-modal-delete
        v-if="showModalDelete"
        :items-to-delete="[mediaFolder]"
        @media-delete-modal-close="closeModalDelete"
        @media-delete-modal-items-delete="deleteSelectedItems"
    />
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-modal-move
    v-if="showModalMove"
    :items-to-move="[item]"
    @media-move-modal-close="closeModalMove"
    @media-move-modal-items-move="onFolderMoved"
/>
{% endblock %}

{% block sw_media_quickinfo_cover_modal %}
<sw-media-modal-v2
    v-if="showCoverSelectionModal"
    :allow-multi-select="false"
    file-accept="image/*"
    @modal-close="closeCoverSelectionModal"
    @media-modal-selection-change="onCoverSelectionChange"
```

### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="items"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
    {% endblock %}
</div>
{% endblock %}


```
