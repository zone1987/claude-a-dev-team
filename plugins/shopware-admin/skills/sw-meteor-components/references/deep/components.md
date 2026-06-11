# Meteor Component Library — Vollständige Komponenten-Referenz

Paket: `@shopware-ag/meteor-component-library`  
Quelle: `packages/component-library/src/components/`

Alle Komponenten beginnen mit `mt-*`. Kategorien entsprechen der Verzeichnisstruktur.

---

## Form-Komponenten

### `mt-button`

Primärer Aktionsbutton.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `is` | `Component \| string` | `'button'` | Rendert als dieses Element |
| `variant` | `'primary'\|'secondary'\|'tertiary'\|'critical'` | `'secondary'` | Variante |
| `ghost` | `boolean` | `false` | Ghost-Stil (transparent) |
| `size` | `'x-small'\|'small'\|'default'\|'large'` | `'small'` | Größe |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `square` | `boolean` | `false` | Quadratisch |
| `block` | `boolean` | `false` | Volle Breite |
| `isLoading` | `boolean` | `false` | Ladeanimation |
| `link` | `string` | `undefined` | **@deprecated** — nutze `is="a" href="..."` |

**Slots:** `default`, `iconFront: { size: number }`, `iconBack: { size: number }`

```html
<mt-button variant="primary" @click="save">Speichern</mt-button>
<mt-button variant="critical" ghost>Löschen</mt-button>
```

---

### `mt-text-field`

Einzeiliges Textfeld.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `modelValue` | `string \| number` | `''` | Wert (v-model) |
| `label` | `string` | `null` | Beschriftung |
| `placeholder` | `string` | `''` | Platzhaltertext |
| `helpText` | `string` | `null` | Hilfstext |
| `size` | `'small'\|'default'` | `'default'` | Größe |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `required` | `boolean` | `false` | Pflichtfeld |
| `error` | `{ code: number, detail: string }` | `null` | Fehlerobjekt |
| `copyable` | `boolean` | `false` | Kopierfunktion |
| `copyableTooltip` | `boolean` | `false` | Tooltip nach erfolgreichem Kopieren |
| `maxLength` | `number` | — | Maximale Zeichenanzahl |
| `isInherited` | `boolean` | `false` | Vererbung aktiv |
| `isInheritanceField` | `boolean` | `false` | Hat Vererbungs-Toggle |
| `disableInheritanceToggle` | `boolean` | `false` | Vererbungs-Toggle deaktivieren |

**Events:** `update:modelValue`, `change`, `inheritance-restore`, `inheritance-remove`

**Slots:** `prefix`, `suffix`, `hint`

```html
<mt-text-field v-model="product.name" label="Name" :error="errors.name" />
```

---

### `mt-number-field`

Zahleneingabefeld.

**Props:** Alle von `mt-text-field` plus:

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `numberType` | `'float'\|'int'` | `'float'` | Zahlentyp |
| `step` | `number` | `null` | Schrittweite |
| `min` | `number` | `null` | Minimalwert |
| `max` | `number` | `null` | Maximalwert |
| `fillDigits` | `boolean` | `false` | Nullstellen auffüllen |
| `digits` | `number` | `2` | Nachkommastellen (float) |

**Events:** `update:modelValue`, `input-change`, `change`, `inheritance-restore`, `inheritance-remove`

---

### `mt-textarea`

Mehrzeiliges Textfeld.

**Props:**

| Prop | Typ | Beschreibung |
|---|---|---|
| `modelValue` | `string` | Wert |
| `label` | `string` | Beschriftung |
| `placeholder` | `string` | Platzhalter |
| `helpText` | `string` | Hilfstext |
| `error` | `{ detail: string }` | Fehler |
| `maxLength` | `number` | Maximale Zeichen |
| `disabled` | `boolean` | Deaktiviert |
| `required` | `boolean` | Pflichtfeld |
| `isInherited` | `boolean` | Vererbung aktiv |
| `isInheritanceField` | `boolean` | Vererbungs-Toggle anzeigen |

**Events:** `update:modelValue`, `change`, `inheritance-restore`, `inheritance-remove`

---

### `mt-email-field`

E-Mail-Eingabefeld (basiert auf `mt-text-field`, type=email). Gleiche Props/Events.

---

### `mt-password-field`

