# Shopware 6 — Deliveries (Cart)

The `DeliveryProcessor` calculates deliveries (`Delivery`) including shipping costs from the selected shipping method and its
price matrix/rules.

- A `Delivery` groups positions with a delivery date (`DeliveryDate` derived from `DeliveryTime`) and shipping costs (`ShippingCosts`).
- Shipping costs come from the `shipping_method` price matrix (weight/price/quantity) or from rules (`shopware-framework` → `sw-custom-rule`).
- Implement custom shipping cost logic in a processor (`sw-cart-processor`) or by adjusting the shipping method prices.

Maintaining shipping methods/price matrices: `shopware-merchant` (`sw-merchant-settings-shipping-methods`). Custom shipping method
on the technical side: `sw-shipping-method`. Delivery times: `sw-merchant-settings-delivery-times`.
