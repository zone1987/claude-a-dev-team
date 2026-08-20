# sw-circle-icon

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `any` | `50` | no |  |
| iconName | `any` | — | yes |  |
| variant | `any` | `''` | no | Valid: `info`, `danger`, `success`, `warning`, `neutral`, `primary` |

## Computed Properties

| Name | Description |
|------|-------------|
| `iconSize` | |
| `backgroundStyles` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-adding-failed/sw-extension-adding-failed.html.twig`
```twig
<sw-circle-icon
    :size="72"
    icon-name="regular-times-circle-s"
    variant="danger"
/>
{% endblock %}

{% block sw_extension_adding_failed_headline %}
<h3>{{ title || headline }}</h3>
{% endblock %}

{% block sw_extension_adding_failed_notification %}
<p>{{ detail || text }}</p>
<p v-if="documentationLink">
    <a :href="documentationLink">
```

### Example 2
Source: `sw-extension/component/sw-extension-adding-success/sw-extension-adding-success.html.twig`
```twig
        <sw-circle-icon
            :size="72"
            icon-name="regular-checkmark"
            variant="success"
        />
        {% endblock %}

        {% block sw_extension_adding_success_headline %}
        <h3>{{ $tc('sw-extension-store.component.sw-extension-adding-success.titleSuccess') }}</h3>
        {% endblock %}

        {% block sw_extension_adding_success_sub_headline %}
        <p>{{ $tc('sw-extension-store.component.sw-extension-adding-success.subtitleSuccess') }}</p>
        {% endblock %}

```
