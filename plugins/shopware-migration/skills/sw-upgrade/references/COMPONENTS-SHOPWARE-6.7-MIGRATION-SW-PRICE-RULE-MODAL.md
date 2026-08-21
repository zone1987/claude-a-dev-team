# sw-price-rule-modal

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |

## Examples

### Example 1
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrix/sw-settings-shipping-price-matrix.html.twig`
```twig
            <sw-price-rule-modal
                v-if="showRuleModal"
                rule-aware-group-key="shippingMethodPriceCalculations"
                @save="onSaveRule"
                @modal-close="onCloseRuleModal"
            />
        </template>
    </sw-select-rule-create>
</template>
{% endblock %}
{% block sw_settings_shipping_price_matrix_price_grid_column_quantity_start %}
<template
    #column-quantityStart="{ item, itemIndex, compact }"
>
    <mt-number-field
```

### Example 2
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrix/sw-settings-shipping-price-matrix.html.twig`
```twig
                    <sw-price-rule-modal
                        v-if="showRuleModal"
                        rule-aware-group-key="shippingMethodPriceCalculations"
                        @save="onSaveRule"
                        @modal-close="onCloseRuleModal"
                    />
                </template>
            </sw-select-rule-create>
            {% endblock %}
        </sw-container>
    </div>
    {% endblock %}
</template>

{% block sw_settings_shipping_price_matrix_delete_modal %}
```
