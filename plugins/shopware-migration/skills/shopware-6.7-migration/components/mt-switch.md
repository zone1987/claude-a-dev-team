# mt-switch

> Toggle switch input with label and optional bordered appearance.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `boolean` | — | no | |
| label | `string` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| inheritedValue | `boolean` | — | no | |
| required | `boolean` | — | no | |
| disabled | `boolean` | — | no | |
| checked | `boolean` | — | no | |
| bordered | `boolean` | — | no | |
| helpText | `string` | — | no | |
| error | `{ detail: string }` | — | no | |
| removeTopMargin | `boolean` | — | no | |
| name | `string` | — | no | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| update:modelValue | — | |
| inheritance-remove | — | |
| inheritance-restore | — | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<mt-switch
    :model-value="country.forceStateInRegistration"
    class="sw-settings-country-address-handling__option-items"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelForceStateInRegistration')"
    @update:model-value="updateCountry('forceStateInRegistration', $event)"
/>

<mt-switch
    :model-value="country.postalCodeRequired"
    class="sw-settings-country-address-handling__option-items"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelPostalCodeRequired')"
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
            <mt-switch
                :model-value="country.checkAdvancedPostalCodePattern"
                class="sw-settings-country-address-handling__option-items"
                :disabled="!acl.can('country.editor') || disabledAdvancedPostalCodePattern || undefined"
                :label="$tc('sw-settings-country.detail.labelCheckAdvancedPostalCodePattern')"
                :help-text="$tc('sw-settings-country.detail.helpTextAdvancedPostalCodePattern', {5: '{5}', 4: '{4}', 2: '{2}'}, 0)"
                @update:model-value="updateCountry('checkAdvancedPostalCodePattern', $event)"
            />

            <mt-text-field
                :model-value="country.advancedPostalCodePattern"
                class="sw-settings-country-address-handling__text-field"
                :class="{'is--disabled': !country.checkAdvancedPostalCodePattern}"
                :disabled="!acl.can('country.editor') || undefined"
                :placeholder="$tc('sw-settings-country.detail.placeholderAdvancedPostalCodePattern')"
```

### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-switch
    v-model="country.active"
    name="sw-field--country-active"
    class="sw-settings-country-general__option-items"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelActive')"
/>
{% endblock %}

{% block sw_settings_country_general_content_field_shipping_available %}

<mt-switch
    v-model="country.shippingAvailable"
    name="sw-field--country-shippingAvailable"
```

### Example 4
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<mt-switch
    v-model="country.companyTax.enabled"
    name="sw-field--country-companyTax-enabled"
    class="sw-settings-country-general__option-items switch-field-company-tax-free"
    bordered
    :disabled="!acl.can('country.editor') || undefined"
    :label="$tc('sw-settings-country.detail.labelCompanyTaxFree')"
    :help-text="$tc('sw-settings-country.detail.helpTextCompanyTaxFree')"
/>
{% endblock %}

<sw-container
    v-if="country.companyTax.enabled"
    class="sw-settings-country-general-company-tax"
>
```

### Example 5
Source: `sw-bulk-edit/component/sw-bulk-edit-order/sw-bulk-edit-order-documents-generate-invoice/sw-bulk-edit-order-documents-generate-invoice.html.twig`
```twig
    <mt-switch
        v-model="generateData.forceDocumentCreation"
        :label="$tc('sw-bulk-edit.order.documents.forceDocumentCreation')"
        :help-text="$tc('sw-bulk-edit.order.documents.forceDocumentCreationHelpText')"
    />
    {% endblock %}

    {% block sw_bulk_edit_order_documents_generate_invoice_placeholder %}
    {% endblock %}
</div>
{% endblock %}

```
