# sw-product-settings-mode

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modeSettings | `any` | — | yes |  |
| isLoading | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| settings-change | — | |
| settings-item-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeSetting` | |
| `onChangeSettingItem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `advancedMode` | |
| `settings` | |

## Examples

### Example 1
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
            <sw-product-settings-mode
                v-if="showAdvanceModeSetting"
                :is-loading="isLoading"
                :mode-settings="advancedModeSetting"
                @settings-item-change="onChangeSettingItem"
                @settings-change="onChangeSetting"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}

    <template #sidebar>
        {% block sw_product_detail_sidebar %}
        {% endblock %}
```
