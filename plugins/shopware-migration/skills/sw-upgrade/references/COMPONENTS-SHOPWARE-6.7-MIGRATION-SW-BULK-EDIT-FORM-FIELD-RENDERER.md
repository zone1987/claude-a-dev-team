# sw-bulk-edit-form-field-renderer

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:default-unit | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onUpdateDefaultUnit` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
                    <sw-bulk-edit-form-field-renderer
                        v-bind="formField"
                        :key="`formField-${index}`"
                        v-model:value="entity[formField.name]"
                        @update:value="onChangeValue($event, formField.name)"
                    />
                </div>
            </template>
            <template v-else>
                <sw-bulk-edit-form-field-renderer
                    v-if="isDisplayingValue"
                    v-bind="formField"
                    :key="`formField-${index}`"
                    v-model="entity[formField.name]"
                    v-model:value="entity[formField.name]"
```

### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
                            <sw-bulk-edit-form-field-renderer
                                v-bind="formField"
                                :key="`formField-${index}`"
                                v-model:value="entity[formField.name]"
                                @update:value="onChangeValue($event, formField.name)"
                            />
                        </div>
                    </template>
                    <template v-else>
                        <sw-bulk-edit-form-field-renderer
                            v-bind="formField"
                            :key="`formField-${index}`"
                            v-model:value="entity[formField.name]"
                            @update:value="onChangeValue($event, formField.name)"
                            @update:default-unit="$emit('update:default-unit', $event)"
```
