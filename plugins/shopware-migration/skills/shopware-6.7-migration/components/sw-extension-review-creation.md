# sw-extension-review-creation

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| created | — | |

## Methods

| Method | Description |
|--------|-------------|
| `handleCreateReview` | |
| `createReview` | |
| `validateInputs` | |
| `validateHeadline` | |
| `validateRating` | |
| `onChange` | |
| `emitCreated` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentUser` | |
| `userName` | |
| `installedVersion` | |
| `hasError` | |
| `disabled` | |

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

### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-card/sw-extension-ratings-card.html.twig`
```twig
        <sw-extension-review-creation
            :extension="extension"
            @created="$emit('update-extension')"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-meteor-card>
{% endblock %}

```
