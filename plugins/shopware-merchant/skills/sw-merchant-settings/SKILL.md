---
name: sw-merchant-settings
description: >
  Shopware Einstellungen Überblick, Shop-Einstellungen, System-Einstellungen, Grundkonfiguration,
  Shopware Administration Einstellungen, Konfiguration Shop Allgemein System, Einstellungen-Kapitel,
  Shopware 6 Settings Overview
---

# Shopware 6 – Einstellungen (Überblick)

Der Bereich **Einstellungen** in Shopware 6 enthält alle zentralen Konfigurationsmöglichkeiten für Shop, System und Erweiterungen.

## Unterbereiche

| Bereich | Pfad im Admin | Skill |
|---|---|---|
| Shop-Grundlagen, Stammdaten, Adressen | Einstellungen > Shop | `sw-merchant-settings-shop-basics` |
| Währungen & Sprachen | Einstellungen > Shop | `sw-merchant-settings-currencies-languages` |
| Steuern | Einstellungen > Regional > Steuern | `sw-merchant-settings-tax` |
| Textbausteine (Snippets) | Einstellungen > Shop > Textbausteine | `sw-merchant-settings-snippets` |
| SEO-Einstellungen & Sitemap | Einstellungen > Shop > SEO | `sw-merchant-settings-seo` |
| Zahlungsarten | Einstellungen > Handel > Zahlungsarten | `sw-merchant-settings-payment-methods` |
| Versandarten | Einstellungen > Handel > Versand | `sw-merchant-settings-shipping-methods` |
| Lieferzeiten | Einstellungen > Handel > Lieferzeiten | `sw-merchant-settings-delivery-times` |
| Rule Builder / Regeln | Einstellungen > Automatisierung | `sw-merchant-settings-rule-builder` |
| Flow Builder / Abläufe | Einstellungen > Automatisierung | `sw-merchant-settings-flow-builder` |
| E-Mail-Templates & Mailer | Einstellungen > Inhalte | `sw-merchant-settings-mail-templates` |
| Import / Export | Einstellungen > Automatisierung | `sw-merchant-settings-import-export` |
| Integrationen & API-Zugänge | Einstellungen > System | `sw-merchant-settings-integrations-api` |
| Benutzer & Rechte | Einstellungen > System | `sw-merchant-settings-users-permissions` |
| Caches & Indizes | Einstellungen > System | `sw-merchant-settings-caches-indexes` |
| System-Info, Logs, Konto | Einstellungen > System | `sw-merchant-settings-system-info` |

## Schnelleinstieg

- **E-Mail-Versand konfigurieren**: Einstellungen > System > Mailer → `sw-merchant-settings-mail-templates`
- **Neue Zahlungsart anlegen**: Einstellungen > Handel > Zahlungsarten → `sw-merchant-settings-payment-methods`
- **Versandkosten einrichten**: Einstellungen > Handel > Versand → `sw-merchant-settings-shipping-methods`
- **Automatisierungsregel erstellen**: Einstellungen > Automatisierung > Rule Builder → `sw-merchant-settings-rule-builder`
- **Flow-Automatisierung einrichten**: Einstellungen > Automatisierung > Flow Builder → `sw-merchant-settings-flow-builder`
- **Benutzer anlegen / Rollen**: Einstellungen > System > Benutzer & Rechte → `sw-merchant-settings-users-permissions`
- **API-Integration einrichten**: Einstellungen > System > Integrationen → `sw-merchant-settings-integrations-api`
- **Cache leeren**: Einstellungen > System > Caches & Indizes → `sw-merchant-settings-caches-indexes`
- **Produkte importieren**: Einstellungen > Automatisierung > Import/Export → `sw-merchant-settings-import-export`
- **Steuersätze verwalten**: Einstellungen > Regional > Steuern → `sw-merchant-settings-tax`

## Hinweis zu Cloud vs. Self-Hosted

Einige System-Einstellungen (Mailer, Caches & Indizes, Shopware-Account, Updates) sind **ausschließlich für Self-Hosted-Installationen** relevant und in der Shopware Cloud nicht verfügbar.
