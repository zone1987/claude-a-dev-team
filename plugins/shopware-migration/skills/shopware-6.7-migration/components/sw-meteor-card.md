# sw-meteor-card

> A flexible and extensible content container (card) used in the Shopware Administration. Supports tabs, toolbars, action slots, grid content, and footers. Commonly used in extension and settings pages.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `String` | `null` | no | Title displayed in the card header |
| hero | `Boolean` | `false` | no | Enables hero styling for the card |
| isLoading | `Boolean` | `false` | no | Shows a loader overlay on the card content |
| large | `Boolean` | `false` | no | Applies large card styling |
| defaultTab | `String` | `null` | no | Name of the tab to activate by default |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | `{ activeTab: String }` | Main content area, receives the currently active tab name |
| title | — | Custom title content, replaces the default title rendering |
| action | — | Header action area (e.g. buttons, links) displayed next to the title |
| toolbar | — | Toolbar area below the title and above tabs |
| tabs | `{ activeTab: String }` | Tab items area, should contain `sw-tabs-item` components |
| grid | `{ title: String }` | Grid content area, alternative to default slot for grid layouts |
| footer | — | Footer area below the content |

## Events / Emits

This component does not emit custom events.

## Methods

| Method | Parameters | Return | Description |
|--------|-----------|--------|-------------|
| setActiveTab | `(name: String)` | `void` | Sets the active tab by name |
| createdComponent | — | `void` | Lifecycle method called on created, sets the default tab |

## Data

| Name | Type | Default | Description |
|------|------|---------|-------------|
| activeTab | `String` | `null` | Tracks the currently active tab name |

## Computed Properties

| Name | Type | Description |
|------|------|-------------|
| hasTabs | `Boolean` | Whether the tabs slot is provided |
| hasToolbar | `Boolean` | Whether the toolbar slot is provided |
| hasContent | `Boolean` | Whether the default or grid slot is provided |
| hasDefaultSlot | `Boolean` | Whether the default slot is provided |
| hasHeader | `Boolean` | Whether any header element (toolbar, tabs, title, action) is present |
| isToolbarLastHeaderElement | `Boolean` | Whether the toolbar is the last header element (no tabs) |
| cardClasses | `Object` | Dynamic CSS classes for card styling |

## Examples

### Example 1: Basic Usage with Tabs
Source: component definition (JSDoc example)
```html
<sw-meteor-card defaultTab="tab1">
    <template #tabs="{ activeTab }">
        <sw-tabs-item name="tab1" :activeTab="activeTab">Tab 1</sw-tabs-item>
        <sw-tabs-item name="tab2" :activeTab="activeTab">Tab 2</sw-tabs-item>
    </template>

    <template #default="{ activeTab }">
        <p v-if="activeTab === 'tab1'">Tab 1</p>
        <p v-if="activeTab === 'tab2'">Tab 2</p>
    </template>
</sw-meteor-card>
```

### Example 2: Extension Card Base
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```html
<sw-meteor-card
    class="sw-extension-card-base"
    :class="extensionCardClasses"
>
    <sw-loader v-if="isLoading" />
    <div class="sw-extension-card-base__switch">
        <mt-switch
            v-model="isActive"
            :disabled="!allowActivation"
        />
    </div>
    <!-- card content -->
</sw-meteor-card>
```

### Example 3: With Title and Action Slot
```html
<sw-meteor-card title="Account Settings">
    <template #action>
        <sw-button variant="primary" @click="save">Save</sw-button>
    </template>

    <div class="account-form">
        <!-- form content -->
    </div>
</sw-meteor-card>
```

### Example 4: Hero Card with Loading State
```html
<sw-meteor-card
    :hero="true"
    :is-loading="isLoadingData"
    title="Dashboard Overview"
>
    <div class="dashboard-content">
        <!-- dashboard widgets -->
    </div>
</sw-meteor-card>
```

### Example 5: Card with Footer
```html
<sw-meteor-card title="Product List">
    <div class="product-grid">
        <!-- product items -->
    </div>

    <template #footer>
        <sw-pagination :total="total" :page="page" @page-change="onPageChange" />
    </template>
</sw-meteor-card>
```
