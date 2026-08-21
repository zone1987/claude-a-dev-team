# Shopware 6 — Storefront Twig functions

Important built-in functions/helpers in Storefront templates:

| Function | Purpose |
|---|---|
| `{{ "key"\|trans }}` | Snippet translation (`sw-storefront-translations`) |
| `{% sw_icon 'cart' %}` | Include an SVG icon (`sw-storefront-icons`) |
| `{{ seoUrl('frontend.detail.page', {productId: id}) }}` | Generate a SEO URL (`sw-seo-urls`) |
| `{{ searchMedia(ids, context) }}` / `sw_thumbnails` | Load media/thumbnails (`sw-storefront-assets`) |
| `{{ config('FfPlugin.config.x') }}` | Read system/plugin config |
| `{{ theme_config('sw-color-brand-primary') }}` | Read a theme variable (`sw-theme-config`) |
| `{% sw_include '...' %}` | Overridable include |

Add your own functions/filters: `sw-twig-extension`. In JS, access rendered data via `data-*` attributes (`sw-ajax-data`).
