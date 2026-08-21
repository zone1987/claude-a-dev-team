# Shopware 6 — CMS DataResolver

Loads a CMS element's data server-side. Extends `AbstractCmsElementResolver` with `collect()` (which data to fetch)
and `enrich()` (attach the fetched data to the element).

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
