# sw-media-compact-upload-v2

> Compact variant of the media upload component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowMultiSelect | `any` | `false` | no |  |
| disableDeletionForLastItem | `any` | — | no |  |
| variant | `any` | `'regular'` | no | Valid: `compact`, `regular` |
| source | `null \| null` | `''` | no |  |
| sourceMultiselect | `any` | — | no |  |
| fileAccept | `any` | `'image/*'` | no |  |
| removeButtonLabel | `any` | `''` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| context-menu-items | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| delete-item | — | |
| selection-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `onModalClosed` | |
| `getFileName` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaPreview` | |
| `removeFileButtonLabel` | |
| `isDeletionDisabled` | |
| `mediaNameFilter` | |

## Examples

### Example 1
Source: `sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig`
```twig
<sw-media-compact-upload-v2
    default-folder="product"
    :label="$tc('sw-property.detail.labelMediaUpload')"
    :source="currentOption.mediaId"
    :upload-tag="currentOption.id"
    :disabled="!allowEdit"
    @media-upload-remove-image="removeMedia"
    @selection-change="setMedia"
/>
{% endblock %}

<sw-custom-field-set-renderer
    v-if="showCustomFields"
    :entity="currentOption"
    :sets="customFieldSets"
```

### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
        <sw-media-compact-upload-v2
            :source="section && section.backgroundMedia && section.backgroundMedia.id ? section.backgroundMedia : null"
            :upload-tag="uploadTag"
            :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
            :default-folder="cmsPageState.pageEntityName"
            :allow-multi-select="false"
            @media-upload-remove-image="removeMedia"
            @selection-change="onSetBackgroundMedia"
        />
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

```

### Example 3
Source: `sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig`
```twig
        <sw-media-compact-upload-v2
            :source="block && block.backgroundMedia && block.backgroundMedia.id ? block.backgroundMedia : null"
            :upload-tag="uploadTag"
            :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
            :default-folder="cmsPageState.pageEntityName"
            :allow-multi-select="false"
            @media-upload-remove-image="removeMedia"
            @selection-change="onSetBackgroundMedia"
        />
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

```

### Example 4
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
        <sw-media-compact-upload-v2
            v-if="productDownloadFolderId"
            :button-label="$tc('sw-product.variations.configuratorModal.uploadAllButton')"
            :remove-button-label="$tc('sw-product.variations.configuratorModal.removeAllButton')"
            upload-tag="upload_all"
            private-filesystem
            :source-multiselect="downloadFilesForAllVariants.length > 0 ? downloadFilesForAllVariants : null"
            allow-multi-select
            add-files-on-multiselect
            :target-folder-id="productDownloadFolderId"
            file-accept="*/*"
            @delete-item="(file) => removeFileForAllVariants(file)"
        />
    </div>
</div>
```

### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
                    <sw-media-compact-upload-v2
                        v-if="productDownloadFolderId"
                        :upload-tag="item.productNumber"
                        :disabled="item.type !== 'digital'"
                        private-filesystem
                        allow-multi-select
                        add-files-on-multiselect
                        :source-multiselect="item.downloads.length > 0 ? item.downloads : null"
                        :target-folder-id="productDownloadFolderId"
                        file-accept="*/*"
                        @delete-item="(file) => removeFile(`${file.fileName}.${file.fileExtension}`, item)"
                    />
                </div>
            </template>

```
