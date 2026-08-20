# Shopware 6 — Rate-Limiter

Shopware liefert Limiter (z.B. Login, Reset-Password, Contact-Form). Eigene Limits werden unter
`shopware.api.rate_limiter` / `config/packages` definiert und im Controller über den `RateLimiter` geprüft.

```php
$this->rateLimiter->ensureAccepted('ff_content_import', $cacheKey);
// wirft RateLimitExceededException bei Überschreitung
```

Policy-Typen: `time_backoff` (steigende Wartezeit) und `system_config`. Limiter zurücksetzen nach Erfolg via
`reset($key)`. Für öffentliche Store-API-Endpunkte sinnvoll gegen Missbrauch.

→ Policies, Konfig-Beispiele, Integration: [RATE-LIMITER-DETAIL.md](RATE-LIMITER-DETAIL.md)
