---
name: sw-customer
description: >
  Kunden im Shopware-6-Checkout-Kontext (technisch): customer-Entity, Registrierung/Login (Store-API/AccountService),
  Kundengruppen, Adressen, SalesChannelContext-Kunde, Events. Trigger: "Customer entity", "Kunde technisch", "Registrierung shopware",
  "AccountService", "customer.repository", "Kundengruppe technisch", "logged in customer context". Shopware 6.7.
---

# Shopware 6 — Customer (technisch)

Kunden sind `customer`-Entities (mit `customer_address`, `customer_group`). Im Storefront/Headless laufen Login/Register
über die Store-API bzw. den `AccountService`/`SalesChannelContextService`.

```php
$customer = $context->getCustomer();              // aktueller (eingeloggter) Kunde oder null
$this->customerRepository->search($criteria, $context->getContext());
```

- Registrierung/Login: Store-API (`shopware-api` → `sw-store-api-endpoints`), `sw-context-token` trägt den Login-State.
- Kundengruppen steuern Brutto/Netto-Anzeige und Sichtbarkeiten; Rules können auf Gruppe/Kunde matchen (`sw-custom-rule`).
- Events: `CustomerRegisterEvent`, `CustomerLoginEvent`, `customer.written` (`sw-events-subscriber`).

Datenmodell-Erweiterung am Kunden: `shopware-data` (`sw-entity-extension`/`sw-custom-fields`). Betreibersicht:
`shopware-merchant` (`sw-merchant-customers`).
