---
name: sw-twig-templates
description: >
  Storefront-Twig-Templates in Shopware 6 überschreiben/erweitern: Verzeichnis-Konvention Resources/views/storefront,
  {% sw_extends %}, {% block %} überschreiben, {{ parent() }}, Header/Footer anpassen. Trigger: "Twig überschreiben",
  "sw_extends", "block überschreiben storefront", "Template anpassen", "Resources/views storefront", "parent() twig".
  Shopware 6.7.
---

# Shopware 6 — Storefront-Templates

Templates liegen unter `src/Resources/views/storefront/...` und spiegeln die Core-Pfade. Mit `sw_extends` wird das
Original geerbt und nur der gewünschte Block überschrieben.

```twig
{% sw_extends '@Storefront/storefront/page/product-detail/index.html.twig' %}

{% block page_product_detail_buy_container %}
    {{ parent() }}
    <div class="ff-hint">{{ "ff.hint"|trans }}</div>
{% endblock %}
```

`{% sw_extends %}` statt Twig-`extends` (Mehrfach-Vererbung über Plugins hinweg). `{{ parent() }}` behält Core-Inhalt.
Block-Namen aus dem Original übernehmen. Header/Footer über deren Blöcke. Eigene Funktionen: `sw-twig-functions`.

→ Template-Override-Details: [../sw-storefront-controller/references/storefront.md](../sw-storefront-controller/references/storefront.md)
