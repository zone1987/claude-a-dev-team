---
name: sw-seo-urls
description: >
  SEO-URLs in Shopware 6: eigene SeoUrlRoute (AbstractSeoUrlRoute) + Template, SEO-URLs generieren/aktualisieren,
  seoUrl() im Twig, robots.txt erweitern. Trigger: "SEO URL", "SeoUrlRoute", "seoUrl twig", "eigene SEO-URL",
  "AbstractSeoUrlRoute", "robots.txt erweitern", "sprechende URL". Shopware 6.7.
---

# Shopware 6 — SEO-URLs

Für eigene Detailseiten sprechende URLs über eine `AbstractSeoUrlRoute` + konfigurierbares SEO-Template bereitstellen.

```php
class FfExampleSeoUrlRoute extends AbstractSeoUrlRoute
{
    public const ROUTE_NAME = 'frontend.ff.example';
    public const DEFAULT_TEMPLATE = '{{ example.name }}';
    public function getConfig(): SeoUrlRouteConfig { /* Entity + Route + Template */ }
    public function prepareCriteria(Criteria $criteria, SalesChannelEntity $sc): void { /* Associations */ }
    public function getMapping(Entity $example, ?SalesChannelEntity $sc): SeoUrlMapping { /* infoPath + seoPathInfo-Vars */ }
}
```

Registrierung via `shopware.seo_url.route`-Tag; generieren über den SeoUrlUpdater (bei Writes/Indexer). Im Template
`{{ seoUrl('frontend.ff.example', {id: id}) }}`. `robots.txt` per Subscriber auf das Robots-Event erweitern.

→ SEO-Details: [references/seo.md](references/seo.md)
