# sw-cms-block-config

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| block-delete | — | |
| block-duplicate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSetBackgroundMedia` | |
| `successfulUpload` | |
| `removeMedia` | |
| `onBlockDelete` | |
| `onBlockDuplicate` | |
| `onBlockNameChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `uploadTag` | |
| `mediaRepository` | |
| `cmsPageState` | |
| `cmsBlocks` | |
| `blockConfig` | |
| `quickactionsDisabled` | |
| `duplicateDisabled` | |
| `combinedDuplicateDisabled` | |
| `combinedDuplicateClasses` | |
| `quickactionClasses` | |
| `backgroundModeOptions` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
        <sw-cms-block-config
            :block="selectedBlock"
            @block-delete="onBlockDelete"
            @block-duplicate="onBlockDuplicate"
        />
    </template>
    {% endblock %}
</sw-sidebar-collapse>
{% endblock %}

{% block sw_cms_sidebar_block_layout_settings_content %}
<sw-sidebar-collapse :expand-on-loading="false">

    {% block sw_cms_sidebar_block_layout_settings_header %}
    <template #header>
```
