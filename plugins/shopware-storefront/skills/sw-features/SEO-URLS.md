# Shopware 6 — SEO URLs

Provide readable URLs for your own detail pages via an `AbstractSeoUrlRoute` plus a configurable SEO template.

```php
class FfExampleSeoUrlRoute extends AbstractSeoUrlRoute
{
    public const ROUTE_NAME = 'frontend.ff.example';
    public const DEFAULT_TEMPLATE = '{{ example.name }}';
    public function getConfig(): SeoUrlRouteConfig { /* entity + route + template */ }
    public function prepareCriteria(Criteria $criteria, SalesChannelEntity $sc): void { /* associations */ }
    public function getMapping(Entity $example, ?SalesChannelEntity $sc): SeoUrlMapping { /* infoPath + seoPathInfo vars */ }
}
```

Register it via the `shopware.seo_url.route` tag; generate URLs through the SeoUrlUpdater (on writes/indexer). In the template
use `{{ seoUrl('frontend.ff.example', {id: id}) }}`. Extend `robots.txt` with a subscriber on the robots event.

→ SEO details: [SEO.md](SEO.md)
