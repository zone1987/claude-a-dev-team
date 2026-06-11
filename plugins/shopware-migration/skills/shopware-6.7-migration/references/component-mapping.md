# Component Mapping Reference: sw-* to mt-*

Complete migration reference for all deprecated `sw-*` administration components to their `mt-*` Meteor replacements in Shopware 6.7. All `sw-*` components are tagged for removal in v6.8.0.

> **Detaillierter Guide:** Für vollständige Props/Events/Slots-Tabellen und echte Vorher/Nachher-Beispiele aus `src/module/` siehe [`component-migration-guide.md`](./component-migration-guide.md).

---

## Shopware Layout Components (NOT migrated to mt-*)

The following `sw-*` components are **Shopware-specific layout components** that are **not** part of the Meteor component library. They have no `mt-*` equivalent and must **not** be replaced:

| Component | Keep As | Notes |
|-----------|---------|-------|
| `sw-page` | `sw-page` | Page layout with smart bar, content slot — no `mt-page` exists |
| `sw-card-view` | `sw-card-view` | Card container layout — no `mt-card-view` exists |

These components remain `sw-*` in Shopware 6.7 and are maintained by Shopware directly.

---

## Master Mapping Table

| # | Old Component | New Component | Codemod Support |
|---|---|---|---|
| 1 | `sw-button` | `mt-button` | Automated |
| 2 | `sw-text-field` | `mt-text-field` | Automated |
| 3 | `sw-number-field` | `mt-number-field` | Automated |
| 4 | `sw-select-field` | `mt-select` | Automated |
| 5 | `sw-switch-field` | `mt-switch` | Automated |
| 6 | `sw-checkbox-field` | `mt-checkbox` | Automated |
| 7 | `sw-alert` | `mt-banner` | Automated |
| 8 | `sw-card` | `mt-card` | Automated |
| 9 | `sw-tabs` | `mt-tabs` | Automated |
| 10 | `sw-icon` | `mt-icon` | Automated |
| 11 | `sw-modal` | `mt-modal` | Manual |
| 12 | `sw-loader` | `mt-loader` | Automated |
| 13 | `sw-password-field` | `mt-password-field` | Automated |
| 14 | `sw-email-field` | `mt-email-field` | Automated |
| 15 | `sw-url-field` | `mt-url-field` | Automated |
| 16 | `sw-textarea-field` | `mt-textarea` | Automated |
| 17 | `sw-colorpicker` | `mt-colorpicker` | Automated |
| 18 | `sw-datepicker` | `mt-datepicker` | Automated |
| 19 | `sw-pagination` | `mt-pagination` | Manual |
| 20 | `sw-skeleton-bar` | `mt-skeleton-bar` | Automated |
| 21 | `sw-progress-bar` | `mt-progress-bar` | Automated |
| 22 | `sw-popover` | `mt-floating-ui` | Automated |
| 23 | `sw-data-grid` | `mt-data-table` | Manual (human review) |
| 24 | `sw-external-link` | `mt-external-link` | Automated |
| 25 | `sw-text-editor` | `mt-text-editor` | Manual (feature flag) |

---

## 1. sw-button to mt-button

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `variant="primary"` | `variant="primary"` | Unchanged |
| `variant="ghost"` | `variant="secondary" :ghost="true"` | Split into variant + ghost |
| `variant="danger"` | `variant="critical"` | Renamed |
| `variant="ghost-danger"` | `variant="critical" :ghost="true"` | Split |
| `variant="contrast"` | `variant="primary"` | Mapped to primary |
| `variant="context"` | `variant="secondary"` | Mapped to secondary |
| `size="x-small"` | `size="x-small"` | Unchanged |
| `size="small"` | `size="small"` | Unchanged (default) |
| `size="large"` | `size="large"` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:isLoading` | `:isLoading` | Unchanged |
| `:block` | `:block` | Unchanged |
| `:square` | `:square` | Unchanged |
| `:router-link` | Removed | Use `@click` + `this.$router.push(...)` — **kein** `<router-link>` Wrapper |
| `link="url"` | Removed (deprecated) | Use `is="a" href="url"` instead |

### Slot Changes

| Old Slot | New Slot |
|---|---|
| `default` | `default` |
| -- | `iconFront` (new, receives `{ size }`) |
| -- | `iconBack` (new, receives `{ size }`) |

### Event Changes

Standard DOM events via `$attrs`. No Shopware-specific events.

### Before/After

```html
<!-- BEFORE -->
<sw-button variant="ghost" @click="onSave">
    {{ $tc('global.default.save') }}
