# Shopware 6 — SCSS variables

Make configurable values (colors, dimensions) available as SCSS variables. Two ways:

1. **Theme config** (`theme.json` `fields`) → variables like `$sw-color-brand-primary` available automatically (`sw-theme-config`).
2. **Dynamically via subscriber** on `ThemeCompilerEnrichScssVariablesEvent` (plugin without its own theme):

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

In SCSS then `color: $ff-accent;`. In Twig `{{ theme_config('ff-accent') }}`. Variable names kebab-case without `$`.
