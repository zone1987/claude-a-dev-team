# sw-extension-select-rating

> Shopware Administration component.

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
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation-inputs/sw-extension-review-creation-inputs.html.twig`
```twig
            <sw-extension-select-rating
                v-model:value="rating"
                :error="errors.ratingError"
                required
                :label="$tc('sw-extension-store.component.sw-extension-ratings.sw-extension-review-creation-inputs.labelRating')"
            />
            {% endblock %}
        </div>
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_extension_review_creation_inputs_description_input %}
    <mt-textarea
        v-model="text"
```
