# sw-product-visibility-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| criteria | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-label-property | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-add | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `addItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `repository` | |
| `associationRepository` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-visibility/sw-bulk-edit-product-visibility.html.twig`
```twig
        <sw-product-visibility-select
            ref="productVisibility"
            :key="isInherited"
            class="sw-product-detail__select-visibility"
            :entity-collection="currentValue"
            :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
            :disabled="disabled || undefined"
            @update:entity-collection="updateCurrentValue"
        />
    </template>
</sw-inherit-wrapper>
{% endblock %}

{% block sw_bulk_edit_product_visibility_advanced %}
<sw-container
```

### Example 2
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
            <sw-product-visibility-select
                v-if="!loading.product && !loading.parentProduct && multiSelectVisible"
                ref="productVisibility"
                :key="isInherited"
                class="sw-product-detail__select-visibility"
                :entity-collection="currentValue"
                :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
                :disabled="isInherited || !allowEdit"
                @update:entity-collection="updateCurrentValue"
            />
        </template>
    </sw-inherit-wrapper>
    {% endblock %}
</sw-container>

```
