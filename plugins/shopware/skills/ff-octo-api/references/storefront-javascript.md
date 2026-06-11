# Storefront JavaScript

## Plugin-Registrierung

**Datei:** `src/Resources/app/storefront/src/main.js`

```javascript
import FfBuyBoxPlugin from './plugin/buy-box.plugin';
PluginManager.register('FfBuyBox', FfBuyBoxPlugin, '[data-ff-buy-box]');
```

Nur **ein** Plugin wird global registriert. Alle anderen sind Child-Plugins.

---

## Plugin-Hierarchie

```
FfBuyBoxPlugin (Parent) — [data-ff-buy-box]
  ├── DateSelectPlugin    — [data-date-select]
  ├── TimeSelectPlugin    — [data-time-select]
  ├── QuantitySelectPlugin — [data-quantity-select]
  └── BuyBtnPlugin        — .buy-widget button.btn-buy
```

Child-Plugins werden via `BuyBoxPluginRegistry` verwaltet und nach jedem DOM-Update (Availability-Response) neu initialisiert.

---

## FfBuyBoxPlugin

**Datei:** `src/plugin/buy-box.plugin.js`
**Selector:** `[data-ff-buy-box]`

### Optionen (aus Twig-Data-Attribute)

```javascript
static options = {
    apiProduct: {},          // { identifier, uuid, product: {...} }
    product: {},             // Shopware-Produktdaten
    selector: {
        wrapper: '.product-detail-configurator-details-wrapper'
    },
    routes: {
        checkAvailability: '/octo-api/availability/check',
        getItem: '/octo-api/session/get-item',
        setItem: '/octo-api/session/set',
        removeItem: '/octo-api/session/remove-item'
    }
};
```

### State

```javascript
this.selectedDate = null;     // Datum vom DateSelectPlugin
this.selectedTime = null;     // Uhrzeit vom TimeSelectPlugin
this.selectedUnits = [];      // Units vom QuantitySelectPlugin
this.localDateStart = null;   // UTC ISO String
this.localDateEnd = null;     // UTC ISO String
```

### Event-Subscriptions

```javascript
document.$emitter.subscribe('octo-date-changed', this._onDateChanged.bind(this));
document.$emitter.subscribe('octo-time-changed', this._onTimeChanged.bind(this));
document.$emitter.subscribe('octo-quantity-changed', this._onQuantityChanged.bind(this));
```

### _loadAvailability()

1. Publiziert `octo-state-change: {key: 'availability', value: true}` (Loading-Start)
2. POST an `/octo-api/availability/check`:
   ```json
   {
       "identifier": "goldentours",
       "productId": "shopware-product-id",
       "productUuid": "api-product-uuid",
       "product": { ... },
       "localDateStart": "2025-03-15T00:00:00.000Z",
       "localDateEnd": "2025-03-15T23:59:59.000Z",
       "units": [{"id": "unit-uuid", "quantity": 2}]
   }
   ```
3. Response ist **HTML-String**
4. Ersetzt `.product-detail-configurator-details-wrapper` via `ElementReplaceHelper.replaceFromMarkup()`
5. **Re-initialisiert alle Child-Plugins** via `BuyBoxPluginRegistry.initializePlugins()`
6. Publiziert `octo-state-change: {key: 'availability', value: false}` (Loading-Ende)

---

## DateSelectPlugin

**Datei:** `src/plugin/date-select.plugin.js`
**Selector:** `[data-date-select]`

### Optionen

```javascript
static options = {
    apiProduct: {},
    selectedOptionUuid: null,
    dateFormat: 'd.m.Y',
    locale: 'de-DE',
    minDate: null,
    defaultDate: null     // Wird auf morgen gesetzt
};
```

### Initialisierung

1. Default-Datum = morgen
2. Initialisiert **Flatpickr** mit:
   - Locale: deutsch oder englisch (basierend auf option)
   - minDate: heute
   - onChange, onMonthChange, onDayCreate Callbacks
3. Ruft sofort `onChange` mit Default-Datum auf

### _loadCalendarAvailability()

Wird bei **Monatswechsel** aufgerufen:

