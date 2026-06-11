---
name: sw-scss-variables
description: >
  SCSS-Variablen im Shopware-6-Storefront bereitstellen/überschreiben: Theme-Config-Felder → SCSS-Variablen,
  Variablen per Subscriber injizieren, theme_config(). Trigger: "SCSS Variable", "Theme-Variable", "sw-color-brand",
  "ThemeCompilerEnrichScssVariablesEvent", "scss variable subscriber", "konfigurierbare Farbe". Shopware 6.7.
---

# Shopware 6 — SCSS-Variablen

Konfigurierbare Werte (Farben, Maße) als SCSS-Variablen verfügbar machen. Zwei Wege:

1. **Theme-Config** (`theme.json` `fields`) → Variablen wie `$sw-color-brand-primary` automatisch verfügbar (`sw-theme-config`).
2. **Dynamisch per Subscriber** auf `ThemeCompilerEnrichScssVariablesEvent` (Plugin ohne eigenes Theme):

```php
public static function getSubscribedEvents(): array
{
    return [ ThemeCompilerEnrichScssVariablesEvent::class => 'enrich' ];
}
public function enrich(ThemeCompilerEnrichScssVariablesEvent $event): void
{
    $event->addVariable('ff-accent', $this->config->getString('FfPlugin.config.accent') ?: '#0af');
}
```

Im SCSS dann `color: $ff-accent;`. Im Twig `{{ theme_config('ff-accent') }}`. Variablen-Namen kebab-case ohne `$`.
