# sw-category-sales-channel-multi-select

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-label-property | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-add | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `addItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-entry-point-card/sw-category-entry-point-card.html.twig`
```twig
<sw-category-sales-channel-multi-select
    v-if="associatedCollection"
    class="sw-category-entry-point-card__sales-channel-selection"
    :entity-collection="associatedCollection"
    :label="salesChannelSelectionLabel"
    :criteria="salesChannelCriteria"
    :placeholder="$tc('sw-category.base.entry-point-card.placeholderSalesChannels')"
    :disabled="!selectedEntryPoint || !acl.can('category.editor')"
    @update:entity-collection="onSalesChannelChange"
/>
{% endblock %}

{% block sw_category_entry_point_card_button_configure_home %}
<mt-button
    v-if="selectedEntryPoint === 'navigationSalesChannels' && category.navigationSalesChannels.length > 0"
```
