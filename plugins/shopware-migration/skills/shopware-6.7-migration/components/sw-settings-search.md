# sw-settings-search

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getProductSearchConfigs` | |
| `getDefaultSearchConfig` | |
| `createDefaultSearchConfig` | |
| `createConfigFields` | |
| `onSaveDefaultSearchConfig` | |
| `onChangeLanguage` | |
| `onTabChange` | |
| `onSaveSearchSettings` | |
| `saveFinish` | |
| `fetchSalesChannels` | |
| `unsavedDataLeaveHandler` | |
| `onSalesChannelChanged` | |
| `onLiveSearchResultsChanged` | |
| `onEditChanged` | |
| `onConfirmLeave` | |
| `onCloseLeaveModal` | |
| `onCancelLeaveModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productSearchRepository` | |
| `productSearchFieldRepository` | |
| `productSearchConfigsCriteria` | |
| `productDefaultConfigsCriteria` | |
| `allowSave` | |
| `tooltipSave` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
    <sw-settings-search-example-modal
        v-if="showExampleModal"
        @modal-close="onCloseExampleModal"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_settings_search_view_live_search_sales_channel %}
<sw-single-select
    class="sw-settings-search-live-search__sales-channel-select"
    value-property="id"
    label-property="translated.name"
    :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSalesChannel')"
    :label="$tc('sw-settings-search.liveSearchTab.labelSalesChannelSelect')"
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
                    <sw-settings-search-live-search-keyword
                        :text="(item.name || item.translated.name)"
                        :search-term="liveSearchTerm"
                    />
                </sw-product-variant-info>
            </template>
            {% endblock %}

            {% block sw_settings_search_view_live_search_results_search_grid_score %}
            <template #column-score="{ item }">
                <span class="sw-settings-search-live-search__grid-result__score">
                    {{ Math.round(parseFloat(item.extensions.search._score)) }}
                </span>
            </template>
            {% endblock %}
```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
    <sw-settings-search-example-modal
        v-if="showExampleModal"
        @modal-close="onCloseExampleModal"
    />
    {% endblock %}
    {% endblock %}
</sw-container>
{% endblock %}

{% block sw_settings_search_searchable_content_tabs %}
<sw-tabs
    :default-item="defaultTab"
    position-identifier="sw-settings-search-searchable-content"
>
    <template #default="{ active }">
```

### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-general
                v-if="active === tabNames.generalTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                :field-configs="fieldConfigs"
                @data-load="loadData"
                @config-save="saveConfig"
            />
            {% endblock %}

            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
```

### Example 5
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-search-behaviour
        :is-loading="isLoading"
        :search-behaviour-configs="productSearchConfigs"
    />
    {% endblock %}

    {% block sw_settings_search_searchable_content_card %}
    <sw-settings-search-searchable-content
        :product-search-configs="productSearchConfigs"
        :search-config-id="searchConfigId"
    />
    {% endblock %}

    {% block sw_settings_search_excluded_search_terms_card %}
    <sw-settings-search-excluded-search-terms
```
