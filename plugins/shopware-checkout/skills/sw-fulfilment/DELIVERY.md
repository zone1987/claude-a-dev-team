# Shopware 6 — Lieferungen (Cart)

Der `DeliveryProcessor` berechnet Lieferungen (`Delivery`) inkl. Versandkosten aus der gewählten Versandart und deren
Preismatrix/Regeln.

- Eine `Delivery` bündelt Positionen mit Lieferdatum (`DeliveryDate` aus `DeliveryTime`) und Versandkosten (`ShippingCosts`).
- Versandkosten kommen aus der `shipping_method`-Preismatrix (Gewicht/Preis/Menge) bzw. Rules (`shopware-framework` → `sw-custom-rule`).
- Eigene Versandkostenlogik über einen Processor (`sw-cart-processor`) oder Anpassung der Versandart-Preise.

Versandarten/Preismatrix pflegen: `shopware-merchant` (`sw-merchant-settings-shipping-methods`). Eigene Versandart
technisch: `sw-shipping-method`. Lieferzeiten: `sw-merchant-settings-delivery-times`.
