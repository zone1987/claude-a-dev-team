# OctoProductEntity (`src/Core/Content/OctoProduct/OctoProductEntity.php`)

## Zweck
Entity-Klasse zu `ff_octo_product`. Hält die Supplier-Produktdaten als typisierte Properties.

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Content\OctoProduct`
- `class OctoProductEntity extends Entity`, nutzt `EntityIdTrait`.

## Properties
| Property | Typ | Default | Bedeutung |
|----------|-----|---------|-----------|
| `$uuid` | ?string | null | API-Produkt-UUID. |
| `$identifier` | ?string | null | Supplier-Name. |
| `$product` | array | `[]` | Vollständige API-Produktdaten. |

## Methoden
Getter/Setter (fluent): `getUuid()/setUuid()`, `getIdentifier()/setIdentifier()`, `getProduct()/setProduct()`.

## Besonderheiten
- Über `ProductExtension` als `ffOctoProduct`-Association am Shopware-Produkt verfügbar (`$product->getExtension('ffOctoProduct')`).

## Bezüge
`OctoProductDefinition`, `OctoProductCollection`, `Extension/Content/Product/ProductExtension.php`.
