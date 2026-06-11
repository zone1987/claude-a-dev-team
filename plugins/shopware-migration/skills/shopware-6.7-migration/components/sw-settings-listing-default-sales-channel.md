# sw-settings-listing-default-sales-channel

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchSalesChannelsSystemConfig` | |
| `displayAdvancedVisibility` | |
| `closeAdvancedVisibility` | |
| `saveSalesChannelVisibilityConfig` | |
| `updateSalesChannel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `salesChannel` | |

## Examples

### Example 1
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
    <sw-settings-listing-default-sales-channel
        ref="defaultSalesChannelCard"
        :is-loading="isLoading"
    />
</mt-card>
{% endblock %}

{% block sw_settings_listing_content_card_view_system_config %}
<sw-system-config
    ref="systemConfig"
    sales-channel-switchable
    domain="core.listing"
    @loading-changed="onLoadingChanged"
>

```

### Example 2
Source: `sw-first-run-wizard/view/sw-first-run-wizard-defaults/sw-first-run-wizard-defaults.html.twig`
```twig
    <sw-settings-listing-default-sales-channel
        ref="defaultSalesChannelCard"
        :is-loading="isLoading"
        @vue:mounted="() => defaultSalesChannelCardLoaded = true"
    />
    {% endblock %}
</div>
{% endblock %}

```
