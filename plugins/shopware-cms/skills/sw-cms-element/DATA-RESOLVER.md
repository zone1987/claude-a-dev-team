# Shopware 6 — CMS-DataResolver

Lädt serverseitig die Daten eines CMS-Elements. Erweitert `AbstractCmsElementResolver` mit `collect()` (welche Daten
nachladen) und `enrich()` (geladene Daten ans Element hängen).

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

Registrierung via `shopware.cms.data_resolver`-Tag. `getType()` = Element-Name. `collect()` bündelt Criteria
(performant, gebündelte Queries), `enrich()` setzt `$slot->setData(...)` → im Storefront als `element.data`.
Slot-Konfiguration: `sw-cms-slot-config`.
