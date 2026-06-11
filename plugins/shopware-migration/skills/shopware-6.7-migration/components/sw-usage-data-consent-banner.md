# sw-usage-data-consent-banner

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| canBeHidden | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onReject` | |
| `onAccept` | |
| `onHide` | |
| `onClose` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isAccepted` | |
| `isHidden` | |
| `hasSufficientPrivileges` | |

## Examples

### Example 1
Source: `sw-settings-usage-data/view/sw-settings-usage-data-general/sw-settings-usage-data-general.html.twig`
```twig
<sw-usage-data-consent-banner v-if="!feature.isActive('PRODUCT_ANALYTICS')" />
```

### Example 2
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-usage-data-consent-banner
    v-if="!feature.isActive('PRODUCT_ANALYTICS')"
    can-be-hidden
/>

<sw-extension-component-section
    position-identifier="sw-dashboard__before-content"
    class="sw-dashboard__before-content"
/>

{% block sw_dashboard_index_content_info_grid %}
<div class="sw-dashboard-index__card-grid">
    {% block sw_dashboard_index_content_info_grid_inner %}

    {% block sw_dashboard_index_content_info__grid_inner_welcome_card %}
```
