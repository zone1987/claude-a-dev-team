# sw-model-editor

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
| `setGizmoMode` | |
| `save` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
                    <sw-model-editor
                        ref="modelEditorRef"
                        :source="item"
                        @save="onSaveComplete"
                    />
                </div>
                <template #modal-footer>
                    <mt-button
                        variant="primary"
                        @click="$refs.modelEditorRef.save()"
                    >
                        {{ $tc('sw-media.sw-model-editor.saveChanges') }}
                    </mt-button>
                </template>
            </sw-modal>
```
