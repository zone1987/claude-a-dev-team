# sw-media-entity-mapper

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `mapEntity` | |

## Examples

### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
        <sw-media-entity-mapper
            v-for="mediaItem in items"
            :key="mediaItem.id"
            :item="mediaItem"
            :selected="true"
            :is-list="true"
            :show-context-menu-button="false"
            :show-selection-indicator="true"
            @media-item-selection-remove="onRemoveItemFromSelection"
        />
    </template>
    {% endblock %}
</sw-media-collapse>
{% endblock %}

```

### Example 2
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-entity-mapper
    v-for="(gridItem, index) in selectableItems"
    :key="gridItem.getEntityName() + '_' + gridItem.id"
    :class="`sw-media-grid-item__item--${index}`"
    :item="gridItem"
    :disabled="disabled"
    :allow-edit="acl.can('media.editor')"
    :allow-delete="acl.can('media.deleter')"
    :selected="showItemSelected(gridItem)"
    :show-selection-indicator="isListSelect"
    :show-context-menu-button="editable"
    :is-list="showItemsAsList"
    :editable="editable"
    :allow-multi-select="allowMultiSelect"
    @media-item-replaced="refreshList"
```
