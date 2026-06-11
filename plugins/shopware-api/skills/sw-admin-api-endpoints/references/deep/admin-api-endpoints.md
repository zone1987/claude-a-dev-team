# Shopware Admin API — Vollständige Endpunkt-Referenz

**API-Version:** 6.7.9999999-dev | **Quelle:** `adminapi.json` | **Gesamt-Operationen:** 1093 | **Tags:** 143

**Basis:** `{shop}/api` | **Security:** `oAuth` (OAuth2 password / clientCredentials, Token via `POST /api/oauth/token`)

---

## ACL Role (7 ops)

```
GET    /acl-role                  — List with basic information of Acl Role resources.
POST   /acl-role                  — Create a new Acl Role resources.
GET    /acl-role/{id}             — Detailed information about a Acl Role resource.
DELETE /acl-role/{id}             — Delete a Acl Role resource.
PATCH  /acl-role/{id}             — Partially update information about a Acl Role resource.
POST   /aggregate/acl-role        — Aggregate for the Acl Role resources.
POST   /search/acl-role           — Search for the Acl Role resources.
```

## App (7 ops)

```
GET    /app                       — List with basic information of App resources.
POST   /app                       — Create a new App resources.
GET    /app/{id}                  — Detailed information about a App resource.
DELETE /app/{id}                  — Delete a App resource.
PATCH  /app/{id}                  — Partially update information about a App resource.
POST   /aggregate/app             — Aggregate for the App resources.
POST   /search/app                — Search for the App resources.
```

## App Action Button (7 ops)

```
GET    /app-action-button         — List with basic information of App Action Button resources.
POST   /app-action-button         — Create a new App Action Button resources.
GET    /app-action-button/{id}    — Detailed information about a App Action Button resource.
DELETE /app-action-button/{id}    — Delete a App Action Button resource.
PATCH  /app-action-button/{id}    — Partially update information about a App Action Button resource.
POST   /aggregate/app-action-button — Aggregate for the App Action Button resources.
POST   /search/app-action-button  — Search for the App Action Button resources.
```

## App Administration Snippet (7 ops)

```
GET    /app-administration-snippet       — List with basic information of App Administration Snippet resources.
POST   /app-administration-snippet       — Create a new App Administration Snippet resources.
GET    /app-administration-snippet/{id}  — Detailed information about a App Administration Snippet resource.
DELETE /app-administration-snippet/{id}  — Delete a App Administration Snippet resource.
PATCH  /app-administration-snippet/{id}  — Partially update information about a App Administration Snippet resource.
POST   /aggregate/app-administration-snippet — Aggregate for the App Administration Snippet resources.
POST   /search/app-administration-snippet    — Search for the App Administration Snippet resources.
```

## App Cms Block (7 ops)

```
GET    /app-cms-block             — List with basic information of App Cms Block resources.
POST   /app-cms-block             — Create a new App Cms Block resources.
GET    /app-cms-block/{id}        — Detailed information about a App Cms Block resource.
DELETE /app-cms-block/{id}        — Delete a App Cms Block resource.
PATCH  /app-cms-block/{id}        — Partially update information about a App Cms Block resource.
POST   /aggregate/app-cms-block   — Aggregate for the App Cms Block resources.
POST   /search/app-cms-block      — Search for the App Cms Block resources.
```

## App Flow Action (7 ops)

```
GET    /app-flow-action           — List with basic information of App Flow Action resources.
POST   /app-flow-action           — Create a new App Flow Action resources.
GET    /app-flow-action/{id}      — Detailed information about a App Flow Action resource.
DELETE /app-flow-action/{id}      — Delete a App Flow Action resource.
PATCH  /app-flow-action/{id}      — Partially update information about a App Flow Action resource.
POST   /aggregate/app-flow-action — Aggregate for the App Flow Action resources.
POST   /search/app-flow-action    — Search for the App Flow Action resources.
```

## App Flow Event (7 ops)

```
GET    /app-flow-event            — List with basic information of App Flow Event resources.
POST   /app-flow-event            — Create a new App Flow Event resources.
GET    /app-flow-event/{id}       — Detailed information about a App Flow Event resource.
DELETE /app-flow-event/{id}       — Delete a App Flow Event resource.
PATCH  /app-flow-event/{id}       — Partially update information about a App Flow Event resource.
POST   /aggregate/app-flow-event  — Aggregate for the App Flow Event resources.
POST   /search/app-flow-event     — Search for the App Flow Event resources.
```

## App Mcp Prompt (7 ops)

```
GET    /app-mcp-prompt            — List with basic information of App Mcp Prompt resources.
POST   /app-mcp-prompt            — Create a new App Mcp Prompt resources.
GET    /app-mcp-prompt/{id}       — Detailed information about a App Mcp Prompt resource.
DELETE /app-mcp-prompt/{id}       — Delete a App Mcp Prompt resource.
PATCH  /app-mcp-prompt/{id}       — Partially update information about a App Mcp Prompt resource.
POST   /aggregate/app-mcp-prompt  — Aggregate for the App Mcp Prompt resources.
POST   /search/app-mcp-prompt     — Search for the App Mcp Prompt resources.
```

## App Mcp Resource (7 ops)

```
GET    /app-mcp-resource          — List with basic information of App Mcp Resource resources.
POST   /app-mcp-resource          — Create a new App Mcp Resource resources.
GET    /app-mcp-resource/{id}     — Detailed information about a App Mcp Resource resource.
DELETE /app-mcp-resource/{id}     — Delete a App Mcp Resource resource.
PATCH  /app-mcp-resource/{id}     — Partially update information about a App Mcp Resource resource.
POST   /aggregate/app-mcp-resource — Aggregate for the App Mcp Resource resources.
POST   /search/app-mcp-resource   — Search for the App Mcp Resource resources.
```

## App Mcp Tool (7 ops)

```
GET    /app-mcp-tool              — List with basic information of App Mcp Tool resources.
POST   /app-mcp-tool              — Create a new App Mcp Tool resources.
GET    /app-mcp-tool/{id}         — Detailed information about a App Mcp Tool resource.
DELETE /app-mcp-tool/{id}         — Delete a App Mcp Tool resource.
PATCH  /app-mcp-tool/{id}         — Partially update information about a App Mcp Tool resource.
POST   /aggregate/app-mcp-tool    — Aggregate for the App Mcp Tool resources.
POST   /search/app-mcp-tool       — Search for the App Mcp Tool resources.
```

## App Payment Method (7 ops)

```
GET    /app-payment-method        — List with basic information of App Payment Method resources.
POST   /app-payment-method        — Create a new App Payment Method resources.
GET    /app-payment-method/{id}   — Detailed information about a App Payment Method resource.
DELETE /app-payment-method/{id}   — Delete a App Payment Method resource.
PATCH  /app-payment-method/{id}   — Partially update information about a App Payment Method resource.
POST   /aggregate/app-payment-method — Aggregate for the App Payment Method resources.
POST   /search/app-payment-method — Search for the App Payment Method resources.
```

## App Script Condition (7 ops)

```
GET    /app-script-condition      — List with basic information of App Script Condition resources.
POST   /app-script-condition      — Create a new App Script Condition resources.
GET    /app-script-condition/{id} — Detailed information about a App Script Condition resource.
DELETE /app-script-condition/{id} — Delete a App Script Condition resource.
PATCH  /app-script-condition/{id} — Partially update information about a App Script Condition resource.
POST   /aggregate/app-script-condition — Aggregate for the App Script Condition resources.
POST   /search/app-script-condition    — Search for the App Script Condition resources.
```

## App Shipping Method (7 ops)

```
GET    /app-shipping-method       — List with basic information of App Shipping Method resources.
POST   /app-shipping-method       — Create a new App Shipping Method resources.
GET    /app-shipping-method/{id}  — Detailed information about a App Shipping Method resource.
DELETE /app-shipping-method/{id}  — Delete a App Shipping Method resource.
PATCH  /app-shipping-method/{id}  — Partially update information about a App Shipping Method resource.
POST   /aggregate/app-shipping-method — Aggregate for the App Shipping Method resources.
POST   /search/app-shipping-method    — Search for the App Shipping Method resources.
```

## App System (5 ops)

```
POST   /_action/app-system/secret/rotate          — Initiate secret rotation for the calling app
GET    /app-system/privileges/requested           — Get requested privileges for all apps
GET    /app-system/shop/verify                    — Verify a shop's APP_URL
PATCH  /app-system/{appName}/privileges           — Accept or revoke privileges for an app
GET    /app-system/{appName}/privileges/accepted  — Get accepted privileges for an app
```

## App Template (7 ops)

```
GET    /app-template              — List with basic information of App Template resources.
POST   /app-template              — Create a new App Template resources.
GET    /app-template/{id}         — Detailed information about a App Template resource.
DELETE /app-template/{id}         — Delete a App Template resource.
PATCH  /app-template/{id}         — Partially update information about a App Template resource.
POST   /aggregate/app-template    — Aggregate for the App Template resources.
POST   /search/app-template       — Search for the App Template resources.
```

## Asset Management (9 ops)

```
POST   /_action/media/external-link                    — Create external media link
POST   /_action/media/presign-upload                   — Prepare a presigned upload
POST   /_action/media/upload                           — Upload a new media file
POST   /_action/media/upload_by_url                    — Upload a media file from URL
POST   /_action/media/{mediaId}/external-thumbnails    — Add external thumbnails to media
DELETE /_action/media/{mediaId}/external-thumbnails    — Delete all external thumbnails from media
POST   /_action/media/{mediaId}/finalize-upload        — Finalize a presigned upload
POST   /_action/media/{mediaId}/upload                 — Upload a file to a media entity
POST   /_action/media/{mediaId}/video-cover            — Assign or remove a video cover image
```

## Authorization & Authentication (2 ops)

```
POST   /_action/user/logout  — Logout the current user
POST   /oauth/token          — Fetch an access token
```

## Bulk Operations (1 op)

```
POST   /_action/sync  — Bulk edit entities
```

## Category (7 ops)

```
GET    /category                  — List with basic information of Category resources.
POST   /category                  — Create a new Category resources.
GET    /category/{id}             — Detailed information about a Category resource.
DELETE /category/{id}             — Delete a Category resource.
PATCH  /category/{id}             — Partially update information about a Category resource.
POST   /aggregate/category        — Aggregate for the Category resources.
POST   /search/category           — Search for the Category resources.
```

## Cms Block (7 ops)

```
GET    /cms-block                 — List with basic information of Cms Block resources.
POST   /cms-block                 — Create a new Cms Block resources.
GET    /cms-block/{id}            — Detailed information about a Cms Block resource.
DELETE /cms-block/{id}            — Delete a Cms Block resource.
PATCH  /cms-block/{id}            — Partially update information about a Cms Block resource.
POST   /aggregate/cms-block       — Aggregate for the Cms Block resources.
POST   /search/cms-block          — Search for the Cms Block resources.
```

## Cms Page (7 ops)

```
GET    /cms-page                  — List with basic information of Cms Page resources.
POST   /cms-page                  — Create a new Cms Page resources.
GET    /cms-page/{id}             — Detailed information about a Cms Page resource.
DELETE /cms-page/{id}             — Delete a Cms Page resource.
PATCH  /cms-page/{id}             — Partially update information about a Cms Page resource.
POST   /aggregate/cms-page        — Aggregate for the Cms Page resources.
POST   /search/cms-page           — Search for the Cms Page resources.
```

