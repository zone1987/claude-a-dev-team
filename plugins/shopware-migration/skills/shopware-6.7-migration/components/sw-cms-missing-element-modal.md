# sw-cms-missing-element-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| missingElements | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| modal-save | — | |
| modal-dont-remind-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `onSave` | |
| `onChangeDontRemindCheckbox` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `element` | |
| `title` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
                <sw-cms-missing-element-modal
                    v-if="showMissingElementModal"
                    :missing-elements="missingElements"
                    @modal-close="onCloseMissingElementModal"
                    @modal-save="onSaveMissingElementModal"
                    @modal-dont-remind-change="onChangeDontRemindCheckbox"
                />
                {% endblock %}
            </div>
            {% endblock %}
        </div>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}
```
