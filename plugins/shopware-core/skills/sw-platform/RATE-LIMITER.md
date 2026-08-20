# Shopware 6 — Rate Limiter

Shopware ships limiters (e.g. login, reset password, contact form). Define your own limits under
`shopware.api.rate_limiter` / `config/packages` and check them in the controller through the `RateLimiter`.

```php
$this->rateLimiter->ensureAccepted('ff_content_import', $cacheKey);
// throws RateLimitExceededException once the limit is exceeded
```

Policy types: `time_backoff` (increasing wait time) and `system_config`. Reset the limiter after success via
`reset($key)`. Worth applying to public Store API endpoints to prevent abuse.

→ Policies, config examples, integration: [RATE-LIMITER-DETAIL.md](RATE-LIMITER-DETAIL.md)
