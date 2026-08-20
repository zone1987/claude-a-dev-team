# sw-cms-stage-add-block

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| stage-block-add | — | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-stage-add-block
    v-if="isSystemDefaultLanguage && !disabled"
    :key="0"
    v-droppable="{ dragGroup: 'cms-stage', data: getDropData(0, 'sidebar') }"
    @stage-block-add="onAddSectionBlock"
/>
{% endblock %}

<template
    v-for="(block, index) in sideBarBlocks"
    :key="block.id"
>
    {% block sw_cms_section_sidebar_block %}
    <sw-cms-block
        class="sw-cms-stage-block"
```

### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
            <sw-cms-stage-add-block
                v-if="isSystemDefaultLanguage && !disabled"
                :key="index + 1"
                v-droppable="{ dragGroup: 'cms-stage', data: getDropData(block.position + 1, 'sidebar') }"
                @stage-block-add="onAddSectionBlock"
            />
            {% endblock %}
        </template>
    </template>
</div>
{% endblock %}

{% block sw_cms_section_content %}
<div
    v-if="!isCollapsed || !isVisible"
```
