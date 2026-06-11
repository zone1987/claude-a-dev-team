# sw-form-field-renderer

> Dynamic form field renderer that generates form inputs from custom field definitions.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | `null` | no |  |
| config | `any` | `null` | no |  |
| value | `any` | — | yes |  |
| error | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| slotName | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitUpdate` | |
| `getTranslations` | |
| `getComponentFromType` | |
| `createRepository` | |
| `fetchSystemCurrency` | |
| `getScopedSlots` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `bind` | |
| `hasConfig` | |
| `componentName` | |
| `swFieldType` | |
| `translations` | |
| `optionTranslations` | |
| `componentPropName` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/sw-bulk-edit-custom-fields/sw-bulk-edit-custom-fields.html.twig`
```twig
                    <sw-form-field-renderer
                        v-bind="getBind(customField, props)"
                        :key="props.isInherited"
                        :class="'sw-form-field-renderer-input-field__' + customField.name"
                        :disabled="disabled || props.isInherited"
                        :value="props.currentValue"
                        @update:value="props.updateCurrentValue"
                    />
                </template>
            </sw-inherit-wrapper>
            {% endblock %}
        </sw-container>
    </template>
</div>
{% endblock %}
```

### Example 2
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
        <sw-form-field-renderer
            v-else-if="formField"
            v-model:value="documentConfig.config[formField.name]"
            :disabled="!acl.can('document.editor') || undefined"
            class="sw-settings-document-detail__form-field-renderer"
            v-bind="formField"
        />

        <div
            v-else
            :key="`else-formField-${index}`"
        ></div>
        {% endblock %}
    </template>
</template>
```

### Example 3
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
                            <sw-form-field-renderer
                                v-model:value="documentConfig.config[formField.name]"
                                :disabled="!acl.can('document.editor') || undefined"
                                v-bind="formField"
                            />
                            {% endblock %}
                        </template>
                    </template>
                    {% endblock %}
                </sw-container>
            </mt-card>
            {% endblock %}

            {% block sw_settings_document_detail_custom_field_sets %}
            <mt-card
```

### Example 4
Source: `sw-settings/component/sw-system-config/sw-system-config.html.twig`
```twig
            <sw-form-field-renderer
                v-if="props"
                v-bind="getMeteorElementBind(element, props)"
                v-on="getMeteorElementEventsHandler(element, props)"
            />
        </template>
    </sw-inherit-wrapper>
</template>

<template v-else>
{% block sw_system_config_content_card_field %}
    <sw-inherit-wrapper
        v-model:value="actualConfigData[currentSalesChannelId][element.name]"
        v-bind="getInheritWrapperBind(element)"
        :has-parent="isNotDefaultSalesChannel"
```

### Example 5
Source: `sw-flow/component/modals/sw-flow-app-action-modal/sw-flow-app-action-modal.html.twig`
```twig
<sw-form-field-renderer
    v-for="field in fields"
    :key="field.name"
    v-model:value="config[field.name]"
    :type="field.type"
    :config="getConfig(field)"
    :error="errors[field.name]"
    @update:value="onChange($event, field)"
/>

{% endblock %}
<template #modal-footer>
    {% block sw_flow_app_action_modal_footer_cancel_button %}
    <mt-button
        class="sw-flow-app-action-modal__cancel-button"
```
