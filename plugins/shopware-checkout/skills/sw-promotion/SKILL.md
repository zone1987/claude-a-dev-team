---
name: sw-promotion
description: >
  Promotions/Aktionen in Shopware 6 technisch: promotion-Entity (Rabattarten, Codes, Bedingungen/Rules, discount scopes),
  PromotionProcessor, eigene Rabatt-Logik. Trigger: "Promotion shopware", "Aktion technisch", "promotion entity",
  "Gutscheincode technisch", "PromotionDiscount", "promotion rule", "Rabattaktion plugin". Shopware 6.7.
---

# Shopware 6 — Promotions (technisch)

Aktionen sind `promotion`-Entities mit Rabatten (`promotion_discount`), optionalen Codes (`promotion_individual_code`)
und Bedingungen über Rules (`shopware-framework` → `sw-custom-rule`). Berechnung übernimmt der `PromotionProcessor`/-Collector.

- Rabattarten: prozentual, absolut, Festpreis, Versandkostenrabatt; Scope (Cart/Delivery/Set).
- Codes: kein Code, fester Code, individuelle Codes (generiert).
- Bedingungen (Vorbedingung/Rabatt-Regel) über den Rule Builder.
- Programmatisch per `promotion.repository` anlegen (Migration/Service).

Eigene, von Promotions nicht abgedeckte Rabattlogik → eigener Processor (`sw-cart-discount`/`sw-cart-processor`).
Betreibersicht (Aktion/Code anlegen): `shopware-merchant` (`sw-merchant-marketing-promotions`/`-codes`).
