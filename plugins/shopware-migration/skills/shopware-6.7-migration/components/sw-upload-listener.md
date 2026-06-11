# sw-upload-listener

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| uploadTag | `any` | — | yes |  |
| autoUpload | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `convertStoreEventToVueEvent` | |
| `handleError` | |
| `updateSuccessNotification` | |
| `showErrorNotification` | |
| `syncEntitiesAndRunUploads` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

## Examples

### Example 1
Source: `sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig`
```twig
<sw-upload-listener
    :upload-tag="currentOption.id"
    auto-upload
    @media-upload-finish="successfulUpload"
/>
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
```

### Example 2
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
<sw-upload-listener
    :key="category.id + 'uploadListener'"
    :upload-tag="category.id"
    auto-upload
    @media-upload-finish="onSetMediaItem"
/>
<sw-media-upload-v2
    :key="category.id + 'upload'"
    :label="$tc('sw-category.base.menu.imageLabel')"
    variant="regular"
    :disabled="!acl.can('category.editor')"
    :source="mediaItem"
    :upload-tag="category.id"
    :allow-multi-select="false"
    :default-folder="category.getEntityName()"
```

### Example 3
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

        {% block sw_cms_section_config_background_image_position_field %}
        <mt-select
            v-model="section.backgroundMediaMode"
            :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
            :disabled="!section.backgroundMediaId"
            :options="backgroundMediaModeOptions"
        />
        {% endblock %}
        {% endblock %}
```

### Example 4
Source: `sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig`
```twig
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

        {% block sw_cms_block_config_background_image_position_field %}
        <mt-select
            v-model="block.backgroundMediaMode"
            :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
            :disabled="!block.backgroundMediaId"
            :options="backgroundModeOptions"
        />
        {% endblock %}
        {% endblock %}
```

### Example 5
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="onVideoUpload"
        />
        {% endblock %}

        {% block sw_cms_element_video_config_media_modal %}
        <sw-media-modal-v2
            v-if="showMediaModal"
            variant="full"
            :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
            :entity-context="cmsPageState.entityName"
            :allow-multi-select="false"
            :initial-folder-id="cmsPageState.defaultMediaFolderId"
```
