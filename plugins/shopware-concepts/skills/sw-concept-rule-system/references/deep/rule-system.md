# Shopware Rule-System — Vollständige Konzept-Doku

Quellen: `concepts/framework/rule-system/index.md`, `rule-concepts.md`, `rule-evaluation.md`

---

## Rule-System Überblick (index.md)

Generisches System zur Beschreibung von Business-Bedingungen als **komposable Regeln**.
Ausgewertet gegen spezifischen Kontext (Cart, Order, Customer).

**Rule Builder** = Administration-Feature für visuelle Konfiguration und Kombination von Regeln.

### Einsatzbereiche

- **Checkout / Cart** — Availability und Verhalten von Versand-/Zahlungsmethoden, Produktpreisen
- **Promotionen** — Anwenden/Einschränken basierend auf Customer, Cart-Inhalt, anderen Kriterien
- **Flow Builder** — Regel-Bedingungen für Flows

### Beispiel-Szenario

"Wenn Kunde ein Auto kauft, bekommt er eine Sonnenbrille gratis im selben Auftrag."

Rule-System sitzt zwischen Cart-Zustand (Auto ist im Cart) und gewünschter Aktion
(Sonnenbrille ist gratis), ohne diese Logik direkt in den Cart zu embedden.

---

## Rule Concepts (rule-concepts.md)

### Rule

- Einzelne Bedingung → `true` oder `false`
- Beantwortet spezifische Fragen: "Gehört Kunde zur Standardgruppe?", "Ist Cart > 50€?"
- **Keine Datenbeschaffung** — erhält alle Daten via RuleScope
- **Keine Seiteneffekte** — ändert nichts an Cart, Orders oder anderen States (pure function)

### RuleScope (Kontext-Träger)

Definiert Kontext für Regelauswertung und stellt Daten bereit.

| Scope | Inhalt |
|---|---|
| `CheckoutRuleScope` | SalesChannelContext (Customer, Sales Channel, Currency, etc.) |
| `CartRuleScope` | CheckoutRuleScope + Cart-Daten |
| `FlowRuleScope` | Checkout-Infos + Order-Daten |
| `LineItemScope` | Einzelnes Line Item |

Regeln hängen nur von dem ab, was der Scope exponiert → wiederverwendbar über Features hinweg.

### Container Rules (Baumstruktur)

Kombinieren Ergebnisse anderer Regeln via logische Operatoren. Keine eigene Bedingungsauswertung.

| Container | Bedeutung |
|---|---|
| `AndRule` | Alle Kinder müssen matchen |
| `OrRule` | Mindestens ein Kind muss matchen |
| `NotRule` | Dieses Kind darf nicht matchen |

Vollständige Regeldefinition = **Baum** aus Container-Knoten (AND/OR/NOT) und Blatt-Knoten
(konkrete Bedingungen).

Beispiel-Baum:
```
OrRule
├── LineItemsInCartCountRule (operator: ">=", count: 40)
└── GoodsPriceRule (operator: ">=", amount: 500)
```

### Operatoren und Vergleiche

- Gleichheit/Ungleichheit: `=`, `!=`
- Bereiche: `<`, `<=`, `>`, `>=`
- Leer-Prüfungen: `empty`

Konsistente Semantik via `RuleComparison` für vergleichbare Werttypen.

### Rule Config (UI-Vertrag)

`RuleConfig` definiert, welche Felder und Operatoren in der Admin-UI angezeigt werden:

- **Operator-Set** — welche Operatoren sind für diese Regel gültig
- **Field Definitions** — `name` (Identifier), `type` (UI-Darstellung: number/text/date), zusätzliche Config
  (Optionen für Select-Felder, Einheit für Zahlenfelder)

### Rule Constraints (Validierung)

`RuleConstraints` beschreiben, was eine valide Konfiguration für eine Regel ist.

- **Value Constraints** — Felder müssen bestimmte Typen/Werte haben (nicht leer, numerisch, etc.)
- **Operator Constraints** — nur bestimmte Operatoren erlaubt

---

## Rule Evaluation (rule-evaluation.md)

### Lifecycle Überblick

```
Rule Builder → Validation → Database → Runtime scope → Match / Evaluate
```

1. Rule Builder lässt User Regelbaum erstellen (Container + Bedingungen)
2. Rule-System validiert jede Bedingung gegen entsprechende Rule-Klasse im Registry
3. Valide Regeln werden in DB persistiert
4. Zur Laufzeit: Domain baut passenden RuleScope, berechnet matchende Regeln
5. Features filtern nach Rule-IDs im Context oder evaluieren Regelbaum direkt

### 1. Von Rule Builder zu gespeicherter Regeldefinition

**Datenbankstruktur:**
- `rule` — repräsentiert die gesamte Regel
- `rule_condition` — Container-Knoten und Blatt-Bedingungen
  - `parent_id` — für Baumstruktur
  - `type` — mappt auf Rule-Klasse
  - `value` — JSON mit konfiguriertem Werten (Operator, Schwellwerte, IDs)

**Validierung**: `RuleValidator` subscribt auf Write-Events und prüft `RuleConditionEntity`:
- Typ → Rule-Klasse via `RuleConditionRegistry` auflösen
- Constraints der Rule-Klasse prüfen
- Ungültige Payloads werden abgelehnt

### 2. Evaluation vorbereiten

**Scope Owners** (wer baut welchen Scope):

- **Cart/Checkout**: `CartRuleLoader` — Haupt-Einstiegspunkt; baut Scopes und evaluiert Regeln
- **Flows**: `FlowRuleScopeBuilder` — baut `FlowRuleScope`; rekonstruiert Cart-ähnlichen Kontext aus Order
- **Line Items**: `AnyRuleLineItemMatcher` — baut `LineItemScope` für Einzelzeilen-Tests

Regeln sind **pure functions** — abhängig nur von übergebenem Scope, kein globaler State.

### 3. Matching Rules (Checkout)

**Iterativer Prozess** (bei Checkout):

```
Load candidate rules
→ Build scope from cart
→ Filter matching rules (RuleCollection::filterMatchingRules)
→ Cart changed? → Recalculate cart → (wiederholen)
→ Expose matching rule IDs on SalesChannelContext
```

Ergebnis: konsistentes Paar (Cart, matching Rule IDs).

### 4. Rules zur Laufzeit nutzen

#### ID-basierte Entscheidungen (Performance-Pfad)

Entities wie `shipping_method`, `payment_method`, `tax_provider` haben `availability_rule_id`.
Erlaubt wenn Rule ID in `SalesChannelContext::getRuleIds()` → kein Direktaufruf nötig.

#### Direkte Evaluation (Flexibilitäts-Pfad)

Features holen Regelbaum aus DB, bauen entsprechenden Scope, rufen `Rule::match(RuleScope $scope)` auf.

Delegation bei Container Rules:
```
Feature → OrRule::match(scope)
OrRule → Rule1::match(scope) → false
OrRule → Rule2::match(scope) → false
OrRule → Feature: false
```
