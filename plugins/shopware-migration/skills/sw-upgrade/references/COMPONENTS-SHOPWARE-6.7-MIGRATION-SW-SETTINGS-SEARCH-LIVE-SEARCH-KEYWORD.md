# sw-settings-search-live-search-keyword

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | `null` | yes |  |
| searchTerm | `any` | `null` | yes |  |
| highlightClass | `any` | `'sw-settings-search-live-search-keyword__highlight'` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getClass` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `textIsHighlighted` | |
| `parsedSearch` | |
| `parsedMsg` | |

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
