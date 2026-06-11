# sw-data-grid-column-boolean

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isInlineEdit | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| value | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.searchable" />
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.tokenize" />
```

### Example 3
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
    <sw-data-grid-column-boolean
        v-model:value="item.status"
        :is-inline-edit="false"
    />
</template>
{% endblock %}

{% block sw_review_list_content_list_title %}
<template #column-title="{ item }">
    <div class="sw-review-text_ellipsis">
        <router-link :to="{ name: 'sw.review.detail', params: { id: item.id } }">
            {{ item.title }}
        </router-link>
    </div>
</template>
```

### Example 4
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
                <sw-data-grid-column-boolean
                    :value="item.comment && item.comment.length > 0"
                    :is-inline-edit="false"
                />
            </template>
            {% endblock %}
        </sw-entity-listing>
        {% endblock %}
    </div>
    {% endblock %}
</template>
{% endblock %}

{% block sw_review_list_sidebar %}
<template #sidebar>
```

### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-data-grid-column-boolean
        v-model:value="item.active"
        :is-inline-edit="isInlineEdit"
        :disabled="isActiveFieldInherited(item)"
    />

    <sw-inheritance-switch
        :is-inherited="isActiveFieldInherited(item)"
        class="sw-product-variants-overview__active-inherited-icon"
        @inheritance-restore="onActiveInheritanceRestore(item)"
        @inheritance-remove="onActiveInheritanceRemove(item)"
    />
</template>

<template v-else>
```