Passwort-Eingabefeld mit Sichtbarkeits-Toggle. Gleiche Props wie `mt-text-field`.

---

### `mt-url-field`

URL-Eingabefeld. Gleiche Props wie `mt-text-field`.

---

### `mt-checkbox`

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `modelValue` | `boolean` | `undefined` | v-model |
| `checked` | `boolean` | `undefined` | Checkbox-Zustand (alternativ zu v-model) |
| `label` | `string` | `undefined` | Beschriftung |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `partial` | `boolean` | `false` | Unbestimmt (indeterminate) |
| `error` | `{ detail: string }` | — | Fehler |
| `isInherited` | `boolean` | `false` | Vererbung aktiv |
| `isInheritanceField` | `boolean` | `false` | Vererbungs-Toggle |

**Events:** `update:modelValue`, `update:checked`, `change` (**@deprecated**), `inheritance-remove`, `inheritance-restore`

---

### `mt-switch`

Toggle-Switch.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `modelValue` | `boolean` | `undefined` | v-model |
| `label` | `string` | `undefined` | Beschriftung |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `required` | `boolean` | `false` | Pflichtfeld |
| `bordered` | `boolean` | `false` | Mit Rahmen |
| `helpText` | `string` | — | Hilfstext |
| `error` | `{ detail: string }` | — | Fehler |
| `checked` | `boolean` | — | Alternativer Zustand |
| `isInherited` | `boolean` | `false` | Vererbung |
| `isInheritanceField` | `boolean` | `false` | Vererbungs-Toggle |

**Events:** `change: [boolean]`, `update:modelValue: [boolean]`, `inheritance-remove`, `inheritance-restore`

---

### `mt-select`

Dropdown-Auswahl (single oder multi).

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `options` | `Array` | required | Optionen-Array |
| `modelValue` | `string\|number\|boolean\|Array\|null` | `null` | Wert |
| `labelProperty` | `string \| string[]` | `'label'` | Label-Key im Options-Objekt |
| `valueProperty` | `string` | `'value'` | Wert-Key im Options-Objekt |
| `enableMultiSelection` | `boolean` | `false` | Mehrfachauswahl |
| `label` | `string` | `''` | Feld-Beschriftung |
| `placeholder` | `string` | `''` | Platzhalter |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `isInherited` | `boolean` | `false` | Vererbung |
| `isInheritanceField` | `boolean` | `false` | Vererbungs-Toggle |
| `error` | Object | — | Fehler |
| `valueLimit` | `number` | `5` | Angezeigte Auswahl-Chips |

**Events:** `update:modelValue`, `change`, `item-add`, `item-remove`, `paginate`, `search-term-change`, `inheritance-restore`, `inheritance-remove`

---

### `mt-datepicker`

Datums-/Zeitauswahl.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `modelValue` | `string\|string[]\|Date\|Date[]\|null` | — | Wert |
| `label` | `string\|null` | — | Beschriftung |
| `dateType` | `'date'\|'datetime'\|'time'` | `'date'` | Modus |
| `locale` | `string` | — | Locale (z.B. `'de'`) |
| `format` | `string\|function` | — | Anzeigeformat |
| `timeZone` | `string` | — | Zeitzone |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `error` | Object | — | Fehler |

**Events:** `update:modelValue`, `change`

---

### `mt-colorpicker`

Farbauswahl-Feld.

**Events:** `update:modelValue`, `change`

---

### `mt-slider`

Schieberegler.

**Events:** `update:modelValue`, `change`

---

### `mt-radio-group`

Radio-Button-Gruppe (Headless-Komponenten-System).

Unterkomponenten: `mt-radio-group-root`, `mt-radio-group-item`, `mt-radio-group-custom-item`, `mt-radio-group-list`, `mt-radio-group-indicator`

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

Rich-Text-Editor (WYSIWYG, basiert auf Tiptap).

**Events:** `update:modelValue`, `change`

---

### `mt-unit-field`

Zahlenfeld mit Einheitenauswahl. Kombiniert `mt-number-field` + `mt-unit-select`.

---

### `mt-help-text`

Kleines Hilfstext-Icon mit Tooltip.

**Props:** `text: string`

---

## Layout-Komponenten

### `mt-card`

