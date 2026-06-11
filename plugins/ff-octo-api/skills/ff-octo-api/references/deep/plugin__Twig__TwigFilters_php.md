# TwigFilters (`src/Twig/TwigFilters.php`)

## Zweck
Twig-Extension, die den Filter `json_decode` bereitstellt (Storefront-Templates dekodieren JSON-Strings aus Session/Payload).

## Typ & Vererbung
- Namespace: `FfOctoApi\Twig`
- `class TwigFilters extends AbstractExtension`
- Registriert in `twig.xml`.

## Methoden
- `getFilters(): TwigFilter[]` → Filter `json_decode` → `jsonDecode`.
- `jsonDecode(mixed $value): mixed` — nur Strings; `@json_decode($value, true)`; sonst `null`.

## Verwendung (Twig)
`{{ jsonString|json_decode }}`, z.B. `app.request.session.get('octo-product-session-' ~ product.id)|json_decode`.

## Bezüge
`twig.xml`, `../twig-templates.md`. Die Funktion `ff_octo_listing_price` liegt NICHT hier, sondern in `TwigFunctions`.
