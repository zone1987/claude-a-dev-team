# sw-customer-default-addresses

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `renderFormattingAddress` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `defaultShippingAddressLink` | |
| `defaultBillingAddressLink` | |

## Examples

### Example 1
Source: `sw-customer/view/sw-customer-detail-base/sw-customer-detail-base.html.twig`
```twig
                <sw-customer-default-addresses
                    :customer-edit-mode="customerEditMode"
                    :customer="customer"
                />
            </template>
            {% endblock %}
        </mt-card>
        {% endblock %}

        {% block sw_customer_detail_custom_field_sets %}
        <mt-card
            v-if="!!customerCustomFieldSets && customerCustomFieldSets.length > 0"
            position-identifier="sw-customer-detail-base-custom-field-sets"
            :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
            :is-loading="customer.isLoading"
```
