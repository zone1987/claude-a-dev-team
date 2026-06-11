# Database-Entities & Schema

## Tabelle: ff_octo_product

```sql
CREATE TABLE `ff_octo_product` (
    `id`          BINARY(16)    NOT NULL,
    `uuid`        VARCHAR(36)   NOT NULL,        -- API Product UUID (unique)
    `identifier`  VARCHAR(50)   NOT NULL,        -- Supplier: goldentours, gocity, ...
    `product`     JSON          DEFAULT (JSON_ARRAY()),  -- Komplettes API-Produkt
    `created_at`  DATETIME(3)   NOT NULL,
    `updated_at`  DATETIME(3)   NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uniq_uuid` (`uuid`),
    INDEX `idx_identifier` (`identifier`),
    INDEX `idx_identifier_uuid` (`identifier`, `uuid`),
    INDEX `idx_created_at` (`created_at`),
    CHECK (JSON_VALID(`product`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Product-Tabellen-Erweiterung

```sql
-- Migration1757686022CreateProductExtension
ALTER TABLE `product` ADD COLUMN `ff_octo_product_id` BINARY(16) NULL;
ALTER TABLE `product` ADD CONSTRAINT `fk.product.ff_octo_product_id`
    FOREIGN KEY (`ff_octo_product_id`) REFERENCES `ff_octo_product` (`id`)
    ON DELETE CASCADE;
```

Zusätzlich wird die Shopware-Vererbung (Inheritance) für das Feld registriert.

---

## Entity-Definition

### OctoProductDefinition

**Datei:** `src/Core/Content/OctoProduct/OctoProductDefinition.php`

```php
class OctoProductDefinition extends EntityDefinition
{
    public const ENTITY_NAME = 'ff_octo_product';

    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new IdField('id', 'id'))->addFlags(new PrimaryKey(), new Required(), new ApiAware()),
            (new StringField('uuid', 'uuid'))->addFlags(new Required(), new ApiAware()),
            (new StringField('identifier', 'identifier'))->addFlags(new Required(), new ApiAware()),
            (new JsonField('product', 'product'))->addFlags(new ApiAware()),
        ]);
    }
}
```

### OctoProductEntity

**Datei:** `src/Core/Content/OctoProduct/OctoProductEntity.php`

```php
class OctoProductEntity extends Entity
{
    use EntityIdTrait;

    protected ?string $uuid = null;
    protected ?string $identifier = null;
    protected array $product = [];

    // Getter/Setter für alle Felder
}
```

### OctoProductCollection

Standard-Shopware-Collection ohne eigene Methoden.

---

## Product Extension

**Datei:** `src/Extension/Content/Product/ProductExtension.php`

```php
class ProductExtension extends EntityExtension
{
    public function extendFields(FieldCollection $collection): void
    {
        $collection->add(
            (new FkField('ff_octo_product_id', 'ffOctoProductId', OctoProductDefinition::class))
                ->addFlags(new ApiAware(), new Inherited(), new CascadeDelete())
        );

        $collection->add(
            (new ManyToOneAssociationField('ffOctoProduct', 'ff_octo_product_id', OctoProductDefinition::class))
                ->addFlags(new ApiAware(), new Extension(), new Inherited(), new CascadeDelete())
        );
    }

    public function getDefinitionClass(): string
    {
        return ProductDefinition::class;
    }
}
```

---

## Zugriff auf OCTO-Daten

### PHP

```php
// Extension laden
$product->getExtension('ffOctoProduct');            // OctoProductEntity|null
$product->get('ffOctoProductId');                    // Binary(16) UUID

// OctoProduct-Daten
$octoProduct = $product->getExtension('ffOctoProduct');
$octoProduct->getUuid();          // API UUID
$octoProduct->getIdentifier();    // 'goldentours', 'gocity', etc.
$octoProduct->getProduct();       // Komplettes API-Produkt als Array
```

### Twig

```twig
{# Prüfung ob OCTO-Produkt #}
{% if product.extensions.foreignKeys.ffOctoProductId is not null %}

{# Extension-Objekt #}
{% set octoProduct = product.getExtension('ffOctoProduct') %}
{{ octoProduct.uuid }}
{{ octoProduct.identifier }}
{{ octoProduct.product|json_encode }}
```

### Admin (JavaScript)

```javascript
// Criteria mit Association
const criteria = new Criteria();
criteria.addAssociation('ffOctoProduct');

// Zugriff
this.product.ffOctoProduct?.uuid;
this.product.ffOctoProduct?.identifier;
this.product.ffOctoProduct?.product;
```

---

## Migrationen

### Migration1755686022CreateOctoProductTable

**Timestamp:** 1755686022
- Erstellt `ff_octo_product` Tabelle
- Erstellt Unique-Index auf `uuid`

### Migration1757686022CreateProductExtension

**Timestamp:** 1757686022
- Nutzt `InheritanceUpdaterTrait`
- Fügt `ff_octo_product_id` Spalte zur `product` Tabelle hinzu
- Registriert Vererbung für das FK-Feld und die Assoziation

### Migration1768988700AddOctoProductIdentifierIndex

**Timestamp:** 1768988700
- Erstellt Index `idx_identifier` auf `identifier`-Spalte
- Erstellt Composite-Index `idx_identifier_uuid` auf `identifier` + `uuid`

---

## Deinstallation

**Datei:** `src/FfOctoApi.php`

```php
public function uninstall(UninstallContext $uninstallContext): void
{
    if ($uninstallContext->keepUserData()) {
        return;
    }

    // 1. Foreign Keys entfernen
    // 2. Tabellen-Vererbung entfernen
    // 3. ff_octo_product Tabelle löschen
}
```

Nutzt `DatabaseTrait` für:
- `removeInheritance()` — Entfernt Spalte und Vererbungs-Registrierung
- `dropTable()` — Löscht die Tabelle

---

## API-Produkt JSON-Struktur (Beispiel)

```json
{
    "id": "api-product-uuid",
    "internalName": "Tower of London",
    "title": "Tower of London Tickets",
    "reference": "tower-of-london",
    "description": "...",
    "availabilityType": "START_TIME",
    "defaultCurrency": "GBP",
    "availableCurrencies": ["GBP", "EUR"],
    "options": [
        {
            "id": "option-uuid",
            "internalName": "Standard Entry",
            "reference": "standard-entry",
            "default": true,
            "units": [
                {
                    "id": "unit-uuid",
                    "internalName": "Adult",
                    "type": "ADULT",
                    "restrictions": {
                        "minAge": 16,
                        "maxAge": null,
                        "paxCount": 1,
                        "accompaniedBy": []
                    },
                    "pricing": [
                        {
                            "original": 3300,
                            "retail": 2800,
                            "net": 2300,
                            "currency": "GBP",
                            "currencyPrecision": 2
                        },
                        {
                            "original": 3800,
                            "retail": 3200,
                            "net": 2700,
                            "currency": "EUR",
                            "currencyPrecision": 2
                        }
                    ]
                }
            ]
        }
    ],
    "pricingFrom": [
        { "retail": 2800, "currency": "GBP", "currencyPrecision": 2 }
    ]
}
```

**Unit-Typen:** ADULT, YOUTH, CHILD, INFANT, FAMILY, SENIOR, STUDENT, OTHER
