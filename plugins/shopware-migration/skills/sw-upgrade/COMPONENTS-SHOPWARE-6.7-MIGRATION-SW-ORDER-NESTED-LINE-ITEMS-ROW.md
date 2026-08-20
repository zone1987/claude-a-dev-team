# sw-order-nested-line-items-row

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| lineItem | `any` | — | yes |  |
| currency | `any` | — | yes |  |
| renderParent | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getNestingClasses` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-nested-line-items-row/sw-order-nested-line-items-row.html.twig`
```twig
        <sw-order-nested-line-items-row
            v-for="child in lineItem.children"
            :key="child.id"
            :line-item="child"
            :currency="currency"
            :render-parent="true"
        />
    </template>
    {% endblock %}

</div>
{% endblock %}

```

### Example 2
Source: `sw-order/component/sw-order-nested-line-items-modal/sw-order-nested-line-items-modal.html.twig`
```twig
        <sw-order-nested-line-items-row
            class="sw-order-nested-line-items-modal__content"
            :line-item="lineItem"
            :currency="order.currency"
        />
        {% endblock %}

    </div>
    {% endblock %}

    {% block sw_order_nested_line_item_modal_footer %}
    <template #modal-footer>

        {% block sw_order_nested_line_item_modal_footer_content %}
        <mt-button
```
