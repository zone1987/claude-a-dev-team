---
name: sw-hosting-webserver
description: >
  Shopware 6 Webserver-Konfiguration — Nginx, Apache, Caddy, FrankenPHP, Trusted Proxies, Varnish, Fastly.
  Triggers: "nginx config", "apache config", "caddy", "frankenphp", "reverse proxy", "varnish setup",
  "fastly setup", "trusted proxy", "webserver konfigurieren", "Varnish XKey", "HTTP reverse cache",
  "ban method", "cache invalidation", "BAN request"
---

# Shopware Hosting — Web Server & Reverse Proxy

Refer to `references/deep/webserver.md` for full VCL examples and Fastly configs.

## Recommended web server
Caddy or FrankenPHP for containers (automatic resource allocation, single process).
For bare-metal: Nginx or Apache (see Shopware config references for full configs).

## Varnish XKey (recommended)

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

```dotenv
SHOPWARE_HTTP_CACHE_ENABLED=1
```

Use `xkey.softpurge` in VCL for soft-purge (stale-while-revalidate behavior).

Docker image: `ghcr.io/shopware/varnish-shopware`

## Fastly

```yaml
shopware:
    http_cache:
        reverse_proxy:
            enabled: true
            fastly:
                enabled: true
                api_key: '<token>'
                service_id: '<id>'
                soft_purge: '1'
        stale_while_revalidate: 300
        stale_if_error: 3600
```

## Trusted proxies (since SW 6.6)
Create `config/packages/trusted_env.yaml` — see Shopware recipes for template.

## Cache commands
```bash
bin/console cache:clear          # clears app + HTTP cache
bin/console cache:clear:all      # clears everything (since 6.6.8)
bin/console cache:clear:http     # clears only HTTP/reverse-proxy cache (since 6.6.10)
```

See also: `sw-hosting-caching-http`, `sw-hosting-performance`.

Full reference: `references/deep/webserver.md`