</sw-button>

<sw-button variant="danger" size="small" :disabled="!hasChanges">
    {{ $tc('global.default.delete') }}
</sw-button>

<sw-button variant="primary" :router-link="{ name: 'my.route' }">
    Go to page
</sw-button>

<sw-button variant="primary" :router-link="{ name: 'my.route', params: { id: item.id } }">
    Edit item
</sw-button>

<!-- AFTER -->
<mt-button variant="secondary" :ghost="true" @click="onSave">
    {{ $tc('global.default.save') }}
</mt-button>

<mt-button variant="critical" size="small" :disabled="!hasChanges">
    {{ $tc('global.default.delete') }}
</mt-button>

<!-- router-link: KEIN Wrapper! Stattdessen @click mit $router.push() -->
<mt-button variant="primary" @click="$router.push({ name: 'my.route' })">
    Go to page
</mt-button>

<mt-button variant="primary" @click="$router.push({ name: 'my.route', params: { id: item.id } })">
    Edit item
</mt-button>
```

### Router-Link Migration — Wichtige Regel

`mt-button` unterstützt kein `:router-link` Prop. Buttons mit Router-Navigation werden **nicht** in `<router-link>` gewrappt, sondern erhalten ein `@click` Event mit `$router.push()`.

**Inline (einfache Routen):**
```html
<mt-button @click="$router.push({ name: 'route.name' })">...</mt-button>
```

**Als Methode (empfohlen bei Params oder komplexer Logik):**
```html
<!-- Template -->
<mt-button variant="primary" @click="onNavigate">
    Edit item
</mt-button>

<!-- Script (Options API) -->
methods: {
    onNavigate() {
        this.$router.push({ name: 'my.route', params: { id: this.item.id } });
    },
},

<!-- Script (Composition API) -->
const router = useRouter();
function onNavigate() {
    router.push({ name: 'my.route', params: { id: item.value.id } });
}
```

---

## 2. sw-text-field to mt-text-field

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `@change` | `@change` | Unchanged |
| `:label` | `:label` | Unchanged |
| `:placeholder` | `:placeholder` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:required` | `:required` | Unchanged |
| `:error` | `:error` | Format: `{ code, detail }` |
| `:helpText` | `:helpText` | Unchanged |
| `:copyable` | `:copyable` | Unchanged |
| `:maxLength` | `:maxLength` | Unchanged |
| `:size` | `:size` | `"small"` or `"default"` |
| `:isInheritanceField` | `:isInheritanceField` | Unchanged |
| `:isInherited` | `:isInherited` | Unchanged |

### Slot Changes

| Old Slot | New Slot |
|---|---|
| `prefix` | `prefix` |
| `suffix` | `suffix` |
| `label` | `label` |
| `hint` | `hint` |

### Before/After

```html
<!-- BEFORE -->
<sw-text-field
    :value="product.name"
    :label="$tc('sw-product.detail.labelName')"
    :error="productNameError"
    :helpText="$tc('sw-product.detail.helpName')"
    @input="onNameChange"
/>

<!-- AFTER -->
<mt-text-field
    v-model="product.name"
    :label="$tc('sw-product.detail.labelName')"
    :error="productNameError"
    :helpText="$tc('sw-product.detail.helpName')"
    @update:modelValue="onNameChange"
/>
```

---

## 3. sw-number-field to mt-number-field

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:numberType` | `:numberType` | `"int"` or `"float"` |
| `:step` | `:step` | Unchanged |
| `:min` | `:min` | Unchanged |
| `:max` | `:max` | Unchanged |
| `:label` | `:label` | Unchanged |
| `:digits` | `:digits` | Decimal places for float |
| `:fillDigits` | `:fillDigits` | Pad decimals |

### Before/After

```html
<!-- BEFORE -->
<sw-number-field
    :value="item.stock"
    :label="$tc('sw-product.detail.labelStock')"
    numberType="int"
    :min="0"
    @input="onStockChange"
