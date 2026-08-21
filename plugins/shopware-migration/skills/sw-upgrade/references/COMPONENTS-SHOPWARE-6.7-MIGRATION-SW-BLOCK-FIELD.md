# sw-block-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `any` | `'default'` | no | Valid: `small`, `medium`, `default` |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-field-input | — | |
| hint | — | |
| label | — | |

## Methods

| Method | Description |
|--------|-------------|
| `setFocusClass` | |
| `removeFocusClass` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swBlockSize` | |
| `swBlockFieldClasses` | |

## Examples

### Example 1
Source: `sw-cms/elements/buy-box/component/sw-cms-el-buy-box.html.twig`
```twig
<sw-block-field class="sw-cms-el-buy-box__quantity">
    <template #sw-field-input>
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <select>
            <option
                :value="product.minPurchase"
                selected
            >
                {{ product.minPurchase }}
            </option>
        </select>
        <div class="sw-cms-el-buy-box__icon">
            <mt-icon
                name="regular-chevron-up-xxs"
                decorative
```

### Example 2
Source: `sw-cms/elements/buy-box/component/sw-cms-el-buy-box.html.twig`
```twig
<sw-block-field class="sw-cms-el-buy-box__quantity">
    <template #sw-field-input>
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <select>
            <option
                value="1"
                selected
            >
                1
            </option>
        </select>
        <div class="sw-cms-el-buy-box__icon">
            <mt-icon
                name="regular-chevron-up-xxs"
                size="16px"
```

### Example 3
Source: `sw-order/component/sw-order-promotion-tag-field/sw-order-promotion-tag-field.html.twig`
```twig
<sw-block-field
    class="sw-tagged-field sw-order-promotion-tag-field"
    :class="taggedFieldClasses"
    v-bind="$attrs"
    :disabled="disabled"
>
    <template #sw-field-input="{ identification, error, disabled, size, setFocusClass, removeFocusClass }">

        {% block sw_tagged_field_inner %}
        <ul
            class="sw-tagged-field__tag-list"
            :class="taggedFieldListClasses"
            role="listbox"
            tabindex="0"
            @click="setFocus(true)"
```
