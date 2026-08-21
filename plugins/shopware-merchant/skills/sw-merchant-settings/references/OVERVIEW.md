# Shopware 6 – Einstellungen (Settings) (overview)

The **Einstellungen** area in Shopware 6 holds every central configuration option for shop, system and extensions.

## Contents

- [Sub-areas](#sub-areas)
- [Quick start](#quick-start)
- [Note on Cloud vs. self-hosted](#note-on-cloud-vs-self-hosted)
- [Shopware 6 – Einstellungen (Settings) (complete overview reference)](#shopware-6-einstellungen-settings-complete-overview-reference)

## Sub-areas

| Area | Path in the admin | Skill |
|---|---|---|
| Shop basics, Stammdaten (Master data), Adressen (Addresses) | Einstellungen > Shop | `sw-merchant-settings-shop-basics` |
| Währungen (Currencies) & Sprachen (Languages) | Einstellungen > Shop | `sw-merchant-settings-currencies-languages` |
| Steuern (Taxes) | Einstellungen > Regional > Steuern | `sw-merchant-settings-tax` |
| Textbausteine (Snippets) | Einstellungen > Shop > Textbausteine | `sw-merchant-settings-snippets` |
| SEO-Einstellungen (SEO settings) & Sitemap | Einstellungen > Shop > SEO | `sw-merchant-settings-seo` |
| Zahlungsarten (Payment methods) | Einstellungen > Handel (Commerce) > Zahlungsarten | `sw-merchant-settings-payment-methods` |
| Versandarten (Shipping methods) | Einstellungen > Handel > Versand (Shipping) | `sw-merchant-settings-shipping-methods` |
| Lieferzeiten (Delivery times) | Einstellungen > Handel > Lieferzeiten | `sw-merchant-settings-delivery-times` |
| Rule Builder / Regeln (Rules) | Einstellungen > Automatisierung (Automation) | `sw-merchant-settings-rule-builder` |
| Flow Builder / Abläufe (Flows) | Einstellungen > Automatisierung | `sw-merchant-settings-flow-builder` |
| Email templates & mailer | Einstellungen > Inhalte (Content) | `sw-merchant-settings-mail-templates` |
| Import / Export | Einstellungen > Automatisierung | `sw-merchant-settings-import-export` |
| Integrationen (Integrations) & API access | Einstellungen > System | `sw-merchant-settings-integrations-api` |
| Benutzer & Rechte (Users & permissions) | Einstellungen > System | `sw-merchant-settings-users-permissions` |
| Caches & Indizes (Caches & indexes) | Einstellungen > System | `sw-merchant-settings-caches-indexes` |
| System info, logs, account | Einstellungen > System | `sw-merchant-settings-system-info` |

## Quick start

- **Configure email sending**: Einstellungen > System > Mailer → `sw-merchant-settings-mail-templates`
- **Create a new payment method**: Einstellungen > Handel > Zahlungsarten → `sw-merchant-settings-payment-methods`
- **Set up shipping costs**: Einstellungen > Handel > Versand → `sw-merchant-settings-shipping-methods`
- **Create an automation rule**: Einstellungen > Automatisierung > Rule Builder → `sw-merchant-settings-rule-builder`
- **Set up flow automation**: Einstellungen > Automatisierung > Flow Builder → `sw-merchant-settings-flow-builder`
- **Create users / roles**: Einstellungen > System > Benutzer & Rechte → `sw-merchant-settings-users-permissions`
- **Set up an API integration**: Einstellungen > System > Integrationen → `sw-merchant-settings-integrations-api`
- **Clear the cache**: Einstellungen > System > Caches & Indizes → `sw-merchant-settings-caches-indexes`
- **Import products**: Einstellungen > Automatisierung > Import/Export → `sw-merchant-settings-import-export`
- **Manage tax rates**: Einstellungen > Regional > Steuern → `sw-merchant-settings-tax`

## Note on Cloud vs. self-hosted

Some system settings (Mailer, Caches & Indizes, Shopware Account, updates) are relevant **exclusively for self-hosted installations** and are not available in Shopware Cloud.

## Shopware 6 – Einstellungen (Settings) (complete overview reference)

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen

---

### Chapter structure

The "Einstellungen" chapter is divided into three main areas:

1. **Shop** — general shop configuration
2. **System** — technical system settings (predominantly self-hosted)
3. **Erweiterungen** (Extensions) — plugin management (see the extensions chapter)

---

### Area: Shop

| Topic | Path in the admin | Skill |
|---|---|---|
| Stammdaten (Master data) | Einstellungen > Shop > Stammdaten | `sw-merchant-settings-shop-basics` |
| Adressen (Addresses) | Einstellungen > Shop > Adressen | `sw-merchant-settings-shop-basics` |
| Anreden (Salutations) | Einstellungen > Customer > Anreden | `sw-merchant-settings-shop-basics` |
| Kundengruppen (Customer groups) | Einstellungen > Kundengruppen | `sw-merchant-settings-shop-basics` |
| Nummernkreise (Number ranges) | Einstellungen > Allgemein (General) > Nummernkreise | `sw-merchant-settings-shop-basics` |
| Anmeldung & Registrierung (Login & registration) | Einstellungen > Kunde (Customer) | `sw-merchant-settings-shop-basics` |
| Warenkorb (Cart) | Einstellungen > Allgemein > Warenkorb | `sw-merchant-settings-shop-basics` |
| Produkte (Products) (listings) | Einstellungen > Allgemein > Produkte | `sw-merchant-settings-shop-basics` |
| Newsletter configuration | Einstellungen > Shop > Newsletter | `sw-merchant-settings-shop-basics` |
| Tags | Einstellungen > Allgemein > Tags | `sw-merchant-settings-shop-basics` |
| Maßeinheiten (Units of measure) | Einstellungen > Allgemein > Produkteinheiten (Product units) | `sw-merchant-settings-shop-basics` |
| Maßeinheitensystem (Unit system) | Einstellungen > Allgemein > Maßeinheitensystem | `sw-merchant-settings-shop-basics` |
| Dokumente (Documents) | Einstellungen > Handel (Commerce) > Dokumente | `sw-merchant-settings-shop-basics` |
| Wesentliche Merkmale (Essential features) | Einstellungen > Shop > Wesentliche Merkmale | `sw-merchant-settings-shop-basics` |
| Zusatzfelder (Custom fields) | Einstellungen > System > Zusatzfelder | `sw-merchant-settings-shop-basics` |
| Währungen (Currencies) | Einstellungen > Shop > Währungen | `sw-merchant-settings-currencies-languages` |
| Sprachen (Languages) | Einstellungen > Allgemein > Sprachen | `sw-merchant-settings-currencies-languages` |
| Länder (Countries) | Einstellungen > Regional > Länder | `sw-merchant-settings-currencies-languages` |
| Steuern (Taxes) | Einstellungen > Regional > Steuern | `sw-merchant-settings-tax` |
| Textbausteine (Snippets) | Einstellungen > Shop > Textbausteine | `sw-merchant-settings-snippets` |
| SEO-Einstellungen (SEO settings) | Einstellungen > Shop > SEO | `sw-merchant-settings-seo` |
| Sitemap | Einstellungen > Shop > Sitemap | `sw-merchant-settings-seo` |
| Suche (Search) (incl. Advanced Search) | Einstellungen > Shop > Suche | `sw-merchant-settings-system-info` |
| Zahlungsarten (Payment methods) | Einstellungen > Handel > Zahlungsarten | `sw-merchant-settings-payment-methods` |
| Versandarten (Shipping methods) | Einstellungen > Handel > Versand (Shipping) | `sw-merchant-settings-shipping-methods` |
| Lieferzeiten (Delivery times) | Einstellungen > Handel > Lieferzeiten | `sw-merchant-settings-delivery-times` |
| Lagerhäuser (Warehouses) | Einstellungen > Handel > Lagerhäuser | `sw-merchant-settings-shipping-methods` |
| Abonnements (Subscriptions) | Einstellungen > Handel > Abonnements | `sw-merchant-settings-shop-basics` |
| Rule Builder | Einstellungen > Automatisierung (Automation) > Rule Builder | `sw-merchant-settings-rule-builder` |
| Flow Builder | Einstellungen > Automatisierung > Flow Builder | `sw-merchant-settings-flow-builder` |
| Import/Export | Einstellungen > Automatisierung > Import/Export | `sw-merchant-settings-import-export` |
| Business-Events (legacy) | Einstellungen > Shop > Business-Events | `sw-merchant-settings-system-info` |
| Email templates | Einstellungen > Inhalte (Content) > E-Mail-Templates | `sw-merchant-settings-mail-templates` |

---

### Area: System

| Topic | Path in the admin | Skill |
|---|---|---|
| Benutzer & Rechte (Users & permissions) | Einstellungen > System > Benutzer & Rechte | `sw-merchant-settings-users-permissions` |
| Integrationen (Integrations) | Einstellungen > System > Integrationen | `sw-merchant-settings-integrations-api` |
| Mailer | Einstellungen > System > Mailer | `sw-merchant-settings-mail-templates` |
| Caches & Indizes (Caches & indexes) | Einstellungen > System > Caches & Indizes | `sw-merchant-settings-caches-indexes` |
| Ereignis-Logs (Event logs) | Einstellungen > System > Ereignis-Logs | `sw-merchant-settings-system-info` |
| Shopware Account | Einstellungen > System > Shopware Account | `sw-merchant-settings-system-info` |
| Datenschutzeinstellungen (Privacy settings) | Einstellungen > System > Datenschutz (Privacy) | `sw-merchant-settings-system-info` |
| Shopware Updates | Einstellungen > System > Shopware Updates | `sw-merchant-settings-system-info` |
| Zusatzfelder (Custom fields) | Einstellungen > System > Zusatzfelder | `sw-merchant-settings-shop-basics` |

---

### Note: Cloud vs. self-hosted

The following settings are relevant **for self-hosted only**:
- Mailer (SMTP configuration)
- Caches & Indizes
- Shopware Account (licence host)
- Shopware Updates
- Ereignis-Logs (system side)
