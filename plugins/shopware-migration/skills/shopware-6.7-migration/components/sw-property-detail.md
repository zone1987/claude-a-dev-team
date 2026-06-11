# sw-property-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| groupId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `saveFinish` | |
| `saveOnLanguageChange` | |
| `abortOnLanguageChange` | |
| `onChangeLanguage` | |
| `onSave` | |
| `onCancel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `optionRepository` | |
| `propertyRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `defaultCriteria` | |
| `useNaturalSorting` | |
| `showCustomFields` | |

## Examples

### Example 1
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
<sw-property-detail-base
    v-if="propertyGroup"
    :property-group="propertyGroup"
    :allow-edit="acl.can('property.editor')"
/>
{% endblock %}

{% block sw_property_detail_content_option_list %}
<sw-property-option-list
    v-if="propertyGroup"
    ref="optionListing"
    :is-loading="isLoading || undefined"
    :option-repository="optionRepository"
    :property-group="propertyGroup"
/>
```