## Cms Section (7 ops)

```
GET    /cms-section               — List with basic information of Cms Section resources.
POST   /cms-section               — Create a new Cms Section resources.
GET    /cms-section/{id}          — Detailed information about a Cms Section resource.
DELETE /cms-section/{id}          — Delete a Cms Section resource.
PATCH  /cms-section/{id}          — Partially update information about a Cms Section resource.
POST   /aggregate/cms-section     — Aggregate for the Cms Section resources.
POST   /search/cms-section        — Search for the Cms Section resources.
```

## Cms Slot (7 ops)

```
GET    /cms-slot                  — List with basic information of Cms Slot resources.
POST   /cms-slot                  — Create a new Cms Slot resources.
GET    /cms-slot/{id}             — Detailed information about a Cms Slot resource.
DELETE /cms-slot/{id}             — Delete a Cms Slot resource.
PATCH  /cms-slot/{id}             — Partially update information about a Cms Slot resource.
POST   /aggregate/cms-slot        — Aggregate for the Cms Slot resources.
POST   /search/cms-slot           — Search for the Cms Slot resources.
```

## Consent Management (3 ops) [Experimental]

```
GET    /consents         — List all consents for current user
POST   /consents/accept  — Accept a consent
POST   /consents/revoke  — Revoke a consent
```

## Country (7 ops)

```
GET    /country                   — List with basic information of Country resources.
POST   /country                   — Create a new Country resources.
GET    /country/{id}              — Detailed information about a Country resource.
DELETE /country/{id}              — Delete a Country resource.
PATCH  /country/{id}              — Partially update information about a Country resource.
POST   /aggregate/country         — Aggregate for the Country resources.
POST   /search/country            — Search for the Country resources.
```

## Country State (7 ops)

```
GET    /country-state             — List with basic information of Country State resources.
POST   /country-state             — Create a new Country State resources.
GET    /country-state/{id}        — Detailed information about a Country State resource.
DELETE /country-state/{id}        — Delete a Country State resource.
PATCH  /country-state/{id}        — Partially update information about a Country State resource.
POST   /aggregate/country-state   — Aggregate for the Country State resources.
POST   /search/country-state      — Search for the Country State resources.
```

## Currency (7 ops)

```
GET    /currency                  — List with basic information of Currency resources.
POST   /currency                  — Create a new Currency resources.
GET    /currency/{id}             — Detailed information about a Currency resource.
DELETE /currency/{id}             — Delete a Currency resource.
PATCH  /currency/{id}             — Partially update information about a Currency resource.
POST   /aggregate/currency        — Aggregate for the Currency resources.
POST   /search/currency           — Search for the Currency resources.
```

## Currency Country Rounding (7 ops)

```
GET    /currency-country-rounding        — List with basic information of Currency Country Rounding resources.
POST   /currency-country-rounding        — Create a new Currency Country Rounding resources.
GET    /currency-country-rounding/{id}   — Detailed information about a Currency Country Rounding resource.
DELETE /currency-country-rounding/{id}   — Delete a Currency Country Rounding resource.
PATCH  /currency-country-rounding/{id}   — Partially update information about a Currency Country Rounding resource.
POST   /aggregate/currency-country-rounding — Aggregate for the Currency Country Rounding resources.
POST   /search/currency-country-rounding    — Search for the Currency Country Rounding resources.
```

## Custom Entity (7 ops)

```
GET    /custom-entity             — List with basic information of Custom Entity resources.
POST   /custom-entity             — Create a new Custom Entity resources.
GET    /custom-entity/{id}        — Detailed information about a Custom Entity resource.
DELETE /custom-entity/{id}        — Delete a Custom Entity resource.
PATCH  /custom-entity/{id}        — Partially update information about a Custom Entity resource.
POST   /aggregate/custom-entity   — Aggregate for the Custom Entity resources.
POST   /search/custom-entity      — Search for the Custom Entity resources.
```

## Custom Field (7 ops)

```
GET    /custom-field              — List with basic information of Custom Field resources.
POST   /custom-field              — Create a new Custom Field resources.
GET    /custom-field/{id}         — Detailed information about a Custom Field resource.
DELETE /custom-field/{id}         — Delete a Custom Field resource.
PATCH  /custom-field/{id}         — Partially update information about a Custom Field resource.
POST   /aggregate/custom-field    — Aggregate for the Custom Field resources.
POST   /search/custom-field       — Search for the Custom Field resources.
```

## Custom Field Set (7 ops)

```
GET    /custom-field-set          — List with basic information of Custom Field Set resources.
POST   /custom-field-set          — Create a new Custom Field Set resources.
GET    /custom-field-set/{id}     — Detailed information about a Custom Field Set resource.
DELETE /custom-field-set/{id}     — Delete a Custom Field Set resource.
PATCH  /custom-field-set/{id}     — Partially update information about a Custom Field Set resource.
POST   /aggregate/custom-field-set — Aggregate for the Custom Field Set resources.
POST   /search/custom-field-set   — Search for the Custom Field Set resources.
```

## Custom Field Set Relation (7 ops)

```
GET    /custom-field-set-relation        — List with basic information of Custom Field Set Relation resources.
POST   /custom-field-set-relation        — Create a new Custom Field Set Relation resources.
GET    /custom-field-set-relation/{id}   — Detailed information about a Custom Field Set Relation resource.
DELETE /custom-field-set-relation/{id}   — Delete a Custom Field Set Relation resource.
PATCH  /custom-field-set-relation/{id}   — Partially update information about a Custom Field Set Relation resource.
POST   /aggregate/custom-field-set-relation — Aggregate for the Custom Field Set Relation resources.
POST   /search/custom-field-set-relation    — Search for the Custom Field Set Relation resources.
```

## Customer (7 ops)

```
GET    /customer                  — List with basic information of Customer resources.
POST   /customer                  — Create a new Customer resources.
GET    /customer/{id}             — Detailed information about a Customer resource.
DELETE /customer/{id}             — Delete a Customer resource.
PATCH  /customer/{id}             — Partially update information about a Customer resource.
POST   /aggregate/customer        — Aggregate for the Customer resources.
POST   /search/customer           — Search for the Customer resources.
```

## Customer Address (7 ops)

```
GET    /customer-address          — List with basic information of Customer Address resources.
POST   /customer-address          — Create a new Customer Address resources.
GET    /customer-address/{id}     — Detailed information about a Customer Address resource.
DELETE /customer-address/{id}     — Delete a Customer Address resource.
PATCH  /customer-address/{id}     — Partially update information about a Customer Address resource.
POST   /aggregate/customer-address — Aggregate for the Customer Address resources.
POST   /search/customer-address   — Search for the Customer Address resources.
```

## Customer Group (7 ops)

```
GET    /customer-group            — List with basic information of Customer Group resources.
POST   /customer-group            — Create a new Customer Group resources.
GET    /customer-group/{id}       — Detailed information about a Customer Group resource.
DELETE /customer-group/{id}       — Delete a Customer Group resource.
PATCH  /customer-group/{id}       — Partially update information about a Customer Group resource.
POST   /aggregate/customer-group  — Aggregate for the Customer Group resources.
POST   /search/customer-group     — Search for the Customer Group resources.
```

## Customer Recovery (7 ops)

```
GET    /customer-recovery         — List with basic information of Customer Recovery resources.
POST   /customer-recovery         — Create a new Customer Recovery resources.
GET    /customer-recovery/{id}    — Detailed information about a Customer Recovery resource.
DELETE /customer-recovery/{id}    — Delete a Customer Recovery resource.
PATCH  /customer-recovery/{id}    — Partially update information about a Customer Recovery resource.
POST   /aggregate/customer-recovery — Aggregate for the Customer Recovery resources.
POST   /search/customer-recovery  — Search for the Customer Recovery resources.
```

## Customer Wishlist (7 ops)

```
GET    /customer-wishlist         — List with basic information of Customer Wishlist resources.
POST   /customer-wishlist         — Create a new Customer Wishlist resources.
GET    /customer-wishlist/{id}    — Detailed information about a Customer Wishlist resource.
DELETE /customer-wishlist/{id}    — Delete a Customer Wishlist resource.
PATCH  /customer-wishlist/{id}    — Partially update information about a Customer Wishlist resource.
POST   /aggregate/customer-wishlist — Aggregate for the Customer Wishlist resources.
POST   /search/customer-wishlist  — Search for the Customer Wishlist resources.
```

## Customer Wishlist Product (7 ops)

```
GET    /customer-wishlist-product        — List with basic information of Customer Wishlist Product resources.
POST   /customer-wishlist-product        — Create a new Customer Wishlist Product resources.
GET    /customer-wishlist-product/{id}   — Detailed information about a Customer Wishlist Product resource.
DELETE /customer-wishlist-product/{id}   — Delete a Customer Wishlist Product resource.
PATCH  /customer-wishlist-product/{id}   — Partially update information about a Customer Wishlist Product resource.
POST   /aggregate/customer-wishlist-product — Aggregate for the Customer Wishlist Product resources.
POST   /search/customer-wishlist-product    — Search for the Customer Wishlist Product resources.
```

## Customer impersonation (1 op)

```
POST   /_proxy/generate-imitate-customer-token  — Generate a customer impersonation token
```

## Delivery Time (7 ops)

```
GET    /delivery-time             — List with basic information of Delivery Time resources.
POST   /delivery-time             — Create a new Delivery Time resources.
GET    /delivery-time/{id}        — Detailed information about a Delivery Time resource.
DELETE /delivery-time/{id}        — Delete a Delivery Time resource.
PATCH  /delivery-time/{id}        — Partially update information about a Delivery Time resource.
POST   /aggregate/delivery-time   — Aggregate for the Delivery Time resources.
POST   /search/delivery-time      — Search for the Delivery Time resources.
```

## Document (7 ops)

```
GET    /document                  — List with basic information of Document resources.
POST   /document                  — Create a new Document resources.
GET    /document/{id}             — Detailed information about a Document resource.
DELETE /document/{id}             — Delete a Document resource.
PATCH  /document/{id}             — Partially update information about a Document resource.
POST   /aggregate/document        — Aggregate for the Document resources.
POST   /search/document           — Search for the Document resources.
```

## Document Base Config (7 ops)

```
GET    /document-base-config      — List with basic information of Document Base Config resources.
POST   /document-base-config      — Create a new Document Base Config resources.
GET    /document-base-config/{id} — Detailed information about a Document Base Config resource.
DELETE /document-base-config/{id} — Delete a Document Base Config resource.
PATCH  /document-base-config/{id} — Partially update information about a Document Base Config resource.
POST   /aggregate/document-base-config — Aggregate for the Document Base Config resources.
POST   /search/document-base-config    — Search for the Document Base Config resources.
```

## Document Base Config Sales Channel (7 ops)

```
GET    /document-base-config-sales-channel       — List with basic information of Document Base Config Sales Channel resources.
POST   /document-base-config-sales-channel       — Create a new Document Base Config Sales Channel resources.
GET    /document-base-config-sales-channel/{id}  — Detailed information about a Document Base Config Sales Channel resource.
DELETE /document-base-config-sales-channel/{id}  — Delete a Document Base Config Sales Channel resource.
PATCH  /document-base-config-sales-channel/{id}  — Partially update information about a Document Base Config Sales Channel resource.
POST   /aggregate/document-base-config-sales-channel — Aggregate for the Document Base Config Sales Channel resources.
POST   /search/document-base-config-sales-channel    — Search for the Document Base Config Sales Channel resources.
```

