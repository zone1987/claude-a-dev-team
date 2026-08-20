# Shopware Frontends — @shopware/helpers

Reine Utility-Funktionen (kein State) für wiederkehrende Aufgaben in headless Frontends:

- **Übersetzungen**: `getTranslatedProperty(entity, 'name')` — liefert den übersetzten Wert (translated-Array).
- **Preise/Währung**: Format-Helfer für Brutto/Netto/Listenpreis, Währungssymbol.
- **URLs/SEO**: `getProductRoute`/`getCategoryRoute`, `buildUrlPrefix` (Sprach-Präfix) für SEO-Pfade.
- **Media/Thumbnails**: passendes Thumbnail/`srcset` aus einer Media-Entity wählen.
- **Cart**: Hilfsfunktionen für LineItem-Berechnungen/Anzeige.

```ts
import { getTranslatedProperty, getProductRoute } from '@shopware/helpers';
const name = getTranslatedProperty(product, 'name');
const to = getProductRoute(product);
```

Ergänzt die Composables (`sw-composables`); für API-Aufrufe `sw-api-client-js`. Funktionen sind tree-shakeable
einzeln importierbar.

→ Vollständige Referenz: [FRONTENDS-HELPERS-HELPERS-REFERENCE.md](FRONTENDS-HELPERS-HELPERS-REFERENCE.md)
