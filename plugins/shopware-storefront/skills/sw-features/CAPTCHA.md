# Shopware 6 — Captcha

Forms (contact, registration) are protected by captchas (configurable in the basic information settings).
Add a custom captcha via `AbstractCaptcha`:

```php
class FfCaptcha extends AbstractCaptcha
{
    public function supports(Request $request, array $captchaConfig): bool { return ($captchaConfig['active'] ?? false); }
    public function isValid(Request $request, array $captchaConfig): bool { /* validation */ return true; }
    public function getName(): string { return 'ffCaptcha'; }
}
```

Register it via the `shopware.storefront.captcha` tag; add the frontend markup in the form template. For most cases
the built-in captchas are sufficient (server-side honeypot, reCaptcha v2/v3) — write your own only for special requirements.
