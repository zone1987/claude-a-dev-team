# Shopware 6 — Storefront icons

Icons are included via `sw_icon`. Place custom icons as SVG in an icon pack
(`src/Resources/app/storefront/dist/assets/icon/<pack>/<name>.svg`).

```twig
{% sw_icon 'heart' style { 'pack': 'ff', 'size': 'sm' } %}
```

To override a core icon, provide an SVG with the same name in your own plugin's default pack (theme inheritance
applies). Set `size`/`color` via the `style` map or CSS. Use larger graphics as assets (`sw-storefront-assets`), not as icons.
