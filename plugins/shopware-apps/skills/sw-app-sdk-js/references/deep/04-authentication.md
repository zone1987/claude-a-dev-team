# JS SDK — Authentication & Signature Verification

## WebCryptoHmacSigner

Uses the Web Crypto API (`crypto.subtle`). Caches `CryptoKey` objects by secret for performance.

```ts
constructor()  // initializes TextEncoder + key cache Map<string, CryptoKey>
```

| Method | Purpose |
|--------|---------|
| `sign(message: string, secret: string): Promise<string>` | Returns lowercase hex HMAC-SHA256 |
| `verify(signature: string, data: string, secret: string): Promise<boolean>` | Signs data, compares (string equality, not constant-time) |
| `verifyGetRequest(request: Request, secret: string): Promise<void>` | Extracts `shopware-shop-signature` query param, builds message from remaining sorted params, verifies. Throws on missing or invalid. |
| `signResponse(response: Response, secret: string): Promise<void>` | Reads body, computes HMAC, sets `shopware-app-signature` header on response |
| `getKeyForSecret(secret: string): Promise<CryptoKey>` | Imports + caches HMAC-SHA256 key |
| `buf2hex(buf: ArrayBuffer): string` | Utility: ArrayBuffer → lowercase hex |

### HMAC message construction — GET requests

All query params except `shopware-shop-signature`, sorted alphabetically, concatenated as `key=value` joined by `&`.

### HMAC message construction — POST requests

Response body text. For registration proof: `shopId + shopUrl + appName`.

## DualSignatureVerifier

Handles secret rotation fallback (60-second window) and dual-signature (app + shop) logic.

```ts
constructor(
    private readonly signer: WebCryptoHmacSigner,
    private readonly now: () => Date = () => new Date()  // injectable for testing
)
```

**Constants:**
- `INFLIGHT_ALLOWANCE_MS = 60_000`
- Header names: `shopware-shop-signature`, `shopware-shop-signature-previous`, `shopware-app-signature`

### Methods

#### `authenticateRegistrationRequest(req, cfg, shop): Promise<void>`

Always verifies `shopware-app-signature` with `cfg.appSecret`.

Dual-sig is required when:
- `cfg.enforceDoubleSignature === true`, OR
- `shop.hasVerifiedWithDoubleSignature()` returns `true`, OR
- `shopware-shop-signature` header is present in the request

If dual-sig required AND shop is confirmed: also verifies `shopware-shop-signature` against current shop secret.

#### `authenticateRegistrationConfirmation(req, body, shop, cfg): Promise<void>`

Verifies `shopware-shop-signature` header against `shop.getPendingShopSecret()`.

If shop is already confirmed AND dual-sig required: also verifies `shopware-shop-signature-previous` against current shop secret.

#### `authenticatePostRequest(req, body, shop): Promise<void>`

1. Tries current `shopSecret`.
2. On failure: checks if `previousShopSecret` exists and rotation was within 60s.
3. If within window: tries `previousShopSecret`.
4. Throws original error if all attempts fail.

#### `authenticateGetRequest(req, shop): Promise<void>`

Same rotation fallback logic as `authenticatePostRequest` but for GET signature in query params.

## Secret Rotation Fallback — Full Logic

```
1. Verify with shop.getShopSecret() → success → done
2. prev = shop.getPreviousShopSecret()
   if prev === null → rethrow original error
3. rotatedAt = shop.getSecretsRotatedAt()
   if rotatedAt === null → rethrow original error
4. elapsed = now() - rotatedAt
   if elapsed > INFLIGHT_ALLOWANCE_MS (60 000 ms) → rethrow original error
5. Verify with prev → success → done; else rethrow original error
```

## Registration Proof Signature

Computed by `Registration.authorize()` internally:

```
HMAC-SHA256(shopId + shopUrl + appName, appSecret)
```

The result is placed in the `proof` field of the Step 1 response JSON.
