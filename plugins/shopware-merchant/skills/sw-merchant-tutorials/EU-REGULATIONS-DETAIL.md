# Shopware 6 — Tutorials: EU regulations (complete reference)

---

## 1. GDPR (General Data Protection Regulation)

**Source:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/dsgvo  
**In force since:** 25 May 2018

### Which personal data is processed?

| Category | Data |
|-----------|-------|
| Customer data | Address, date of birth, company name |
| Bestellungen (Orders) | Delivery address, order total, cart, IP address, referrer |
| Newsletter | Registration data |
| Forms | Salutation, name, e-mail, phone |
| Bewertungen (Reviews) | Product reviews linked to a customer account |
| Admin | Staff data including e-mail |
| API | Data retrievable through authorised interfaces |

### IP addresses are stored in

- `order_customer` (per order)
- `customer` (last order)
- `log_entry` (backend activities)
- `version_commit_data` (current usage data)

### Encryption

The HTTPS protocol with an SSL certificate is required for secure data transmission.

### Cookies (browser storage)

- Session cookies (cart, login status)
- CSRF cookies (protection function)
- Timezone cookies (time zone calibration)

Shopware only ever stores IDs in the customer's browser.

### Embedding the privacy policy

- Use the pre-configured "Datenschutz" (Privacy) Erlebniswelt (Shopping Experience)
- Adjust under Einstellungen (Settings) > Shop > Stammdaten (Master data)
- Link it in the checkout and in forms

### Cookie Consent Manager

- Shopware provides an integrated Cookie Consent Manager
- Plugins can register their own cookies
- Link for later changes: `/cookie/offcanvas`
- Settings: Einstellungen > Allgemein (General) > Stammdaten (accept-all button)
- Adjust texts: Einstellungen > Regional > Textbausteine (Snippets) (search for "Cookie")

### Exporting data in a structured form

Import/Export function for CSV/XML export of personal data.

### Deleting data

Can be carried out via the admin customer module (links are removed automatically).

**Carts:** deleted after 120 days by default, configurable via `shopware.yaml`.

### FAQ

- No separate GDPR plugin is planned — updates are provided where necessary
- Registration references the privacy policy via the snippet `general.privacyNotice`
- Forms automatically contain a data protection checkbox
- Third-party extensions (PayPal, ERP, newsletter) may initiate their own data flows

---

## 2. One-Stop-Shop procedure (EU-OSS)

**Source:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/one-stop-shop  
**From version:** 6.4.1.0  
**In force since:** 1 July 2021

### Definition

EU-OSS is an electronic portal through which merchants and companies can fulfil their VAT obligations within the EU centrally, instead of registering separately in each country.

### Threshold

**EUR 10,000 EU-wide (uniform).** Merchants exceeding this amount should register with the responsible OSS portal.

### Shopware configuration

- Continue to configure tax rates via the Steuern (Taxes) module
- The delivery country must be displayed next to the price
- Customers must be able to select the delivery country transparently (with the corresponding prices)

---

*Source: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/eu-regelungen — as of: 2026-06*
