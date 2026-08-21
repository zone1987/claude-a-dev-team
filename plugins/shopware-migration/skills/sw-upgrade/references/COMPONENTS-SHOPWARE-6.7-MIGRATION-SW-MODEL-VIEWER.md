# sw-model-viewer

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `mountedComponent` | |
| `initializeQuickView` | |
| `disposeQuickView` | |
| `onMediaLibraryItemUpdated` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
    <sw-model-viewer
        :source="item"
    />
</div>

{% block sw_model_editor_modal %}
<sw-modal
    v-if="showModelEditorModal"
    class="sw-model-editor-modal"
    :title="$tc('sw-media.sw-model-editor.titleModal')"
    variant="full"
    @modal-close="closeModelEditorModal()"
>
    <div class="sw-model-editor-modal-wrapper">
        <sw-model-editor
```
