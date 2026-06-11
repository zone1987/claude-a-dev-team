# sw-cms-layout-assignment-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onModalClose` | |
| `saveShopPages` | |
| `loadSystemConfig` | |
| `validateCategories` | |
| `validateLandingPages` | |
| `validateProducts` | |
| `onConfirm` | |
| `openConfirmChangesModal` | |
| `closeConfirmChangesModal` | |
| `onDiscardChanges` | |
| `discardCategoryChanges` | |
| `discardLandingPageChanges` | |
| `discardShopPageChanges` | |
| `discardProductChanges` | |
| `onAbort` | |
| `onKeepEditing` | |
| `onConfirmChanges` | |
| `onInputSalesChannelSelect` | |
| `onExtraCategories` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `systemConfigDomain` | |
| `shopPages` | |
| `productColumns` | |
| `productCriteria` | |
| `isProductDetailPage` | |
| `assetFilter` | |
| `categoryRepository` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
            <sw-cms-layout-assignment-modal
                v-if="showLayoutAssignmentModal"
                :page="page"
                @modal-close="closeLayoutAssignmentModal"
            />
            {% endblock %}

            <sw-confirm-modal
                v-if="showLayoutSetAsDefaultModal"
                class="sw-cms-detail__confirm-set-as-default-modal"
                :title="$tc('sw-cms.components.setDefaultLayoutModal.title')"
                :text="$tc('sw-cms.components.setDefaultLayoutModal.infoText', {}, page.type === 'product_detail')"
                @confirm="onConfirmLayoutSetAsDefault"
                @cancel="onCloseLayoutSetAsDefault"
                @close="onCloseLayoutSetAsDefault"
```