/>

<!-- AFTER -->
<mt-number-field
    v-model="item.stock"
    :label="$tc('sw-product.detail.labelStock')"
    numberType="int"
    :min="0"
    @update:modelValue="onStockChange"
/>
```

---

## 4. sw-select-field to mt-select

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `:options` | `:options` | Array of `{ label, value }` objects |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:placeholder` | `:placeholder` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:required` | `:required` | Unchanged |
| `:error` | `:error` | Format: `{ code, detail }` |
| `:helpText` | `:helpText` | Unchanged |
| `:aside` | Removed | No longer supported |
| -- | `:enableMultiSelection` | New: replaces multi-select component |
| -- | `:labelProperty` | Default: `"label"` |
| -- | `:valueProperty` | Default: `"value"` |
| -- | `:valueLimit` | Chips shown before collapse |
| -- | `:searchFunction` | Custom search callback |

### Slot Changes

| Old Slot | New Slot |
|---|---|
| `prefix` | `prefix` |
| `suffix` | `suffix` |
| `hint` | `hint` |
| -- | `before-item-list` (new) |
| -- | `result-item` (new, receives item context) |
| -- | `after-item-list` (new) |

### Before/After

```html
<!-- BEFORE -->
<sw-select-field
    :value="config.sortOrder"
    :label="$tc('my-plugin.config.sortOrder')"
    :options="sortOptions"
    @input="onSortChange"
/>

<!-- AFTER -->
<mt-select
    v-model="config.sortOrder"
    :label="$tc('my-plugin.config.sortOrder')"
    :options="sortOptions"
    @update:modelValue="onSortChange"
/>
```

---

## 5. sw-switch-field to mt-switch

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@change` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:bordered` | `:bordered` | Unchanged |
| `:helpText` | `:helpText` | Unchanged |
| `:noMarginTop` | Removed | Use `:removeTopMargin="true"` or CSS |
| `:ghostValue` | Removed | No longer supported |
| `:padded` | Removed | No longer supported |
| `:partlyChecked` | Removed | No longer supported |
| `:size` | Removed | No longer supported |
| `:id` | Removed | Use `name` instead |

### Before/After

```html
<!-- BEFORE -->
<sw-switch-field
    :value="product.active"
    :label="$tc('sw-product.detail.labelActive')"
    :disabled="!acl.can('product.editor')"
    @input="onActiveChange"
/>

<!-- AFTER -->
<mt-switch
    v-model="product.active"
    :label="$tc('sw-product.detail.labelActive')"
    :disabled="!acl.can('product.editor')"
    @change="onActiveChange"
/>
```

---

## 6. sw-checkbox-field to mt-checkbox

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:bordered` | `:bordered` | Unchanged |
| `:helpText` | `:helpText` | Unchanged |
| `:partial` | `:partial` | Indeterminate state |
| -- | `v-model:checked` | Alternative binding via `checked` prop |
| `:ghostValue` | Removed | No longer supported |

### Before/After

```html
<!-- BEFORE -->
<sw-checkbox-field
    :value="item.selected"
    :label="item.name"
    @input="onSelectChange"
/>

<!-- AFTER -->
<mt-checkbox
    v-model="item.selected"
    :label="item.name"
    @update:modelValue="onSelectChange"
/>
```

---

## 7. sw-alert to mt-banner

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `variant="info"` | `variant="info"` | Unchanged |
| `variant="warning"` | `variant="attention"` | **Renamed** |
| `variant="error"` | `variant="critical"` | **Renamed** |
| `variant="success"` | `variant="positive"` | **Renamed** |
| -- | `variant="neutral"` | New default variant |
| -- | `variant="inherited"` | New variant for inheritance |
| `appearance="default"` | Removed | Use `variant` only |
| `appearance="notification"` | Removed | Use `variant` only |
| `appearance="system"` | Removed | Use `variant` only |
| `:title` | `:title` | Unchanged |
| `:closable` | `:closable` | Unchanged |
| `:showIcon` | `:hideIcon` (inverted!) | **Logic inverted**: `showIcon=false` becomes `hideIcon=true` |
| `:notificationIndex` | `:bannerIndex` | **Renamed** |
| `@close` | `@close` | Unchanged |

### Slot Changes