## Document File (7 ops)

```
GET    /document-file             — List with basic information of Document File resources.
POST   /document-file             — Create a new Document File resources.
GET    /document-file/{id}        — Detailed information about a Document File resource.
DELETE /document-file/{id}        — Delete a Document File resource.
PATCH  /document-file/{id}        — Partially update information about a Document File resource.
POST   /aggregate/document-file   — Aggregate for the Document File resources.
POST   /search/document-file      — Search for the Document File resources.
```

## Document Management (4 ops)

```
POST   /_action/document/{documentId}/upload           — Upload a file for a document
GET    /_action/document/{documentId}/{deepLinkCode}   — Download a document
POST   /_action/order/document/download                — Download a documents
POST   /_action/order/document/{documentTypeName}/create — Create documents for orders
```

## Document Type (7 ops)

```
GET    /document-type             — List with basic information of Document Type resources.
POST   /document-type             — Create a new Document Type resources.
GET    /document-type/{id}        — Detailed information about a Document Type resource.
DELETE /document-type/{id}        — Delete a Document Type resource.
PATCH  /document-type/{id}        — Partially update information about a Document Type resource.
POST   /aggregate/document-type   — Aggregate for the Document Type resources.
POST   /search/document-type      — Search for the Document Type resources.
```

## Email support validation (1 op)

```
POST   /_action/validation/email  — Email support.
```

## Experimental (30 ops)

```
POST   /_action/integration/{integrationId}/mcp-allowlist  — Save MCP allowlist for an integration
GET    /_action/mcp/capabilities                           — List all registered MCP capabilities
GET    /_action/mcp/tools                                  — List registered MCP tools
POST   /_action/sso/invite-user                            — Experimental: Invite a new SSO user
POST   /_action/user/{userId}/mcp-allowlist                — Save MCP allowlist for a user
GET    /_info/is-sso                                       — Experimental: Is SSO environment
POST   /_mcp                                               — MCP JSON-RPC endpoint
GET    /_mcp                                               — MCP SSE stream
DELETE /_mcp                                               — Close MCP session
OPTIONS /_mcp                                              — MCP CORS preflight
POST   /aggregate/sales-channel-tracking-customer          — Aggregate for the Sales Channel Tracking Customer resources. [Experimental]
POST   /aggregate/sales-channel-tracking-order             — Aggregate for the Sales Channel Tracking Order resources. [Experimental]
GET    /consents                                           — List all consents for current user [Experimental]
POST   /consents/accept                                    — Accept a consent [Experimental]
POST   /consents/revoke                                    — Revoke a consent [Experimental]
GET    /oauth/sso/auth                                     — Experimental: Redirect to SSO login
GET    /oauth/sso/code                                     — Experimental: Callback for SSO login
GET    /oauth/sso/config                                   — Experimental: Loads SSO login configuration.
GET    /sales-channel-tracking-customer                    — List with basic information of Sales Channel Tracking Customer resources. [Experimental]
POST   /sales-channel-tracking-customer                    — Create a new Sales Channel Tracking Customer resources. [Experimental]
GET    /sales-channel-tracking-customer/{id}               — Detailed information about a Sales Channel Tracking Customer resource. [Experimental]
DELETE /sales-channel-tracking-customer/{id}               — Delete a Sales Channel Tracking Customer resource. [Experimental]
PATCH  /sales-channel-tracking-customer/{id}               — Partially update information about a Sales Channel Tracking Customer resource. [Experimental]
GET    /sales-channel-tracking-order                       — List with basic information of Sales Channel Tracking Order resources. [Experimental]
POST   /sales-channel-tracking-order                       — Create a new Sales Channel Tracking Order resources. [Experimental]
GET    /sales-channel-tracking-order/{id}                  — Detailed information about a Sales Channel Tracking Order resource. [Experimental]
DELETE /sales-channel-tracking-order/{id}                  — Delete a Sales Channel Tracking Order resource. [Experimental]
PATCH  /sales-channel-tracking-order/{id}                  — Partially update information about a Sales Channel Tracking Order resource. [Experimental]
POST   /search/sales-channel-tracking-customer             — Search for the Sales Channel Tracking Customer resources. [Experimental]
POST   /search/sales-channel-tracking-order                — Search for the Sales Channel Tracking Order resources. [Experimental]
```

## Flow (7 ops)

```
GET    /flow                      — List with basic information of Flow resources.
POST   /flow                      — Create a new Flow resources.
GET    /flow/{id}                 — Detailed information about a Flow resource.
DELETE /flow/{id}                 — Delete a Flow resource.
PATCH  /flow/{id}                 — Partially update information about a Flow resource.
POST   /aggregate/flow            — Aggregate for the Flow resources.
POST   /search/flow               — Search for the Flow resources.
```

## Flow Sequence (7 ops)

```
GET    /flow-sequence             — List with basic information of Flow Sequence resources.
POST   /flow-sequence             — Create a new Flow Sequence resources.
GET    /flow-sequence/{id}        — Detailed information about a Flow Sequence resource.
DELETE /flow-sequence/{id}        — Delete a Flow Sequence resource.
PATCH  /flow-sequence/{id}        — Partially update information about a Flow Sequence resource.
POST   /aggregate/flow-sequence   — Aggregate for the Flow Sequence resources.
POST   /search/flow-sequence      — Search for the Flow Sequence resources.
```

## Flow Template (7 ops)

```
GET    /flow-template             — List with basic information of Flow Template resources.
POST   /flow-template             — Create a new Flow Template resources.
GET    /flow-template/{id}        — Detailed information about a Flow Template resource.
DELETE /flow-template/{id}        — Delete a Flow Template resource.
PATCH  /flow-template/{id}        — Partially update information about a Flow Template resource.
POST   /aggregate/flow-template   — Aggregate for the Flow Template resources.
POST   /search/flow-template      — Search for the Flow Template resources.
```

## Import Export File (7 ops)

```
GET    /import-export-file        — List with basic information of Import Export File resources.
POST   /import-export-file        — Create a new Import Export File resources.
GET    /import-export-file/{id}   — Detailed information about a Import Export File resource.
DELETE /import-export-file/{id}   — Delete a Import Export File resource.
PATCH  /import-export-file/{id}   — Partially update information about a Import Export File resource.
POST   /aggregate/import-export-file — Aggregate for the Import Export File resources.
POST   /search/import-export-file — Search for the Import Export File resources.
```

## Import Export Log (7 ops)

```
GET    /import-export-log         — List with basic information of Import Export Log resources.
POST   /import-export-log         — Create a new Import Export Log resources.
GET    /import-export-log/{id}    — Detailed information about a Import Export Log resource.
DELETE /import-export-log/{id}    — Delete a Import Export Log resource.
PATCH  /import-export-log/{id}    — Partially update information about a Import Export Log resource.
POST   /aggregate/import-export-log — Aggregate for the Import Export Log resources.
POST   /search/import-export-log  — Search for the Import Export Log resources.
```

## Import Export Profile (7 ops)

```
GET    /import-export-profile     — List with basic information of Import Export Profile resources.
POST   /import-export-profile     — Create a new Import Export Profile resources.
GET    /import-export-profile/{id} — Detailed information about a Import Export Profile resource.
DELETE /import-export-profile/{id} — Delete a Import Export Profile resource.
PATCH  /import-export-profile/{id} — Partially update information about a Import Export Profile resource.
POST   /aggregate/import-export-profile — Aggregate for the Import Export Profile resources.
POST   /search/import-export-profile    — Search for the Import Export Profile resources.
```

## Increment Storage (5 ops)

```
POST   /_action/decrement/{pool}         — Decrement a value in the specified pool
DELETE /_action/delete-increment/{pool}  — Delete increment keys from pool
POST   /_action/increment/{pool}         — Increment a value in the specified pool
GET    /_action/increment/{pool}         — List increment values from pool
POST   /_action/reset-increment/{pool}   — Reset increment values in pool
```

## Integration (7 ops)

```
GET    /integration               — List with basic information of Integration resources.
POST   /integration               — Create a new Integration resources.
GET    /integration/{id}          — Detailed information about a Integration resource.
DELETE /integration/{id}          — Delete a Integration resource.
PATCH  /integration/{id}          — Partially update information about a Integration resource.
POST   /aggregate/integration     — Aggregate for the Integration resources.
POST   /search/integration        — Search for the Integration resources.
```

## Landing Page (7 ops)

```
GET    /landing-page              — List with basic information of Landing Page resources.
POST   /landing-page              — Create a new Landing Page resources.
GET    /landing-page/{id}         — Detailed information about a Landing Page resource.
DELETE /landing-page/{id}         — Delete a Landing Page resource.
PATCH  /landing-page/{id}         — Partially update information about a Landing Page resource.
POST   /aggregate/landing-page    — Aggregate for the Landing Page resources.
POST   /search/landing-page       — Search for the Landing Page resources.
```

## Language (7 ops)

```
GET    /language                  — List with basic information of Language resources.
POST   /language                  — Create a new Language resources.
GET    /language/{id}             — Detailed information about a Language resource.
DELETE /language/{id}             — Delete a Language resource.
PATCH  /language/{id}             — Partially update information about a Language resource.
POST   /aggregate/language        — Aggregate for the Language resources.
POST   /search/language           — Search for the Language resources.
```

## Locale (7 ops)

```
GET    /locale                    — List with basic information of Locale resources.
POST   /locale                    — Create a new Locale resources.
GET    /locale/{id}               — Detailed information about a Locale resource.
DELETE /locale/{id}               — Delete a Locale resource.
PATCH  /locale/{id}               — Partially update information about a Locale resource.
POST   /aggregate/locale          — Aggregate for the Locale resources.
POST   /search/locale             — Search for the Locale resources.
```

## Log Entry (7 ops)

```
GET    /log-entry                 — List with basic information of Log Entry resources.
POST   /log-entry                 — Create a new Log Entry resources.
GET    /log-entry/{id}            — Detailed information about a Log Entry resource.
DELETE /log-entry/{id}            — Delete a Log Entry resource.
PATCH  /log-entry/{id}            — Partially update information about a Log Entry resource.
POST   /aggregate/log-entry       — Aggregate for the Log Entry resources.
POST   /search/log-entry          — Search for the Log Entry resources.
```

## MCP (8 ops)

```
POST   /_action/integration/{integrationId}/mcp-allowlist  — Save MCP allowlist for an integration
GET    /_action/mcp/capabilities                           — List all registered MCP capabilities
GET    /_action/mcp/tools                                  — List registered MCP tools
POST   /_action/user/{userId}/mcp-allowlist                — Save MCP allowlist for a user
POST   /_mcp                                               — MCP JSON-RPC endpoint
GET    /_mcp                                               — MCP SSE stream
DELETE /_mcp                                               — Close MCP session
OPTIONS /_mcp                                              — MCP CORS preflight
```

## Mail Header Footer (7 ops)

```
GET    /mail-header-footer        — List with basic information of Mail Header Footer resources.
POST   /mail-header-footer        — Create a new Mail Header Footer resources.
GET    /mail-header-footer/{id}   — Detailed information about a Mail Header Footer resource.
DELETE /mail-header-footer/{id}   — Delete a Mail Header Footer resource.
PATCH  /mail-header-footer/{id}   — Partially update information about a Mail Header Footer resource.
POST   /aggregate/mail-header-footer — Aggregate for the Mail Header Footer resources.
POST   /search/mail-header-footer — Search for the Mail Header Footer resources.
```

