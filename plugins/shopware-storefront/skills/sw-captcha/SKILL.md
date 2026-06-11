---
name: sw-captcha
description: >
  Captcha im Shopware-6-Storefront: eingebaute Captchas (Honeypot, basicCaptcha, googleReCaptcha) nutzen/konfigurieren
  und ein eigenes Captcha via AbstractCaptcha registrieren. Trigger: "Captcha", "AbstractCaptcha", "Honeypot",
  "reCaptcha shopware", "eigenes Captcha", "Formularschutz storefront". Shopware 6.7.
---

# Shopware 6 — Captcha

Formulare (Kontakt, Registrierung) werden über Captchas geschützt (konfigurierbar in den Basic-Information-Settings).
Eigenes Captcha über `AbstractCaptcha`:

```php
class FfCaptcha extends AbstractCaptcha
{
    public function supports(Request $request, array $captchaConfig): bool { return ($captchaConfig['active'] ?? false); }
    public function isValid(Request $request, array $captchaConfig): bool { /* Validierung */ return true; }
    public function getName(): string { return 'ffCaptcha'; }
}
```

Registrierung via `shopware.storefront.captcha`-Tag; Frontend-Markup im Form-Template ergänzen. Für die meisten Fälle
reichen die eingebauten Captchas (Honeypot serverseitig, reCaptcha v2/v3) — eigenes nur bei Sonderanforderung.
