# sw-sidebar-collapse

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| expandChevronDirection | `any` | `'right'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header | expanded: expanded | |
| actions | — | |
| content | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-expanded | — | |

## Methods

| Method | Description |
|--------|-------------|
| `collapseItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `expandButtonClass` | |
| `collapseButtonClass` | |

## Examples

### Example 1
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

### Example 2
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

### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-collapse :expand-on-loading="true">

    {% block sw_cms_sidebar_page_settings_header %}
    <template #header>
        <span>{{ $tc('sw-cms.detail.sidebar.headerPageSettings') }}</span>
    </template>
    {% endblock %}

    {% block sw_cms_sidebar_page_settings_form %}
    <template #content>
        <div class="sw-cms-sidebar__settings">
            {% block sw_cms_sidebar_page_settings_name_field %}

            <mt-text-field
                v-model="page.name"
```

### Example 4
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-collapse :expand-on-loading="true">

    {% block sw_cms_sidebar_block_settings_header %}
    <template #header>
        <span>
            {{ $tc('sw-cms.sidebar.contentMenu.generalSettings') }}
        </span>
    </template>
    {% endblock %}

    {% block sw_cms_sidebar_block_settings_form %}
    <template #content>
        <sw-cms-block-config
            :block="selectedBlock"
            @block-delete="onBlockDelete"
```

### Example 5
Source: `sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig`
```twig
<sw-sidebar-collapse
    v-for="cmsElementGroup in groupedCmsElements"
    :key="cmsElementGroup.title"
    expand-on-loading
    expand-chevron-direction="up"
>
    <template #header>
        {{ $tc(cmsElementGroup.title) }}
    </template>

    <template #content>
        <div class="sw-cms-slot__element-selection">
            {% block sw_cms_slot_content_element_modal_selection_element %}
            <template
                v-for="element in cmsElementGroup.items"
```
