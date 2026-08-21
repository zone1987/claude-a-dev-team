# sw-extension-review-reply

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| reply | `any` | — | yes |  |
| producerName | `any` | — | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `creationDate` | |

## Examples

### Example 1
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
