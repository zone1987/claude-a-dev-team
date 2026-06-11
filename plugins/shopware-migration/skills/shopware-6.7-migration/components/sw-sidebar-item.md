# sw-sidebar-item

> Individual item within a sw-sidebar component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| icon | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| position | `any` | `'top'` | no |  |
| badge | `any` | `0` | no |  |
| hasSimpleBadge | `any` | `false` | no |  |
| badgeType | `any` | `'info'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| headline-content | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| toggle-active | — | |
| close-content | — | |
| click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerToggleActiveListener` | |
| `registerCloseContentListener` | |
| `openContent` | |
| `closeContent` | |
| `sidebarButtonClick` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sidebarItemClasses` | |
| `hasDefaultSlot` | |
| `showContent` | |

## Examples

### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-settings-logging.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 2
Source: `sw-property/page/sw-property-list/sw-property-list.html.twig`
```twig
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-property.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-item
    ref="pageConfigSidebar"
    icon="regular-cog"
    :title="$tc('sw-cms.detail.sidebar.titlePageSettings')"
    :has-simple-badge="hasPageConfigErrors"
    badge-type="error"
    :disabled="page.locked || disabled"
>

    {% block sw_cms_sidebar_page_settings_content %}
    <sw-sidebar-collapse :expand-on-loading="true">

        {% block sw_cms_sidebar_page_settings_header %}
        <template #header>
            <span>{{ $tc('sw-cms.detail.sidebar.headerPageSettings') }}</span>
```

### Example 4
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-item
    ref="blockSelectionSidebar"
    icon="regular-plus-circle"
    :title="addBlockTitle"
    :disabled="currentDeviceView === 'form' || !isSystemDefaultLanguage || page.locked || disabled"
>
    {% block sw_cms_sidebar_block_overview_content %}
    <div class="sw-cms-sidebar__block-overview">

        {% block sw_cms_sidebar_block_overview_category %}
        <div class="sw-cms-sidebar__block-category">
            <mt-select
                v-model="currentBlockCategory"
                :label="$tc('sw-cms.detail.label.blockCategorySelection')"
                :options="cmsBlockCategoriesOptions"
```

### Example 5
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-review.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}

            {% block sw_review_list_sidebar_filter %}
            <sw-sidebar-filter-panel
                entity="product_review"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
```
