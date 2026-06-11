# Detaillierter sw-* → mt-* Component Migration Guide

> Vollständige Migrationsreferenz für alle 19 deprecated `sw-*` Wrapper-Komponenten zu ihren `mt-*` Meteor-Ersetzungen in Shopware 6.7. Alle `sw-*` Wrapper sind als deprecated markiert und werden in v6.8.0 entfernt.

---

## Scope

Dieses Dokument deckt exakt **19 deprecated Wrapper-Komponenten** ab, die in Shopware 6.7 ein `mt-*` Äquivalent haben. Jede Komponente wird mit vollständiger Props/Events/Slots-Tabelle und echten Vorher/Nachher-Beispielen aus `src/module/` dokumentiert.

### Abgedeckte Komponenten

| # | Alt (sw-*) | Neu (mt-*) | Kategorie |
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

### NICHT migriert (kein mt-* Ersatz oder nicht über Wrapper)

| Komponente | Status | Grund |
|-----------|--------|-------|
| `sw-page` | Bleibt `sw-page` | Shopware-spezifisches Layout, kein `mt-page` |
| `sw-card-view` | Bleibt `sw-card-view` | Shopware-spezifisches Layout, kein `mt-card-view` |
| `sw-modal` | Bleibt `sw-modal` | 136 Nutzungen in 6.7, nur 6× `mt-modal` in neuen Modulen |
| `sw-external-link` | Bleibt `sw-external-link` | Kein deprecated Wrapper in 6.7 |
| `sw-data-grid` | Manuell → `mt-data-table` | Komplett andere API, erfordert manuelle Migration |
| `sw-progress-bar` | Direkt `mt-progress-bar` | Kein deprecated Wrapper — direkte Nutzung |

---

## Universelle Migrationsmuster

### v-model Änderung (alle Formularfelder)

| Alt | Neu | Anwendung |
|-----|-----|-----------|
| `v-model:value="x"` | `v-model="x"` | Standard für alle Felder |
| `:value="x"` + `@update:value` | `:modelValue="x"` + `@update:modelValue` | Einweg-Binding |
| `@input` | `@update:modelValue` | Event-Name für Wertänderungen |
| `v-model:value="x"` (Checkbox) | `v-model:checked="x"` | **Nur bei mt-checkbox!** |

### Button Variants

| Alt (sw-button) | Neu (mt-button) |
|----------------|-----------------|
| *(kein variant)* | `variant="secondary"` |
| `variant="primary"` | `variant="primary"` |
| `variant="danger"` | `variant="critical"` |
| `variant="ghost"` | `variant="tertiary"` |
| `variant="ghost-danger"` | `variant="critical" ghost` |
| `variant="contrast"` | `variant="primary"` |
| `variant="context"` | `variant="secondary"` |

### Alert/Banner Variants

| Alt (sw-alert) | Neu (mt-banner) |
|---------------|-----------------|
| `variant="info"` | `variant="info"` |
| `variant="warning"` | `variant="attention"` |
| `variant="error"` | `variant="critical"` |
| `variant="success"` | `variant="positive"` |

### Codemod-Tool

Shopware stellt einen Codemod bereit, der viele dieser Migrationen automatisch durchführt:
```bash
npx @shopware-ag/meteor-admin-sdk-codemod
```

> **Hinweis:** Der Codemod deckt die meisten Prop-Umbenennungen und Komponentennamen ab, aber komplexere Migrationen (Tabs-Items, Select-Options, Router-Link) erfordern manuelle Nacharbeit.

---

## 1. sw-button → mt-button

> Der `sw-button` Wrapper leitet ab v6.7 an die Meteor-Komponente `mt-button` weiter. Die Prop `routerLink` wird im Wrapper via `$router.push()` behandelt und ist in `mt-button` selbst nicht mehr vorhanden. Der Wrapper setzt einen Fallback `variant="secondary"`.

### Props