| Old Slot | New Slot |
|---|---|
| `default` | `default` |
| -- | `customIcon` (new) |

### Before/After

```html
<!-- BEFORE -->
<sw-alert variant="error" :title="$tc('error.title')" :closable="true">
    {{ errorMessage }}
</sw-alert>

<sw-alert variant="success" :showIcon="false">
    {{ successMessage }}
</sw-alert>

<!-- AFTER -->
<mt-banner variant="critical" :title="$tc('error.title')" :closable="true">
    {{ errorMessage }}
</mt-banner>

<mt-banner variant="positive" :hideIcon="true">
    {{ successMessage }}
</mt-banner>
```

---

## 8. sw-card to mt-card

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:title` | `:title` | Unchanged |
| `:subtitle` | `:subtitle` | Unchanged |
| `:isLoading` | `:isLoading` | Unchanged |
| `:large` | `:large` | Deprecated in mt-card v4.0.0 |
| `:hero` | Removed | No longer supported |
| `:aiBadge` | Removed | No longer supported |
| -- | `:inheritance` | New: `v-model:inheritance` |

### Slot Changes

| Old Slot | New Slot | Notes |
|---|---|---|
| `default` | `default` | Unchanged |
| `title` | `title` | Unchanged |
| `subtitle` | `subtitle` | Unchanged |
| `avatar` | `avatar` | Unchanged |
| `footer` | `footer` | Unchanged |
| `toolbar` | `toolbar` | Unchanged |
| `tabs` | `tabs` | Unchanged |
| `headerRight` | `headerRight` | Unchanged |
| `context-actions` | `context-actions` | Unchanged |
| `grid` | `grid` | Receives `{ title }` |
| `before-card` | Handled by Shopware wrapper | Not in base mt-card |
| `after-card` | Handled by Shopware wrapper | Not in base mt-card |

### Before/After

```html
<!-- BEFORE -->
<sw-card :title="$tc('my-plugin.detail.cardTitle')" :isLoading="isLoading">
    <sw-text-field :value="item.name" :label="$tc('name')" />
</sw-card>

<!-- AFTER -->
<mt-card :title="$tc('my-plugin.detail.cardTitle')" :isLoading="isLoading">
    <mt-text-field v-model="item.name" :label="$tc('name')" />
</mt-card>
```

---

## 9. sw-tabs to mt-tabs

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:items` (child components) | `:items` (array prop) | **Major change**: items are now data, not children |
| `:vertical` | `:vertical` | Unchanged |
| `:small` | `:small` | Deprecated in v4.0.0 |
| -- | `:defaultItem` | New: set initially active tab |

### Items Format

```javascript
// OLD: sw-tabs used child <sw-tabs-item> components
// NEW: mt-tabs uses a data array
const tabItems = [
    { label: 'General', name: 'general' },
    { label: 'Advanced', name: 'advanced', hasError: false },
    { label: 'Disabled', name: 'disabled', disabled: true },
    { label: 'Warning', name: 'warning', badge: 'warning' },
];
```

### Event Changes

| Old Event | New Event |
|---|---|
| `@new-item-active` | `@new-item-active` (itemName: string) |

### Before/After

```html
<!-- BEFORE -->
<sw-tabs @new-item-active="onTabChange">
    <template #default="{ active }">
        <sw-tabs-item :active-tab="active" name="general">
            {{ $tc('general') }}
        </sw-tabs-item>
        <sw-tabs-item :active-tab="active" name="advanced">
            {{ $tc('advanced') }}
        </sw-tabs-item>
    </template>

    <template #content="{ active }">
        <template v-if="active === 'general'">...</template>
        <template v-if="active === 'advanced'">...</template>
    </template>
</sw-tabs>

<!-- AFTER -->
<mt-tabs
    :items="[
        { label: $tc('general'), name: 'general' },
        { label: $tc('advanced'), name: 'advanced' },
    ]"
    @new-item-active="onTabChange"
/>
<!-- Content is rendered separately based on active tab state -->
<template v-if="activeTab === 'general'">...</template>
<template v-if="activeTab === 'advanced'">...</template>
```

---

