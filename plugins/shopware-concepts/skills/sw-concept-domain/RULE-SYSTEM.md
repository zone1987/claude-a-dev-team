# Shopware Rule-System — Konzept

Vollständige Konzept-Doku: `RULE-SYSTEM-DETAIL.md`

## Kurzüberblick

Das Rule-System beschreibt Business-Bedingungen als **komposable Regeln**, die gegen einen Kontext
(Cart, Order, Customer) ausgewertet werden. Wird eingesetzt in: Checkout, Promotionen, Flow Builder.

### Rule

- Einzelne Bedingung → `true` oder `false`
- Keine Seiteneffekte, keine Datenbeschaffung (pure function)
- Erhält alle Daten über **RuleScope**

### RuleScope (Kontext-Träger)

- `CheckoutRuleScope` — SalesChannelContext (Customer, Currency, etc.)
- `CartRuleScope` — Checkout + Cart-Daten
- `FlowRuleScope` — Checkout + Order-Daten
- `LineItemScope` — einzelnes Line Item

### Container Rules (Baumstruktur)

- `AndRule` — alle Kinder müssen matchen
- `OrRule` — mindestens ein Kind muss matchen
- `NotRule` — Kind darf nicht matchen
- Beliebig tief schachtelbar

### Evaluation-Lifecycle

1. Rule Builder → visuelle Konfiguration
2. Validierung via `RuleConstraints` und `RuleConfig`
3. Persistenz in DB (`rule` + `rule_condition` mit `parent_id`)
4. Laufzeit: `CartRuleLoader` baut Scope, filtert Kandidaten, iteriert bis stabil
5. ID-basiert (Zahlungsart-Availability) oder Direkt-Evaluation (Flow Builder)

Technische Umsetzung: `shopware-framework` (Dev-Plugin)
