# sw-collapse

> Collapsible content panel with animated expand/collapse.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| expandOnLoading | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header | — | |
| content | — | |

## Methods

| Method | Description |
|--------|-------------|
| `collapseItem` | |

## Examples

### Example 1
Source: `sw-settings-language/page/sw-settings-language-list/sw-settings-language-list.html.twig`
```twig
<sw-collapse expand-on-loading>

    {% block sw_settings_language_list_grid_sidebar_filter_header %}
    <template #header="{ expanded }">
        <div class="sw-settings-language-list__collapse-header">

            {% block sw_settings_language_list_grid_sidebar_filter_header_title %}
            <h4 class="sw-settings-language-list__collapse-title">
                {{ $t('sw-settings-language.list.titleSidebarQuickFilter') }}
            </h4>
            {% endblock %}

            {% block sw_settings_language_list_grid_sidebar_filter_header_icon %}
            {% block sw_settings_language_list_grid_sidebar_filter_header_icon_expanded %}
            <mt-icon
```
