# PriceService (`src/Service/PriceService.php`)

## Zweck
Zentrale Preislogik: berechnet aus den OCTO-API-/Offline-Produktdaten die Shopware-Preise für Parent + Varianten (Lowest-Price je Option), rechnet Fremdwährung (v.a. GBP) in EUR um und zieht die Provision ab. Beinhaltet den RheinKurier-/Offline-Fallback, der den 0,00-€-Bug verhindert. **Hotspot.**

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `class PriceService`

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$currencies` | array | Map `ISO` → Currency-Factor (im Konstruktor aus `currencyRepository` geladen/gecacht). |

## Konstruktor / DI
`OctoLoggerInterface $logger`, `EntityRepository $productRepository`, `EntityRepository $currencyRepository`, `OctoApiClientRegistry $clientRegistry`, `PropertyService $propertyService`, `SystemConfigService $systemConfigService`. Lädt alle Währungen (ISO→Factor).

## Methoden
### `updatePrices(productId, identifier, ?apiProduct=null, ?context=null): void`
- Lädt Produkt; lädt `apiProduct` nach (`getApiProductBySwProduct`), wenn nicht übergeben.
- **`$hasUsableTopLevelId = !empty(apiProduct['id']) && !empty(apiProduct['reference'])`** — entscheidet Mapping-Pfad.
  - Mit Top-Level-ID: `getApiProductOptions` (deterministisches Property-Group-Option-Mapping) → `getApiProductOptionUnits`.
  - **Ohne (Offline/RheinKurier):** `getAllUnitsFlat` → alle Units flach, jede Variante bekommt den Attraktions-Lowest-Price (verhindert 0,00 €).
- `lowestAttractionPrice = getLowestPriceFrom(units)`.
- Parent-Preis via `getProductPrice`. Pro Child: option-spezifischen Lowest-Price ermitteln; Fallback = Attraktions-Lowest-Price (statt 0,00 €). Upsert aller Preise.
- Exception → warning (bei Code `Level::Warning`) oder error.

### `private getAllUnitsFlat(apiProduct): array`
Sammelt alle `options[].units[]` flach (Offline-Fallback).

### `getLowestPrice(units): array` (public)
Filtert Begleit-/CHILD/INFANT-Units raus, nimmt `unit['price']`. **`array_values()`-Reindex** (Units kommen mit String-Keys aus dem AvailbilityController — ohne Reindex „Ab 0,00 €"). Filtert `net != 0` (**loose compare**, damit float 0.0 als „kein Preis" gilt — `feedback_zero_price_never_ok`), sortiert aufsteigend, gibt günstigsten zurück (Fallback erster Unit-Preis).

### `getLowestPriceFrom(units): array` (public)
Wie oben, aber Preise via `getUnitPrices` (aus `pricingFrom`).

### `private getUnitPrices(units): array`
Pro Unit: nimmt `pricingFrom` mit `currency==GBP` (sonst erstes), rechnet `original/retail/net` nach EUR um (`currencyToEur`), Currency `EUR`.

### `private currencyToEur(pricing, key): float`
`factor = currencies[currency] ?? 1`; `price * (1/factor)` gerundet (int). Wirft Exception bei fehlendem Key.

### `private getApiProductOptionUnits(options): array`
Flacht `options[].units`.

### `private getApiProductOptions(apiProduct, identifier): array`
Map `propertyGroupOptionId → apiOption`; ID via `propertyService->getPropertyGroupOptionId(apiProductId, option.id)`, wobei `apiProductId = Uuid::fromStringToHex("{id}-{reference}-{identifier}")`.

### `private getProductById(productId, ?context): ?ProductEntity`
Criteria mit Assoziationen `children`, `ffOctoProduct`, `properties.options`, `options`, `configuratorSettings.option`, `customFields`; `considerInheritance(true)`.

### `private getApiProductBySwProduct(product): array`
Wirft Warning-Exception ohne `ffOctoProduct`. **Offline:** nutzt persistierte `ffOctoProduct.product` (DB) statt API-Call (Offline liefert `[]`). Sonst Capabilities setzen + `client->getProduct(uuid)`.

### `getProductPrice(product, lowestPrice): array` (public)
Rechnet `gross/net` aus `retail/net / 10^currencyPrecision`. Provision (`getProvision`): wenn >0, `net = round(gross - gross/100*provision, 2)`. Baut `price` (gross/net = gross!) + `purchasePrices` (net). 

### `getConvertedExchangePrice(pricing): array` (public)
`retail` nach EUR umgerechnet / `10^currencyPrecision`, Currency EUR (genutzt vom AvailbilityController).

### Provision
- `getProvision(product)`: produktspezifisch überschreibt global.
- `getProductProvision(product)`: Custom Field `rk_product_provision_value`.
- `getMainProvision()`: Config `FfOctoApi.config.provisionValue`.

## Besonderheiten / Fallstricke
- **0,00 € niemals gültig** — mehrere bewusste Maßnahmen (loose compare, array_values-Reindex, Offline-Fallback). Beim Anfassen NICHT entfernen.
- **Currency-Factor-Richtung:** `currencies[ISO]` ist der Shopware-Factor (EUR-Basis); Umrechnung nutzt den Kehrwert.
- `getProductPrice` setzt im `price`-Block `net = gross` (brutto), den eigentlichen Netto-/Einkaufspreis in `purchasePrices` — bewusst, nicht „verwechselt".
- Mapping bricht ohne `apiProduct['id']`+`reference` → Offline-Fallback greift.

## Bezüge
`PropertyService`, `OctoApiClientRegistry`, `OctoProductEntity`, `Controller/PriceController.php`, `Core/Checkout/Cart/OctoCartCollector.php`, `Command/PriceUpdateCommand.php`, `../price-calculation.md`, `../appserver-integration.md`.