Primärer Container mit Titel, Untertitel und Slots.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `title` | `string` | — | Titel |
| `subtitle` | `string` | — | Untertitel |
| `isLoading` | `boolean` | `false` | Ladeanimation |
| `inheritance` | `boolean` | `undefined` | Vererbungs-Visualisierung |
| `large` | `boolean` | — | **@deprecated** v4.0.0 |

**Events:** `update:inheritance: [boolean]`

**Slots:** `default`, `title`, `subtitle`, `avatar`, `grid`, `footer`, `toolbar`, `tabs`, `before-card`, `after-card`, `headerRight`, `context-actions`

```html
<mt-card title="Produkt-Infos">
  <template #toolbar>
    <mt-button>Neu</mt-button>
  </template>
  <!-- Inhalt -->
</mt-card>
```

---

### `mt-collapsible`

Aufklappbarer Bereich (Headless, basiert auf Reka UI).

Unterkomponenten: `mt-collapsible` (Root), `mt-collapsible-trigger`, `mt-collapsible-content`

**mt-collapsible Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `open` | `boolean` | — | Kontrollierter Zustand |
| `defaultOpen` | `boolean` | — | Initialer Zustand |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `as` | `string\|object` | `'div'` | Root-Element |
| `keepMounted` | `boolean` | `true` | DOM erhalten wenn geschlossen |

```html
<mt-collapsible>
  <mt-collapsible-trigger>Titel</mt-collapsible-trigger>
  <mt-collapsible-content>Inhalt</mt-collapsible-content>
</mt-collapsible>
```

---

### `mt-empty-state`

Leer-Zustand-Anzeige.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `headline` | `string` | required | Überschrift |
| `description` | `string` | required | Beschreibung |
| `icon` | `string` | required | Icon-Name |
| `linkHref` | `string` | — | Link-URL |
| `linkText` | `string` | — | Link-Text |
| `linkType` | `'external'\|'internal'` | `'internal'` | Link-Typ |
| `buttonText` | `string` | — | Button-Text |

**Events:** `button-click`

---

### `mt-inset`

Inset-Container für eingerückten Inhalt (interner Wrapper).

---

## Navigation-Komponenten

### `mt-tabs`

Tab-Navigation.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `items` | `TabItem[]` | required | Tab-Einträge |
| `vertical` | `boolean` | `false` | Vertikale Ausrichtung |
| `defaultItem` | `string` | `''` | Standardmäßig aktiver Tab (name) |
| `small` | `boolean` | `false` | **@deprecated** v4.0.0 |

**TabItem-Interface:**

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

Styled Link.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `to` | `string` | — | router-link Ziel |
| `as` | `string` | `'router-link'` | Render-Element |
| `variant` | `'primary'\|'critical'` | `'primary'` | Variante |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `type` | `'external'\|'internal'` | — | Link-Typ |

**Events:** `click: [MouseEvent]`

---

### `mt-search`

Suchfeld.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `modelValue` | `string` | — | Suchbegriff |
| `placeholder` | `string` | `'Search'` | Platzhalter |
| `size` | `'small'\|'default'` | `'default'` | Größe |
| `disabled` | `boolean` | `false` | Deaktiviert |

**Events:** `update:modelValue`, `change: [string]`

---

### `mt-segmented-control`

Segmentierte Auswahl (ähnlich Radio-Buttons).

---

## Feedback-Komponenten

### `mt-banner`

Hinweis-/Warnmeldung.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | `'neutral'\|'info'\|'attention'\|'critical'\|'positive'\|'inherited'` | `'neutral'` | Variante |
| `title` | `string` | — | Titel |
| `hideIcon` | `boolean` | `false` | Icon ausblenden |
| `closable` | `boolean` | `false` | Schließbar |
| `bannerIndex` | `string` | — | Eindeutige ID für Events |
| `icon` | `string` | — | Eigenes Icon (überschreibt Variant-Icon) |

**Events:** `close: [bannerIndex?: string]`

**Slot:** `default`

```html
<mt-banner variant="critical" title="Fehler" closable @close="dismiss">
  Beim Speichern ist ein Fehler aufgetreten.
</mt-banner>
```

---

### `mt-badge`

