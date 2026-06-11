# sw-entity-single-select

> Single-select dropdown for Shopware entities with search and API integration.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| resetOption | `any` | `''` | no |  |
| labelProperty | `null \| null` | `'name'` | no |  |
| labelCallback | `any` | `null` | no |  |
| entity | `any` | — | yes |  |
| resultLimit | `any` | `25` | no |  |
| criteria | `any` | — | no |  |
| context | `any` | — | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| disableAutoClose | `any` | `false` | no |  |
| disabledSelectionTooltip | `any` | — | no |  |
| descriptionPosition | `any` | `'right'` | no | Valid: `bottom`, `right`, `left` |
| allowEntityCreation | `any` | `false` | no |  |
| entityCreationLabel | `any` | — | no |  |
| advancedSelectionComponent | `any` | `''` | no |  |
| advancedSelectionParameters | `any` | — | no |  |
| displayVariants | `any` | `false` | no |  |
| shouldShowActiveState | `any` | `false` | no |  |
| disabled | `any` | — | no |  |
| label | `any` | — | no |  |
| size | `any` | `'default'` | no |  |
| popoverClasses | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| result-description-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| search | — | |
| option-select | — | |
| before-selection-clear | — | |
| search-term-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadSelected` | |
| `createCollection` | |
| `isSelected` | |
| `debouncedSearch` | |
| `search` | |
| `handleSearchPromise` | |
| `paginate` | |
| `loadData` | |
| `checkEntityExists` | |
| `displaySearch` | |
| `displayLabelProperty` | |
| `onSelectExpanded` | |
| `tryGetSearchText` | |
| `onSelectCollapsed` | |
| `closeResultList` | |
| `setValue` | |
| `addItem` | |
| `clearSelection` | |
| `clearInput` | |
| `resetActiveItem` | |
| `onInputSearchTerm` | |
| `getKey` | |
| `isSelectionDisabled` | |
| `getDisabledSelectionTooltip` | |
| `createNewEntity` | |
| `filterSearchGeneratedTags` | |
| `openAdvancedSelectionModal` | |
| `closeAdvancedSelectionModal` | |
| `onAdvancedSelectionSubmit` | |
| `getActiveIconColor` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `inputClasses` | |
| `selectionTextClasses` | |
| `repository` | |
| `results` | |
| `isAdvancedSelectionActive` | |
| `advancedSelectionInitialSearchTerm` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
            <sw-entity-single-select
                v-model:value="customerId"
                class="sw-settings-country-address-handling__customer-select"
                :label="$tc('sw-settings-country.detail.labelCustomer')"
                :placeholder="$tc('sw-settings-country.detail.placeholderSelectCustomer')"
                entity="customer"
                show-clearable-button
                :criteria="customerCriteria"
                :label-callback="customerLabel"
                @update:value="onChangeCustomer"
            />

            <sw-settings-country-preview-template :formatting-address="formattingAddress" />

            <mt-button
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
        <sw-entity-single-select
            v-model:value="country.customerTax.currencyId"
            name="sw-field--country-customerTax-currencyId"
            class="sw-settings-country-general__customer-select-currency sw-settings-country-general__select"
            entity="currency"
            bordered
            show-clearable-button
            :disabled="!acl.can('country.editor') || undefined"
        />
    </template>
</mt-number-field>
{% endblock %}
{% endblock %}

{% block sw_settings_country_general_content_show_tax_free_currency_dependent_values %}
```

### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
        <sw-entity-single-select
            v-model:value="country.companyTax.currencyId"
            name="sw-field--country-companyTax-currencyId"
            class="sw-settings-country-general__company-select-currency sw-settings-country-general__select"
            entity="currency"
            show-clearable-button
            :disabled="!acl.can('country.editor') || undefined"
        />
    </template>
</mt-number-field>
{% endblock %}
{% endblock %}

{% block sw_settings_country_general_content_show_company_tax_free_currency_dependent_values %}
<sw-container
```

### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
<sw-entity-single-select
    v-model:value="currentCustomFieldId"
    class="sw-settings-search-custom-field-select"
    entity="custom_field"
    :criteria="customFieldFilteredCriteria"
    show-clearable-button
    @update:value="(id, customfield) => onSelectCustomField(customfield)"
>

    <template #selection-label-property="{ item }">
        {{ showCustomFieldWithSet(item) }}
    </template>

    <template #result-label-property="{ item }">
        {{ showCustomFieldWithSet(item) }}
```

### Example 5
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
<sw-entity-single-select
    v-if="numberRange.type"
    id="numberRangeTypes"
    v-model:value="numberRange.typeId"
    name="sw-field--numberRange-typeId"
    entity="number_range_type"
    class="sw-number-range-detail__select-type"
    :disabled="disableNumberRangeTypeSelect"
    required
    show-clearable-button
    label-property="typeName"
    :label="$tc('sw-settings-number-range.detail.labelType')"
    :criteria="numberRange.type.global ? numberRangeTypeCriteriaGlobal : numberRangeTypeCriteria"
    :error="numberRangeTypeIdError"
    @update:value="onChangeType"
```
