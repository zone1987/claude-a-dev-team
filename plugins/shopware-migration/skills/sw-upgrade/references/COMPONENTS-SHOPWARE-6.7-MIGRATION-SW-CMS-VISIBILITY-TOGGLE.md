# sw-cms-visibility-toggle

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | — | yes |  |
| isCollapsed | `any` | — | yes |  |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-visibility-toggle
    v-if="isVisible"
    :text="toggleButtonText"
    :is-collapsed="isCollapsed"
    :class="expandedClass"
    @toggle="toggleVisibility"
/>
{% block sw_cms_section_sidebar %}
<div
    v-if="isSideBarType && (!isCollapsed || !isVisible)"
    class="sw-cms-section__sidebar"
    :class="sectionSidebarClasses"
>

    <template v-if="sideBarEmpty">
```

### Example 2
Source: `sw-cms/component/sw-cms-block/sw-cms-block.html.twig`
```twig
<sw-cms-visibility-toggle
    v-if="isVisible"
    :text="toggleButtonText"
    :is-collapsed="isCollapsed"
    :class="expandedClass"
    @toggle="toggleVisibility"
/>
{% block sw_cms_block_content %}
<div
    v-if="!isCollapsed || !isVisible"
    class="sw-cms-block__content"
    :class="expandedClass"
    :style="blockPadding"
>
    <slot>
```
