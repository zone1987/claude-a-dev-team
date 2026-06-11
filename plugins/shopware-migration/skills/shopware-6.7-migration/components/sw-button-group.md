# sw-button-group

> Groups multiple buttons together with consistent spacing.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | `false` | no |  |
| splitButton | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `buttonGroupClasses` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-mapping/sw-import-export-edit-profile-modal-mapping.html.twig`
```twig
<sw-button-group class="sw-import-export-edit-profile-modal-mapping__position-buttons">
    {% block sw_import_export_edit_profile_modal_mapping_grid_position_column_button_group_up %}
    <mt-button
        size="x-small"
        square
        :disabled="isFirstMapping(item) || !!searchTerm"
        variant="secondary"
        @click="updateSorting(itemIndex, 'up')"
    >
        {% block sw_import_export_edit_profile_modal_mapping_grid_position_column_button_group_up_icon %}
        <mt-icon
            name="regular-chevron-up-xs"
            size="10px"
        />
        {% endblock %}
```

### Example 2
Source: `sw-settings-rule/page/sw-settings-rule-detail/sw-settings-rule-detail.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('rule.editor'),
        showOnDisabledElements: true
    }"
    class="sw-settings-rule-detail__save-button-group"
    :split-button="true"
>
    {% block sw_settings_rule_detail_actions_save %}
    <sw-button-process
        v-model:process-success="isSaveSuccessful"
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-rule-detail__save-action"
        :is-loading="isLoading"
```

### Example 3
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product.creator'),
        showOnDisabledElements: true
    }"
    class="sw-product-list__add-button-group"
    split-button
>
    {% block sw_product_list_smart_bar_actions_add %}
    <mt-button
        v-tooltip="{
            message: $tc('sw-privileges.tooltip.warning'),
            disabled: acl.can('product.creator'),
            showOnDisabledElements: true
```

### Example 4
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product.editor'),
        showOnDisabledElements: true
    }"
    class="sw-product-detail__save-button-group"
    :split-button="true"
>
    {% block sw_product_detail_actions_save %}
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-product-detail__save-action"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
```

### Example 5
Source: `sw-product-stream/page/sw-product-stream-detail/sw-product-stream-detail.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product_stream.editor'),
        showOnDisabledElements: true
    }"
    class="sw-product-stream-detail__save-button-group"
    :split-button="true"
>
    {% block sw_product_stream_detail_actions_save %}
    <sw-button-process
        v-model:process-success="isSaveSuccessful"
        v-tooltip.bottom="tooltipSave"
        class="sw-product-stream-detail__save-action"
        :is-loading="isLoading"
```