| Alt (sw-button) | Neu (mt-button) | Änderung |
|-----------|-----------|----------|
| `variant`: `primary`, `ghost`, `danger`, `ghost-danger`, `contrast`, `context` | `variant`: `primary`, `secondary`, `tertiary`, `critical`, `action` | Werte umbenannt: `ghost` → `tertiary`, `danger` → `critical`; Default `""` → `"secondary"` |
| `size`: `x-small`, `small` (Default: `""`) | `size`: `x-small`, `small`, `default`, `large` (Default: `"default"`) | Neue Größen `default` und `large` hinzugefügt |
| `routerLink` (Object) | — entfallen — | Wrapper übernimmt via `$router.push()`; `mt-button` hat kein `routerLink` |
| `isLoading` (Boolean) | `isLoading` (Boolean) | Identisch |
| — | `ghost` (Boolean) | Neu: Separate Boolean-Prop für Ghost-Darstellung |
| — | `is` (Component/String) | Neu: Erlaubt Rendering als anderes Element |

### Events

| Alt (sw-button) | Neu (mt-button) | Änderung |
|-----------|-----------|----------|
| `@click` | `@click` | Identisch |

### Slots

| Alt (sw-button) | Neu (mt-button) | Änderung |
|-----------|-----------|----------|
| `default` | `default` | Identisch |
| — | `iconFront` (scope: `{ size }`) | Neu: Slot für Icon vor dem Text |
| — | `iconBack` (scope: `{ size }`) | Neu: Slot für Icon nach dem Text |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-settings-customer-group/page/sw-settings-customer-group-detail/sw-settings-customer-group-detail.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-settings-customer-group/page/sw-settings-customer-group-detail/sw-settings-customer-group-detail.html.twig -->
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

### Router-Link Migration

`mt-button` unterstützt kein `:router-link` Prop. Buttons mit Router-Navigation erhalten ein `@click` Event mit `$router.push()`:

```html
<!-- Inline (einfache Routen): -->
<mt-button @click="$router.push({ name: 'route.name' })">...</mt-button>

<!-- Als Methode (empfohlen bei Params): -->
<mt-button variant="primary" @click="onNavigate">Edit item</mt-button>
```

---

## 2. sw-alert → mt-banner

> Der Komponentenname ändert sich von "Alert" zu "Banner". Die Varianten-Werte werden umbenannt (`warning` → `attention`, `error` → `critical`, `success` → `positive`). Die `appearance`-Prop entfällt komplett.

### Props

| Alt (sw-alert) | Neu (mt-banner) | Änderung |
|-----------|-----------|----------|
| `variant`: `info`, `warning`, `error`, `success` | `variant`: `info`, `attention`, `critical`, `positive`, `neutral`, `inherited` | Umbenannt: `warning` → `attention`, `error` → `critical`, `success` → `positive`; Neu: `inherited` |
| `appearance`: `default`, `notification`, `system` | — entfallen — | Komplett entfernt in `mt-banner` |
| `showIcon` (Boolean, Default: `true`) | `hideIcon` (Boolean, Default: `false`) | **Logik invertiert**: `showIcon=false` → `hideIcon=true` |
| `notificationIndex` (String) | `bannerIndex` (String) | Umbenannt |
| `closable` (Boolean) | `closable` (Boolean) | Identisch |
| `title` (String) | `title` (String) | Identisch |

### Events

| Alt (sw-alert) | Neu (mt-banner) | Änderung |
|-----------|-----------|----------|
| `@close(notificationIndex)` | `@close(bannerIndex?)` | Parameter umbenannt |

### Slots

| Alt (sw-alert) | Neu (mt-banner) | Änderung |
|-----------|-----------|----------|
| `default` | `default` | Identisch |
| `actions` | — entfallen — | Slot existiert in `mt-banner` nicht mehr |
| — | `customIcon` | Neu: Eigenes Icon |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-view/sw-category-view.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-view/sw-category-view.html.twig -->
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

> Der Wrapper leitet alle Slots dynamisch an `mt-card` weiter. Die Props `hero`, `aiBadge` und `contentPadding` entfallen. Der Slot `header-right` wird zu `headerRight` (camelCase).

