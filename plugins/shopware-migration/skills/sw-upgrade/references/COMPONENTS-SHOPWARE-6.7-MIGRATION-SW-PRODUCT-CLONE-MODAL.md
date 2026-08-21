# sw-product-clone-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| clone-finish | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `duplicate` | |
| `cloneParent` | |
| `verifyVariants` | |
| `getChildrenIds` | |
| `duplicateVariant` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `progressInPercentage` | |
| `repository` | |

## Examples

### Example 1
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
    <sw-product-clone-modal
        v-if="cloning"
        :product="product"
        @clone-finish="onDuplicateFinish"
    />
    {% endblock %}

    {% block sw_product_list_content_variant_modal %}
    <sw-product-variant-modal
        v-if="showVariantModal"
        :product-entity="productEntityVariantModal"
        @modal-close="closeVariantModal"
    />
    {% endblock %}
</template>
```

### Example 2
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
            <sw-product-clone-modal
                v-if="cloning"
                :product="product"
                @clone-finish="onDuplicateFinish"
            />
            {% endblock %}

            {% block sw_product_settings_mode %}
            <sw-product-settings-mode
                v-if="showAdvanceModeSetting"
                :is-loading="isLoading"
                :mode-settings="advancedModeSetting"
                @settings-item-change="onChangeSettingItem"
                @settings-change="onChangeSetting"
            />
```
