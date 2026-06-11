# sw-contextual-field

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-contextual-field-prefix | — | |
| sw-field-input | — | |
| sw-contextual-field-suffix | — | |
| hint | — | |
| label | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasPrefix` | |
| `hasSuffix` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-contextual-field
    class="sw-settings-country-new-snippet-modal__search-field"
    required
    :disabled="disabled"
    :error="null"
>
    <template #sw-field-input="{ identification, disabled, error, size, setFocusClass, removeFocusClass }">
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <input
            ref="searchInput"
            v-model="searchTerm"
            type="text"
            class="sw-settings-country-new-snippet-modal__input-field"
            :placeholder="$tc('sw-settings-country.detail.placeholderSearchSnippet')"
            :disabled="disabled"
```

### Example 2
Source: `sw-flow/component/sw-flow-trigger/sw-flow-trigger.html.twig`
```twig
<sw-contextual-field
    v-tooltip="{
        message: getEventName(eventName),
        disabled: !eventName || isUnknownTrigger,
    }"
    class="sw-flow-trigger__search-field"
    :required="!isTemplate"
    :label="$tc('sw-flow.detail.trigger.name')"
    :disabled="disabled"
    :error="flowEventNameError"
>
    <template #sw-field-input="{ identification, disabled, error, size, setFocusClass, removeFocusClass }">
        {% block sw_flow_trigger_select_field_input %}
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <input
```