## Mail Operations (7 ops)

```
POST   /_action/mail-template/available-variables  — Fetch the available variables for a business event and an optional parent variable path.
POST   /_action/mail-template/build                — Build up a mail template
POST   /_action/mail-template/get-data-and-send    — Fetch the template data and send a mail
POST   /_action/mail-template/preview              — Preview a mail template
POST   /_action/mail-template/send                 — Send a mail
POST   /_action/mail-template/simulate             — Simulate a mail template
POST   /_action/mail-template/validate             — Validate a mail content
```

## Mail Template (7 ops)

```
GET    /mail-template             — List with basic information of Mail Template resources.
POST   /mail-template             — Create a new Mail Template resources.
GET    /mail-template/{id}        — Detailed information about a Mail Template resource.
DELETE /mail-template/{id}        — Delete a Mail Template resource.
PATCH  /mail-template/{id}        — Partially update information about a Mail Template resource.
POST   /aggregate/mail-template   — Aggregate for the Mail Template resources.
POST   /search/mail-template      — Search for the Mail Template resources.
```

## Mail Template Type (7 ops)

```
GET    /mail-template-type        — List with basic information of Mail Template Type resources.
POST   /mail-template-type        — Create a new Mail Template Type resources.
GET    /mail-template-type/{id}   — Detailed information about a Mail Template Type resource.
DELETE /mail-template-type/{id}   — Delete a Mail Template Type resource.
PATCH  /mail-template-type/{id}   — Partially update information about a Mail Template Type resource.
POST   /aggregate/mail-template-type — Aggregate for the Mail Template Type resources.
POST   /search/mail-template-type — Search for the Mail Template Type resources.
```

## Main Category (7 ops)

```
GET    /main-category             — List with basic information of Main Category resources.
POST   /main-category             — Create a new Main Category resources.
GET    /main-category/{id}        — Detailed information about a Main Category resource.
DELETE /main-category/{id}        — Delete a Main Category resource.
PATCH  /main-category/{id}        — Partially update information about a Main Category resource.
POST   /aggregate/main-category   — Aggregate for the Main Category resources.
POST   /search/main-category      — Search for the Main Category resources.
```

## Measurement Display Unit (7 ops)

```
GET    /measurement-display-unit        — List with basic information of Measurement Display Unit resources.
POST   /measurement-display-unit        — Create a new Measurement Display Unit resources.
GET    /measurement-display-unit/{id}   — Detailed information about a Measurement Display Unit resource.
DELETE /measurement-display-unit/{id}   — Delete a Measurement Display Unit resource.
PATCH  /measurement-display-unit/{id}   — Partially update information about a Measurement Display Unit resource.
POST   /aggregate/measurement-display-unit — Aggregate for the Measurement Display Unit resources.
POST   /search/measurement-display-unit    — Search for the Measurement Display Unit resources.
```

## Measurement System (7 ops)

```
GET    /measurement-system        — List with basic information of Measurement System resources.
POST   /measurement-system        — Create a new Measurement System resources.
GET    /measurement-system/{id}   — Detailed information about a Measurement System resource.
DELETE /measurement-system/{id}   — Delete a Measurement System resource.
PATCH  /measurement-system/{id}   — Partially update information about a Measurement System resource.
POST   /aggregate/measurement-system — Aggregate for the Measurement System resources.
POST   /search/measurement-system — Search for the Measurement System resources.
```

## Media (7 ops)

```
GET    /media                     — List with basic information of Media resources.
POST   /media                     — Create a new Media resources.
GET    /media/{id}                — Detailed information about a Media resource.
DELETE /media/{id}                — Delete a Media resource.
PATCH  /media/{id}                — Partially update information about a Media resource.
POST   /aggregate/media           — Aggregate for the Media resources.
POST   /search/media              — Search for the Media resources.
```

## Media Default Folder (7 ops)

```
GET    /media-default-folder      — List with basic information of Media Default Folder resources.
POST   /media-default-folder      — Create a new Media Default Folder resources.
GET    /media-default-folder/{id} — Detailed information about a Media Default Folder resource.
DELETE /media-default-folder/{id} — Delete a Media Default Folder resource.
PATCH  /media-default-folder/{id} — Partially update information about a Media Default Folder resource.
POST   /aggregate/media-default-folder — Aggregate for the Media Default Folder resources.
POST   /search/media-default-folder    — Search for the Media Default Folder resources.
```

## Media Folder (7 ops)

```
GET    /media-folder              — List with basic information of Media Folder resources.
POST   /media-folder              — Create a new Media Folder resources.
GET    /media-folder/{id}         — Detailed information about a Media Folder resource.
DELETE /media-folder/{id}         — Delete a Media Folder resource.
PATCH  /media-folder/{id}         — Partially update information about a Media Folder resource.
POST   /aggregate/media-folder    — Aggregate for the Media Folder resources.
POST   /search/media-folder       — Search for the Media Folder resources.
```

## Media Folder Configuration (7 ops)

```
GET    /media-folder-configuration        — List with basic information of Media Folder Configuration resources.
POST   /media-folder-configuration        — Create a new Media Folder Configuration resources.
GET    /media-folder-configuration/{id}   — Detailed information about a Media Folder Configuration resource.
DELETE /media-folder-configuration/{id}   — Delete a Media Folder Configuration resource.
PATCH  /media-folder-configuration/{id}   — Partially update information about a Media Folder Configuration resource.
POST   /aggregate/media-folder-configuration — Aggregate for the Media Folder Configuration resources.
POST   /search/media-folder-configuration    — Search for the Media Folder Configuration resources.
```

## Media Thumbnail (7 ops)

```
GET    /media-thumbnail           — List with basic information of Media Thumbnail resources.
POST   /media-thumbnail           — Create a new Media Thumbnail resources.
GET    /media-thumbnail/{id}      — Detailed information about a Media Thumbnail resource.
DELETE /media-thumbnail/{id}      — Delete a Media Thumbnail resource.
PATCH  /media-thumbnail/{id}      — Partially update information about a Media Thumbnail resource.
POST   /aggregate/media-thumbnail — Aggregate for the Media Thumbnail resources.
POST   /search/media-thumbnail    — Search for the Media Thumbnail resources.
```

## Media Thumbnail Size (7 ops)

```
GET    /media-thumbnail-size      — List with basic information of Media Thumbnail Size resources.
POST   /media-thumbnail-size      — Create a new Media Thumbnail Size resources.
GET    /media-thumbnail-size/{id} — Detailed information about a Media Thumbnail Size resource.
DELETE /media-thumbnail-size/{id} — Delete a Media Thumbnail Size resource.
PATCH  /media-thumbnail-size/{id} — Partially update information about a Media Thumbnail Size resource.
POST   /aggregate/media-thumbnail-size — Aggregate for the Media Thumbnail Size resources.
POST   /search/media-thumbnail-size    — Search for the Media Thumbnail Size resources.
```

## Newsletter Recipient (7 ops)

```
GET    /newsletter-recipient      — List with basic information of Newsletter Recipient resources.
POST   /newsletter-recipient      — Create a new Newsletter Recipient resources.
GET    /newsletter-recipient/{id} — Detailed information about a Newsletter Recipient resource.
DELETE /newsletter-recipient/{id} — Delete a Newsletter Recipient resource.
PATCH  /newsletter-recipient/{id} — Partially update information about a Newsletter Recipient resource.
POST   /aggregate/newsletter-recipient — Aggregate for the Newsletter Recipient resources.
POST   /search/newsletter-recipient    — Search for the Newsletter Recipient resources.
```

## Notification (7 ops)

```
GET    /notification              — List with basic information of Notification resources.
POST   /notification              — Create a new Notification resources.
GET    /notification/{id}         — Detailed information about a Notification resource.
DELETE /notification/{id}         — Delete a Notification resource.
PATCH  /notification/{id}         — Partially update information about a Notification resource.
POST   /aggregate/notification    — Aggregate for the Notification resources.
POST   /search/notification       — Search for the Notification resources.
```

## Number Range (7 ops)

```
GET    /number-range              — List with basic information of Number Range resources.
POST   /number-range              — Create a new Number Range resources.
GET    /number-range/{id}         — Detailed information about a Number Range resource.
DELETE /number-range/{id}         — Delete a Number Range resource.
PATCH  /number-range/{id}         — Partially update information about a Number Range resource.
POST   /aggregate/number-range    — Aggregate for the Number Range resources.
POST   /search/number-range       — Search for the Number Range resources.
```

## Number Range Management (2 ops)

```
GET    /_action/number-range/reserve/{type}/{saleschannel}   — Reserve or preview a number-range / document number.
GET    /_action/number-range/{numberRangeId}/preview-pattern — Preview a persisted number range
```

## Number Range Sales Channel (7 ops)

```
GET    /number-range-sales-channel        — List with basic information of Number Range Sales Channel resources.
POST   /number-range-sales-channel        — Create a new Number Range Sales Channel resources.
GET    /number-range-sales-channel/{id}   — Detailed information about a Number Range Sales Channel resource.
DELETE /number-range-sales-channel/{id}   — Delete a Number Range Sales Channel resource.
PATCH  /number-range-sales-channel/{id}   — Partially update information about a Number Range Sales Channel resource.
POST   /aggregate/number-range-sales-channel — Aggregate for the Number Range Sales Channel resources.
POST   /search/number-range-sales-channel    — Search for the Number Range Sales Channel resources.
```

## Number Range State (7 ops)

```
GET    /number-range-state        — List with basic information of Number Range State resources.
POST   /number-range-state        — Create a new Number Range State resources.
GET    /number-range-state/{id}   — Detailed information about a Number Range State resource.
DELETE /number-range-state/{id}   — Delete a Number Range State resource.
PATCH  /number-range-state/{id}   — Partially update information about a Number Range State resource.
POST   /aggregate/number-range-state — Aggregate for the Number Range State resources.
POST   /search/number-range-state — Search for the Number Range State resources.
```

## Number Range Type (7 ops)

```
GET    /number-range-type         — List with basic information of Number Range Type resources.
POST   /number-range-type         — Create a new Number Range Type resources.
GET    /number-range-type/{id}    — Detailed information about a Number Range Type resource.
DELETE /number-range-type/{id}    — Delete a Number Range Type resource.
PATCH  /number-range-type/{id}    — Partially update information about a Number Range Type resource.
POST   /aggregate/number-range-type — Aggregate for the Number Range Type resources.
POST   /search/number-range-type  — Search for the Number Range Type resources.
```

## Order (7 ops)

```
GET    /order                     — List with basic information of Order resources.
POST   /order                     — Create a new Order resources.
GET    /order/{id}                — Detailed information about a Order resource.
DELETE /order/{id}                — Delete a Order resource.
PATCH  /order/{id}                — Partially update information about a Order resource.
POST   /aggregate/order           — Aggregate for the Order resources.
POST   /search/order              — Search for the Order resources.
```

## Order Address (7 ops)

```
GET    /order-address             — List with basic information of Order Address resources.
POST   /order-address             — Create a new Order Address resources.
GET    /order-address/{id}        — Detailed information about a Order Address resource.
DELETE /order-address/{id}        — Delete a Order Address resource.
PATCH  /order-address/{id}        — Partially update information about a Order Address resource.
POST   /aggregate/order-address   — Aggregate for the Order Address resources.
POST   /search/order-address      — Search for the Order Address resources.
```

