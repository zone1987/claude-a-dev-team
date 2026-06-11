# ProductExtension (`src/Extension/Content/Product/ProductExtension.php`)

## Zweck
DAL-EntityExtension, die das Shopware-`product` um die Verknüpfung zur `ff_octo_product`-Entity erweitert (FK + Association). Grundlage für `product.extensions.ffOctoProduct` und `extensions.foreignKeys.ffOctoProductId`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Extension\Content\Product`
- `class ProductExtension extends EntityExtension`
- Registriert in `extensions.xml` (Tag `shopware.entity.extension`).

## Methoden
### `extendFields(FieldCollection $collection): void`
Fügt hinzu:
- `FkField('ff_octo_product_id', 'ffOctoProductId', OctoProductDefinition)` mit Flags `ApiAware`, `Inherited`, `CascadeDelete`.
- `ManyToOneAssociationField('ffOctoProduct', 'ff_octo_product_id', OctoProductDefinition, 'id')` mit Flags `ApiAware`, `Extension`, `Inherited`, `CascadeDelete`.

### `getDefinitionClass(): string`
`ProductDefinition::class`.

### `getEntityName(): string`
`ProductDefinition::ENTITY_NAME` (`product`).

## Besonderheiten
- **`Inherited`:** Varianten erben die `ffOctoProduct`-Zuordnung vom Parent.
- **`CascadeDelete`:** Löschen des Produkts entfernt die Zuordnung (Orphan-Cleanup zusätzlich via `ProductDeleteSubscriber`).
- Twig-Erkennung: `product.extensions.foreignKeys.ffOctoProductId != null`.

## Bezüge
`OctoProductDefinition`, `Subscriber/ProductDeleteSubscriber.php`, `Migration/Migration1757686022CreateProductExtension.php`, `extensions.xml`, `../database-entities.md`.
