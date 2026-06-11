---
name: sw-cms-slot-config
description: >
  Slot-/Element-Konfiguration in Shopware 6 CMS: FieldConfig/FieldConfigCollection, source 'static' vs. 'mapped',
  defaultConfig-Struktur, Werte im Resolver/Template lesen. Trigger: "FieldConfig cms", "slot config", "source static mapped",
  "element.config", "cms config field", "getFieldConfig". Shopware 6.7.
---

# Shopware 6 — CMS-Slot-/Element-Config

Jedes Element hat eine Konfiguration (`defaultConfig` im Admin), zur Laufzeit als `FieldConfigCollection` am Slot.

```php
$config = $slot->getFieldConfig()->get('product');
$config->getValue();        // roher Wert
$config->getStringValue();  // typisiert
$config->isStatic();        // source 'static' (fester Wert) vs. 'mapped' (aus Mapping-Entity)
```

`defaultConfig`-Feld: `{ source: 'static'|'mapped', value: ... }`. **static** = fest gewählter Wert (z.B. konkretes
Produkt); **mapped** = aus dem Kontext gemappt (z.B. `product.name` auf einer Produktseite). Im Admin via
`cms-element`-Mixin an `element.config.<feld>.value` gebunden; im Resolver (`sw-cms-data-resolver`) auswerten,
im Template als `element.config` (`sw-cms-element-storefront`).
