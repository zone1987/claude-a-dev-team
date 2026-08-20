# sw-extension-deactivation-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| isLicensed | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| extension-deactivate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |
| `emitDeactivate` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `removeHint` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-bought/sw-extension-card-bought.html.twig`
```twig
<sw-extension-deactivation-modal
    v-if="showDeactivationModal"
    :extension-name="label"
    :is-licensed="license !== null"
    :is-loading="isLoading"
    @modal-close="closeDeactivationModal"
    @extension-deactivate="closeModalAndDeactivateExtension"
/>
{% endblock %}

{% block sw_extension_card_base_info_content %}
    {% parent %}

<section v-if="priceInfo && extension.storeLicense.variant === 'rent'">
    <span class="sw-extension-card-bought__info-price">
```
