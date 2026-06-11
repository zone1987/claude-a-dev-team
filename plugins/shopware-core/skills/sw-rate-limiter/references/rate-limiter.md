# Rate Limiter

## Overview

Plugins can add rate limiting to custom routes to prevent abuse. Shopware uses Symfony's RateLimiter component.

## Adding a Rate Limiter

### Configuration (services.xml)

```xml
<service id="FfContentPlus\Core\Framework\RateLimiter\FfContentPlusRateLimiterFactory"
         class="Shopware\Core\Framework\RateLimiter\RateLimiterFactory">
    <argument>ff_content_plus_api</argument>
    <argument>%shopware.api.rate_limiter.ff_content_plus_api%</argument>
    <argument type="service" id="cache.rate_limiter"/>
    <argument type="service" id="lock.factory"/>
</service>
```

### Rate Limiter Configuration (config/packages/)

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

## Using Rate Limiter in Routes

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

## Available Policies

| Policy | Description |
|--------|------------|
| `fixed_window` | Fixed number of requests per time window |
| `sliding_window` | Sliding window rate limiting |
| `token_bucket` | Token bucket algorithm |
| `time_backoff` | Increasingly strict limits (recommended for APIs) |

## RateLimitExceededException

When the limit is exceeded, Shopware throws `RateLimitExceededException`. The storefront automatically handles this with a user-friendly error page.
