# sw-multi-tag-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| valueLimit | `any` | `5` | no |  |
| placeholder | `any` | `''` | no |  |
| isLoading | `any` | `false` | no |  |
| validMessage | `any` | `''` | no |  |
| invalidMessage | `any` | `''` | no |  |
| validate | `any` | — | no |  |
| disabled | `any` | `false` | no |  |
| autocomplete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| message-add-data | — | |
| message-enter-valid-data | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| add-item-is-valid | — | |
| update:value | — | |
| display-values-expand | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSelectionListKeyDownEnter` | |
| `addItem` | |
| `remove` | |
| `removeLastItem` | |
| `onSearchTermChange` | |
| `getKey` | |
| `setDropDown` | |
| `expandValueLimit` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `errorObject` | |
| `inputIsValid` | |
| `visibleValues` | |
| `totalValuesCount` | |
| `invisibleValueCount` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
<sw-multi-tag-select
    class="sw-product-category-form__search-keyword-field"
    :value="currentValue ? currentValue : []"
    :placeholder="$tc('sw-product.categoryForm.placeholderSearchKeywords')"
    :disabled="isInherited || !allowEdit"
    @update:value="updateCurrentValue"
>
    <template #message-add-data>
        <span>{{ $tc('sw-product.categoryForm.textAddSearchKeyword') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-product.categoryForm.textEnterValidSearchKeyword') }}</span>
    </template>
</sw-multi-tag-select>
```

### Example 2
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
<sw-multi-tag-select
    v-model:value="delivery.trackingCodes"
    class="sw-order-user-card__tracking-code-select"
    :placeholder="$tc('sw-order.detailBase.placeholderTrackingCodeSelect')"
    @update:value="emitChange"
>
    <template #message-add-data>
        <span>{{ $tc('sw-order.detailBase.addTrackingCode') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-order.detailBase.enterValidTrackingCode') }}</span>
    </template>
</sw-multi-tag-select>
```

### Example 3
Source: `sw-order/component/sw-order-create-options/sw-order-create-options.html.twig`
```twig
<sw-multi-tag-select
    class="sw-order-create-options__promotion-code"
    :value="promotionCodes"
    :label="$tc('sw-order.createBase.labelPromotions')"
    :validate="validatePromotions"
    @update:value="changePromotionCodes"
>
    <template #message-add-data>
        <span>{{ $tc('sw-order.initialModal.options.placeholderAddPromotion') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-order.createBase.placeholderAddPromotion') }}</span>
    </template>
</sw-multi-tag-select>
```

### Example 4
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-multi-tag-select
    v-model:value="delivery.trackingCodes"
    class="sw-order-user-card__tracking-code-select"
    :disabled="!acl.can('order.editor') || undefined"
    :placeholder="$tc('sw-order.detailBase.placeholderTrackingCodeSelect')"
    :label="$tc('sw-order.detailBase.labelTrackingCodes')"
    :validate="validateTrackingCode"
    @update:value="saveAndReload"
>
    <template #message-add-data>
        <span>{{ $tc('sw-order.detailBase.addTrackingCode') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-order.detailBase.enterValidTrackingCode') }}</span>
    </template>
```
