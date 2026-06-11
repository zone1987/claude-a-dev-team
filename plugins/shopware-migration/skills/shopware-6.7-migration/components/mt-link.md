# mt-link

> Styled link component for navigation with external/internal variants.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| to | `string` | — | no | |
| as | `string` | — | no | |
| variant | `"primary" | "critical"` | — | no | |
| disabled | `boolean` | — | no | |
| type | `"external" | "internal"` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | event: MouseEvent | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<mt-link
    type="external"
    href="https://developer.shopware.com/docs/guides/hosting/installation-updates/extension-managment.html"
>
    {{ $tc('sw-app.component.sw-app-wrong-app-url-modal.labelLearnMoreButton') }}
</mt-link>
```

### Example 2
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
<mt-link
    class="sw-extension-permissions-modal__detail-link"
    as="button"
    type="internal"
    @click="openDetailsModal(key)"
>
    {{ $tc('sw-extension-store.component.sw-extension-permissions-modal.textEntities') }}
</mt-link>
```

### Example 3
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
<mt-link
    class="sw-extension-permissions-modal__detail-link"
    as="button"
    type="internal"
    @click="toggleDomainsModal(true)"
>
    {{ $tc('sw-extension-store.component.sw-extension-permissions-modal.showDomains') }}
</mt-link>
```

### Example 4
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
<mt-link
    v-if="salesChannel.length > 0"
    class="sw-settings-listing-default-sales-channel__quick-link"
    as="button"
    type="internal"
    variant="primary"
    @click="displayAdvancedVisibility"
    @keydown.enter="displayAdvancedVisibility"
>
    {{ $tc('sw-settings-listing.index.defaultSalesChannel.linkAdvancedVisibility') }}
</mt-link>
```

### Example 5
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
<mt-link
    as="button"
    class="sw-import-export-exporter__link"
    @click="setExportModalProfile('product_configurator_setting')"
>
    {{ $tc('sw-import-export.exporter.directExportVariantsLabel') }}
</mt-link>
```
