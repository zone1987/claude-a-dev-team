# sw-settings-tag-detail-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| editedTag | `any` | `null` | no |  |
| counts | `any` | — | no |  |
| property | `any` | `null` | no |  |
| entity | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `onCancel` | |
| `addAssignment` | |
| `removeAssignment` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `tagRepository` | |
| `tagDefinition` | |
| `tagNameError` | |
| `title` | |
| `allowSave` | |
| `tooltipSave` | |
| `computedCounts` | |

## Examples

### Example 1
Source: `sw-settings-tag/page/sw-settings-tag-list/sw-settings-tag-list.html.twig`
```twig
        <sw-settings-tag-detail-modal
            v-if="showDetailModal === item.id"
            :edited-tag="item"
            :counts="getCounts(item.id)"
            :property="detailProperty"
            :entity="detailEntity"
            @finish="onSaveFinish"
            @close="onCloseDetailModal"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-entity-listing>
{% endblock %}

```
