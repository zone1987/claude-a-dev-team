# sw-custom-field-list

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| set | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-changed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `createdComponent` | |
| `loadCustomFields` | |
| `selectionChanged` | |
| `onCustomFieldDelete` | |
| `onDeleteCustomFields` | |
| `onAddCustomField` | |
| `onCancelCustomField` | |
| `onInlineEditFinish` | |
| `onSaveCustomField` | |
| `onInlineEditCancel` | |
| `onCustomFieldEdit` | |
| `removeEmptyProperties` | |
| `isCustomFieldNameUnique` | |
| `onPageChange` | |
| `onCancelDeleteCustomField` | |
| `onDeleteCustomField` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `globalCustomFieldRepository` | |

## Examples

### Example 1
Source: `sw-settings-custom-field/page/sw-settings-custom-field-set-detail/sw-settings-custom-field-set-detail.html.twig`
```twig
                <sw-custom-field-list
                    v-if="set.id"
                    ref="customFieldList"
                    :set="set"
                    @loading-changed="onLoadingChanged"
                />
                {% endblock %}
            </div>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
