# Ventrata OCTO API — Alle Endpunkte (Konsolidierte Referenz)

**Base-URL:** `https://api.ventrata.com/octo`

---

## Core-Endpunkte (immer verfügbar, keine Capability nötig)

### Supplier & Capabilities

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/supplier/` | Supplier-Informationen abrufen | — |
| `GET` | `/capabilities/` | Alle unterstützten Capabilities auflisten | — |

### Products

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/products/` | Alle Produkte des Suppliers | — |
| `GET` | `/products/{id}` | Einzelnes Produkt nach ID | — |

### Availability

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/availability/` | Verfügbarkeit prüfen (Timeslots/Tage) | — |
| `POST` | `/availability/calendar` | Kalender-Übersicht der Verfügbarkeit (ein Eintrag pro Tag) | — |
| `POST` | `/availability/batch` | Batch-Verfügbarkeitsprüfung (mehrere Anfragen) | — |
| `POST` | `/availability/calendar/batch` | Batch-Kalender-Verfügbarkeitsprüfung | — |

### Bookings (Core-Lifecycle)

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/bookings/` | Buchung reservieren (→ Status: ON_HOLD) | — |
| `GET` | `/bookings/` | Buchungen auflisten/filtern | — |
| `GET` | `/bookings/{uuid}` | Einzelne Buchung abrufen | — |
| `PATCH` | `/bookings/{uuid}` | Buchung aktualisieren | — |
| `POST` | `/bookings/{uuid}/confirm` | Buchung bestätigen (→ Status: CONFIRMED) | — |
| `POST` | `/bookings/{uuid}/cancel` | Buchung stornieren (→ Status: CANCELLED) | — |
| `POST` | `/bookings/{uuid}/extend` | Reservierungs-Ablaufzeit verlängern | — |
| `DELETE` | `/bookings/{uuid}` | Buchung löschen (nur ON_HOLD) | — |

---

## Capability: octo/pricing

Keine eigenen Endpunkte — erweitert die Responses der Core-Endpunkte um Preisfelder.

**Aktivierung:** `Octo-Capabilities: octo/pricing` Header
**Felder werden hinzugefügt zu:** Products, Availability, Bookings, Orders, Gifts

---

## Capability: octo/content

Keine eigenen Endpunkte — erweitert Responses um Inhaltsfelder.

**Aktivierung:** `Octo-Capabilities: octo/content` Header
**Felder werden hinzugefügt zu:** Products, Options, Units, Availability, Booking, Supplier

---

## Capability: octo/cart

Multi-Booking Cart / Orders. Gruppiert mehrere Buchungen zu einer Bestellung.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/orders/` | Order (Cart) erstellen mit mehreren Buchungen | `octo/cart` |
| `GET` | `/orders/` | Orders auflisten | `octo/cart` |
| `GET` | `/orders/{uuid}` | Einzelne Order abrufen | `octo/cart` |
| `PATCH` | `/orders/{uuid}` | Order aktualisieren | `octo/cart` |
| `POST` | `/orders/{uuid}/confirm` | Order bestätigen | `octo/cart` |
| `POST` | `/orders/{uuid}/cancel` | Order stornieren | `octo/cart` |
| `DELETE` | `/orders/{uuid}` | Order löschen | `octo/cart` |

---

## Capability: octo/gifts

Gift-Voucher-Verwaltung.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/gifts/` | Gift-Voucher erstellen | `octo/gifts` |
| `GET` | `/gifts/` | Gift-Voucher auflisten | `octo/gifts` |
| `GET` | `/gifts/{uuid}` | Einzelnen Gift-Voucher abrufen | `octo/gifts` |
| `PATCH` | `/gifts/{uuid}` | Gift-Voucher aktualisieren | `octo/gifts` |
| `POST` | `/gifts/{uuid}/confirm` | Gift-Voucher bestätigen | `octo/gifts` |
| `POST` | `/gifts/{uuid}/cancel` | Gift-Voucher stornieren | `octo/gifts` |
| `DELETE` | `/gifts/{uuid}` | Gift-Voucher löschen | `octo/gifts` |

---

## Capability: octo/redemption

