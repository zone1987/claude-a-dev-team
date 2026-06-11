# sw-base-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | `null` | no |  |
| label | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| hint | `any` | `null` | no |  |
| isInvalid | `any` | `false` | no |  |
| aiBadge | `any` | `false` | no |  |
| error | `null` | — | no |  |
| disabled | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| isInherited | `any` | `false` | no |  |
| isInheritanceField | `any` | `false` | no |  |
| disableInheritanceToggle | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| sw-field-input | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| base-field-mounted | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identification` | |
| `hasLabel` | |
| `hasError` | |
| `hasHint` | |
| `swFieldClasses` | |
| `swFieldLabelClasses` | |
| `showLabel` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-select-rating/sw-extension-select-rating.html.twig`
```twig
<sw-base-field
    class="sw-field--rating-select"
    v-bind="$attrs"
>
    {% block sw_select_rating_input %}
    <template #sw-field-input>
        {% block sw_select_rating_input_stars %}
        <sw-extension-rating-stars
            v-model:rating="currentValue"
            editable
            @update:rating="onChange"
        />
        {% endblock %}
    </template>
    {% endblock %}
```
