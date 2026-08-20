# Shopware 6 — Customer (technical)

Customers are `customer` entities (together with `customer_address`, `customer_group`). In the storefront and headless
setups login/registration run through the Store API or the `AccountService`/`SalesChannelContextService`.

```php
$customer = $context->getCustomer();              // current (logged-in) customer or null
$this->customerRepository->search($criteria, $context->getContext());
```

- Registration/login: Store API (`shopware-api` → `sw-store-api-endpoints`), `sw-context-token` carries the login state.
- Customer groups control gross/net display and visibilities; rules can match on group/customer (`sw-custom-rule`).
- Events: `CustomerRegisterEvent`, `CustomerLoginEvent`, `customer.written` (`sw-events-subscriber`).

Extending the customer data model: `shopware-data` (`sw-entity-extension`/`sw-custom-fields`). Merchant view:
`shopware-merchant` (`sw-merchant-customers`).
