# Shopware Store API — vollständige Endpunktliste (6.7)

Base-URL `/store-api`. Auth-Header: `sw-access-key` (Pflicht), `sw-context-token` (Kontext/Session).
Quelle: offizielle OpenAPI (store-api-reference). 110 Operationen / 20 Bereiche.

## API

- `GET /script/{hook}` — Access point for different api logics which are provided by apps over script hooks
- `POST /script/{hook}` — Access point for different api logics which are provided by apps over script hooks

## Address

- `DELETE /account/address/{addressId}` — Delete an address of a customer
- `PATCH /account/address/default-billing/{addressId}` — Change a customer's default billing address
- `PATCH /account/address/default-shipping/{addressId}` — Change a customer's default shipping address
- `PATCH /account/address/{addressId}` — Modify an address of a customer
- `POST /account/address` — Create a new address for a customer
- `POST /account/list-address` — Fetch addresses of a customer

## App system

- `POST /app-system/{name}/generate-token` — Generate JWT token for app system backend

## Cart

- `DELETE /checkout/cart` — Delete a cart
- `DELETE /checkout/cart/line-item` — Remove items from the cart
- `GET /checkout/cart` — Fetch or create a cart
- `GET /shipping-cost/cart` — Calculate shipping costs for the cart
- `GET /shipping-cost/product/{productId}` — Calculate shipping costs for a product
- `PATCH /checkout/cart/line-item` — Update items in the cart
- `POST /checkout/cart/line-item` — Add items to the cart
- `POST /checkout/cart/line-item/delete` — Remove items from the cart

## Category

- `GET /category` — Fetch a list of categories
- `GET /category/{navigationId}` — Fetch a single category
- `GET /navigation/{activeId}/{rootId}` — Fetch a navigation menu
- `POST /category` — Fetch a list of categories
- `POST /category/{navigationId}` — Fetch a single category
- `POST /navigation/{activeId}/{rootId}` — Fetch a navigation menu

## Content

- `GET /cms/{id}` — Fetch and resolve a CMS page
- `GET /landing-page/{landingPageId}` — Fetch a landing page with the resolved CMS page
- `GET /media` — Fetch and resolve Media Entities
- `POST /cms/{id}` — Fetch and resolve a CMS page
- `POST /contact-form` — Submit a contact form message
- `POST /landing-page/{landingPageId}` — Fetch a landing page with the resolved CMS page
- `POST /media` — Fetch and resolve Media Entities
- `POST /revocation-request-form` — Submit a revocation request form message

## Document

- `GET /document/download/{documentId}/{deepLinkCode}` — Download generated document
- `POST /document/download/{documentId}/{deepLinkCode}` — Download generated document

## Experimental

- `GET /breadcrumb/{id}` — Fetch a breadcrumb
- `GET /cookie-groups` — Fetch all cookie groups

## Gateway

- `GET /checkout/gateway` — Call the checkout gateway
- `GET /context/gateway` — Call the context gateway
- `POST /context/gateway` — Call the context gateway

## Login & Registration

- `GET /customer-group-registration/config/{customerGroupId}` — Fetch registration settings for customer group
- `POST /account/login` — Log in a customer
- `POST /account/login/imitate-customer` — Imitate the log in as a customer
- `POST /account/logout` — Log out a customer
- `POST /account/register` — Register a customer
- `POST /account/register-confirm` — Confirm a customer registration

## Newsletter

- `POST /newsletter/confirm` — Confirm a newsletter registration
- `POST /newsletter/subscribe` — Create or remove a newsletter subscription
- `POST /newsletter/unsubscribe` — Remove a newsletter subscription

## Order

- `GET /order/download/{orderId}/{downloadId}` — Download a purchased file
- `POST /checkout/order` — Create an order from a cart
- `POST /order` — Fetch a list of orders
- `POST /order/payment` — Update the payment method of an order
- `POST /order/state/cancel` — Cancel an order

## Payment & Shipping

- `GET /handle-payment` — Initiate a payment for an order
- `GET /shipping-method` — Fetch shipping methods
- `POST /handle-payment` — Initiate a payment for an order
- `POST /shipping-method` — Fetch shipping methods

## Payment Method

- `GET /payment-method` — Loads all available payment methods
- `POST /payment-method` — Loads all available payment methods

## Product

- `GET /product` — Fetch a list of products
- `GET /product-export/{accessKey}/{fileName}` — Export product export
- `GET /product-listing/{categoryId}` — Fetch a product listing by category
- `GET /product/purchase-limit` — Fetch current purchase quantity limits for products
- `GET /product/{productId}` — Fetch a single product
- `GET /product/{productId}/cross-selling` — Fetch cross-selling groups of a product
- `GET /product/{productId}/find-variant` — Search for a matching variant by product options.
- `GET /product/{productId}/reviews` — Fetch product reviews
- `GET /search` — Search for products
- `GET /search-suggest` — Search for products (suggest)
- `POST /product` — Fetch a list of products
- `POST /product-listing/{categoryId}` — Fetch a product listing by category
- `POST /product/{productId}` — Fetch a single product
- `POST /product/{productId}/cross-selling` — Fetch cross-selling groups of a product
- `POST /product/{productId}/find-variant` — Search for a matching variant by product options.
- `POST /product/{productId}/review` — Save a product review
- `POST /product/{productId}/reviews` — Fetch product reviews
- `POST /search` — Search for products
- `POST /search-suggest` — Search for products (suggest)

## Profile

- `DELETE /account/customer` — Delete the customer's profile
- `POST /account/change-email` — Change the customer's email address
- `POST /account/change-language` — Change the customer's language.
- `POST /account/change-password` — Change the customer's password
- `POST /account/change-profile` — Change the customer's information
- `POST /account/convert-guest` — Convert a guest customer to a registered customer
- `POST /account/customer` — Get information about current customer
- `POST /account/customer-recovery-is-expired` — Checks if the customer recovery entry for a given hash is expired.
- `POST /account/newsletter-recipient` — Fetch newsletter recipients
- `POST /account/recovery-password` — Send a password recovery mail
- `POST /account/recovery-password-confirm` — Reset a password with recovery credentials

## Sitemap & Routes

- `GET /seo-url` — Fetch SEO routes
- `GET /sitemap` — Fetch sitemaps
- `GET /sitemap/{filePath}` — Download sitemap file
- `POST /seo-url` — Fetch SEO routes

## System & Context

- `GET /context` — Fetch the current context
- `GET /country` — Fetch countries
- `GET /country-state/{countryId}` — Fetch the states of a country
- `GET /currency` — Fetch currencies
- `GET /language` — Fetch languages
- `GET /salutation` — Fetch salutations
- `PATCH /context` — Modify the current context
- `POST /country` — Fetch countries
- `POST /country-state/{countryId}` — Fetch the states of a country
- `POST /currency` — Fetch currencies
- `POST /language` — Fetch languages
- `POST /salutation` — Fetch salutations

## System Info & Health Check

- `GET /_info/openapi3.json` — Get OpenAPI Specification
- `GET /_info/routes` — Get API routes

## Wishlist

- `DELETE /customer/wishlist/delete/{productId}` — Remove a product from a wishlist
- `POST /customer/wishlist` — Fetch a wishlist
- `POST /customer/wishlist/add/{productId}` — Add a product to a wishlist
- `POST /customer/wishlist/merge` — Create a wishlist for a customer

