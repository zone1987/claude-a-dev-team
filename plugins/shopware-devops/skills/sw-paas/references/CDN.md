# Shopware PaaS Native — CDN & Custom Domains

## Fastly CDN (active automatically)

- Default CDN for all PaaS Native environments
- Two services: `storefront` + `cdn` (for S3 assets)
- Automatic cache invalidation via the Deployment Helper
- HTTP cache at the edge = less Redis load, lower latency globally
- WAF (Next-Gen WAF, OWASP Top 10) active by default — no setup required

## Set up a custom domain

### Subdomain (non-apex, e.g. `shop.example.com`)

```dns
CNAME: cdn.shopware.shop
```

### Apex domain (e.g. `example.com`)

```dns
# A records
151.101.3.52
151.101.67.52
151.101.131.52
151.101.195.52

# AAAA records
2a04:4e42::820
2a04:4e42:200::820
2a04:4e42:400::820
2a04:4e42:600::820

# TXT record (ownership)
_shopware-challenge.example.com. TXT "shopware-challenge=<org-id>"
```

### Procedure

```bash
# 1. Configure DNS (provider)
# 2. Wait for propagation (15-30 min up to 48h)
# 3. Check DNS
dig shop.example.com CNAME        # Subdomain
dig example.com A                  # Apex
dig _shopware-challenge.example.com TXT

# 4. Create the domain (validates DNS live!)
sw-paas domain create

# 5. Redeploy the application
sw-paas application deploy create

# 6. Configure the domain in the sales channel in the Shopware admin
```

## Fastly Snippets (PaaS Native)

```bash
composer require shopware/fastly-meta
```

FASTLY_API_KEY and FASTLY_SERVICE_ID are provided automatically.
Snippets are installed automatically during deployment.

## Deep dive

[CDN-DETAIL.md](CDN-DETAIL.md)
