# sw-gtc-checkbox

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation/sw-extension-review-creation.html.twig`
```twig
    <sw-gtc-checkbox
        v-model:value="tocAccepted"
    />
    {% endblock %}

    {% block sw_extension_review_creation_buttons %}
    <div class="sw-extension-review-creation__buttons">
        {% block sw_extension_review_creation_buttons_submit_button %}
        <sw-button-process
            class="sw-extension-review-creation__submit"
            variant="primary"
            size="small"
            :is-loading="isLoading"
            :process-success="isCreatedSuccessful"
            :disabled="disabled"
```

### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-rating-modal/sw-extension-rating-modal.html.twig`
```twig
<sw-gtc-checkbox
    v-model:value="tocAccepted"
/>
{% endblock %}

{% block sw_extension_rating_modal_slot_footer_buttons %}
<div class="sw-extension-rating-modal__buttons">
    {% block sw_extension_rating_modal_slot_footer_buttons_cancel %}
    <mt-button
        size="small"
        :disabled="isLoading"
        variant="secondary"
        @click="emitClose"
    >
        {{ $tc('global.default.cancel') }}
```
