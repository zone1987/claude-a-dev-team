# sw-context-button

> Trigger button that opens a context menu dropdown.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showMenuOnStartup | `any` | `false` | no |  |
| menuWidth | `any` | `220` | no |  |
| menuHorizontalAlign | `any` | `'right'` | no |  |
| menuVerticalAlign | `any` | `'bottom'` | no |  |
| icon | `any` | `'solid-ellipsis-h-s'` | no |  |
| iconSize | `any` | `'16px'` | no |  |
| disabled | `any` | `false` | no |  |
| autoClose | `any` | `true` | no |  |
| autoCloseOutsideClick | `any` | `false` | no |  |
| additionalContextMenuClasses | `any` | — | no |  |
| zIndex | `any` | `1100` | no |  |
| ariaLabel | `any` | `'sw-context-button.ariaLabel'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| button | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-open-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onClickButton` | |
| `openMenu` | |
| `handleClickEvent` | |
| `closeMenu` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `menuStyles` | |
| `contextClass` | |
| `contextButtonClass` | |
| `contextMenuClass` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
<sw-context-button
    :menu-width="300"
    :auto-close="false"
    :auto-close-outside-click="true"
>
    <template #button>

        {% block sw_settings_country_currency_hamburger_menu_trigger %}
        <mt-button
            class="sw-settings-country-currency-hamburger-menu__button"
            size="x-small"
            square
            variant="secondary"
        >

```

### Example 2
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-context-button class="sw-multi-snippet-drag-and-drop__context-button">
    <sw-context-menu-item
        :disabled="isMaxLines"
        @click="openModal"
    >
        {{ $tc('sw-settings-country.general.actions.newSnippet') }}
    </sw-context-menu-item>

    <sw-context-menu-item
        :disabled="isMaxLines"
        @click="addNewLineAt('above')"
    >
        {{ $tc('sw-settings-country.general.actions.createBefore') }}
    </sw-context-menu-item>

```

### Example 3
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-context-button
    v-if="showContextMenu"
    class="sw-extension-card-base__context-menu"
    :menu-width="180"
>
    {% block sw_extension_card_base_context_menu_actions %}
    <sw-context-menu-item
        v-if="openLinkExists && extension.active"
        :disabled="!openLinkExists"
        :router-link="link"
    >
        {{ $tc('sw-extension-store.component.sw-extension-card-base.contextMenu.openExtension') }}
    </sw-context-menu-item>

    <sw-context-menu-item
```

### Example 4
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
<sw-context-button class="sw-category-layout-card__desc-actions-menu">
    {% block sw_category_detail_layout_desc_actions_designer %}
    <sw-context-menu-item
        class="sw-category-detail-layout__open-in-pagebuilder"
        :disabled="!acl.can('category.editor')"
        @click="openInPagebuilder"
    >
        {{ $t('global.default.edit') }}
    </sw-context-menu-item>
    {% endblock %}

    {% block sw_category_detail_layout_desc_actions_remove %}
    <sw-context-menu-item
        v-if="cmsPage"
        :disabled="!acl.can('category.editor')"
```

### Example 5
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-context-button
    v-tooltip="toolTip"
    class="sw-tree-item__context_button"
    :disabled="disableContextMenu || undefined"
>

    {% block sw_landing_page_tree_items_actions_edit %}
    <sw-context-menu-item @click="onChangeRoute(item)">
        {{ $tc('global.default.edit') }}
    </sw-context-menu-item>
    {% endblock %}

    {% block sw_landing_page_tree_items_actions_duplicate %}
    <sw-context-menu-item
        class="sw-context-menu__duplicate-action"
```
