# sw-avatar

> Avatar component displaying user initials, images, or placeholder icons.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| color | `any` | `''` | no |  |
| size | `any` | `null` | no |  |
| firstName | `any` | `''` | no |  |
| lastName | `any` | `''` | no |  |
| imageUrl | `any` | `null` | no |  |
| placeholder | `any` | `false` | no |  |
| sourceContext | `any` | `null` | no |  |
| variant | `any` | `'circle'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `generateAvatarInitialsSize` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `avatarSize` | |
| `avatarInitials` | |
| `avatarInitialsSize` | |
| `avatarImage` | |
| `avatarColor` | |
| `hasAvatarImage` | |
| `showPlaceholder` | |
| `showInitials` | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-account/sw-extension-my-extensions-account.html.twig`
```twig
        <sw-avatar
            size="36px"
            color="#E3F3FF"
            placeholder
        />

        <span class="sw-extension-my-extensions-account__wrapper-content-login-status-id">{{ userInfo.email }}</span>

        <mt-button
            class="sw-extension-my-extensions-account__logout-button"
            variant="primary"
            size="small"
            @click="logout"
        >
            {{ $tc('sw-extension.my-extensions.account.logout') }}
```

### Example 2
Source: `sw-customer/page/sw-customer-list/sw-customer-list.html.twig`
```twig
    <sw-avatar
        :size="compact ? '32px' : '48px'"
        :source-context="item"
        :first-name="item.firstName"
        :last-name="item.lastName"
    />
</template>
{% endblock %}

{% block sw_customer_list_grid_columns_name %}
<template #column-firstName="{ item, compact, isInlineEdit }">

    {% block sw_customer_list_grid_inline_edit_name %}
    <template v-if="isInlineEdit">
        {% block sw_customer_list_grid_inline_edit_first_name %}
```

### Example 3
Source: `sw-customer/component/sw-customer-card/sw-customer-card.html.twig`
```twig
<sw-avatar
    size="80px"
    :source-context="customer"
    :first-name="customer.firstName"
    :last-name="customer.lastName"
/>
{% endblock %}

{% block sw_customer_card_metadata %}
<div class="sw-customer-card__metadata">
    {% block sw_customer_card_metadata_customer_name %}
    {% block sw_custsomer_card_metadata_customer_name_label %}
    <template v-if="!editMode">
        <div
            v-if="customer"
```

### Example 4
Source: `sw-users-permissions/components/sw-users-permissions-user-listing/sw-users-permissions-user-listing.html.twig`
```twig
    <sw-avatar
        v-if="!isSso"
        :size="compact ? '32px' : '48px'"
        :first-name="item.firstName"
        :last-name="item.lastName"
        variant="square"
        :source-context="item"
    />
</template>
{% endblock %}

{% block sw_settings_user_list_column_username %}
<template #column-username="{ item }">
    {% block sw_settings_user_list_column_username_content %}
    <router-link
```

### Example 5
Source: `sw-order/component/sw-order-create-details-header/sw-order-create-details-header.html.twig`
```twig
<sw-avatar
    v-if="customer"
    size="80px"
    :color="$route.meta.$module.color"
    :first-name="customer.firstName"
    :last-name="customer.lastName"
/>
<sw-avatar
    v-else
    size="80px"
    color="#f9fafb"
/>
{% endblock %}

{% block sw_order_create_details_header_profile_searching %}
```
