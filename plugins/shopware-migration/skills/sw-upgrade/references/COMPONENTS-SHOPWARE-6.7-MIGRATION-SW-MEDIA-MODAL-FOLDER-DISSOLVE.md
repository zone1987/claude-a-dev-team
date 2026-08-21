# sw-media-modal-folder-dissolve

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemsToDissolve | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-folder-dissolve-modal-close | — | |
| media-folder-dissolve-modal-dissolve | — | |

## Methods

| Method | Description |
|--------|-------------|
| `closeDissolveModal` | |
| `_dissolveSelection` | |
| `dissolveSelection` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
    <sw-media-modal-folder-dissolve
        v-if="showFolderDissolve"
        :items-to-dissolve="[mediaFolder]"
        @media-folder-dissolve-modal-dissolve="onFolderDissolved"
        @media-folder-dissolve-modal-close="closeFolderDissolve"
    />
    {% endblock %}

    {% block sw_media_folder_info_move_modal %}
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="[mediaFolder]"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
    <sw-media-modal-folder-dissolve
        v-if="!hasMedia && showFolderDissolve"
        :items-to-dissolve="items"
        @media-folder-dissolve-modal-dissolve="onFolderDissolved"
        @media-folder-dissolve-modal-close="closeFolderDissolve"
    />
    {% endblock %}

    {% block sw_media_sidebar_folder_move_modal %}
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="items"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
```
