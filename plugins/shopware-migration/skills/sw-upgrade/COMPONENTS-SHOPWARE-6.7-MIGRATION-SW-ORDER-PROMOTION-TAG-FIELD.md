# sw-order-promotion-tag-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currency | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| on-remove-code | — | |

## Methods

| Method | Description |
|--------|-------------|
| `performAddTag` | |
| `dismissTag` | |
| `setFocus` | |
| `getPromotionCodeDescription` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `taggedFieldListClasses` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-promotion-field/sw-order-promotion-field.html.twig`
```twig
<sw-order-promotion-tag-field
    v-model:value="promotionCodeTags"
    :disabled="!hasLineItem || isLoading || !acl.can('order.editor') || undefined"
    :currency="currency"
    :label="$t('sw-order.detailsTab.promotionsField.labelPromotions')"
    :placeholder="$t('sw-order.detailsTab.promotionsField.placeholderPromotions')"
    :error="promotionError"
    @on-remove-code="onRemoveExistingCode"
/>
{% endblock %}

{% block sw_order_promotion_field_switch %}
<h3 class="sw-order-promotion-field__apply_auto_promotions__title">
    {{ $t('sw-order.detailsTab.promotionsField.automaticPromotions.title') }}
</h3>
```

### Example 2
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
        <sw-order-promotion-tag-field
            v-model:value="promotionCodeTags"
            :disabled="!hasLineItem"
            :currency="currency"
            :label="$tc('sw-order.createBase.labelAddPromotion')"
            :placeholder="$tc('sw-order.createBase.placeholderAddPromotion')"
            :error="promotionError"
            @on-remove-code="onRemoveExistingCode"
        />
        {% endblock %}

        {% block sw_order_create_details_switch_disable_auto_promotion %}

        <mt-switch
            class="sw-order-create-details__disable-auto-promotion"
```

### Example 3
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
    <sw-order-promotion-tag-field
        v-model:value="promotionCodeTags"
        :disabled="!hasLineItem"
        :currency="currency"
        :label="$tc('sw-order.createBase.labelAddPromotion')"
        :placeholder="$tc('sw-order.createBase.placeholderAddPromotion')"
        :error="promotionError"
        @on-remove-code="onRemoveExistingCode"
    />
    {% endblock %}
</div>
<sw-description-list
    grid="1fr 1fr"
    class="sw-order-create-summary__data"
>
```
