# sw-category-entry-point-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannelCollection | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `closeModal` | |
| `getCmsPageTypeName` | |
| `onLayoutSelect` | |
| `onLayoutReset` | |
| `openInPagebuilder` | |
| `openLayoutModal` | |
| `closeLayoutModal` | |
| `applyChanges` | |
| `hasNotAppliedChanges` | |
| `isAttributeEqual` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `selectedSalesChannel` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-entry-point-card/sw-category-entry-point-card.html.twig`
```twig
    <sw-category-entry-point-modal
        v-if="configureHomeModalVisible"
        :sales-channel-collection="category.navigationSalesChannels"
        @modal-close="closeConfigureHomeModal"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```
