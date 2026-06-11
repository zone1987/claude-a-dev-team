# sw-bulk-edit-change-type-field-renderer

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| bulkEditData | `any` | — | yes |  |
| formFields | `any` | — | yes |  |
| entity | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| valueFieldWithBoxType | — | |
| valueField | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-value | — | |
| update:default-unit | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `hasFormFieldConfig` | |
| `getConfigValue` | |
| `showSelectBoxType` | |
| `onChangeValue` | |
| `onChangeToggle` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
    <sw-bulk-edit-change-type-field-renderer
        :form-fields="generalFormFields"
        :bulk-edit-data="bulkEditProduct"
        :entity="product"
        @inheritance-restore="onInheritanceRestore"
        @inheritance-remove="onInheritanceRemove"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_bulk_edit_product_content_prices_card %}
<mt-card
    class="sw-bulk-edit-product-base__prices"
    position-identifier="sw-bulk-edit-product-prices"
```

### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-bulk-edit-change-type-field-renderer
    :form-fields="advancedPricesFormFields"
    :bulk-edit-data="bulkEditProduct"
    :entity="product"
>
    <template #valueFieldWithBoxType="{ formField, entity, index }">
        <sw-inheritance-switch
            v-if="isChild"
            :is-inherited="bulkEditProduct[formField.name].isInherited"
            @inheritance-restore="onInheritanceRestore(formField)"
            @inheritance-remove="onInheritanceRemove(formField)"
        />

        <a
            v-if="['add', 'overwrite'].includes(bulkEditProduct[formField.name].type)"
```

### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
    <sw-bulk-edit-change-type-field-renderer
        :form-fields="statusFormFields"
        :bulk-edit-data="bulkEditData"
        :entity="order"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_bulk_edit_order_content_documents %}
<mt-card
    class="sw-bulk-edit-order-base__documents"
    position-identifier="sw-bulk-edit-order-documents"
    :title="$tc('sw-bulk-edit.order.documents.cardTitle')"
    :is-loading="isLoading"
```

### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <sw-bulk-edit-change-type-field-renderer
            :form-fields="tagsFormFields"
            :bulk-edit-data="bulkEditData"
            :entity="order"
        />
        {% endblock %}
    </mt-card>
    {% endblock %}

    {% block sw_bulk_edit_order_custom_field_card %}
    <mt-card
        class="sw-bulk-edit-order-base__custom_fields"
        position-identifier="sw-bulk-edit-order-custom-fields"
        :title="$tc('sw-bulk-edit.order.customFields.cardTitle')"
        :is-loading="isLoading"
```

### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
        <sw-bulk-edit-change-type-field-renderer
            :form-fields="accountFormFields"
            :bulk-edit-data="bulkEditData"
            :entity="customer"
        />
        {% endblock %}
    </template>
</mt-card>
{% endblock %}

{% block sw_bulk_edit_customer_tags_card %}
<mt-card
    class="sw-bulk-edit-customer-base__tags"
    position-identifier="sw-bulk-edit-customer-tags"
    :title="$tc('sw-bulk-edit.customer.tags.cardTitle')"
```
