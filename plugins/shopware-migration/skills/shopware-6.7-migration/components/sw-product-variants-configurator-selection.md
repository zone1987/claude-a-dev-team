# sw-product-variants-configurator-selection

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| toolbar | — | |
| toolbar-search-field | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| option-select | — | |

## Methods

| Method | Description |
|--------|-------------|
| `addOptionCount` | |
| `selectOptions` | |
| `onOptionSelect` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `configuratorSettingsRepository` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
    <sw-product-variants-configurator-selection
        v-show="activeTab == 'options'"
        :product="product"
        :options="product.configuratorSettings"
        :overlay="false"
        :collapsible="false"
        :is-add-only="isAddOnly"
        @variations-finish-generate="$emit('variations-finish-generate')"
        @option-select="calcVariantsNumber()"
    />
    {% endblock %}

    {% block sw_product_modal_variant_generation_main_configurator_prices %}
    <sw-product-variants-configurator-prices
        v-if="activeTab == 'prices'"
```
