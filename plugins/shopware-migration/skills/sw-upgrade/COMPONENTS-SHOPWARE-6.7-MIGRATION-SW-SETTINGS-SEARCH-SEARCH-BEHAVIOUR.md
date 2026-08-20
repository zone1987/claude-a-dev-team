# sw-settings-search-search-behaviour

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchBehaviourConfigs | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `conditionsOptions` | |

## Examples

### Example 1
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
