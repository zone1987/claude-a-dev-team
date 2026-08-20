# Shopware 6 — Admin API `_action` endpoints

Operations that are not plain CRUD live under `/api/_action/...` (all with bearer auth).

| Purpose | Endpoint (example) |
|---|---|
| Change order state | `POST /api/_action/order/{orderId}/state/{transition}` (e.g. `process`, `complete`) |
| Order transaction/delivery state | `POST /api/_action/order_transaction/{id}/state/{transition}`, `order_delivery/...` |
| Clear cache / index | `DELETE /api/_action/cache`, `POST /api/_action/index` |
| Reserve number range | `POST /api/_action/number-range/reserve/{type}/{salesChannelId}` |
| Generate document | `POST /api/_action/order/{id}/document/{type}` |
| Send mail | `POST /api/_action/mail-template/send` |
| Sync (bulk) | `POST /api/_action/sync` (`sw-sync-api`) |
| Clone | `POST /api/_action/clone/{entity}/{id}` |
| System config | `GET/POST /api/_action/system-config` |

The available state transitions depend on the state machine (`shopware-checkout` → `sw-order-state-machine`).
**Complete list of all `_action` endpoints of the specific shop**: OpenAPI catalogue (`sw-api-catalog` / `/sw-api-map`).
