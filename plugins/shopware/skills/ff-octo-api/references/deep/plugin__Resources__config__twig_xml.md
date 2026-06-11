# twig.xml (`src/Resources/config/twig.xml`)

## Zweck
Registriert die beiden Twig-Extensions.

## Definierte Services
- `FfOctoApi\Twig\TwigFilters` — Tag `twig.extension` (Filter `json_decode`).
- `FfOctoApi\Twig\TwigFunctions` — Argument `PriceService`, Tag `twig.extension` (Funktion `ff_octo_listing_price`).

## Bezüge
`Twig/TwigFilters.php`, `Twig/TwigFunctions.php`.
