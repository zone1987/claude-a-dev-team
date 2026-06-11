---
name: sw-storefront-icons
description: >
  Eigene SVG-Icons im Shopware-6-Storefront: Icon-Set unter Resources/app/storefront/dist/assets/icon, sw_icon
  mit pack, Icon überschreiben. Trigger: "sw_icon", "eigenes Icon Storefront", "Icon hinzufügen", "icon pack",
  "SVG icon storefront", "Icon überschreiben". Shopware 6.7.
---

# Shopware 6 — Storefront-Icons

Icons werden über `sw_icon` eingebunden. Eigene Icons als SVG in einem Icon-Pack ablegen
(`src/Resources/app/storefront/dist/assets/icon/<pack>/<name>.svg`).

```twig
{% sw_icon 'heart' style { 'pack': 'ff', 'size': 'sm' } %}
```

Ein Core-Icon überschreiben = gleichnamige SVG im Default-Pack des eigenen Plugins bereitstellen (Theme-Inheritance
greift). `size`/`color` über `style`-Map oder CSS. Größere Grafiken als Asset (`sw-storefront-assets`), nicht als Icon.
