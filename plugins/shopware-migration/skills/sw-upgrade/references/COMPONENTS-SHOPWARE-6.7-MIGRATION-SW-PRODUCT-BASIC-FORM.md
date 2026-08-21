# sw-product-basic-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |
| showSettingsInformation | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateIsTitleRequired` | |
| `getInheritValue` | |
| `loadProductNumberRangeId` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `productNameError` | |
| `productDescriptionError` | |
| `productProductNumberError` | |
| `productManufacturerIdError` | |
| `productActiveError` | |
| `productMarkAsTopsellerError` | |
| `numberRangeRepository` | |
| `isTitleRequired` | |
| `productNumberRangeLink` | |
| `productNumberHelpText` | |
| `highlightHelpText` | |
| `numberRangeCriteria` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
    <sw-product-basic-form
        :show-settings-information="showModeSetting"
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}

</mt-card>
{% endblock %}

<mt-card
    v-if="isDownloadCardVisible"
    class="sw-product-detail-base__downloads"
    :subtitle="$tc('sw-product.detailBase.cardSubtitleDownloads')"
    :is-loading="loading.product || loading.customFieldSets || loading.downloads"
    position-identifier="sw-product-detail-base-downloads"
```
