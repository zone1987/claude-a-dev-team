# sw-arrow-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| primary | `any` | `'#ffffff'` | no |  |
| secondary | `any` | `'#d1d9e0'` | no |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getArrow` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `arrowFill` | |

## Examples

### Example 1
Source: `sw-product-stream/component/sw-product-stream-field-select/sw-product-stream-field-select.html.twig`
```twig
<sw-arrow-field
    v-if="options.length > 1"
    class="sw-product-stream-field-select"
    :class="{ 'has--error': hasError }"
    :primary="arrowPrimaryColor"
    secondary="#ffffff"
>
    <sw-single-select
        size="medium"
        :options="options"
        :value="field"
        :placeholder="$tc('sw-product-stream.filter.placeholderFieldSelect')"
        :disabled="disabled"
        show-clearable-button
        @update:value="changeField"
```

### Example 2
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-arrow-field
    ref="product-stream-value-operator-select"
    class="sw-product-stream-value__operator-select"
    :disabled="!acl.can('product_stream.editor')"
>
    <sw-single-select
        v-model:value="filterType"
        name="sw-field--filterType"
        size="medium"
        :options="operators"
        :placeholder="$tc('sw-product-stream.filter.placeholderOperatorSelect')"
        :disabled="disabled"
        show-clearable-button
    />
</sw-arrow-field>
```

### Example 3
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-arrow-field
    ref="product-stream-value-range-from-arrow-field"
    :disabled="disabled"
>
    <component
        :is="inputComponent"
        v-model:value="gte"
        size="medium"
        :disabled="disabled"
        :step="1"
    />
</sw-arrow-field>
```