### Props

| Alt (sw-card) | Neu (mt-card) | Änderung |
|-----------|-----------|----------|
| `positionIdentifier` (String, required) | — via $attrs — | Nicht mehr als required Prop; wird via `$attrs` durchgereicht |
| `hero` (Boolean) | — entfallen — | Komplett entfernt |
| `aiBadge` (Boolean) | — entfallen — | Komplett entfernt |
| `contentPadding` (Boolean) | — entfallen — | Komplett entfernt |
| `title` (String) | `title` (String) | Identisch |
| `subtitle` (String) | `subtitle` (String) | Identisch |
| `isLoading` (Boolean) | `isLoading` (Boolean) | Identisch |
| `large` (Boolean) | `large` (Boolean) | Identisch |
| — | `inheritance` (Boolean) | Neu: Inheritance-Modus mit `v-model:inheritance` |

### Events

| Alt (sw-card) | Neu (mt-card) | Änderung |
|-----------|-----------|----------|
| — | `@update:inheritance(value)` | Neu: Event für Inheritance-Toggle |

### Slots

| Alt (sw-card) | Neu (mt-card) | Änderung |
|-----------|-----------|----------|
| `default` | `default` | Identisch |
| `title` | `title` | Identisch |
| `subtitle` | `subtitle` | Identisch |
| `avatar` | `avatar` | Identisch |
| `footer` | `footer` | Identisch |
| `toolbar` | `toolbar` | Identisch |
| `tabs` | `tabs` | Identisch |
| `header-right` | `headerRight` | **Umbenannt**: kebab-case → camelCase |
| `context-actions` | `context-actions` | Identisch |
| `grid` | `grid` | Identisch |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-settings-delivery-times/page/sw-settings-delivery-time-list/sw-settings-delivery-time-list.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-settings-delivery-times/page/sw-settings-delivery-time-list/sw-settings-delivery-time-list.html.twig -->
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

> Die Boolean-Props `small` und `large` entfallen zugunsten eines expliziten `size`-Strings. Der Default-Size ist `"24px"`. Der neue `mode` Prop erlaubt die Unterscheidung zwischen `solid` und `regular` Icons.

### Props

| Alt (sw-icon) | Neu (mt-icon) | Änderung |
|-----------|-----------|----------|
| `small` (Boolean) | — entfallen — | Ersetzt durch `size="16px"` |
| `large` (Boolean) | — entfallen — | Ersetzt durch `size="32px"` |
| `size` (String) | `size` (String, Default: `"24px"`) | Default nun explizit `"24px"` |
| `name` (String, required) | `name` (String, required) | Identisch |
| `color` (String) | `color` (String) | Identisch |
| `decorative` (Boolean) | `decorative` (Boolean) | Identisch |
| — | `mode`: `solid`, `regular` | Neu: Explizite Wahl zwischen Solid- und Regular-Icons |

### Events

Keine relevanten Event-Änderungen.

### Slots

| Alt (sw-icon) | Neu (mt-icon) | Änderung |
|-----------|-----------|----------|
| `default` | — entfallen — | `mt-icon` hat keinen Default-Slot |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig -->
<sw-icon
    small
    name="regular-files"
    class="sw-media-sidebar__quickactions-icon"
/>
```

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig -->
<mt-icon
    size="16px"
    name="regular-files"
    class="sw-media-sidebar__quickactions-icon"
/>
```

---

## 5. sw-tabs → mt-tabs

> Die grundlegendste Änderung: `mt-tabs` verwendet eine deklarative `:items`-Array-Prop anstelle von `sw-tabs-item`-Kindkomponenten in Slots. Route-Navigation wird per `onClick`-Callback im Item-Objekt definiert. In 6.7 konvertiert der Wrapper automatisch die alten `sw-tabs-item`-Kinder; ab v6.8.0 muss `mt-tabs` direkt mit `:items` verwendet werden.

### Props

