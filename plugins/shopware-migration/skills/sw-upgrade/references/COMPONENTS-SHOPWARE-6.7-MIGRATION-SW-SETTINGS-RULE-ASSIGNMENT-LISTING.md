# sw-settings-rule-assignment-listing

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| link-column | item: item, column: column | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| delete-items | — | |

## Methods

| Method | Description |
|--------|-------------|
| `deleteItems` | |

## Examples

### Example 1
Source: `sw-settings-rule/view/sw-settings-rule-detail-assignments/sw-settings-rule-detail-assignments.html.twig`
```twig
<sw-settings-rule-assignment-listing
    v-if="entity.loadedData && entity.loadedData.length > 0"
    class="sw-settings-rule-detail-assignments__entity-listing"
    :class="`sw-settings-rule-detail-assignments__entity-listing-${entity.id}`"
    :is-loading="isLoading"
    :detail-route="entity.detailRoute"
    :data-source="entity.loadedData"
    :repository="entity.repository"
    :local-mode="false"
    :criteria-limit="5"
    :allow-delete="allowDeletion(entity) && acl.can('rule.editor')"
    :allow-inline-edit="false"
    :show-settings="false"
    :show-selection="allowDeletion(entity) && acl.can('rule.editor')"
    :allow-column-edit="false"
```
