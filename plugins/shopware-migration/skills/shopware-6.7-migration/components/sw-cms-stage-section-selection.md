# sw-cms-stage-section-selection

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| section-select | — | |

## Methods

| Method | Description |
|--------|-------------|
| `selectSection` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-stage-add-section/sw-cms-stage-add-section.html.twig`
```twig
    <sw-cms-stage-section-selection
        v-if="showSelection"
        @section-select="onAddSection"
    />
    {% endblock %}

    {% block sw_cms_add_section_button %}
    <div
        v-if="!forceChoose"
        class="sw-cms-stage-add-section__button"
        :class="{ 'is--open': showSelection }"
        role="button"
        tabindex="0"
        @click="toggleSelection"
        @keydown.enter="toggleSelection"
```

### Example 2
Source: `sw-cms/component/sw-cms-create-wizard/sw-cms-create-wizard.html.twig`
```twig
<sw-cms-stage-section-selection @section-select="onSectionSelect" />
```
