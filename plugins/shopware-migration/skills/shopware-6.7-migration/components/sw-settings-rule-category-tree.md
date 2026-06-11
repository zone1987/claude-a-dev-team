# sw-settings-rule-category-tree

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| association | `any` | — | yes |  |
| categoriesCollection | `any` | — | yes |  |
| hideHeadline | `any` | `false` | no |  |
| hideSearch | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-selection | — | |

## Methods

| Method | Description |
|--------|-------------|
| `searchTreeItems` | |
| `onCheckItem` | |
| `getTreeItems` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `categoryRepository` | |
| `treeCriteria` | |

## Examples

### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-add-assignment-modal/sw-settings-rule-add-assignment-modal.html.twig`
```twig
<sw-settings-rule-category-tree
    v-if="entityContext.entityName === 'category'"
    :rule="rule"
    :association="entityContext.addContext.association"
    :categories-collection="entities"
    :hide-headline="true"
    :hide-search="true"
    placeholder="Add categories"
    @on-selection="onSelect"
/>
{% endblock %}

{% block sw_settings_rule_add_assignment_modal_listing %}
<sw-settings-rule-add-assignment-listing
    v-else
```