| Alt (sw-tabs) | Neu (mt-tabs) | Änderung |
|-----------|-----------|----------|
| Kindkomponenten `<sw-tabs-item>` im Default-Slot | `:items` (Array von `TabItem[]`) | **Komplett neues Modell**: Deklaratives Array statt Slot-Kinder |
| `isVertical` (Boolean) | `vertical` (Boolean) | Umbenannt |
| `small` (Boolean) | `small` (Boolean) | Deprecated in Meteor v4 |
| `alignRight` (Boolean) | — entfallen — | Komplett entfernt |
| `defaultItem` (String) | `defaultItem` (String) | Identisch |

**TabItem-Interface (neu):**
```typescript
interface TabItem {
    label: string;      // Anzeigetext (früher: Slot-Content von sw-tabs-item)
    name: string;       // Identifier (früher: name-Prop auf sw-tabs-item)
    hasError?: boolean;
    disabled?: boolean;
    badge?: "positive" | "critical" | "warning" | "info";
    onClick?: (name: string) => void;  // Früher: route-Prop auf sw-tabs-item
    hidden?: boolean;
}
```

### Events

| Alt (sw-tabs) | Neu (mt-tabs) | Änderung |
|-----------|-----------|----------|
| `@new-item-active(item)` | `@new-item-active(item)` | Identisch |

### Slots

| Alt (sw-tabs) | Neu (mt-tabs) | Änderung |
|-----------|-----------|----------|
| `default` (scope: `{ active }`) — enthält `sw-tabs-item`-Kinder | — entfallen — | Ersetzt durch `:items`-Prop |
| `content` (scope: `{ active }`) | `content` (scope: `{ active }`) | Inhalt-Slot bleibt (im Wrapper) |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-view/sw-category-view.html.twig -->
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

### Nachher (6.7 — Zielformat mit mt-tabs)
```twig
<!-- Zielformat für direkte mt-tabs Nutzung (ab v6.8 erforderlich) -->
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

> **Hinweis:** In 6.7 wird `sw-tabs` in den Modulen noch verwendet — der Wrapper konvertiert automatisch die `sw-tabs-item`-Kinder in das `items`-Array (siehe `itemsBackwardCompatible` Computed Property). Ab v6.8.0 wird der Wrapper entfernt.

---

## 6. sw-text-field → mt-text-field

> Einfaches Texteingabefeld. Der Wrapper konvertiert `value`/`update:value` auf das Vue-3-Standard `modelValue`/`update:modelValue`.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |
| `copyable` | — entfallen — | Entfernt in mt-text-field |
| `copyableTooltip` | — entfallen — | Entfernt in mt-text-field |
| `idSuffix` | — entfallen — | Entfernt in mt-text-field |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt (Vue-3-Standard) |
| `@inheritance-restore` | — entfallen — | Entfernt |
| `@inheritance-remove` | — entfallen — | Entfernt |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `label` | `label` | Identisch |
| `hint` | `hint` | Identisch |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-newsletter-recipient/page/sw-newsletter-recipient-detail/sw-newsletter-recipient-detail.html.twig -->
{% block sw_newsletter_recipient_detail_form_title %}
<sw-text-field
    v-model:value="newsletterRecipient.title"
    :label="$tc('sw-newsletter-recipient.list.title')"
    :disabled="!acl.can('newsletter_recipient.editor')"
/>
{% endblock %}
```

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-newsletter-recipient/page/sw-newsletter-recipient-detail/sw-newsletter-recipient-detail.html.twig -->
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

