# sw-sales-channel-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onGridOpenDetails` | |
| `onCloseModal` | |
| `onAddChannel` | |
| `openRoute` | |
| `isProductComparisonSalesChannelType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `productStreamRepository` | |
| `addChannelAction` | |

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

### Example 2
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
<sw-sales-channel-modal
    v-if="showModal"
    @modal-close="showModal=false"
/>
{% endblock %}

{% block sw_sales_channel_menu_headline %}
<div class="sw-admin-menu__headline">
    {% block sw_sales_channel_menu_headline_text %}
    <div class="collapsible-text sw-admin-menu__headline_text">
        <router-link
            :to="{ name: 'sw.sales.channel.list' }"
        >{{ $tc('sw-sales-channel.general.titleMenuItems') }}</router-link>
    </div>
    {% endblock %}
```
