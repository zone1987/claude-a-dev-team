# sw-product-modal-variant-generation

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| groups | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |
| actualStatus | `any` | `'is-physical'` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| variations-finish-generate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountComponent` | |
| `onQueuesHandler` | |
| `onProgressMaxHandler` | |
| `onProgressActualHandler` | |
| `removeFile` | |
| `removeFileForAllVariants` | |
| `getList` | |
| `handlePageChange` | |
| `generateVariants` | |
| `showNextStep` | |
| `calcVariantsNumber` | |
| `onChangeAllVariantValues` | |
| `onChangeVariantValue` | |
| `isUploadDisabled` | |
| `isExistingMedia` | |
| `successfulUpload` | |
| `updateUsageForAllVariantFiles` | |
| `pushFileToUsageList` | |
| `onModalCancel` | |
| `addOriginalConfiguratorSettings` | |
| `emptyConfiguratorSettings` | |
| `onTermChange` | |
| `removeDuplicateEntries` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currencies` | |
| `productRepository` | |
| `optionRepository` | |
| `mediaRepository` | |
| `progressInPercentage` | |
| `progressMessage` | |
| `buttonVariant` | |
| `buttonLabel` | |
| `isGenerateButtonDisabled` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
    <sw-product-modal-variant-generation
        v-if="activeModal === 'variantGeneration'"
        :product="productEntity"
        :groups="groups"
        :actual-status="activeTab"
        :selected-groups="configSettingGroups"
        @modal-close="activeModal = ''"
        @variations-finish-generate="updateVariations"
    />
    {% endblock %}

    {% block sw_product_detail_variants_modal_delivery %}
    <sw-product-modal-delivery
        v-if="activeModal === 'deliveryModal'"
        :product="productEntity"
```
