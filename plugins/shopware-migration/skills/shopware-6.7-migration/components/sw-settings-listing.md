# sw-settings-listing

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `createdComponent` | |
| `fetchProductSortingOptions` | |
| `fetchSearchResultSortingOptions` | |
| `fetchCustomFields` | |
| `onSave` | |
| `saveProductSortingOptions` | |
| `saveSearchResultSortingOptions` | |
| `onDeleteProductSorting` | |
| `checkForPagination` | |
| `onPageChange` | |
| `onEditProductSortingOption` | |
| `formatProductSortingOptionField` | |
| `getCustomFieldLabelByCriteriaName` | |
| `getCustomFieldByName` | |
| `onAddNewProductSortingOption` | |
| `onSearchProductSortingOptions` | |
| `onSaveProductSortingOptionInlineEdit` | |
| `isItemACustomField` | |
| `getCustomFieldById` | |
| `stripCustomFieldPath` | |
| `isProductSortingEditable` | |
| `onChangeLanguage` | |
| `setDefaultSortingActive` | |
| `isItemDefaultSorting` | |
| `onLoadingChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productSortingOptionRepository` | |
| `customFieldRepository` | |
| `salesChannelRepository` | |
| `systemConfigRepository` | |
| `productSortingsOptionsCriteria` | |
| `searchResultSortingOptionCriteria` | |
| `productSortingOptionsSearchCriteria` | |
| `sortingOptionsGridTotal` | |
| `customFieldCriteria` | |
| `productSortingOptionColumns` | |
| `assetFilter` | |
| `salesChannelDefaultSortingError` | |

## Examples

### Example 1
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
    <sw-settings-listing-default-sales-channel
        ref="defaultSalesChannelCard"
        :is-loading="isLoading"
    />
</mt-card>
{% endblock %}

{% block sw_settings_listing_content_card_view_system_config %}
<sw-system-config
    ref="systemConfig"
    sales-channel-switchable
    domain="core.listing"
    @loading-changed="onLoadingChanged"
>

```

### Example 2
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

### Example 3
Source: `sw-settings-listing/page/sw-settings-listing-option-create/sw-settings-listing-option-create.html.twig`
```twig
<sw-settings-listing-option-criteria-grid
    v-if="productSortingEntity"
    :product-sorting-entity="productSortingEntity"
    @criteria-delete="onDeleteCriteria"
    @criteria-add="onAddCriteria"
/>
{% endblock %}

{% block sw_settings_listing_option_base_language_switch %}
<!-- eslint-disable vue/valid-v-slot -->
<template #language-switch>
    <sw-language-switch
        :disabled="isNewProductSorting"
        @on-change="onChangeLanguage"
    />
```

### Example 4
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
    <sw-settings-listing-option-general-info
        v-if="productSortingEntity"
        :sorting-option="productSortingEntity"
        :is-default-sorting="isDefaultSorting"
        :label-error="sortingOptionLabelError"
        :technical-name-error="sortingOptionTechnicalNameError"
    />
    {% endblock %}

    {% block sw_settings_listing_option_base_smart_bar_actions_grid %}
    <sw-settings-listing-option-criteria-grid
        v-if="productSortingEntity"
        :product-sorting-entity="productSortingEntity"
        @criteria-delete="onDeleteCriteria"
        @criteria-add="onAddCriteria"
```

### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
            <sw-settings-listing-visibility-detail
                ref="visibilityConfig"
                :config="visibilityConfig"
            />

            <template #modal-footer>
                <mt-button
                    variant="primary"
                    size="small"
                    @click="closeAdvancedVisibility"
                >
                    {{ $tc('global.default.apply') }}
                </mt-button>
            </template>
        </sw-modal>
```
