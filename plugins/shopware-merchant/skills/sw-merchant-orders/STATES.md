# Shopware 6 – State management (order/payment/delivery state)

Complete reference of all states, transitions and the payment logic after ordering.

Detailed documentation: [STATES-DETAIL.md](STATES-DETAIL.md)

## Three state dimensions

| State | Controls |
|---|---|
| Bestellstatus (Order state) | Overall condition of the order; cancelling releases the stock |
| Zahlungsstatus (Payment state) | Payment process (Offen (Open) → Bezahlt (Paid) / Fehlgeschlagen (Failed) / Erstattet (Refunded)) |
| Lieferstatus (Delivery state) | Shipping process (Offen → Geliefert (Shipped) → Retoure (Return)) |

## Source
https://docs.shopware.com/de/shopware-6-de/bestellungen/uebersicht
https://docs.shopware.com/de/shopware-6-de/bestellungen/zahlungsvorgang-nach-bestellung
