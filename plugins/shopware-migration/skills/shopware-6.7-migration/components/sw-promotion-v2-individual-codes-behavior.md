# sw-promotion-v2-individual-codes-behavior

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| delete-finish | — | |
| generate-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `onSearchTermChange` | |
| `loadIndividualCodesGrid` | |
| `onSelectionChange` | |
| `onCodeSelectionChange` | |
| `onShowCodeDeleteModal` | |
| `onShowCodeBulkDeleteModal` | |
| `onConfirmCodeDelete` | |
| `onConfirmCodeBulkDelete` | |
| `onCloseDeleteModal` | |
| `onCloseBulkDeleteModal` | |
| `onOpenGenerateCodesModal` | |
| `onGenerateFinish` | |
| `onCloseGenerateCodesModal` | |
| `onOpenAddCodesModal` | |
| `onAddCodes` | |
| `onCloseAddCodesModal` | |
| `routeToCustomer` | |
| `createRoutingErrorNotification` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `promotionRepository` | |
| `customerRepository` | |
| `deleteConfirmText` | |
| `codeColumns` | |
| `assetFilter` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig`
```twig
            <sw-promotion-v2-individual-codes-behavior
                :promotion="promotion"
                @generate-finish="$emit('generate-individual-codes-finish')"
                @delete-finish="$emit('delete-individual-codes-finish')"
            />
            {% endblock %}

        </template>
        {% endblock %}

    </mt-card>
    {% endblock %}

    {% block sw_promotion_detail_custom_field_sets %}
    <mt-card
```