## Order Customer (7 ops)

```
GET    /order-customer            — List with basic information of Order Customer resources.
POST   /order-customer            — Create a new Order Customer resources.
GET    /order-customer/{id}       — Detailed information about a Order Customer resource.
DELETE /order-customer/{id}       — Delete a Order Customer resource.
PATCH  /order-customer/{id}       — Partially update information about a Order Customer resource.
POST   /aggregate/order-customer  — Aggregate for the Order Customer resources.
POST   /search/order-customer     — Search for the Order Customer resources.
```

## Order Delivery (7 ops)

```
GET    /order-delivery            — List with basic information of Order Delivery resources.
POST   /order-delivery            — Create a new Order Delivery resources.
GET    /order-delivery/{id}       — Detailed information about a Order Delivery resource.
DELETE /order-delivery/{id}       — Delete a Order Delivery resource.
PATCH  /order-delivery/{id}       — Partially update information about a Order Delivery resource.
POST   /aggregate/order-delivery  — Aggregate for the Order Delivery resources.
POST   /search/order-delivery     — Search for the Order Delivery resources.
```

## Order Delivery Position (7 ops)

```
GET    /order-delivery-position        — List with basic information of Order Delivery Position resources.
POST   /order-delivery-position        — Create a new Order Delivery Position resources.
GET    /order-delivery-position/{id}   — Detailed information about a Order Delivery Position resource.
DELETE /order-delivery-position/{id}   — Delete a Order Delivery Position resource.
PATCH  /order-delivery-position/{id}   — Partially update information about a Order Delivery Position resource.
POST   /aggregate/order-delivery-position — Aggregate for the Order Delivery Position resources.
POST   /search/order-delivery-position    — Search for the Order Delivery Position resources.
```

## Order Line Item (7 ops)

```
GET    /order-line-item           — List with basic information of Order Line Item resources.
POST   /order-line-item           — Create a new Order Line Item resources.
GET    /order-line-item/{id}      — Detailed information about a Order Line Item resource.
DELETE /order-line-item/{id}      — Delete a Order Line Item resource.
PATCH  /order-line-item/{id}      — Partially update information about a Order Line Item resource.
POST   /aggregate/order-line-item — Aggregate for the Order Line Item resources.
POST   /search/order-line-item    — Search for the Order Line Item resources.
```

## Order Line Item Download (7 ops)

```
GET    /order-line-item-download        — List with basic information of Order Line Item Download resources.
POST   /order-line-item-download        — Create a new Order Line Item Download resources.
GET    /order-line-item-download/{id}   — Detailed information about a Order Line Item Download resource.
DELETE /order-line-item-download/{id}   — Delete a Order Line Item Download resource.
PATCH  /order-line-item-download/{id}   — Partially update information about a Order Line Item Download resource.
POST   /aggregate/order-line-item-download — Aggregate for the Order Line Item Download resources.
POST   /search/order-line-item-download    — Search for the Order Line Item Download resources.
```

## Order Management (4 ops)

```
POST   /_action/order/{orderId}/state/{transition}                         — Transition an order to a new state
POST   /_action/order_delivery/{orderDeliveryId}/state/{transition}        — Transition an order delivery to a new state
POST   /_action/order_transaction/{orderTransactionId}/state/{transition}  — Transition an order transaction to a new state
POST   /_action/order_transaction_capture_refund/{refundId}                — Refund an order transaction capture
```

## Order Transaction (7 ops)

```
GET    /order-transaction         — List with basic information of Order Transaction resources.
POST   /order-transaction         — Create a new Order Transaction resources.
GET    /order-transaction/{id}    — Detailed information about a Order Transaction resource.
DELETE /order-transaction/{id}    — Delete a Order Transaction resource.
PATCH  /order-transaction/{id}    — Partially update information about a Order Transaction resource.
POST   /aggregate/order-transaction — Aggregate for the Order Transaction resources.
POST   /search/order-transaction  — Search for the Order Transaction resources.
```

## Order Transaction Capture (7 ops)

```
GET    /order-transaction-capture        — List with basic information of Order Transaction Capture resources.
POST   /order-transaction-capture        — Create a new Order Transaction Capture resources.
GET    /order-transaction-capture/{id}   — Detailed information about a Order Transaction Capture resource.
DELETE /order-transaction-capture/{id}   — Delete a Order Transaction Capture resource.
PATCH  /order-transaction-capture/{id}   — Partially update information about a Order Transaction Capture resource.
POST   /aggregate/order-transaction-capture — Aggregate for the Order Transaction Capture resources.
POST   /search/order-transaction-capture    — Search for the Order Transaction Capture resources.
```

## Order Transaction Capture Refund (7 ops)

```
GET    /order-transaction-capture-refund        — List with basic information of Order Transaction Capture Refund resources.
POST   /order-transaction-capture-refund        — Create a new Order Transaction Capture Refund resources.
GET    /order-transaction-capture-refund/{id}   — Detailed information about a Order Transaction Capture Refund resource.
DELETE /order-transaction-capture-refund/{id}   — Delete a Order Transaction Capture Refund resource.
PATCH  /order-transaction-capture-refund/{id}   — Partially update information about a Order Transaction Capture Refund resource.
POST   /aggregate/order-transaction-capture-refund — Aggregate for the Order Transaction Capture Refund resources.
POST   /search/order-transaction-capture-refund    — Search for the Order Transaction Capture Refund resources.
```

## Order Transaction Capture Refund Position (7 ops)

```
GET    /order-transaction-capture-refund-position        — List with basic information of Order Transaction Capture Refund Position resources.
POST   /order-transaction-capture-refund-position        — Create a new Order Transaction Capture Refund Position resources.
GET    /order-transaction-capture-refund-position/{id}   — Detailed information about a Order Transaction Capture Refund Position resource.
DELETE /order-transaction-capture-refund-position/{id}   — Delete a Order Transaction Capture Refund Position resource.
PATCH  /order-transaction-capture-refund-position/{id}   — Partially update information about a Order Transaction Capture Refund Position resource.
POST   /aggregate/order-transaction-capture-refund-position — Aggregate for the Order Transaction Capture Refund Position resources.
POST   /search/order-transaction-capture-refund-position    — Search for the Order Transaction Capture Refund Position resources.
```

## Order address (1 op)

```
POST   /_action/order/{orderId}/order-address  — Update order addresses
```

## Payment Method (7 ops)

```
GET    /payment-method            — List with basic information of Payment Method resources.
POST   /payment-method            — Create a new Payment Method resources.
GET    /payment-method/{id}       — Detailed information about a Payment Method resource.
DELETE /payment-method/{id}       — Delete a Payment Method resource.
PATCH  /payment-method/{id}       — Partially update information about a Payment Method resource.
POST   /aggregate/payment-method  — Aggregate for the Payment Method resources.
POST   /search/payment-method     — Search for the Payment Method resources.
```

## Plugin (7 ops)

```
GET    /plugin                    — List with basic information of Plugin resources.
POST   /plugin                    — Create a new Plugin resources.
GET    /plugin/{id}               — Detailed information about a Plugin resource.
DELETE /plugin/{id}               — Delete a Plugin resource.
PATCH  /plugin/{id}               — Partially update information about a Plugin resource.
POST   /aggregate/plugin          — Aggregate for the Plugin resources.
POST   /search/plugin             — Search for the Plugin resources.
```

## Product (7 ops)

```
GET    /product                   — List with basic information of Product resources.
POST   /product                   — Create a new Product resources.
GET    /product/{id}              — Detailed information about a Product resource.
DELETE /product/{id}              — Delete a Product resource.
PATCH  /product/{id}              — Partially update information about a Product resource.
POST   /aggregate/product         — Aggregate for the Product resources.
POST   /search/product            — Search for the Product resources.
```

## Product Configurator Setting (7 ops)

```
GET    /product-configurator-setting        — List with basic information of Product Configurator Setting resources.
POST   /product-configurator-setting        — Create a new Product Configurator Setting resources.
GET    /product-configurator-setting/{id}   — Detailed information about a Product Configurator Setting resource.
DELETE /product-configurator-setting/{id}   — Delete a Product Configurator Setting resource.
PATCH  /product-configurator-setting/{id}   — Partially update information about a Product Configurator Setting resource.
POST   /aggregate/product-configurator-setting — Aggregate for the Product Configurator Setting resources.
POST   /search/product-configurator-setting    — Search for the Product Configurator Setting resources.
```

## Product Cross Selling (7 ops)

```
GET    /product-cross-selling     — List with basic information of Product Cross Selling resources.
POST   /product-cross-selling     — Create a new Product Cross Selling resources.
GET    /product-cross-selling/{id} — Detailed information about a Product Cross Selling resource.
DELETE /product-cross-selling/{id} — Delete a Product Cross Selling resource.
PATCH  /product-cross-selling/{id} — Partially update information about a Product Cross Selling resource.
POST   /aggregate/product-cross-selling — Aggregate for the Product Cross Selling resources.
POST   /search/product-cross-selling    — Search for the Product Cross Selling resources.
```

## Product Cross Selling Assigned Products (7 ops)

```
GET    /product-cross-selling-assigned-products        — List with basic information of Product Cross Selling Assigned Products resources.
POST   /product-cross-selling-assigned-products        — Create a new Product Cross Selling Assigned Products resources.
GET    /product-cross-selling-assigned-products/{id}   — Detailed information about a Product Cross Selling Assigned Products resource.
DELETE /product-cross-selling-assigned-products/{id}   — Delete a Product Cross Selling Assigned Products resource.
PATCH  /product-cross-selling-assigned-products/{id}   — Partially update information about a Product Cross Selling Assigned Products resource.
POST   /aggregate/product-cross-selling-assigned-products — Aggregate for the Product Cross Selling Assigned Products resources.
POST   /search/product-cross-selling-assigned-products    — Search for the Product Cross Selling Assigned Products resources.
```

## Product Download (7 ops)

```
GET    /product-download          — List with basic information of Product Download resources.
POST   /product-download          — Create a new Product Download resources.
GET    /product-download/{id}     — Detailed information about a Product Download resource.
DELETE /product-download/{id}     — Delete a Product Download resource.
PATCH  /product-download/{id}     — Partially update information about a Product Download resource.
POST   /aggregate/product-download — Aggregate for the Product Download resources.
POST   /search/product-download   — Search for the Product Download resources.
```

## Product Export (7 ops)

```
GET    /product-export            — List with basic information of Product Export resources.
POST   /product-export            — Create a new Product Export resources.
GET    /product-export/{id}       — Detailed information about a Product Export resource.
DELETE /product-export/{id}       — Delete a Product Export resource.
PATCH  /product-export/{id}       — Partially update information about a Product Export resource.
POST   /aggregate/product-export  — Aggregate for the Product Export resources.
POST   /search/product-export     — Search for the Product Export resources.
```

## Product Feature Set (7 ops)

```
GET    /product-feature-set       — List with basic information of Product Feature Set resources.
POST   /product-feature-set       — Create a new Product Feature Set resources.
GET    /product-feature-set/{id}  — Detailed information about a Product Feature Set resource.
DELETE /product-feature-set/{id}  — Delete a Product Feature Set resource.
PATCH  /product-feature-set/{id}  — Partially update information about a Product Feature Set resource.
POST   /aggregate/product-feature-set — Aggregate for the Product Feature Set resources.
POST   /search/product-feature-set    — Search for the Product Feature Set resources.
```

