# sw-product-stream-field-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| definition | `any` | — | yes |  |
| field | `any` | `null` | no |  |
| index | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| hasError | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| field-changed | — | |

## Methods

| Method | Description |
|--------|-------------|
| `changeField` | |
| `getPropertyTranslation` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `options` | |
| `arrowPrimaryColor` | |

## Examples

### Example 1
Source: `sw-product-stream/component/sw-product-stream-filter/sw-product-stream-filter.html.twig`
```twig
        <sw-product-stream-field-select
            v-bind="{ field: fields[index], definition, index }"
            :disabled="!acl.can('product_stream.editor') || undefined"
            :has-error="hasError"
            @field-changed="updateFields"
        />
        {% endblock %}
    </template>
    {% endblock %}

    {% block sw_product_stream_filter_value %}
    <sw-product-stream-value
        v-bind="{ condition, ...lastField }"
        :disabled="!acl.can('product_stream.editor') || undefined"
        @type-change="changeType"
```
