# sw-custom-field-set-detail-base

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| set | `any` | — | yes |  |
| technicalNameError | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| reset-errors | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onAddRelation` | |
| `onRemoveRelation` | |
| `searchRelationEntityNames` | |
| `onTechnicalNameChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `locales` | |
| `customFieldSetRelationRepository` | |
| `selectedRelationEntityNames` | |
| `relationEntityNames` | |

## Examples

### Example 1
Source: `sw-settings-custom-field/page/sw-settings-custom-field-set-detail/sw-settings-custom-field-set-detail.html.twig`
```twig
                <sw-custom-field-set-detail-base
                    :set="set"
                    :technical-name-error="technicalNameError"
                    @reset-errors="onResetErrors"
                />
                {% endblock %}

                {% block sw_settings_custom_field_set_detail_content_detail_custom_field_list %}
                <sw-custom-field-list
                    v-if="set.id"
                    ref="customFieldList"
                    :set="set"
                    @loading-changed="onLoadingChanged"
                />
                {% endblock %}
```
