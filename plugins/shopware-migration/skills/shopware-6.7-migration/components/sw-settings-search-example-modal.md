# sw-settings-search-example-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |

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