> Numerisches Eingabefeld mit Unterstützung für Integer/Float, Min/Max/Step. Der Wrapper konvertiert `value` auf `v-model` und emittiert zusätzlich `change` für Rückwärtskompatibilität.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |
| `digits` | — entfallen — | Entfernt in mt-number-field |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt (Vue-3-Standard) |
| `@input-change` | — entfallen — | Entfernt |
| `@change` | `@change` | Identisch (Wrapper emittiert weiterhin für Kompatibilität) |
| `@inheritance-restore` | — entfallen — | Entfernt |
| `@inheritance-remove` | — entfallen — | Entfernt |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `label` | `label` | Identisch |
| `hint` | `hint` | Identisch |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig -->
<sw-number-field
    v-model:value="promotion.priority"
    :disabled="!acl.can('promotion.editor')"
    :label="$tc('sw-promotion-v2.detail.base.general.priorityLabel')"
    :help-text="$tc('sw-promotion-v2.detail.base.general.helpTextPriority')"
/>
```

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig -->
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

> Checkbox-Feld für boolesche Werte. **Wichtigste Änderung**: Das Binding wechselt von `value` auf `checked` — sowohl beim Prop als auch beim Event. Dies ist die einzige Komponente, die `v-model:checked` statt `v-model` verwendet.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` (Boolean) | `checked` (Boolean) | **Umbenannt**: `v-model:value` wird zu `v-model:checked` |
| `ghostValue` | — entfallen — | Entfernt |
| `inheritedValue` | — entfallen — | Entfernt |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:checked` | **Umbenannt**: Wrapper konvertiert `update:checked` auf `update:value` |
| `@inheritance-restore` | — entfallen — | Entfernt |
| `@inheritance-remove` | — entfallen — | Entfernt |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `label` | `label` | Identisch |
| `hint` | `hint` | Identisch |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig -->
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

> Toggle/Switch für boolesche Werte. Der Tippfehler `borderd` wird zu `bordered` korrigiert. Props `size` und `noMarginTop` entfallen.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` (Boolean) | `modelValue` (Boolean) | Umbenannt: `v-model:value` wird zu `v-model` |
| `checked` (Boolean) | `modelValue` (Boolean) | Zusammengeführt: Wrapper akzeptiert beides |
| `borderd` | `bordered` | **Tippfehler korrigiert** |
| `size` | — entfallen — | Entfernt (`small`, `medium`, `default`) |
| `noMarginTop` | — entfallen — | Entfernt |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt |
| `@inheritance-restore` | — entfallen — | Entfernt |
| `@inheritance-remove` | — entfallen — | Entfernt |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `label` | — entfallen — | Label wird nur als Prop übergeben |
| `hint` | — entfallen — | `mt-switch` hat keine Slot-Unterstützung |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig -->
{% block sw_category_detail_information_visible %}
<sw-switch-field
    v-model:value="reversedVisibility"
    borderd
    :disabled="!acl.can('category.editor')"
    :label="$tc('sw-category.base.menu.visible')"
/>
{% endblock %}
```

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig -->
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

> Native Select-Dropdown. **Gravierendste Änderung**: `<option>`-Slots im Template entfallen komplett und werden durch ein `:options`-Array-Prop ersetzt. Die Optionen müssen in ein JavaScript-Array im Component verschoben werden.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |
| `options` (optional, Array) | `options` (erforderlich, Array) | Nun **die einzige Möglichkeit** Optionen zu definieren (Slots entfallen) |
| `aside` | — entfallen — | Entfernt |
| `placeholder` | `placeholder` | Identisch |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt (Vue-3-Standard) |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| default (`<option>` Elemente) | — entfallen — | **Entfernt**: Optionen müssen als `:options`-Array übergeben werden |
| `label` | — entfallen — | Entfernt als Slot |
| `hint` | — entfallen — | Entfernt als Slot |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig -->
{% block sw_cms_block_config_background_image_position_field %}
<mt-select
    v-model="block.backgroundMediaMode"
    :label="$tc('sw-cms.detail.label.backgroundMediaMode')"
    :disabled="!block.backgroundMediaId"
    :options="backgroundModeOptions"
/>
{% endblock %}
```

**Optionen in den Component verschieben:**
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

