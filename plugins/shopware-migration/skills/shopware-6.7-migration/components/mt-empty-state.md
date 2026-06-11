# mt-empty-state

> Empty state display with icon, title, and description for zero-data scenarios.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| headline | `string` | — | yes | |
| description | `string` | — | yes | |
| icon | `string` | — | yes | |
| linkHref | `string` | — | no | |
| linkText | `string` | — | no | |
| linkType | `"external" | "internal"` | — | no | |
| buttonText | `string` | — | no | |
| centered | `boolean` | — | no | |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| button | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| button-click | — | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
        <mt-empty-state
            v-if="showEmptyState"
            :icon="$route.meta.$module.icon"
            :headline="$tc('sw-country-state-detail.emptyTitle')"
            :description="$tc('sw-country-state-detail.emptySubline')"
        />
        {% endblock %}
    </template>
    {% block sw_settings_country_state_detail %}
    <sw-country-state-detail
        v-if="currentCountryState"
        :country-state="currentCountryState"
        @attribute-edit-save="onSaveCountryState"
        @attribute-edit-cancel="onCancelCountryState"
    />
```

### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <mt-empty-state
            v-if="!isLoading && selectedIds.length == 0"
            :icon="$route.meta.$module.icon"
            :headline="$tc('sw-bulk-edit.product.messageEmptyTitle')"
            :description="$tc('sw-bulk-edit.product.messageEmptySubline')"
        />

        {% block sw_bulk_edit_product_save_modal %}
        <router-view
            v-slot="{ Component }"
        >
            <component
                :is="Component"
                :item-total="selectedIds.length"
                :is-loading="isLoading"
```

### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <mt-empty-state
            v-if="selectedIds.length <= 0 && !isLoading"
            :icon="$route.meta.$module.icon"
            :headline="$tc('sw-bulk-edit.order.messageEmptyTitle')"
            :description="$tc('sw-bulk-edit.order.messageEmptySubline')"
        />
        {% endblock %}

        {% block sw_bulk_edit_order_save_modal %}
        <router-view
            v-slot="{ Component }"
        >
            <component
                :is="Component"
                :item-total="selectedIds.length"
```

### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
        <mt-empty-state
            v-if="selectedIds.length <= 0 && !isLoading"
            icon="solid-users"
            :headline="$tc('sw-bulk-edit.customer.messageEmptyTitle')"
            :description="$tc('sw-bulk-edit.customer.messageEmptySubline')"
        />
        {% endblock %}

        {% block sw_bulk_edit_customer_save_modal %}
        <router-view
            v-slot="{ Component }"
        >
            <component
                :is="Component"
                :item-total="selectedIds.length"
```

### Example 5
Source: `sw-settings-units/page/sw-settings-units-list/sw-settings-units.html.twig`
```twig
<mt-empty-state
    v-if="!isLoading && isEmpty"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-settings-units.empty-state.title')"
    :description="$tc('sw-settings-units.empty-state.subline')"
/>

<template #grid>
    <sw-data-grid
        v-show="isLoading || !isEmpty"
        ref="swDataGrid"
        class="sw-settings-units-grid"
        :is-loading="isLoading"
        :data-source="unitList"
        :columns="unitColumns()"
```
