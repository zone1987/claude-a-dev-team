# mt-textarea

> Multi-line text input with label and error handling.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| required | `boolean` | — | no | |
| disabled | `boolean` | — | no | |
| name | `string` | — | no | |
| label | `string` | — | no | |
| placeholder | `string` | — | no | |
| error | `{` | — | no | |
| detail | `string` | — | yes | |
| helpText | `string` | — | no | |
| maxLength | `number` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-remove | — | |
| inheritance-restore | — | |
| change | — | |
| focus | — | |
| blur | — | |

## Examples

### Example 1
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
            <mt-textarea
                v-if="activeTab === 'raw'"
                :model-value="displayString"
            />
            {% endblock %}
            {% endblock %}
        </template>

    </sw-tabs>
    {% endblock %}

    {% block sw_settings_logging_entry_info_footer %}
    <template #modal-footer>
        {% block sw_settings_logging_entry_info_close_button %}
        <mt-button
```

### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-invoice/sw-bulk-edit-order-documents-generate-invoice.html.twig`
```twig
    <mt-textarea
        v-model="generateData.documentComment"
        :label="$tc('sw-bulk-edit.order.documents.generateInvoice.labelTextarea')"
        :placeholder="$tc('sw-bulk-edit.order.documents.generateInvoice.placeholderTextarea')"
    />
    {% endblock %}

    {% block sw_bulk_edit_order_documents_generate_invoice_toggle_skip %}

    <mt-switch
        v-model="generateData.forceDocumentCreation"
        :label="$tc('sw-bulk-edit.order.documents.forceDocumentCreation')"
        :help-text="$tc('sw-bulk-edit.order.documents.forceDocumentCreationHelpText')"
    />
    {% endblock %}
```

### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation-inputs/sw-extension-review-creation-inputs.html.twig`
```twig
    <mt-textarea
        v-model="text"
        :label="$tc('sw-extension-store.component.sw-extension-ratings.sw-extension-review-creation-inputs.labelText')"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 4
Source: `sw-settings-product-feature-sets/page/sw-settings-product-feature-sets-detail/sw-settings-product-feature-sets-detail.html.twig`
```twig
                    <mt-textarea
                        v-model="productFeatureSet.description"
                        :label="$tc('sw-settings-product-feature-sets.detail.labelDescription')"
                        class="sw-settings-product-feature-sets-detail__description"
                        :error="productFeatureSetDescriptionError"
                        :disabled="!acl.can('product_feature_sets.editor')"
                        :placeholder="placeholder(productFeatureSet, 'description', $tc('sw-settings-product-feature-sets.detail.placeholderDescription'))"
                    />
                    {% endblock %}

                </mt-card>
                {% endblock %}

                {% block sw_settings_product_feature_set_detail_content_values_card %}
                <sw-settings-product-feature-sets-values-card
```

### Example 5
Source: `sw-property/component/sw-property-detail-base/sw-property-detail-base.html.twig`
```twig
<mt-textarea
    v-model="propertyGroup.description"
    name="sw-field--propertyGroup-description"
    :label="$tc('sw-property.detail.labelDescription')"
    :placeholder="placeholder(propertyGroup, 'description', $tc('sw-property.detail.placeholderDescription'))"
    :disabled="!allowEdit"
/>
{% endblock %}

{% block sw_property_detail_filter_visible_container %}
<sw-container
    columns="repeat(2, 1fr)"
    gap="0px 30px"
>
    {% block sw_property_detail_base_filterable %}
```
