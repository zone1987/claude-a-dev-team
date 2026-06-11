# SEO (Search Engine Optimization)

## Overview

Plugins can register custom SEO URL templates for their entities and extend robots.txt.

## Custom SEO URL Template

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Seo;

use FfContentPlus\Core\Content\FfContentPlusItemDefinition;
use Shopware\Core\Content\Seo\SeoUrlRoute\SeoUrlMapping;
use Shopware\Core\Content\Seo\SeoUrlRoute\SeoUrlRouteConfig;
use Shopware\Core\Content\Seo\SeoUrlRoute\SeoUrlRouteInterface;
use Shopware\Core\Framework\DataAbstractionLayer\Entity;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SalesChannel\SalesChannelEntity;

#[Package('custom-plugins')]
class FfContentPlusSeoUrlRoute implements SeoUrlRouteInterface
{
    final public const ROUTE_NAME = 'frontend.ff-content-plus.detail';
    final public const DEFAULT_TEMPLATE = '{{ item.translated.name }}';

    public function getConfig(): SeoUrlRouteConfig
    {
        return new SeoUrlRouteConfig(
            FfContentPlusItemDefinition::class,
            self::ROUTE_NAME,
            self::DEFAULT_TEMPLATE,
        );
    }

    public function prepareCriteria(
        Criteria $criteria,
        SalesChannelEntity $salesChannel,
    ): void {
        // Add filters/associations for data needed by the template
    }

    public function getMapping(
        Entity $entity,
        ?SalesChannelEntity $salesChannel,
    ): SeoUrlMapping {
        return new SeoUrlMapping(
            $entity,
            ['id' => $entity->getId()],
            ['item' => $entity],
        );
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Core\Content\Seo\FfContentPlusSeoUrlRoute">
    <argument type="service" id="FfContentPlus\Core\Content\FfContentPlusItemDefinition"/>
    <tag name="shopware.seo_url.route"/>
</service>
```

## SEO URL Template Variables

The template uses Twig syntax and has access to the entity and its translations:

```
{{ item.translated.name }}                    → my-product-name
{{ item.translated.name }}/{{ item.id }}      → my-product-name/abc123
content/{{ item.translated.name }}            → content/my-product-name
```

## Extending robots.txt

Subscribe to `RobotsTxtResolveEvent`:

```php
use Shopware\Storefront\Event\RobotsTxtResolveEvent;

class RobotsTxtSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            RobotsTxtResolveEvent::class => 'onRobotsTxtResolve',
        ];
    }

    public function onRobotsTxtResolve(RobotsTxtResolveEvent $event): void
    {
        $content = $event->getContent();
        $content .= "\nDisallow: /ff-content-plus/internal/*";
        $event->setContent($content);
    }
}
```

## Canonical URLs

Set canonical URLs in storefront controllers:

```php
use Shopware\Storefront\Page\GenericPageLoadedEvent;

public function onPageLoaded(GenericPageLoadedEvent $event): void
{
    $page = $event->getPage();
    $page->getMetaInformation()?->setCanonical($canonicalUrl);
}
```
