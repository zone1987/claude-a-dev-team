# sw-product-add-properties-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| newProperties | `any` | — | yes |  |
| propertiesAvailable | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| toolbar | — | |
| toolbar-search-field | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-cancel | — | |
| modal-save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |
| `onOpenProperties` | |
| `onSelectOption` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `showSaveButton` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-properties/sw-product-properties.html.twig`
```twig
        <sw-product-add-properties-modal
            v-if="showAddPropertiesModal"
            :new-properties="newProperties"
            :properties-available="propertiesAvailable"
            @modal-cancel="onCancelAddPropertiesModal"
            @modal-save="onSaveAddPropertiesModal($event, updateCurrentValue)"
        />
        {% endblock %}
    </template>
</sw-inherit-wrapper>
{% endblock %}

```

### Example 2
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
    <sw-product-add-properties-modal
        v-if="showAddPropertiesModal"
        :new-properties="newProperties"
        @modal-cancel="onCancelAddPropertiesModal"
        @modal-save="onSaveAddPropertiesModal"
    />
    {% endblock %}
</div>
{% endblock %}

```
