# sw-sortable-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| sortable | `any` | — | no |  |
| dragConf | `any` | — | no |  |
| scrollOnDrag | `any` | — | no |  |
| scrollOnDragConf | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `findScrollableParent` | |
| `hasOrderChanged` | |
| `onDragEnter` | |
| `onDragStart` | |
| `onScroll` | |
| `scroll` | |
| `onDrop` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasItems` | |
| `isSortable` | |
| `mergedDragConfig` | |
| `mergedScrollOnDragConfig` | |
| `scrollableParent` | |

## Examples

### Example 1
Source: `sw-settings-tax/component/sw-settings-tax-provider-sorting-modal/sw-settings-tax-provider-sorting-modal.html.twig`
```twig
<sw-sortable-list
    class="sw-settings-tax-provider-sorting-modal__tax-provider-list"
    :items="sortedTaxProviders"
    @items-sorted="onSort"
>
    <template #item="{ item: taxProvider }">
        <div
            class="sw-settings-tax-provider-sorting-modal__tax-provider-list-item"
            :class="!taxProvider.active ? 'is--disabled' : ''"
        >
            <mt-icon
                class="sw-settings-tax-provider-sorting-modal__tax-provider-list-item__action"
                name="regular-grip-vertical"
            />

```

### Example 2
Source: `sw-settings-payment/component/sw-settings-payment-sorting-modal/sw-settings-payment-sorting-modal.html.twig`
```twig
<sw-sortable-list
    class="sw-settings-payment-sorting-modal__payment-method-list"
    :items="sortedPaymentMethods"
    :scroll-on-drag="true"
    :scroll-on-drag-conf="scrollOnDragConf"
    @items-sorted="onSort"
>
    {% block sw_settings_payment_sorting_modal_content_payment_method %}
    <template #item="{ item: paymentMethod }">
        <div
            class="sw-settings-payment-sorting-modal__payment-method-list-item"
            :class="!paymentMethod.active ? 'is--disabled' : ''"
        >
            {% block sw_settings_payment_sorting_modal_content_payment_method_action %}
            <mt-icon
```
