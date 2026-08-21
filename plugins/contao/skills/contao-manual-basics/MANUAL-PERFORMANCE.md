# Contao 5.x — Performance

Sources:
- https://docs.contao.org/5.x/manual/en/performance/
- https://docs.contao.org/5.x/manual/en/performance/cronjobs/
- https://docs.contao.org/5.x/manual/en/performance/http-caching/
- https://docs.contao.org/5.x/manual/en/performance/php-setup/

---

## Contents

- [Overview](#overview)
- [1. Cronjob framework](#1-cronjob-framework)
- [2. HTTP caching](#2-http-caching)
- [3. PHP setup](#3-php-setup)
- [Summary: optimisation steps](#summary-optimisation-steps)

## Overview

Performance depends on several infrastructure factors: web server (Apache, Nginx, LiteSpeed), operating system and storage solution (HDD vs. SSD). There is no universally perfect configuration for Contao. This chapter is a collection of proven practices.

---

## 1. Cronjob framework

### Basic principle

Contao contains an integrated cronjob framework that allows developers to register cronjobs for extensions in a uniform way.

**Default behaviour**: cronjobs are executed on every website visit → this can impair performance.

**Recommendation**: set up real server cronjobs.

**Important**: not all registered jobs run on website visits. Backend search indexing happens **exclusively via a real CLI cronjob**.

### Configuration

The framework needs only **one cronjob executed every minute**, which manages all registered tasks:

```cron
* * * * * <php-binary> <contao-verzeichnis>/vendor/bin/contao-console contao:cron
```

**Practical example (Plesk)**:
```cron
* * * * * /opt/plesk/php/8.2/bin/php /var/www/vhosts/my.host.com/vendor/bin/contao-console contao:cron
```

---

## 2. HTTP caching

### Basic principle

Contao uses HTTP standards for caching. The system works with an **integrated cache proxy** that caches responses based on HTTP headers. The system works "out of the box" with good default values.

### Important Cache-Control headers

| Header | Description |
|--------|-------------|
| `private` | Only the browser may cache |
| `public` | Browsers and proxies may cache |
| `max-age` | Cache duration in seconds (private clients) |
| `s-maxage` | Cache duration for public caches |

**Example**:
```
Cache-Control: max-age=3600, s-maxage=7200, public
```
→ Private clients: 1 hour, public caches: 2 hours

### Cache status indicators

The `Contao-Cache` header shows the cache status:

| Value | Meaning |
|------|-----------|
| `miss` | No cache entry; Contao is executed |
| `miss/store` | A new cache entry is being stored |
| `fresh` | The response comes from the cache |

### When is caching disabled (private)?

The system forces `Cache-Control: private` when:
- An `Authorization` header is present (authentication)
- A PHP session is active
- Response cookies are set
- Relevant request cookies are present

### Cookie management

By default Contao ignores irrelevant cookies (e.g. `_ga_*`, `_pk_*`) and thereby enables better cache ratios.

Configuration via environment variables:
```env
COOKIE_ALLOW_LIST=PHPSESSID,csrf_https-contao_csrf_token,csrf_contao_csrf_token,trusted_device,REMEMBERME
COOKIE_REMOVE_FROM_DENY_LIST=__utm.+,AMP_TOKEN
```

### Cache tagging

Internally, responses receive `X-Cache-Tags` with references to database entries. When changes occur, Contao automatically invalidates all affected cache entries — precise invalidation instead of clearing the entire cache.

### Optimising query parameters

Tracking parameters such as `utm_*` disable caching. Solution:
```env
QUERY_PARAMS_REMOVE_FROM_DENY_LIST=fbclid
```

⚠️ **Warning**: disable Cache-Control if the parameters are actively used.

### Configuration recommendations

- Set the shared cache duration ≥ the private cache duration
- Frequently changed content: lower values
- Static content: higher values possible

---

## 3. PHP setup

### PHP version

Always use the latest PHP version supported by Contao — every version brings performance improvements.

| Contao version | Minimum PHP |
|----------------|-------------|
| 5.7+ | PHP 8.3 |
| 5.5+ | PHP 8.2 |
| 5.0+ | PHP 8.1 |

### SAPI (server API)

The server API determines how PHP communicates with the web server.

**Recommendation**: `fpm (php-fpm)` — the only SAPI with support for `fastcgi_finish_request()`. This allows Contao to do cleanup work **after** the response has been sent → shorter response time for visitors.

| SAPI | Recommendation |
|------|-----------|
| `fpm` (php-fpm) | ✅ Recommended |
| `litespeed` | ✅ Good |
| `mod_php` | ⚠️ Acceptable |
| `cgi` | ❌ Not recommended |

### OPcache

OPcache is the **single biggest performance gain** for PHP applications.

**How PHP works without OPcache**:
1. Lexing: breaking the source code into tokens
2. Parsing: making sense of the token sets
3. Compilation: translating PHP code into bytecode
4. Execution: executing the bytecode

OPcache stores the bytecode after step 3 in RAM or on the file system. On subsequent requests step 4 is executed directly — steps 1–3 are skipped.

**Recommended php.ini configuration:**

```ini
; Maximum RAM for OPcache (in MB)
opcache.memory_consumption = 128

; Maximum number of cached files
opcache.max_accelerated_files = 20000

; Internal string table (recommended for frameworks such as Symfony: 32–64 MB)
opcache.interned_strings_buffer = 32

; Do NOT check file changes automatically (better performance)
; Manual clearing on deployment required!
opcache.validate_timestamps = 0
```

**Clearing OPcache:**
- Contao Manager → system maintenance
- Deployment tools (cachetool, smart-core/accelerator-cache-bundle)

**Note**: CLI and web processes do not share a bytecode cache — clearing on the CLI side is not sufficient.

### Realpath cache

PHP caches file system information (`stat()` calls) within a process. These calls are relatively expensive.

**Recommended configuration:**

```ini
realpath_cache_size = 4096K
realpath_cache_ttl = 600
```

⚠️ **Warning**: if `open_basedir` is enabled, PHP disables the realpath cache at runtime! Many hosters use `open_basedir` as a security measure — this has a negative effect on performance.

---

## Summary: optimisation steps

| Measure | Effort | Effect |
|---------|---------|---------|
| Set up a real cronjob | Low | Medium |
| Update the PHP version | Medium | High |
| Use `php-fpm` | Medium | Medium |
| Configure OPcache | Low | Very high |
| `opcache.validate_timestamps=0` | Low | High |
| Increase the realpath cache | Low | Medium |
| Cookie management | Medium | High (cache hit rate) |
| SSD instead of HDD | High | High |
