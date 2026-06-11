# sw-external-link

> **Migration wrapper** — Delegates to `mt-link` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-link](mt-link.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| small | `any` | `false` | no |  |
| icon | `any` | `'regular-external-link-s'` | no |  |
| rel | `any` | `'noopener'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClick` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `iconSize` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```twig
<sw-external-link
    small
    :href="extension.producerWebsite"
    class="sw-extension-config__producer-link"
>
    {{ extension.producerName }}
</sw-external-link>
```

### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-external-link
    :href="item.url"
    download
>

    <mt-icon
        size="16px"
        name="regular-cloud-download"
        class="sw-media-sidebar__quickactions-icon"
    />
    {{ $t('sw-media.sidebar.actions.download') }}
</sw-external-link>
```

### Example 3
Source: `sw-settings-usage-data/component/sw-usage-data-consent-banner/sw-usage-data-consent-banner.html.twig`
```twig
<sw-external-link :href="$tc('sw-usage-data-consent-banner.privacyPolicyLink')">
    {{ $tc('sw-usage-data-consent-banner.privacyPolicy') }}
</sw-external-link>
```

### Example 4
Source: `sw-order/component/sw-order-details-state-card/sw-order-details-state-card.html.twig`
```twig
<sw-external-link
    class="sw-order-detail-state-card__state-history-button"
    icon="regular-long-arrow-right"
    @click="onShowStatusHistory"
>
    {{ $tc('sw-order.stateCard.labelShowHistoryModal') }}
</sw-external-link>
```

### Example 5
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-external-link :href="$tc(`sw-dashboard.helpcard.${key}Link`)">
    {{ $tc(`sw-dashboard.helpcard.${key}`) }}
</sw-external-link>
```
