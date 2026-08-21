# sw-extension-rating-stars

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| editable | `any` | `false` | no |  |
| size | `any` | `8` | no |  |
| rating | `any` | `0` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:rating | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `colorClass` | |
| `addRating` | |
| `showPartialStar` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `editableClass` | |
| `sizeValue` | |
| `starSize` | |
| `partialStarSize` | |
| `partialStarWidth` | |
| `defaultSizeForEditable` | |
| `scaleFactor` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review/sw-extension-review.html.twig`
```twig
<sw-extension-rating-stars
    :rating="review.rating"
    :size="12"
/>
{% endblock %}

{% block sw_extension_review_text %}
<p
    v-if="review.text"
    class="sw-extension-review__text"
>
    {{ review.text }}
</p>
{% endblock %}

```

### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-select-rating/sw-extension-select-rating.html.twig`
```twig
        <sw-extension-rating-stars
            v-model:rating="currentValue"
            editable
            @update:rating="onChange"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-base-field>
    {% endblock %}
{% endblock %}

```

### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-summary/sw-extension-ratings-summary.html.twig`
```twig
        <sw-extension-rating-stars
            :rating="Number(ratingGroup.rating)"
            :size="12"
        />
        {% endblock %}
    </template>
</div>
{% endblock %}

{% block sw_extension_ratings_summary_grid_rating_progress_bars %}
<div class="sw-extension-ratings-summary__progress-bars">
    {% block sw_extension_ratings_summary_grid_rating_progress_bars_count_rows %}
    <div class="sw-extension-ratings-summary__rows">
        <template
            v-for="ratingGroup in summary.ratingAssignment"
```
