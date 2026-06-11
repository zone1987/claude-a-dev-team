# sw-extension-review

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| review | `any` | — | yes |  |
| producerName | `any` | — | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `lastChangeDate` | |
| `reviewHasReplies` | |

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
Source: `sw-extension/component/sw-ratings/sw-extension-review/sw-extension-review.html.twig`
```twig
        <sw-extension-review-reply
            v-for="(reply, index) in review.replies"
            :key="`sw-extension-review__reply-${index}`"
            :producer-name="producerName"
            :reply="reply"
        />
        {% endblock %}
    </template>
    {% endblock %}
</div>
{% endblock %}

```

### Example 3
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

### Example 4
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-card/sw-extension-ratings-card.html.twig`
```twig
        <sw-extension-review
            v-for="(review, index) in reviews"
            :key="`sw-extension-ratings-card__reviews-review-${index}`"
            :producer-name="producerName"
            :review="review"
        />
        {% endblock %}

        {% block sw_extension_ratings_card_has_reviews_wrapper_more_button %}
        <mt-button
            v-if="canShowMore"
            size="small"
            variant="secondary"
            @click="loadMoreReviews"
        >
```

### Example 5
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
