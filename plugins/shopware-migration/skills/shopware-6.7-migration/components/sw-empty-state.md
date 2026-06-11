# sw-empty-state

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | `null` | yes |  |
| subline | `any` | `null` | no |  |
| showDescription | `any` | `true` | no |  |
| color | `any` | `null` | no |  |
| icon | `any` | `null` | no |  |
| absolute | `any` | `true` | no |  |
| emptyModule | `any` | `false` | no |  |
| autoHeight | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| icon | — | |
| actions | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `moduleColor` | |
| `moduleDescription` | |
| `moduleIcon` | |
| `hasActionSlot` | |
| `classes` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-empty-state
    v-if="showEmptyState"
    :title="$tc('sw-settings-search.generalTab.textEmptyStateExcludedSearchTerms')"
    :show-description="false"
    :has-action-slot="true"
    :absolute="false"
    class="sw-empty-state"
>
    <template #icon>
        {% block sw_settings_search_excluded_search_terms_empty_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-search.generalTab.textEmptyStateExcludedSearchTerms')"
        >
        {% endblock %}
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-empty-state
    v-if="isEmpty"
    :title="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
    :show-description="false"
    :has-action-slot="true"
    :absolute="false"
>
    <template #icon>
        {% block sw_settings_search_searchable_content_general_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
        >
        {% endblock %}
    </template>
```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
<sw-empty-state
    v-if="isEmpty"
    :title="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
    :show-description="false"
    :has-action-slot="true"
    :absolute="false"
>
    <template #icon>
        {% block sw_settings_search_searchable_content_customfields_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
        >
        {% endblock %}
    </template>
```

### Example 4
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-empty-state
    v-else
    class="sw-settings-listing-index__sorting-options-empty-state"
    :title="$tc('sw-settings-listing.index.productSorting.emptyState.title')"
    :subline="$tc('sw-settings-listing.index.productSorting.emptyState.subline')"
    :absolute="false"
>

    {% block sw_settings_listing_content_card_view_options_card_empty_state_icon %}
    <template #icon>
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-listing.index.productSorting.emptyState.title')"
        >
    </template>
```

### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-option-criteria-grid/sw-settings-listing-option-criteria-grid.html.twig`
```twig
<sw-empty-state
    v-else
    class="sw-settings-listing-option-criteria-grid__criteria-empty-state"
    title=""
    :subline="$tc('sw-settings-listing.base.criteria.emptyStateSubline')"
>

    {% block sw_settings_listing_option_criteria_card_empty_state_icon %}
    <template #icon>
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            alt=""
        >
    </template>
    {% endblock %}
```