## 10. sw-icon to mt-icon

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:name` | `:name` | Icon names from `@shopware-ag/meteor-icon-kit` |
| `:small` | `:size="16px"` | Replaced by explicit size |
| `:large` | `:size="32px"` | Replaced by explicit size |
| `:color` | `:color` | CSS color value |
| `:decorative` | `:decorative` | Sets `aria-hidden` |
| -- | `:mode` | New: `"solid"` or `"regular"` (default) |

### Before/After

```html
<!-- BEFORE -->
<sw-icon name="regular-checkmark-xs" small />
<sw-icon name="regular-times-s" large color="#ff0000" />

<!-- AFTER -->
<mt-icon name="regular-checkmark-xs" size="16px" />
<mt-icon name="regular-times-s" size="32px" color="#ff0000" />
```

---

## 11. sw-modal to mt-modal

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:title` | `:title` | Unchanged |
| `:subtitle` | `:subtitle` | New in mt-modal |
| `:variant` | `:width` | Size names: `"s"`, `"m"`, `"l"`, `"xl"`, `"full"` |
| `variant="small"` | `width="s"` | Renamed |
| `variant="default"` | `width="m"` | Renamed (default) |
| `variant="large"` | `width="l"` | Renamed |
| `variant="full"` | `width="full"` | Renamed |
| -- | `:inset` | New: padding control |
| -- | `:hideHeader` | New: hide header |
| `:showHeader` | `:hideHeader` (inverted) | Logic inverted |

### Slot Changes

| Old Slot | New Slot |
|---|---|
| `default` | `default` |
| `modal-header` | `header-left` + `header-right` |
| `modal-title` | Use `:title` prop |
| `modal-footer` | `footer` |
| -- | `title-after` (new) |

### Before/After

```html
<!-- BEFORE -->
<sw-modal
    :title="$tc('my-plugin.modal.title')"
    variant="large"
    @modal-close="onClose"
>
    <template #modal-body>
        <sw-text-field :value="item.name" />
    </template>
    <template #modal-footer>
        <sw-button variant="primary" @click="onSave">
            {{ $tc('global.default.save') }}
        </sw-button>
    </template>
</sw-modal>

<!-- AFTER -->
<mt-modal
    :title="$tc('my-plugin.modal.title')"
    width="l"
    @close="onClose"
>
    <mt-text-field v-model="item.name" />
    <template #footer>
        <mt-button variant="primary" @click="onSave">
            {{ $tc('global.default.save') }}
        </mt-button>
    </template>
</mt-modal>
```

---

## 12. sw-loader to mt-loader

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:size` | `:size` | Format: `"{number}px"` (default: `"50px"`) |

### Before/After

```html
<!-- BEFORE -->
<sw-loader size="30px" />

<!-- AFTER -->
<mt-loader size="30px" />
```

---

## 13. sw-password-field to mt-password-field

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:placeholder` | `:placeholder` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:required` | `:required` | Unchanged |
| `:error` | `:error` | Format: `{ code, detail }` |
| `:helpText` | `:helpText` | Unchanged |
| `:passwordToggleAble` | `:toggable` | **Renamed** |
| `@submit` | `@submit` | Unchanged |

### Before/After

```html
<!-- BEFORE -->
<sw-password-field
    :value="credentials.password"
    :label="$tc('password')"
    :passwordToggleAble="true"
    @input="onPasswordChange"
/>

<!-- AFTER -->
<mt-password-field
    v-model="credentials.password"
    :label="$tc('password')"
    :toggable="true"
    @update:modelValue="onPasswordChange"
/>
```

---

## 14. sw-email-field to mt-email-field

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:error` | `:error` | Format: `{ detail }` |
| `:copyable` | `:copyable` | Unchanged |
| `:helpText` | `:helpText` | Unchanged |

Built-in email validation is included in the component.

### Before/After

```html
<!-- BEFORE -->
<sw-email-field
    :value="customer.email"
    :label="$tc('email')"
    @input="onEmailChange"
/>

<!-- AFTER -->
<mt-email-field
    v-model="customer.email"
    :label="$tc('email')"
    @update:modelValue="onEmailChange"
/>
```

---

