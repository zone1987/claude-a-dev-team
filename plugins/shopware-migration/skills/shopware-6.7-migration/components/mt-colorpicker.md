# mt-colorpicker

> Color picker with hex input, alpha channel, and visual color selection.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| update:modelValue | — | |

## Examples

### Example 1
Source: `sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig`
```twig
<mt-colorpicker
    v-model="colorHexCode"
    name="sw-field--currentOption-colorHexCode"
    :disabled="!allowEdit"
    :label="$tc('sw-property.detail.labelOptionColor')"
    :z-index="1000"
/>
{% endblock %}

{% block sw_property_option_detail_media %}
<sw-upload-listener
    :upload-tag="currentOption.id"
    auto-upload
    @media-upload-finish="successfulUpload"
/>
```

### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
<mt-colorpicker
    v-model="section.backgroundColor"
    :label="$tc('sw-cms.detail.label.backgroundColorLabel')"
    :placeholder="$tc('sw-cms.detail.label.backgroundColorField')"
/>
{% endblock %}

{% block sw_cms_section_config_background_image_field %}
<sw-media-compact-upload-v2
    :source="section && section.backgroundMedia && section.backgroundMedia.id ? section.backgroundMedia : null"
    :upload-tag="uploadTag"
    :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
    :default-folder="cmsPageState.pageEntityName"
    :allow-multi-select="false"
    @media-upload-remove-image="removeMedia"
```

### Example 3
Source: `sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig`
```twig
<mt-colorpicker
    v-model="block.backgroundColor"
    :label="$tc('sw-cms.detail.label.backgroundColorLabel')"
    :placeholder="$tc('sw-cms.detail.label.backgroundColorField')"
/>
{% endblock %}

{% block sw_cms_block_config_background_image_field %}
<sw-media-compact-upload-v2
    :source="block && block.backgroundMedia && block.backgroundMedia.id ? block.backgroundMedia : null"
    :upload-tag="uploadTag"
    :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
    :default-folder="cmsPageState.pageEntityName"
    :allow-multi-select="false"
    @media-upload-remove-image="removeMedia"
```

### Example 4
Source: `sw-cms/elements/vimeo-video/config/sw-cms-el-config-vimeo-video.html.twig`
```twig
        <mt-colorpicker
            v-model="element.config.color.value"
            class="sw-cms-el-config-vimeo-video__color"
            :z-index="1001"
            :alpha="false"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
{% endblock %}

{% block sw_cms_element_vimeo_video_config_player_controls %}
<div class="sw-cms-el-config-vimeo-video__player-controls">
    <sw-cms-inherit-wrapper
        field="autoplay"
```
