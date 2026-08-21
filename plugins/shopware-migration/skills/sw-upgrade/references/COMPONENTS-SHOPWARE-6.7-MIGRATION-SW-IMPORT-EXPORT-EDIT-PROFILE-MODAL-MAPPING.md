# sw-import-export-edit-profile-modal-mapping

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | `null` | no |  |
| systemRequiredFields | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-mapping | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `toggleAddMappingActionState` | |
| `onDeleteMapping` | |
| `loadMappings` | |
| `onAddMapping` | |
| `onSearch` | |
| `debouncedSearch` | |
| `isDefaultValueCheckboxDisabled` | |
| `isDefaultValueTextFieldDisabled` | |
| `isRequiredBySystem` | |
| `updateSorting` | |
| `swapItems` | |
| `isFirstMapping` | |
| `isLastMapping` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `languageRepository` | |
| `currencyRepository` | |
| `customFieldSetRepository` | |
| `languageCriteria` | |
| `currencyCriteria` | |
| `customFieldSetCriteria` | |
| `mappingColumns` | |
| `mappingsExist` | |
| `sortedMappings` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-mapping-page/sw-import-export-new-profile-wizard-mapping-page.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        class="sw-import-export-new-profile-wizard-mapping-page__mapping"
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
    {% endblock %}
</template>

<template v-if="active === 'advanced' && profile.type !== 'export' && profile.config.updateEntities !== false">
    {% block sw_import_export_edit_profile_modal_tabs_advanced %}
    {% block sw_import_export_edit_profile_modal_tabs_advanced_text %}
    <p class="sw-import-export-edit-profile-modal__text">
        {{ $tc('sw-import-export.profile.advancedDescription') }}
    </p>
```
