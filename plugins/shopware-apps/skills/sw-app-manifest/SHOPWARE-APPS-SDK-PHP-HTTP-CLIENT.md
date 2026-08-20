---
title: PHP SDK HTTP Client
impact: HIGH
impactDescription: The HTTP client handles OAuth2 token management for Shopware API calls
tags: sdk, php, http-client, api, oauth2
---

## PHP SDK HTTP Client

The PHP SDK provides a PSR-18 compatible HTTP client with automatic OAuth2 token management.

### Creating the Client

```php
use Shopware\App\SDK\HttpClient\ClientFactory;

$httpClient = ClientFactory::createClient($shop);
```

### SimpleHttpClient Wrapper

```php
use Shopware\App\SDK\HttpClient\SimpleHttpClient;

$client = new SimpleHttpClient($httpClient);

// GET
$response = $client->get($shop, '/api/product');

// POST
$response = $client->post($shop, '/api/product', [
    'name' => 'My Product',
    'productNumber' => 'SW-001',
    'stock' => 10,
    'taxId' => 'tax-id-uuid',
]);

// PATCH
$response = $client->patch($shop, '/api/product/uuid', [
    'name' => 'Updated Name',
]);

// DELETE
$response = $client->delete($shop, '/api/product/uuid');
```

### Response Signing

Action buttons, payment handlers, and tax providers require signed responses:

```php
use Shopware\App\SDK\Authentication\ResponseSigner;

$signer = new ResponseSigner();
$signedResponse = $signer->signResponse($psrResponse, $shop);
```

**Incorrect (forgetting to sign response for action button):**

```php
return new JsonResponse(['actionType' => 'notification', 'payload' => ['status' => 'success']]);
```

**Correct (response is signed):**

```php
$response = new JsonResponse(['actionType' => 'notification', 'payload' => ['status' => 'success']]);
$signer = new ResponseSigner();
return $signer->signResponse($response, $shop);
```
