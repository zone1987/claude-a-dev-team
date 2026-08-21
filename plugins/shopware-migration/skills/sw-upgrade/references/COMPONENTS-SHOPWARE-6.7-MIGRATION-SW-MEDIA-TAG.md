# sw-media-tag

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| media | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `handleChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-tag
    :disabled="!acl.can('media.editor')"
    :media="item"
/>
{% endblock %}

{% block sw_media_quickinfo_usage %}
<sw-media-collapse
    v-if="editable && item.hasFile"
    :expand-on-loading="true"
    :title="$t('sw-media.sidebar.sections.usage')"
>

    <template #content>
        <sw-media-quickinfo-usage :item="item" />
```
