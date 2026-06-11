# sw-cms-section-actions

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| section | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `selectSection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |
| `cmsPageStateStore` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-section-actions
    :section="section"
    :disabled="disabled || undefined"
/>
{% endblock %}

<div
    class="sw-cms-section__wrapper"
    :style="sectionStyles"
>
    <sw-cms-visibility-toggle
        v-if="isVisible"
        :text="toggleButtonText"
        :is-collapsed="isCollapsed"
        :class="expandedClass"
```
