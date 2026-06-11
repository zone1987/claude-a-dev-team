# sw-internal-link

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| routerLink | `any` | — | no |  |
| target | `any` | `null` | no |  |
| icon | `any` | `'regular-long-arrow-right'` | no |  |
| inline | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| hideIcon | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `elementType` | |
| `componentClasses` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-measurement-form/sw-product-measurement-form.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.sales.channel.list' }"
    hide-icon
    inline
>
    {{ $tc('sw-product.measurementForm.linkText') }}
</sw-internal-link>
```

### Example 2
Source: `sw-settings-payment/component/sw-payment-card/sw-payment-card.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.settings.payment.detail', params: { id: paymentMethod.id }}"
    :disabled="!acl.can('payment.editor') || undefined"
    hide-icon
>
    {{ $tc('sw-settings-payment.overview.editDetails') }}
</sw-internal-link>
```

### Example 3
Source: `sw-settings-usage-data/component/sw-usage-data-consent-banner/sw-usage-data-consent-banner.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.settings.usage.data.index' }"
>
    {{ $tc('sw-usage-data-consent-banner.togglePath') }}
</sw-internal-link>
```

### Example 4
Source: `sw-settings-measurement/component/sw-settings-measurement-default-units/sw-settings-measurement-default-units.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.sales.channel.list' }"
    inline
    hide-icon
>
    {{ $tc('sw-settings-measurement.defaultUnits.linkText') }}
</sw-internal-link>
```
