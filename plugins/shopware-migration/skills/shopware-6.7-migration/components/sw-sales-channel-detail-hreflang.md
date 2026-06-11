# sw-sales-channel-detail-hreflang

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `domainCriteria` | |

## Examples

### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-detail-hreflang
    v-if="salesChannel && isStorefront"
    :sales-channel="salesChannel"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_options_domains %}
<sw-sales-channel-detail-domains
    v-if="salesChannel && isDomainAware"
    :sales-channel="salesChannel"
    :disable-edit="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
```
