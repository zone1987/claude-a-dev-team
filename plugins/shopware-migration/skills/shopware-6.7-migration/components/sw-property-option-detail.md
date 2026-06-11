# sw-property-option-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentOption | `any` | — | no |  |
| allowEdit | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| cancel-option-edit | — | |
| save-option-edit | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `onCancel` | |
| `onSave` | |
| `successfulUpload` | |
| `removeMedia` | |
| `setMedia` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `colorHexCode` | |
| `modalTitle` | |
| `currentOptionNameError` | |
| `showCustomFields` | |

## Examples

### Example 1
Source: `sw-property/component/sw-property-option-list/sw-property-option-list.html.twig`
```twig
    <sw-property-option-detail
        v-if="currentOption"
        :current-option="currentOption"
        :allow-edit="acl.can('property.editor')"
        @save-option-edit="onSaveOption"
        @cancel-option-edit="onCancelOption"
    />
    {% endblock %}

    {% block sw_property_option_list_loader %}
    <sw-loader v-if="isLoading" />
    {% endblock %}
</mt-card>
{% endblock %}

```
