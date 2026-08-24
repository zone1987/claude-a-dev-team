# Shopware 6 — CMS DataResolver

Loads a CMS element's data server-side. Extends `AbstractCmsElementResolver` with `collect()` (which data to fetch)
and `enrich()` (attach the fetched data to the element).

## Contents

- [collect: preparing the criteria](#collect-preparing-the-criteria)
- [enrich: attaching the data](#enrich-attaching-the-data)
- [Extending the resolution, and why a page event is too late](#extending-the-resolution-and-why-a-page-event-is-too-late)

```php
class FfTeaserResolver extends AbstractCmsElementResolver
{
    public function getType(): string { return 'ff-teaser'; }

    public function collect(CmsSlotEntity $slot, ResolverContext $ctx): ?CriteriaCollection
    {
        $config = $slot->getFieldConfig()->get('product');
        if (!$config || $config->getValue() === null) { return null; }
        $criteria = new Criteria([$config->getStringValue()]);
        $collection = new CriteriaCollection();
        $collection->add('product_' . $slot->getUniqueIdentifier(), ProductDefinition::class, $criteria);
        return $collection;
    }

    public function enrich(CmsSlotEntity $slot, ResolverContext $ctx, ElementDataCollection $result): void
    {
        $data = new ArrayStruct(); /* ... */ $slot->setData($data);
    }
}
```

Registered via the `shopware.cms.data_resolver` tag. `getType()` = the element name. `collect()` bundles criteria
(efficient, batched queries), `enrich()` calls `$slot->setData(...)` → available in the storefront as `element.data`.
Slot configuration: `sw-cms-slot-config`.

## collect: preparing the criteria

`collect()` builds the criteria object. Read the element's configuration through
`$slot->getFieldConfig()`, then reach the individual fields on it — the guide reads a
`myCustomMedia` field holding a `mediaId`. Where the field is empty, return `null` and nothing is
loaded.

Registration goes through the `shopware.cms.data_resolver` tag:

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(DailyMotionCmsElementResolver::class)
        ->tag('shopware.cms.data_resolver');
};
```

The `CriteriaCollection` key must be unique per slot, which is what
`$slot->getUniqueIdentifier()` is for:

```php
$criteriaCollection->add('media_' . $slot->getUniqueIdentifier(), MediaDefinition::class, $criteria);
```

**For an attribute entity there is no explicit definition class.** Pass the definition name as the
second argument instead — `'example_entity.definition'` in place of `MediaDefinition::class`.

## enrich: attaching the data

`enrich()` runs additional logic on what was resolved, with the same access to the configuration
fields. It is where an external API call belongs — the guide reads a `myCustomApiPayload` field,
passes it to a `MyCustomAPI` client (`$myCustomAPI->query($myCustomApiPayload)`), and hands the
response to the slot with `$slot->setData($response)`. In the storefront the result is available as
`element.data`.

## Extending the resolution, and why a page event is too late

**A CMS element is not live-bound to its entity.** During slot resolution a resolver *copies* values
out of the entity into the CMS structs — `ProductNameCmsElementResolver`, for example, takes `name`
off the product entity and writes it into the CMS text element. From then on the storefront renders
from the CMS structs, not from the entity.

The consequence is a trap worth knowing: **subscribing to `ProductPageLoadedEvent` and changing the
product there has no effect on the CMS output**, because the copy already happened. To change what a
CMS element displays, intervene inside the resolution pipeline instead.

Shopware publishes three extension points under `Shopware\Core\Content\Cms\Extension`, following
the extension-point pattern. Each is dispatched with `.pre` and `.post` suffixes — so
`cms-slots-data.resolve.pre` fires before that phase and `.post` after it.

| Extension class | Event name | What it intercepts |
|---|---|---|
| `CmsSlotsDataCollectExtension` | `cms-slots-data.collect` | the collection phase, where the criteria list is populated by each resolver |
| `CmsSlotsDataEnrichExtension` | `cms-slots-data.enrich` | the enrichment phase, where slots are populated from the search results |
| `CmsSlotsDataResolveExtension` | `cms-slots-data.resolve` | the whole resolution: collection plus enrichment |

To change entity data before it reaches the elements: subscribe to the resolve event, inspect the
`ResolverContext`, check the entity type, and modify it — the built-in resolvers then pick up the
modified entity.

```php
// namespace Swag\BasicExample\DataResolver;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

class CmsPreResolveSubscriber implements EventSubscriberInterface
{
public static function getSubscribedEvents(): array
{
    return [
        CmsSlotsDataResolveExtension::pre() => 'onCmsSlotsResolvePre',
    ];
}

public function onCmsSlotsResolvePre(CmsSlotsDataResolveExtension $event): void
{
    $resolverContext = $event->getResolverContext();
    $entity = $resolverContext->getEntity();

    if ($entity instanceof ProductEntity) {
        $entity->setName('New custom name');
    }
}
}
```

The resolver class itself sits under the plugin's own namespace — `Swag\BasicExample\DataResolver`
for `DailyMotionCmsElementResolver` in the guide.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/content/cms/add-data-to-cms-elements.html](https://developer.shopware.com/docs/guides/plugins/plugins/content/cms/add-data-to-cms-elements.html),
Shopware 6.7, retrieved 2026-08-21.
