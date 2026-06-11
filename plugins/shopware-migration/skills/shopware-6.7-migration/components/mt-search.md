# mt-search

> Search input field with debounced search event.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `string` | — | no | |
| placeholder | `string` | — | no | |
| size | `"small" | "default"` | — | no | |
| disabled | `boolean` | — | no | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | value: string | |
| update:modelValue | value: string | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-mapping/sw-import-export-edit-profile-modal-mapping.html.twig`
```twig
    <mt-search
        v-model="searchTerm"
        class="sw-import-export-view-profiles__search"
        size="small"
        :disabled="!mappingsExist"
        @change="onSearch"
    />
    {% endblock %}

    {% block sw_import_export_edit_profile_modal_mapping_toolbar_add_mapping %}
    <mt-button
        v-tooltip="{
            message: $tc('sw-import-export.profile.addMappingTooltipText'),
            disabled: addMappingEnabled,
            showOnDisabledElements: true
```

### Example 2
Source: `sw-import-export/view/sw-import-export-view-profiles/sw-import-export-view-profiles.html.twig`
```twig
    <mt-search
        v-model="searchTerm"
        class="sw-import-export-view-profiles__search"
        size="small"
        @change="onSearch"
    />
    {% endblock %}

    {% block sw_import_export_view_profile_profiles_toolbar_add_new_profile %}
    <mt-button
        v-tooltip="createTooltip"
        class="sw-import-export-view-profiles__create-action"
        ghost
        :disabled="isLoading || isNotSystemLanguage"
        size="small"
```

### Example 3
Source: `sw-settings/page/sw-settings-index/sw-settings-index.html.twig`
```twig
    <mt-search
        v-model="searchQuery"
        class="sw-settings__content-header-search"
        :placeholder="$t('sw-settings.index.search.placeholder')"
        size="small"
    />
</div>
{% endblock %}

{# @deprecated tag:v6.8.0 - will be removed without replacement #}
<mt-banner
    v-if="!feature.isActive('v6.8.0.0') && !hideSettingRenameBanner"
    class="sw-settings__content-rename-banner"
    variant="info"
    closable
```