Kleines Status-Badge.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | `'neutral'\|'info'\|'attention'\|'critical'\|'positive'` | `'neutral'` | Variante |
| `icon` | `string` | — | Icon |
| `size` | `'s'\|'m'\|'l'` | `'s'` | Größe |
| `statusIndicator` | `boolean` | `false` | Als Punkt-Indikator |

**Slots:** `default`, `icon: { size: number }`

---

### `mt-color-badge`

Farbiger Badge-Punkt (wird in Tabs als Status-Indikator genutzt).

---

### `mt-loader`

Lade-Spinner.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `size` | `string` | `'50px'` | Größe (z.B. `'32px'`) |
| `title` | `string` | — | Barrierefreiheit-Titel |
| `description` | `string` | — | Beschreibung |
| `backdrop` | `boolean` | `true` | Hintergrund-Overlay |

---

### `mt-progress-bar`

Fortschrittsbalken.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `label` | `string` | required | Beschriftung |
| `maxValue` | `number` | required | Maximalwert |
| `modelValue` | `number` | — | Aktueller Wert (v-model) |
| `error` | `{ detail: string, code: number } \| null` | — | Fehler |
| `progressLabelType` | `string` | `'percent'` | Label-Typ ('percent' oder Einheit) |

**Events:** `update:modelValue`

---

### `mt-skeleton-bar`

Lade-Skeleton-Platzhalter. Keine Props erforderlich.

---

### `mt-snackbar`

Snackbar-Benachrichtigung.

---

### `mt-toast`

Toast-Benachrichtigung (interne Komponente; extern via Admin-SDK `toast.dispatch`).

---

### `mt-promo-badge`

Promo/Marketing-Badge.

---

## Overlay-Komponenten

### `mt-modal`

Modal-Dialog (Headless-Komponenten-System basierend auf Reka UI).

Unterkomponenten: `mt-modal` (Wrapper), `mt-modal-root`, `mt-modal-trigger`, `mt-modal-action`, `mt-modal-close`

**mt-modal Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `title` | `string` | — | Titel |
| `subtitle` | `string` | — | Untertitel |
| `width` | `'s'\|'m'\|'l'\|'xl'\|'full'` | `'m'` | Breite |
| `inset` | `boolean` | `false` | Mit Innenabstand |
| `hideHeader` | `boolean` | `false` | Header ausblenden |

**Slots:** `default` (Inhalt), `header` (Kopfbereich)

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

Tooltip-Wrapper.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `content` | `string` | required | Tooltip-Text (HTML wird sanitiert) |
| `delayDurationInMs` | `number` | `300` | Einblende-Verzögerung |
| `hideDelayDurationInMs` | `number` | `300` | Ausblende-Verzögerung |
| `placement` | `Placement` (Floating UI) | `'top'` | Position |
| `maxWidth` | `number` | `240` | Max-Breite in px |

**Slot:** `default` — das Element, das den Tooltip auslöst (benötigt `id="mt-tooltip--{id}__trigger"`)

---

### `mt-popover`

Schwebende Overlay-Karte (für Dropdown-Menüs etc.).

**Props:**

| Prop | Typ | Beschreibung |
|---|---|---|
| `title` | `string` | Popover-Titel |
| `childViews` | `View[]` | Unteransichten für Navigation |

**Slots:** `trigger: { toggleFloatingUi }`, `popover-items__base`, `popover-items__{viewId}`

---

### `mt-popover-item`

Einzelner Eintrag in einem Popover.

**Props:** `label`, `showOptions`, `showCheckbox`, `checkboxChecked`

**Events:** `click-options`, `change-checkbox`

---

### `mt-popover-item-result`

Suchergebnis-Liste in einem Popover. Enthält Suchfeld und Options-Liste.

---

## Tabellen- und Listen-Komponenten

### `mt-data-table`

Vollständige Datentabelle mit Pagination, Sortierung, Filterung, Spaltenkonfiguration.

**Props:**

