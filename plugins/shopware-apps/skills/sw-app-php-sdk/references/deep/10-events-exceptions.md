# PHP SDK — PSR-14 Events & Exceptions

## Events

All events reside in `Shopware\App\SDK\Event\`.

### AbstractAppLifecycleEvent (base)

```php
__construct(RequestInterface $request, ShopInterface $shop)
getRequest(): RequestInterface
getShop(): ShopInterface
```

### Event Table

| Class | Dispatched when | Extra methods |
|-------|----------------|---------------|
| `BeforeRegistrationStartsEvent` | Before new or re-registration shop is saved in Step 1 | — |
| `BeforeRegistrationCompletedEvent` | Before Step 2 credentials are persisted | `getConfirmation(): array{apiKey: string, secretKey: string}` |
| `RegistrationCompletedEvent` | After Step 2 credentials are persisted | — |
| `BeforeShopActivateEvent` | Before `app.activated` webhook is processed | — |
| `ShopActivatedEvent` | After shop is activated (`setShopActive(true)` + persisted) | — |
| `BeforeShopDeactivatedEvent` | Before `app.deactivated` webhook is processed | — |
| `ShopDeactivatedEvent` | After shop is deactivated (`setShopActive(false)` + persisted) | — |
| `BeforeShopDeletionEvent` | Before shop is deleted from repository | — |
| `ShopDeletedEvent` | After `deleteShop()` has been called | — |

### Usage with Symfony EventDispatcher

```php
use Symfony\Component\EventDispatcher\EventDispatcher;
use Shopware\App\SDK\Event\ShopActivatedEvent;

$dispatcher = new EventDispatcher();
$dispatcher->addListener(ShopActivatedEvent::class, function (ShopActivatedEvent $event) {
    $shop = $event->getShop();
    // Provision resources for $shop->getShopId()
});

$lifecycle = new AppLifecycle($registration, $resolver, $repo, $logger, $dispatcher);
```

### Usage with any PSR-14 dispatcher

```php
$dispatcher->dispatch(new ShopActivatedEvent($request, $shop));
```

## Exceptions

All exceptions reside in `Shopware\App\SDK\Exception\`.

| Class | Extends | Message | Extra method |
|-------|---------|---------|--------------|
| `MalformedWebhookBodyException` | `\RuntimeException` | `'Malformed webhook body, cannot parse body'` | — |
| `MissingClaimException` | `\RuntimeException` | `'Missing claim "{name}", did you forgot...'` | `getClaimName(): string` |
| `MissingShopParameterException` | `\RuntimeException` | `'Missing shop parameters'` | — |
| `ShopNotFoundException` | `\RuntimeException` | `'Shop with id "{id}" not found'` | `getShopId(): string` |
| `SignatureInvalidException` | `\Exception` | `'Signature could not be verified'` | `getRequest(): RequestInterface` |
| `SignatureNotFoundException` | `\RuntimeException` | `'Signature is not present in request'` | `getRequest(): RequestInterface` |

### Exception handling pattern

```php
use Shopware\App\SDK\Exception\SignatureInvalidException;
use Shopware\App\SDK\Exception\ShopNotFoundException;

try {
    $shop = $shopResolver->resolveShop($request);
    $action = $contextResolver->assembleActionButton($request, $shop);
} catch (SignatureInvalidException $e) {
    return new Response(401, [], 'Invalid signature');
} catch (ShopNotFoundException $e) {
    return new Response(404, [], 'Shop ' . $e->getShopId() . ' not found');
} catch (MalformedWebhookBodyException $e) {
    return new Response(400, [], $e->getMessage());
}
```
