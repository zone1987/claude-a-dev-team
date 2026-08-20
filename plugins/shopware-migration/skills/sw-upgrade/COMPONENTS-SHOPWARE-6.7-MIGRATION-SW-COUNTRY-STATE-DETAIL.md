# sw-country-state-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| countryState | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| attribute-edit-cancel | — | |
| attribute-edit-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `tooltipSave` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
    <sw-country-state-detail
        v-if="currentCountryState"
        :country-state="currentCountryState"
        @attribute-edit-save="onSaveCountryState"
        @attribute-edit-cancel="onCancelCountryState"
    />
    {% endblock %}
</mt-card>
{% endblock %}


```
