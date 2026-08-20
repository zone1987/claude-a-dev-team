# mt-unit-field

> Number input with a unit selector dropdown (e.g., px, em, %).

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| defaultUnit | `Unit` | — | yes | |
| measurementType | `"length" | "mass"` | — | no | |
| modelValue | `number | undefined` | — | no | |
| placeholder | `string` | — | no | |
| numberType | `"float" | "int"` | — | no | |
| step | `number` | — | no | |
| min | `number` | — | no | |
| max | `number` | — | no | |
| digits | `number` | — | no | |
| fillDigits | `boolean` | — | no | |
| allowEmpty | `boolean` | — | no | |
| numberAlignEnd | `boolean` | — | no | |
| label | `string` | — | no | |
| error | `object` | — | no | |
| disabled | `boolean` | — | no | |
| required | `boolean` | — | no | |
| name | `string` | — | no | |
| size | `string` | — | no | |
| helpText | `string` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| disableInheritanceToggle | `boolean` | — | no | |
| copyable | `boolean` | — | no | |
| copyableTooltip | `boolean` | — | no | |
| zIndex | `number | null` | — | no | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | value: number | undefined | |
| update:defaultUnit | value: Unit | |
| update:measurementType | value: "length" | "mass" | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-measurement-form/sw-product-measurement-form.html.twig`
```twig
        <mt-unit-field
            measurement-type="length"
            :model-value="props.currentValue"
            :default-unit="lengthUnit"
            :label="$t('sw-product.settingsForm.labelWidth')"
            :is-inheritance-field="props.isInheritField"
            :is-inherited="props.isInherited"
            :placeholder="$t('sw-product.settingsForm.placeholderWidth')"
            :min="0"
            :step="1"
            :digits="3"
            :error="productWidthError"
            :disabled="props.isInherited || !allowEdit"
            :allow-empty="true"
            @update:model-value="props.updateCurrentValue"
```

### Example 2
Source: `sw-product/component/sw-product-measurement-form/sw-product-measurement-form.html.twig`
```twig
            <mt-unit-field
                measurement-type="length"
                :model-value="props.currentValue"
                :default-unit="lengthUnit"
                :label="$t('sw-product.settingsForm.labelHeight')"
                :is-inheritance-field="props.isInheritField"
                :is-inherited="props.isInherited"
                :placeholder="$t('sw-product.settingsForm.placeholderHeight')"
                :min="0"
                :step="1"
                :digits="3"
                :error="productHeightError"
                :disabled="props.isInherited || !allowEdit"
                :allow-empty="true"
                @update:model-value="props.updateCurrentValue"
```
