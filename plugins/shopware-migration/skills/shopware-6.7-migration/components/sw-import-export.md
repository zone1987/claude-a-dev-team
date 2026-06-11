# sw-import-export

> Shopware Administration component.

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-identifiers/sw-import-export-edit-profile-modal-identifiers.html.twig`
```twig
            <sw-import-export-entity-path-select
                v-else
                :value="item.selected"
                :languages="languages"
                :currencies="currencies"
                :entity-type="item.entityName"
                :disabled="profile.systemDefault"
                :custom-field-sets="customFieldSets"
                @update:value="onChangeIdentifier($event, item.entityName)"
            >
                <template #before-item-list>
                    <span></span>
                </template>
            </sw-import-export-entity-path-select>
        </template>
```

### Example 2
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
        <sw-import-export-exporter
            :source-entity="exportModalProfile"
            @export-started="$emit('export-started', $event)"
        />
        {% endblock %}

        <template #modal-footer>
            {% block sw_import_export_exporter_modal_footer %}
            <mt-button
                size="small"
                variant="secondary"
                @click="setExportModalProfile(null)"
            >
                {{ $tc('sw-import-export.exporter.close') }}
            </mt-button>
```

### Example 3
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-activity-log-info-modal
        v-if="showDetailModal"
        :log-entity="selectedLog"
        @log-close="closeSelectedLog"
    />
    {% endblock %}

    {% block sw_import_export_activity_result_modal %}
    <sw-import-export-activity-result-modal
        v-if="showResultModal"
        :log-entity="selectedLog"
        :result="selectedResult"
        @result-close="closeSelectedResult"
    />
    {% endblock %}
```

### Example 4
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-general :profile="profile" />
```

### Example 5
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-field-indicators :profile="profile" />
```
