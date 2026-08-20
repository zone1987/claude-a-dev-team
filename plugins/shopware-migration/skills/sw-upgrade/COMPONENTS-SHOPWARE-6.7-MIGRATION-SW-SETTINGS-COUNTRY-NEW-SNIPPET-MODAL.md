# sw-settings-country-new-snippet-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selections | `any` | — | no |  |
| currentPosition | `any` | — | yes |  |
| addressFormat | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| getLabelProperty | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selected-option | — | |
| label-property | — | |
| input | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCloseModal` | |
| `addElement` | |
| `debouncedSearch` | |
| `search` | |
| `getSnippetsTree` | |
| `onClickDismiss` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `selection` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
    <sw-settings-country-new-snippet-modal
        v-if="isOpenModal"
        :selections="snippets"
        :current-position="currentPosition"
        :address-format="addressFormat"
        :get-label-property="getLabelProperty"
        @change="change"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```
