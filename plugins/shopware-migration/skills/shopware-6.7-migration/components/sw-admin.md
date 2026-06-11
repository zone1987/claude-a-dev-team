# sw-admin

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `onUserActivity` | |
| `onRemoveToast` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isLoggedIn` | |
| `overrideComponents` | |
| `snackbar` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
<sw-admin-menu-item
    v-for="(entry, index) in buildMenuTree"
    :key="entry.id || index"
    class="sw-admin-menu__sales-channel-item"
    :entry="entry"
    icon-size="16px"
    :class="['sw-admin-menu__sales-channel-item--' + index]"
>
    <template #additional-text>
        {% block sw_sales_channel_menu_navigation_item_additional_text %}
        <button
            v-if="entry.domainLink && entry.active"
            class="sw-sales-channel-menu-domain-link"
            :title="$tc('sw-sales-channel.general.tooltipOpenStorefront')"
            @click.prevent="openStorefrontLink(entry.domainLink)"
```
