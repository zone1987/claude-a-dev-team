# sw-settings-rule-add-assignment-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| entityContext | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close-add-modal | — | |
| entities-saved | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntities` | |
| `onCloseAddModal` | |
| `onAdd` | |
| `updateEntities` | |
| `insertEntities` | |
| `onSelect` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalSize` | |

## Examples

### Example 1
Source: `sw-settings-rule/view/sw-settings-rule-detail-assignments/sw-settings-rule-detail-assignments.html.twig`
```twig
    <sw-settings-rule-add-assignment-modal
        v-if="addModal"
        :rule="rule"
        :entity-context="addEntityContext"
        @entities-saved="onEntitiesSaved"
        @close-add-modal="onCloseAddModal"
    />
    {% endblock %}
</div>
{% endblock %}

```
