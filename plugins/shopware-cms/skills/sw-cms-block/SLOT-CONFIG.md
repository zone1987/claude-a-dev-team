# Shopware 6 — CMS slot and element config

Every element has a configuration (`defaultConfig` in the admin), available at runtime as a `FieldConfigCollection` on the slot.

```php
$config = $slot->getFieldConfig()->get('product');
$config->getValue();        // raw value
$config->getStringValue();  // typed
$config->isStatic();        // source 'static' (fixed value) vs. 'mapped' (from a mapping entity)
```

`defaultConfig` field: `{ source: 'static'|'mapped', value: ... }`. **static** = a fixed chosen value (e.g. a specific
product); **mapped** = mapped from the context (e.g. `product.name` on a product page). In the admin it is bound to
`element.config.<field>.value` via the `cms-element` mixin; evaluate it in the resolver (`sw-cms-data-resolver`),
and read it in the template as `element.config` (`sw-cms-element-storefront`).
