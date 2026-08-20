# Shopware 6 — Sitemap

Eigene Seiten in die XML-Sitemap aufnehmen über einen `AbstractUrlProvider`.

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

Registrierung via `shopware.sitemap.url_provider`-Tag. Sitemap wird per ScheduledTask/Command (`sitemap:generate`) gebaut.
Einträge entfernen/anpassen über den jeweiligen Provider bzw. Events.
