---
name: sw-concept-checkout
description: >
  Shopware Checkout-Konzept: Cart (Struktur, Zustände, Berechnung), Orders (State Machines),
  Payments (Synchron/Asynchron, Handler). Trigger: "Cart Konzept", "wie funktioniert der Warenkorb",
  "Shopware Cart", "Order State Machine", "Payment Handler", "wie wird eine Bestellung abgewickelt",
  "checkout flow shopware", "cart calculation", "line items", "cart enrichment",
  "Bestellstatus", "Zahlungsstatus", "Lieferstatus", "asynchronous payment shopware",
  "synchronous payment", "CartService", "wie funktioniert Zahlung in Shopware".
---

# Shopware Checkout — Konzept

Vollständige Konzept-Doku: `references/deep/checkout.md`

## Kurzüberblick

### Cart

- **Nicht über DAL** — Cart wird als Ganzes gespeichert/geladen (kein EntityRepository)
- **Zustände**: Empty → Dirty (nach Änderung) → Calculated
- **Berechnung** (4 Phasen): Enrich → Process → Validate → Persist
- **Line Items** — stackable, removable; können andere Line Items enthalten (Bundles)
- **Enrichment** — Produkte, Promotionen, Versandkosten werden lazy geladen
- **Rule-Validierung** — iterativ bis stabil (z.B. Produkt kaufen → Sonnenbrille gratis → Rabatt)
- **CartService** — zentrales Facade für alle Cart-Operationen

### Orders

- **Denormalisiert** — alle Daten werden zum Bestellzeitpunkt persistiert (kein Catalog-Abhängigkeit)
- **Drei State Machines**: Order, Order Transaction (Zahlung), Order Delivery (Versand)
- **Workflow-optimiert** — nur definierte Zustandsübergänge erlaubt

### Payments

- **Synchron** — direktes Feedback vom Gateway
- **Asynchron** — Redirect-Flow; Callback URL `/payment/finalize-transaction`
- **Payment Handler** — zentraler Erweiterungspunkt; registriert in Datenbank

Technische Umsetzung: `shopware-checkout` (Dev-Plugin)
