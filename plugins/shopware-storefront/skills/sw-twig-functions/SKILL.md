---
name: sw-twig-functions
description: >
  Eingebaute Storefront-Twig-Funktionen in Shopware 6 nutzen: sw_icon, sw_thumbnails/searchMedia, seoUrl, sw_csrf,
  config/theme_config, sw_include. Trigger: "sw_icon", "seoUrl twig", "sw_thumbnails", "theme_config twig",
  "config() twig", "Twig Funktion storefront", "searchMedia". Shopware 6.7.
---

# Shopware 6 — Storefront-Twig-Funktionen

Wichtige eingebaute Funktionen/Helfer in Storefront-Templates:

| Funktion | Zweck |
|---|---|
| `{{ "key"\|trans }}` | Snippet-Übersetzung (`sw-storefront-translations`) |
| `{% sw_icon 'cart' %}` | SVG-Icon einbinden (`sw-storefront-icons`) |
| `{{ seoUrl('frontend.detail.page', {productId: id}) }}` | SEO-URL erzeugen (`sw-seo-urls`) |
| `{{ searchMedia(ids, context) }}` / `sw_thumbnails` | Medien/Thumbnails laden (`sw-storefront-assets`) |
| `{{ config('FfPlugin.config.x') }}` | System-/Plugin-Config lesen |
| `{{ theme_config('sw-color-brand-primary') }}` | Theme-Variable lesen (`sw-theme-config`) |
| `{% sw_include '...' %}` | überschreibbares Include |

Eigene Funktionen/Filter ergänzen: `sw-twig-extension`. Im JS auf gerenderte Daten via `data-*`-Attribute zugreifen (`sw-ajax-data`).
