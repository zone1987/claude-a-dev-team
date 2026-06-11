---
name: sw-admin-api-actions
description: >
  Die _action-Endpunkte der Shopware-6 Admin API (nicht-CRUD-Operationen): Order-State-Transitions
  (/api/_action/order/{id}/state/{transition}), Cache (/api/_action/cache, index), Number-Range, Document-Erzeugung,
  Mail send, Clone. Trigger: "_action endpoint", "order state transition api", "cache clear api", "document api action",
  "number-range reserve api", "mail send api", "api action shopware". Shopware 6.7.
---

# Shopware 6 — Admin-API `_action`-Endpunkte

Operationen, die kein reines CRUD sind, liegen unter `/api/_action/...` (alle mit Bearer-Auth).

| Zweck | Endpoint (Beispiel) |
|---|---|
| Order-State wechseln | `POST /api/_action/order/{orderId}/state/{transition}` (z.B. `process`, `complete`) |
| Order-Transaction/Delivery-State | `POST /api/_action/order_transaction/{id}/state/{transition}`, `order_delivery/...` |
| Cache leeren / Index | `DELETE /api/_action/cache`, `POST /api/_action/index` |
| Number-Range reservieren | `POST /api/_action/number-range/reserve/{type}/{salesChannelId}` |
| Dokument erzeugen | `POST /api/_action/order/{id}/document/{type}` |
| Mail senden | `POST /api/_action/mail-template/send` |
| Sync (Bulk) | `POST /api/_action/sync` (`sw-sync-api`) |
| Clone | `POST /api/_action/clone/{entity}/{id}` |
| System-Config | `GET/POST /api/_action/system-config` |

Verfügbare State-Transitions hängen von der State-Machine ab (`shopware-checkout` → `sw-order-state-machine`).
**Vollständige Liste aller `_action`-Endpunkte des konkreten Shops**: OpenAPI-Katalog (`sw-api-catalog` / `/sw-api-map`).
