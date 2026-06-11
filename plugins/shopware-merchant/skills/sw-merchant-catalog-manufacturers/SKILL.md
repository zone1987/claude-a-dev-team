---
name: sw-merchant-catalog-manufacturers
description: >
  Shopware Hersteller verwalten, Hersteller anlegen, Hersteller bearbeiten, Herstellerseite,
  Hersteller Logo, Hersteller Website, Produkthersteller, Herstellerübersicht Shopware,
  Herstellerseite anlegen, SEO Hersteller, Herstellerinformationen Produkt
---

# Shopware 6 – Hersteller

Hersteller werden unter **Kataloge > Hersteller** verwaltet und können Produkten zugewiesen werden.
Sie erscheinen auf der Produktdetailseite (oben rechts).

## Hersteller anlegen

1. Kataloge > Hersteller > **„Hersteller anlegen"**
2. **Pflichtfeld**: Name
3. Optional: Website-Link, Logo, Beschreibung (unterstützt Twig-Variablen)
4. Speichern

## Hersteller-Aktionen

| Aktion | Beschreibung |
|---|---|
| Bearbeiten | Öffnet Bearbeitungsmaske |
| Duplizieren | Kopie mit allen Daten erstellen |
| Löschen | Nur möglich wenn keinem Produkt zugewiesen |

## Herstellerseite erstellen (Workaround)

Shopware 6 hat keine native Herstellerseite. Vorgehen:
1. Erlebniswelt-Landingpage in „Inhalte > Erlebniswelten" erstellen
2. Unter Kataloge > Kategorien eine Landingpage anlegen (SEO-URL setzen)
3. Layout der Erlebniswelt zuweisen
4. Diese SEO-URL beim Hersteller unter „Hersteller-URL" eintragen (mit führendem `/`)

Siehe `references/deep/manufacturers.md` für vollständige Anleitung.

## Quelle
https://docs.shopware.com/de/shopware-6-de/produkte/hersteller
