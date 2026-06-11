# sw-cms-inherit-wrapper

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| element | `any` | — | yes |  |
| field | `any` | — | yes |  |
| fieldPath | `any` | — | no |  |
| label | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance:restore | — | |
| inheritance:remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cmsElements` | |
| `baseConfig` | |
| `childConfig` | |
| `runtimeConfig` | |
| `supportsInheritance` | |
| `isInherited` | |
| `fullPath` | |
| `fieldDefaultValue` | |

## Examples

### Example 1
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="boxLayout"
    :element="element"
    :label="$t('sw-cms.elements.productBox.config.label.layoutType')"
>

    <template #default="{ isInherited }">
        <mt-select
            v-model="element.config.boxLayout.value"
            :options="boxLayoutOptions"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
```

### Example 2
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="boxHeadlineLevel"
    :element="element"
    :label="$t('sw-cms.elements.productBox.config.label.headlineLevel')"
>
    <template #default="{ isInherited }">
        <mt-select
            v-model="element.config.boxHeadlineLevel.value"
            :help-text="$t('sw-cms.elements.productBox.config.label.headlineLevelHelp')"
            :options="boxHeadlineLevel"
            :hide-clearable-button="true"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
```

### Example 3
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="media"
    :element="element"
    :label="$t('sw-cms.elements.video.label')"
>
    <template #default="{ isInherited }">
        {% block sw_cms_element_video_config_media_upload %}
        <sw-cms-mapping-field
            v-model:config="element.config.media"
            value-types="entity"
            entity="media"
            :disabled="isInherited"
        >
            <sw-media-upload-v2
                variant="regular"
```

### Example 4
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="autoPlay"
    :element="element"
>
    <template #default="{ isInherited }">
        <mt-switch
            v-model="element.config.autoPlay.value"
            class="sw-cms-el-config-video__checkboxes-auto-play"
            :disabled="isInherited"
            :label="$t('sw-cms.elements.video.config.label.autoPlay')"
            :help-text="$t('sw-cms.elements.video.config.helpText.autoPlay')"
        />
    </template>
</sw-cms-inherit-wrapper>
```

### Example 5
Source: `sw-cms/elements/form/config/sw-cms-el-config-form.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="type"
    :element="element"
    :label="$t('sw-cms.elements.form.config.label.type')"
>
    <template #default="{ isInherited }">
        <mt-select
            v-model="element.config.type.value"
            :options="formTypeOptions"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
```