```javascript
OctoApiService.getAvailabilityCalendar(identifier, productId, optionId, date, units)
```

- Tage mit `statusCode !== 'AVAILABLE'` werden deaktiviert
- Deaktivierte Tage bekommen Tooltip mit `statusMessage`
- Aktualisiert Flatpickr `config.disable` und zeichnet neu

### Events

- **Publiziert:** `octo-date-changed` mit `{ selectedDate }`
- **Publiziert:** `octo-calendar-changed` mit `{ calendar, selectedDate, status }`
- **Publiziert:** `octo-state-change` mit `{ key: 'calendar', value: true/false }`

### Calendar-Status (3-Werte-Enum)

Der `status`-String im `octo-calendar-changed`-Event differenziert drei Fälle der Calendar-Response — wichtig, weil sie sehr unterschiedliches BuyBox-Verhalten erfordern:

| Status | Wann? | Wirkung in BuyBox |
|---|---|---|
| `'available'` | Provider lieferte Tage, mindestens einer ist buchbar | Normalfall: `_loadTimeWidget`, `availability/check` läuft |
| `'empty-month'` | Provider lieferte Tage, alle `available: false` (echter leerer Monat, z. B. London Eye Juni 2026) | `_resetBuyBoxForEmptyMonth`, blockiert nachfolgende `/availability/check`-Calls |
| `'unsupported'` | Provider lieferte einen wirklich leeren Array `[]` — meist weil sein OCTO-Endpoint `/availability/calendar` mit HTTP 404 antwortet (Beispiel: GoCity-Pässe haben kein Tag-für-Tag-Modell) | `_calendarEmpty = false`, KEIN Reset, KEIN Block — das nachfolgende `octo-date-changed` darf normal `/availability/check` triggern |

**Wichtig im Date-Select-Plugin:** Bei `'unsupported'` wird `flatpickrInstance.setDate(this.selectedDate, true, 'date')` **übersprungen**, weil das das vom User gerade gewählte Datum durch den alten Init-Wert überschreiben würde.

---

## TimeSelectPlugin

**Datei:** `src/plugin/time-select.plugin.js`
**Selector:** `[data-time-select]`

### Verhalten

1. Hört auf `change` Event des `<select>` Elements
2. Speichert Uhrzeit via Session-API:
   ```javascript
   POST /octo-api/session/set { key: 'time', value: '09:00' }
   ```
3. Publiziert `octo-time-changed` Event
4. Publiziert `octo-state-change` mit `{ key: 'time', value: true/false }`

---

## QuantitySelectPlugin

**Datei:** `src/plugin/quantity-select.plugin.js`
**Selector:** `[data-quantity-select]`

### Optionen

```javascript
static options = {
    unit: {},       // { id, type, restrictions, price, quantity }
    units: [],      // Alle Units (für Referenz)
    debounce: 500   // Debounce in ms
};
```

### DOM-Selektoren

```javascript
this.subtractBtn = this.el.querySelector('.detail-unit-quantity-subtract');
this.addBtn = this.el.querySelector('.detail-unit-quantity-add');
this.countEl = this.el.querySelector('.detail-unit-quantity-count');
```

### Verhalten

- **Minus:** `count -= 1` (Minimum 0, Button disabled bei 0)
- **Plus:** `count += 1`
- **Debounce:** 500ms nach letzter Änderung
- **Init:** `_publish(false)` — kein Reload
- **Change:** `_publish(true)` — löst Availability-Check aus

### Events

- **Publiziert:** `octo-quantity-changed` mit `{ count, unit, reload }`

---

## BuyBtnPlugin

**Datei:** `src/plugin/buy-btn.plugin.js`
**Selector:** `.buy-widget button.btn-buy`

### Verhalten

Nutzt JavaScript **Proxy** für reaktiven State:
```javascript
this._selected = new Proxy({date: null, time: null, units: []}, {
    set: (target, key, value) => {
        target[key] = value;
        this._updateState();
        return true;
    }
});
```

Hört auf Events:
- `octo-date-changed` → `_selected.date = date`
- `octo-time-changed` → `_selected.time = time`
- `octo-units-changed` → `_selected.units = units`

---

## Services

### ApiService

