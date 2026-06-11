# ProductDetailSubscriber (`src/Subscriber/ProductDetailSubscriber.php`)

## Zweck
Erweitert die Criteria der Storefront-Produktdetailseite, damit `ffOctoProduct` und die Options/Property-Gruppen mitgeladen werden (für die Buy-Widget-Darstellung).

## Typ & Vererbung
- Namespace: `FfOctoApi\Subscriber`
- `class ProductDetailSubscriber implements EventSubscriberInterface`
- Registriert in `subscribers.xml`.

## Abonnierte Events
- `ProductPageCriteriaEvent::class` → `onProductPageCriteria`.

## Methoden
### `onProductPageCriteria(ProductPageCriteriaEvent $event)`
Fügt Assoziationen hinzu: `ffOctoProduct`, `options.group.options`.

## Bezüge
`Extension/Content/Product/ProductExtension.php`, Twig `buy-widget/*`, `subscribers.xml`.