## Product Keyword Dictionary (7 ops)

```
GET    /product-keyword-dictionary        — List with basic information of Product Keyword Dictionary resources.
POST   /product-keyword-dictionary        — Create a new Product Keyword Dictionary resources.
GET    /product-keyword-dictionary/{id}   — Detailed information about a Product Keyword Dictionary resource.
DELETE /product-keyword-dictionary/{id}   — Delete a Product Keyword Dictionary resource.
PATCH  /product-keyword-dictionary/{id}   — Partially update information about a Product Keyword Dictionary resource.
POST   /aggregate/product-keyword-dictionary — Aggregate for the Product Keyword Dictionary resources.
POST   /search/product-keyword-dictionary    — Search for the Product Keyword Dictionary resources.
```

## Product Manufacturer (7 ops)

```
GET    /product-manufacturer      — List with basic information of Product Manufacturer resources.
POST   /product-manufacturer      — Create a new Product Manufacturer resources.
GET    /product-manufacturer/{id} — Detailed information about a Product Manufacturer resource.
DELETE /product-manufacturer/{id} — Delete a Product Manufacturer resource.
PATCH  /product-manufacturer/{id} — Partially update information about a Product Manufacturer resource.
POST   /aggregate/product-manufacturer — Aggregate for the Product Manufacturer resources.
POST   /search/product-manufacturer    — Search for the Product Manufacturer resources.
```

## Product Media (7 ops)

```
GET    /product-media             — List with basic information of Product Media resources.
POST   /product-media             — Create a new Product Media resources.
GET    /product-media/{id}        — Detailed information about a Product Media resource.
DELETE /product-media/{id}        — Delete a Product Media resource.
PATCH  /product-media/{id}        — Partially update information about a Product Media resource.
POST   /aggregate/product-media   — Aggregate for the Product Media resources.
POST   /search/product-media      — Search for the Product Media resources.
```

## Product Price (7 ops)

```
GET    /product-price             — List with basic information of Product Price resources.
POST   /product-price             — Create a new Product Price resources.
GET    /product-price/{id}        — Detailed information about a Product Price resource.
DELETE /product-price/{id}        — Delete a Product Price resource.
PATCH  /product-price/{id}        — Partially update information about a Product Price resource.
POST   /aggregate/product-price   — Aggregate for the Product Price resources.
POST   /search/product-price      — Search for the Product Price resources.
```

## Product Review (7 ops)

```
GET    /product-review            — List with basic information of Product Review resources.
POST   /product-review            — Create a new Product Review resources.
GET    /product-review/{id}       — Detailed information about a Product Review resource.
DELETE /product-review/{id}       — Delete a Product Review resource.
PATCH  /product-review/{id}       — Partially update information about a Product Review resource.
POST   /aggregate/product-review  — Aggregate for the Product Review resources.
POST   /search/product-review     — Search for the Product Review resources.
```

## Product Search Config (7 ops)

```
GET    /product-search-config     — List with basic information of Product Search Config resources.
POST   /product-search-config     — Create a new Product Search Config resources.
GET    /product-search-config/{id} — Detailed information about a Product Search Config resource.
DELETE /product-search-config/{id} — Delete a Product Search Config resource.
PATCH  /product-search-config/{id} — Partially update information about a Product Search Config resource.
POST   /aggregate/product-search-config — Aggregate for the Product Search Config resources.
POST   /search/product-search-config    — Search for the Product Search Config resources.
```

## Product Search Config Field (7 ops)

```
GET    /product-search-config-field        — List with basic information of Product Search Config Field resources.
POST   /product-search-config-field        — Create a new Product Search Config Field resources.
GET    /product-search-config-field/{id}   — Detailed information about a Product Search Config Field resource.
DELETE /product-search-config-field/{id}   — Delete a Product Search Config Field resource.
PATCH  /product-search-config-field/{id}   — Partially update information about a Product Search Config Field resource.
POST   /aggregate/product-search-config-field — Aggregate for the Product Search Config Field resources.
POST   /search/product-search-config-field    — Search for the Product Search Config Field resources.
```

## Product Search Keyword (7 ops)

```
GET    /product-search-keyword    — List with basic information of Product Search Keyword resources.
POST   /product-search-keyword    — Create a new Product Search Keyword resources.
GET    /product-search-keyword/{id} — Detailed information about a Product Search Keyword resource.
DELETE /product-search-keyword/{id} — Delete a Product Search Keyword resource.
PATCH  /product-search-keyword/{id} — Partially update information about a Product Search Keyword resource.
POST   /aggregate/product-search-keyword — Aggregate for the Product Search Keyword resources.
POST   /search/product-search-keyword    — Search for the Product Search Keyword resources.
```

## Product Sorting (7 ops)

```
GET    /product-sorting           — List with basic information of Product Sorting resources.
POST   /product-sorting           — Create a new Product Sorting resources.
GET    /product-sorting/{id}      — Detailed information about a Product Sorting resource.
DELETE /product-sorting/{id}      — Delete a Product Sorting resource.
PATCH  /product-sorting/{id}      — Partially update information about a Product Sorting resource.
POST   /aggregate/product-sorting — Aggregate for the Product Sorting resources.
POST   /search/product-sorting    — Search for the Product Sorting resources.
```

## Product Stream (7 ops)

```
GET    /product-stream            — List with basic information of Product Stream resources.
POST   /product-stream            — Create a new Product Stream resources.
GET    /product-stream/{id}       — Detailed information about a Product Stream resource.
DELETE /product-stream/{id}       — Delete a Product Stream resource.
PATCH  /product-stream/{id}       — Partially update information about a Product Stream resource.
POST   /aggregate/product-stream  — Aggregate for the Product Stream resources.
POST   /search/product-stream     — Search for the Product Stream resources.
```

## Product Stream Filter (7 ops)

```
GET    /product-stream-filter     — List with basic information of Product Stream Filter resources.
POST   /product-stream-filter     — Create a new Product Stream Filter resources.
GET    /product-stream-filter/{id} — Detailed information about a Product Stream Filter resource.
DELETE /product-stream-filter/{id} — Delete a Product Stream Filter resource.
PATCH  /product-stream-filter/{id} — Partially update information about a Product Stream Filter resource.
POST   /aggregate/product-stream-filter — Aggregate for the Product Stream Filter resources.
POST   /search/product-stream-filter    — Search for the Product Stream Filter resources.
```

## Product Visibility (7 ops)

```
GET    /product-visibility        — List with basic information of Product Visibility resources.
POST   /product-visibility        — Create a new Product Visibility resources.
GET    /product-visibility/{id}   — Detailed information about a Product Visibility resource.
DELETE /product-visibility/{id}   — Delete a Product Visibility resource.
PATCH  /product-visibility/{id}   — Partially update information about a Product Visibility resource.
POST   /aggregate/product-visibility — Aggregate for the Product Visibility resources.
POST   /search/product-visibility — Search for the Product Visibility resources.
```

## Promotion (7 ops)

```
GET    /promotion                 — List with basic information of Promotion resources.
POST   /promotion                 — Create a new Promotion resources.
GET    /promotion/{id}            — Detailed information about a Promotion resource.
DELETE /promotion/{id}            — Delete a Promotion resource.
PATCH  /promotion/{id}            — Partially update information about a Promotion resource.
POST   /aggregate/promotion       — Aggregate for the Promotion resources.
POST   /search/promotion          — Search for the Promotion resources.
```

## Promotion Discount (7 ops)

```
GET    /promotion-discount        — List with basic information of Promotion Discount resources.
POST   /promotion-discount        — Create a new Promotion Discount resources.
GET    /promotion-discount/{id}   — Detailed information about a Promotion Discount resource.
DELETE /promotion-discount/{id}   — Delete a Promotion Discount resource.
PATCH  /promotion-discount/{id}   — Partially update information about a Promotion Discount resource.
POST   /aggregate/promotion-discount — Aggregate for the Promotion Discount resources.
POST   /search/promotion-discount — Search for the Promotion Discount resources.
```

## Promotion Discount Prices (7 ops)

```
GET    /promotion-discount-prices        — List with basic information of Promotion Discount Prices resources.
POST   /promotion-discount-prices        — Create a new Promotion Discount Prices resources.
GET    /promotion-discount-prices/{id}   — Detailed information about a Promotion Discount Prices resource.
DELETE /promotion-discount-prices/{id}   — Delete a Promotion Discount Prices resource.
PATCH  /promotion-discount-prices/{id}   — Partially update information about a Promotion Discount Prices resource.
POST   /aggregate/promotion-discount-prices — Aggregate for the Promotion Discount Prices resources.
POST   /search/promotion-discount-prices    — Search for the Promotion Discount Prices resources.
```

## Promotion Individual Code (7 ops)

```
GET    /promotion-individual-code        — List with basic information of Promotion Individual Code resources.
POST   /promotion-individual-code        — Create a new Promotion Individual Code resources.
GET    /promotion-individual-code/{id}   — Detailed information about a Promotion Individual Code resource.
DELETE /promotion-individual-code/{id}   — Delete a Promotion Individual Code resource.
PATCH  /promotion-individual-code/{id}   — Partially update information about a Promotion Individual Code resource.
POST   /aggregate/promotion-individual-code — Aggregate for the Promotion Individual Code resources.
POST   /search/promotion-individual-code    — Search for the Promotion Individual Code resources.
```

## Promotion Sales Channel (7 ops)

```
GET    /promotion-sales-channel        — List with basic information of Promotion Sales Channel resources.
POST   /promotion-sales-channel        — Create a new Promotion Sales Channel resources.
GET    /promotion-sales-channel/{id}   — Detailed information about a Promotion Sales Channel resource.
DELETE /promotion-sales-channel/{id}   — Delete a Promotion Sales Channel resource.
PATCH  /promotion-sales-channel/{id}   — Partially update information about a Promotion Sales Channel resource.
POST   /aggregate/promotion-sales-channel — Aggregate for the Promotion Sales Channel resources.
POST   /search/promotion-sales-channel    — Search for the Promotion Sales Channel resources.
```

## Promotion Setgroup (7 ops)

```
GET    /promotion-setgroup        — List with basic information of Promotion Setgroup resources.
POST   /promotion-setgroup        — Create a new Promotion Setgroup resources.
GET    /promotion-setgroup/{id}   — Detailed information about a Promotion Setgroup resource.
DELETE /promotion-setgroup/{id}   — Delete a Promotion Setgroup resource.
PATCH  /promotion-setgroup/{id}   — Partially update information about a Promotion Setgroup resource.
POST   /aggregate/promotion-setgroup — Aggregate for the Promotion Setgroup resources.
POST   /search/promotion-setgroup — Search for the Promotion Setgroup resources.
```

## Property Group (7 ops)

```
GET    /property-group            — List with basic information of Property Group resources.
POST   /property-group            — Create a new Property Group resources.
GET    /property-group/{id}       — Detailed information about a Property Group resource.
DELETE /property-group/{id}       — Delete a Property Group resource.
PATCH  /property-group/{id}       — Partially update information about a Property Group resource.
POST   /aggregate/property-group  — Aggregate for the Property Group resources.
POST   /search/property-group     — Search for the Property Group resources.
```

## Property Group Option (7 ops)

