# sw-media-modal-delete

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemsToDelete | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-delete-modal-close | — | |
| media-delete-modal-items-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `closeDeleteModal` | |
| `getEntityRepository` | |
| `_deleteSelection` | |
| `deleteSelection` | |
| `updateSuccessNotification` | |
| `_checkInUsage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaNameFilter` | |
| `snippets` | |
| `mediaQuickInfo` | |
| `mediaInUsages` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
    <sw-media-modal-delete
        v-if="showModalDelete"
        :items-to-delete="[mediaFolder]"
        @media-delete-modal-close="closeModalDelete"
        @media-delete-modal-items-delete="deleteSelectedItems"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-modal-delete
    v-if="showModalDelete"
    :items-to-delete="[item]"
    @media-delete-modal-close="closeModalDelete"
    @media-delete-modal-items-delete="deleteSelectedItems"
/>
{% endblock %}

{% block sw_media_quickinfo_move_modal %}
<sw-media-modal-move
    v-if="showModalMove"
    :items-to-move="[item]"
    @media-move-modal-close="closeModalMove"
    @media-move-modal-items-move="onFolderMoved"
/>
```

### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
    <sw-media-modal-delete
        v-if="showModalDelete"
        :items-to-delete="items"
        @media-delete-modal-close="closeModalDelete"
        @media-delete-modal-items-delete="deleteSelectedItems"
    />
    {% endblock %}

    {% block sw_media_sidebar_folder_dissolve_modal %}
    <sw-media-modal-folder-dissolve
        v-if="!hasMedia && showFolderDissolve"
        :items-to-dissolve="items"
        @media-folder-dissolve-modal-dissolve="onFolderDissolved"
        @media-folder-dissolve-modal-close="closeFolderDissolve"
    />
```
