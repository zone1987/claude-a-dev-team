# sw-language-switch

> Language selector for switching the admin editing language.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| changeGlobalLanguage | `any` | `true` | no |  |
| abortChangeFunction | `any` | — | no |  |
| saveChangesFunction | `any` | — | no |  |
| savePermission | `any` | `true` | no |  |
| allowEdit | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `onInput` | |
| `checkAbort` | |
| `emitChange` | |
| `onCloseChangesModal` | |
| `onClickSaveChanges` | |
| `onClickRevertUnsavedChanges` | |
| `changeToNewLanguage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `languageCriteria` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-language-switch @on-change="onChangeLanguage" />
```

### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
    <sw-language-switch
        :save-changes-function="saveOnLanguageChange"
        :abort-change-function="abortOnLanguageChange"
        @on-change="onChangeLanguage"
    />
</template>
{% endblock %}

{% block sw_settings_country_detail_content %}
<template #content>
    <sw-card-view>
        {% block sw_settings_country_detail_content_language_info %}
        <sw-language-info
            :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
        />
```

### Example 3
Source: `sw-settings-country/page/sw-settings-country-create/sw-settings-country-create.html.twig`
```twig
<sw-language-switch disabled />
```

### Example 4
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-language-switch @on-change="onChangeLanguage" />
```

### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
    <sw-language-switch
        :disabled="salutationId == null || undefined"
        @on-change="onChangeLanguage"
    />
</template>
{% endblock %}

{% block sw_settings_salutation_detail_actions %}
<template #smart-bar-actions>
    {% block sw_settings_salutation_detail_actions_cancel %}
    <mt-button
        v-tooltip.bottom="tooltipCancel"
        class="sw-settings-salutation-detail__cancel"
        variant="secondary"
        size="default"
```
