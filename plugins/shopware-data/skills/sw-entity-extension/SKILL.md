---
name: sw-entity-extension
description: >
  Bestehende Core-Entities in Shopware 6 erweitern: EntityExtension mit extendFields(), zusätzliche Felder/
  Associations zu product/order/customer etc. ohne Core-Änderung. Trigger: "EntityExtension", "Core-Entity erweitern",
  "Feld zu product hinzufügen", "extendFields", "getDefinitionClass extension", "association zu order". Shopware 6.7.
  Scaffolder: /sw-entity-extension.
---

# Shopware 6 — Entity-Extension

Um einer Core-Entity (oder fremden Entity) Felder/Associations hinzuzufügen, OHNE deren Definition zu ändern.

```php
class ProductExtension extends EntityExtension
{
    public function getDefinitionClass(): string { return ProductDefinition::class; }

    public function extendFields(FieldCollection $collection): void
    {
        $collection->add(
            (new OneToManyAssociationField('ffNotes', FfNoteDefinition::class, 'product_id'))
                ->addFlags(new ApiAware(), new CascadeDelete())
        );
    }
}
```

Registrierung via `shopware.entity.extension`-Tag. Eigene Spalten erfordern eine Migration. Zusätzliche
einfache Felder gehen oft einfacher über **CustomFields** (`sw-custom-fields`) — Extension für echte Associations/Logik.

→ Gerüst: [examples/EntityExtension.php](examples/EntityExtension.php)
