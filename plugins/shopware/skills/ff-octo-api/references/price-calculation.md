# Preisberechnung

## Zwei Systeme

Das Plugin hat zwei verschiedene Preisberechnungsmechanismen:

1. **Statisch (PriceService)** — Shopware-Produktpreise aktualisieren (für Listenansicht, Suche, etc.)
2. **Dynamisch (OctoCartCollector)** — Echtzeitpreise im Warenkorb basierend auf gewählten Units

---

## 1. Statische Preisberechnung (PriceService)

**Datei:** `src/Service/PriceService.php`

### Wann werden Preise aktualisiert?

| Auslöser | Handler/Service |
|----------|----------------|
| Scheduled Task (alle 3h) | `OctoApiPriceUpdaterHandler` → `PriceService::updatePrices()` |
| Produkt gespeichert | `ProductSaveSubscriber` → `PriceService::updatePrices()` |
| Admin-Button | `PriceController::updateProductPrices()` → `PriceService::updatePrices()` |

### PriceService::updatePrices()

```php
public function updatePrices(
    string $productId,
    string $identifier,
    ?array $apiProduct = null,
    ?Context $context = null
): void
```

#### Ablauf:

1. **Produkt laden** mit: children, ffOctoProduct, properties, configuratorSettings
2. **API-Produkt laden** (wenn nicht übergeben): `client->getProduct(uuid)`
3. **Optionen mappen:**
   ```php
   // Deterministische UUIDs für Property Groups
   $propertyGroupOptionId = Uuid::fromStringToHex("{apiProductId}-{reference}-{identifier}-property-group-option");
   ```
4. **Units sammeln** aus allen Optionen
5. **Niedrigsten Preis finden:**
   ```php
   // NUR Units OHNE accompaniedBy-Einschränkung
   // Nach Netto-Preis sortieren
   // Niedrigsten mit Preis > 0 nehmen
   ```
6. **Preise schreiben:**
   - **Hauptprodukt:** Niedrigster Preis aller Optionen
   - **Varianten:** Niedrigster Preis der jeweiligen Option

### Währungsumrechnung

```php
private function getUnitPrices(array $apiProductOptionUnits): array
```

**Präferenz:** GBP wird bevorzugt, wenn vorhanden.

**Umrechnung GBP → EUR:**
```php
// Shopware Währungsfaktor für GBP: z.B. 0.8744
// Umrechnung: preis × (1 / faktor)
// Beispiel: 2500 (= £25.00) × (1 / 0.8744) = 2859 (= €28.59)
$euroPrice = $price * (1 / $gbpFactor);
```

Die Währungsfaktoren werden aus der Shopware-Datenbank geladen:
```php
$this->currencies = []; // ISO code => factor
// z.B. ['GBP' => 0.8744, 'EUR' => 1.0, 'USD' => 1.0833]
```

### Minor Units

API-Preise sind in **Minor Units** (Cent):
```
2500 mit currencyPrecision: 2 = 25.00 EUR/GBP
44900 mit currencyPrecision: 2 = 449.00 SEK
```

**Division:** `price / pow(10, currencyPrecision)`

### Provisionsabzug

```php
private function getProvision(ProductEntity $product): float
{
    // 1. Produkt-spezifisch (Custom Field)
    $productProvision = $this->getProductProvision($product);
    // Custom Field: rk_product_provision_value
    
    // 2. Global (Plugin-Config)
    $mainProvision = $this->getMainProvision();
    // Config: FfOctoApi.config.provisionValue (default 10%)
    
    return $productProvision > 0 ? $productProvision : $mainProvision;
}
```

**Provision wird NUR vom Netto abgezogen:**
```php
$net = $net - ($net / 100 * $provision);
```

### Preis-Array-Struktur

```php
public function getProductPrice(ProductEntity $product, array $lowestPrice): array
{
    return [
        [
            'currencyId' => $this->getCurrencyIdByIso('EUR'),
            'gross' => $retailPrice / pow(10, $currencyPrecision),  // Brutto = Retail
            'net' => $netPrice,     // Netto nach Provision
            'linked' => false,      // Brutto ≠ Netto
        ]
    ];
}
```

**Shopware-Felder:**
- `price` = Retail-Preis (Brutto = Verkaufspreis)
- `purchasePrices` = Netto-Preis nach Provision (Einkaufspreis)

### Rekursionsschutz

```php
// ProductSaveSubscriber
if ($event->getContext()->hasExtension('octo_price_update')) {
    return; // Verhindert Endlosschleife
}
$event->getContext()->addExtension('octo_price_update', new ArrayStruct());
```

---

## 2. Dynamische Preisberechnung (OctoCartCollector)

**Datei:** `src/Core/Checkout/Cart/OctoCartCollector.php`
**Priority:** 6000

### Wann berechnet?

Bei **jeder** Cart-Neuberechnung (Seite laden, Item hinzufügen/entfernen, etc.)

### OctoCartCollector::process()

```php
foreach ($toCalculate->getLineItems()->filterType(LineItem::PRODUCT_LINE_ITEM_TYPE) as $lineItem) {
    if ($lineItem->getPayloadValue('isOctoProduct') !== true) continue;
    
    // 1. Session laden
    $uniqueId = $this->getUniqueLineItemId($lineItem->getReferencedId(), $units);
    $sessionItem = $this->getSessionItem($uniqueId);
    
    // 2. Preis berechnen
    $price = 0;
    foreach ($sessionItem['units'] as $unit) {
        $price += $unit['price']['retail'] * $unit['quantity'];
    }
    
    // 3. Shopware-Preis überschreiben
    $definition = $this->getPriceDefinition($price, 1, $taxRate, $context);
    $lineItem->setPriceDefinition($definition);
    // → QuantityPriceDefinition mit absolutem Preis
}
```

### Preise in der Availability-Response

Preise werden bereits in Phase 2 (Verfügbarkeitsprüfung) konvertiert und in der Session gespeichert:

```php
// In AvailbilityController
$retailPrice = $availability['unitPricing'][$unitIndex]['retail'];
$convertedPrice = $this->priceService->getConvertedExchangePrice($pricing);
// → EUR-Preis / pow(10, currencyPrecision)
```

---

## 3. Offline-Client-Preise (RheinKurier)

Für Offline-Clients werden Preise aus dem gespeicherten `pricingFrom`-Feld extrahiert:

```php
// In AvailbilityController::getAvailability()
if ($client->isOffline()) {
    $pricingFrom = $apiProduct['product']['pricingFrom'] ?? [];
    // Generiert Fake-Availability mit diesen Preisen
}
```

---

## Zusammenfassung: Preisfluss

```
API-Produkt (GBP/EUR Minor Units)
  ↓
Währungsumrechnung (GBP → EUR via Shopware-Faktoren)
  ↓
Division durch 10^currencyPrecision (Cent → Euro)
  ↓
┌─────────────────────────┬──────────────────────────┐
│ Statisch (PriceService) │ Dynamisch (CartCollector) │
├─────────────────────────┼──────────────────────────┤
│ Niedrigster Preis       │ Σ(retail × quantity)     │
│ aller Units             │ der gewählten Units      │
│ Provisionsabzug (Netto) │ Kein Provisionsabzug     │
│ → Shopware product.price│ → Cart CalculatedPrice   │
└─────────────────────────┴──────────────────────────┘
```