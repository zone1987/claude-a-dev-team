# sw-import-export-exporter

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sourceEntity | `any` | `''` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| export-started | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onProfileSelect` | |
| `onStartProcess` | |
| `handleProgress` | |
| `setExportModalProfile` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `profileCriteria` | |
| `disableExporting` | |
| `showProductVariantsInfo` | |

## Examples

### Example 1
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

### Example 2
Source: `sw-import-export/view/sw-import-export-view-export/sw-import-export-view-export.html.twig`
```twig
        <sw-import-export-exporter
            @export-started="reloadContent"
        />
    </mt-card>
    {% endblock %}

    {% block sw_import_export_view_export_activity %}
    <mt-card
        class="sw-import-export-view-export__activity"
        position-identifier="sw-import-export-view-export-activity"
        :title="$tc('sw-import-export.exporter.exportActivityLabel')"
        :subtitle="$tc('sw-import-export.exporter.exportActivityDescription')"
    >
        {# @deprecated tag:v6.8.0 - Block will be removed. #}
        {% block sw_import_export_view_export_activity_title %}
```
