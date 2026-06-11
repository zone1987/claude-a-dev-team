# sw-import-export-importer

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sourceEntity | `any` | `''` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| import-started | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onProfileSelect` | |
| `onStartProcess` | |
| `onStartDryRunProcess` | |
| `handleProgress` | |
| `setImportModalProfile` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `profileCriteria` | |
| `logRepository` | |
| `disableImporting` | |
| `showProductVariantsInfo` | |
| `logCriteria` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-importer/sw-import-export-importer.html.twig`
```twig
        <sw-import-export-importer
            :source-entity="importModalProfile"
            @import-started="$emit('import-started', $event)"
        />
        {% endblock %}

        <template #modal-footer>
            {% block sw_import_export_importer_modal_footer %}
            <mt-button
                size="small"
                variant="secondary"
                @click="setImportModalProfile(null)"
            >
                {{ $tc('sw-import-export.importer.close') }}
            </mt-button>
```

### Example 2
Source: `sw-import-export/view/sw-import-export-view-import/sw-import-export-view-import.html.twig`
```twig
        <sw-import-export-importer
            @import-started="reloadContent"
        />
    </mt-card>
    {% endblock %}

    {% block sw_import_export_view_import_activity %}
    <mt-card
        class="sw-import-export-view-import__activity"
        position-identifier="sw-import-export-view-import-log-activity"
        :title="$tc('sw-import-export.importer.importActivityLabel')"
        :subtitle="$tc('sw-import-export.exporter.exportActivityDescription')"
    >
        {# @deprecated tag:v6.8.0 - Block will be removed. #}
        {% block sw_import_export_view_import_activity_title %}
```
