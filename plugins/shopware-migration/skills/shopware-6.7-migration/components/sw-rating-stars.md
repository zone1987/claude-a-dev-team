# sw-rating-stars

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| maxStars | `any` | `5` | no |  |
| iconSize | `any` | `16` | no |  |
| displayFractions | `any` | `4` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `ratingTooltip` | |
| `cappedValue` | |
| `partialStarCutStyle` | |
| `dynamicWidthStyle` | |

## Examples

### Example 1
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
                    <sw-rating-stars
                        :value="review.points"
                        class="star-count-display"
                    />

                    <div class="star-count-description">
                        {{ $tc(`sw-review.detail.review${Math.round(stars)}PointRatingText`) }}
                    </div>
                </div>
            </div>

            {% endblock %}
            {% endblock %}
        </div>
        {% endblock %}
```

### Example 2
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
<sw-rating-stars :value="item.points" />
```

### Example 3
Source: `sw-product/view/sw-product-detail-reviews/sw-product-detail-reviews.html.twig`
```twig
<sw-rating-stars :value="item.points" />
```
