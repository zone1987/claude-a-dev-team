# sw-email-field-deprecated

> **Deprecated in 6.7** — Use `mt-email-field` instead. Will be removed in 6.8.
> See [mt-email-field](mt-email-field.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-email-field>` | `<mt-email-field>` |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prefix | — | |
| suffix | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |

## Examples

### Example 1
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
<sw-email-field
    v-else-if="type === 'email'"
    class="sw-custom-entity-input-field__email"
    :value="currentValue"
    :label="label"
    :placeholder="placeholder"
    :help-text="helpText"
    @change="onChange"
/>-->

<!-- ToDo NEXT-22874 - Implement json field -->
<!--<sw-????
    v-else-if="type === 'json'"
    class="sw-custom-entity-input-field__json"
    :value="currentValue"
```
