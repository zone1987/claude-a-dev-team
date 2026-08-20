# sw-import-export-activity-log-info-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| logEntity | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| log-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `calculateFileSize` | |
| `openDownload` | |
| `getStateLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `typeText` | |
| `stateClass` | |
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
