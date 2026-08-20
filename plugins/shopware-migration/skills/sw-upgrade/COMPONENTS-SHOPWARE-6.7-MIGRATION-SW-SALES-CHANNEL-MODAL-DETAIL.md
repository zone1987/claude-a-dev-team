# sw-sales-channel-modal-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| detailType | `any` | `null` | no |  |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal/sw-sales-channel-modal.html.twig`
```twig
<sw-sales-channel-modal-detail
    v-else
    :detail-type="detailType"
/>
{% endblock %}

{% block sw_sales_channel_modal_footer %}
<template #modal-footer>
    <a
        href="#"
        class="sw-sales-channel-modal__footer_left"
        @click.prevent="openRoute({ name: 'sw.sales.channel.list' })"
    >
        {{ $tc('sw-sales-channel.general.manageSalesChannels') }}
    </a>
```
