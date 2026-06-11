---
name: sw-twig-extension
description: >
  Eine eigene Twig-Extension in Shopware 6 registrieren (AbstractExtension): Functions/Filters für Storefront-Templates,
  Service-Tag twig.extension. Trigger: "Twig Extension", "eigener Twig-Filter", "AbstractExtension twig",
  "twig.extension tag", "getFunctions getFilters", "custom twig filter". Shopware 6.7.
---

# Shopware 6 — Twig-Extension

Eigene Twig-Funktionen/-Filter über eine `AbstractExtension`-Klasse, registriert mit `twig.extension`-Tag.

```php
class FfTwigExtension extends AbstractExtension
{
    public function getFilters(): array
    {
        return [ new TwigFilter('ff_money', [$this, 'formatMoney']) ];
    }
    public function formatMoney(float $value): string { return number_format($value, 2, ',', '.') . ' €'; }
}
```

Nutzung im Template: `{{ price|ff_money }}`. Services per Constructor injizieren. Für eingebaute Storefront-Funktionen
(`sw_icon`, `seoUrl`, `searchMedia` …) siehe `sw-twig-functions`. Keine schwere Logik im Filter — in Service auslagern.
