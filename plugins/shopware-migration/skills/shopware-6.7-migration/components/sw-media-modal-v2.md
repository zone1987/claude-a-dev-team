# sw-media-modal-v2

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isOpen | `any` | `true` | no |  |
| initialFolderId | `any` | `null` | no |  |
| entityContext | `any` | `null` | no |  |
| defaultTab | `any` | `'library'` | no | Valid: `upload`, `library` |
| allowMultiSelect | `any` | `true` | no |  |
| fileAccept | `any` | `'image/*'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| media-modal-selection-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `fetchCurrentFolder` | |
| `addResizeListener` | |
| `removeOnResizeListener` | |
| `getComponentWidth` | |
| `onModalRootChange` | |
| `onEmitModalClosed` | |
| `onEmitSelection` | |
| `refreshList` | |
| `onMediaRemoveSelected` | |
| `onMediaAddSelected` | |
| `onMediaItemSelect` | |
| `resetSelection` | |
| `onItemsDeleted` | |
| `onMediaFoldersDissolved` | |
| `onUploadsAdded` | |
| `onUploadFinished` | |
| `onUploadFailed` | |
| `selectMediaItem` | |
| `checkMediaItem` | |
| `onSearchTermChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `tabNameUpload` | |
| `tabNameLibrary` | |
| `hasUploads` | |
| `uploadTag` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 2
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
<sw-media-modal-v2
    v-if="showMediaModal"
    :allow-multi-select="false"
    :entity-context="category.getEntityName()"
    @media-modal-selection-change="onMediaSelectionChange"
    @modal-close="showMediaModal = false"
/>
{% endblock %}

{% block sw_category_detail_menu_description %}
<sw-text-editor
    v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
    :key="category.id + 'description'"
    v-model:value="category.description"
    class="sw-category-detail-base__description"
```

### Example 3
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
<sw-media-modal-v2
    v-if="showMediaModal"
    :caption="$tc('sw-cms.components.cmsListItem.modal.captionMediaUpload')"
    :entity-context="'cms_page'"
    :allow-multi-select="false"
    @media-modal-selection-change="onPreviewImageChange"
    @modal-close="onModalClose"
/>
{% endblock %}

<sw-confirm-modal
    v-if="showLayoutSetAsDefaultModal"
    class="sw-cms-list__confirm-set-as-default-modal"
    :title="$tc('sw-cms.components.setDefaultLayoutModal.title')"
    :text="$tc('sw-cms.components.setDefaultLayoutModal.infoText', {}, newDefaultLayout.type === 'product_detail')"
```

### Example 4
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
        <sw-media-modal-v2
            v-if="showMediaModal"
            variant="full"
            :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
            :entity-context="cmsPageState.entityName"
            :allow-multi-select="false"
            :initial-folder-id="cmsPageState.defaultMediaFolderId"
            file-accept="video/*"
            @media-upload-remove-video="onVideoRemove"
            @media-modal-selection-change="onSelectionChanges"
            @modal-close="onCloseModal"
        />
        {% endblock %}
    </template>
</sw-cms-inherit-wrapper>
```

### Example 5
Source: `sw-cms/elements/youtube-video/config/sw-cms-el-config-youtube-video.html.twig`
```twig
            <sw-media-modal-v2
                v-if="mediaModalIsOpen"
                variant="full"
                :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
                :entity-context="cmsPageState.entityName"
                :allow-multi-select="false"
                :initial-folder-id="cmsPageState.defaultMediaFolderId"
                @media-upload-remove-image="onImageRemove"
                @media-modal-selection-change="onSelectionChanges"
                @modal-close="onCloseModal"
            />
            {% endblock %}
        </template>
    </sw-cms-inherit-wrapper>
    {% endblock %}
```
