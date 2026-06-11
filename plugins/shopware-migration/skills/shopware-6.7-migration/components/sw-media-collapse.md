# sw-media-collapse

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `expandButtonClass` | |
| `collapseButtonClass` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-collapse
    v-if="editable"
    :title="$tc('sw-media.sidebar.sections.actions')"
    :expand-on-loading="true"
>

    {% block sw_media_quickinfo_folder_quickactions_content %}
    <template #content>
        <ul class="sw-media-sidebar__quickactions-list">
            {% block sw_media_quickinfo_folder_quickactions_move %}
            <li
                v-tooltip="{
                    message: $tc('sw-privileges.tooltip.warning'),
                    disabled: acl.can('media.editor'),
                    showOnDisabledElements: true
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-collapse
    :expand-on-loading="true"
    :title="$tc('sw-media.sidebar.sections.metadata')"
>

    {% block sw_media_quickinfo_folder_metadata_content %}
    <template #content>
        <dl class="sw-media-sidebar__metadata-list">
            {% block sw_media_quickinfo_folder_metadata_content_base %}
            <sw-media-quickinfo-metadata-item
                class="sw-media-quickinfo-metadata-name"
                :class="nameItemClasses"
                :label-name="$tc('sw-media.sidebar.metadata.name')"
                :truncated="false"
            >
```

### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-collapse
    v-if="editable"
    :title="$t('sw-media.sidebar.sections.actions')"
    :expand-on-loading="true"
>

    <template #content>
        {% block sw_media_quickinfo_quickactions_content %}
        <ul
            :key="item.id"
            class="sw-media-sidebar__quickactions-list"
        >
            {% block sw_media_quickinfo_quickactions_replace %}
            <li
                v-if="!item.private"
```

### Example 4
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-collapse
    v-if="isSpatial"
    :title="$t('sw-media.sidebar.sections.configuration')"
    :expand-on-loading="true"
>
    <template #content>
        <sw-inherit-wrapper
            v-model:value="arReady"
            :inherited-value="defaultArReady"
            @update:value="toggleAR"
        >
            <template #content="props">

                <mt-switch
                    :is-inheritance-field="props.isInheritField"
```

### Example 5
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
<sw-media-collapse
    v-if="editable"
    :title="$tc('sw-media.sidebar.sections.actions')"
    :expand-on-loading="true"
>

    {% block sw_media_quickinfo_multiple_quickactions_content %}
    <template #content>
        <ul class="sw-media-sidebar__quickactions-list">
            {% block sw_media_quickinfo_multiple_quickactions_move %}
            <li
                class="quickaction--move"
                :class="quickActionClasses(!acl.can('media.editor'))"
                role="button"
                tabindex="0"
```
