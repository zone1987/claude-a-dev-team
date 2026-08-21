# mt-datepicker

> Date/time picker with calendar and various date format support.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | — | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-invoice/sw-bulk-edit-order-documents-generate-invoice.html.twig`
```twig
    <mt-datepicker
        v-model="generateData.documentDate"
        class="sw-bulk-edit-order-documents-generate-invoice__item"
        hide-hint
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelDatePicker')"
        :placeholder="$tc('sw-datepicker.date.placeholder')"
    />
    {% endblock %}

    {% block sw_bulk_edit_order_documents_generate_invoice_textarea %}
    <mt-textarea
        v-model="generateData.documentComment"
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelTextarea')"
        :placeholder="$tc('sw-bulk-edit.order.documents.generateInvoice.placeholderTextarea')"
    />
```

### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-delivery-note/sw-bulk-edit-order-documents-generate-delivery-note.html.twig`
```twig
    <mt-datepicker
        v-model="generateData.custom.deliveryDate"
        class="sw-bulk-edit-order-documents-generate-invoice__item"
        hide-hint
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelDatePicker')"
        :placeholder="$tc('sw-datepicker.date.placeholder')"
    />
    <mt-datepicker
        v-model="generateData.custom.deliveryNoteDate"
        class="sw-bulk-edit-order-documents-generate-invoice__item"
        hide-hint
        :label="$tc('sw-bulk-edit.order.documents.generateDeliveryNote.labelDeliveryDatePicker')"
        :placeholder="$tc('sw-datepicker.date.placeholder')"
    />
</template>
```

### Example 3
Source: `sw-settings-tax/component/sw-settings-tax-rule-modal/sw-settings-tax-rule-modal.html.twig`
```twig
    <mt-datepicker
        v-model="taxRule.activeFrom"
        date-type="datetime"
        :error="taxRuleActiveFromError"
        :label="$tc('sw-settings-tax.taxRuleCard.labelActiveFrom')"
        :placeholder="$tc('sw-datepicker.datetime.placeholder')"
    />
    {% endblock %}
</sw-container>
{% endblock %}

{% block sw_settings_tax_rule_modal_form_footer %}
<template #modal-footer>
    {% block sw_settings_tax_rule_modal_form_footer_cancel %}
    <mt-button
```

### Example 4
Source: `sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig`
```twig
    <mt-datepicker
        v-model="promotion.validFrom"
        class="sw-promotion-v2-detail-base__field-valid-from"
        date-type="datetime"
        :label="$tc('sw-promotion-v2.detail.base.general.validFromLabel')"
        :placeholder="$tc('sw-promotion-v2.detail.base.general.validFromPlaceholder')"
        :disabled="!acl.can('promotion.editor')"
    />
    {% endblock %}

    {% block sw_promotion_v2_detail_base_general_valid_until %}
    <mt-datepicker
        v-model="promotion.validUntil"
        class="sw-promotion-v2-detail-base__field-valid-until"
        date-type="datetime"
```

### Example 5
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
<mt-datepicker
    v-else-if="type === 'date'"
    class="sw-custom-entity-input-field__date"
    hide-hint
    :model-value="currentValue"
    :label="label"
    :placeholder="placeholder"
    :help-text="helpText"
    @update:model-value="onChange"
/>

<!-- ToDo NEXT-22874 - Implement email-field verification to entity_schema
<sw-email-field
    v-else-if="type === 'email'"
    class="sw-custom-entity-input-field__email"
```
