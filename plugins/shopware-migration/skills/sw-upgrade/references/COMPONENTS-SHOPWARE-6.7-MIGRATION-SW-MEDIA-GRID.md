# sw-media-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| presentation | `any` | `'medium-preview'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| content | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-grid-selection-clear | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `clearSelectionOnClickOutside` | |
| `originatesFromExcludedComponent` | |
| `isEmittedFromChildren` | |
| `emitSelectionCleared` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaColumnDefinitions` | |
| `presentationClass` | |
| `nonDeselectingComponents` | |

## Examples

### Example 1
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-grid
    ref="mediaGrid"
    class="sw-media-library_media-grid"
    :presentation="gridPresentation"
    @media-grid-selection-clear="clearSelection"
>

    {% block sw_media_library_back_to_parent_item %}
    <sw-media-folder-item
        v-if="parentFolder && (!isLoading || selectableItems.length > 0)"
        :allow-edit="acl.can('media.editor')"
        :allow-delete="acl.can('media.deleter')"
        :disabled="disabled"
        class="sw-media-library__parent-folder"
        :item="parentFolder"
```

### Example 2
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
<sw-media-grid
    :presentation="compact ? 'list-preview' : 'medium-preview'"
    :class="{'sw-media-modal-v2__upload-media-grid--compact': compact }"
>
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
```