Ticket-Einlösung an Attraktionen.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/redemption/lookup` | Ticket-Suche per Code/E-Mail/Mobil | `octo/redemption` |
| `POST` | `/redemption/redeem` | Ticket einlösen | `octo/redemption` |
| `POST` | `/redemption/unredeem` | Ticket-Einlösung rückgängig machen | `octo/redemption` |
| `POST` | `/redemption/noshow` | No-Show markieren | `octo/redemption` |

---

## Capability: octo/webhooks

Webhook-Verwaltung für Event-Benachrichtigungen.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/webhooks/` | Webhook registrieren | `octo/webhooks` |
| `GET` | `/webhooks/` | Alle Webhooks auflisten | `octo/webhooks` |
| `GET` | `/webhooks/{id}` | Einzelnen Webhook abrufen | `octo/webhooks` |
| `PATCH` | `/webhooks/{id}` | Webhook aktualisieren | `octo/webhooks` |
| `DELETE` | `/webhooks/{id}` | Webhook löschen | `octo/webhooks` |
| `POST` | `/webhooks/{id}/trigger` | Webhook manuell triggern (Test) | `octo/webhooks` |

**Event-Typen:** `booking_update`, `order_update`, `availability_update`, `product_update`

---

## Capability: octo/mappings

Self-Service-Mapping zwischen Reseller-Produkt-IDs und Supplier-IDs.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/mappings/` | Alle Mappings auflisten | `octo/mappings` |
| `POST` | `/mappings/` | Neues Mapping erstellen | `octo/mappings` |
| `DELETE` | `/mappings/{id}` | Mapping löschen | `octo/mappings` |

---

## Capability: octo/offers

Supplier-Angebote und angebotsbewusstes Pricing.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/offers/` | Verfügbare Angebote auflisten | `octo/offers` |

---

## Capability: octo/checkin

Online Check-in für Bookings/Orders/Gifts.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/checkin/lookup` | Check-in nach Referenz suchen | `octo/checkin` |
| `POST` | `/checkin/checkin` | Check-in durchführen | `octo/checkin` |

---

## Capability: octo/cardPayments

Kartenzahlungs-Integration.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/card-payments/` | Kartenzahlung initiieren | `octo/cardPayments` |
| `GET` | `/card-payments/{id}` | Kartenzahlung abrufen | `octo/cardPayments` |
| `GET` | `/card-payments/lookup` | Kartenzahlung per Referenz suchen | `octo/cardPayments` |

---

## Capability: octo/memberships

Mitgliedschaften/Jahrestickets.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/memberships/lookup` | Mitgliedschaft suchen | `octo/memberships` |

---

## Capability: octo/identities

Identitätsverwaltung (z.B. für Redemption-Geräte).

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/identities/` | Identität erstellen | `octo/identities` |
| `PATCH` | `/identities/{id}` | Identität aktualisieren | `octo/identities` |
| `DELETE` | `/identities/{id}` | Identität löschen | `octo/identities` |

---

## Capability: octo/campaigns

Kampagnen auflisten.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `GET` | `/campaigns/` | Alle Kampagnen auflisten | `octo/campaigns` |

---

## Capability: octo/notifications

