# sw-address

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| address | `any` | — | no |  |
| headline | `any` | `''` | no |  |
| formattingAddress | `any` | `null` | no |  |
| showEditButton | `any` | `false` | no |  |
| editLink | `any` | `null` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `addressClasses` | |
| `displayFormattingAddress` | |

## Examples

### Example 1
Source: `sw-customer/component/sw-customer-default-addresses/sw-customer-default-addresses.html.twig`
```twig
        <sw-address
            :address="customer.defaultShippingAddress"
            :headline="$tc('sw-customer.detailBase.titleDefaultShippingAddress')"
            :show-edit-button="customerEditMode"
            :edit-link="defaultShippingAddressLink"
            :formatting-address="formattingShippingAddress"
        />
        {% endblock %}
    </sw-card-section>
    {% endblock %}

    {% block sw_customer_default_addresses_billing %}
    <sw-card-section v-if="customer.defaultBillingAddress.id">
        {% block sw_customer_default_addresses_billing_postal %}
        <sw-address
```

### Example 2
Source: `sw-customer/view/sw-customer-detail-addresses/sw-customer-detail-addresses.html.twig`
```twig
    <sw-address
        class="sw-customer-detail-addresses__confirm-delete-address"
        :address="item"
    />
    {% endblock %}

    {% block sw_customer_detail_addresses_delete_modal_footer %}
    <template #modal-footer>
        {% block sw_customer_detail_addresses_delete_modal_cancel %}
        <mt-button
            size="small"
            variant="secondary"
            @click="onCloseDeleteAddressModal"
        >
            {{ $tc('global.default.cancel') }}
```

### Example 3
Source: `sw-order/component/sw-order-delivery-metadata/sw-order-delivery-metadata.html.twig`
```twig
            <sw-address
                class="sw-order-delivery-metdata__address"
                :headline="$tc('sw-order.detailBase.headlineDeliveryAddress')"
                :address="delivery.shippingOrderAddress"
                :formatting-address="formattingAddress"
            />
            {% block sw_order_delivery_metadata_delivery_phone_number %}
            <dt>{{ $tc('sw-order.detailBase.labelCustomerPhoneNumber') }}</dt>
            <dd v-if="delivery.shippingOrderAddress.phoneNumber">
                {{ delivery.shippingOrderAddress.phoneNumber }}
            </dd>
            <dd v-else>
                {{ $tc('sw-order.detailBase.labelNoPhoneNumber') }}
            </dd>
            {% endblock %}
```

### Example 4
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
        <sw-address
            :address="billingAddress"
            :formatting-address="formattingAddress"
        />
    </dd>
    {% endblock %}

    {% block sw_order_detail_base_order_overview_left_column_slot %}
    {% endblock %}

</sw-description-list>
{% endblock %}

{% block sw_order_detail_base_order_overview_right_column %}
<sw-description-list
```

### Example 5
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
                <sw-address
                    :address="delivery.shippingOrderAddress"
                    :formatting-address="formattingAddress"
                />
            </dd>

            <dd v-else>
                {{ $tc('sw-order.detailBase.labelNoDeliveriesYet') }}
            </dd>
            {% endblock %}

            {% block sw_order_detail_base_order_overview_right_column_slot %}
            {% endblock %}

        </sw-description-list>
```
