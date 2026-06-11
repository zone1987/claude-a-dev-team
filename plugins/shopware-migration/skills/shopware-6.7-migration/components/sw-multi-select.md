# sw-multi-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `any` | — | yes |  |
| value | `any` | — | yes |  |
| labelProperty | `any` | `'label'` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| placeholder | `any` | `''` | no |  |
| valueLimit | `any` | `5` | no |  |
| isLoading | `any` | `false` | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| searchFunction | `any` | — | no |  |
| label | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| item-add | — | |
| item-remove | — | |
| search-term-change | — | |
| display-values-expand | — | |
| paginate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `addItem` | |
| `remove` | |
| `removeLastItem` | |
| `expandValueLimit` | |
| `onSearchTermChange` | |
| `resetActiveItem` | |
| `onSelectExpanded` | |
| `onSelectCollapsed` | |
| `getKey` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `visibleValues` | |
| `totalValuesCount` | |
| `invisibleValueCount` | |
| `currentValue` | |
| `visibleResults` | |

## Examples

### Example 1
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
        <sw-multi-select
            v-if="numberRange && (!numberRange.global || numberRange.global === false)"
            class="sw-number-range-detail__select-type"
            :label="$tc('sw-settings-number-range.detail.labelSalesChannel')"
            :disabled="!numberRange.typeId || !acl.can('number_ranges.editor')"
            :value="selectedNumberRangeSalesChannels"
            :options="salesChannels"
            name="sw-field--selectedNumberRangeSalesChannels"
            label-property="translated.name"
            value-property="id"
            @item-add="addSalesChannel"
            @item-remove="removeSalesChannel"
        />
        {% endblock %}
    </sw-container>
```

### Example 2
Source: `sw-settings-basic-information/component/sw-settings-captcha-select-v2/sw-settings-captcha-select-v2.html.twig`
```twig
<sw-multi-select
    v-model:value="activeCaptchaSelect"
    v-bind="attributes"
    :options="availableCaptchas"
/>
{% endblock %}

{% block sw_settings_captcha_select_v2_google_recaptcha_v2 %}
<sw-container
    v-if="currentValue.googleReCaptchaV2.isActive"
    class="sw-settings-captcha-select-v2__google-recaptcha-v2"
>

    {% block sw_settings_captcha_select_v2_google_recaptcha_v2_description %}
    <p class="sw-settings-captcha-select-v2__description sw-settings-captcha-select-v2__google-recaptcha-v2-description">
```

### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
            <sw-multi-select
                class="sw-cms-layout-assignment-modal__shop-page-select"
                :options="shopPages"
                :disabled="props.isInherited"
                :value="props.currentValue"
                :map-inheritance="props"
                @update:value="props.updateCurrentValue"
            />
        </template>
    </sw-inherit-wrapper>
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_product_detail_pages_select %}
```

### Example 4
Source: `sw-promotion-v2/component/sw-promotion-v2-sales-channel-select/sw-promotion-v2-sales-channel-select.html.twig`
```twig
<sw-multi-select
    v-model:value="salesChannelIds"
    v-bind="$attrs"
    :options="salesChannels"
    value-property="id"
    label-property="name"
>

    {% block sw_promotion_v2_sales_channel_selection_label %}
    <template #selection-label-property="{ item }">
        {{ item.name || item.translated.name }}
    </template>
    {% endblock %}

    {% block sw_promotion_v2_sales_channel_selection_result_label %}
```

### Example 5
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
<sw-multi-select
    v-if="documentConfig.salesChannels && (!documentConfig.global || documentConfig.global === false)"
    id="documentSalesChannel"
    v-model:value="documentConfigSalesChannels"
    @update:value="(v) => documentConfigSalesChannels = v"
    name="sw-field--documentConfigSalesChannels"
    v-tooltip="{
        showDelay: 300,
        message: $tc('sw-settings-document.detail.disabledSalesChannelSelect'),
        disabled: !!documentConfig.documentType
    }"
    label-property="name"
    value-property="id"
    :options="documentConfigSalesChannelOptionsCollection"
    :label="$tc('sw-settings-document.detail.labelSalesChannel')"
```
