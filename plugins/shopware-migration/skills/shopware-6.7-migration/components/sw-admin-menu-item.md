# sw-admin-menu-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entry | `any` | — | yes |  |
| parentEntries | `any` | — | no |  |
| displayIcon | `any` | `true` | no |  |
| iconSize | `any` | `'20px'` | no |  |
| collapsibleText | `any` | `true` | no |  |
| sidebarExpanded | `any` | `true` | no |  |
| borderColor | `any` | `'#333'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additional-text | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| menu-item-click | — | |
| menu-item-enter | — | |
| sub-menu-item-enter | — | |

## Methods

| Method | Description |
|--------|-------------|
| `hasAccessToRoute` | |
| `getIconName` | |
| `getItemName` | |
| `subIsActive` | |
| `getElementClasses` | |
| `onSubMenuItemEnter` | |
| `isFirstPluginInMenuEntries` | |
| `getCustomKey` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `getLinkToProp` | |
| `getEntryLabel` | |
| `showMenuItem` | |
| `entryPath` | |
| `children` | |

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

### Example 2
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
            <sw-admin-menu-item
                v-if="moreSalesChannelAvailable"
                :entry="moreItemsEntry"
                class="sw-admin-menu__sales-channel-more-items"
                icon-size="16px"
            />
            {% endblock %}
        </ul>
        {% endblock %}

        {% block sw_sales_channel_menu_context_button_collapsed %}
        <sw-context-button
            class="sw-sales-channel-menu__collapsed-context-menu"
            icon="regular-ellipsis-v"
            aria-label="sw-sales-channel.general.manageSalesChannels"
```
