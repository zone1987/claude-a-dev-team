# sw-promotion-v2-generate-codes-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| generate-finish | — | |
| close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatePattern` | |
| `updatePreview` | |
| `onGenerate` | |
| `onClose` | |

## Examples

### Example 1
Source: `sw-promotion-v2/component/promotion-codes/sw-promotion-v2-individual-codes-behavior/sw-promotion-v2-individual-codes-behavior.html.twig`
```twig
<sw-promotion-v2-generate-codes-modal
    v-if="generateCodesModal"
    :promotion="promotion"
    @generate-finish="onGenerateFinish"
    @close="onCloseGenerateCodesModal"
/>
{% endblock %}

{% block sw_promotion_v2_individual_codes_behavior_add_codes_modal %}
<sw-modal
    v-if="addCodesModal"
    class="sw-promotion-v2-individual-codes-behavior__add-codes-modal"
    variant="small"
    :title="$tc('sw-promotion-v2.detail.base.codes.individual.addCodesModal.title')"
    @modal-close="onCloseAddCodesModal"
```
