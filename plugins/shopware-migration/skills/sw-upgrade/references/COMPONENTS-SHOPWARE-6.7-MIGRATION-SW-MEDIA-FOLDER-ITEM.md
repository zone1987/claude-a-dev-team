# sw-media-folder-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isParent | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-folder-remove | — | |
| media-folder-changed | — | |
| media-folder-delete | — | |
| media-folder-dissolve | — | |
| media-folder-move | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getIconConfigFromFolder` | |
| `onChangeName` | |
| `onBlur` | |
| `rejectRenaming` | |
| `navigateToFolder` | |
| `openSettings` | |
| `closeSettings` | |
| `openDissolveModal` | |
| `closeDissolveModal` | |
| `openDeleteModal` | |
| `closeDeleteModal` | |
| `emitItemDeleted` | |
| `onFolderDissolved` | |
| `onFolderMoved` | |
| `openMoveModal` | |
| `closeMoveModal` | |
| `refreshIconConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaDefaultFolderRepository` | |
| `moduleFactory` | |
| `mediaFolder` | |
| `iconName` | |
| `assetFilter` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-folder-item
    v-if="parentFolder && (!isLoading || selectableItems.length > 0)"
    :allow-edit="acl.can('media.editor')"
    :allow-delete="acl.can('media.deleter')"
    :disabled="disabled"
    class="sw-media-library__parent-folder"
    :item="parentFolder"
    :show-selection-indicator="false"
    :show-context-menu-button="false"
    :allow-multi-select="allowMultiSelect"
    :is-list="showItemsAsList"
    is-parent
    @media-item-click="goToParentFolder"
/>
{% endblock %}
```