> Passwort-Eingabefeld mit Sichtbarkeits-Toggle. Strukturell sehr ähnlich zu `sw-text-field`.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |
| `placeholder` | `placeholder` | Identisch (explizit durchgereicht) |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt; Wrapper emittiert beides für Kompatibilität |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `label` | `label` | Identisch |
| `hint` | `hint` | Identisch |

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-login/view/sw-login-login/sw-login-login.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-login/view/sw-login-login/sw-login-login.html.twig -->
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

> E-Mail-Eingabefeld mit eingebauter Validierung. Folgt dem Standard-v-model-Migrationsmuster.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt (Vue-3-Standard) |

### Slots

Keine Änderungen. Slots (`default`, `prefix`) werden 1:1 durchgereicht.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-customer/component/sw-customer-card/sw-customer-card.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-customer/component/sw-customer-card/sw-customer-card.html.twig -->
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

> Mehrzeiliges Texteingabefeld. **Achtung**: Der Komponentenname ändert sich von `sw-textarea-field` zu `mt-textarea` (nicht `mt-textarea-field`).

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt (Vue-3-Standard) |

### Slots

Keine Änderungen. Slots (`default`, `hint`) werden durchgereicht.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-seo-form/sw-category-seo-form.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-category/component/sw-category-seo-form/sw-category-seo-form.html.twig -->
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

> Farbauswahl-Komponente. Die `color-output`-Prop entfällt (war `auto`, `hex`, `hsl`, `rgb`). `mt-colorpicker` gibt immer Hex aus.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |
| `color-output` | — entfallen — | Entfernt; `mt-colorpicker` gibt immer Hex aus |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt |
| `@change` | `@update:modelValue` | `@change` wird im Wrapper auf `@update:modelValue` gemappt |

### Slots

Keine Änderungen. Default-Slot wird durchgereicht.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig -->
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

> Datumsauswahl-Komponente mit Kalender und verschiedenen Datumsformaten. Folgt dem Standard-v-model-Migrationsmuster.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt |

### Slots

Keine Änderungen.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-customer/component/sw-customer-base-form/sw-customer-base-form.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-customer/component/sw-customer-base-form/sw-customer-base-form.html.twig -->
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

> URL-Eingabefeld mit Protokoll-Prefix-Anzeige (SSL-Toggle). Folgt dem Standard-v-model-Migrationsmuster.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `value` | `modelValue` | Umbenannt: `v-model:value` wird zu `v-model` |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@update:value` | `@update:modelValue` | Umbenannt |

### Slots

Keine Änderungen.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig -->
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

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig -->
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

> Lade-Spinner für asynchrone Operationen. Einfache 1:1-Ersetzung ohne Prop-Änderungen.

### Props

Keine Änderungen. Der `size`-Prop bleibt identisch (Format: `"${number}px"`, Default: `"50px"`).

### Events

Keine Events.

### Slots

Keine Slots.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-login/page/index/sw-login.html.twig -->
{% block sw_login_loader %}
<sw-loader v-if="isLoading" />
{% endblock %}
```

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-login/page/index/sw-login.html.twig -->
{% block sw_login_loader %}
<mt-loader v-if="isLoading" />
{% endblock %}
```

---

## 18. sw-popover → mt-floating-ui

> Tiefgreifende Änderung: `sw-popover` hatte eigene Positionierungslogik. `mt-floating-ui` nutzt `@floating-ui/dom`. Der Wrapper mappt `resizeWidth` auf `matchReferenceWidth` und die Slot-Struktur ändert sich grundlegend.

### Props

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `resizeWidth` | `matchReferenceWidth` | **Umbenannt** |
| `popoverClass` | — entfallen — | Entfernt; CSS direkt verwenden |
| `popoverConfigExtension` | `floatingUiOptions` | Ersetzt durch `@floating-ui/dom` Config |
| `isOpened` | `isOpened` | Identisch |
| — | `showArrow` (Boolean) | Neu: Pfeil-Anzeige |
| — | `offset` (Number) | Neu: Abstand zum Trigger (Default: 6) |

### Events

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `@close-popover` | `@close` | Umbenannt |

### Slots

| Alt (sw-*) | Neu (mt-*) | Änderung |
|-----------|-----------|----------|
| `default` (Trigger-Element) | `trigger` | **Umbenannt**: Trigger-Content in neuen `trigger`-Slot |
| `popover-content` | `default` (scope: `{ referenceElementWidth, referenceElementHeight }`) | **Umbenannt**: Popover-Inhalt wird zum Default-Slot |

### Vorher (6.6)
```twig
<!-- Konzeptbeispiel für sw-popover -->
<sw-popover :isOpened="showPopover" @close-popover="showPopover = false">
    <template #default>
        <sw-button @click="showPopover = !showPopover">Toggle</sw-button>
    </template>
    <template #popover-content>
        <div>Popover content here</div>
    </template>
