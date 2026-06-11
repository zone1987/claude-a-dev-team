# sw-sales-channel-detail

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadSalesChannel` | |
| `getLoadSalesChannelCriteria` | |
| `onTemplateSelected` | |
| `onTemplateModalClose` | |
| `onTemplateModalConfirm` | |
| `loadCustomFieldSets` | |
| `generateAccessUrl` | |
| `loadProductExportTemplates` | |
| `saveFinish` | |
| `setInvalidFileName` | |
| `onSave` | |
| `updateAnalytics` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `productExport` | |
| `isStorefront` | |
| `isProductComparison` | |
| `isHeadless` | |
| `salesChannelRepository` | |
| `salesChannelAnalyticsRepository` | |
| `customFieldRepository` | |
| `productExportRepository` | |
| `storefrontSalesChannelCriteria` | |
| `tooltipSave` | |
| `allowSaving` | |

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

### Example 2
Source: `sw-sales-channel/view/sw-sales-channel-detail-product-comparison/sw-sales-channel-detail-product-comparison.html.twig`
```twig
            <sw-sales-channel-detail-product-comparison-preview
                :content="previewContent"
                :errors="previewErrors"
                @close="onPreviewClose"
            />
            {% endblock %}
        </div>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```