```
GET    /property-group-option     — List with basic information of Property Group Option resources.
POST   /property-group-option     — Create a new Property Group Option resources.
GET    /property-group-option/{id} — Detailed information about a Property Group Option resource.
DELETE /property-group-option/{id} — Delete a Property Group Option resource.
PATCH  /property-group-option/{id} — Partially update information about a Property Group Option resource.
POST   /aggregate/property-group-option — Aggregate for the Property Group Option resources.
POST   /search/property-group-option    — Search for the Property Group Option resources.
```

## Rule (7 ops)

```
GET    /rule                      — List with basic information of Rule resources.
POST   /rule                      — Create a new Rule resources.
GET    /rule/{id}                 — Detailed information about a Rule resource.
DELETE /rule/{id}                 — Delete a Rule resource.
PATCH  /rule/{id}                 — Partially update information about a Rule resource.
POST   /aggregate/rule            — Aggregate for the Rule resources.
POST   /search/rule               — Search for the Rule resources.
```

## Rule Condition (7 ops)

```
GET    /rule-condition            — List with basic information of Rule Condition resources.
POST   /rule-condition            — Create a new Rule Condition resources.
GET    /rule-condition/{id}       — Detailed information about a Rule Condition resource.
DELETE /rule-condition/{id}       — Delete a Rule Condition resource.
PATCH  /rule-condition/{id}       — Partially update information about a Rule Condition resource.
POST   /aggregate/rule-condition  — Aggregate for the Rule Condition resources.
POST   /search/rule-condition     — Search for the Rule Condition resources.
```

## Sales Channel (7 ops)

```
GET    /sales-channel             — List with basic information of Sales Channel resources.
POST   /sales-channel             — Create a new Sales Channel resources.
GET    /sales-channel/{id}        — Detailed information about a Sales Channel resource.
DELETE /sales-channel/{id}        — Delete a Sales Channel resource.
PATCH  /sales-channel/{id}        — Partially update information about a Sales Channel resource.
POST   /aggregate/sales-channel   — Aggregate for the Sales Channel resources.
POST   /search/sales-channel      — Search for the Sales Channel resources.
```

## Sales Channel Analytics (7 ops)

```
GET    /sales-channel-analytics        — List with basic information of Sales Channel Analytics resources.
POST   /sales-channel-analytics        — Create a new Sales Channel Analytics resources.
GET    /sales-channel-analytics/{id}   — Detailed information about a Sales Channel Analytics resource.
DELETE /sales-channel-analytics/{id}   — Delete a Sales Channel Analytics resource.
PATCH  /sales-channel-analytics/{id}   — Partially update information about a Sales Channel Analytics resource.
POST   /aggregate/sales-channel-analytics — Aggregate for the Sales Channel Analytics resources.
POST   /search/sales-channel-analytics    — Search for the Sales Channel Analytics resources.
```

## Sales Channel Domain (7 ops)

```
GET    /sales-channel-domain      — List with basic information of Sales Channel Domain resources.
POST   /sales-channel-domain      — Create a new Sales Channel Domain resources.
GET    /sales-channel-domain/{id} — Detailed information about a Sales Channel Domain resource.
DELETE /sales-channel-domain/{id} — Delete a Sales Channel Domain resource.
PATCH  /sales-channel-domain/{id} — Partially update information about a Sales Channel Domain resource.
POST   /aggregate/sales-channel-domain — Aggregate for the Sales Channel Domain resources.
POST   /search/sales-channel-domain    — Search for the Sales Channel Domain resources.
```

## Sales Channel Tracking Customer (7 ops) [Experimental]

```
GET    /sales-channel-tracking-customer        — List with basic information of Sales Channel Tracking Customer resources.
POST   /sales-channel-tracking-customer        — Create a new Sales Channel Tracking Customer resources.
GET    /sales-channel-tracking-customer/{id}   — Detailed information about a Sales Channel Tracking Customer resource.
DELETE /sales-channel-tracking-customer/{id}   — Delete a Sales Channel Tracking Customer resource.
PATCH  /sales-channel-tracking-customer/{id}   — Partially update information about a Sales Channel Tracking Customer resource.
POST   /aggregate/sales-channel-tracking-customer — Aggregate for the Sales Channel Tracking Customer resources.
POST   /search/sales-channel-tracking-customer    — Search for the Sales Channel Tracking Customer resources.
```

## Sales Channel Tracking Order (7 ops) [Experimental]

```
GET    /sales-channel-tracking-order        — List with basic information of Sales Channel Tracking Order resources.
POST   /sales-channel-tracking-order        — Create a new Sales Channel Tracking Order resources.
GET    /sales-channel-tracking-order/{id}   — Detailed information about a Sales Channel Tracking Order resource.
DELETE /sales-channel-tracking-order/{id}   — Delete a Sales Channel Tracking Order resource.
PATCH  /sales-channel-tracking-order/{id}   — Partially update information about a Sales Channel Tracking Order resource.
POST   /aggregate/sales-channel-tracking-order — Aggregate for the Sales Channel Tracking Order resources.
POST   /search/sales-channel-tracking-order    — Search for the Sales Channel Tracking Order resources.
```

## Sales Channel Type (7 ops)

```
GET    /sales-channel-type        — List with basic information of Sales Channel Type resources.
POST   /sales-channel-type        — Create a new Sales Channel Type resources.
GET    /sales-channel-type/{id}   — Detailed information about a Sales Channel Type resource.
DELETE /sales-channel-type/{id}   — Delete a Sales Channel Type resource.
PATCH  /sales-channel-type/{id}   — Partially update information about a Sales Channel Type resource.
POST   /aggregate/sales-channel-type — Aggregate for the Sales Channel Type resources.
POST   /search/sales-channel-type — Search for the Sales Channel Type resources.
```

## Salutation (7 ops)

```
GET    /salutation                — List with basic information of Salutation resources.
POST   /salutation                — Fetches salutations with a criteria obj.
GET    /salutation/{id}           — Detailed information about a Salutation resource.
DELETE /salutation/{id}           — Delete a Salutation resource.
PATCH  /salutation/{id}           — Partially update information about a Salutation resource.
POST   /aggregate/salutation      — Aggregate for the Salutation resources.
POST   /search/salutation         — Search for the Salutation resources.
```

## Scheduled Task (7 ops)

```
GET    /scheduled-task            — List with basic information of Scheduled Task resources.
POST   /scheduled-task            — Create a new Scheduled Task resources.
GET    /scheduled-task/{id}       — Detailed information about a Scheduled Task resource.
DELETE /scheduled-task/{id}       — Delete a Scheduled Task resource.
PATCH  /scheduled-task/{id}       — Partially update information about a Scheduled Task resource.
POST   /aggregate/scheduled-task  — Aggregate for the Scheduled Task resources.
POST   /search/scheduled-task     — Search for the Scheduled Task resources.
```

## Script (7 ops)

```
GET    /script                    — List with basic information of Script resources.
POST   /script                    — Create a new Script resources.
GET    /script/{id}               — Detailed information about a Script resource.
DELETE /script/{id}               — Delete a Script resource.
PATCH  /script/{id}               — Partially update information about a Script resource.
POST   /aggregate/script          — Aggregate for the Script resources.
POST   /search/script             — Search for the Script resources.
```

## Seo Url (7 ops)

```
GET    /seo-url                   — List with basic information of Seo Url resources.
POST   /seo-url                   — Create a new Seo Url resources.
GET    /seo-url/{id}              — Detailed information about a Seo Url resource.
DELETE /seo-url/{id}              — Delete a Seo Url resource.
PATCH  /seo-url/{id}              — Partially update information about a Seo Url resource.
POST   /aggregate/seo-url         — Aggregate for the Seo Url resources.
POST   /search/seo-url            — Search for the Seo Url resources.
```

## Seo Url Template (7 ops)

```
GET    /seo-url-template          — List with basic information of Seo Url Template resources.
POST   /seo-url-template          — Create a new Seo Url Template resources.
GET    /seo-url-template/{id}     — Detailed information about a Seo Url Template resource.
DELETE /seo-url-template/{id}     — Delete a Seo Url Template resource.
PATCH  /seo-url-template/{id}     — Partially update information about a Seo Url Template resource.
POST   /aggregate/seo-url-template — Aggregate for the Seo Url Template resources.
POST   /search/seo-url-template   — Search for the Seo Url Template resources.
```

## Shipping Method (7 ops)

```
GET    /shipping-method           — List with basic information of Shipping Method resources.
POST   /shipping-method           — Create a new Shipping Method resources.
GET    /shipping-method/{id}      — Detailed information about a Shipping Method resource.
DELETE /shipping-method/{id}      — Delete a Shipping Method resource.
PATCH  /shipping-method/{id}      — Partially update information about a Shipping Method resource.
POST   /aggregate/shipping-method — Aggregate for the Shipping Method resources.
POST   /search/shipping-method    — Search for the Shipping Method resources.
```

## Shipping Method Price (7 ops)

```
GET    /shipping-method-price     — List with basic information of Shipping Method Price resources.
POST   /shipping-method-price     — Create a new Shipping Method Price resources.
GET    /shipping-method-price/{id} — Detailed information about a Shipping Method Price resource.
DELETE /shipping-method-price/{id} — Delete a Shipping Method Price resource.
PATCH  /shipping-method-price/{id} — Partially update information about a Shipping Method Price resource.
POST   /aggregate/shipping-method-price — Aggregate for the Shipping Method Price resources.
POST   /search/shipping-method-price    — Search for the Shipping Method Price resources.
```

## Snippet (7 ops)

```
GET    /snippet                   — List with basic information of Snippet resources.
POST   /snippet                   — Create a new Snippet resources.
GET    /snippet/{id}              — Detailed information about a Snippet resource.
DELETE /snippet/{id}              — Delete a Snippet resource.
PATCH  /snippet/{id}              — Partially update information about a Snippet resource.
POST   /aggregate/snippet         — Aggregate for the Snippet resources.
POST   /search/snippet            — Search for the Snippet resources.
```

## Snippet Set (7 ops)

```
GET    /snippet-set               — List with basic information of Snippet Set resources.
POST   /snippet-set               — Create a new Snippet Set resources.
GET    /snippet-set/{id}          — Detailed information about a Snippet Set resource.
DELETE /snippet-set/{id}          — Delete a Snippet Set resource.
PATCH  /snippet-set/{id}          — Partially update information about a Snippet Set resource.
POST   /aggregate/snippet-set     — Aggregate for the Snippet Set resources.
POST   /search/snippet-set        — Search for the Snippet Set resources.
```

## SSO (3 ops) [Experimental]

```
GET    /oauth/sso/auth    — Experimental: Redirect to SSO login
GET    /oauth/sso/code    — Experimental: Callback for SSO login
GET    /oauth/sso/config  — Experimental: Loads SSO login configuration.
```

## State Machine (9 ops)

```
GET    /_action/state-machine/{entityName}/{entityId}/state                      — Get available transitions for an entity
POST   /_action/state-machine/{entityName}/{entityId}/state/{transition}         — Transition an entity to a new state
GET    /state-machine                                                             — List with basic information of State Machine resources.
POST   /state-machine                                                             — Create a new State Machine resources.
GET    /state-machine/{id}                                                        — Detailed information about a State Machine resource.
DELETE /state-machine/{id}                                                        — Delete a State Machine resource.
PATCH  /state-machine/{id}                                                        — Partially update information about a State Machine resource.
POST   /aggregate/state-machine                                                   — Aggregate for the State Machine resources.
POST   /search/state-machine                                                      — Search for the State Machine resources.
```

