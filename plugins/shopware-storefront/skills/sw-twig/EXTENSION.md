# Shopware 6 — Twig extension

Add custom Twig functions/filters through an `AbstractExtension` class, registered with the `twig.extension` tag.

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

Usage in the template: `{{ price|ff_money }}`. Inject services via the constructor. For the built-in Storefront functions
(`sw_icon`, `seoUrl`, `searchMedia` …) see `sw-twig-functions`. Keep heavy logic out of the filter — move it into a service.
