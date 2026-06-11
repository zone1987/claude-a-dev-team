---
name: sw-sales-agent-api
description: >
  Die Shopware Commercial "Sales Agent" (SwagSalesAgent) API: B2B-Vertriebs-Extension, in der Sales-Agents zugewiesene
  Kunden verwalten/in deren Namen bestellen. Eigene API-Endpunkte zusätzlich zur Store/Admin-API. Trigger: "Sales Agent",
  "SwagSalesAgent", "swag-sales-agent", "Vertriebsmitarbeiter API", "sales agent endpoints", "B2B sales agent shopware".
  Shopware 6.7 (Commercial).
---

# Shopware 6 — Sales-Agent-API (Commercial)

**SwagSalesAgent** ist eine Commercial-Extension: Vertriebsmitarbeiter (Sales Agents) werden in der Administration
verwaltet, bekommen Kunden zugewiesen und können in deren Kontext agieren (Angebote/Bestellungen). Die Extension
bringt eigene API-Endpunkte mit (zusätzlich zu Admin/Store API).

- Nur verfügbar, wenn die Commercial-/Sales-Agent-Extension installiert ist.
- Authentifizierung folgt dem jeweiligen Kontext (Admin-OAuth für Verwaltung; Sales-Agent-spezifische Auth/Token
  für die Agent-App) — genaues Schema je installierter Version.
- **Verbindliche, vollständige Endpunktliste**: die installierte Extension exponiert ihre Routen in der OpenAPI-Spec —
  über den API-Katalog erfassen (`sw-api-catalog` / `/sw-api-map`); die offizielle Referenz liegt unter
  `shopware.stoplight.io/docs/swag-sales-agent` (JS-Doku, im Browser).

Für Standard-Verkaufsprozesse die Store API (`sw-store-api-endpoints`); Sales-Agent nur bei installierter B2B-Extension.
