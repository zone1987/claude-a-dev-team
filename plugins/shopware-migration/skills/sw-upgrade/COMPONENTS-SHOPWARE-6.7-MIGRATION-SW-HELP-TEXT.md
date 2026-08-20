# sw-help-text

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | `''` | yes |  |
| width | `any` | `200` | no |  |
| tooltipPosition | `any` | `'top'` | no | Valid: `top`, `bottom`, `left`, `right` |
| showDelay | `any` | `100` | no |  |
| hideDelay | `any` | `100` | no |  |

## Examples

### Example 1
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
        <sw-help-text
            :width="380"
            :text="$t('sw-settings-number-range.detail.helpTextAdvancedField')"
        />
    </div>
    {% endblock %}
</sw-container>

<sw-container
    columns="repeat(auto-fit, minmax(250px, 1fr))"
    gap="0px 30px"
>
    {% block sw_settings_number_range_detail_content_field_current_number %}
    <mt-text-field
        v-if="state"
```

### Example 2
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-help-text
        class="sw-import-export-activity__invalid-records-help-text"
        :text="$t('sw-import-export.activity.invalidHelpText')"
    />
</template>
{% block sw_import_export_activity_listing_invalid_records %}

<template #column-invalidRecords="{ item }">
    <template v-if="item.invalidRecordsLog">
        {{ item.invalidRecordsLog.records }}
    </template>

    <template v-else>
        0
    </template>
```

### Example 3
Source: `sw-first-run-wizard/view/sw-first-run-wizard-mailer-selection/sw-first-run-wizard-mailer-selection.html.twig`
```twig
    <sw-help-text
        class="sw-first-run-wizard-mailer-selection__help-text"
        :text="$tc('sw-first-run-wizard.mailerSelection.localOptionHelptext')"
    />

    <mt-icon
        name="regular-paper-plane"
        class="sw-first-run-wizard-mailer-selection__selection-icon"
    />

    <p>
        <span>{{ $tc('sw-first-run-wizard.mailerSelection.localOption') }}</span>
        <br>
        <span>{{ $tc('sw-first-run-wizard.mailerSelection.localOptionSubline') }}</span>
    </p>
```

### Example 4
Source: `sw-customer/component/sw-customer-base-info/sw-customer-base-info.html.twig`
```twig
<sw-help-text :text="$tc('sw-customer.baseInfo.helpTextBoundSalesChannel')" />
```

### Example 5
Source: `sw-settings-custom-field/page/sw-settings-custom-field-set-list/sw-settings-custom-field-set-list.html.twig`
```twig
        <sw-help-text
            class="sw-settings-custom-field-set-list__help-text-global-set"
            :text="$tc('sw-settings-custom-field.set.list.helpTextGlobalSet')"
        />
    </template>
    <template v-else>
        <router-link
            :title="$tc('sw-settings-custom-field.set.list.contextMenuEdit')"
            class="sw-custom-field-set-list__column-name"
            :to="{ name: 'sw.settings.custom.field.detail', params: { id: item.id } }"
        >
            {{ getInlineSnippet(item.config.label) || item.name }}
        </router-link>
    </template>
</sw-grid-column>
```
