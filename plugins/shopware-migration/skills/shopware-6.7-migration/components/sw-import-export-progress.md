# sw-import-export-progress

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| activityType | `any` | `'import'` | no | Valid: `import`, `export` |
| disableButton | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-start | — | |
| process-start-dryrun | — | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
    <sw-import-export-progress
        activity-type="export"
        :disable-button="disableExporting"
        @process-start="onStartProcess"
    />
    {% endblock %}
</div>
{% endblock %}

```

### Example 2
Source: `sw-import-export/component/sw-import-export-importer/sw-import-export-importer.html.twig`
```twig
    <sw-import-export-progress
        activity-type="import"
        :disable-button="disableImporting"
        @process-start="onStartProcess"
        @process-start-dryrun="onStartDryRunProcess"
    />
    {% endblock %}
</div>
{% endblock %}

```
