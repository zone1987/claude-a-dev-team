# sw-order-promotion-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| error | — | |
| loading-change | — | |
| reload-entity-data | — | |
| save-and-reload | — | |
| save-and-recalculate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitEntityData` | |
| `emitLoadingChange` | |
| `saveAndReload` | |
| `saveAndRecalculate` | |
| `handleUnsavedOrderChangesResponse` | |
| `handleError` | |
| `deleteAutomaticPromotions` | |
| `toggleAutomaticPromotions` | |
| `applyAutomaticPromotions` | |
| `onSubmitCode` | |
| `handlePromotionResponse` | |
| `onRemoveExistingCode` | |
| `dismissPromotionUpdates` | |
| `getLineItemByPromotionCode` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `order` | |
| `isOrderLoading` | |
| `versionContext` | |
| `orderLineItemRepository` | |
| `hasLineItem` | |
| `currency` | |
| `manualPromotions` | |
| `automaticPromotions` | |
| `promotionCodeTags` | |
| `hasAutomaticPromotions` | |
| `changesetGenerator` | |
| `hasOrderUnsavedChanges` | |
| `promotionsRemoved` | |
| `promotionsAdded` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
        <sw-order-promotion-field
            class="sw-order-detail-general__promotions"
            @loading-change="updateLoading"
            @reload-entity-data="reloadEntityData"
            @save-and-reload="saveAndReload"
            @error="showError"
        />
    </mt-card>

    <sw-extension-component-section
        position-identifier="sw-order-detail-base-promotions__after"
    />
    {% endblock %}
</div>
{% endblock %}
```
