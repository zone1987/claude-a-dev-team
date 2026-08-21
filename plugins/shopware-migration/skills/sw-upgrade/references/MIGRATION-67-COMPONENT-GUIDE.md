# Detailed sw-* → mt-* component migration guide

> Complete migration reference for all 19 deprecated `sw-*` wrapper components to their `mt-*` Meteor replacements in Shopware 6.7. All `sw-*` wrappers are marked as deprecated and will be removed in v6.8.0.

---

## Contents

- [Scope](#scope)
- [Universal migration patterns](#universal-migration-patterns)
- [1. sw-button → mt-button](#1-sw-button-mt-button)
- [2. sw-alert → mt-banner](#2-sw-alert-mt-banner)
- [3. sw-card → mt-card](#3-sw-card-mt-card)
- [4. sw-icon → mt-icon](#4-sw-icon-mt-icon)
- [5. sw-tabs → mt-tabs](#5-sw-tabs-mt-tabs)
- [6. sw-text-field → mt-text-field](#6-sw-text-field-mt-text-field)
- [7. sw-number-field → mt-number-field](#7-sw-number-field-mt-number-field)
- [8. sw-checkbox-field → mt-checkbox](#8-sw-checkbox-field-mt-checkbox)
- [9. sw-switch-field → mt-switch](#9-sw-switch-field-mt-switch)
- [10. sw-select-field → mt-select](#10-sw-select-field-mt-select)
- [11. sw-password-field → mt-password-field](#11-sw-password-field-mt-password-field)
- [12. sw-email-field → mt-email-field](#12-sw-email-field-mt-email-field)
- [13. sw-textarea-field → mt-textarea](#13-sw-textarea-field-mt-textarea)
- [14. sw-colorpicker → mt-colorpicker](#14-sw-colorpicker-mt-colorpicker)
- [15. sw-datepicker → mt-datepicker](#15-sw-datepicker-mt-datepicker)
- [16. sw-url-field → mt-url-field](#16-sw-url-field-mt-url-field)
- [17. sw-loader → mt-loader](#17-sw-loader-mt-loader)
- [18. sw-popover → mt-floating-ui](#18-sw-popover-mt-floating-ui)
- [19. sw-skeleton-bar → mt-skeleton-bar](#19-sw-skeleton-bar-mt-skeleton-bar)
- [Summary of the migration patterns](#summary-of-the-migration-patterns)

## Scope

This document covers exactly **19 deprecated wrapper components** that have an `mt-*` equivalent in Shopware 6.7. Every component is documented with a complete props/events/slots table and real before/after examples from `src/module/`.

### Covered components

| # | Old (sw-*) | New (mt-*) | Category |
|---|-----------|-----------|-----------|
| 1 | `sw-button` | `mt-button` | Base |
| 2 | `sw-alert` | `mt-banner` | Base |
| 3 | `sw-card` | `mt-card` | Base |
| 4 | `sw-icon` | `mt-icon` | Base |
| 5 | `sw-tabs` | `mt-tabs` | Base |
| 6 | `sw-text-field` | `mt-text-field` | Form |
| 7 | `sw-number-field` | `mt-number-field` | Form |
| 8 | `sw-checkbox-field` | `mt-checkbox` | Form |
| 9 | `sw-switch-field` | `mt-switch` | Form |
| 10 | `sw-select-field` | `mt-select` | Form |
| 11 | `sw-password-field` | `mt-password-field` | Form |
| 12 | `sw-email-field` | `mt-email-field` | Form |
| 13 | `sw-textarea-field` | `mt-textarea` | Form |
| 14 | `sw-colorpicker` | `mt-colorpicker` | Form |
| 15 | `sw-datepicker` | `mt-datepicker` | Form |
| 16 | `sw-url-field` | `mt-url-field` | Form |
| 17 | `sw-loader` | `mt-loader` | Utils |
| 18 | `sw-popover` | `mt-floating-ui` | Utils |
| 19 | `sw-skeleton-bar` | `mt-skeleton-bar` | Utils |

### NOT migrated (no mt-* replacement or not via a wrapper)

| Component | Status | Reason |
|-----------|--------|-------|
| `sw-page` | stays `sw-page` | Shopware-specific layout, no `mt-page` |
| `sw-card-view` | stays `sw-card-view` | Shopware-specific layout, no `mt-card-view` |
| `sw-modal` | stays `sw-modal` | 136 usages in 6.7, only 6× `mt-modal` in new modules |
| `sw-external-link` | stays `sw-external-link` | No deprecated wrapper in 6.7 |
| `sw-data-grid` | manual → `mt-data-table` | Completely different API, requires manual migration |
| `sw-progress-bar` | directly `mt-progress-bar` | No deprecated wrapper — direct usage |

---

## Universal migration patterns

### v-model change (all form fields)

| Old | New | Application |
|-----|-----|-----------|
| `v-model:value="x"` | `v-model="x"` | Standard for all fields |
| `:value="x"` + `@update:value` | `:modelValue="x"` + `@update:modelValue` | One-way binding |
| `@input` | `@update:modelValue` | Event name for value changes |
| `v-model:value="x"` (checkbox) | `v-model:checked="x"` | **Only for mt-checkbox!** |

### Button variants

| Old (sw-button) | New (mt-button) |
|----------------|-----------------|
| *(no variant)* | `variant="secondary"` |
| `variant="primary"` | `variant="primary"` |
| `variant="danger"` | `variant="critical"` |
| `variant="ghost"` | `variant="tertiary"` |
| `variant="ghost-danger"` | `variant="critical" ghost` |
| `variant="contrast"` | `variant="primary"` |
| `variant="context"` | `variant="secondary"` |

### Alert/banner variants

| Old (sw-alert) | New (mt-banner) |
|---------------|-----------------|
| `variant="info"` | `variant="info"` |
| `variant="warning"` | `variant="attention"` |
| `variant="error"` | `variant="critical"` |
| `variant="success"` | `variant="positive"` |

### Codemod tool

Shopware provides a codemod that performs many of these migrations automatically:
```bash
npx @shopware-ag/meteor-admin-sdk-codemod
```

> **Note:** The codemod covers most prop renames and component names, but more complex migrations (tabs items, select options, router link) require manual follow-up work.

---

## 1. sw-button → mt-button

> From v6.7 on, the `sw-button` wrapper forwards to the Meteor component `mt-button`. The `routerLink` prop is handled in the wrapper via `$router.push()` and no longer exists in `mt-button` itself. The wrapper sets a fallback `variant="secondary"`.

### Props

| Old (sw-button) | New (mt-button) | Change |
|-----------|-----------|----------|
| `variant`: `primary`, `ghost`, `danger`, `ghost-danger`, `contrast`, `context` | `variant`: `primary`, `secondary`, `tertiary`, `critical`, `action` | Values renamed: `ghost` → `tertiary`, `danger` → `critical`; default `""` → `"secondary"` |
| `size`: `x-small`, `small` (default: `""`) | `size`: `x-small`, `small`, `default`, `large` (default: `"default"`) | New sizes `default` and `large` added |
| `routerLink` (Object) | — dropped — | Wrapper takes over via `$router.push()`; `mt-button` has no `routerLink` |
| `isLoading` (Boolean) | `isLoading` (Boolean) | Identical |
| — | `ghost` (Boolean) | New: separate boolean prop for the ghost appearance |
| — | `is` (Component/String) | New: allows rendering as a different element |

### Events

| Old (sw-button) | New (mt-button) | Change |
|-----------|-----------|----------|
| `@click` | `@click` | Identical |

### Slots

| Old (sw-button) | New (mt-button) | Change |
|-----------|-----------|----------|
| `default` | `default` | Identical |
| — | `iconFront` (scope: `{ size }`) | New: slot for an icon before the text |
| — | `iconBack` (scope: `{ size }`) | New: slot for an icon after the text |

### Before (6.6)
```twig
<!-- File: src/module/sw-settings-customer-group/page/sw-settings-customer-group-detail/sw-settings-customer-group-detail.html.twig -->
{% block sw_settings_customer_group_detail_actions_cancel %}
<sw-button
    v-tooltip.bottom="tooltipCancel"
    class="sw-settings-customer-group-detail__cancel"
    @click="onCancel"
>
    {{ $tc('global.default.cancel') }}
</sw-button>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-settings-customer-group/page/sw-settings-customer-group-detail/sw-settings-customer-group-detail.html.twig -->
{% block sw_settings_customer_group_detail_actions_cancel %}
<mt-button
    v-tooltip.bottom="tooltipCancel"
    class="sw-settings-customer-group-detail__cancel"
    variant="secondary"
    size="default"
    @click="onCancel"
>
    {{ $tc('global.default.cancel') }}
</mt-button>
{% endblock %}
```

### Router-link migration

`mt-button` does not support a `:router-link` prop. Buttons with router navigation get an `@click` event with `$router.push()`:

```html
<!-- Inline (simple routes): -->
<mt-button @click="$router.push({ name: 'route.name' })">...</mt-button>

<!-- As a method (recommended for params): -->
<mt-button variant="primary" @click="onNavigate">Edit item</mt-button>
```

---

## 2. sw-alert → mt-banner

> The component name changes from "Alert" to "Banner". The variant values are renamed (`warning` → `attention`, `error` → `critical`, `success` → `positive`). The `appearance` prop is dropped entirely.

### Props

| Old (sw-alert) | New (mt-banner) | Change |
|-----------|-----------|----------|
| `variant`: `info`, `warning`, `error`, `success` | `variant`: `info`, `attention`, `critical`, `positive`, `neutral`, `inherited` | Renamed: `warning` → `attention`, `error` → `critical`, `success` → `positive`; new: `inherited` |
| `appearance`: `default`, `notification`, `system` | — dropped — | Removed entirely in `mt-banner` |
| `showIcon` (Boolean, default: `true`) | `hideIcon` (Boolean, default: `false`) | **Logic inverted**: `showIcon=false` → `hideIcon=true` |
| `notificationIndex` (String) | `bannerIndex` (String) | Renamed |
| `closable` (Boolean) | `closable` (Boolean) | Identical |
| `title` (String) | `title` (String) | Identical |

### Events

| Old (sw-alert) | New (mt-banner) | Change |
|-----------|-----------|----------|
| `@close(notificationIndex)` | `@close(bannerIndex?)` | Parameter renamed |

### Slots

| Old (sw-alert) | New (mt-banner) | Change |
|-----------|-----------|----------|
| `default` | `default` | Identical |
| `actions` | — dropped — | The slot no longer exists in `mt-banner` |
| — | `customIcon` | New: custom icon |

### Before (6.6)
```twig
<!-- File: src/module/sw-category/component/sw-category-view/sw-category-view.html.twig -->
{% block sw_category_view_column_info %}
<sw-alert
    v-if="category.isColumn"
    class="swag-category-view__column-info"
    variant="info"
>
    <div class="swag-category-view__column-info-header">
        {{ $tc('sw-category.view.columnInfoHeader') }}
    </div>
    <div class="swag-category-view__column-info-content">
        {{ $tc('sw-category.view.columnInfo') }}
    </div>
</sw-alert>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-category/component/sw-category-view/sw-category-view.html.twig -->
{% block sw_category_view_column_info %}
<mt-banner
    v-if="isCategoryColumn"
    class="swag-category-view__column-info"
    variant="info"
>
    <div class="swag-category-view__column-info-header">
        {{ $tc('sw-category.view.columnInfoHeader') }}
    </div>
    <div class="swag-category-view__column-info-content">
        {{ $tc('sw-category.view.columnInfo') }}
    </div>
</mt-banner>
{% endblock %}
```

---

## 3. sw-card → mt-card

> The wrapper forwards all slots dynamically to `mt-card`. The props `hero`, `aiBadge` and `contentPadding` are dropped. The slot `header-right` becomes `headerRight` (camelCase).

### Props

| Old (sw-card) | New (mt-card) | Change |
|-----------|-----------|----------|
| `positionIdentifier` (String, required) | — via $attrs — | No longer a required prop; passed through via `$attrs` |
| `hero` (Boolean) | — dropped — | Removed entirely |
| `aiBadge` (Boolean) | — dropped — | Removed entirely |
| `contentPadding` (Boolean) | — dropped — | Removed entirely |
| `title` (String) | `title` (String) | Identical |
| `subtitle` (String) | `subtitle` (String) | Identical |
| `isLoading` (Boolean) | `isLoading` (Boolean) | Identical |
| `large` (Boolean) | `large` (Boolean) | Identical |
| — | `inheritance` (Boolean) | New: inheritance mode with `v-model:inheritance` |

### Events

| Old (sw-card) | New (mt-card) | Change |
|-----------|-----------|----------|
| — | `@update:inheritance(value)` | New: event for the inheritance toggle |

### Slots

| Old (sw-card) | New (mt-card) | Change |
|-----------|-----------|----------|
| `default` | `default` | Identical |
| `title` | `title` | Identical |
| `subtitle` | `subtitle` | Identical |
| `avatar` | `avatar` | Identical |
| `footer` | `footer` | Identical |
| `toolbar` | `toolbar` | Identical |
| `tabs` | `tabs` | Identical |
| `header-right` | `headerRight` | **Renamed**: kebab-case → camelCase |
| `context-actions` | `context-actions` | Identical |
| `grid` | `grid` | Identical |

### Before (6.6)
```twig
<!-- File: src/module/sw-settings-delivery-times/page/sw-settings-delivery-time-list/sw-settings-delivery-time-list.html.twig -->
{% block sw_settings_delivery_time_list_grid_wrapper %}
<sw-card position-identifier="sw-settings-delivery-time-list-grid-wrapper">
    <template #grid>
        {% block sw_settings_delivery_time_list_grid %}
        <sw-entity-listing
            class="sw-settings-delivery-time-list-grid"
            :items="deliveryTimes"
            :columns="deliveryTimeColumns()"
        />
        {% endblock %}
    </template>
</sw-card>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-settings-delivery-times/page/sw-settings-delivery-time-list/sw-settings-delivery-time-list.html.twig -->
{% block sw_settings_delivery_time_list_grid_wrapper %}
<mt-card position-identifier="sw-settings-delivery-time-list-grid-wrapper">
    <template #grid>
        {% block sw_settings_delivery_time_list_grid %}
        <sw-entity-listing
            class="sw-settings-delivery-time-list-grid"
            :data-source="deliveryTimes"
            :columns="deliveryTimeColumns()"
        />
        {% endblock %}
    </template>
</mt-card>
{% endblock %}
```

---

## 4. sw-icon → mt-icon

> The boolean props `small` and `large` are dropped in favor of an explicit `size` string. The default size is `"24px"`. The new `mode` prop allows distinguishing between `solid` and `regular` icons.

### Props

| Old (sw-icon) | New (mt-icon) | Change |
|-----------|-----------|----------|
| `small` (Boolean) | — dropped — | Replaced by `size="16px"` |
| `large` (Boolean) | — dropped — | Replaced by `size="32px"` |
| `size` (String) | `size` (String, default: `"24px"`) | Default is now explicitly `"24px"` |
| `name` (String, required) | `name` (String, required) | Identical |
| `color` (String) | `color` (String) | Identical |
| `decorative` (Boolean) | `decorative` (Boolean) | Identical |
| — | `mode`: `solid`, `regular` | New: explicit choice between solid and regular icons |

### Events

No relevant event changes.

### Slots

| Old (sw-icon) | New (mt-icon) | Change |
|-----------|-----------|----------|
| `default` | — dropped — | `mt-icon` has no default slot |

### Before (6.6)
```twig
<!-- File: src/module/sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig -->
<sw-icon
    small
    name="regular-files"
    class="sw-media-sidebar__quickactions-icon"
/>
```

### After (6.7)
```twig
<!-- File: src/module/sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig -->
<mt-icon
    size="16px"
    name="regular-files"
    class="sw-media-sidebar__quickactions-icon"
/>
```

---

## 5. sw-tabs → mt-tabs

> The most fundamental change: `mt-tabs` uses a declarative `:items` array prop instead of `sw-tabs-item` child components in slots. Route navigation is defined via an `onClick` callback in the item object. In 6.7 the wrapper automatically converts the old `sw-tabs-item` children; from v6.8.0 on, `mt-tabs` must be used directly with `:items`.

### Props

| Old (sw-tabs) | New (mt-tabs) | Change |
|-----------|-----------|----------|
| Child components `<sw-tabs-item>` in the default slot | `:items` (array of `TabItem[]`) | **Completely new model**: declarative array instead of slot children |
| `isVertical` (Boolean) | `vertical` (Boolean) | Renamed |
| `small` (Boolean) | `small` (Boolean) | Deprecated in Meteor v4 |
| `alignRight` (Boolean) | — dropped — | Removed entirely |
| `defaultItem` (String) | `defaultItem` (String) | Identical |

**TabItem interface (new):**
```typescript
interface TabItem {
    label: string;      // Display text (formerly: slot content of sw-tabs-item)
    name: string;       // Identifier (formerly: name prop on sw-tabs-item)
    hasError?: boolean;
    disabled?: boolean;
    badge?: "positive" | "critical" | "warning" | "info";
    onClick?: (name: string) => void;  // Formerly: route prop on sw-tabs-item
    hidden?: boolean;
}
```

### Events

| Old (sw-tabs) | New (mt-tabs) | Change |
|-----------|-----------|----------|
| `@new-item-active(item)` | `@new-item-active(item)` | Identical |

### Slots

| Old (sw-tabs) | New (mt-tabs) | Change |
|-----------|-----------|----------|
| `default` (scope: `{ active }`) — contains `sw-tabs-item` children | — dropped — | Replaced by the `:items` prop |
| `content` (scope: `{ active }`) | `content` (scope: `{ active }`) | Content slot remains (in the wrapper) |

### Before (6.6)
```twig
<!-- File: src/module/sw-category/component/sw-category-view/sw-category-view.html.twig -->
<sw-tabs
    v-if="!isLoading"
    position-identifier="sw-category-view"
    class="sw-customer-detail-page__tabs"
>
    <sw-tabs-item
        class="sw-category-detail__tab-base"
        :route="{ name: 'sw.category.detail.base' }"
        :title="$tc('sw-category.view.general')"
    >
        {{ $tc('sw-category.view.general') }}
    </sw-tabs-item>

    <sw-tabs-item
        v-show="isPage && !isCustomEntity"
        class="sw-category-detail__tab-products"
        :route="{ name: 'sw.category.detail.products' }"
        :title="$tc('sw-category.view.products')"
    >
        {{ $tc('sw-category.view.products') }}
    </sw-tabs-item>
</sw-tabs>
```

### After (6.7 — target format with mt-tabs)
```twig
<!-- Target format for direct mt-tabs usage (required from v6.8) -->
<mt-tabs
    v-if="!isLoading"
    position-identifier="sw-category-view"
    :items="[
        {
            label: $tc('sw-category.view.general'),
            name: 'general',
            onClick: () => $router.push({ name: 'sw.category.detail.base' })
        },
        {
            label: $tc('sw-category.view.products'),
            name: 'products',
            hidden: !(isPage && !isCustomEntity),
            onClick: () => $router.push({ name: 'sw.category.detail.products' })
        }
    ]"
    @new-item-active="onTabChange"
/>
```

> **Note:** In 6.7 `sw-tabs` is still used in the modules — the wrapper automatically converts the `sw-tabs-item` children into the `items` array (see the `itemsBackwardCompatible` computed property). From v6.8.0 on, the wrapper is removed.

---

## 6. sw-text-field → mt-text-field

> Simple text input field. The wrapper converts `value`/`update:value` to the Vue 3 standard `modelValue`/`update:modelValue`.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |
| `copyable` | — dropped — | Removed in mt-text-field |
| `copyableTooltip` | — dropped — | Removed in mt-text-field |
| `idSuffix` | — dropped — | Removed in mt-text-field |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed (Vue 3 standard) |
| `@inheritance-restore` | — dropped — | Removed |
| `@inheritance-remove` | — dropped — | Removed |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `label` | `label` | Identical |
| `hint` | `hint` | Identical |

### Before (6.6)
```twig
<!-- File: src/module/sw-newsletter-recipient/page/sw-newsletter-recipient-detail/sw-newsletter-recipient-detail.html.twig -->
{% block sw_newsletter_recipient_detail_form_title %}
<sw-text-field
    v-model:value="newsletterRecipient.title"
    :label="$tc('sw-newsletter-recipient.list.title')"
    :disabled="!acl.can('newsletter_recipient.editor')"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-newsletter-recipient/page/sw-newsletter-recipient-detail/sw-newsletter-recipient-detail.html.twig -->
{% block sw_newsletter_recipient_detail_form_title %}
<mt-text-field
    v-model="newsletterRecipient.title"
    :label="$tc('sw-newsletter-recipient.list.title')"
    :disabled="!acl.can('newsletter_recipient.editor')"
/>
{% endblock %}
```

---

## 7. sw-number-field → mt-number-field

> Numeric input field with support for integer/float, min/max/step. The wrapper converts `value` to `v-model` and additionally emits `change` for backward compatibility.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |
| `digits` | — dropped — | Removed in mt-number-field |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed (Vue 3 standard) |
| `@input-change` | — dropped — | Removed |
| `@change` | `@change` | Identical (the wrapper still emits it for compatibility) |
| `@inheritance-restore` | — dropped — | Removed |
| `@inheritance-remove` | — dropped — | Removed |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `label` | `label` | Identical |
| `hint` | `hint` | Identical |

### Before (6.6)
```twig
<!-- File: src/module/sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig -->
<sw-number-field
    v-model:value="promotion.priority"
    :disabled="!acl.can('promotion.editor')"
    :label="$tc('sw-promotion-v2.detail.base.general.priorityLabel')"
    :help-text="$tc('sw-promotion-v2.detail.base.general.helpTextPriority')"
/>
```

### After (6.7)
```twig
<!-- File: src/module/sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig -->
<mt-number-field
    v-model="promotion.priority"
    :disabled="!acl.can('promotion.editor')"
    :label="$tc('sw-promotion-v2.detail.base.general.priorityLabel')"
    :step="1"
    :min="0"
    number-type="int"
    :help-text="$tc('sw-promotion-v2.detail.base.general.helpTextPriority')"
/>
```

---

## 8. sw-checkbox-field → mt-checkbox

> Checkbox field for boolean values. **Most important change**: the binding switches from `value` to `checked` — for both the prop and the event. This is the only component that uses `v-model:checked` instead of `v-model`.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` (Boolean) | `checked` (Boolean) | **Renamed**: `v-model:value` becomes `v-model:checked` |
| `ghostValue` | — dropped — | Removed |
| `inheritedValue` | — dropped — | Removed |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:checked` | **Renamed**: the wrapper converts `update:checked` to `update:value` |
| `@inheritance-restore` | — dropped — | Removed |
| `@inheritance-remove` | — dropped — | Removed |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `label` | `label` | Identical |
| `hint` | `hint` | Identical |

### Before (6.6)
```twig
<!-- File: src/module/sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig -->
{% block sw_bulk_edit_change_type_field_renderer_change_field_title %}
<sw-checkbox-field
    v-model:value="bulkEditData[formField.name].isChanged"
    class="sw-bulk-edit-change-field__change"
    :label="!formField.config.changeLabel ? $tc('sw-bulk-edit.general.defaultChangeLabel') : formField.config.changeLabel"
    :help-text="formField.labelHelpText"
    :disabled="!!bulkEditData[formField.name].disabled"
    @update:value="onChangeToggle($event, formField.name)"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig -->
{% block sw_bulk_edit_change_type_field_renderer_change_field_title %}
<mt-checkbox
    v-model:checked="bulkEditData[formField.name].isChanged"
    class="sw-bulk-edit-change-field__change"
    :label="!formField.config.changeLabel ? $tc('sw-bulk-edit.general.defaultChangeLabel') : formField.config.changeLabel"
    :help-text="formField.labelHelpText"
    :disabled="!!bulkEditData[formField.name].disabled"
    @update:checked="onChangeToggle($event, formField.name)"
/>
{% endblock %}
```

---

## 9. sw-switch-field → mt-switch

> Toggle/switch for boolean values. The typo `borderd` is corrected to `bordered`. The props `size` and `noMarginTop` are dropped.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` (Boolean) | `modelValue` (Boolean) | Renamed: `v-model:value` becomes `v-model` |
| `checked` (Boolean) | `modelValue` (Boolean) | Merged: the wrapper accepts both |
| `borderd` | `bordered` | **Typo corrected** |
| `size` | — dropped — | Removed (`small`, `medium`, `default`) |
| `noMarginTop` | — dropped — | Removed |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed |
| `@inheritance-restore` | — dropped — | Removed |
| `@inheritance-remove` | — dropped — | Removed |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `label` | — dropped — | The label is only passed as a prop |
| `hint` | — dropped — | `mt-switch` has no slot support |

### Before (6.6)
```twig
<!-- File: src/module/sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig -->
{% block sw_category_detail_information_visible %}
<sw-switch-field
    v-model:value="reversedVisibility"
    borderd
    :disabled="!acl.can('category.editor')"
    :label="$tc('sw-category.base.menu.visible')"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig -->
{% block sw_category_detail_information_visible %}
<mt-switch
    v-model="reversedVisibility"
    bordered
    :disabled="!acl.can('category.editor')"
    :label="$tc('sw-category.base.menu.visible')"
/>
{% endblock %}
```

---

## 10. sw-select-field → mt-select

> Native select dropdown. **Most severe change**: `<option>` slots in the template are dropped entirely and replaced by an `:options` array prop. The options must be moved into a JavaScript array in the component.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |
| `options` (optional, array) | `options` (required, array) | Now **the only way** to define options (slots are dropped) |
| `aside` | — dropped — | Removed |
| `placeholder` | `placeholder` | Identical |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed (Vue 3 standard) |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| default (`<option>` elements) | — dropped — | **Removed**: options must be passed as an `:options` array |
| `label` | — dropped — | Removed as a slot |
| `hint` | — dropped — | Removed as a slot |

### Before (6.6)
```twig
<!-- File: src/module/sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig -->
{% block sw_cms_block_config_background_image_position_field %}
<sw-select-field
    v-model:value="block.backgroundMediaMode"
    :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
    :disabled="!block.backgroundMediaId"
>
    <option value="auto">
        {{ $tc('sw-cms.detail.label.backgroundMediaModeAuto') }}
    </option>
    <option value="contain">
        {{ $tc('sw-cms.detail.label.backgroundMediaModeContain') }}
    </option>
    <option value="cover">
        {{ $tc('sw-cms.detail.label.backgroundMediaModeCover') }}
    </option>
</sw-select-field>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig -->
{% block sw_cms_block_config_background_image_position_field %}
<mt-select
    v-model="block.backgroundMediaMode"
    :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
    :disabled="!block.backgroundMediaId"
    :options="backgroundModeOptions"
/>
{% endblock %}
```

**Moving the options into the component:**
```js
computed: {
    backgroundModeOptions() {
        return [
            { value: 'auto', label: this.$tc('sw-cms.detail.label.backgroundMediaModeAuto') },
            { value: 'contain', label: this.$tc('sw-cms.detail.label.backgroundMediaModeContain') },
            { value: 'cover', label: this.$tc('sw-cms.detail.label.backgroundMediaModeCover') },
        ];
    },
},
```

---

## 11. sw-password-field → mt-password-field

> Password input field with a visibility toggle. Structurally very similar to `sw-text-field`.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |
| `placeholder` | `placeholder` | Identical (passed through explicitly) |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed; the wrapper emits both for compatibility |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `label` | `label` | Identical |
| `hint` | `hint` | Identical |

### Before (6.6)
```twig
<!-- File: src/module/sw-login/view/sw-login-login/sw-login-login.html.twig -->
{% block sw_login_login_password_field %}
<sw-password-field
    v-model:value="password"
    name="sw-field--password"
    :label="$tc('sw-login.index.labelPassword')"
    :placeholder="$tc('sw-login.index.placeholderPassword')"
    :disabled="showLoginAlert"
    required
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-login/view/sw-login-login/sw-login-login.html.twig -->
{% block sw_login_login_password_field %}
<mt-password-field
    v-model="password"
    name="sw-field--password"
    :label="$tc('sw-login.index.labelPassword')"
    :placeholder="$tc('sw-login.index.placeholderPassword')"
    :disabled="showLoginAlert"
    required
/>
{% endblock %}
```

---

## 12. sw-email-field → mt-email-field

> Email input field with built-in validation. Follows the standard v-model migration pattern.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed (Vue 3 standard) |

### Slots

No changes. Slots (`default`, `prefix`) are passed through 1:1.

### Before (6.6)
```twig
<!-- File: src/module/sw-customer/component/sw-customer-card/sw-customer-card.html.twig -->
{% block sw_customer_card_metadata_customer_email_editor %}
<sw-email-field
    v-else
    v-model:value="customer.email"
    name="sw-field--customer-email"
    validation="required"
    required
    :label="$tc('sw-customer.card.labelEmail')"
    :placeholder="$tc('sw-customer.card.placeholderEmail')"
    :error="customerEmailError"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-customer/component/sw-customer-card/sw-customer-card.html.twig -->
{% block sw_customer_card_metadata_customer_email_editor %}
<mt-email-field
    v-else
    v-model="customer.email"
    name="sw-field--customer-email"
    validation="required"
    required
    :label="$tc('sw-customer.card.labelEmail')"
    :placeholder="$tc('sw-customer.card.placeholderEmail')"
    :error="customerEmailError"
/>
{% endblock %}
```

---

## 13. sw-textarea-field → mt-textarea

> Multi-line text input field. **Caution**: the component name changes from `sw-textarea-field` to `mt-textarea` (not `mt-textarea-field`).

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed (Vue 3 standard) |

### Slots

No changes. Slots (`default`, `hint`) are passed through.

### Before (6.6)
```twig
<!-- File: src/module/sw-category/component/sw-category-seo-form/sw-category-seo-form.html.twig -->
{% block sw_category_seo_form_meta_description %}
<sw-textarea-field
    v-model:value="category.metaDescription"
    maxlength="255"
    :disabled="!acl.can('category.editor')"
    :label="$tc('sw-category.base.seo.labelMetaDescription')"
    :help-text="$tc('sw-landing-page.base.seo.helpTextMetaDescription')"
    :placeholder="$tc('sw-category.base.seo.placeholderMetaDescription')"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-category/component/sw-category-seo-form/sw-category-seo-form.html.twig -->
{% block sw_category_seo_form_meta_description %}
<mt-textarea
    v-model="category.metaDescription"
    maxlength="255"
    :disabled="!acl.can('category.editor')"
    :label="$tc('sw-category.base.seo.labelMetaDescription')"
    :help-text="$tc('sw-landing-page.base.seo.helpTextMetaDescription')"
    :placeholder="$tc('sw-category.base.seo.placeholderMetaDescription')"
/>
{% endblock %}
```

---

## 14. sw-colorpicker → mt-colorpicker

> Color picker component. The `color-output` prop is dropped (it was `auto`, `hex`, `hsl`, `rgb`). `mt-colorpicker` always outputs hex.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |
| `color-output` | — dropped — | Removed; `mt-colorpicker` always outputs hex |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed |
| `@change` | `@update:modelValue` | `@change` is mapped to `@update:modelValue` in the wrapper |

### Slots

No changes. The default slot is passed through.

### Before (6.6)
```twig
<!-- File: src/module/sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig -->
{% block sw_property_option_detail_color %}
<sw-colorpicker
    v-model:value="currentOption.colorHexCode"
    name="sw-field--currentOption-colorHexCode"
    color-output="hex"
    :disabled="!allowEdit"
    :label="$tc('sw-property.detail.labelOptionColor')"
    :z-index="1000"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig -->
{% block sw_property_option_detail_color %}
<mt-colorpicker
    v-model="colorHexCode"
    name="sw-field--currentOption-colorHexCode"
    :disabled="!allowEdit"
    :label="$tc('sw-property.detail.labelOptionColor')"
    :z-index="1000"
/>
{% endblock %}
```

---

## 15. sw-datepicker → mt-datepicker

> Date picker component with a calendar and various date formats. Follows the standard v-model migration pattern.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed |

### Slots

No changes.

### Before (6.6)
```twig
<!-- File: src/module/sw-customer/component/sw-customer-base-form/sw-customer-base-form.html.twig -->
{% block sw_customer_base_form_birthday_field %}
<sw-datepicker
    v-model:value="customer.birthday"
    type="date"
    name="birthday"
    hide-hint
    :label="$tc('sw-customer.baseForm.labelBirthday')"
    :placeholder="$tc('sw-datepicker.date.placeholder')"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-customer/component/sw-customer-base-form/sw-customer-base-form.html.twig -->
{% block sw_customer_base_form_birthday_field %}
<mt-datepicker
    v-model="customer.birthday"
    type="date"
    name="birthday"
    hide-hint
    :label="$tc('sw-customer.baseForm.labelBirthday')"
    :placeholder="$tc('sw-datepicker.date.placeholder')"
/>
{% endblock %}
```

---

## 16. sw-url-field → mt-url-field

> URL input field with a protocol prefix display (SSL toggle). Follows the standard v-model migration pattern.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `value` | `modelValue` | Renamed: `v-model:value` becomes `v-model` |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Renamed |

### Slots

No changes.

### Before (6.6)
```twig
<!-- File: src/module/sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig -->
{% block sw_sales_channel_detail_domains_input_url %}
<sw-url-field
    v-model:value="currentDomain.url"
    type="text"
    omit-url-hash
    omit-url-search
    :label="$tc('sw-sales-channel.detail.labelInputUrl')"
    :error="error"
    @update:value="onInput"
/>
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig -->
{% block sw_sales_channel_detail_domains_input_url %}
<mt-url-field
    v-model="currentDomain.url"
    type="text"
    omit-url-hash
    omit-url-search
    :label="$tc('sw-sales-channel.detail.labelInputUrl')"
    :error="error"
    @update:model-value="onInput"
/>
{% endblock %}
```

---

## 17. sw-loader → mt-loader

> Loading spinner for asynchronous operations. Simple 1:1 replacement without prop changes.

### Props

No changes. The `size` prop stays identical (format: `"${number}px"`, default: `"50px"`).

### Events

No events.

### Slots

No slots.

### Before (6.6)
```twig
<!-- File: src/module/sw-login/page/index/sw-login.html.twig -->
{% block sw_login_loader %}
<sw-loader v-if="isLoading" />
{% endblock %}
```

### After (6.7)
```twig
<!-- File: src/module/sw-login/page/index/sw-login.html.twig -->
{% block sw_login_loader %}
<mt-loader v-if="isLoading" />
{% endblock %}
```

---

## 18. sw-popover → mt-floating-ui

> Far-reaching change: `sw-popover` had its own positioning logic. `mt-floating-ui` uses `@floating-ui/dom`. The wrapper maps `resizeWidth` to `matchReferenceWidth` and the slot structure changes fundamentally.

### Props

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `resizeWidth` | `matchReferenceWidth` | **Renamed** |
| `popoverClass` | — dropped — | Removed; use CSS directly |
| `popoverConfigExtension` | `floatingUiOptions` | Replaced by `@floating-ui/dom` config |
| `isOpened` | `isOpened` | Identical |
| — | `showArrow` (Boolean) | New: arrow display |
| — | `offset` (Number) | New: distance from the trigger (default: 6) |

### Events

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `@close-popover` | `@close` | Renamed |

### Slots

| Old (sw-*) | New (mt-*) | Change |
|-----------|-----------|----------|
| `default` (trigger element) | `trigger` | **Renamed**: trigger content into the new `trigger` slot |
| `popover-content` | `default` (scope: `{ referenceElementWidth, referenceElementHeight }`) | **Renamed**: popover content becomes the default slot |

### Before (6.6)
```twig
<!-- Conceptual example for sw-popover -->
<sw-popover :isOpened="showPopover" @close-popover="showPopover = false">
    <template #default>
        <sw-button @click="showPopover = !showPopover">Toggle</sw-button>
    </template>
    <template #popover-content>
        <div>Popover content here</div>
    </template>
</sw-popover>
```

### After (6.7)
```twig
<!-- Direct mt-floating-ui format -->
<mt-floating-ui :isOpened="showPopover" @close="showPopover = false">
    <template #trigger>
        <mt-button @click="showPopover = !showPopover">Toggle</mt-button>
    </template>
    <template #default>
        <div>Popover content here</div>
    </template>
</mt-floating-ui>
```

> **Note:** In 6.7 `sw-popover` is still used in modules as the wrapper name. The wrapper delegates internally to `mt-floating-ui`. From v6.8.0 on, `mt-floating-ui` must be used directly.

---

## 19. sw-skeleton-bar → mt-skeleton-bar

> Skeleton loading placeholder. Simple 1:1 replacement without prop, event or slot changes.

### Props

No changes. No specific props (only standard HTML attributes via `v-bind="$attrs"`).

### Events

No events.

### Slots

No slots.

### Before (6.6)
```twig
<!-- File: src/module/sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig -->
<div v-else>
    <sw-skeleton-bar style="width: 100%; min-height: 250px;" />
</div>
```

### After (6.7)
```twig
<!-- File: src/module/sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig -->
<div v-else>
    <mt-skeleton-bar style="width: 100%; min-height: 250px;" />
</div>
```

---

## Summary of the migration patterns

### Patterns common to all form fields (6-16)

| Pattern | Old (6.6) | New (6.7) |
|--------|-----------|-----------|
| **v-model binding** | `v-model:value="..."` | `v-model="..."` |
| **Manual binding** | `:value="..."` + `@update:value="..."` | `:model-value="..."` + `@update:model-value="..."` |
| **Component name** | `sw-*-field` | `mt-*` (without `-field` for checkbox, switch, select, textarea) |

### Special cases

| Component | Particularity |
|-----------|-------------|
| **sw-checkbox-field** | `v-model:checked` instead of `v-model` — the only exception |
| **sw-switch-field** | Typo `borderd` → `bordered`; props `size`, `noMarginTop` dropped; slots `label`, `hint` dropped |
| **sw-select-field** | Inline `<option>` slots → `:options` array prop (biggest structural change) |
| **sw-tabs** | `<sw-tabs-item>` children → `:items` array with `onClick` callbacks (most complex migration) |
| **sw-button** | `routerLink` → `@click` + `$router.push()`; the default variant becomes `"secondary"` |
| **sw-alert** | `showIcon` → `hideIcon` (logic inverted); `appearance` is dropped entirely |
| **sw-popover** | Slot rename: `default` → `trigger`, `popover-content` → `default` |
| **sw-colorpicker** | `color-output` is dropped (always hex) |

### Data sources (wrapper files in 6.7)

All wrapper files are located under:
```
vendor/shopware/administration/Resources/app/administration/src/app/component/
├── base/
│   ├── sw-button/index.js + sw-button.html.twig
│   ├── sw-alert/index.ts + sw-alert.html.twig
│   ├── sw-card/index.ts + sw-card.html.twig
│   ├── sw-icon/index.js + sw-icon.html.twig
│   └── sw-tabs/index.ts + sw-tabs.html.twig
├── form/
│   ├── sw-text-field/index.ts + sw-text-field.html.twig
│   ├── sw-number-field/index.ts + sw-number-field.html.twig
│   ├── sw-checkbox-field/index.ts + sw-checkbox-field.html.twig
│   ├── sw-switch-field/index.js + sw-switch-field.html.twig
│   ├── sw-select-field/index.ts + sw-select-field.html.twig
│   ├── sw-password-field/index.ts + sw-password-field.html.twig
│   ├── sw-email-field/index.ts + sw-email-field.html.twig
│   ├── sw-textarea-field/index.ts + sw-textarea-field.html.twig
│   ├── sw-colorpicker/index.ts + sw-colorpicker.html.twig
│   ├── sw-datepicker/index.ts + sw-datepicker.html.twig
│   └── sw-url-field/index.ts + sw-url-field.html.twig
└── utils/
    ├── sw-loader/index.js + sw-loader.html.twig
    ├── sw-popover/index.ts + sw-popover.html.twig
    └── sw-skeleton-bar/index.ts + sw-skeleton-bar.html.twig
```

> **See also:** `references/component-mapping.md` for the quick reference table with all components.