</sw-popover>
```

### Nachher (6.7)
```twig
<!-- Direktes mt-floating-ui Format -->
<mt-floating-ui :isOpened="showPopover" @close="showPopover = false">
    <template #trigger>
        <mt-button @click="showPopover = !showPopover">Toggle</mt-button>
    </template>
    <template #default>
        <div>Popover content here</div>
    </template>
</mt-floating-ui>
```

> **Hinweis:** In 6.7 wird `sw-popover` in Modulen weiterhin als Wrapper-Name verwendet. Der Wrapper delegiert intern an `mt-floating-ui`. Ab v6.8.0 muss `mt-floating-ui` direkt verwendet werden.

---

## 19. sw-skeleton-bar → mt-skeleton-bar

> Skeleton-Loading-Platzhalter. Einfache 1:1-Ersetzung ohne Prop-, Event- oder Slot-Änderungen.

### Props

Keine Änderungen. Keine spezifischen Props (nur Standard-HTML-Attribute via `v-bind="$attrs"`).

### Events

Keine Events.

### Slots

Keine Slots.

### Vorher (6.6)
```twig
<!-- Datei: src/module/sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig -->
<div v-else>
    <sw-skeleton-bar style="width: 100%; min-height: 250px;" />
</div>
```

### Nachher (6.7)
```twig
<!-- Datei: src/module/sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig -->
<div v-else>
    <mt-skeleton-bar style="width: 100%; min-height: 250px;" />
</div>
```

---

## Zusammenfassung der Migrationsmuster

### Gemeinsame Muster aller Formularfelder (6-16)

| Muster | Alt (6.6) | Neu (6.7) |
|--------|-----------|-----------|
| **v-model Binding** | `v-model:value="..."` | `v-model="..."` |
| **Manuelles Binding** | `:value="..."` + `@update:value="..."` | `:model-value="..."` + `@update:model-value="..."` |
| **Komponentenname** | `sw-*-field` | `mt-*` (ohne `-field` bei checkbox, switch, select, textarea) |

### Sonderfälle

| Komponente | Besonderheit |
|-----------|-------------|
| **sw-checkbox-field** | `v-model:checked` statt `v-model` — einzige Ausnahme |
| **sw-switch-field** | Tippfehler `borderd` → `bordered`; Props `size`, `noMarginTop` entfallen; Slots `label`, `hint` entfallen |
| **sw-select-field** | Inline `<option>`-Slots → `:options`-Array-Prop (größte strukturelle Änderung) |
| **sw-tabs** | `<sw-tabs-item>`-Kinder → `:items`-Array mit `onClick`-Callbacks (komplexeste Migration) |
| **sw-button** | `routerLink` → `@click` + `$router.push()`; Default-Variant wird `"secondary"` |
| **sw-alert** | `showIcon` → `hideIcon` (Logik invertiert); `appearance` entfällt komplett |
| **sw-popover** | Slot-Umbenennung: `default` → `trigger`, `popover-content` → `default` |
| **sw-colorpicker** | `color-output` entfällt (immer Hex) |

### Datenquellen (Wrapper-Dateien in 6.7)

Alle Wrapper-Dateien befinden sich unter:
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

> **Siehe auch:** `references/component-mapping.md` für die Quick-Reference-Tabelle mit allen Komponenten.
