# mt-email-field

> Email input field with built-in validation.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `boolean` | — | no | |
| required | `boolean` | — | no | |
| modelValue | `string` | — | no | |
| name | `string` | — | no | |
| label | `string` | — | no | |
| error | `{` | — | no | |
| detail | `string` | — | yes | |
| helpText | `string` | — | no | |
| copyable | `boolean` | — | no | |
| copyableTooltip | `boolean` | — | no | |
| placeholder | `string` | — | no | |
| small | `boolean` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| prefix | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| blur | — | |
| focus | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Examples

### Example 1
Source: `sw-customer/component/sw-customer-base-form/sw-customer-base-form.html.twig`
```twig
<mt-email-field
    v-model="customer.email"
    name="sw-field--customer-email"
    required
    :label="$tc('sw-customer.baseForm.labelEmail')"
    :placeholder="$tc('sw-customer.baseForm.placeholderEmail')"
    :error="customerEmailError"
/>
{% endblock %}

{% block sw_customer_base_form_password_field %}
<mt-password-field
    v-model="customer.password"
    name="sw-field--customer-password"
    autocomplete="new-password"
```

### Example 2
Source: `sw-customer/component/sw-customer-card/sw-customer-card.html.twig`
```twig
<mt-email-field
    v-else
    v-model="customer.email"
    name="sw-field--customer-email"
    validation="required"
    required
    :label="$tc('sw-customer.card.labelEmail')"
    :placeholder="$tc('sw-customer.card.placeholderEmail')"
    :error="customerEmailError"
/>
{% endblock %}
{% endblock %}

{% block sw_customer_card_password %}
<mt-password-field
```
