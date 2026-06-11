# sw-plugin-box

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| pluginId | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `checkPluginConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pluginRepository` | |

## Examples

### Example 1
Source: `sw-settings-payment/page/sw-settings-payment-detail/sw-settings-payment-detail.html.twig`
```twig
<sw-plugin-box
    v-if="!!paymentMethod.pluginId"
    :plugin-id="paymentMethod.pluginId"
/>
{% endblock %}

<sw-container
    columns="3fr 3fr 1fr"
    gap="0px 30px"
>
    {% block sw_settings_payment_detail_content_field_name %}

    <mt-text-field
        v-model="paymentMethod.name"
        name="sw-field--paymentMethod-name"
```
