---
name: sw-paas-cdn
description: >
  Shopware PaaS Native CDN: Fastly Integration, Custom Domains (Apex/Subdomain),
  DNS-Konfiguration, Fastly Snippets, Web Application Firewall (WAF), NGWAF.
  Trigger: "paas fastly cdn", "paas custom domain einrichten", "sw-paas domain
  create", "paas dns konfigurieren", "paas cdn fastly", "paas apex domain",
  "paas waf", "paas web application firewall", "paas fastly snippets",
  "shopware paas domain", "paas cdn konfiguration".
---

# Shopware PaaS Native — CDN & Custom Domains

## Fastly CDN (automatisch aktiv)

- Standard CDN für alle PaaS-Native-Umgebungen
- Zwei Services: `storefront` + `cdn` (für S3-Assets)
- Automatische Cache-Invalidierung via Deployment Helper
- HTTP Cache am Edge = weniger Redis-Last, geringere Latenz global
- WAF (Next-Gen WAF, OWASP Top 10) standardmäßig aktiv — kein Setup nötig

## Custom Domain einrichten

### Subdomain (nicht-Apex, z.B. `shop.example.com`)

```dns
CNAME: cdn.shopware.shop
```

### Apex Domain (z.B. `example.com`)

```dns
# A Records
151.101.3.52
151.101.67.52
151.101.131.52
151.101.195.52

# AAAA Records
2a04:4e42::820
2a04:4e42:200::820
2a04:4e42:400::820
2a04:4e42:600::820

# TXT Record (Ownership)
_shopware-challenge.example.com. TXT "shopware-challenge=<org-id>"
```

### Ablauf

```bash
# 1. DNS konfigurieren (Provider)
# 2. Propagation abwarten (15-30 Min bis 48h)
# 3. DNS prüfen
dig shop.example.com CNAME        # Subdomain
dig example.com A                  # Apex
dig _shopware-challenge.example.com TXT

# 4. Domain anlegen (validiert DNS live!)
sw-paas domain create

# 5. Application redeployen
sw-paas application deploy create

# 6. Domain in Shopware-Admin Sales Channel konfigurieren
```

## Fastly Snippets (PaaS Native)

```bash
composer require shopware/fastly-meta
```

FASTLY_API_KEY und FASTLY_SERVICE_ID werden automatisch bereitgestellt.
Snippets werden automatisch beim Deployment installiert.

## Vertiefung

[references/deep/cdn.md](references/deep/cdn.md)
