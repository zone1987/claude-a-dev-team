# sw-condition-tree

> Visual rule/condition tree builder with AND/OR grouping.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| conditionDataProviderService | `any` | — | yes |  |
| conditionRepository | `any` | `null` | no |  |
| initialConditions | `any` | `null` | no |  |
| rootCondition | `any` | `null` | no |  |
| allowedTypes | `any` | `null` | no |  |
| scopes | `any` | `null` | no |  |
| associationField | `any` | — | yes |  |
| associationValue | `any` | — | yes |  |
| associationEntity | `any` | `null` | no |  |
| childAssociationField | `any` | `'children'` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| conditions-changed | — | |
| initial-loading-done | — | |

## Methods

| Method | Description |
|--------|-------------|
| `buildTree` | |
| `createTreeRecursive` | |
| `getRootNodes` | |
| `needsRootOrContainer` | |
| `applyRoot` | |
| `createCondition` | |
| `insertNodeIntoTree` | |
| `removeNodeFromTree` | |
| `validatePosition` | |
| `getDeletedIds` | |
| `getDeletedIdsRecursive` | |
| `emitChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `availableTypes` | |
| `rootId` | |
| `availableGroups` | |
| `restrictedConditions` | |

## Examples

### Example 1
Source: `sw-settings-rule/view/sw-settings-rule-detail-base/sw-settings-rule-detail-base.html.twig`
```twig
    <sw-condition-tree
        :initial-conditions="conditions"
        :condition-repository="conditionRepository"
        :condition-data-provider-service="ruleConditionDataProviderService"
        association-field="ruleId"
        :association-value="rule.id"
        :association-entity="rule"
        :root-condition="null"
        :disabled="!acl.can('rule.editor') || undefined"
        @conditions-changed="$emit('conditions-changed', $event)"
        @initial-loading-done="$emit('tree-finished-loading')"
    />
</mt-card>
{% endblock %}

```

### Example 2
Source: `sw-product/component/sw-product-cross-selling-form/sw-product-cross-selling-form.html.twig`
```twig
    <sw-condition-tree
        v-if="productStreamFilterRepository"
        v-show="false"
        association-field="productStreamId"
        child-association-field="queries"
        :initial-conditions="productStreamFilter"
        :condition-repository="productStreamFilterRepository"
        :condition-data-provider-service="productStreamConditionService"
        :association-value="associationValue"
        :root-condition="null"
        @conditions-changed="updateProductStreamFilterTree"
    />
    {% endblock %}
</div>
{% endblock %}
```

### Example 3
Source: `sw-flow/component/modals/sw-flow-rule-modal/sw-flow-rule-modal.html.twig`
```twig
                <sw-condition-tree
                    v-if="conditionRepository"
                    class="sw-flow-rule-modal__rule"
                    association-field="ruleId"
                    :initial-conditions="conditions"
                    :condition-repository="conditionRepository"
                    :condition-data-provider-service="ruleConditionDataProviderService"
                    :association-value="rule.id"
                    :association-entity="rule"
                    :root-condition="null"
                    @conditions-changed="onConditionsChanged"
                />
                {% endblock %}
            </div>
            {% endblock %}
```

### Example 4
Source: `sw-product-stream/page/sw-product-stream-detail/sw-product-stream-detail.html.twig`
```twig
    <sw-condition-tree
        v-if="productStream"
        :initial-conditions="productStreamFilters"
        :condition-repository="productStreamFiltersRepository"
        :condition-data-provider-service="productStreamConditionService"
        child-association-field="queries"
        association-field="productStreamId"
        :association-value="productStream.id"
        :root-condition="null"
        :disabled="!acl.can('product_stream.editor')"
        @conditions-changed="updateFilterTree"
    />
    {% endblock %}

    {% block sw_product_stream_detail_filter_preview_button %}
```
