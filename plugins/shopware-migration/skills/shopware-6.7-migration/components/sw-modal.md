# sw-modal

> Modal dialog overlay with title, subtitle, body content, and footer actions.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | `''` | no |  |
| subtitle | `any` | `null` | no |  |
| size | `any` | `''` | no |  |
| variant | `any` | `'default'` | no | Valid: `default`, `small`, `large`, `full` |
| isLoading | `any` | `false` | no |  |
| selector | `any` | `'body'` | no |  |
| showHeader | `any` | `true` | no |  |
| showFooter | `any` | `true` | no |  |
| closable | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| modal-header | — | |
| modal-title | — | |
| body | — | |
| modal-loader | — | |
| modal-footer | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `destroyedComponent` | |
| `setFocusToModal` | |
| `closeModalOnClickOutside` | |
| `closeModal` | |
| `closeModalOnEscapeKey` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalClasses` | |
| `modalDialogClasses` | |
| `modalBodyClasses` | |
| `hasFooterSlot` | |
| `showHelpSidebar` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-modal
    v-if="showDeleteModal === item.id"
    :title="$tc('global.default.warning')"
    variant="small"
    @modal-close="onCloseDeleteModal"
>
    {% block sw_settings_country_list_delete_modal_confirm_delete_text %}
    <p class="sw-settings-country-list__confirm-delete-text">
        {{ $tc('sw-settings-country.list.textDeleteConfirm', { name: item.name }, 0) }}
    </p>
    {% endblock %}

    {% block sw_settings_country_list_delete_modal_footer %}
    <template #modal-footer>
        {% block sw_settings_country_list_delete_modal_cancel %}
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
<sw-modal
    class="sw-settings-country-currency-dependent-modal"
    :title="$tc('sw-settings-country.detail.currencyDependentValues')"
    @modal-close="closeModal"
>

    {% block sw_settings_country_currency_dependent_modal_content %}
    <sw-data-grid
        class="sw-settings-country-currency-dependent-modal__grid"
        :data-source="currencyDependsValue"
        :is-loading="isLoading"
        :show-selection="false || undefined"
        :plain-appearance="true"
        :columns="countryCurrencyColumns"
    >
```

### Example 3
Source: `sw-settings-country/component/sw-country-state-detail/sw-country-state-detail.html.twig`
```twig
<sw-modal
    class="sw-country-state-detail"
    :title="modalTitle"
    @modal-close="onCancel"
>
    {% block sw_country_state_detail_modal %}
    <sw-container
        columns="1fr 1fr"
        gap="20px"
    >
        <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks, vue/attributes-order -->
        {% block sw_country_state_detail_modal_technical_name %}

        <mt-text-field
            v-model="countryState.name"
```

### Example 4
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-modal
    class="sw-settings-country-new-snippet-modal"
    :title="$tc('sw-settings-country.detail.newSnippetModalTitle')"
    @modal-close="onCloseModal"
>
    <sw-contextual-field
        class="sw-settings-country-new-snippet-modal__search-field"
        required
        :disabled="disabled"
        :error="null"
    >
        <template #sw-field-input="{ identification, disabled, error, size, setFocusClass, removeFocusClass }">
            <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
            <input
                ref="searchInput"
```

### Example 5
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
<sw-modal
    :title="$tc('sw-settings-logging.entryInfo.title')"
    @modal-close="onClose"
>

    {% block sw_settings_logging_entry_info_tabs %}
    <sw-tabs position-identifier="sw-settings-logging-entry-info">

        {% block sw_settings_logging_entry_info_tab_items %}
        <sw-tabs-item
            :active="activeTab === 'raw'"
            @click="activeTab = 'raw'"
        >
            {{ $tc('sw-settings-logging.entryInfo.tabRaw') }}
        </sw-tabs-item>
```
