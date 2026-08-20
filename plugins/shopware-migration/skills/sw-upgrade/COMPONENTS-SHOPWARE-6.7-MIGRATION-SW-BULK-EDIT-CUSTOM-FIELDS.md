# sw-bulk-edit-custom-fields

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `initializeCustomFields` | |
| `toggleItemCheck` | |
| `updateCustomField` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <sw-bulk-edit-custom-fields
            class="sw-bulk-edit__custom-fields"
            :sets="customFieldSets"
            :entity="product"
            :parent-entity="parentProduct"
            @change="onCustomFieldsChange"
        />
    </mt-card>
    {% endblock %}
</sw-card-view>
<mt-empty-state
    v-if="!isLoading && selectedIds.length == 0"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-bulk-edit.product.messageEmptyTitle')"
    :description="$tc('sw-bulk-edit.product.messageEmptySubline')"
```

### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <sw-bulk-edit-custom-fields
            class="sw-bulk-edit__custom-fields"
            :sets="customFieldSets"
            @change.self="onCustomFieldsChange"
        />
    </mt-card>
    {% endblock %}
</sw-card-view>

{% block sw_bulk_edit_order_empty_state %}
<mt-empty-state
    v-if="selectedIds.length <= 0 && !isLoading"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-bulk-edit.order.messageEmptyTitle')"
    :description="$tc('sw-bulk-edit.order.messageEmptySubline')"
```

### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
            <sw-bulk-edit-custom-fields
                class="sw-bulk-edit__custom-fields"
                :sets="customFieldSets"
                @change="onCustomFieldsChange"
            />
        </template>
    </mt-card>
    {% endblock %}
</sw-card-view>

{% block sw_bulk_edit_customer_empty_state %}
<mt-empty-state
    v-if="selectedIds.length <= 0 && !isLoading"
    icon="solid-users"
    :headline="$tc('sw-bulk-edit.customer.messageEmptyTitle')"
```
