# sw-grid-column

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | `null` | no |  |
| iconLabel | `any` | `null` | no |  |
| align | `any` | `'left'` | no |  |
| flex | `any` | `1` | no |  |
| sortable | `any` | `false` | no |  |
| dataIndex | `any` | `''` | no |  |
| editable | `any` | `false` | no |  |
| truncate | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| inline-edit | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerColumn` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `parentGrid` | |

## Examples

### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid-column
    :label="$tc('sw-product.visibility.columnSalesChannel')"
    flex="0.5fr"
    align="left"
>
    {% block sw_settings_listing_visibility_detail_columns_sales_channel_label %}
    <span
        v-tooltip="{ message: item.name, disabled: item.name.length < 10 }"
        class="sw-product-visibility-detail__name"
    >
        {{ truncateFilter(item.name, 30) }}
    </span>
    {% endblock %}
</sw-grid-column>
```

### Example 2
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid-column
    :label="$tc('sw-product.visibility.columnAll')"
    flex="0.3fr"
    align="left"
>
    <sw-radio-field
        :disabled="disabled"
        :value="item.visibility"
        :name="'visibility' + item.id"
        :options="[{ value: 30 }]"
        @update:value="changeVisibilityValue($event, item)"
    />
</sw-grid-column>
```

### Example 3
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
<sw-grid-column
    flex="minmax(100px, 2fr)"
    :label="$tc('sw-import-export.activity.result.entityName')"
    :class="`sw-import-export-activity-result-modal__column-${item.entityName}-label`"
>
    {{ item.entityName }}
</sw-grid-column>
```

### Example 4
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
<sw-grid-column
    flex="minmax(50px, 1fr)"
    :label="$tc('sw-import-export.activity.result.changes')"
    :class="`sw-import-export-activity-result-modal__column-${item.entityName}-changes`"
>
    {{ item.insert + item.update }}
</sw-grid-column>
```

### Example 5
Source: `sw-settings-document/page/sw-settings-document-list/sw-settings-document-list.html.twig`
```twig
<sw-grid-column
    class="sw-document-list__column-name"
    flex="minmax(100px, 1fr)"
    :label="$tc('sw-settings-document.list.columnName')"
>
    {% block sw_settings_document_list_columns_name_link %}
    <mt-link :to="{ name: 'sw.settings.document.detail', params: { id: item.id } }">
            {% block sw_settings_document_list_columns_name_link_inner %}
        {{ item.name }}
            {% endblock %}
    </mt-link>
    {% endblock %}
</sw-grid-column>
```
