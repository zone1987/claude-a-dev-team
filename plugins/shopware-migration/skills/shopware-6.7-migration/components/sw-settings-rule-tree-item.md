# sw-settings-rule-tree-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| association | `any` | — | yes |  |
| hideActions | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `hasItemAssociation` | |

## Examples

### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-category-tree/sw-settings-rule-category-tree.html.twig`
```twig
            <sw-settings-rule-tree-item
                v-for="item in treeItems"
                :key="item.id"
                :association="association"
                :item="item"
                :sortable="false"
                should-focus
                :mark-inactive="true"
                :hide-action="true"
                @check-item="checkItem"
            />
            {% endblock %}
        </template>
        <template
            v-if="hideHeadline"
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
