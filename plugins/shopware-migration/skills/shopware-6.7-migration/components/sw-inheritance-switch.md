# sw-inheritance-switch

> Toggle switch for enabling/disabling value inheritance.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isInherited | `any` | `false` | yes |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClickRestoreInheritance` | |
| `onClickRemoveInheritance` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `unInheritClasses` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-inheritance-switch
    v-if="isChild"
    :is-inherited="bulkEditProduct[formField.name].isInherited"
    @inheritance-restore="onInheritanceRestore(formField)"
    @inheritance-remove="onInheritanceRemove(formField)"
/>

<a
    v-if="['add', 'overwrite'].includes(bulkEditProduct[formField.name].type)"
    :class="{ 'is--disabled': !!bulkEditProduct[formField.name].isInherited }"
    class="quick-link"
    role="link"
    tabindex="0"
    @click="displayAdvancePricesModal = true"
    @keydown.enter="displayAdvancePricesModal = true"
```

### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
                    <sw-inheritance-switch
                        :is-inherited="bulkEditData[formField.name].isInherited"
                        @inheritance-restore="onInheritanceRestore(formField)"
                        @inheritance-remove="onInheritanceRemove(formField)"
                    />
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
```

### Example 3
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
                            <sw-inheritance-switch
                                :is-inherited="bulkEditData[formField.name].isInherited"
                                @inheritance-restore="onInheritanceRestore(formField)"
                                @inheritance-remove="onInheritanceRemove(formField)"
                            />
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
```

### Example 4
Source: `sw-cms/component/sw-cms-inherit-wrapper/sw-cms-inherit-wrapper.html.twig`
```twig
        <sw-inheritance-switch
            v-if="supportsInheritance"
            :is-inherited="isInherited"
            @inheritance-restore="showModal = true;"
            @inheritance-remove="onInheritanceRemove"
        />

        <!-- eslint-disable-next-line vuejs-accessibility/label-has-for -->
        <label v-if="label">{{ label }}</label>
    </div>

    <slot v-bind="{ isInherited }"></slot>

    <sw-confirm-modal
        v-if="showModal"
```

### Example 5
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrix/sw-settings-shipping-price-matrix.html.twig`
```twig
            <sw-inheritance-switch
                v-if="!currency.isSystemDefault"
                class="sw-settings-shipping-price-matrix__price-inherit-icon"
                :is-inherited="props.isInherited"
                :disabled="disabled"
                @inheritance-restore="props.restoreInheritance"
                @inheritance-remove="props.removeInheritance"
            />

            <mt-number-field
                v-model="props.currentValue.gross"
                :name="`sw-field--${item.id}-${currency.id}-gross`"
                :size="compact ? 'small' : 'default'"
                class="sw-settings-shipping-price-matrix__price-input"
                :digits="50"
```
