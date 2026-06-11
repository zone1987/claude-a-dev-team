# sw-settings-search-search-index

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `getLatestProductKeywordIndexed` | |
| `getTotalProduct` | |
| `updateProgress` | |
| `pollData` | |
| `clearPolling` | |
| `rebuildSearchIndex` | |
| `buildFinish` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productSearchKeywordRepository` | |
| `productCriteria` | |
| `productSearchKeywordsCriteria` | |

## Examples

### Example 1
Source: `sw-settings-search/view/sw-settings-search-view-live-search/sw-settings-search-view-live-search.html.twig`
```twig
    <sw-settings-search-search-index
        v-if="!storefrontEsEnable"
        :is-loading="isLoading"
    />

    {% block sw_settings_search_view_live_search_content_card %}
    <sw-settings-search-live-search
        v-bind="$props"
    />
    {% endblock %}
</div>
{% endblock %}

```
