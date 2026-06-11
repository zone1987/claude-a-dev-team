# sw-data-grid-column-position

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| item | `any` | — | yes |  |
| field | `any` | `'position'` | no |  |
| showValue | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| lower-position-value | — | |
| position-changed | — | |
| raise-position-value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onLowerPositionValue` | |
| `onRaisePositionValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `itemMin` | |
| `itemMax` | |

## Examples

### Example 1
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-values-card/sw-settings-product-feature-sets-values-card.html.twig`
```twig
                <sw-data-grid-column-position
                    ref="columnPosition"
                    v-model:value="values"
                    :show-value="false"
                    :item="item"
                    :disabled="!allowEdit || undefined"
                    @position-changed="onPositionChange"
                />
            </template>
            {% endblock %}

        </sw-data-grid>
        {% endblock %}

    </div>
```

### Example 2
Source: `sw-product/component/sw-product-cross-selling-assignment/sw-product-cross-selling-assignment.html.twig`
```twig
                <sw-data-grid-column-position
                    ref="columnPosition"
                    v-model:value="assignedProducts"
                    :show-value="true"
                    :item="item"
                />
            </template>
            {% endblock %}
        </sw-data-grid>
        {% endblock %}
        {% block sw_product_cross_selling_assignment_empty_state %}
        <mt-empty-state
            v-if="!total && !isLoadingGrid"
            class="sw-product-cross-selling-assignment__option-list-empty-state"
            :icon="$route.meta.$module.icon"
```
