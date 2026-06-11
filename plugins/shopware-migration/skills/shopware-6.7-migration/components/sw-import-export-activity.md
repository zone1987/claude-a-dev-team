# sw-import-export-activity

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | `'import'` | no | Valid: `import`, `export` |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `addActivity` | |
| `fetchActivities` | |
| `updateActivitiesInProgress` | |
| `updateActivitiesFromLogs` | |
| `onOpenProfile` | |
| `onAbortProcess` | |
| `closeSelectedProfile` | |
| `onShowLog` | |
| `onShowResult` | |
| `closeSelectedLog` | |
| `closeSelectedResult` | |
| `openProcessFileDownload` | |
| `saveSelectedProfile` | |
| `calculateFileSize` | |
| `getStateLabel` | |
| `getStateClass` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `logRepository` | |
| `profileRepository` | |
| `activityCriteria` | |
| `exportActivityColumns` | |
| `hasActivitiesInProgress` | |
| `downloadFileText` | |
| `showGrid` | |
| `showEmptyState` | |
| `showSpinner` | |
| `emptyStateSubLine` | |
| `emptyStateTitle` | |
| `dateFilter` | |

## Examples

### Example 1
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

### Example 2
Source: `sw-import-export/view/sw-import-export-view-import/sw-import-export-view-import.html.twig`
```twig
            <sw-import-export-activity
                ref="activityGrid"
                type="import"
            />
        </template>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```

### Example 3
Source: `sw-import-export/view/sw-import-export-view-export/sw-import-export-view-export.html.twig`
```twig
            <sw-import-export-activity
                ref="activityGrid"
                type="export"
            />
        </template>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```
