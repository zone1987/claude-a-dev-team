# sw-settings-rule-tree

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| check-item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `checkItem` | |
| `getTreeItems` | |

## Examples

### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-category-tree/sw-settings-rule-category-tree.html.twig`
```twig
<sw-settings-rule-tree
    ref="swTree"
    :allow-create-categories="false"
    :allow-delete-categories="false"
    :items="categories"
    after-id-property="afterCategoryId"
    :sortable="false"
    @get-tree-items="getTreeItems"
    @search-tree-items="searchTreeItems"
    @check-item="onCheckItem"
>
    {% block sw_settings_rule_category_tree_items %}
    <template
        #items="{
            treeItems,
```

### Example 2
Source: `sw-settings-rule/component/sw-settings-rule-tree-item/sw-settings-rule-tree-item.html.twig`
```twig
<sw-settings-rule-tree-item
    v-for="child in item.children"
    :key="child.id"
    :association="association"
    :item="child"
    :dragged-item="draggedItem"
    :parent-scope="parentScope"
    :new-element-id="newElementId"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :active-parent-ids="activeParentIds"
    :active-item-ids="activeItemIds"
    :mark-inactive="markInactive"
    :sortable="sortable"
    :should-focus="shouldFocus"
```
