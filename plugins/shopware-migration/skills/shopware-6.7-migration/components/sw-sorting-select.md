# sw-sorting-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sortBy | `any` | `'createdAt'` | no |  |
| sortDirection | `any` | `'DESC'` | no |  |
| additionalSortOptions | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sorting-changed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSortingChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sortOptions` | |
| `sortingConditionConcatenation` | |
| `sortingConditionOptions` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
    <sw-sorting-select
        :sort-by="sortBy"
        :sort-direction="sortDirection"
        @sorting-changed="onSort"
    />
    {% endblock %}

</div>
{% endblock %}

{% block sw_cms_list_listing_actions_mode %}
<div
    class="sw-cms-list__actions-mode"
    role="button"
    tabindex="0"
```

### Example 2
Source: `sw-cms/component/sw-cms-layout-modal/sw-cms-layout-modal.html.twig`
```twig
<sw-sorting-select
    class="sw-cms-layout-modal__header-sorting-select"
    :sort-by="sortBy"
    :sort-direction="sortDirection"
    @sorting-changed="onSort"
/>
{% endblock %}

{% block sw_cms_layout_modal_header_view_toggle %}
<div
    class="sw-cms-layout-modal__actions-mode"
    role="button"
    tabindex="0"
    @click="toggleListMode"
    @keydown.enter="toggleListMode"
```
