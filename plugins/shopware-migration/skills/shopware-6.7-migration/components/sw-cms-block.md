# sw-cms-block

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |
| active | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| hasWarnings | `any` | `false` | no |  |
| hasErrors | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| block-overlay-click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlockOverlayClick` | |
| `toggleVisibility` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customBlockClass` | |
| `blockStyles` | |
| `blockPadding` | |
| `overlayClasses` | |
| `toolbarClasses` | |
| `assetFilter` | |
| `isVisible` | |
| `toggleButtonText` | |
| `expandedClass` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-block
    class="sw-cms-stage-block"
    :block="block"
    :disabled="disabled || undefined"
    :active="selectedBlock !== null && selectedBlock.id === block.id"
    :has-errors="hasBlockErrors(block)"
    @block-overlay-click="onBlockSelection(block)"
>

    {% block sw_cms_section_sidebar_block_component %}
    <component
        :is="getBlockComponent(block.type)"
        :block="block"
    >
        {% block sw_cms_section_content_block_slot %}
```

### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-block
    class="sw-cms-stage-block"
    :block="block"
    :disabled="disabled || undefined"
    :active="selectedBlock !== null && selectedBlock.id === block.id"
    :has-errors="hasBlockErrors(block)"
    @block-overlay-click="onBlockSelection(block)"
>

    {% block sw_cms_section_content_block_component %}
    <component
        :is="getBlockComponent(block.type)"
        :block="block"
    >
        {% block sw_cms_section_content_block_component_slot %}
```

### Example 3
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
