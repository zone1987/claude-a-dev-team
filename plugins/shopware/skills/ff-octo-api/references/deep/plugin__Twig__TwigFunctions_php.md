# TwigFunctions (`src/Twig/TwigFunctions.php`)

## Zweck
Twig-Extension mit der Funktion `ff_octo_listing_price`, die aus den API-Produktdaten den niedrigsten Anzeigepreis (EUR) für Listings/Produktkarten berechnet.

## Typ & Vererbung
- Namespace: `FfOctoApi\Twig`
- `class TwigFunctions extends AbstractExtension`
- Registriert in `twig.xml`.

## Konstruktor / DI
`PriceService $priceService`.

## Methoden
- `getFunctions(): TwigFunction[]` → `ff_octo_listing_price` → `getListingPrice`.
- `getListingPrice(?array $apiProduct): ?float`:
  - `null` bei null/keinen Units.
  - sammelt alle `options[].units[]`, `priceService->getLowestPriceFrom($units)`.
  - `retail <= 0` → `null` (kein „Ab 0,00 €"). Sonst `retail / 10^precision`.

## Besonderheiten / Fallstricke
- Liefert bewusst `null` bei `retail <= 0` (0,00-€-Schutz) — Template muss den null-Fall behandeln.
- Genutzt in `component/product/card/price-unit.html.twig`.

## Bezüge
`Service/PriceService.php`, `Resources/views/storefront/component/product/card/price-unit.html.twig`, `twig.xml`, `../twig-templates.md`.
