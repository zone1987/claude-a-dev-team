# sw-tagged-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| placeholder | `any` | — | no |  |
| addOnKey | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `dismissLastTag` | |
| `dismissTag` | |
| `performAddTag` | |
| `setFocus` | |
| `noTriggerKey` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasValues` | |
| `taggedFieldClasses` | |
| `taggedFieldInputClasses` | |

## Examples

### Example 1
Source: `sw-cms/elements/form/config/sw-cms-el-config-form.html.twig`
```twig
                    <sw-tagged-field
                        v-model:value="element.config.mailReceiver.value"
                        :class="getLastMailClass"
                        name="mailReceiver"
                        placeholder="john@doe.com"
                        :disabled="isInherited"
                        @update:value="updateMailReceiver"
                    />
                </template>
            </sw-cms-inherit-wrapper>
        </sw-container>
        {% endblock %}
    </template>
</sw-tabs>
{% endblock %}
```

### Example 2
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
    <sw-tagged-field
        ref="product-stream-value-multi-value-tagged-field"
        v-model:value="multiValue"
        size="medium"
    />
    {% endblock %}
</template>

<template v-else-if="filterType === 'since' || filterType === 'until'">
    {% block sw_product_stream_value_relative_time_operator %}
    <sw-arrow-field
        ref="product-stream-value-relative-time-arrow-field"
        :disabled="disabled"
    >
        <sw-single-select
```
