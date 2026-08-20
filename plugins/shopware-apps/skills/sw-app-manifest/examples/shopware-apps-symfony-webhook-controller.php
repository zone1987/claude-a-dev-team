<?php

declare(strict_types=1);

/**
 * Shopware App Webhook Controller using shopware/app-bundle (Symfony)
 * Install: composer require shopware/app-bundle
 */

namespace App\Controller;

use Shopware\App\SDK\Authentication\ResponseSigner;
use Shopware\App\SDK\Context\ActionButton\ActionButtonAction;
use Shopware\App\SDK\Context\Module\ModuleAction;
use Shopware\App\SDK\Context\Payment\PaymentPayAction;
use Shopware\App\SDK\Context\Webhook\WebhookAction;
use Shopware\App\SDK\HttpClient\ClientFactory;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class WebhookController
{
    public function __construct(
        private readonly ClientFactory $clientFactory,
        private readonly ResponseSigner $signer,
    ) {
    }

    // --- Webhook Handler ---

    #[Route('/webhook/product-changed', methods: ['POST'])]
    public function productChanged(WebhookAction $action): Response
    {
        $shopId = $action->shop->getShopId();
        $event = $action->eventName;
        $payload = $action->payload;
        $entityIds = $payload['primaryKey'] ?? [];

        // Use HTTP client to call Shopware Admin API
        $client = $this->clientFactory->createClient($action->shop);
        $response = $client->sendPostRequest('/api/search/product', [
            'ids' => $entityIds,
            'limit' => count($entityIds),
        ]);

        return new Response('', Response::HTTP_OK);
    }

    #[Route('/webhook/order-placed', methods: ['POST'])]
    public function orderPlaced(WebhookAction $action): Response
    {
        $orderId = $action->payload['primaryKey'] ?? null;

        // Fetch full order via API
        $client = $this->clientFactory->createClient($action->shop);
        $order = $client->sendPostRequest('/api/search/order', [
            'ids' => [$orderId],
            'associations' => [
                'lineItems' => [],
                'orderCustomer' => [],
            ],
        ]);

        return new Response('', Response::HTTP_OK);
    }

    // --- Action Button Handler ---

    #[Route('/action/sync-product', methods: ['POST'])]
    public function syncProduct(ActionButtonAction $action): JsonResponse
    {
        $entityIds = $action->ids;
        $entity = $action->entity;

        // Process the action button click
        return new JsonResponse([
            'actionType' => 'notification',
            'payload' => [
                'status' => 'success',
                'message' => sprintf('Successfully synced %d %s(s).', count($entityIds), $entity),
            ],
        ]);
    }

    // --- Admin Module (iFrame) ---

    #[Route('/admin/dashboard', name: 'admin_dashboard')]
    public function adminDashboard(ModuleAction $action): Response
    {
        $shopUrl = $action->shop->getShopUrl();

        // The base-app-url in manifest.xml ensures this route is loaded as iframe
        return new Response(
            <<<HTML
            <!DOCTYPE html>
            <html>
            <head>
                <title>App Dashboard</title>
                <script>window.parent.postMessage('sw-app-loaded', '*');</script>
            </head>
            <body>
                <h1>My App Dashboard</h1>
                <p>Connected to: {$shopUrl}</p>
            </body>
            </html>
            HTML,
            Response::HTTP_OK,
            ['Content-Type' => 'text/html']
        );
    }

    // --- Payment Handler ---

    #[Route('/payment/pay', methods: ['POST'])]
    public function pay(PaymentPayAction $action): Response
    {
        $order = $action->order;
        $transaction = $action->orderTransaction;
        $amount = $transaction['amount']['totalPrice'];
        $orderNumber = $order['orderNumber'];

        // Process payment...
        $response = new JsonResponse(['status' => 'paid']);

        return $this->signer->signResponse($response, $action->shop);
    }

    // --- Flow Action Handler ---

    #[Route('/flow/slack-notify', methods: ['POST'])]
    public function slackNotify(WebhookAction $action): Response
    {
        $payload = $action->payload;

        // Config values from flow action definition
        $channel = $payload['config']['channel'] ?? '#general';
        $message = $payload['config']['message'] ?? '';

        // Parameters interpolated from flow data
        $orderNumber = $payload['order_number'] ?? '';
        $customerName = $payload['customer_name'] ?? '';

        // Send to Slack...
        return new Response('', Response::HTTP_OK);
    }
}
