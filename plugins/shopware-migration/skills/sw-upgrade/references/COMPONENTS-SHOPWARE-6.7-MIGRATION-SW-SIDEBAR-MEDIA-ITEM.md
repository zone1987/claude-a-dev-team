# sw-sidebar-media-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialFolderId | `any` | `null` | no |  |
| isParentLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| context-menu-items | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |
| `initializeContent` | |
| `getSubFolders` | |
| `handleFolderGridItemDelete` | |
| `handleMediaGridItemDelete` | |
| `onLoadMore` | |
| `extendList` | |
| `getList` | |
| `getListingCriteria` | |
| `openContent` | |
| `onNavigateToFolder` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `showMore` | |
| `itemsLoaded` | |

## Examples

### Example 1
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
<sw-sidebar-media-item ref="mediaSidebarItem">
    <template
        #context-menu-items="media"
    >
        <sw-context-menu-item @click="setMediaFromSidebar(media.mediaItem)">
            {{ $tc('sw-settings-shipping.sidebar.labelUseAsLogo') }}
        </sw-context-menu-item>
    </template>
</sw-sidebar-media-item>
```

### Example 2
Source: `sw-settings-payment/page/sw-settings-payment-detail/sw-settings-payment-detail.html.twig`
```twig
<sw-sidebar-media-item ref="mediaSidebarItem">
    <template
        #context-menu-items="media"
    >
        <sw-context-menu-item @click="setMediaFromSidebar(media.mediaItem)">
            {{ $tc('sw-settings-payment.detail.sidebar.labelUseAsLogo') }}
        </sw-context-menu-item>
    </template>
</sw-sidebar-media-item>
```

### Example 3
Source: `sw-mail-template/page/sw-mail-template-detail/sw-mail-template-detail.html.twig`
```twig
<sw-sidebar-media-item ref="mediaSidebarItem">
    <template
        #context-menu-items="media"
    >
        {% block sw_mail_template_detail_sidebar_add_attachment %}
        <sw-context-menu-item
            :disabled="!acl.can('mail_templates.editor') || undefined"
            @click="onAddItemToAttachment(media.mediaItem)"
        >
            {{ $tc('sw-mail-template.detail.sidebar.labelContextMenuAddToMailTemplate') }}
        </sw-context-menu-item>
        {% endblock %}
    </template>
</sw-sidebar-media-item>
```
