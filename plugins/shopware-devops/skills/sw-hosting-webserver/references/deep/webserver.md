# Shopware 6 — Web Server & Reverse Proxy (Deep Reference)

Sources: `guides/hosting/infrastructure/reverse-http-cache.md`, `guides/hosting/index.md`

## Recommended web servers

| Server | Use case |
|---|---|
| **Caddy** | Recommended for production (simple config) |
| **FrankenPHP** | Recommended for containers (single process, auto resource allocation) |
| **Nginx** | Traditional production setups |
| **Apache** | Legacy setups |
| **Symfony CLI** | Local development only |

Full config references:
- Caddy: https://developer.shopware.com/docs/resources/references/config-reference/server/caddy.html
- Apache: https://developer.shopware.com/docs/resources/references/config-reference/server/apache.html
- Nginx: https://developer.shopware.com/docs/resources/references/config-reference/server/nginx.html

## HTTP cache enable

```dotenv
SHOPWARE_HTTP_CACHE_ENABLED=1
SHOPWARE_HTTP_DEFAULT_TTL=7200
```

## Varnish XKey (recommended, Shopware ≥ 6.6)

**Note:** Redis-based BAN (old method) is deprecated since 6.6.x and removed in 6.7.0. Use XKey instead.

### Shopware config

```yaml
# config/packages/shopware.yaml
shopware:
    http_cache:
        reverse_proxy:
            enabled: true
            ban_method: "BAN"
            hosts: ["http://varnish"]
            max_parallel_invalidations: 3
            use_varnish_xkey: true
```

### VCL soft purge (keep stale cache during refresh)

```diff
-set req.http.n-gone = xkey.purge(req.http.xkey);
+set req.http.n-gone = xkey.softpurge(req.http.xkey);
```

XKey module requires Varnish 6.0+ and separate installation.

Docker image: `ghcr.io/shopware/varnish-shopware` (pre-configured with Shopware VCL).

### Trusted proxies (since SW 6.6)

`TRUSTED_PROXIES` env variable no longer taken into account out of the box. Create:
`config/packages/trusted_env.yaml` (see Shopware recipes template).

### Debugging Varnish

Check for `Cache-Control: public` and `Xkey:` headers:
```bash
curl -vvv -H 'Host: <sales-channel-domain>' <app-server-ip> 1> /dev/null
```

Expected response:
```
< Cache-Control: public, s-maxage=7200
< Xkey: theme.sw-logo-desktop, ...
```

If `Age: 0` always returned → cache not working → check `Cache-Control: public` is set by app.

## Fastly (since 6.4.11.0)

```yaml
shopware:
    http_cache:
        stale_while_revalidate: 300
        stale_if_error: 3600
        reverse_proxy:
            enabled: true
            fastly:
                enabled: true
                api_key: '<personal-token-from-fastly>'
                service_id: '<service-id>'
                soft_purge: '1'
```

Fastly VCL snippets: https://github.com/shopware/recipes/tree/main/shopware/fastly-meta/6.7/config/fastly

Deployment Helper Fastly integration:
```bash
composer require shopware/fastly-meta
# Set FASTLY_API_KEY and FASTLY_SERVICE_ID env vars
```

## HTTP Caching Policies (experimental, since CACHE_REWORK feature flag)

```yaml
shopware:
    http_cache:
        policies:
            custom_policy:
                headers:
                    cache_control:
                        public: true
                        max_age: 600
                        s_maxage: 3600
        default_policies:
            store_api:
                cacheable: custom_policy
        route_policies:
            store-api.product.search: custom_policy
```

Default policies: `storefront.cacheable`, `store_api.cacheable`, `no_cache_private`.

Policy precedence (highest to lowest):
1. `route_policies[route#hook]`
2. `route_policies[route]`
3. `default_policies[area].{cacheable|uncacheable}`

## Cache commands

```bash
bin/console cache:clear          # app cache + HTTP cache (pre-6.7: also HTTP cache)
bin/console cache:clear:all      # everything including HTTP cache, all pools (since 6.6.8)
bin/console cache:clear:http     # reverse proxy cache only (since 6.6.10)
bin/console cache:pool:clear --all  # only object cache, not HTTP (pre-6.6.10)
```

## Logged-in / cart-filled cache bypass

Disable for projects not using Dynamic Access or user-specific content:
```yaml
# config/packages/prod/shopware.yaml
shopware:
    cache:
        invalidation:
            http_cache: []
```

## CDN for assets

Ensure `Cache-Control: public, max-age=86400` on CDN responses for assets.
