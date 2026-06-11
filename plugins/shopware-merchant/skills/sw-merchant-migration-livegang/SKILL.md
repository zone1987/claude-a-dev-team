---
name: sw-merchant-migration-livegang
description: >
  Livegang nach Shopware-Migration: Domain umstellen, DNS-Routing auf /public/ konfigurieren,
  Shopware Account Lizenzierungshost umtragen, Verkaufskanäle auf neue Domain umstellen,
  Migrationsdaten aufräumen, Magento-spezifische Hinweise (Passwort-Algorithmus). Trigger:
  "Livegang Migration Shopware", "Domain nach Migration umstellen", "Shopware 6 live schalten
  nach Migration", "Verkaufskanal Domain umtragen", "Migration abschließen Shopware",
  "Migrationsdaten aufräumen", "Apache Konfiguration Shopware Migration", "Shopware Account
  nach Migration umstellen". Shopware 6.7.
---

# Shopware Migration — Livegang

Destilliert aus `docs.shopware.com/de/migration-de/Livegang`. Gilt für SW5→SW6, SW6→SW6, Magento→SW6.

## Kurzübersicht

1. Änderungen im **Zielshop** (SW6): Lizenz + Domain in Verkaufskanälen
2. Änderungen im **Quellshop**: Shop verschieben / Domain anpassen
3. Änderungen beim **Hoster**: DNS-Routing auf `/public/` konfigurieren
4. **Migrationsdaten aufräumen** (Datenbankbereinigung)

Tiefes Schritt-für-Schritt-Wissen: `references/deep/livegang.md`

---

*Quelle: https://docs.shopware.com/de/migration-de/Livegang*
