# Individual Pricing — Entwickler-Referenz

**Verfuegbar ab Shopware 6.7.8.0**

## Konzept

Individual Pricing ermoeglicht Haendlern, katalogweite Rabatte und Sonderpreise fuer B2B-Kunden
zu definieren — auf Basis von Firmen, Organisationseinheiten, Mitarbeitern oder Tags.

## Preistypen (actionType)

| Typ              | Beschreibung                                  |
|------------------|-----------------------------------------------|
| `by_percent`     | Prozentualer Abzug (z.B. 10% Rabatt)          |
| `by_fixed`       | Fixer Abzug (z.B. 5 EUR Rabatt)               |
| `to_fixed`       | Festpreis (z.B. genau 99,99 EUR)              |
| `volume_pricing` | Staffelpreise nach Menge                      |

## Entitaeten

```sql
b2b_components_individual_pricing:
  id, active, show_strike_through, name, target (companies|tags),
  priority (INT), apply_to_all_products (BOOL), product_stream_id (FK),
  use_validity_range (BOOL), valid_from, valid_until,
  description, action_type, action_amount,
  created_by_id, updated_by_id, custom_fields

b2b_components_individual_pricing_tier:
  id, individual_pricing_id (FK), qty_from (INT), qty_to (INT, NULL = unbegrenzt), price (JSON)

b2b_components_individual_pricing_company_assignment:
  id, individual_pricing_id (FK), customer_id (FK),
  scope (whole_company|all_org_units|specific_units), organization_unit_ids (JSON)

b2b_components_individual_pricing_computed_cache:
  id, individual_pricing_id (FK), product_id (FK, NULL = alle Produkte)

b2b_components_individual_pricing_tag:
  individual_pricing_id (FK), tag_id (FK)
```

## Preis-Workflow (Runtime)

**Phase 1: Context-Erstellung** — `AudienceContextResolver` bestimmt Kundentyp
(Business Partner, Employee, Tag-basierter Kunde)

**Phase 2: Produkt-Laden** — `IndividualPricingProductSubscriber` wird bei Produktlade-Event ausgeloest

**Phase 3: Preisaufloesung** — computed cache wird abgefragt, Regeln nach Prioritaet gefiltert

**Phase 4: Preisanwendung** — Einzelpreise oder Volumenpreise werden angewendet, optional
mit Strike-through des Originalpreises

### Priorisierungslogik

1. Nur Regeln hoechster Prioritaet werden ausgewertet
2. Bei mehreren passenden Regeln gleicher Prioritaet: Regel mit niedrigstem Preis gewinnt
3. Keine Regel passt → Standard-Katalogpreis

### Prioritaetshierarchie gesamt

1. Individual Pricing (hoechste Prioritaet, wenn anwendbar)
2. Shopware Custom Pricing
3. Produkt-Staffelpreise/Advanced Prices
4. Regel-basierte Preise
5. Standard-Listenpreis

## Caching-Strategie

**Hybrid-Ansatz:**
- Spezifische Produkte: Pre-computed Cache-Eintraege pro Produkt-Regel-Paar (sofortige Suche)
- Alle Produkte: Single NULL-Eintrag pro Regel (schnelle Suche + Runtime-Berechnung)

Cache wird automatisch ueber Message Queue (asynchron) aktualisiert, in Batches von 1.000 Produkten.

**Hinweis:** Nach Erstellen/Aendern von Preisregeln mit spezifischen Produkten:
Wartezeit bis Queue verarbeitet ist, bevor Preise sichtbar werden.
Regeln mit "Alle Produkte" wirken sofort (Runtime).

## HTTP-Cache-Verhalten

| Kundentyp                    | Cachebar     | Grund                                      |
|------------------------------|--------------|--------------------------------------------|
| Tag-basiert                  | Ja (shared)  | Gleiche Tags → gleiche Preise              |
| Org.-Einheit-Mitarbeiter     | Ja (shared)  | Gleiche Abteilung → gleiche Preise         |
| Business Partner             | Nein         | Kundenspezifische Preise                   |
| Mitarbeiter ohne Org.-Einheit| Nein         | Individuell                                |

## Bekannte Einschraenkungen

Preisfilterung und -sortierung in Produktlisten basiert auf indizierten Originalpreisen.
Individual Pricing wird **nach** Datenbankabfragen angewendet → Preissortierung/-filterung
kann inkorrekte Ergebnisse zeigen.

**Workaround:** Preissortierung und Preisbereichs-Filterung werden in der Storefront automatisch
deaktiviert, wenn Individual Pricing fuer den eingeloggten Kunden aktiv ist.

## Erweiterungspunkte

### Extension: `IndividualPricingApplyExtension`

Hook beim Anwenden des Preises (Validation, Logging, Trigger externer Systeme):

```php
class IndividualPricingLogger implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [IndividualPricingApplyExtension::NAME => 'onPricingApply'];
    }

    public function onPricingApply(IndividualPricingApplyExtension $extension): void
    {
        // $extension->product, $extension->individualPricing, $extension->context
        $this->logger->info('Individual pricing applied', [
            'product_id' => $extension->product->getId(),
            'rule_id' => $extension->individualPricing->getIndividualPricingId(),
        ]);
    }
}
```

### Events

| Event                                       | Zweck                                       |
|---------------------------------------------|---------------------------------------------|
| `IndividualPricingIndexerEvent`             | Reagieren auf Indexierungsanfragen          |
| `IndividualPricingLookupCriteriaEvent`      | Criteria fuer Einzelprodukt-Lookup anpassen |
| `IndividualPricingLookupBatchCriteriaEvent` | Criteria fuer Batch-Lookup anpassen         |

### Messages (asynchron)

| Message                                         | Zweck                                          |
|-------------------------------------------------|------------------------------------------------|
| `IndividualPricingCacheEntryUpdaterMessage`     | Cache bei Regelaenderungen neu aufbauen        |
| `IndividualPricingBuildCacheSingleRuleMessage`  | Cache fuer einzelne Regel neu aufbauen         |

## Voraussetzungen

- Employee Management + Organization Unit muessen installiert und aktiviert sein
- Ab Shopware 6.7.8.0
