# sw-settings-tag-detail-assignments

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| tag | `any` | — | yes |  |
| toBeAdded | `any` | — | yes |  |
| toBeDeleted | `any` | — | yes |  |
| initialCounts | `any` | — | no |  |
| property | `any` | `null` | no |  |
| entity | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| remove-assignment | — | |
| add-assignment | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `search` | |
| `addTagAggregations` | |
| `searchInheritedEntities` | |
| `onTermChange` | |
| `onAssignmentChange` | |
| `onSelectionChange` | |
| `getCount` | |
| `countIncrease` | |
| `countDecrease` | |
| `isInherited` | |
| `parentHasTags` | |
| `hasInheritedTag` | |
| `onPageChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `tagDefinition` | |
| `isInheritable` | |
| `assignmentAssociations` | |
| `assignmentAssociationsColumns` | |
| `entityRepository` | |
| `entityCriteria` | |
| `entitiesColumns` | |
| `selectedAssignments` | |
| `totalAssignments` | |

## Examples

### Example 1
Source: `sw-settings-tag/component/sw-settings-tag-detail-modal/sw-settings-tag-detail-modal.html.twig`
```twig
            <sw-settings-tag-detail-assignments
                :tag="tag"
                :initial-counts="computedCounts"
                :to-be-added="assignmentsToBeAdded"
                :to-be-deleted="assignmentsToBeDeleted"
                :property="property"
                :entity="entity"
                @add-assignment="addAssignment"
                @remove-assignment="removeAssignment"
            />
            {% endblock %}
        </template>
    </template>
</sw-tabs>
{% endblock %}
```
