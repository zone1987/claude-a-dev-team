# sw-sales-channel-modal-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productStreamsExist | `any` | `true` | no |  |
| productStreamsLoading | `any` | `false` | no |  |
| addChannelAction | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| grid-channel-add | — | |
| grid-detail-open | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddChannel` | |
| `onOpenDetail` | |
| `isProductComparisonSalesChannelType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelTypeRepository` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal/sw-sales-channel-modal.html.twig`
```twig
<sw-sales-channel-modal-grid
    v-if="!detailType"
    :product-streams-exist="productStreamsExist"
    :product-streams-loading="productStreamsLoading"
    :add-channel-action="addChannelAction"
    @grid-detail-open="onGridOpenDetails"
    @grid-channel-add="onAddChannel"
/>
{% endblock %}

{% block sw_sales_channel_modal_detail %}
<sw-sales-channel-modal-detail
    v-else
    :detail-type="detailType"
/>
```
