# sw-boolean-radio-group

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `true` | no |  |
| labelOptionTrue | `any` | — | yes |  |
| labelOptionFalse | `any` | — | yes |  |
| bordered | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `options` | |
| `castedValue` | |

## Examples

### Example 1
Source: `sw-settings-customer-group/page/sw-settings-customer-group-detail/sw-settings-customer-group-detail.html.twig`
```twig
            <sw-boolean-radio-group
                v-model:value="customerGroup.displayGross"
                bordered
                :label="$tc('sw-settings-customer-group.detail.fieldDisplayGrossLabel')"
                :label-option-true="$tc('sw-settings-customer-group.detail.fieldDisplayGrossValues', {}, 1)"
                :label-option-false="$tc('sw-settings-customer-group.detail.fieldDisplayGrossValues', {}, 0)"
                :disabled="!acl.can('customer_groups.editor') || undefined"
            />
            {% endblock %}

            <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks,vue/attributes-order -->
            {% block sw_settings_customer_group_detail_content_card_registration_form %}

            <mt-switch
                v-model="customerGroup.registrationActive"
```