## State Machine History (7 ops)

```
GET    /state-machine-history     — List with basic information of State Machine History resources.
POST   /state-machine-history     — Create a new State Machine History resources.
GET    /state-machine-history/{id} — Detailed information about a State Machine History resource.
DELETE /state-machine-history/{id} — Delete a State Machine History resource.
PATCH  /state-machine-history/{id} — Partially update information about a State Machine History resource.
POST   /aggregate/state-machine-history — Aggregate for the State Machine History resources.
POST   /search/state-machine-history    — Search for the State Machine History resources.
```

## State Machine State (7 ops)

```
GET    /state-machine-state       — List with basic information of State Machine State resources.
POST   /state-machine-state       — Create a new State Machine State resources.
GET    /state-machine-state/{id}  — Detailed information about a State Machine State resource.
DELETE /state-machine-state/{id}  — Delete a State Machine State resource.
PATCH  /state-machine-state/{id}  — Partially update information about a State Machine State resource.
POST   /aggregate/state-machine-state — Aggregate for the State Machine State resources.
POST   /search/state-machine-state    — Search for the State Machine State resources.
```

## State Machine Transition (7 ops)

```
GET    /state-machine-transition        — List with basic information of State Machine Transition resources.
POST   /state-machine-transition        — Create a new State Machine Transition resources.
GET    /state-machine-transition/{id}   — Detailed information about a State Machine Transition resource.
DELETE /state-machine-transition/{id}   — Delete a State Machine Transition resource.
PATCH  /state-machine-transition/{id}   — Partially update information about a State Machine Transition resource.
POST   /aggregate/state-machine-transition — Aggregate for the State Machine Transition resources.
POST   /search/state-machine-transition    — Search for the State Machine Transition resources.
```

## System Config (12 ops)

```
GET    /_action/system-config             — Get configuration values
POST   /_action/system-config             — Save configuration values
POST   /_action/system-config/batch       — Batch save configuration values
GET    /_action/system-config/check       — Check configuration
GET    /_action/system-config/schema      — Get configuration schema
GET    /system-config                     — List with basic information of System Config resources.
POST   /system-config                     — Create a new System Config resources.
GET    /system-config/{id}                — Detailed information about a System Config resource.
DELETE /system-config/{id}                — Delete a System Config resource.
PATCH  /system-config/{id}                — Partially update information about a System Config resource.
POST   /aggregate/system-config           — Aggregate for the System Config resources.
POST   /search/system-config              — Search for the System Config resources.
```

## System Info & Health Check (10 ops)

```
GET    /_info/config               — Get public runtime config & feature metadata
GET    /_info/events.json          — Get Business events
GET    /_info/flow-actions.json    — Get actions for flow builder
GET    /_info/health-check         — Check that the Application is running
GET    /_info/message-stats.json   — Get statistics message queue
GET    /_info/openapi3.json        — Get OpenAPI Specification
GET    /_info/queue.json           — Get message queue statistics (deprecated)
GET    /_info/routes               — Get API routes
GET    /_info/system-health-check  — Perform a detailed system health check
GET    /_info/version              — Get the Shopware version
```

## System Operations (12 ops)

```
DELETE /_action/cache                        — Clear caches
DELETE /_action/cache-delayed                — Clear all invalidated caches
GET    /_action/cache_info                   — Get cache information
DELETE /_action/cleanup                      — Clear old cache folders
DELETE /_action/container_cache              — Clear container caches
POST   /_action/index                        — Run indexer
POST   /_action/index-products               — Send product indexing message
POST   /_action/indexing                     — Run indexer
POST   /_action/indexing/{indexer}           — Iterate an indexer
POST   /_action/message-queue/consume        — Consume messages from the message queue.
GET    /_action/scheduled-task/min-run-interval — Get the minimum schedules task interval
POST   /_action/scheduled-task/run           — Run scheduled tasks.
```

## Tag (7 ops)

```
GET    /tag                       — List with basic information of Tag resources.
POST   /tag                       — Create a new Tag resources.
GET    /tag/{id}                  — Detailed information about a Tag resource.
DELETE /tag/{id}                  — Delete a Tag resource.
PATCH  /tag/{id}                  — Partially update information about a Tag resource.
POST   /aggregate/tag             — Aggregate for the Tag resources.
POST   /search/tag                — Search for the Tag resources.
```

## Tax (7 ops)

```
GET    /tax                       — List with basic information of Tax resources.
POST   /tax                       — Create a new Tax resources.
GET    /tax/{id}                  — Detailed information about a Tax resource.
DELETE /tax/{id}                  — Delete a Tax resource.
PATCH  /tax/{id}                  — Partially update information about a Tax resource.
POST   /aggregate/tax             — Aggregate for the Tax resources.
POST   /search/tax                — Search for the Tax resources.
```

## Tax Provider (7 ops)

```
GET    /tax-provider              — List with basic information of Tax Provider resources.
POST   /tax-provider              — Create a new Tax Provider resources.
GET    /tax-provider/{id}         — Detailed information about a Tax Provider resource.
DELETE /tax-provider/{id}         — Delete a Tax Provider resource.
PATCH  /tax-provider/{id}         — Partially update information about a Tax Provider resource.
POST   /aggregate/tax-provider    — Aggregate for the Tax Provider resources.
POST   /search/tax-provider       — Search for the Tax Provider resources.
```

## Tax Rule (7 ops)

```
GET    /tax-rule                  — List with basic information of Tax Rule resources.
POST   /tax-rule                  — Create a new Tax Rule resources.
GET    /tax-rule/{id}             — Detailed information about a Tax Rule resource.
DELETE /tax-rule/{id}             — Delete a Tax Rule resource.
PATCH  /tax-rule/{id}             — Partially update information about a Tax Rule resource.
POST   /aggregate/tax-rule        — Aggregate for the Tax Rule resources.
POST   /search/tax-rule           — Search for the Tax Rule resources.
```

## Tax Rule Type (7 ops)

```
GET    /tax-rule-type             — List with basic information of Tax Rule Type resources.
POST   /tax-rule-type             — Create a new Tax Rule Type resources.
GET    /tax-rule-type/{id}        — Detailed information about a Tax Rule Type resource.
DELETE /tax-rule-type/{id}        — Delete a Tax Rule Type resource.
PATCH  /tax-rule-type/{id}        — Partially update information about a Tax Rule Type resource.
POST   /aggregate/tax-rule-type   — Aggregate for the Tax Rule Type resources.
POST   /search/tax-rule-type      — Search for the Tax Rule Type resources.
```

## Theme (12 ops)

```
PATCH  /_action/theme/{themeId}                                  — Update theme configuration
POST   /_action/theme/{themeId}/assign/{salesChannelId}          — Assign theme to sales channel
GET    /_action/theme/{themeId}/configuration                    — Get theme configuration
PATCH  /_action/theme/{themeId}/reset                            — Reset theme configuration
GET    /_action/theme/{themeId}/structured-fields                — Get theme configuration fields in structured format
GET    /theme                                                    — List with basic information of Theme resources.
POST   /theme                                                    — Create a new Theme resources.
GET    /theme/{id}                                               — Detailed information about a Theme resource.
DELETE /theme/{id}                                               — Delete a Theme resource.
PATCH  /theme/{id}                                               — Partially update information about a Theme resource.
POST   /aggregate/theme                                          — Aggregate for the Theme resources.
POST   /search/theme                                             — Search for the Theme resources.
```

## Unit (7 ops)

```
GET    /unit                      — List with basic information of Unit resources.
POST   /unit                      — Create a new Unit resources.
GET    /unit/{id}                 — Detailed information about a Unit resource.
DELETE /unit/{id}                 — Delete a Unit resource.
PATCH  /unit/{id}                 — Partially update information about a Unit resource.
POST   /aggregate/unit            — Aggregate for the Unit resources.
POST   /search/unit               — Search for the Unit resources.
```

## User (7 ops)

```
GET    /user                      — List with basic information of User resources.
POST   /user                      — Create a new User resources.
GET    /user/{id}                 — Detailed information about a User resource.
DELETE /user/{id}                 — Delete a User resource.
PATCH  /user/{id}                 — Partially update information about a User resource.
POST   /aggregate/user            — Aggregate for the User resources.
POST   /search/user               — Search for the User resources.
```

## User Access Key (7 ops)

```
GET    /user-access-key           — List with basic information of User Access Key resources.
POST   /user-access-key           — Create a new User Access Key resources.
GET    /user-access-key/{id}      — Detailed information about a User Access Key resource.
DELETE /user-access-key/{id}      — Delete a User Access Key resource.
PATCH  /user-access-key/{id}      — Partially update information about a User Access Key resource.
POST   /aggregate/user-access-key — Aggregate for the User Access Key resources.
POST   /search/user-access-key    — Search for the User Access Key resources.
```

## User Config (7 ops)

```
GET    /user-config               — List with basic information of User Config resources.
POST   /user-config               — Create a new User Config resources.
GET    /user-config/{id}          — Detailed information about a User Config resource.
DELETE /user-config/{id}          — Delete a User Config resource.
PATCH  /user-config/{id}          — Partially update information about a User Config resource.
POST   /aggregate/user-config     — Aggregate for the User Config resources.
POST   /search/user-config        — Search for the User Config resources.
```

## User Recovery (7 ops)

```
GET    /user-recovery             — List with basic information of User Recovery resources.
POST   /user-recovery             — Create a new User Recovery resources.
GET    /user-recovery/{id}        — Detailed information about a User Recovery resource.
DELETE /user-recovery/{id}        — Delete a User Recovery resource.
PATCH  /user-recovery/{id}        — Partially update information about a User Recovery resource.
POST   /aggregate/user-recovery   — Aggregate for the User Recovery resources.
POST   /search/user-recovery      — Search for the User Recovery resources.
```

## Webhook (7 ops)

```
GET    /webhook                   — List with basic information of Webhook resources.
POST   /webhook                   — Create a new Webhook resources.
GET    /webhook/{id}              — Detailed information about a Webhook resource.
DELETE /webhook/{id}              — Delete a Webhook resource.
PATCH  /webhook/{id}              — Partially update information about a Webhook resource.
POST   /aggregate/webhook         — Aggregate for the Webhook resources.
POST   /search/webhook            — Search for the Webhook resources.
```

## Webhook Event Log (7 ops)

```
GET    /webhook-event-log         — List with basic information of Webhook Event Log resources.
POST   /webhook-event-log         — Create a new Webhook Event Log resources.
GET    /webhook-event-log/{id}    — Detailed information about a Webhook Event Log resource.
DELETE /webhook-event-log/{id}    — Delete a Webhook Event Log resource.
PATCH  /webhook-event-log/{id}    — Partially update information about a Webhook Event Log resource.
POST   /aggregate/webhook-event-log — Aggregate for the Webhook Event Log resources.
POST   /search/webhook-event-log  — Search for the Webhook Event Log resources.
```

---

## Hinweis: Operationen-Überlappung (Tags mit mehrfach gelisteten Ops)

Die Tag-Gruppierung der OpenAPI-Spec enthält einige Duplikate (Operationen können mehrere Tags haben). Die oben genannten 1093 Operationen beziehen sich auf die Gesamt-Anzahl aller `(method, path)`-Kombinationen in `adminapi.json`. Einige `_action`-Endpunkte erscheinen in mehreren Tags (z.B. Consent Management sowohl im "Consent Management"- als auch im "Experimental"-Tag).
