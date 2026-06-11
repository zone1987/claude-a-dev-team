# sw-import-export-activity-result-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| logEntity | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| result-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `calculateFileSize` | |
| `openDownload` | |
| `getStateLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mainEntity` | |
| `mainEntityResult` | |
| `result` | |
| `logTypeText` | |
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-activity-result-modal
        v-if="showResultModal"
        :log-entity="selectedLog"
        :result="selectedResult"
        @result-close="closeSelectedResult"
    />
    {% endblock %}

    {% block sw_import_export_activity_modal %}
    <sw-import-export-edit-profile-modal
        v-if="selectedProfile"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @profile-close="closeSelectedProfile"
    />
```