## 15. sw-url-field to mt-url-field

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:omitUrlHash` | `:omitUrlHash` | Unchanged |
| `:omitUrlSearch` | `:omitUrlSearch` | Unchanged |
| `:error` | `:error` | Format: `{ detail }` |
| `:copyable` | `:copyable` | Unchanged |

Features: SSL toggle (https/http), URL parsing, copy-to-clipboard.

### Before/After

```html
<!-- BEFORE -->
<sw-url-field
    :value="shop.url"
    :label="$tc('shopUrl')"
    @input="onUrlChange"
/>

<!-- AFTER -->
<mt-url-field
    v-model="shop.url"
    :label="$tc('shopUrl')"
    @update:modelValue="onUrlChange"
/>
```

---

## 16. sw-textarea-field to mt-textarea

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:placeholder` | `:placeholder` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:required` | `:required` | Unchanged |
| `:maxLength` | `:maxLength` | Shows character counter |
| `:helpText` | `:helpText` | Unchanged |

### Before/After

```html
<!-- BEFORE -->
<sw-textarea-field
    :value="product.description"
    :label="$tc('description')"
    :maxLength="500"
    @input="onDescChange"
/>

<!-- AFTER -->
<mt-textarea
    v-model="product.description"
    :label="$tc('description')"
    :maxLength="500"
    @update:modelValue="onDescChange"
/>
```

---

## 17. sw-colorpicker to mt-colorpicker

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding (hex string) |
| `@input` | `@update:modelValue` | Event renamed |
| `:label` | `:label` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:readonly` | `:readonly` | Unchanged |
| `:helpText` | `:helpText` | Unchanged |
| `:colorOutput` | Removed | Always outputs hex |
| `:zIndex` | Removed | Uses Floating UI |

### Before/After

```html
<!-- BEFORE -->
<sw-colorpicker
    :value="theme.primaryColor"
    :label="$tc('primaryColor')"
    @input="onColorChange"
/>

<!-- AFTER -->
<mt-colorpicker
    v-model="theme.primaryColor"
    :label="$tc('primaryColor')"
    @update:modelValue="onColorChange"
/>
```

---

## 18. sw-datepicker to mt-datepicker

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding |
| `@input` | `@update:modelValue` | Event renamed |
| `:dateType` | `:dateType` | `"date"`, `"datetime"`, `"time"` |
| `:label` | `:label` | Unchanged |
| `:placeholder` | `:placeholder` | Unchanged |
| `:disabled` | `:disabled` | Unchanged |
| `:required` | `:required` | Unchanged |
| `:config` | Removed | Use individual props instead |
| -- | `:locale` | New: locale string (default: `"de"`) |
| -- | `:timeZone` | New: timezone (default: `"UTC"`) |
| -- | `:is24` | New: 24-hour format (default: `true`) |
| -- | `:range` | New: range selection |
| -- | `:minDate` | New: minimum selectable date |
| -- | `:textInput` | New: allow typing dates |
| -- | `:hourIncrement` | New: time picker step |
| -- | `:minuteIncrement` | New: time picker step |

### Before/After

```html
<!-- BEFORE -->
<sw-datepicker
    :value="product.releaseDate"
    :label="$tc('releaseDate')"
    dateType="date"
    @input="onDateChange"
/>

<!-- AFTER -->
<mt-datepicker
    v-model="product.releaseDate"
    :label="$tc('releaseDate')"
    dateType="date"
    @update:modelValue="onDateChange"
/>
```

---

## 19. sw-pagination to mt-pagination

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:total` | `:totalItems` | **Renamed** |
| `:limit` | `:limit` | Unchanged |
| `:page` | `:currentPage` | **Renamed** |
| `@page-change` | `@change-current-page` | **Renamed** |

### Before/After

```html
<!-- BEFORE -->
<sw-pagination
    :total="totalCount"
    :limit="limit"
    :page="currentPage"
    @page-change="onPageChange"
/>

<!-- AFTER -->
<mt-pagination
    :totalItems="totalCount"
    :limit="limit"
    :currentPage="currentPage"
    @change-current-page="onPageChange"
/>
```

---

## 20. sw-skeleton-bar to mt-skeleton-bar

Direct replacement with no prop changes. Shimmer animation, 32px height.

```html
<!-- BEFORE -->
<sw-skeleton-bar />

