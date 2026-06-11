# sw-multi-tag-ip-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| validate | `any` | — | no |  |
| knownIps | `any` | — | no |  |
| errorCode | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |

## Methods

| Method | Description |
|--------|-------------|
| `addSpecific` | |
| `getKnownIp` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `errorObject` | |
| `validKnownIps` | |
| `validUnselectedKnownIps` | |

## Examples

### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-multi-tag-ip-select
        v-model:value="maintenanceIpAllowlist"
        :is-loading="isLoading"
        :disabled="!acl.can('sales_channel.editor') || undefined"
        class="sw-order-user-card__tag-select"
        :label="$tc('sw-sales-channel.detail.ipAddressAllowlist')"
        :help-text="$tc('sw-sales-channel.detail.ipAddressAllowlistHelpText')"
        :known-ips="knownIps"
        :validate="validateMaintenanceIpCidr"
        error-code="SHOPWARE_INVALID_IP_CIDR"
    />
    {% endblock %}

    {% block sw_sales_channel_detail_base_settings_link %}
    <div class="sw-sales-channel-detail-base__settings-link">
```
