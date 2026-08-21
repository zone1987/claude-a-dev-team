# sw-settings-search-live-search

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentSalesChannelId | `any` | `null` | no |  |
| searchTerms | `any` | `null` | no |  |
| searchResults | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| live-search-results-change | — | |
| sales-channel-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `searchOnStorefront` | |
| `fetchSalesChannels` | |
| `fetchProductSortings` | |
| `changeSalesChannel` | |
| `onShowExampleModal` | |
| `onCloseExampleModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `productSortingRepository` | |
| `isSearchEnable` | |
| `searchColumns` | |
| `products` | |
| `productSortingCriteria` | |
| `searchParams` | |

## Examples

### Example 1
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

### Example 2
Source: `sw-settings-search/view/sw-settings-search-view-live-search/sw-settings-search-view-live-search.html.twig`
```twig
    <sw-settings-search-live-search
        v-bind="$props"
    />
    {% endblock %}
</div>
{% endblock %}

```
