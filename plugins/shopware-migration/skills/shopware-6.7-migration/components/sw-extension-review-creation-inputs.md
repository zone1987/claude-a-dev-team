# sw-extension-review-creation-inputs

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| errors | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| changed | — | |

## Examples

### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation/sw-extension-review-creation.html.twig`
```twig
<sw-extension-review-creation-inputs
    :errors="errors"
    @changed="onChange"
/>
{% endblock %}

{% block sw_extension_review_creation_gtc_checkbox %}
<sw-gtc-checkbox
    v-model:value="tocAccepted"
/>
{% endblock %}

{% block sw_extension_review_creation_buttons %}
<div class="sw-extension-review-creation__buttons">
    {% block sw_extension_review_creation_buttons_submit_button %}
```

### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-rating-modal/sw-extension-rating-modal.html.twig`
```twig
    <sw-extension-review-creation-inputs
        :errors="errors"
        @changed="onChange"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_extension_rating_modal_slot_footer %}
<template #modal-footer>
    {% block sw_extension_rating_modal_slot_footer_gtc_checkbox %}
    <sw-gtc-checkbox
        v-model:value="tocAccepted"
    />
    {% endblock %}
```
