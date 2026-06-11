# sw-media-quickinfo-usage

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| routerLinkTarget | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadSlotConfigAssociations` | |
| `loadProductAssociations` | |
| `loadCategoryAssociations` | |
| `loadManufacturerAssociations` | |
| `loadMailTemplateAssociations` | |
| `loadDocumentBaseConfigAssociations` | |
| `loadAvatarUserAssociations` | |
| `loadPaymentMethodAssociations` | |
| `loadShippingMethodAssociations` | |
| `loadLayoutAssociations` | |
| `isExistedCmsMedia` | |
| `getProductUsage` | |
| `getCategoryUsage` | |
| `getManufacturerUsage` | |
| `getMailTemplateUsage` | |
| `getDocumentBaseConfigUsage` | |
| `getAvatarUserUsage` | |
| `getPaymentMethodUsage` | |
| `getShippingMethodUsage` | |
| `getLayoutUsage` | |
| `getLandingPageUsage` | |
| `getIconForModule` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `landingPageRepository` | |
| `categoryRepository` | |
| `cmsPageRepository` | |
| `moduleFactory` | |
| `slotConfigCriteria` | |
| `cmsPageBlockConfigCriteria` | |
| `getUsages` | |
| `isNotUsed` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-usage :item="item" />
```
