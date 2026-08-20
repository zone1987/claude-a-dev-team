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
