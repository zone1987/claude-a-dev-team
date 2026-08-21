# Shopware 6 – Einstellungen (Settings) (overview)

The **Einstellungen** area in Shopware 6 holds every central configuration option for shop, system and extensions.

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
