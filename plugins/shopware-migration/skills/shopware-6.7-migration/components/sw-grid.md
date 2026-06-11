# sw-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | `null` | no |  |
| selectable | `any` | `true` | no |  |
| variant | `any` | `'normal'` | no |  |
| header | `any` | `true` | no |  |
| sortBy | `any` | `null` | no |  |
| sortDirection | `any` | `'ASC'` | no |  |
| isFullpage | `any` | `false` | no |  |
| table | `any` | `false` | no |  |
| allowInlineEdit | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |
| header | — | |
| body | — | |
| items | — | |
| columns | item: item | |
| empty | — | |
| pagination | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inline-edit-finish | — | |
| inline-edit-start | — | |
| sw-grid-disable-inline-editing | — | |
| inline-edit-cancel | — | |
| sw-grid-select-all | — | |
| sw-grid-select-item | — | |
| sort-column | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatedComponent` | |
| `registerGridDisableInlineEditListener` | |
| `unregisterGridDisableInlineEditListener` | |
| `onInlineEditFinish` | |
| `onInlineEditStart` | |
| `registerInlineEditingEvents` | |
| `inlineEditingStart` | |
| `disableActiveInlineEditing` | |
| `selectAll` | |
| `getSelection` | |
| `selectItem` | |
| `isSelected` | |
| `checkSelection` | |
| `getScrollBarWidth` | |
| `onGridCellClick` | |
| `setScrollbarOffset` | |
| `setColumns` | |
| `getKey` | |
| `startInlineEditing` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sort` | |
| `sortDir` | |
| `sizeClass` | |
| `hasPaginationSlot` | |
| `gridClasses` | |
| `gridContentClasses` | |
| `columnFlex` | |

## Examples

### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid
    class="sw-settings-listing-visibility-detail"
    table
    :items="items"
    :selectable="false"
>
    {% block sw_settings_listing_visibility_detail_columns %}
    <template #columns="{ item }">
        {% block sw_settings_listing_visibility_detail_columns_sales_channel %}
        <sw-grid-column
            :label="$tc('sw-product.visibility.columnSalesChannel')"
            flex="0.5fr"
            align="left"
        >
            {% block sw_settings_listing_visibility_detail_columns_sales_channel_label %}
```

### Example 2
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid-column
    :label="$tc('sw-product.visibility.columnSearchOnly')"
    flex="0.7fr"
    align="left"
>
    <sw-radio-field
        :disabled="disabled"
        :value="item.visibility"
        :name="'visibility' + item.id"
        :options="[{ value: 20 }]"
        @update:value="changeVisibilityValue($event, item)"
    />
</sw-grid-column>
{% endblock %}

```

### Example 3
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
<sw-grid
    table
    :items="result"
    :selectable="false"
>
    {% block sw_import_export_activity_result_modal_activity_table_columns %}
    <template #columns="{ item }">
        {% block sw_import_export_activity_result_modal_activity_table_columns_label %}
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
            :label="$tc('sw-import-export.activity.result.skipped')"
            :class="`sw-import-export-activity-result-modal__column-${item.entityName}-skipped`"
        >
            {{ item.insertSkip + item.updateSkip }}
        </sw-grid-column>
        {% endblock %}
    </template>
    {% endblock %}
</sw-grid>
```

### Example 5
Source: `sw-settings-document/page/sw-settings-document-list/sw-settings-document-list.html.twig`
```twig
<sw-grid
    class="sw-settings-document-list-grid"
    :items="items"
    :selectable="false"
    table
>
    <template #columns="{ item }">
        {% block sw_product_list_grid_columns %}

        {% block sw_settings_document_list_columns_name %}
        <sw-grid-column
            class="sw-document-list__column-name"
            flex="minmax(100px, 1fr)"
            :label="$tc('sw-settings-document.list.columnName')"
        >
```
