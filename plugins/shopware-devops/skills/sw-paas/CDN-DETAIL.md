# Shopware PaaS Native — CDN & Custom Domains (Deep Reference)

Sources: `products/paas/shopware/cdn/index.md`,
`products/paas/shopware/cdn/fastly-snippets.md`,
`products/paas/shopware/cdn/security-features.md`,
`products/paas/shopware-paas/fastly.md`

---

## Contents

- [Fastly CDN — overview](#fastly-cdn-overview)
- [Web Application Firewall (WAF)](#web-application-firewall-waf)
- [Custom Domains](#custom-domains)
- [Fastly Snippets (PaaS Native)](#fastly-snippets-paas-native)
- [Fastly (classic Shopware PaaS / Platform.sh)](#fastly-classic-shopware-paas-platformsh)

## Fastly CDN — overview

Fastly is the primary CDN for Shopware PaaS Native. Benefits:

- **Global performance**: responses from edge locations worldwide
- **Resource optimization**: less load on application servers
- **Redis relief**: HTTP cache at the edge instead of Redis
- **Auto-scaling**: traffic spikes without impact on the app

### Two Fastly services

| Service | Purpose |
|---------|-------|
| `storefront` | Proxy for storefront and admin |
| `cdn` | Proxy for all S3 CDN assets (public bucket) |

### Configuration

Fully automatic — no additional setup required.
Configured through `config/packages/prod/fastly.yaml` (via k8s-meta).

---

## Web Application Firewall (WAF)

Enabled by default via Fastly NGWAF — no user action required.

- Feature set: NGWAF `Core`
- Protects against: OWASP Top 10 categories
- Further add-ons on the roadmap (no concrete schedule)

---

## Custom Domains

### Requirements

- `sw-paas` CLI installed and configured
- Organization ID known: `sw-paas org list`
- Domain registered with access to DNS management
- Deployment permissions available

### Important: configure DNS before creating the domain!

The platform validates DNS in real time during `sw-paas domain create`.
On error: creating the domain fails.

---

### DNS configuration: subdomain (non-apex)

Example: `shop.example.com`, `www.example.com`

```dns
shop.example.com.  IN  CNAME  cdn.shopware.shop.
```

### DNS configuration: apex domain

Example: `example.com`

#### A records (IPv4, create all 4!)

```dns
example.com.  IN  A  151.101.3.52
example.com.  IN  A  151.101.67.52
example.com.  IN  A  151.101.131.52
example.com.  IN  A  151.101.195.52
```

#### AAAA records (IPv6, create all 4!)

```dns
example.com.  IN  AAAA  2a04:4e42::820
example.com.  IN  AAAA  2a04:4e42:200::820
example.com.  IN  AAAA  2a04:4e42:400::820
example.com.  IN  AAAA  2a04:4e42:600::820
```

#### TXT record (domain ownership verification)

```dns
_shopware-challenge.example.com.  IN  TXT  "shopware-challenge=<organization-id>"
```

Determine the organization ID:
```bash
sw-paas org list
```

---

### DNS configuration overview

| Record type | Apex | Subdomain | Target | Count | Purpose |
|------------|:----:|:---------:|------|:------:|-------|
| `CNAME` | No | Yes | `cdn.shopware.shop` | 1 | Traffic routing |
| `A` | Yes | No | Fastly IPv4 | 4 | IPv4 routing |
| `AAAA` | Yes | No | Fastly IPv6 | 4 | IPv6 routing |
| `TXT` | Yes | No | Ownership proof | 1 | Domain validation |

---

### Step by step: set up a domain

#### Step 1: configure DNS

Create the records at your DNS provider/registrar (see above).

#### Step 2: check DNS propagation

```bash
# Subdomain
dig shop.example.com CNAME

# Apex domain
dig example.com A
dig example.com AAAA
dig _shopware-challenge.example.com TXT

# Test with a public DNS server
dig @8.8.8.8 example.com A
```

Online tool: https://www.whatsmydns.net

**DNS propagation**: normally 15-30 min, up to 48 hours.

#### Step 3: create the domain in PaaS

```bash
sw-paas domain create
```

Multiple domains are possible: repeat the command for each domain.

#### Step 4: redeploy the application

```bash
sw-paas application deploy create
# Alternatively:
sw-paas application update  # (the same commit can be used)
```

#### Step 5: configure Shopware

1. Shopware Admin → Sales Channel
2. Configure the domain
3. Assign the storefront

---

### Troubleshooting: DNS validation fails

**Symptoms:** error during `sw-paas domain create`

**Solutions:**

1. **Check the DNS records:**
   - Apex: are all 4 A records, all 4 AAAA records and the TXT record present?
   - Subdomain: CNAME pointing to `cdn.shopware.shop`?

2. **Wait for propagation:**
   - Run the `dig` commands
   - Use an online tool for global propagation

3. **Check the organization ID:**
   - `sw-paas org list`
   - TXT record: `shopware-challenge=<exact-org-id>`

4. **Rule out typos:**
   - Is the domain name correct?
   - No whitespace in the DNS records?

### Troubleshooting: domain created, no traffic response

**Symptoms:** domain created, but the site is unreachable

**Solutions:**

1. Was the deployment successful? → `sw-paas application deploy get`
2. Is the domain entered in the sales channel in the Shopware admin?
3. Clear the cache (test in a browser incognito window)
4. Is DNS propagation still in progress? Allow more time

---

## Fastly Snippets (PaaS Native)

### Storefront service snippets

```bash
composer require shopware/fastly-meta
```

- `FASTLY_API_KEY` and `FASTLY_SERVICE_ID`: provided automatically
- Snippets are installed/updated automatically during deployment
- No further action required

### Limitations

Currently snippets can only be configured for the `storefront` service.
Support for the `cdn` service is in development.

---

## Fastly (classic Shopware PaaS / Platform.sh)

Shopware 6.4.11+ required.

### Setup

1. Set `FASTLY_API_TOKEN` and `FASTLY_SERVICE_ID` in the environment / contact support
2. Install the Fastly package:
   ```bash
   composer require fastly
   ```
3. Disable caching in `.platform/routes.yaml`
4. Push → Fastly is activated

### Soft purge recommended

Prevents impact from large cache invalidations.
[Fastly Soft Purge Docs](https://developer.shopware.com/docs/guides/hosting/infrastructure/reverse-http-cache.html#fastly-soft-purge)
