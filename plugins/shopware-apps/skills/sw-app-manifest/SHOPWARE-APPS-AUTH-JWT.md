---
title: JWT Tokens for In-App Purchases
impact: HIGH
impactDescription: JWT verification is required to validate in-app purchase entitlements from the Shopware Store
tags: auth, jwt, in-app-purchases, token
---

## JWT Tokens for In-App Purchases

Shopware apps can offer in-app purchases (IAP) through the Shopware Store. When a merchant has purchased IAP features, Shopware delivers a signed JWT token to the app server containing the purchased entitlements. The app must verify and decode this token to determine which features are unlocked.

### How the JWT Is Delivered

The JWT token is included in requests from Shopware to the app server in one of two ways:

- **As a query parameter:** `in-app-purchases` (for GET requests)
- **As a body field:** `inAppPurchases` (for POST/webhook requests)

```
GET https://my-app.example.com/action?in-app-purchases=eyJhbGciOiJSUzI1NiIs...
```

```json
{
    "source": { "shopId": "abc123", "url": "https://my-shop.com" },
    "data": { ... },
    "inAppPurchases": "eyJhbGciOiJSUzI1NiIs..."
}
```

### JWT Claims

The decoded JWT contains claims with the identifiers of purchased in-app features:

```json
{
    "iat": 1694000000,
    "exp": 1694003600,
    "iss": "Shopware",
    "sub": "abc123",
    "purchases": [
        { "identifier": "premium-analytics", "quantity": 1 },
        { "identifier": "advanced-export", "quantity": 1 }
    ]
}
```

### JWKS URL

The JWT is signed using RS256. Verify it using the JSON Web Key Set (JWKS) published at:

```
https://api.shopware.com/inappfeatures/jwks
```

### Node.js Verification (jose library)

```javascript
import * as jose from 'jose';

const JWKS_URL = 'https://api.shopware.com/inappfeatures/jwks';

async function verifyInAppPurchases(token) {
    const JWKS = jose.createRemoteJWKSet(new URL(JWKS_URL));

    try {
        const { payload } = await jose.jwtVerify(token, JWKS, {
            issuer: 'Shopware',
        });

        return payload.purchases || [];
    } catch (error) {
        console.error('IAP token verification failed:', error.message);
        return [];
    }
}

// Usage in request handler:
app.post('/webhook', async (req, res) => {
    const token = req.body.inAppPurchases;

    if (token) {
        const purchases = await verifyInAppPurchases(token);
        const hasPremium = purchases.some(p => p.identifier === 'premium-analytics');

        if (hasPremium) {
            // Enable premium feature
        }
    }
});
```

### PHP Verification (shopware/app-php-sdk)

```php
use Shopware\App\SDK\InAppPurchases\InAppPurchaseVerifier;

$verifier = new InAppPurchaseVerifier();

// The SDK handles JWKS fetching and JWT verification
$purchases = $verifier->verify($jwtToken);

foreach ($purchases as $purchase) {
    if ($purchase->getIdentifier() === 'premium-analytics') {
        // Enable premium feature
    }
}
```

### Best Practices

**Incorrect (not verifying the token):**

```javascript
// WRONG: Never trust the token without verification
const payload = JSON.parse(atob(token.split('.')[1]));
const purchases = payload.purchases;
```

**Correct (verifying with JWKS):**

```javascript
// CORRECT: Always verify the JWT signature using the JWKS
const JWKS = jose.createRemoteJWKSet(new URL(JWKS_URL));
const { payload } = await jose.jwtVerify(token, JWKS, { issuer: 'Shopware' });
const purchases = payload.purchases;
```

- Always verify the JWT signature against the JWKS endpoint before trusting the claims.
- Cache the JWKS response to avoid repeated network requests (the `jose` library does this automatically).
- Check the `exp` (expiration) claim to reject expired tokens.
- Use the `sub` (subject) claim to match the token to the correct shop.