Benachrichtigungs-Abonnements.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/notifications/` | Benachrichtigung abonnieren | `octo/notifications` |
| `GET` | `/notifications/` | Abonnements auflisten | `octo/notifications` |
| `DELETE` | `/notifications/{id}` | Abonnement kündigen | `octo/notifications` |

---

## Capability: octo/waitlists

Wartelisten für ausgebuchte Produkte.

| Methode | Pfad | Zweck | Capability |
|---------|------|-------|-----------|
| `POST` | `/waitlists/` | Wartelisten-Eintrag erstellen | `octo/waitlists` |

---

## Capability: octo/adjustments

Erweiterte Preisanpassungen bei Buchungen. Keine eigenen Endpunkte — erweitert Booking-Request/-Response.

---

## Capabilities ohne eigene Endpunkte

Diese Capabilities erweitern nur die Responses bestehender Endpunkte:

| Capability | Erweitert |
|-----------|----------|
| `octo/pricing` | Products, Availability, Bookings, Orders, Gifts |
| `octo/content` | Products, Options, Units, Availability, Booking, Supplier |
| `octo/extras` | Products (extraOptions), Bookings (extraItems) |
| `octo/packages` | Products (packages), Bookings (packageOptionId) |
| `octo/pickups` | Products, Availability, Bookings (pickupRequired, pickupPoint, etc.) |
| `octo/questions` | Products (questions), Bookings (questionAnswers) |
| `octo/waivers` | Products (waivers), Bookings (waiver submissions) |
| `octo/resources` | Availability (resources), Bookings (resource assignments) |
| `octo/rentals` | Products, Availability, Bookings (rentalDurationId) |
| `octo/adjustments` | Bookings (adjustments) |
| `octo/localization` | Lokalisierungsfelder |

---

## Vollständige Endpunkt-Gesamtübersicht

| # | Methode | Pfad | Capability |
|---|---------|------|-----------|
| 1 | GET | /supplier/ | Core |
| 2 | GET | /capabilities/ | Core |
| 3 | GET | /products/ | Core |
| 4 | GET | /products/{id} | Core |
| 5 | POST | /availability/ | Core |
| 6 | POST | /availability/calendar | Core |
| 7 | POST | /availability/batch | Core |
| 8 | POST | /availability/calendar/batch | Core |
| 9 | POST | /bookings/ | Core |
| 10 | GET | /bookings/ | Core |
| 11 | GET | /bookings/{uuid} | Core |
| 12 | PATCH | /bookings/{uuid} | Core |
| 13 | POST | /bookings/{uuid}/confirm | Core |
| 14 | POST | /bookings/{uuid}/cancel | Core |
| 15 | POST | /bookings/{uuid}/extend | Core |
| 16 | DELETE | /bookings/{uuid} | Core |
| 17 | POST | /orders/ | octo/cart |
| 18 | GET | /orders/ | octo/cart |
| 19 | GET | /orders/{uuid} | octo/cart |
| 20 | PATCH | /orders/{uuid} | octo/cart |
| 21 | POST | /orders/{uuid}/confirm | octo/cart |
| 22 | POST | /orders/{uuid}/cancel | octo/cart |
| 23 | DELETE | /orders/{uuid} | octo/cart |
| 24 | POST | /gifts/ | octo/gifts |
| 25 | GET | /gifts/ | octo/gifts |
| 26 | GET | /gifts/{uuid} | octo/gifts |
| 27 | PATCH | /gifts/{uuid} | octo/gifts |
| 28 | POST | /gifts/{uuid}/confirm | octo/gifts |
| 29 | POST | /gifts/{uuid}/cancel | octo/gifts |
| 30 | DELETE | /gifts/{uuid} | octo/gifts |
| 31 | GET | /redemption/lookup | octo/redemption |
| 32 | POST | /redemption/redeem | octo/redemption |
| 33 | POST | /redemption/unredeem | octo/redemption |
| 34 | POST | /redemption/noshow | octo/redemption |
| 35 | POST | /webhooks/ | octo/webhooks |
| 36 | GET | /webhooks/ | octo/webhooks |
| 37 | GET | /webhooks/{id} | octo/webhooks |
| 38 | PATCH | /webhooks/{id} | octo/webhooks |
| 39 | DELETE | /webhooks/{id} | octo/webhooks |
| 40 | POST | /webhooks/{id}/trigger | octo/webhooks |
| 41 | GET | /mappings/ | octo/mappings |
| 42 | POST | /mappings/ | octo/mappings |
| 43 | DELETE | /mappings/{id} | octo/mappings |
| 44 | GET | /offers/ | octo/offers |
| 45 | GET | /checkin/lookup | octo/checkin |
| 46 | POST | /checkin/checkin | octo/checkin |
| 47 | POST | /card-payments/ | octo/cardPayments |
| 48 | GET | /card-payments/{id} | octo/cardPayments |
| 49 | GET | /card-payments/lookup | octo/cardPayments |
| 50 | GET | /memberships/lookup | octo/memberships |
| 51 | POST | /identities/ | octo/identities |
| 52 | PATCH | /identities/{id} | octo/identities |
| 53 | DELETE | /identities/{id} | octo/identities |
| 54 | GET | /campaigns/ | octo/campaigns |
| 55 | POST | /notifications/ | octo/notifications |
| 56 | GET | /notifications/ | octo/notifications |
| 57 | DELETE | /notifications/{id} | octo/notifications |
| 58 | POST | /waitlists/ | octo/waitlists |

---

## Pflicht-Header für alle Endpunkte

```http
Authorization: Bearer {api_key}
Octo-Capabilities: {kommagetrennte Liste oder leer}
Content-Type: application/json  # nur bei POST, PATCH, DELETE
```

---

**Quellen:**
- Ventrata OCTO Skills: `octo-overview`, `octo-products`, `octo-availability`, `octo-bookings`,
  `octo-headers`, `octo-pricing`, `octo-content`, `octo-cart`, `octo-gift-vouchers`,
  `octo-redemption`, `octo-webhooks`, `octo-mappings`, `octo-offers`, `octo-online-check-in`,
  `octo-card-payments`, `octo-memberships`, `octo-identities`, `octo-campaigns`,
  `octo-notifications`, `octo-waitlists`
- https://docs.ventrata.com (Ventrata API-Dokumentation)
