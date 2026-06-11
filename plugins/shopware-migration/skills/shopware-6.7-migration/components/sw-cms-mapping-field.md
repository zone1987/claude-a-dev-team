# sw-cms-mapping-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| config | `any` | — | yes |  |
| valueTypes | `null \| null` | `'string'` | no |  |
| entity | `any` | `null` | no |  |
| label | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| preview | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateMappingTypes` | |
| `updateDemoValue` | |
| `onMappingSelect` | |
| `onMappingRemove` | |
| `getAllowedMappingTypes` | |
| `getDemoValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isMapped` | |
| `hasPreview` | |
| `cmsPageState` | |

## Examples

### Example 1
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.media"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        file-accept="video/*"
```

### Example 2
Source: `sw-cms/elements/youtube-video/config/sw-cms-el-config-youtube-video.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.previewMedia"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
```

### Example 3
Source: `sw-cms/elements/image/config/sw-cms-el-config-image.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.media"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
```

### Example 4
Source: `sw-cms/elements/vimeo-video/config/sw-cms-el-config-vimeo-video.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.previewMedia"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$tc('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
```

### Example 5
Source: `sw-cms/elements/text/config/sw-cms-el-config-text.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.content"
    value-types="string"
    :disabled="isInherited"
>
    <sw-text-editor
        v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        :key="isInherited"
        :value="element.config.content.value"
        :disabled="isInherited"
        :allow-inline-data-mapping="true"
        :sanitize-info-warn="true"
        enable-transparent-background
        @update:value="onInput"
        @blur="onBlur"
```
