# sw-flow-sequence

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `sequenceData` | |
| `isSelectorSequence` | |
| `isConditionSequence` | |
| `isActionSequence` | |
| `trueBlockClasses` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-selector
    v-if="isSelectorSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

{% block sw_flow_sequence_condition %}
<sw-flow-sequence-condition
    v-if="isConditionSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

```

### Example 2
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
        <sw-flow-sequence
            :sequence="sequenceData.trueBlock"
            :disabled="disabled"
        />
    </div>
    {% endblock %}

    {% block sw_flow_sequence_false_block %}
    <div
        v-if="sequenceData.falseBlock"
        class="sw-flow-sequence__false-block"
    >
        <sw-flow-sequence
            :sequence="sequenceData.falseBlock"
            :disabled="disabled"
```

### Example 3
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-flow-sequence-action-error
    v-if="!isValidAction(item.actionName)"
    :sequence="item"
>
    <template #content>
        <div class="sw-flow-sequence-action__error-action">
            <div class="sw-flow-sequence-action__error-action-title">
                <mt-icon
                    name="regular-question-circle-s"
                    size="14px"
                    class="mt-icon-action"
                />

                <span>{{ $tc('sw-flow.actions.unknownLabel') }}</span>
            </div>
```

### Example 4
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
    <sw-flow-sequence-modal
        :sequence="currentSequence"
        :action="selectedAction"
        :modal-name="modalName"
        @process-finish="onSaveActionSuccess"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 5
Source: `sw-flow/view/detail/sw-flow-detail-flow/sw-flow-detail-flow.html.twig`
```twig
                        <sw-flow-sequence
                            name="root-sequence"
                            :sequence="sequence"
                            :disabled="!acl.can('flow.editor')"
                            :is-unknown-trigger="isUnknownTrigger"
                        />
                    </div>
                    {% endblock %}
                </div>
                {% endblock %}
            </transition-group>
            {% endblock %}
        </div>
        {% endblock %}
    </div>
```
