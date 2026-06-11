# ApiService (Storefront) (`src/Resources/app/storefront/src/service/api.service.js`)

## Zweck
Dünner Fetch-Wrapper mit Standard-Headern (`Content-Type: application/json`, `X-Requested-With: XMLHttpRequest`).

## Typ
- `export default class ApiService` (statisch)

## Methoden
- `static _getBasicHeaders()` — Basis-Header.
- `static post(route, params, headers={})` — `fetch` POST, JSON-Body.
- `static get(route, headers={})` — `fetch` GET.

## Bezüge
`octo-api.service.js`.
