---
title: PHP SDK Symfony Integration
impact: HIGH
impactDescription: The Symfony bundle provides automatic route registration and DI integration
tags: sdk, php, symfony, bundle, framework
---

## PHP SDK Symfony Integration

The `shopware/app-bundle` provides automatic route registration, dependency injection, and lifecycle handling for Symfony applications.

### Installation

```bash
composer require shopware/app-bundle
```

### Configuration

```yaml
# config/packages/shopware_app.yaml
shopware_app:
    app_name: 'MyApp'
    app_secret: 'my-secret'
    confirmation_url: 'https://my-app.com/app/register/confirm'
    # Optional: shop repository (defaults to file-based)
    shop_repository: 'App\Repository\CustomShopRepository'
```

### Auto-Registered Routes

The bundle automatically provides:
- `POST /app/register` — Registration
- `POST /app/register/confirm` — Confirmation
- `POST /app/activate` — Activation
- `POST /app/deactivate` — Deactivation
- `POST /app/delete` — Deletion

### Webhook Controller

```php
use Shopware\App\SDK\Context\Webhook\WebhookAction;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class WebhookController
{
    #[Route('/webhook/product-changed', methods: ['POST'])]
    public function productChanged(WebhookAction $action): Response
    {
        $shopId = $action->shop->getShopId();
        $event = $action->eventName;
        $payload = $action->payload;

        // Process webhook...

        return new Response('', 200);
    }
}
```

### Admin Module Controller

```php
use Shopware\App\SDK\Context\Module\ModuleAction;
use Symfony\Component\HttpFoundation\Response;

class AdminController
{
    #[Route('/app/admin', name: 'admin')]
    public function admin(ModuleAction $action): Response
    {
        return $this->render('admin.html.twig', [
            'shopUrl' => $action->shop->getShopUrl(),
            'inAppPurchases' => $action->inAppPurchases->all(),
        ]);
    }
}
```

### Payment Controller

```php
use Shopware\App\SDK\Context\Payment\PaymentPayAction;
use Shopware\App\SDK\Authentication\ResponseSigner;

class PaymentController
{
    #[Route('/payment/pay', methods: ['POST'])]
    public function pay(PaymentPayAction $action, ResponseSigner $signer): Response
    {
        $order = $action->order;
        $transaction = $action->orderTransaction;

        $response = new JsonResponse(['status' => 'paid']);
        return $signer->signResponse($response, $action->shop);
    }
}
```
