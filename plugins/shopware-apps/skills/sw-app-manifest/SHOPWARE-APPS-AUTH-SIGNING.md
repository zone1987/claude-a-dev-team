---
title: Request and Response Signing
impact: HIGH
impactDescription: Proper request and response signing ensures secure bidirectional communication between app and shop
tags: auth, signing, hmac, response-signing
---

## Request and Response Signing

All communication between Shopware and app servers is authenticated using HMAC-SHA256 signatures. This applies to both incoming requests from Shopware and outgoing responses from the app server.

### Request Signing (Shopware to App)

Every request from Shopware to the app server includes the `shopware-shop-signature` header. This is an HMAC-SHA256 hash of the request body, signed with the **shop secret** (the secret your app provided during the registration handshake).

```php
// Always verify incoming requests
$signature = $request->getHeaderLine('shopware-shop-signature');
$body = $request->getBody()->getContents();

$expected = hash_hmac('sha256', $body, $shopSecret);

if (!hash_equals($expected, $signature)) {
    throw new UnauthorizedException('Invalid signature');
}
```

### Response Signing (App to Shopware)

Certain endpoints **require** the app server to sign its response body so Shopware can verify the response has not been tampered with. Response signing is mandatory for:

- **Action buttons** - Custom admin action button handlers
- **Payment handlers** - Pay, capture, refund, validate endpoints
- **Tax providers** - Custom tax calculation responses
- **Checkout/context gateways** - Cart and context manipulation responses

The response must include a `shopware-app-signature` header containing the HMAC-SHA256 of the response body, signed with the shop secret:

```php
$responseBody = json_encode($responseData);

$signature = hash_hmac('sha256', $responseBody, $shopSecret);

return new Response($responseBody, 200, [
    'Content-Type' => 'application/json',
    'shopware-app-signature' => $signature,
]);
```

### Use Official SDKs

The recommended approach is to use the official SDKs, which handle signing automatically:

**PHP SDK (shopware/app-php-sdk):**

```php
use Shopware\App\SDK\Response\ActionButtonResponse;
use Shopware\App\SDK\HttpClient\SimpleHttpClient\SimpleHttpClient;

// The SDK's ResponseSigner handles signature generation
$responseSigner = new \Shopware\App\SDK\Authentication\ResponseSigner();
$signedResponse = $responseSigner->signResponse(
    $response,
    $shopSecret
);
```

**JavaScript SDK (@shopware-ag/app-server-sdk):**

```javascript
import { AppServer } from '@shopware-ag/app-server-sdk';

const app = new AppServer({
    appName: 'MyApp',
    appSecret: 'myAppSecret',
});

// The SDK handles both request verification and response signing
app.post('/action-button', async (context) => {
    // context.request is already verified
    return context.sign({ success: true }); // Automatically signed
});
```

### Critical: Never Re-Parse Query Strings

When verifying HMAC signatures on GET requests (e.g., during registration), never reconstruct or re-parse the query string. Use the raw query string exactly as received:

**Incorrect (reconstructing query string):**

```php
// WRONG: Re-building the query string may change parameter order or encoding
$params = $request->getQueryParams();
$queryString = http_build_query($params);
$expected = hash_hmac('sha256', $queryString, $secret);
```

**Correct (using raw query string):**

```php
// CORRECT: Use the original query string as-is
$queryString = $request->getUri()->getQuery();
$expected = hash_hmac('sha256', $queryString, $secret);
```

### Shopware May Add Parameters

Shopware reserves the right to add new query parameters or headers to requests **without prior notice** and without considering it a breaking change. Your signature verification must account for this:

- Do not reject requests with unexpected parameters.
- Do not hardcode expected parameter lists.
- Always validate the signature against the **complete** raw query string or body.

### Summary Table

| Direction | Header | Signed With | Required For |
|-----------|--------|-------------|--------------|
| Shopware to App | `shopware-shop-signature` | Shop secret | All requests |
| App to Shopware | `shopware-app-signature` | Shop secret | Action buttons, payments, tax providers, gateways |
| Registration GET | `shopware-app-signature` | App secret (from manifest) | Registration only |
