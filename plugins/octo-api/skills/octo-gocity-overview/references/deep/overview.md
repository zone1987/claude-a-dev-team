# Go City Trade API V2 — Vollständiger Überblick

## Was ist die Go City Trade API V2?

Die Go City Trade API V2 ist eine REST-API für Handelspartner (Trade Partners), um Go City-Bestellungen zu erstellen und zu verwalten. Die API ist konform zum [OCTO-Standard](https://www.octo.travel/) (Open Connectivity for Tourism).

> **Hinweis:** Ab November 2024 ist die API noch nicht für Tests oder Nutzung bereit, aber die Dokumentation wird bereitgestellt, damit API-Konsumenten ihre Migrationen vorbereiten können. Sie beeinträchtigt die V1-API in keiner Weise.

---

## Server-Umgebungen

| Umgebung | Base-URL |
|----------|---------|
| **Staging** | `https://api.staging.gocity.tech` |
| **Production** | `https://api.gocity.com` |

**Pfad-Präfix:** Alle Endpunkte haben den Präfix `/octo/`

### Vollständige Endpunkt-URLs

```
# Staging
https://api.staging.gocity.tech/octo/supplier
https://api.staging.gocity.tech/octo/products
https://api.staging.gocity.tech/octo/products/{id}
https://api.staging.gocity.tech/octo/availability
https://api.staging.gocity.tech/octo/bookings
https://api.staging.gocity.tech/octo/bookings/{id}
https://api.staging.gocity.tech/octo/bookings/{id}/confirm
https://api.staging.gocity.tech/octo/bookings/{id}/cancel

# Production
https://api.gocity.com/octo/supplier
https://api.gocity.com/octo/products
# ... etc.
```

---

## Authentifizierung

Go City verwendet **HTTP Bearer Token** für alle Endpunkte.

```http
Authorization: Bearer {your_token}
```

- **Schema:** `bearerAuth` (HTTP Bearer, OpenAPI 3.1)
- **Token-Format:** Vom Connectivity Manager bereitgestellt
- **Gültig für:** Alle 9 Endpunkte (kein Endpunkt ist öffentlich)
- **Erhalt:** Credentials und Anweisungen werden vom Connectivity Manager bereitgestellt

**Kein API-Key-Endpoint-Discovery** — im Gegensatz zu Ventrata gibt es keinen `GET /capabilities`-Endpunkt.

---

## Unterstützte OCTO-Capabilities

Go City unterstützt derzeit **nur eine Capability**:

| Capability | Status | Bemerkung |
|-----------|--------|-----------|
| `octo/pricing` | Unterstützt | Nur in Staging verfügbar (Stand: 12. August) |

### Aktivierung der octo/pricing Capability

Die Capability kann auf zwei Wegen aktiviert werden:

**Option 1: HTTP-Header**
```http
Octo-Capabilities: octo/pricing
```

**Option 2: Query-Parameter**
```
?_capabilities=octo/pricing
```

Für mehrere Capabilities (theoretisch): kommagetrennte Liste.

```http
Octo-Capabilities: octo/pricing,octo/content
```

> **Hinweis:** `octo/content` ist laut OpenAPI-Spec als Beispiel erwähnt, aber aktuell offiziell nur `octo/pricing` unterstützt.

**Kein Pflicht-Header:** Im Gegensatz zu Ventrata ist `Octo-Capabilities` bei Go City **nicht zwingend** erforderlich — es ist optional für die Preisanzeige.

---

## Produktkonzept: Passes

Bei Go City sind **Produkte Pässe**. Die Produktstruktur folgt einer festen Hierarchie:

```
Produkt = Kombination aus:
  └── Destination (z.B. Chicago, London)
  └── Brand (Go City, Great, Big Bus, Omnia)
  └── Duration Type (Days = All-Inclusive, Choices = Explorer)
  └── Variant (Standard, Plus, Lite, Deluxe, Single-Sell)

Option = Dauer/Typ innerhalb des Produkts:
  └── z.B. "1-Day Standard Pass" oder "1-Choice Extension"

Unit = Ticket-Typ:
  └── Adult
  └── Child
  └── VIP
```

**Beispiel:** Produkt "Chicago Go City All-Inclusive Standard"
- Option: "1 Day Standard Pass"
- Option: "2 Day Standard Pass"
- Option: "1-Choice Extension"
- Jede Option: Adult Unit, Child Unit, VIP Unit

---

## Availability-Modell: Immer FREESALE

Go City-Produkte sind **immer verfügbar**. Der Availability-Schritt ist trotzdem implementiert für die Bequemlichkeit der API-Konsumenten (um eine `availabilityId` für Buchungen zu erhalten).

**Feste Eigenschaften:**
- `status` ist immer `FREESALE`
- `vacancies` ist immer `null` (FREESALE = unbegrenzte Kapazität)
- `openingHours` ist immer `00:00-23:59`
- `availabilityType` ist immer `OPENING_HOURS`

**Dennoch Pflicht:** Obwohl Produkte immer verfügbar sind, ist `availabilityRequired` auf `true` gesetzt — die Partner müssen die `availabilityId` liefern, damit Go City nach Reisedatum abrechnen kann.

---

## Weitere Produkt-Besonderheiten

| Feld | Wert | Bedeutung |
|------|------|-----------|
| `allowFreesale` | immer `true` | Buchung ohne Availability-Prüfung möglich |
| `instantConfirmation` | immer `true` | Sofortige Bestätigung nach Kauf |
| `instantDelivery` | immer `true` | Sofortige Ticket-Lieferung |
| `availabilityRequired` | immer `true` | availabilityId dennoch pflicht (Abrechnungsgründe) |
| `pricingPer` | `UNIT` | Preis pro Person/Ticket |
| `deliveryFormats` | `PDF_URL`, `HTML_URL` | PDF oder HTML-Seite |
| `deliveryMethods` | `TICKET`, `VOUCHER` | Beide Formate |
| `redemptionMethod` | `DIGITAL` oder `PRINT` | |

---

## Alle 9 Endpunkte im Überblick

| Methode | Pfad | Zweck |
|---------|------|-------|
| `GET` | `/octo/supplier` | Supplier-Informationen abrufen |
| `GET` | `/octo/products` | Alle Produkte (Pässe) abrufen |
| `GET` | `/octo/products/{id}` | Einzelnes Produkt abrufen |
| `POST` | `/octo/availability` | Verfügbarkeit prüfen |
| `GET` | `/octo/bookings` | Buchungen filtern/auflisten |
| `POST` | `/octo/bookings` | Buchung reservieren (ON_HOLD) |
| `GET` | `/octo/bookings/{id}` | Einzelne Buchung abrufen |
| `POST` | `/octo/bookings/{id}/confirm` | Buchung bestätigen |
| `POST` | `/octo/bookings/{id}/cancel` | Buchung stornieren |

---

## priceDistributionModel Parameter

Ein Go-City-spezifischer Query-Parameter an mehreren Endpunkten:

```
?priceDistributionModel=PUBLIC      # Standard (Publikumspreise)
?priceDistributionModel=RESTRICTED  # Eingeschränkte/Händlerpreise
```

Verfügbar bei: `GET /products`, `GET /products/{id}`, `POST /availability`, `POST /bookings`, `POST /bookings/{id}/confirm`

---

## Nicht implementierte OCTO-Features

Im Vergleich zur Ventrata-Implementierung fehlen bei Go City:

- `GET /octo/capabilities` — kein Capabilities-Endpunkt
- `POST /octo/availability/calendar` — kein Kalender-Endpunkt
- `PATCH /octo/bookings/{id}` — kein Update-Endpunkt
- `POST /octo/bookings/{id}/extend` — keine Verlängerung
- `DELETE /octo/bookings/{id}` — kein DELETE
- `Octo-Env` Header — kein Test/Live-Modus-Header
- Alle erweiterten Capabilities (octo/content, octo/cart, octo/gifts, etc.)

---

## OpenAPI-Spec

Die vollständige, autoritative OpenAPI 3.1 Spec liegt unter:
`references/gocity-openapi.json`

---

**Quellen:**
- `/tmp/gocity-openapi.json` — Go City Trade API V2 OpenAPI 3.1 Spec
- `/tmp/gocity.html` — Gerenderte Redoc-Dokumentation
