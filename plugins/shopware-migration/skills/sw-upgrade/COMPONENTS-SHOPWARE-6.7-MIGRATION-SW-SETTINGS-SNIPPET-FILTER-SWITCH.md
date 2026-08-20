# sw-settings-snippet-filter-switch

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | `''` | no |  |
| name | `any` | — | yes |  |
| group | `any` | `null` | no |  |
| borderTop | `any` | `false` | no |  |
| borderBottom | `any` | `false` | no |  |
| type | `any` | `'small'` | no |  |
| value | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| template | — | |
| field | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `fieldClasses` | |

## Examples

### Example 1
Source: `sw-settings-snippet/component/sidebar/sw-settings-snippet-sidebar/sw-settings-snippet-sidebar.html.twig`
```twig
<sw-settings-snippet-filter-switch
    name="emptySnippets"
    group="emptySnippets"
    type="small"
    :value="filterSettings?.emptySnippets"
    :label="$tc('sw-settings-snippet.filter.showOnlyEmpty')"
    @update:value="onChange"
/>
{% endblock %}

{% block sw_settings_snippet_grid_sidebar_filter_custom %}
<sw-settings-snippet-filter-switch
    name="editedSnippets"
    group="editedSnippets"
    type="small"
```

### Example 2
Source: `sw-settings-snippet/component/sidebar/sw-settings-snippet-sidebar/sw-settings-snippet-sidebar.html.twig`
```twig
            <sw-settings-snippet-filter-switch
                group="authorFilter"
                :name="item"
                :value="filterSettings?.[item]"
                :label="item"
                @update:value="onChange"
            />
        </div>
    </template>
</sw-sidebar-collapse>
{% endblock %}

{% block sw_settings_snippet_grid_sidebar_filter_more %}
<sw-sidebar-collapse :expand-on-loading="isExpandedMoreFilters">
    <template #header>
```
