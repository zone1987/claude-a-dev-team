# sw-sales-channel-detail-product-comparison-preview

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| content | `any` | `null` | no |  |
| errors | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onModalClose` | |
| `navigateToLine` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `editorConfig` | |
| `displayErrors` | |

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
