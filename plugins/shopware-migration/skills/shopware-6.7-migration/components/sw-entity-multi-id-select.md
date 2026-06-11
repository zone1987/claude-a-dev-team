# sw-entity-multi-id-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| repository | `any` | — | yes |  |
| criteria | `any` | — | no |  |
| context | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-label-property | — | |
| result-description-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateIds` | |

## Examples

### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
<sw-entity-multi-id-select
    v-model:value="configData[null]['core.defaultSalesChannel.salesChannel']"
    :repository="salesChannelRepository"
    :label="$tc('sw-settings.system-config.labelSalesChannelSelect')"
    :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
    @update:value="updateSalesChannel"
/>
{% endblock %}

{% block sw_settings_listing_default_sales_channeld_setting %}
<div class="sw-settings-listing-default-sales-channel__options-container">
    {% block sw_settings_listing_default_sales_channel_setting_active %}
    <mt-switch
        v-model="configData[null]['core.defaultSalesChannel.active']"
        class="sw-settings-listing-default-sales-channel__active-switch"
```

### Example 2
Source: `sw-flow/component/modals/sw-flow-mail-send-modal/sw-flow-mail-send-modal.html.twig`
```twig
<sw-entity-multi-id-select
    v-model:value="documentTypeIds"
    name="sw-field--documentTypeIds"
    :repository="documentTypeRepository"
    class="sw-flow-mail-send-modal__document-types"
    :label="$tc('sw-flow.modals.mail.labelLatestDocuments')"
    :placeholder="$tc('sw-flow.modals.mail.placeholderLatestDocuments')"
/>
{% endblock %}

{% block sw_flow_mail_send_create_new_template %}
<sw-flow-create-mail-template-modal
    v-if="showCreateMailTemplateModal"
    class="sw-flow-mail-send-modal__create-mail-template"
    @process-finish="onCreateMailTemplateSuccess"
```

### Example 3
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-entity-multi-id-select
    v-else-if="isMultiSelectValue"
    ref="product-stream-value-select-entity-multi-id-select"
    v-model:value="multiValue"
    size="medium"
    :repository="entityCustomFieldRepository"
    :criteria="customFieldCriteria"
    :context="context"
    :disabled="disabled"
    @select-collapsed="onSelectCollapsed"
    @search-term-change="setSearchTerm"
>
    <template #result-label-property="{ item, searchTerm, highlightSearchTerm }">
        <slot
            name="result-label-property"
```

### Example 4
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-entity-multi-id-select
    v-else-if="definition.entity === 'property_group_option' && (actualCondition.type === 'equalsAny' || actualCondition.type === 'equalsAll')"
    ref="product-stream-value-select-multi-value"
    v-model:value="multiValue"
    size="medium"
    :repository="repository"
    :criteria="propertyCriteria"
    :context="context"
    :disabled="disabled"
    @select-collapsed="onSelectCollapsed"
    @search-term-change="setSearchTerm"
>

    <template #selection-label-property="{ item }">
        <slot
```
