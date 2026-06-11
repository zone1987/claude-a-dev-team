# sw-single-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `any` | — | yes |  |
| value | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| labelProperty | `any` | `'label'` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| popoverClasses | `any` | — | no |  |
| searchFunction | `any` | — | no |  |
| disableSearchFunction | `any` | `false` | no |  |
| label | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| item-selected | — | |
| on-open-change | — | |
| before-selection-clear | — | |
| search | — | |
| paginate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `onSelectExpanded` | |
| `tryGetSearchText` | |
| `onSelectCollapsed` | |
| `closeResultList` | |
| `setValue` | |
| `resetActiveItem` | |
| `onInputSearchTerm` | |
| `debouncedSearch` | |
| `search` | |
| `getKey` | |
| `clearSelection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `inputClasses` | |
| `selectionTextClasses` | |
| `singleSelection` | |
| `visibleResults` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-single-select
    class="sw-settings-search-live-search__sales-channel-select"
    value-property="id"
    label-property="translated.name"
    :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSalesChannel')"
    :label="$tc('sw-settings-search.liveSearchTab.labelSalesChannelSelect')"
    :value="salesChannelId"
    :options="salesChannels"
    show-clearable-button
    @update:value="changeSalesChannel"
/>
{% endblock %}

{% block sw_settings_search_view_live_search_input %}
<sw-container
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
        <sw-single-select
            v-model:value="item.field"
            class="sw-settings-search-field-select"
            size="small"
            show-clearable-button
            :options="fieldConfigs"
            @update:value="onSelectField(item)"
        />
        {% endblock %}
    </template>
    <template v-else>
        {% block sw_settings_search_searchable_content_general_field_label %}
        {{ getMatchingFields(item.field) }}
        {% endblock %}
    </template>
```

### Example 3
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type/sw-bulk-edit-change-type.html.twig`
```twig
    <sw-single-select
        v-model:value="currentValue"
        class="sw-bulk-edit-change-type__selection"
        :options="options"
        @update:value="onChangeType"
    />
    {% endblock %}

    {% block sw_bulk_edit_change_type_value_field %}
    <slot
        name="value-field"
        v-bind="{ isDisplayingValue }"
    >
    </slot>
    {% endblock %}
```

### Example 4
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
        <sw-single-select
            class="sw-settings-listing-index__default-sorting-select"
            :placeholder="$tc('sw-settings-listing.general.placeholderDefaultSorting')"
            :disabled="isInherited"
            :value="currentValue"
            :options="productSortingOptions"
            :error="hasDefaultSortingError ? salesChannelDefaultSortingError : null"
            label-property="label"
            value-property="id"
            @update:value="updateCurrentValue"
        />
    </template>
</sw-inherit-wrapper>
{% endblock %}

```

### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-option-criteria-grid/sw-settings-listing-option-criteria-grid.html.twig`
```twig
    <sw-single-select
        :value="selectedCriteria"
        :options="criteriaOptions"
        :placeholder="$tc('sw-settings-listing.base.criteria.selectPlaceholder')"
        value-property="value"
        label-property="label"
        show-clearable-button
        @update:value="onAddCriteria"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_settings_listing_option_criteria_card_grid %}
<sw-data-grid
```
