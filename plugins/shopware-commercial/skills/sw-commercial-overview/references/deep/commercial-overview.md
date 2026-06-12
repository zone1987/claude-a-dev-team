# Shopware Commercial Plugin — Entwickler-Referenz

## Uberblick

Das Shopware 6 Commercial Plugin ist eine Gruppe von verschachtelten Sub-Bundles, die erweiterte
Funktionalitaet fuer B2B und Enterprise-Shopbetreiber bereitstellt. Es umfasst u.a.:

- Advanced Search (Elasticsearch/OpenSearch-basiert)
- B2B Components (Employee Management, Quotes, Order Approval, Shopping Lists, Individual Pricing, Organization Unit)
- Subscriptions (Abonnement-Produkte)
- B2B Suite (Legacy, bis SW 6.8 unterstuetzt)
- Migration Assistant (Datenmigration aus SW5, SW6, Magento)

## Plugin-Struktur

Das Commercial Plugin ist als Gruppe von Sub-Bundles aufgebaut (Konzept: Shopware Plugins).
Jedes Feature ist ein eigenstaendiges Bundle. Betreiber-Konfiguration aktiviert/deaktiviert
Features gemaess Lizenz.

## Lizenzierung

Bei Installation versucht das Plugin den Lizenzschluessel ueber den eingeloggten Shopware-Account
zu holen. Ohne Schluessel bleibt das Plugin installiert, aber alle Features sind deaktiviert.

```bash
# Lizenzschluessel aktualisieren
bin/console commercial:license:update

# Lizenzstatus pruefen
bin/console commercial:license:info
```

## Bundles selektiv aktivieren

Seit Commercial 6.6.10.0 koennen einzelne Bundles ueber die Umgebungsvariable gesteuert werden:

```env
SHOPWARE_COMMERCIAL_ENABLED_BUNDLES=CustomPricing,Subscription
```

Alle verfuegbaren Bundle-Namen ermitteln:

```bash
./bin/console debug:container --parameter kernel.bundles --format=json
```

## Plaene

| Plan    | Features (Auszug)                          |
|---------|--------------------------------------------|
| Rise    | Basisfeatures                              |
| Evolve  | Advanced Search, B2B Components            |
| Beyond  | Vollstaendige Commercial-Suite             |

## Installation

Keine Sonderbehandlung erforderlich — identisch mit Standard-Plugin-Installation:
`bin/console plugin:install --activate SwagCommercial`

## Wichtig fuer Entwickler

- Jedes Commercial-Bundle kann in einer Plugin-Erweiterung optional abhaengig sein (conditional loading).
- Bei Entwicklung gegen Commercial-Features: Immer pruefen ob das jeweilige Bundle lizenziert und aktiv ist.
- Betreiber-Sicht (Admin-UI, Merchant-Doku): siehe `shopware-merchant`.
