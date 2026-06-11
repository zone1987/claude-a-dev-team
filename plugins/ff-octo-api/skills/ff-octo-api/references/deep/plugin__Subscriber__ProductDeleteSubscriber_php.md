# ProductDeleteSubscriber (`src/Subscriber/ProductDeleteSubscriber.php`)

## Zweck
Räumt verwaiste `ff_octo_product`-Datensätze auf, wenn die zugehörigen Shopware-Produkte gelöscht werden (Orphan-Cleanup). `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Subscriber`
- `class ProductDeleteSubscriber implements EventSubscriberInterface`
- Registriert in `subscribers.xml`.

## Konstruktor / DI
`Connection $connection` (DBAL), `EntityRepository $octoProductRepository`.

## Abonnierte Events
- `EntityDeleteEvent::class` → `onEntityDelete`.

## Methoden
### `onEntityDelete(EntityDeleteEvent $event)`
- Holt zu löschende `product`-IDs; sammelt **vor** der Löschung die zugehörigen `ff_octo_product_id`s (`getOctoProductIds`); registriert `addSuccess`-Callback, der die OctoProducts **nach** erfolgreicher Produktlöschung löscht.

### `private getOctoProductIds(productIds): array`
Raw-SQL: `SELECT LOWER(HEX(ff_octo_product_id)) FROM product WHERE id IN (:ids) AND ff_octo_product_id IS NOT NULL` (Binary-IDs).

## Besonderheiten
- Bewusste Reihenfolge: IDs vor Delete sammeln, OctoProduct nach Erfolg löschen (kein FK-Konflikt).
- Ergänzt die `CascadeDelete`-Flags der `ProductExtension`.

## Bezüge
`Extension/Content/Product/ProductExtension.php`, `OctoProductDefinition`, `subscribers.xml`.
