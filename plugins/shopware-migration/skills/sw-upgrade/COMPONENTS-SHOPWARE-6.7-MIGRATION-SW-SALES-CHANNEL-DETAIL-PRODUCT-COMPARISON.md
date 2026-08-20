# sw-sales-channel-detail-product-comparison

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| productExport | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `validateTemplate` | |
| `preview` | |
| `outerCompleterFunction` | |
| `onPreviewClose` | |
| `resetValid` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `editorConfig` | |
| `productExportRepository` | |
| `domainRepository` | |
| `salesChannelRepository` | |
| `mainNavigationCriteria` | |
| `outerCompleterFunctionHeader` | |
| `outerCompleterFunctionBody` | |
| `outerCompleterFunctionFooter` | |

## Examples

### Example 1
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