| Prop | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `dataSource` | `Array<{ id: string, [key: string]: any }>` | ja | — | Datensätze |
| `columns` | `ColumnProperty[]` | ja | — | Spaltendefinitionen |
| `currentPage` | `number` | ja | — | Aktuelle Seite |
| `paginationLimit` | `number` | ja | — | Einträge pro Seite |
| `paginationTotalItems` | `number` | ja | — | Gesamt-Anzahl |
| `columnChanges` | `Record<string, ColumnChanges>` | nein | `{}` | Spaltenanpassungen |
| `title` | `string` | nein | `''` | Titel |
| `subtitle` | `string` | nein | `''` | Untertitel |
| `layout` | `'default'\|'full'` | nein | `'default'` | Layout |
| `sortBy` | `string` | nein | `''` | Sortierspalte |
| `sortDirection` | `'ASC'\|'DESC'` | nein | `'ASC'` | Sortierrichtung |
| `isLoading` | `boolean` | nein | `false` | Ladeanimation |
| `disableSearch` | `boolean` | nein | `false` | Suche deaktivieren |
| `filters` | `Filter[]` | nein | `[]` | Filter-Definitionen |
| `paginationOptions` | `number[]` | nein | `[5,10,25,50]` | Pagination-Optionen |
| `allowRowSelection` | `boolean` | nein | `false` | Zeilenauswahl |
| `enableReload` | `boolean` | nein | `false` | Reload-Button |
| `disableEdit` | `boolean` | nein | `false` | Bearbeiten deaktivieren |
| `disableDelete` | `boolean` | nein | `false` | Löschen deaktivieren |

**ColumnProperty:**
```ts
{
  label: string;       // Spaltenüberschrift
  property: string;    // Datenschlüssel
  renderer: 'text' | 'number' | 'price' | 'badge';
  position: number;    // Sortierposition
  allowResize?: boolean;
  allowSort?: boolean;
  width?: string;
  visible?: boolean;
}
```

**Events:** `update:currentPage`, `update:sortBy`, `update:sortDirection`, `update:searchValue`, `change-show-outlines`, `change-show-stripes`, `change-outline-framing`, `change-enable-row-numbering`, `select-all`, `deselect-all`, `row-selected`, `reload`

**Slot:** `toolbar` — zusätzliche Toolbar-Elemente

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

Datentabelle mit direkter Entity-Repository-Integration. Wrapper um `mt-data-table`.

---

### `mt-pagination`

Eigenständige Pagination-Komponente.

**Props:**

| Prop | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `currentPage` | `number` | ja | Aktuelle Seite |
| `limit` | `number` | ja | Einträge pro Seite |
| `totalItems` | `number` | ja | Gesamtanzahl |

**Events:** `change-current-page: [number]`

---

## Icons & Media

### `mt-icon`

Zeigt ein Meteor-Icon an.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `name` | `string` | required | Icon-Name (z.B. `'solid-save'`, `'regular-home'`) |
| `size` | `string` | — | Größe (z.B. `'16px'`, `'24'`) |
| `color` | `string` | — | CSS-Farbe |
| `mode` | `'solid'\|'regular'` | `'regular'` | Stil (wird durch Namens-Präfix überschrieben) |
| `decorative` | `boolean` | `false` | Dekorativ (kein ARIA-Label) |

```html
<mt-icon name="solid-save" size="24px" />
<mt-icon name="regular-home" color="var(--color-icon-primary-default)" />
```

---

### `mt-avatar`

Benutzer-Avatar mit Initialen oder Bild.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `size` | `'2xs'\|'xs'\|'s'\|'m'\|'l'` | `'m'` | Größe |
| `firstName` | `string` | — | Vorname (für Initialen) |
| `lastName` | `string` | — | Nachname (für Initialen) |
| `imageUrl` | `string` | — | Bild-URL (überschreibt Initialen) |
| `variant` | `'circle'\|'square'` | `'circle'` | Form |

---

## Context-Menü

### `mt-context-button`

Button der ein Kontext-Menü öffnet (Drei-Punkte-Menü).

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `icon` | `string` | `'solid-ellipsis-h-s'` | Button-Icon |
| `menuWidth` | `number` | `220` | Menübreite in px |
| `menuHorizontalAlign` | `'right'\|'left'` | `'right'` | Horizontale Ausrichtung |
| `menuVerticalAlign` | `'bottom'\|'top'` | `'bottom'` | Vertikale Ausrichtung |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `hasError` | `boolean` | `false` | Fehlerstatus |
| `autoClose` | `boolean` | `true` | Automatisch schließen |
| `title` | `string` | `''` | Menütitel |

**Slots:** `button-text` (Button-Beschriftung), `default: { toggleFloatingUi }` (Menüinhalt)

---

### `mt-context-menu-item`

