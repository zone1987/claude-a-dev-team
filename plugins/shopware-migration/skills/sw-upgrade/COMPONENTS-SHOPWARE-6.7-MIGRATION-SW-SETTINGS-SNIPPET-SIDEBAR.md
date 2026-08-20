# sw-settings-snippet-sidebar

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filterItems | `any` | — | yes |  |
| authorFilters | `any` | — | yes |  |
| filterSettings | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-sidebar-close | — | |
| sw-sidebar-open | — | |
| change | — | |
| sw-sidebar-collaps-refresh-grid | — | |
| sidebar-reset-all | — | |

## Methods

| Method | Description |
|--------|-------------|
| `closeContent` | |
| `onChange` | |
| `onRefresh` | |
| `resetAll` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `activeFilterNumber` | |
| `isExpandedAuthorFilters` | |
| `isExpandedMoreFilters` | |

## Examples

### Example 1
Source: `sw-settings-snippet/page/sw-settings-snippet-list/sw-settings-snippet-list.html.twig`
```twig
        <sw-settings-snippet-sidebar
            class="sw-settings-snippet-list__grid-sidebar"
            :filter-items="filterItems"
            :author-filters="authorFilters"
            :filter-settings="filterSettings"
            @sidebar-reset-all="onResetAll"
            @change="onChange"
            @sw-sidebar-collaps-refresh-grid="getList"
            @sw-sidebar-close="onSidebarClose"
        />
        {% endblock %}
    </template>

    {% endblock %}

```
