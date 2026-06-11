# sw-time-ago

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| date | `null \| null` | — | yes |  |
| dateTimeFormat | `any` | `{}` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `formatRelativeTime` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `dateObject` | |
| `dateFilter` | |
| `fullDatetime` | |
| `lessThanOneMinute` | |
| `lessThanOneHour` | |
| `lessThanOneMinuteFromNow` | |
| `lessThanOneHourFromNow` | |
| `isToday` | |

## Examples

### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
<sw-time-ago :date="item.createdAt" />
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
        {{ $tc('sw-settings-search.generalTab.textLastedBuild') }} <sw-time-ago
            :date="latestIndex.lastDate"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </template>
    <template v-else>
        {{ $tc('sw-settings-search.generalTab.textSearchNotIndexedYet') }}
    </template>
</span>
{% endblock %}
{% endblock %}

{% block sw_settings_search_search_index_rebuild_progress %}
<div
    v-if="progressBarValue"
```

### Example 3
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
        <sw-time-ago
            v-if="extension.installedAt.date"
            :date="extension.installedAt.date"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </span>

    <span v-else-if="extension.storeLicense">
        {{ $tc('sw-extension-store.component.sw-extension-card-base.purchasedLabel') }}
        <sw-time-ago
            v-if="extension.storeLicense.creationDate"
            :date="extension.storeLicense.creationDate"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </span>
```

### Example 4
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
        <sw-time-ago
            :date="item.createdAt"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </mt-link>
</template>
{% endblock %}

{% block sw_import_export_activity_listing_state %}
<template #column-state="{ item }">
    <sw-color-badge
        v-if="item.state === 'failed'"
        variant="error"
        rounded
    />
```

### Example 5
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
        <sw-time-ago
            :date="logEntity.createdAt"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </dd>
</div>
{% endblock %}

{% block sw_import_export_activity_result_modal_info_log_user %}
<div class="sw-import-export-activity-result-modal__list-item sw-import-export-activity-result-modal__log-info-user">
    <dt>{{ $tc('sw-import-export.activity.result.logInfo.labelUser') }}</dt>

    <dd>{{ logEntity.username }}</dd>
</div>
{% endblock %}
```
