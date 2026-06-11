# sw-users-permissions-configuration

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeLoading` | |

## Examples

### Example 1
Source: `sw-users-permissions/page/sw-users-permissions/sw-users-permissions.html.twig`
```twig
            <sw-users-permissions-configuration
                ref="configuration"
                @loading-change="onChangeLoading"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
