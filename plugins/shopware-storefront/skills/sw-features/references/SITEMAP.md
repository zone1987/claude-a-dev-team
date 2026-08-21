# Shopware 6 — Sitemap

Add your own pages to the XML sitemap via an `AbstractUrlProvider`.

```php
class FfExampleUrlProvider extends AbstractUrlProvider
{
    public function getName(): string { return 'ffExample'; }
    public function getUrls(SalesChannelContext $context, int $limit, ?int $offset = null): UrlResult
    {
        $urls = [];
        foreach ($this->loadIds($limit, $offset) as $id) {
            $u = new Url(); $u->setLoc($this->seoUrl(...))->setLastmod(new \DateTime())->setChangefreq('weekly');
            $urls[] = $u;
        }
        return new UrlResult($urls, $nextOffset);
    }
}
```

Register it via the `shopware.sitemap.url_provider` tag. The sitemap is built by a scheduled task/command (`sitemap:generate`).
Remove or adjust entries through the respective provider or through events.
