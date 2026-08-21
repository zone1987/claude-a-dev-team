# sw-settings-tax-provider-sorting-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxProviders | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `applyChanges` | |
| `onSort` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `taxProviderRepository` | |

## Examples

### Example 1
Source: `sw-settings-tax/page/sw-settings-tax-list/sw-settings-tax-list.html.twig`
```twig
            <sw-settings-tax-provider-sorting-modal
                v-if="showSortingModal"
                :tax-providers="taxProviders"
                @modal-close="showSortingModal = false"
                @modal-save="loadTaxProviders"
            />
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
    {% endblock %}
{% endblock %}

```