**Datei:** `src/service/api.service.js`

```javascript
static async post(route, params = {}, headers = {}) { ... }
static async get(route, headers = {}) { ... }
```

Standard-Headers: `Content-Type: application/json`, `X-Requested-With: XMLHttpRequest`

### OctoApiService

**Datei:** `src/service/octo-api.service.js`

```javascript
static async getAvailabilityCalendar(identifier, productId, optionId, date, units = [])
// POST /octo-api/availability/calendar
// Returns: JSON response
```

### OptionService

**Datei:** `src/service/option.service.js`

```javascript
// Erkennt gewählte Shopware-Variante und mappt zu OCTO-Option
const selector = 'form[data-variant-switch] select';
// Liest <option> Text und sucht in apiProduct.product.options nach match
// Property: selectedOptionUuid (getter)
```

### StateService

**Datei:** `src/service/state.service.js`

```javascript
// Loading-State-Management via Proxy
const states = { availability: false, calendar: false, date: false, time: false };

// Hört auf 'octo-state-change' Events
// Setzt/entfernt 'is-loading' CSS-Klasse auf Haupt-Element
// Validiert State-Keys (wirft Fehler bei ungültigen)
```

### DateHelper

**Datei:** `src/helper/date.helper.js`

```javascript
static getDate(date, hour = 0, minute = 0, seconds = 0)
// Konvertiert lokales Datum zu UTC ISO String
// Returns: z.B. "2025-03-15T00:00:00.000Z"
```

---

## Structs

### BuyBoxPluginRegistry

**Datei:** `src/struct/buy-box-plugin-registry.struct.js`

```javascript
add(name, pluginClass, selector, options = {})
// Registriert Plugin in Registry

initializePlugins()
// Prüft ob Plugin schon im PluginManager
// Neue Plugins: PluginManager.register() + initializePlugin()
// Bestehende: PluginManager.initializePlugin()
```

### BuyBoxPlugin Struct

**Datei:** `src/struct/buy-box-plugin.struct.js`

Immutable Datencontainer:
```javascript
// Properties: pluginName, plugin, selector, pluginOptions
// Nur Getter, keine Setter
```

---

## Event-Übersicht

| Event | Publisher | Subscriber | Payload |
|-------|----------|------------|---------|
| `octo-date-changed` | DateSelectPlugin | FfBuyBoxPlugin, BuyBtnPlugin | `{ date }` |
| `octo-time-changed` | TimeSelectPlugin | FfBuyBoxPlugin, BuyBtnPlugin | `{ time }` |
| `octo-quantity-changed` | QuantitySelectPlugin | FfBuyBoxPlugin | `{ count, unit, reload }` |
| `octo-state-change` | Multiple | StateService | `{ key, value }` |

---

## SCSS-Dateien

### Variablen

**`scss/variables/_custom.scss`:**
- Spacing: `$spacing-space-1` (4px) bis `$spacing-space-12` (80px)
- Font: 'Albert Sans Variable', Weights: 400/500/700/800
- Font-Sizes: h1 (60px) bis small (14px)

**`scss/variables/_colors.scss`:**
- Primary: London (#D92127), New York (#4D8065), Dubai (#946F00)
- Secondary: #27346B
- Grays: 100-800

### Konfigurator-Styles

**`scss/component/_product-detail-configurator.scss`:**

```scss
.product-detail-configurator-details {
    // Card-Layout
    &.is-loading .product-detail-configurator-details-loading { display: flex; }
    &.is-loading .product-detail-configurator-details-content { opacity: 0.3; }
    &.is-default-variant { @include visually-hidden(); }
}

.detail-unit {
    // Flex, space-between, padding-bottom 16px, bottom border
}

.detail-unit-quantity {
    // Inline-flex, 2.25rem Circle-Buttons für +/-
    &-subtract, &-add {
        width: 2.25rem; height: 2.25rem; border-radius: 50%;
    }
}
```

### Line-Item-Styles

**`scss/component/_line-item.scss`:**

```scss
.line-item-product-reservation {
    display: none;
    // Nur in Checkout sichtbar:
    .is-ctl-checkout.is-act-cartpage & { display: block; }
}
```
