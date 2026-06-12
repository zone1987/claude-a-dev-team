# OctoCartCollector (`src/Core/Checkout/Cart/OctoCartCollector.php`)

## Zweck
Cart-Processor, der die Preisberechnung für OCTO-Produkte im Warenkorb **überschreibt**: setzt für LineItems mit `isOctoProduct`-Payload den Preis aus den (Session-)Units, korrigiert Labels für Default-Varianten und entfernt fehlerhafte Items. Stellt sicher, dass der Cart-Preis dem in der Verfügbarkeitsprüfung ermittelten Preis entspricht.

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Checkout\Cart`
- `readonly class OctoCartCollector implements CartProcessorInterface`
- Registriert in `checkout.xml` mit Tag `shopware.cart.processor` (+ `cart.collector`); die **Priority** wird dort gesetzt (laut Skill ~6000) — nicht in der Klasse.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$requestStack` | `RequestStack` | Zugriff auf Session des aktuellen Requests. |
| `$priceDefinitionFactory` | `PriceDefinitionFactory` | Erzeugt `QuantityPriceDefinition`. |
| `$logger` | `OctoLoggerInterface` | Logging. |

## Methoden
### `collect(CartDataCollection, Cart, SalesChannelContext, CartBehavior): void`
Leer (keine Vorab-Datensammlung nötig).

### `process(CartDataCollection, Cart $original, Cart $toCalculate, SalesChannelContext, CartBehavior): void`
- Filtert Produkt-LineItems; pro Item mit Payload `isOctoProduct`:
  - **Default-Varianten-Label:** wenn `isDefaultVariant` + `label.parent` → setzt Label auf Parent, filtert die Parent-Option aus `options`.
  - Holt `units` aus Payload; berechnet `uniqueOctoProductId` (`getUniqueLineItemId`); lädt Session-Item dazu.
  - Wenn Session-Daten vorhanden: Units neu aus Session (`quantity>0`), setzt Payload `availability`.
  - Berechnet `unitPrice = Σ(unit.price.retail × quantity)`, `totalPrice = unitPrice`.
  - Baut `QuantityPriceDefinition` (über `getPriceDefinition`) mit `taxRate` aus Payload, setzt `CalculatedPrice` + `PriceDefinition`.
  - **Bei Exception:** entfernt das LineItem aus `$original` + loggt (defensiv: kaputte Items fliegen raus).

### `private getPriceDefinition(price, quantity, taxRate, context): PriceDefinitionInterface`
Baut `QuantityPriceDefinition` (percentage 100, isCalculated true, eine TaxRule) via Factory.

### `private getSession(request): SessionInterface`
Wirft `LogicException` wenn Sessions deaktiviert.

### `private getSessionItem(name): mixed`
`@json_decode` des Session-Werts des aktuellen Requests; `null` + warning bei Fehlen.

### `private getUniqueLineItemId(referenceId, units): string`
`id_qQty`-String + `Uuid::fromStringToHex`. **Ohne** `quantity>0`-Filter (wie `CartController`, anders als `AvailbilityController`).

## Besonderheiten / Fallstricke
- **Preis-Quelle:** ausschließlich `unit.price.retail` × quantity — ist `retail` 0 (z.B. fehlgeschlagene Availability/Offline-Fallback), wird der Cart-Preis 0 → „0,00 € nie ok"-Regel relevant.
- **`getUniqueLineItemId`-Duplikat** (3. Vorkommen, identisch zu `CartController`). Logikänderung dreifach nachziehen.
- Defensives Entfernen kaputter Items kann „verschwindende" Warenkorbpositionen verursachen → Logs prüfen.
- `readonly` Klasse; Session-Zugriff über `RequestStack` (nicht injizierte Session).

## Bezüge
`Controller/CartController.php`, `Controller/AvailbilityController.php`, `Service/PriceService.php`, `checkout.xml`, `../price-calculation.md`.
