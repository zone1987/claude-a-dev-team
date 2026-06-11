---
title: Webhook HMAC Verification
impact: HIGH
impactDescription: Verifying webhook signatures prevents unauthorized requests and replay attacks
tags: webhook, hmac, signature, verification, security
---

## Webhook HMAC Verification

Every webhook request from Shopware includes a signature header that must be verified to ensure the request is authentic and has not been tampered with.

### shopware-shop-signature Header

Shopware signs every webhook request body with the **shop secret** using HMAC-SHA256. The signature is sent in the `shopware-shop-signature` HTTP header.

**Verification process:**

1. Read the raw request body (do not parse/re-serialize it).
2. Compute HMAC-SHA256 of the raw body using the shop secret as the key.
3. Compare the computed hash with the `shopware-shop-signature` header value.

**PHP verification example:**

```php
$signature = $request->getHeaderLine('shopware-shop-signature');
$body = $request->getBody()->getContents();

$expectedSignature = hash_hmac('sha256', $body, $shopSecret);

if (!hash_equals($expectedSignature, $signature)) {
    return new Response('Unauthorized', 401);
}
```

**Node.js verification example:**

```javascript
const crypto = require('crypto');

function verifyWebhookSignature(body, signature, shopSecret) {
    const expectedSignature = crypto
        .createHmac('sha256', shopSecret)
        .update(body, 'utf8')
        .digest('hex');

    return crypto.timingSafeEqual(
        Buffer.from(expectedSignature, 'hex'),
        Buffer.from(signature, 'hex')
    );
}

// In request handler:
const signature = req.headers['shopware-shop-signature'];
const rawBody = req.rawBody; // Must be the raw string, not parsed JSON

if (!verifyWebhookSignature(rawBody, signature, shopSecret)) {
    res.status(401).send('Unauthorized');
    return;
}
```

**Incorrect (parsing body before verification):**

```javascript
// WRONG: Do not parse and re-stringify the body
const body = JSON.stringify(req.body);
const expected = crypto.createHmac('sha256', secret).update(body).digest('hex');
```

**Correct (using raw body):**

```javascript
// CORRECT: Use the raw request body as-is
const rawBody = req.rawBody;
const expected = crypto.createHmac('sha256', secret).update(rawBody, 'utf8').digest('hex');
```

### Additional Request Headers

Every webhook request includes these informational headers:

| Header | Description |
|--------|-------------|
| `shopware-shop-signature` | HMAC-SHA256 signature of the request body |
| `sw-version` | Shopware version of the sending shop (e.g., `6.6.0.0`) |
| `sw-context-language` | Language ID of the current context |
| `sw-user-language` | Language of the admin user who triggered the action |

### Timestamp Validation

The webhook payload includes a `timestamp` field (Unix timestamp). Validate this to prevent **replay attacks**:

```php
$payload = json_decode($body, true);
$timestamp = $payload['timestamp'];

// Reject requests older than 5 minutes
if (abs(time() - $timestamp) > 300) {
    return new Response('Request expired', 400);
}
```

### Idempotency with eventId

Shopware may retry failed webhook deliveries. Each webhook payload includes a unique `eventId` that remains the same across retries. Use this for **idempotency** to avoid processing the same event multiple times:

```php
$payload = json_decode($body, true);
$eventId = $payload['source']['eventId'] ?? null;

if ($eventId && $this->alreadyProcessed($eventId)) {
    return new Response('Already processed', 200);
}

// Process the webhook...
$this->markAsProcessed($eventId);
```
