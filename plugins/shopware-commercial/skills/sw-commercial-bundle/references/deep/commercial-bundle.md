# Shopware Commercial Plugin — Bundle-Struktur

## Plugin-Aufbau

Das Commercial Plugin ist als Gruppe verschachtelter Sub-Bundles strukturiert.
Jede Funktion (z.B. Advanced Search, Subscriptions, B2B Components) ist ein eigenstaendiges Bundle
innerhalb des Commercial Plugins.

```
SwagCommercial (Root-Bundle)
├── AdvancedSearch
├── B2BComponents
├── Subscriptions
├── CustomPricing
└── ... (weitere Sub-Bundles)
```

## Bundle-Namen ermitteln

```bash
./bin/console debug:container --parameter kernel.bundles --format=json
```

Listet alle registrierten Bundles einschliesslich aller Commercial-Sub-Bundles.

## Selektives Bundle-Aktivieren

Seit Shopware 6.6.10.0 kann ueber eine Umgebungsvariable gesteuert werden,
welche Commercial-Bundles aktiv sind:

```bash
# Nur bestimmte Bundles aktivieren
SHOPWARE_COMMERCIAL_ENABLED_BUNDLES=CustomPricing,Subscription
```

Nicht aufgefuehrte Bundles werden deaktiviert, auch wenn das Commercial Plugin installiert ist.
Nuetzlich fuer Deployments, bei denen nur ein Subset der erworbenen Features benoetigt wird.

## Lizenzierung

### Lizenz automatisch laden

Beim Installieren versucht das Plugin, den Lizenzschluessel ueber den eingeloggten
Shopware Account zu laden. Schlaegt dies fehl, ist das Plugin installiert, aber alle
Features sind deaktiviert.

### Lizenz manuell aktualisieren

```bash
bin/console commercial:license:update
```

Laed den Lizenzschluessel erneut vom Shopware Account.

### Lizenzstatus pruefen

```bash
bin/console commercial:license:info
```

Zeigt:
- Aktuellen Lizenzschluessel (gesetzt/nicht gesetzt)
- Ablaufdatum der Lizenz
- Aktivierte Features

## CommercialBundle-Erweiterungsklassen

Sub-Bundles erben von der Basis-Bundle-Klasse des Commercial Plugins:

```php
class CommercialB2BBundle extends CommercialBundle
{
    public function getTemplatePriority(): int
    {
        return parent::getTemplatePriority() + 1;
    }

    public function build(ContainerBuilder $container): void
    {
        parent::build($container);
        // Eigene DI-Container-Konfiguration
    }
}
```

## Feature-Toggles pro Kunde (CustomerSpecificFeatureService)

Das Commercial Plugin bietet ein System fuer kunden-spezifische Feature-Freischaltungen,
primär im Kontext von B2B Components:

### PHP-Verwendung

```php
class MyService
{
    public function __construct(
        private readonly CustomerSpecificFeatureService $featureService
    ) {}

    public function doAction(CustomerEntity $customer, Context $context): void
    {
        if (!$this->featureService->isAllowed($customer, 'my_feature', $context)) {
            throw new AccessDeniedException();
        }
        // ...
    }
}
```

### Twig-Verwendung

```twig
{% if customerHasFeature('shopping_lists') %}
    <a href="{{ path('frontend.b2b.shopping-list.index') }}">Shopping Lists</a>
{% endif %}
```

### Verbuegbare Feature-Bezeichner

| Feature-Key             | Komponente            |
|-------------------------|-----------------------|
| `employee_management`   | Employee Management   |
| `quote_management`      | Quote Management      |
| `shopping_lists`        | Shopping Lists        |
| `individual_pricing`    | Individual Pricing    |
| `order_approval`        | Order Approval        |
| `budget_management`     | Budget Management     |
| `organization`          | Organization Units    |

## Plugin ohne Commercial Plugin verwenden (optionale Abhaengigkeit)

Wenn ein eigenes Plugin das Commercial Plugin optional abhaengig macht:

```php
// plugin base class
public function build(ContainerBuilder $container): void
{
    parent::build($container);

    if (!class_exists(CommercialBundle::class)) {
        return; // Commercial nicht installiert, nichts tun
    }

    // Commercial-spezifische Services laden
    $loader = new XmlFileLoader($container, new FileLocator($this->getPath() . '/Resources/config'));
    $loader->load('services_commercial.xml');
}
```

## Betreiber-Sicht

Fuer Shopware-Betreiber (Pläne, welche Features in welchem Plan enthalten sind):
Querverweis auf `shopware-merchant` Skill.
Aktivierung und Lizenz-Management: `sw-commercial-overview`.
