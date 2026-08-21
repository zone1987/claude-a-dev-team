# sw-custom-field-translated-labels

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| locales | `any` | `[]` | yes |  |
| config | `any` | — | yes |  |
| propertyNames | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initializeConfiguration` | |
| `getLabel` | |
| `onInput` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `fallbackLocale` | |
| `localeCount` | |

## Examples

### Example 1
Source: `sw-settings-custom-field/component/sw-custom-field-set-detail-base/sw-custom-field-set-detail-base.html.twig`
```twig
<sw-custom-field-translated-labels
    v-if="set.config"
    v-model:config="set.config"
    :disabled="!acl.can('custom_field.editor') || undefined"
    :property-names="propertyNames"
    :locales="locales"
/>
{% endblock %}

{% block sw_settings_custom_field_set_detail_base_multi_select %}
<sw-multi-select
    id="entities"
    class="sw-settings-custom-field-set-detail-base__label-entities"
    :disabled="!acl.can('custom_field.editor') || undefined"
    :label="$tc('sw-settings-custom-field.set.detail.labelEntities')"
```

### Example 2
Source: `sw-settings-custom-field/component/sw-custom-field-type-base/sw-custom-field-type-base.html.twig`
```twig
    <sw-custom-field-translated-labels
        v-model:config="currentCustomField.config"
        :disabled="!acl.can('custom_field.editor')"
        :property-names="propertyNames"
        :locales="locales"
    />
    {% endblock %}
    {% endblock %}
</div>
{% endblock %}

```
