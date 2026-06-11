# sw-tree-item

> Individual tree node within sw-tree.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| draggedItem | `any` | — | no |  |
| newElementId | `any` | — | no |  |
| translationContext | `any` | — | no |  |
| onChangeRoute | `any` | — | no |  |
| disableContextMenu | `any` | — | no |  |
| contextMenuTooltipText | `any` | — | no |  |
| activeParentIds | `any` | — | no |  |
| activeItemIds | `any` | — | no |  |
| sortable | `any` | — | no |  |
| markInactive | `any` | `false` | no |  |
| shouldFocus | `any` | `false` | no |  |
| shouldShowActiveState | `any` | `false` | no |  |
| activeFocusId | `any` | — | no |  |
| displayCheckbox | `any` | — | no |  |
| allowNewCategories | `any` | — | no |  |
| allowDeleteCategories | `any` | — | no |  |
| allowCreateWithoutPosition | `any` | — | no |  |
| allowDuplicate | `any` | — | no |  |
| getItemUrl | `any` | — | no |  |
| getIsHighlighted | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| grip | — | |
| content | — | |
| actions | item: item | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| check-item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `updatedComponent` | |
| `mountedComponent` | |
| `beforeUnmountComponent` | |
| `handleKeyDown` | |
| `openTreeItem` | |
| `getTreeItemChildren` | |
| `dragStart` | |
| `dragEnd` | |
| `onMouseEnter` | |
| `startDrag` | |
| `endDrag` | |
| `moveDrag` | |
| `emitCheckedItem` | |
| `toggleItemCheck` | |
| `addSubElement` | |
| `addElement` | |
| `duplicateElement` | |
| `onDuplicate` | |
| `editElementName` | |
| `onFinishNameingElement` | |
| `onBlurTreeItemInput` | |
| `onCancelSubmit` | |
| `abortCreateElement` | |
| `deleteElement` | |
| `getName` | |
| `getActiveIconColor` | |
| `showItemUrl` | |
| `renderContentSlotNode` | |
| `renderActionsSlotNode` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `checked` | |
| `activeElementId` | |
| `isOpened` | |
| `isDragging` | |
| `styling` | |
| `dragConf` | |
| `parentScope` | |
| `toolTip` | |
| `isDisabled` | |
| `isHighlighted` | |
| `contentSlot` | |
| `actionsSlot` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-tree-item
    v-for="item in treeItems"
    :key="item.id"
    should-focus
    :display-checkbox="false"
    :item="item"
    :active="item.active"
    :sortable="sortable"
    :on-change-route="onChangeRoute"
    :active-parent-ids="selectedItemsPathIds"
    :active-item-ids="checkedItemIds"
    @check-item="checkItem"
>

    <template #actions="{ item }">
```

### Example 2
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-tree-item
    v-for="item in treeItems"
    :key="item.id"
    :item="item"
    :should-show-active-state="true"
    :allow-duplicate="true"
    :allow-new-categories="false || undefined"
    :allow-delete-categories="allowDelete || undefined"
    :active="item.active"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :sortable="sortable || undefined"
    :dragged-item="draggedItem"
    :disable-context-menu="disableContextMenu"
    :display-checkbox="allowEdit || undefined"
```

### Example 3
Source: `sw-category/component/sw-category-tree/sw-category-tree.html.twig`
```twig
        <sw-tree-item
            v-for="item in treeItems"
            :key="item.id"
            :item="item"
            :should-show-active-state="true"
            :allow-duplicate="false"
            :allow-new-categories="allowCreate || undefined"
            :allow-delete-categories="allowDelete || undefined"
            :active="item.active"
            :translation-context="translationContext"
            :on-change-route="onChangeRoute"
            :sortable="sortable"
            :dragged-item="draggedItem"
            :disable-context-menu="disableContextMenu"
            :display-checkbox="allowEdit || undefined"
```

### Example 4
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
        <sw-tree-item
            v-for="(item, index) in treeItems"
            :key="item.id"
            :sortable="false"
            :item="item"
            disable-context-menu
            @check-item="filterOptionChecked"
        />
    </template>
</sw-tree>
{% endblock %}

{% block sw_product_variant_modal_option_list_toolbar_container_filter_buttons %}
<div class="sw-product-variant-modal__filter-buttons">
    {% block sw_product_variant_modal_option_list_toolbar_container_button_filter_reset %}
```

### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-variants-delivery/sw-product-variants-delivery-order/sw-product-variants-delivery-order.html.twig`
```twig
                <sw-tree-item
                    v-for="item in treeItems"
                    :key="item.id"
                    :item="item"
                    :disable-context-menu="true"
                    :sortable="true"
                />
            </template>
        </sw-tree>
        {% endblock %}

        {% block sw_product_variants_delivery_order_loader %}
        <sw-loader v-else />
        {% endblock %}
    </div>
```
