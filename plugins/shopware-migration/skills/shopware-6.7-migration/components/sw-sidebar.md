# sw-sidebar

> Side panel container for filters, navigation, or auxiliary content.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| propagateWidth | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `destroyedComponent` | |
| `_isItemRegistered` | |
| `_isAnyItemActive` | |
| `closeSidebar` | |
| `registerSidebarItem` | |
| `setItemActive` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sections` | |
| `sidebarClasses` | |

## Examples

### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
        <sw-sidebar class="sw-settings-logging-list__sidebar">
            {% block sw_settings_logging_list_sidebar_refresh %}
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
        <sw-sidebar>
            {% block sw_property_list_sidebar_refresh_item %}
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
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-sidebar-collapse
    class="sw-category-detail__category-collapse"
    :expand-on-loading="landingPageId === null"
>
    <template #header>

        {% block sw_category_collapse_header %}
        <div
            v-if="categoryCheckedItem > 0"
            class="sw-category-detail__collapse-selected-count"
        >
            {{ $tc(`sw-category.general.treeHeadSelected`, { count: categoryCheckedItem }) }}:
        </div>
        <div
            v-else
```

### Example 4
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-sidebar-collapse
    class="sw-category-detail__landing-page-collapse"
    :expand-on-loading="landingPageId !== null"
>
    <template #header>

        {% block sw_landing_page_collapse_header %}
        <div
            v-if="landingPageCheckedItem > 0"
            class="sw-category-detail__collapse-selected-count"
        >
            {{ $tc(`sw-landing-page.general.treeHeadSelected`, { count: landingPageCheckedItem }) }}:
        </div>
        <div
            v-else
```

### Example 5
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar class="sw-cms-sidebar">

    {% block sw_cms_sidebar_page_settings %}
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

```
