# Shopware Checkout — Vollständige Konzept-Doku

Quellen: `concepts/commerce/checkout-concept/index.md`, `cart.md`, `orders.md`, `payments.md`

---

## Checkout-Überblick (index.md)

Der Checkout umfasst alle Schritte zum Kauf von Artikeln im Shop.
Kernprozess: **Cart → Order → Payment → Shipping**.

---

## Cart (cart.md)

### Design-Ziele

- **Adaptability** — viele Services für einfache Cart-Nutzung; Cart kann für viele Use Cases angepasst werden
- **Performance** — minimale Berechnungen, Queries und Iterationen; klares State Management
- **Abstraction** — wenige harte Abhängigkeiten auf Core-Entities; Entities via Interfaces referenziert

### Cart Struct (`\Shopware\Core\Checkout\Cart\Cart`)

Eine Instanz = ein Cart. Identifikation nur via Token-Hash (kein User/Customer-Bezug direkt im Struct).
Ermöglicht mehrere Carts pro User, pro Sales Channel, oder kanalübergreifend.

**Enthält:**
- **Line Items** — Bestellpositionen (Produkte, Bundles, Rabatte, Surcharges)
  - Eigenschaften: `stackable` (Menge änderbar), `removable` (via API entfernbar)
  - Können andere Line Items enthalten (Bundles)
  - Haupterweiterungspunkt für Cart-Prozess
- **Transaction** — Zahlungsinformation (Payment Handler + Betrag)
- **Delivery** — Lieferung (Datum, Methode, Zieladresse, Positionen)
- **Error** — Validierungsfehler die Bestellen verhindern
- **Tax** — berechneter Steuersatz
- **Price** — Gesamtpreis (inkl./exkl. MwSt., Versand, Rabatte)

### Cart-Zustände

```
Empty → (add line item) → Dirty → (calculate) → Calculated
Calculated → (modify) → Dirty
Calculated → (order invalid) → Calculated
Calculated → (order) → [done]
```

| Zustand | Beschreibung |
|---|---|
| Empty | Kein Item; Standard-Versand/-Zahlung |
| Dirty | Nach Änderung; ungültige Preise, rohe Line Items, ungewisse Liefergültigkeit |
| Calculated | Nach Berechnung; kann als Bestellung aufgegeben oder enthält Fehler |

### Berechnung (4 Phasen)

```
[*] → Enrich → Process → Validate → Persist → [*]
                           ↑___↓ (wiederholen bis stabil)
```

| Phase | Aufgabe |
|---|---|
| **Enrich** | Bilder, Beschreibungen, Preise für Line Items laden |
| **Process** | Preise aktualisieren, Versand/Zahlung anpassen, Summen berechnen |
| **Validate** | Rule-System prüfen; Cart-Änderungen basierend auf Plausibilitätsprüfungen |
| **Persist** | Storage aktualisieren |

### Cart Enrichment

**Collectors** (`CartDataCollectorInterface`) laden Daten lazy:

| Service | Aufgabe |
|---|---|
| `ProductCartProcessor` | Alle referenzierten Produkte anreichern |
| `CartPromotionsCollector` | Promotionen hinzufügen, entfernen, validieren |
| `ShippingMethodPriceCollector` | Versandpreise |

Ablauf: `collect` (alle Collector) → `enrich` (alle Collector)

### Context Rules und Iteration

Nach Verarbeitung wird Cart gegen Rule-System validiert → mögliche Cart-Änderungen → Re-Validierung.

Beispiel-Szenario (Auto kaufen → Sonnenbrille gratis → 2%-Rabatt):
1. Iteration 1: Auto im Cart → Sonnenbrille automatisch hinzugefügt
2. Iteration 2: 2 Produkte im Cart → 2%-Rabatt hinzugefügt
3. Ergebnis: Auto + Sonnenbrille + 2%-Rabatt → stabil

### Cart Storage

- **Nicht** über DAL verwaltet — Cart wird als Ganzes geschrieben/gelesen
- `CartService` (`\Shopware\Core\Checkout\Cart\SalesChannel\CartService`) — zentrales Facade

---

## Orders (orders.md)

### Design-Ziele

#### Denormalisierung

- Order hängt **nicht** vom Katalog oder Produkten ab
- Alle Line-Item-Daten + berechnete Preise werden beim Bestellen persistiert
- Neuberechnung nur via expliziten API-Aufruf

#### Workflow-abhängig

- Zustandsänderungen erfolgen in definierter, vorhersehbarer und konfigurierbarer Weise
- Nur erlaubte Zustandsübergänge sind möglich

### State Machines (3 Stück)

**Order State Machine:**
```
[*] → Open
Open → In Progress (process)
Open → Cancelled (cancel)
In Progress → Cancelled (cancel)
In Progress → Done (complete)
Cancelled → Open (reopen)
Done → Open (reopen)
```

**Order Transaction State Machine (Zahlung):**
Zustände: Open, In Progress, Authorized, Unconfirmed, Paid, Paid partially,
Reminded, Refunded, Refunded partially, Cancelled, Failed, Chargeback

**Order Delivery State Machine (Versand):**
Zustände: Open, Shipped, Shipped partially, Returned, Returned partially, Cancelled

---

## Payments (payments.md)

### Payment Flow (2 essentielle Schritte)

1. **Bestellung aufgeben** (Place Order)
2. **Zahlung bearbeiten** (Handle Payment)

### Schritte im Detail

#### 1. Zahlungsmethode wählen
- Gespeichert im User Context (`/store-api/context`)

#### 2. Bestellung aufgeben
- Erstellt Bestellung basierend auf aktuellem Context + Cart
- Shopware erstellt Bestellung + offene Transaktion (Placeholder für Zahlung)
- Transaktion enthält: einzige ID, Zahlungsmethode, Gesamtbetrag

#### 2.1 Zahlung vorbereiten (optional)
- Manche Integrationen erstellen Zahlungsreservierung / Autorisierung hier
- Nicht standardisiert durch Shopware

#### 3. Zahlung verarbeiten (Handle Payment)
- Startet Zahlung; bestimmt korrekten Payment Handler

#### 3.1 Payment Handler Typen

| Typ | Beschreibung |
|---|---|
| **Synchron** | Direkte API-Anfrage an Gateway; sofortige Rückmeldung |
| **Asynchron** | Benutzer-Redirect; Redirect-URL enthält Transaktions-Infos + Callback-URL |

Headless: Shopware gibt Redirect-URL in API-Response zurück.
Default Storefront: Redirect erfolgt automatisch.

#### 3.2 Zahlungsausführung am Gateway (nur asynchron)
- Benutzer führt finale Prüfungen/Autorisierungen auf Gateway-UI durch
- Gateway redirectet zu Callback-URL mit Zahlungsergebnis

#### 3.3 Zahlung finalisieren (nur asynchron)
- Getriggert via Callback-URL → `/payment/finalize-transaction`
- Shopware aktualisiert Transaktionsstatus
- Redirect zum entsprechenden Finish-Page

### Hinweise

- Session **nicht** in Headless-Payment-Integrationen verwenden
- Keine Logik in Controllers; Store-API-Routen für Headless hinzufügen
- Spezifische Implementierungsdetails unterscheiden sich je Provider
