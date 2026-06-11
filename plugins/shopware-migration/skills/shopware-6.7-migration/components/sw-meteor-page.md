# sw-meteor-page

> A full-page layout component for the Shopware Administration. Provides a structured page with a search bar, notification center, smart bar (icon, title, actions, tabs), and main content area. Used as the top-level layout for extension and settings pages.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| fullWidth | `Boolean` | `false` | no | Enables full-width content layout (wraps content in a scrollable container) |
| hideIcon | `Boolean` | `false` | no | Hides the module icon in the smart bar |
| fromLink | `RouteLocationNamedRaw \| null` | `null` | no | Explicit parent route for the back navigation link |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | Main content area of the page |
| search-bar | — | Custom search bar, replaces the default `sw-search-bar` |
| smart-bar-back | — | Custom back navigation, replaces the default `sw-meteor-navigation` |
| smart-bar-icon | — | Custom module icon in the smart bar |
| smart-bar-header | — | Custom page title/header text |
| smart-bar-header-meta | — | Meta information displayed below the header |
| smart-bar-description | — | Description text below the module info |
| smart-bar-actions | — | Action buttons in the smart bar (e.g. Save, Cancel) |
| smart-bar-context-buttons | — | Context/dropdown buttons in the smart bar |
| page-tabs | — | Tab items for page-level navigation |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-item-active | `tabItem: String` | Emitted when a new tab becomes active |

## Methods

| Method | Parameters | Return | Description |
|--------|-----------|--------|-------------|
| mountedComponent | — | `void` | Lifecycle method, calls `initPage` on mount |
| emitNewTab | `(tabItem: String)` | `void` | Emits the `new-item-active` event when a tab changes |
| initPage | — | `void` | Reads module info and parent route from `$route.meta` |

## Data

| Name | Type | Default | Description |
|------|------|---------|-------------|
| module | `ModuleManifest \| null` | `null` | Module manifest data (icon, title, color) from route meta |
| parentRoute | `String \| null` | `null` | Parent route path from route meta |

## Computed Properties

| Name | Type | Description |
|------|------|-------------|
| pageClasses | `Object` | Dynamic CSS classes (full-width modifier) |
| hasIcon | `Boolean` | Whether the module has an icon string |
| hasIconOrIconSlot | `Boolean` | Whether an icon exists or the smart-bar-icon slot is provided |
| hasTabs | `Boolean` | Whether the page-tabs slot is provided |
| pageColor | `String` | Module color from manifest, defaults to `#d8dde6` |

## Examples

### Example 1: Extension Config Page
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```html
<sw-meteor-page
    class="sw-extension-config"
    :from-link="fromLink"
>
    <template #smart-bar-icon>
        <sw-extension-icon
            class="sw-extension-config__extension-icon"
            :src="image"
            :alt="extensionLabel"
        />
    </template>

    <template #smart-bar-header>
        {{ extensionLabel }}
    </template>

    <sw-extension-config-renderer
        :extension="extension"
        @save="onSave"
    />
</sw-meteor-page>
```

### Example 2: My Extensions Index Page
Source: `sw-extension/page/sw-extension-my-extensions-index/sw-extension-my-extensions-index.html.twig`
```html
<sw-meteor-page>
    <template #smart-bar-header>
        {{ $tc('sw-extension.my-extensions.title') }}
    </template>

    <template #smart-bar-actions>
        <sw-button variant="primary" @click="onUploadExtension">
            {{ $tc('sw-extension.my-extensions.upload') }}
        </sw-button>
    </template>

    <template #page-tabs>
        <sw-tabs-item :route="{ name: 'sw.extension.my-extensions.listing' }">
            {{ $tc('sw-extension.my-extensions.listing.title') }}
        </sw-tabs-item>
        <sw-tabs-item :route="{ name: 'sw.extension.my-extensions.account' }">
            {{ $tc('sw-extension.my-extensions.account.title') }}
        </sw-tabs-item>
    </template>

    <router-view />
</sw-meteor-page>
```

### Example 3: Simple Full-Width Page
```html
<sw-meteor-page :full-width="true" :hide-icon="true">
    <template #smart-bar-header>
        Custom Page Title
    </template>

    <template #smart-bar-actions>
        <sw-button variant="primary" @click="onSave">Save</sw-button>
    </template>

    <div class="page-content">
        <!-- full-width content -->
    </div>
</sw-meteor-page>
```

### Example 4: Page with Custom Back Navigation
```html
<sw-meteor-page
    :from-link="{ name: 'sw.settings.index' }"
>
    <template #smart-bar-header>
        Settings Detail
    </template>

    <div class="settings-detail-content">
        <!-- settings form -->
    </div>
</sw-meteor-page>
```
