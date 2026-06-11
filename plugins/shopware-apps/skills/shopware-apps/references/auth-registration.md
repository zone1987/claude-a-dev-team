---
title: App Registration Handshake Flow
impact: HIGH
impactDescription: The registration handshake establishes trust between the app server and the Shopware shop
tags: auth, registration, handshake, setup
---

## App Registration Handshake Flow

When a Shopware app with a `<setup>` section is installed, a 5-step handshake establishes mutual trust between the shop and the app server. This process exchanges credentials that are used for all subsequent communication.

### Prerequisites

The manifest must define a setup section:

```xml
<setup>
    <registrationUrl>https://my-app.example.com/register</registrationUrl>
    <secret>myAppSecret</secret>
</setup>
```

### The 5-Step Handshake

#### Step 1: Shopware sends GET request to registration URL

Shopware sends a GET request to the `registrationUrl` with query parameters:

```
GET https://my-app.example.com/register?shop-id=abc123&shop-url=https://my-shop.com&timestamp=1694000000
```

Query parameters:
- `shop-id` - Unique identifier for the shop
- `shop-url` - Base URL of the Shopware shop
- `timestamp` - Unix timestamp of the request

The request includes a `shopware-app-signature` header.

#### Step 2: App server verifies the signature

The `shopware-app-signature` header contains an HMAC-SHA256 hash of the **query string** signed with the app `<secret>` from the manifest:

```php
$queryString = $_SERVER['QUERY_STRING'];
$signature = $_SERVER['HTTP_SHOPWARE_APP_SIGNATURE'];

$expectedSignature = hash_hmac('sha256', $queryString, $appSecret);

if (!hash_equals($expectedSignature, $signature)) {
    return new Response('Unauthorized', 401);
}
```

**Important:** Never re-parse or reconstruct the query string. Use the raw query string exactly as received, because parameter order matters for HMAC validation.

#### Step 3: App server responds with proof and URLs

The app server responds with JSON containing a `proof`, the `secret` for future communication, and a `confirmation_url`:

```php
$shopId = $_GET['shop-id'];
$shopUrl = $_GET['shop-url'];
$appName = 'MyApp';

// Proof = HMAC-SHA256 of shopId + shopUrl + appName
$proof = hash_hmac('sha256', $shopId . $shopUrl . $appName, $appSecret);

return new JsonResponse([
    'proof' => $proof,
    'secret' => 'generatedRandomSecret',     // Store this - used for future HMAC
    'confirmation_url' => 'https://my-app.example.com/confirm'
]);
```

The `proof` is calculated as `HMAC-SHA256(shopId + shopUrl + appName, appSecret)`, proving the app server knows the manifest secret.

#### Step 4: Shopware sends confirmation POST

After verifying the proof, Shopware sends a POST request to the `confirmation_url` with the shop's API credentials:

```json
{
    "apiKey": "SWIAGXKERNKZM0XJCGFOQ2DPBG",
    "secretKey": "VnNsWVBRZnRHY0xnYkVkUjdYd...",
    "timestamp": 1694000000,
    "shopUrl": "https://my-shop.com",
    "shopId": "abc123"
}
```

This POST also includes the `shopware-shop-signature` header, signed with the `secret` you provided in Step 3.

#### Step 5: App server stores credentials

The app server must:
1. Verify the `shopware-shop-signature` on the confirmation request.
2. Store `apiKey` and `secretKey` associated with the `shopId`.
3. Use these credentials to obtain OAuth tokens for the Admin API.

```php
// Verify the confirmation signature
$body = $request->getBody()->getContents();
$signature = $request->getHeaderLine('shopware-shop-signature');
$expected = hash_hmac('sha256', $body, $storedSecret);

if (!hash_equals($expected, $signature)) {
    return new Response('Unauthorized', 401);
}

// Store credentials
$payload = json_decode($body, true);
$this->storeCredentials(
    $payload['shopId'],
    $payload['apiKey'],
    $payload['secretKey'],
    $payload['shopUrl']
);
```

### Timeout

Shopware enforces a **5-second timeout** on the registration request (Step 1). If your app server does not respond within 5 seconds, the registration fails. Keep the registration endpoint fast and defer heavy processing.

### Complete Flow Diagram

```
Shop                                App Server
 |                                       |
 |-- GET /register?shop-id&shop-url ---->|  (1) Registration request
 |   + shopware-app-signature header     |
 |                                       |  (2) Verify signature
 |<---- { proof, secret, confirm_url } --|  (3) Respond with proof
 |                                       |
 |-- POST /confirm ----------------------|  (4) Send API credentials
 |   + shopware-shop-signature header    |
 |   { apiKey, secretKey, shopId, ... }  |
 |                                       |  (5) Store credentials
 |<---- 200 OK -------------------------|
```
