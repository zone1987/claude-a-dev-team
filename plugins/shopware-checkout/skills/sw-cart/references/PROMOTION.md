# Shopware 6 — Promotions (technical)

Campaigns are `promotion` entities with discounts (`promotion_discount`), optional codes (`promotion_individual_code`)
and conditions via rules (`shopware-framework` → `sw-custom-rule`). The `PromotionProcessor`/collector handles the calculation.

- Discount types: percentage, absolute, fixed price, shipping cost discount; scope (cart/delivery/set).
- Codes: no code, fixed code, individual codes (generated).
- Conditions (precondition/discount rule) through the Rule Builder.
- Create programmatically via `promotion.repository` (migration/service).
 
Custom discount logic that promotions do not cover → your own processor (`sw-cart-discount`/`sw-cart-processor`).
Merchant view (creating a campaign/code): `shopware-merchant` (`sw-merchant-marketing-promotions`/`-codes`).
