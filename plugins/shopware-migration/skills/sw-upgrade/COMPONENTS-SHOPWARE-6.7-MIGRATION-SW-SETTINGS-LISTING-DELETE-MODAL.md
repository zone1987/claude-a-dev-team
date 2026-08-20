# sw-settings-listing-delete-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| description | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| cancel | — | |
| delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `emitCancel` | |
| `emitDelete` | |

## Examples

### Example 1
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedProductSortingOption"
            :title="$tc('sw-settings-listing.index.deleteModal.title')"
            :description="$t('sw-settings-listing.index.deleteModal.description', {
                'sortingOptionName': toBeDeletedProductSortingOption.label
            })"
            @cancel="toBeDeletedProductSortingOption = null"
            @delete="onDeleteProductSorting(toBeDeletedProductSortingOption)"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 2
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedCriteria"
            :title="$tc('sw-settings-listing.base.delete.modalTitle')"
            :description="$tc('sw-settings-listing.base.delete.modalDescription')"
            @cancel="toBeDeletedCriteria = null"
            @delete="onConfirmDeleteCriteria"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
