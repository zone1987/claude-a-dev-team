# mt-select

> Dropdown select with single/multi selection, search, and custom rendering.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| prefix | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |
| paginate | — | |
| update:modelValue | — | |
| change | — | |
| item-add | — | |
| item-remove | — | |
| display-values-expand | — | |
| search-term-change | — | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
    <mt-select
        v-model="productSortingKey"
        class="sw-settings-search-live-search__sorting-select"
        value-property="key"
        label-property="translated.label"
        :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSorting')"
        :options="productSortings"
        :disabled="!isSearchEnable || undefined"
        @update:model-value="searchOnStorefront"
    />
</sw-container>
{% endblock %}

{% block sw_settings_search_view_live_search_results %}
<div class="sw-settings-search-live-search__search-results">
```

### Example 2
Source: `sw-extension/component/sw-extension-my-extensions-listing-controls/sw-extension-my-extensions-listing-controls.html.twig`
```twig
    <mt-select
        v-model="selectedSortingOption"
        class="sw-extension-my-extensions-listing-controls__sorting-dropdown"
        small
        :options="sortingOptions"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 3
Source: `sw-property/component/sw-property-detail-base/sw-property-detail-base.html.twig`
```twig
<mt-select
    v-model="propertyGroup.displayType"
    name="sw-field--propertyGroup-displayType"
    validation="required"
    required
    :label="$tc('sw-property.detail.labelDisplayType')"
    :disabled="!allowEdit"
    :options="displayTypeOptions"
/>
{% endblock %}

{% block sw_property_detail_sorting_type %}
<mt-select
    v-model="propertyGroup.sortingType"
    name="sw-field--propertyGroup-sortingType"
```

### Example 4
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
<mt-select
    v-model="section.sizingMode"
    :label="$tc('sw-cms.detail.label.sizingField')"
    :options="sizingModeOptions"
/>
{% endblock %}

{% block sw_cms_sidebar_section_config_sidebar_mobile %}
<mt-select
    v-if="section.type === 'sidebar'"
    v-model="section.mobileBehavior"
    :label="$tc('sw-cms.detail.sidebar.mobile')"
    :options="mobileBehaviorOptions"
/>
{% endblock %}
```

### Example 5
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
        <mt-select
            v-model="section.backgroundMediaMode"
            :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
            :disabled="!section.backgroundMediaId"
            :options="backgroundMediaModeOptions"
        />
        {% endblock %}
        {% endblock %}
    </div>
    {% endblock %}
</div>
{% endblock %}

```