<!-- AFTER -->
<mt-skeleton-bar />
```

---

## 21. sw-progress-bar to mt-progress-bar

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:value` | `v-model` / `:modelValue` | v-model binding (number) |
| `:label` | `:label` | Required |
| `:maxValue` | `:maxValue` | Required |
| `:error` | `:error` | Format: `{ detail, code }` |
| -- | `:progressLabelType` | New: `"percent"` (default) or unit type |

### Before/After

```html
<!-- BEFORE -->
<sw-progress-bar :value="progress" :maxValue="100" />

<!-- AFTER -->
<mt-progress-bar v-model="progress" label="Upload" :maxValue="100" />
```

---

## 22. sw-popover to mt-floating-ui

### Prop Changes

| Old Prop | New Prop | Notes |
|---|---|---|
| `:isOpened` | `:isOpened` | Required |
| `:popoverClass` | Removed | Use CSS instead |
| `:resizeWidth` | `:matchReferenceWidth` | **Renamed** |
| -- | `:floatingUiOptions` | New: `@floating-ui/dom` config |
| -- | `:showArrow` | New: show positioning arrow |
| -- | `:offset` | New: offset from trigger (default: 6) |

### Slot Changes

| Old Slot | New Slot |
|---|---|
| `default` (trigger) | `trigger` |
| `popover-content` | `default` (receives `{ referenceElementWidth, referenceElementHeight }`) |

### Event Changes

| Old Event | New Event |
|---|---|
| `@close-popover` | `@close` |

### Before/After

```html
<!-- BEFORE -->
<sw-popover :isOpened="showPopover" @close-popover="showPopover = false">
    <template #default>
        <sw-button @click="showPopover = !showPopover">Toggle</sw-button>
    </template>
    <template #popover-content>
        <div>Popover content here</div>
    </template>
</sw-popover>

<!-- AFTER -->
<mt-floating-ui :isOpened="showPopover" @close="showPopover = false">
    <template #trigger>
        <mt-button @click="showPopover = !showPopover">Toggle</mt-button>
    </template>
    <template #default>
        <div>Popover content here</div>
    </template>
</mt-floating-ui>
```

**Note:** For complex popover menus with navigation/views, use `mt-popover` instead of `mt-floating-ui`. `mt-popover` supports `childViews` for nested navigation.

---

## 23. sw-data-grid to mt-data-table

This migration **requires manual review**. The codemod adds TODO comments but cannot auto-migrate.

Key differences:
- Column definitions use a different format
- Selection handling changed
- Pagination is separate (`mt-pagination`)
- Sorting API differs

Consult `component-examples.md` for a full data grid migration example.

---

## 24. sw-external-link to mt-external-link

Direct replacement. Props and slots are compatible.

```html
<!-- BEFORE -->
<sw-external-link href="https://example.com">Link text</sw-external-link>

<!-- AFTER -->
<mt-external-link href="https://example.com">Link text</mt-external-link>
```

---

## 25. sw-text-editor to mt-text-editor

**Note:** Requires feature flag `METEOR_TEXT_EDITOR` to be enabled.

The Shopware wrapper for `mt-text-editor` adds custom toolbar button support. Migration is largely API-compatible but verify toolbar customizations work.

### Before/After

```html
<!-- BEFORE -->
<sw-text-editor
    :value="product.description"
    :label="$tc('description')"
    @input="onDescChange"
/>

<!-- AFTER -->
<mt-text-editor
    v-model="product.description"
    :label="$tc('description')"
    @update:modelValue="onDescChange"
/>
```

---

## Common Migration Patterns

### Inheritance Fields (Sales Channel Inheritance)

All mt-* form fields support the inheritance pattern:

```html
<mt-text-field
    v-model="product.name"
    :is-inheritance-field="isInheritedField"
    :is-inherited="isInherited(product, 'name')"
    @inheritance-restore="restoreInheritance(product, 'name')"
    @inheritance-remove="removeInheritance(product, 'name')"
/>
```

### Error Handling

All mt-* fields use the same error object format:

```javascript
// Shopware error mappers work the same way
computed: {
    nameError() {
        return this.getErrorFor('product.name');
        // Returns: { code: number, detail: string } or null
    },
},
```

### Size Variants

```html
<!-- Form fields: "small" or "default" -->
<mt-text-field size="small" />

<!-- Buttons: "x-small", "small" (default), "default", "large" -->
<mt-button size="large" />
```
