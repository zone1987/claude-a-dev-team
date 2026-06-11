# OctoApiService (Storefront) (`src/Resources/app/storefront/src/service/octo-api.service.js`)

## Zweck
Client-Service für die OCTO-Storefront-Endpunkte (`availability/check`, `availability/calendar`). Publiziert Lade-States und parst JSON.

## Typ
- `export default class OctoApiService` (statisch)

## Felder
- `#_routes`: `checkAvailability` = `/octo-api/availability/check`, `availabilityCalendar` = `/octo-api/availability/calendar`.

## Methoden
- `static getAvailabilityCalendar(identifier, productId, optionId, date, units=[])` — publisht `octo-state-change {calendar:true/false}`, POST via `ApiService`, `.json()`.
- `static getAvailability(identifier, productId, productUuid, product, localDate, localTime=null, units=[])` — publisht `octo-state-change {availability:...}`, POST, `.json()`, `catch` loggt.

## Bezüge
`api.service.js`, `buy-box.plugin.js`, `date-select.plugin.js`, `state.service.js`, `Controller/AvailbilityController.php`.