Einzelner Menüeintrag im Kontext-Menü.

**Props:** `label`, `type: 'default'|'critical'`, `disabled`, `icon`

**Events:** `click`

---

### `mt-context-menu-divider`

Trennlinie im Kontext-Menü.

---

## Action-Menü (Reka UI basiert)

### `mt-action-menu`

Dropdown-Menü, basiert auf Reka UI DropdownMenu.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `isSubMenu` | `boolean` | `false` | Als Untermenü rendern |
| `matchTriggerWidth` | `boolean` | `false` | Breite an Trigger anpassen |

**Slot:** `default` — enthält `mt-action-menu-item` und `mt-action-menu-group`

---

### `mt-action-menu-item`

Menüeintrag im Action-Menü.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | `'default'\|'critical'` | `'default'` | Variante |
| `icon` | `string` | — | Icon |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `shortcut` | `ShortcutDefinition` | — | Tastaturkürzel |
| `isSubTrigger` | `boolean` | — | Als Sub-Menü-Trigger |
| `as` | `string` | — | Render-Element |
| `link` | `string` | — | URL |

---

### `mt-action-menu-group`

Gruppe von Menüeinträgen im Action-Menü.

---

## Content-Komponenten

### `mt-text`

Textrenderer mit Design-System-Typografie.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `size` | `'2xs'\|'xs'\|'s'\|'m'\|'l'\|'xl'\|'2xl'\|'3xl'` | — | Schriftgröße |
| `weight` | `'bold'\|'semibold'\|'medium'\|'regular'` | — | Schriftstärke |
| `color` | `string` | — | Farbe (Design-Token-Name oder CSS-Wert) |
| `as` | `string \| Component` | — | Render-Element |

```html
<mt-text size="l" weight="bold">Überschrift</mt-text>
<mt-text size="s" color="color-text-secondary-default">Hinweistext</mt-text>
```

---

## Charts

### `mt-chart`

ApexCharts-Wrapper für Admin-kompatible Diagramme.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `series` | `any[]` | required | Datenserien |
| `options` | `ApexOptions` | `{}` | ApexCharts-Optionen |
| `type` | `ApexChart['type']` | `'area'` | Diagrammtyp |
| `width` | `string\|number` | `'100%'` | Breite |
| `height` | `string\|number` | `'300px'` | Höhe |

---

## Entity-Komponenten

### `mt-entity-select`

Entity-Auswahl mit Repository-Integration.

**Props:**

| Prop | Typ | Default | Beschreibung |
|---|---|---|---|
| `entity` | `keyof EntitySchema.Entities` | required | Entity-Typ |
| `modelValue` | `any` | `null` | Ausgewählter Wert |
| `labelProperty` | `string \| string[]` | `'name'` | Label-Property der Entity |
| `valueProperty` | `string` | `'id'` | Wert-Property der Entity |
| `disabled` | `boolean` | `false` | Deaktiviert |
| `enableMultiSelection` | `boolean` | `false` | Mehrfachauswahl |
| `repository` | `Repository` | — | Eigenes Repository-Objekt |

**Events:** `update:modelValue`

---

## Theme

### `mt-theme-provider`

Stellt das Design-System-Theme bereit. Sollte einmalig in der App-Root verwendet werden.

**Slot:** `default`

---

## Allgemeine Hinweise

### v-model-Binding

- Formfelder: `v-model` bindet auf `modelValue` + `update:modelValue`
- Checkbox: Zusätzlich `checked` + `update:checked` verfügbar
- Vererbungs-Events: `inheritance-restore` und `inheritance-remove` bei Feldern mit `isInheritanceField`

### Design-Token-Variablen

Alle Komponenten verwenden CSS-Custom-Properties:
- `--color-*` — Farben (light/dark theme-fähig)
- `--scale-size-*` — Abstände/Größen
- `--border-radius-*` — Abrundungen
- `--font-family-*`, `--font-size-*` — Typografie

Import der Tokens (Administration):
```js
import '@shopware-ag/meteor-tokens/deliverables/administration/light.css';
// Für Dark-Mode:
import '@shopware-ag/meteor-tokens/deliverables/administration/dark.css';
// Primitive Farben:
import '@shopware-ag/meteor-tokens/deliverables/foundation/primitives.css';
```
