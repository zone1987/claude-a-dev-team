# FfBuyBoxPlugin (`src/Resources/app/storefront/src/plugin/buy-box.plugin.js`)

## Zweck
Zentrales Storefront-Plugin der Buy-Box (PDP). Orchestriert Datum-, Zeit- und Mengen-Auswahl der OCTO-Produkte, ruft `availability/check`, rendert die zurückgelieferten Widget-Fragmente, erzwingt Kapazitätslimits und sperrt die Box bei SOLD_OUT/CLOSED. Registriert die Child-Plugins. **Frontend-Hotspot.**

## Typ & Vererbung
- `export default class FfBuyBoxPlugin extends OctoBasePlugin`
- Registriert via `BuyBoxLoader` auf `[data-ff-buy-box]` (nur sichtbare Instanz).

## Optionen (`static options`)
`apiProduct` (null), `product` (null), `selector.wrapper` (null). Zur Laufzeit zusätzlich `options.routes.checkAvailability`, `options.viewports`.

## State (init)
`cmsBlock`, `selectedDate/Time/Units`, `isActive`; In-Flight-Guards `_availabilityInFlight`/`_availabilityPending`; `_availabilityBlocked` (SOLD_OUT/CLOSED-Sperre); `_calendarEmpty`; `_capacity`; `_unitMeta`.

## Methoden
- `init()` — State, `_loadState()`.
- `_loadState()` — Events registrieren, `OptionService`, Child-Plugins registrieren+initialisieren.
- `_registerPlugins()` — über `BuyBoxPluginRegistry`: `FfReservationCountdown`, `FfDateSelect`, `FfTimeSelect`, `FfQuantitySelect`, `FfBrowserTranslation`, `BuyBtn` (`.buy-widget button.btn-buy`), `AjaxModal`.
- `_initializePlugins()`.
- `_registerEvents()` — `document.$emitter`: `octo-date-changed`, `octo-time-changed`, `octo-quantity-changed`, `octo-quantity-dom-changed`→`_enforceCapacityLimit`, `octo-calendar-changed`.
- `_onCalendarChanged(event)` — 3 Zustände: `unsupported` (kein Calendar-Endpoint, z.B. GoCity → Pipeline nicht blockieren), `empty-month` (Reset + `/check` blockieren), `available` (Time-Widget laden).
- `_resetBuyBoxForEmptyMonth()` — leert Units/Time, Preis-Reset, `_availabilityBlocked=false`, mehrfache verzögerte DOM-Resets (100/400/1000ms), publisht leere units.
- `_performDomReset()` — DOM-Cleanup über **alle** `[data-ff-buy-box]` (Mobile+Desktop): Units leeren, Time verstecken, initialen „Ab"-Preis-Snapshot wiederherstellen.
- `_enforceCapacityLimit()` — summiert DOM-Quantities; bei Limit alle Plus-Buttons disabled + `[data-ff-capacity-limit]`-Alert mit `%count%`. Respektiert `_availabilityBlocked`.
- `_getSelectedEntryFromCalendar(calendar, selectedDate)` — Map-Lookup per `YYYY-MM-DD`.
- `_loadTimeWidget(startTimes, localDate)` — füllt Time-Select; heute → nur Zukunftsslots; 3 Sichtbarkeitszustände (Slots / alle vergangen / keine).
- `_onQuantityChanged(event)` — pflegt `selectedUnits` + `_unitMeta` (restrictions/type, getrennt weil Backend `restrictions` im check-Payload nicht akzeptiert), publisht `octo-units-changed`, `_enforceCapacityLimit`, optional reload.
- `_onTimeChanged` / `_onDateChanged` — setzen State, `_loadAvailability()`.
- `_loadAvailability()` — In-Flight-Koaleszenz; bei `_calendarEmpty` return; `OctoApiService.getAvailability(...)`; rendert `response.widgets` (Selektor→HTML) + re-init Plugins; **Blocked-Logik** bei `available===false`/`SOLD_OUT`/`CLOSED` (Units leeren, Plus disablen, `_availabilityBlocked=true`); merkt `capacity`; im `finally` pending-Folgelauf.

## Besonderheiten / Fallstricke
- **Doppelte DOM-Instanzen** (Mobile/Desktop): nur eine aktiv (Loader), DOM-Resets treffen aber beide.
- **In-Flight-Koaleszenz** verhindert parallele check-Requests bei rapid clicks.
- **Capacity vs. Blocked** sind getrennte Sperrmechanismen — Reihenfolge/Guards beachten.
- Events laufen über `document.$emitter` (global) → bei mehreren BuyBox-Instanzen Vorsicht (Loader entschärft das).
- `0,00 €` wird bewusst vermieden (Reset stellt „Ab"-Preis wieder her).

## Bezüge
`octo-base.plugin.js`, `date-select`/`time-select`/`quantity-select`/`buy-btn`/`reservation-countdown.plugin.js`, `struct/buy-box-plugin-registry.struct.js`, `service/option.service.js`, `service/octo-api.service.js`, `loader/buy-box.loader.js`, `Controller/AvailbilityController.php`, `../storefront-javascript.md`.
