# Shopware 6 — cart line items

A cart position is a `LineItem`. Creating one goes through `LineItemFactoryRegistry`, adding it
through `CartService`. For a type of your own you write a custom LineItemHandler, which this page
covers too.

## Contents

- [Adding a line item](#adding-a-line-item)
- [The fields](#the-fields)
- [A custom line item type](#a-custom-line-item-type)
- [The processor that persists it](#the-processor-that-persists-it)
- [Nested line items](#nested-line-items)

## Adding a line item

Inject `Shopware\Core\Checkout\Cart\LineItemFactoryRegistry` and
`Shopware\Core\Checkout\Cart\SalesChannel\CartService`.

**In a controller the cart comes for free**: declare `Shopware\Core\Checkout\Cart\Cart` as a method
argument and the argument resolver fills it. Outside a controller, fetch it with
`CartService::getCart`.

```php
// <plugin root>/src/Service/ExampleController.php
#[Route(defaults: [PlatformRequest::ATTRIBUTE_ROUTE_SCOPE => [StorefrontRouteScope::ID]])]
class ExampleController extends StorefrontController
{
    public function __construct(
        private LineItemFactoryRegistry $factory,
        private CartService $cartService,
    ) {
    }

    #[Route(path: '/cartAdd', name: 'frontend.example', methods: ['GET'])]
    public function add(Cart $cart, SalesChannelContext $context): StorefrontResponse
    {
        $lineItem = $this->factory->create([
            'type' => LineItem::PRODUCT_LINE_ITEM_TYPE,   // results in 'product'
            'referencedId' => 'myExampleId',              // not a valid UUID — use a real id
            'quantity' => 5,
            'payload' => ['key' => 'value'],
        ], $context);

        $this->cartService->add($cart, $lineItem, $context);

        return $this->renderStorefront('@Storefront/storefront/base.html.twig');
    }
}
```

## The fields

`type` is mandatory. The four types available by default:

| Type | |
|---|---|
| `product` | a product position |
| `promotion` | a promotion |
| `credit` | a credit |
| `custom` | a custom position |

`LineItemFactoryRegistry` holds one handler per type. **An unsupported type throws
`Shopware\Core\Checkout\Cart\Exception\LineItemTypeNotSupportedException`.**

| Field | Meaning |
|---|---|
| `referencedId` | what the item points at — the product id, or for `promotion` the promotion id |
| `quantity` | how many to add |
| `payload` | any additional data your business logic needs; the chosen options of a configurable product are stored here |

The `payload` is the place for information you have to process later, in a processor or a template.
**For the complete list of accepted fields read `createValidatorDefinition` on
`LineItemFactoryRegistry`** — that method is the authoritative list.

## A custom line item type

For an entity of your own — a bundle, say — write a handler and it becomes a valid `type`.

Implement `Shopware\Core\Checkout\Cart\LineItemFactoryHandler\LineItemFactoryInterface`, which
requires three methods:

| Method | Contract |
|---|---|
| `supports` | takes a `$type` string, returns whether this handler handles it |
| `create` | builds the `LineItem`; set everything your type always needs. Called from `LineItemFactoryRegistry::create` |
| `update` | called from `LineItemFactoryRegistry::update`; decides which properties may be changed afterwards |

```php
// <plugin root>/src/Service/ExampleHandler.php
public function update(LineItem $lineItem, array $data, SalesChannelContext $context): void
{
    $lineItem->setReferencedId($data['referencedId']);
}
```

Register with the tag `shopware.cart.line_item.factory`:

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(ExampleHandler::class)
        ->tag('shopware.cart.line_item.factory');
};
```

## The processor that persists it

**A handler alone is not enough: without a processor the item is never persisted in the cart.**

```php
// <plugin root>/src/Core/Checkout/Cart/ExampleProcessor.php
public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                        SalesChannelContext $context, CartBehavior $behavior): void
{
    $lineItems = $original->getLineItems()->filterFlatByType(ExampleHandler::TYPE);

    foreach ($lineItems as $lineItem) {
        $toCalculate->add($lineItem);
    }
}
```

The processor takes the original cart and moves every item of its type into `$toCalculate`, which is
the cart that gets persisted. A processor can do far more than that — see `PROCESSOR.md`.

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(ExampleProcessor::class)
        ->tag('shopware.cart.processor', ['priority' => 4800]);
};
```

## Nested line items

Nested line items need their own processing logic, or an extension of Shopware's cart processors. A
plugin that reuses core line items can call the other processors to handle the nesting for it — see
`NESTED-LINE-ITEMS.md`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-items.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-items.html),
Shopware 6.7, retrieved 2026-08-21.
