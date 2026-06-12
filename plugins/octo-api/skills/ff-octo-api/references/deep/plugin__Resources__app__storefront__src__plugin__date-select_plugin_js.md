# FfDateSelectPlugin (`src/Resources/app/storefront/src/plugin/date-select.plugin.js`)

## Zweck
Datumsauswahl der Buy-Box auf Basis von **flatpickr**. Lädt pro Monat den Verfügbarkeitskalender, deaktiviert nicht-buchbare Tage, wählt automatisch ein verfügbares Datum und publiziert Kalender-/Datums-Events. Quelle der 3 Calendar-Zustände (`available`/`empty-month`/`unsupported`).

## Typ & Vererbung
- `export default class FfDateSelectPlugin extends OctoBasePlugin`
- Registriert auf `[data-ff-date-select]`.

## Optionen (`static options`)
`apiProduct`, `selectedOptionUuid`, `dateFormat` (`d.m.Y`), `locale`, `showClear/showClose`, `enableTime` (false), `useCurrent` (false), `minDate`/`defaultDate` (heute), `snippets.noAvailableSlotsHint`, `warningIcon`.

## Methoden
- `init()` — initialisiert State, justiert `defaultDate` (−1/+1 Tag-Logik), `initFlatpickr()`, `onChange([defaultDate])`.
- `initFlatpickr()` — flatpickr mit Locale (de/en), `onChange`, `onMonthChange`, `onDayCreate` (Titel für disabled Tage).
- `onChangeMonth(...)` — setzt Monat, `_loadCalendarAvailability()`.
- `onChange(selectedDates)` — bei echtem Datumswechsel `_loadCalendarAvailability()`.
- `_loadCalendarAvailability()` — `OctoApiService.getAvailabilityCalendar(...)`; ermittelt `calendarStatus`:
  - `[]` → `unsupported` (Provider ohne Calendar-Endpoint, z.B. GoCity 404→[]) → Pipeline NICHT blockieren, gewähltes Datum NICHT via `setDate` überschreiben.
  - Liste ohne verfügbare Tage → `empty-month` (Hinweis im flatpickr, Tage disabled).
  - sonst `available`. Baut `this.calendar` (Map localDate→entry) + `disabledDates`; wählt ggf. ersten verfügbaren Tag. Publisht `octo-calendar-changed` (calendar, selectedDate, status) und `octo-date-changed` (selectedDate).

## Besonderheiten / Fallstricke
- **`unsupported` vs. `empty-month`** ist die zentrale Unterscheidung; falsch behandelt → entweder verschluckte Klicks (GoCity) oder falsche „keine Slots"-Hinweise.
- `console.table(...)` Debug-Ausgabe ist aktiv (nicht hinter octoDebug).
- Mobile vs. Desktop flatpickr-Container unterschiedlich behandelt (Hint-Platzierung).

## Bezüge
`octo-api.service.js`, `buy-box.plugin.js` (`_onCalendarChanged`), `Controller/AvailbilityController.php::availabilityCalendar`, `Service/CalendarService.php`, `../gocity-api.md`.
