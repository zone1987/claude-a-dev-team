# ProductSaveSubscriber (`src/Subscriber/ProductSaveSubscriber.php`)

## Zweck
Aktualisiert die Preise eines OCTO-Produkts automatisch, wenn das Produkt gespeichert wird. Nutzt einen Rekursionsschutz, um die durch das Preis-Update ausgelöste erneute Speicherung nicht endlos zu wiederholen.

## Typ & Vererbung
- Namespace: `FfOctoApi\Subscriber`
- `class ProductSaveSubscriber implements EventSubscriberInterface`
- Registriert in `subscribers.xml`.

## Konstruktor / DI
`PriceService $priceService`, `EntityRepository $productRepository`.

## Abonnierte Events
- `ProductEvents::PRODUCT_WRITTEN_EVENT` → `onProductSave`.

## Methoden
### `onProductSave(EntityWrittenEvent $event)`
- **Rekursionsschutz:** wenn Context Extension `octo_price_update` hat → return.
- Pro geschriebener ID: lädt Produkt (+`ffOctoProduct`); bei Variante den Parent stattdessen.
- Wenn `ffOctoProduct` vorhanden: klont Context, fügt Extension `octo_price_update` (`ArrayEntity`) hinzu, ruft `priceService->updatePrices(productId, identifier, null, context)`.

## Besonderheiten / Fallstricke
- **Rekursionsschutz** ist essenziell — das Preis-Update schreibt das Produkt erneut; ohne die Context-Extension Endlosschleife.
- Variantenspeicherung triggert Parent-Preisberechnung.

## Bezüge
`Service/PriceService.php`, `subscribers.xml`, `../price-calculation.md`.
