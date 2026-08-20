# Meteor Component Library — complete component reference

Package: `@shopware-ag/meteor-component-library`  
Source: `packages/component-library/src/components/`

All components start with `mt-*`. Categories mirror the directory structure.

---

## Contents

- [Form components](#form-components)
- [Layout components](#layout-components)
- [Navigation components](#navigation-components)
- [Feedback components](#feedback-components)
- [Overlay components](#overlay-components)
- [Table and list components](#table-and-list-components)
- [Icons & media](#icons--media)
- [Context menu](#context-menu)
- [Action menu (Reka UI based)](#action-menu-reka-ui-based)
- [Content components](#content-components)
- [Charts](#charts)
- [Entity components](#entity-components)
- [Theme](#theme)
- [General notes](#general-notes)

## Form components

### `mt-button`

Primary action button.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `is` | `Component \| string` | `'button'` | Renders as this element |
| `variant` | `'primary'\|'secondary'\|'tertiary'\|'critical'` | `'secondary'` | Variant |
| `ghost` | `boolean` | `false` | Ghost style (transparent) |
| `size` | `'x-small'\|'small'\|'default'\|'large'` | `'small'` | Size |
| `disabled` | `boolean` | `false` | Disabled |
| `square` | `boolean` | `false` | Square |
| `block` | `boolean` | `false` | Full width |
| `isLoading` | `boolean` | `false` | Loading animation |
| `link` | `string` | `undefined` | **@deprecated** — use `is="a" href="..."` |

**Slots:** `default`, `iconFront: { size: number }`, `iconBack: { size: number }`

```html
<mt-button variant="primary" @click="save">Speichern</mt-button>
<mt-button variant="critical" ghost>Löschen</mt-button>
```

---

### `mt-text-field`

Single-line text field.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `string \| number` | `''` | Value (v-model) |
| `label` | `string` | `null` | Label |
| `placeholder` | `string` | `''` | Placeholder text |
| `helpText` | `string` | `null` | Help text |
| `size` | `'small'\|'default'` | `'default'` | Size |
| `disabled` | `boolean` | `false` | Disabled |
| `required` | `boolean` | `false` | Required field |
| `error` | `{ code: number, detail: string }` | `null` | Error object |
| `copyable` | `boolean` | `false` | Copy function |
| `copyableTooltip` | `boolean` | `false` | Tooltip after a successful copy |
| `maxLength` | `number` | — | Maximum number of characters |
| `isInherited` | `boolean` | `false` | Inheritance active |
| `isInheritanceField` | `boolean` | `false` | Has an inheritance toggle |
| `disableInheritanceToggle` | `boolean` | `false` | Disable the inheritance toggle |

**Events:** `update:modelValue`, `change`, `inheritance-restore`, `inheritance-remove`

**Slots:** `prefix`, `suffix`, `hint`

```html
<mt-text-field v-model="product.name" label="Name" :error="errors.name" />
```

---

### `mt-number-field`

Numeric input field.

**Props:** all of `mt-text-field` plus:

| Prop | Type | Default | Description |
|---|---|---|---|
| `numberType` | `'float'\|'int'` | `'float'` | Number type |
| `step` | `number` | `null` | Step size |
| `min` | `number` | `null` | Minimum value |
| `max` | `number` | `null` | Maximum value |
| `fillDigits` | `boolean` | `false` | Pad with zeros |
| `digits` | `number` | `2` | Decimal places (float) |

**Events:** `update:modelValue`, `input-change`, `change`, `inheritance-restore`, `inheritance-remove`

---

### `mt-textarea`

Multi-line text field.

**Props:**

| Prop | Type | Description |
|---|---|---|
| `modelValue` | `string` | Value |
| `label` | `string` | Label |
| `placeholder` | `string` | Placeholder |
| `helpText` | `string` | Help text |
| `error` | `{ detail: string }` | Error |
| `maxLength` | `number` | Maximum characters |
| `disabled` | `boolean` | Disabled |
| `required` | `boolean` | Required field |
| `isInherited` | `boolean` | Inheritance active |
| `isInheritanceField` | `boolean` | Show the inheritance toggle |

**Events:** `update:modelValue`, `change`, `inheritance-restore`, `inheritance-remove`

---

### `mt-email-field`

E-mail input field (based on `mt-text-field`, type=email). Same props/events.

---

### `mt-password-field`

Password input field with a visibility toggle. Same props as `mt-text-field`.

---

### `mt-url-field`

URL input field. Same props as `mt-text-field`.

---

### `mt-checkbox`

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `boolean` | `undefined` | v-model |
| `checked` | `boolean` | `undefined` | Checkbox state (alternative to v-model) |
| `label` | `string` | `undefined` | Label |
| `disabled` | `boolean` | `false` | Disabled |
| `partial` | `boolean` | `false` | Indeterminate |
| `error` | `{ detail: string }` | — | Error |
| `isInherited` | `boolean` | `false` | Inheritance active |
| `isInheritanceField` | `boolean` | `false` | Inheritance toggle |

**Events:** `update:modelValue`, `update:checked`, `change` (**@deprecated**), `inheritance-remove`, `inheritance-restore`

---

### `mt-switch`

Toggle switch.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `boolean` | `undefined` | v-model |
| `label` | `string` | `undefined` | Label |
| `disabled` | `boolean` | `false` | Disabled |
| `required` | `boolean` | `false` | Required field |
| `bordered` | `boolean` | `false` | With a border |
| `helpText` | `string` | — | Help text |
| `error` | `{ detail: string }` | — | Error |
| `checked` | `boolean` | — | Alternative state |
| `isInherited` | `boolean` | `false` | Inheritance |
| `isInheritanceField` | `boolean` | `false` | Inheritance toggle |

**Events:** `change: [boolean]`, `update:modelValue: [boolean]`, `inheritance-remove`, `inheritance-restore`

---

### `mt-select`

Dropdown selection (single or multi).

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `options` | `Array` | required | Options array |
| `modelValue` | `string\|number\|boolean\|Array\|null` | `null` | Value |
| `labelProperty` | `string \| string[]` | `'label'` | Label key in the options object |
| `valueProperty` | `string` | `'value'` | Value key in the options object |
| `enableMultiSelection` | `boolean` | `false` | Multiple selection |
| `label` | `string` | `''` | Field label |
| `placeholder` | `string` | `''` | Placeholder |
| `disabled` | `boolean` | `false` | Disabled |
| `isInherited` | `boolean` | `false` | Inheritance |
| `isInheritanceField` | `boolean` | `false` | Inheritance toggle |
| `error` | Object | — | Error |
| `valueLimit` | `number` | `5` | Displayed selection chips |

**Events:** `update:modelValue`, `change`, `item-add`, `item-remove`, `paginate`, `search-term-change`, `inheritance-restore`, `inheritance-remove`

---

### `mt-datepicker`

Date/time selection.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `string\|string[]\|Date\|Date[]\|null` | — | Value |
| `label` | `string\|null` | — | Label |
| `dateType` | `'date'\|'datetime'\|'time'` | `'date'` | Mode |
| `locale` | `string` | — | Locale (e.g. `'de'`) |
| `format` | `string\|function` | — | Display format |
| `timeZone` | `string` | — | Time zone |
| `disabled` | `boolean` | `false` | Disabled |
| `error` | Object | — | Error |

**Events:** `update:modelValue`, `change`

---

### `mt-colorpicker`

Color selection field.

**Events:** `update:modelValue`, `change`

---

### `mt-slider`

Slider control.

**Events:** `update:modelValue`, `change`

---

### `mt-radio-group`

Radio button group (headless component system).

Sub-components: `mt-radio-group-root`, `mt-radio-group-item`, `mt-radio-group-custom-item`, `mt-radio-group-list`, `mt-radio-group-indicator`

```html
<mt-radio-group-root v-model="value">
  <mt-radio-group-list>
    <mt-radio-group-item value="a">Option A</mt-radio-group-item>
    <mt-radio-group-item value="b">Option B</mt-radio-group-item>
  </mt-radio-group-list>
</mt-radio-group-root>
```

---

### `mt-text-editor`

Rich text editor (WYSIWYG, based on Tiptap).

**Events:** `update:modelValue`, `change`

---

### `mt-unit-field`

Number field with a unit selection. Combines `mt-number-field` + `mt-unit-select`.

---

### `mt-help-text`

Small help text icon with a tooltip.

**Props:** `text: string`

---

## Layout components

### `mt-card`

Primary container with title, subtitle and slots.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `title` | `string` | — | Title |
| `subtitle` | `string` | — | Subtitle |
| `isLoading` | `boolean` | `false` | Loading animation |
| `inheritance` | `boolean` | `undefined` | Inheritance visualization |
| `large` | `boolean` | — | **@deprecated** v4.0.0 |

**Events:** `update:inheritance: [boolean]`

**Slots:** `default`, `title`, `subtitle`, `avatar`, `grid`, `footer`, `toolbar`, `tabs`, `before-card`, `after-card`, `headerRight`, `context-actions`

```html
<mt-card title="Produkt-Infos">
  <template #toolbar>
    <mt-button>Neu</mt-button>
  </template>
  <!-- Content -->
</mt-card>
```

---

### `mt-collapsible`

Collapsible area (headless, based on Reka UI).

Sub-components: `mt-collapsible` (root), `mt-collapsible-trigger`, `mt-collapsible-content`

**mt-collapsible props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | `boolean` | — | Controlled state |
| `defaultOpen` | `boolean` | — | Initial state |
| `disabled` | `boolean` | `false` | Disabled |
| `as` | `string\|object` | `'div'` | Root element |
| `keepMounted` | `boolean` | `true` | Keep the DOM when closed |

```html
<mt-collapsible>
  <mt-collapsible-trigger>Titel</mt-collapsible-trigger>
  <mt-collapsible-content>Inhalt</mt-collapsible-content>
</mt-collapsible>
```

---

### `mt-empty-state`

Empty state display.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `headline` | `string` | required | Headline |
| `description` | `string` | required | Description |
| `icon` | `string` | required | Icon name |
| `linkHref` | `string` | — | Link URL |
| `linkText` | `string` | — | Link text |
| `linkType` | `'external'\|'internal'` | `'internal'` | Link type |
| `buttonText` | `string` | — | Button text |

**Events:** `button-click`

---

### `mt-inset`

Inset container for indented content (internal wrapper).

---

## Navigation components

### `mt-tabs`

Tab navigation.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | `TabItem[]` | required | Tab entries |
| `vertical` | `boolean` | `false` | Vertical alignment |
| `defaultItem` | `string` | `''` | Tab active by default (name) |
| `small` | `boolean` | `false` | **@deprecated** v4.0.0 |

**TabItem interface:**

```ts
{
  label: string;
  name: string;
  hasError?: boolean;
  disabled?: boolean;
  badge?: 'positive' | 'critical' | 'warning' | 'info';
  onClick?: (name: string) => void;
}
```

**Events:** `new-item-active: [name: string]`

---

### `mt-link`

Styled link.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `to` | `string` | — | router-link target |
| `as` | `string` | `'router-link'` | Render element |
| `variant` | `'primary'\|'critical'` | `'primary'` | Variant |
| `disabled` | `boolean` | `false` | Disabled |
| `type` | `'external'\|'internal'` | — | Link type |

**Events:** `click: [MouseEvent]`

---

### `mt-search`

Search field.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `string` | — | Search term |
| `placeholder` | `string` | `'Search'` | Placeholder |
| `size` | `'small'\|'default'` | `'default'` | Size |
| `disabled` | `boolean` | `false` | Disabled |

**Events:** `update:modelValue`, `change: [string]`

---

### `mt-segmented-control`

Segmented selection (similar to radio buttons).

---

## Feedback components

### `mt-banner`

Notice/warning message.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `'neutral'\|'info'\|'attention'\|'critical'\|'positive'\|'inherited'` | `'neutral'` | Variant |
| `title` | `string` | — | Title |
| `hideIcon` | `boolean` | `false` | Hide the icon |
| `closable` | `boolean` | `false` | Closable |
| `bannerIndex` | `string` | — | Unique ID for events |
| `icon` | `string` | — | Custom icon (overrides the variant icon) |

**Events:** `close: [bannerIndex?: string]`

**Slot:** `default`

```html
<mt-banner variant="critical" title="Fehler" closable @close="dismiss">
  Beim Speichern ist ein Fehler aufgetreten.
</mt-banner>
```

---

### `mt-badge`

Small status badge.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `'neutral'\|'info'\|'attention'\|'critical'\|'positive'` | `'neutral'` | Variant |
| `icon` | `string` | — | Icon |
| `size` | `'s'\|'m'\|'l'` | `'s'` | Size |
| `statusIndicator` | `boolean` | `false` | As a dot indicator |

**Slots:** `default`, `icon: { size: number }`

---

### `mt-color-badge`

Colored badge dot (used in tabs as a status indicator).

---

### `mt-loader`

Loading spinner.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `string` | `'50px'` | Size (e.g. `'32px'`) |
| `title` | `string` | — | Accessibility title |
| `description` | `string` | — | Description |
| `backdrop` | `boolean` | `true` | Background overlay |

---

### `mt-progress-bar`

Progress bar.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `label` | `string` | required | Label |
| `maxValue` | `number` | required | Maximum value |
| `modelValue` | `number` | — | Current value (v-model) |
| `error` | `{ detail: string, code: number } \| null` | — | Error |
| `progressLabelType` | `string` | `'percent'` | Label type ('percent' or a unit) |

**Events:** `update:modelValue`

---

### `mt-skeleton-bar`

Loading skeleton placeholder. No props required.

---

### `mt-snackbar`

Snackbar notification.

---

### `mt-toast`

Toast notification (internal component; externally via the Admin SDK `toast.dispatch`).

---

### `mt-promo-badge`

Promo/marketing badge.

---

## Overlay components

### `mt-modal`

Modal dialog (headless component system based on Reka UI).

Sub-components: `mt-modal` (wrapper), `mt-modal-root`, `mt-modal-trigger`, `mt-modal-action`, `mt-modal-close`

**mt-modal props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `title` | `string` | — | Title |
| `subtitle` | `string` | — | Subtitle |
| `width` | `'s'\|'m'\|'l'\|'xl'\|'full'` | `'m'` | Width |
| `inset` | `boolean` | `false` | With inner spacing |
| `hideHeader` | `boolean` | `false` | Hide the header |

**Slots:** `default` (content), `header` (header area)

```html
<mt-modal-root v-model:open="showModal">
  <mt-modal-trigger>
    <mt-button>Öffnen</mt-button>
  </mt-modal-trigger>
  <mt-modal title="Titel">
    Inhalt
    <mt-modal-action>
      <mt-button variant="primary">OK</mt-button>
    </mt-modal-action>
  </mt-modal>
</mt-modal-root>
```

---

### `mt-tooltip`

Tooltip wrapper.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `content` | `string` | required | Tooltip text (HTML is sanitized) |
| `delayDurationInMs` | `number` | `300` | Show delay |
| `hideDelayDurationInMs` | `number` | `300` | Hide delay |
| `placement` | `Placement` (Floating UI) | `'top'` | Position |
| `maxWidth` | `number` | `240` | Max width in px |

**Slot:** `default` — the element that triggers the tooltip (requires `id="mt-tooltip--{id}__trigger"`)

---

### `mt-popover`

Floating overlay card (for dropdown menus etc.).

**Props:**

| Prop | Type | Description |
|---|---|---|
| `title` | `string` | Popover title |
| `childViews` | `View[]` | Sub-views for navigation |

**Slots:** `trigger: { toggleFloatingUi }`, `popover-items__base`, `popover-items__{viewId}`

---

### `mt-popover-item`

Single entry in a popover.

**Props:** `label`, `showOptions`, `showCheckbox`, `checkboxChecked`

**Events:** `click-options`, `change-checkbox`

---

### `mt-popover-item-result`

Search result list in a popover. Contains a search field and an options list.

---

## Table and list components

### `mt-data-table`

Complete data table with pagination, sorting, filtering, column configuration.

**Props:**

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `dataSource` | `Array<{ id: string, [key: string]: any }>` | yes | — | Records |
| `columns` | `ColumnProperty[]` | yes | — | Column definitions |
| `currentPage` | `number` | yes | — | Current page |
| `paginationLimit` | `number` | yes | — | Entries per page |
| `paginationTotalItems` | `number` | yes | — | Total count |
| `columnChanges` | `Record<string, ColumnChanges>` | no | `{}` | Column adjustments |
| `title` | `string` | no | `''` | Title |
| `subtitle` | `string` | no | `''` | Subtitle |
| `layout` | `'default'\|'full'` | no | `'default'` | Layout |
| `sortBy` | `string` | no | `''` | Sort column |
| `sortDirection` | `'ASC'\|'DESC'` | no | `'ASC'` | Sort direction |
| `isLoading` | `boolean` | no | `false` | Loading animation |
| `disableSearch` | `boolean` | no | `false` | Disable search |
| `filters` | `Filter[]` | no | `[]` | Filter definitions |
| `paginationOptions` | `number[]` | no | `[5,10,25,50]` | Pagination options |
| `allowRowSelection` | `boolean` | no | `false` | Row selection |
| `enableReload` | `boolean` | no | `false` | Reload button |
| `disableEdit` | `boolean` | no | `false` | Disable editing |
| `disableDelete` | `boolean` | no | `false` | Disable deletion |

**ColumnProperty:**
```ts
{
  label: string;       // Column heading
  property: string;    // Data key
  renderer: 'text' | 'number' | 'price' | 'badge';
  position: number;    // Sort position
  allowResize?: boolean;
  allowSort?: boolean;
  width?: string;
  visible?: boolean;
}
```

**Events:** `update:currentPage`, `update:sortBy`, `update:sortDirection`, `update:searchValue`, `change-show-outlines`, `change-show-stripes`, `change-outline-framing`, `change-enable-row-numbering`, `select-all`, `deselect-all`, `row-selected`, `reload`

**Slot:** `toolbar` — additional toolbar elements

```html
<mt-data-table
  :data-source="products"
  :columns="columns"
  :current-page="1"
  :pagination-limit="25"
  :pagination-total-items="100"
/>
```

---

### `mt-entity-data-table`

Data table with direct entity repository integration. Wrapper around `mt-data-table`.

---

### `mt-pagination`

Standalone pagination component.

**Props:**

| Prop | Type | Required | Description |
|---|---|---|---|
| `currentPage` | `number` | yes | Current page |
| `limit` | `number` | yes | Entries per page |
| `totalItems` | `number` | yes | Total count |

**Events:** `change-current-page: [number]`

---

## Icons & media

### `mt-icon`

Displays a Meteor icon.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `name` | `string` | required | Icon name (e.g. `'solid-save'`, `'regular-home'`) |
| `size` | `string` | — | Size (e.g. `'16px'`, `'24'`) |
| `color` | `string` | — | CSS color |
| `mode` | `'solid'\|'regular'` | `'regular'` | Style (overridden by the name prefix) |
| `decorative` | `boolean` | `false` | Decorative (no ARIA label) |

```html
<mt-icon name="solid-save" size="24px" />
<mt-icon name="regular-home" color="var(--color-icon-primary-default)" />
```

---

### `mt-avatar`

User avatar with initials or an image.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `'2xs'\|'xs'\|'s'\|'m'\|'l'` | `'m'` | Size |
| `firstName` | `string` | — | First name (for the initials) |
| `lastName` | `string` | — | Last name (for the initials) |
| `imageUrl` | `string` | — | Image URL (overrides the initials) |
| `variant` | `'circle'\|'square'` | `'circle'` | Shape |

---

## Context menu

### `mt-context-button`

Button that opens a context menu (three-dot menu).

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `icon` | `string` | `'solid-ellipsis-h-s'` | Button icon |
| `menuWidth` | `number` | `220` | Menu width in px |
| `menuHorizontalAlign` | `'right'\|'left'` | `'right'` | Horizontal alignment |
| `menuVerticalAlign` | `'bottom'\|'top'` | `'bottom'` | Vertical alignment |
| `disabled` | `boolean` | `false` | Disabled |
| `hasError` | `boolean` | `false` | Error state |
| `autoClose` | `boolean` | `true` | Close automatically |
| `title` | `string` | `''` | Menu title |

**Slots:** `button-text` (button label), `default: { toggleFloatingUi }` (menu content)

---

### `mt-context-menu-item`

Single menu entry in the context menu.

**Props:** `label`, `type: 'default'|'critical'`, `disabled`, `icon`

**Events:** `click`

---

### `mt-context-menu-divider`

Divider line in the context menu.

---

## Action menu (Reka UI based)

### `mt-action-menu`

Dropdown menu, based on the Reka UI DropdownMenu.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `isSubMenu` | `boolean` | `false` | Render as a submenu |
| `matchTriggerWidth` | `boolean` | `false` | Match the width to the trigger |

**Slot:** `default` — contains `mt-action-menu-item` and `mt-action-menu-group`

---

### `mt-action-menu-item`

Menu entry in the action menu.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | `'default'\|'critical'` | `'default'` | Variant |
| `icon` | `string` | — | Icon |
| `disabled` | `boolean` | `false` | Disabled |
| `shortcut` | `ShortcutDefinition` | — | Keyboard shortcut |
| `isSubTrigger` | `boolean` | — | As a submenu trigger |
| `as` | `string` | — | Render element |
| `link` | `string` | — | URL |

---

### `mt-action-menu-group`

Group of menu entries in the action menu.

---

## Content components

### `mt-text`

Text renderer with design system typography.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `'2xs'\|'xs'\|'s'\|'m'\|'l'\|'xl'\|'2xl'\|'3xl'` | — | Font size |
| `weight` | `'bold'\|'semibold'\|'medium'\|'regular'` | — | Font weight |
| `color` | `string` | — | Color (design token name or CSS value) |
| `as` | `string \| Component` | — | Render element |

```html
<mt-text size="l" weight="bold">Überschrift</mt-text>
<mt-text size="s" color="color-text-secondary-default">Hinweistext</mt-text>
```

---

## Charts

### `mt-chart`

ApexCharts wrapper for admin-compatible diagrams.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `series` | `any[]` | required | Data series |
| `options` | `ApexOptions` | `{}` | ApexCharts options |
| `type` | `ApexChart['type']` | `'area'` | Chart type |
| `width` | `string\|number` | `'100%'` | Width |
| `height` | `string\|number` | `'300px'` | Height |

---

## Entity components

### `mt-entity-select`

Entity selection with repository integration.

**Props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `entity` | `keyof EntitySchema.Entities` | required | Entity type |
| `modelValue` | `any` | `null` | Selected value |
| `labelProperty` | `string \| string[]` | `'name'` | Label property of the entity |
| `valueProperty` | `string` | `'id'` | Value property of the entity |
| `disabled` | `boolean` | `false` | Disabled |
| `enableMultiSelection` | `boolean` | `false` | Multiple selection |
| `repository` | `Repository` | — | Custom repository object |

**Events:** `update:modelValue`

---

## Theme

### `mt-theme-provider`

Provides the design system theme. Should be used once in the app root.

**Slot:** `default`

---

## General notes

### v-model binding

- Form fields: `v-model` binds to `modelValue` + `update:modelValue`
- Checkbox: additionally `checked` + `update:checked` available
- Inheritance events: `inheritance-restore` and `inheritance-remove` on fields with `isInheritanceField`

### Design token variables

All components use CSS custom properties:
- `--color-*` — colors (light/dark theme capable)
- `--scale-size-*` — spacing/sizes
- `--border-radius-*` — corner rounding
- `--font-family-*`, `--font-size-*` — typography

Importing the tokens (administration):
```js
import '@shopware-ag/meteor-tokens/deliverables/administration/light.css';
// For dark mode:
import '@shopware-ag/meteor-tokens/deliverables/administration/dark.css';
// Primitive colors:
import '@shopware-ag/meteor-tokens/deliverables/foundation/primitives.css';
```
