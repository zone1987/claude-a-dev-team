# sw-media-breadcrumbs

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentFolderId | `any` | `null` | no |  |
| small | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:currentFolderId | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateFolder` | |
| `onBreadcrumbsItemClicked` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `rootFolder` | |
| `swMediaBreadcrumbsClasses` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-media/component/sw-media-save-modal/sw-media-save-modal.html.twig`
```twig
        <sw-media-breadcrumbs
            v-model:current-folder-id="folderId"
            :small="compact"
            :disabled="isLoading"
        />
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_media_save_modal_media_library %}
    <sw-media-library
        ref="mediaLibrary"
        :selection="[]"
        :folder-id="folderId"
        :compact="compact"
```

### Example 2
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
        <sw-media-breadcrumbs
            v-model:current-folder-id="folderId"
            :small="compact"
        />
        {% endblock %}

        {% block sw_media_modal_v2_search_field %}
        <!-- Bound and updated manually to use debounced search term -->
        <sw-simple-search-field
            :value="term"
            @search-term-change="onSearchTermChange"
        />
        {% endblock %}
    </div>
    {% endblock %}
```
