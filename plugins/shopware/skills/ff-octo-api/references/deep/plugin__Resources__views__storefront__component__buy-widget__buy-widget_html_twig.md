# buy-widget.html.twig (`src/Resources/views/storefront/component/buy-widget/buy-widget.html.twig`)

## Zweck
Override des Core-Buy-Widgets für OCTO-Produkte: bindet den OCTO-Configurator ein, ersetzt Preis-/Tax-/Buy-Form-Blöcke (für OCTO-Produkte deaktiviert/ersetzt, sonst Original).

## Typ
- `{% sw_extends '@Storefront/storefront/component/buy-widget/buy-widget.html.twig' %}`

## Überschriebene Blöcke
- `buy_widget_configurator_include` — bei Parent-Produkt + Configurator-Settings: Wrapper `.product-detail-configurator-container` (+ `is-default-variant`) + `sw_include` Core-Configurator.
- `buy_widget_price` — bei OCTO-Produkt: nur JSON-LD-`<meta itemprop="price">` aus `ff_octo_listing_price` (wenn >0); sonst `parent()`.
- `buy_widget_tax` — bei OCTO-Produkt: leer; sonst `parent()`.
- `buy_widget_buy_form` — bei OCTO-Produkt + `product.active`: leer (Buy-Form kommt aus dem Configurator); sonst `parent()`.

## Besonderheiten / Fallstricke
- **Override-Konflikt:** FfLondonTheme überschreibt dasselbe Core-Template (andere Blöcke: Wishlist/RichSnippets/Ordernumber). Ohne `getDepends()` ist die Ladereihenfolge undefiniert → eines kann verloren gehen. Siehe Frontend-Agent.
- OCTO-Erkennung: `product.extensions.foreignKeys.ffOctoProductId != null`.

## Bezüge
`configurator.html.twig`, `Twig/TwigFunctions.php` (`ff_octo_listing_price`), FfLondonTheme `buy-widget.html.twig`, `../twig-templates.md`.
