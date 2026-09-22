# Shopware 6 — Rate Limiter

Shopware ships limiters (e.g. login, reset password, contact form). Define your own limits under
`shopware.api.rate_limiter` / `config/packages` and check them in the controller through the `RateLimiter`.

```php
$this->rateLimiter->ensureAccepted('ff_content_import', $cacheKey);
// throws RateLimitExceededException once the limit is exceeded
```

Policy types: `time_backoff` (increasing wait time) and `system_config`. Reset the limiter after success via
`reset($key)`. Worth applying to public Store API endpoints to prevent abuse.

## Rate Limiter

### Overview

Plugins can add rate limiting to custom routes to prevent abuse. Shopware uses Symfony's RateLimiter component.

### Adding a Rate Limiter

#### Configuration (`src/Resources/config/services/rate-limiter.php`)

PHP, not XML (`XmlFileLoader` is `@deprecated tag:v6.8.0`), explicitly and without autowiring
(→ `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`).

```php
$services->set(FfContentPlusRateLimiterFactory::class, RateLimiterFactory::class)
    ->args([
        'ff_content_plus_api',
        param('shopware.api.rate_limiter.ff_content_plus_api'),
        service('cache.rate_limiter'),
        service('lock.factory'),
    ]);
```

#### Rate Limiter Configuration (config/packages/)

Create `config/packages/ff_content_plus.yaml` or register via plugin configuration:

```yaml
shopware:
    api:
        rate_limiter:
            ff_content_plus_api:
                enabled: true
                policy: time_backoff
                reset: 1 hour
                limits:
                    - limit: 10
                      interval: 10 seconds
                    - limit: 15
                      interval: 30 seconds
                    - limit: 20
                      interval: 60 seconds
```

### Using Rate Limiter in Routes

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Storefront\Controller;

use Shopware\Core\Framework\RateLimiter\RateLimiter;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route(defaults: ['_routeScope' => ['storefront']])]
class FfContentPlusController extends StorefrontController
{
    public function __construct(
        private readonly RateLimiter $rateLimiter,
    )
    {
    }

    #[Route(
        path: '/ff-content-plus/submit',
        name: 'frontend.ff-content-plus.submit',
        methods: ['POST'],
    )]
    public function submit(Request $request): Response
    {
        $this->rateLimiter->ensureAccepted(
            'ff_content_plus_api',
            $request->getClientIp(),
        );

        // Process request...
    }
}
```

### Available Policies

| Policy | Description |
|--------|------------|
| `fixed_window` | Fixed number of requests per time window |
| `sliding_window` | Sliding window rate limiting |
| `token_bucket` | Token bucket algorithm |
| `time_backoff` | Increasingly strict limits (recommended for APIs) |

### RateLimitExceededException

When the limit is exceeded, Shopware throws `RateLimitExceededException`. The storefront automatically handles this with a user-friendly error page.
