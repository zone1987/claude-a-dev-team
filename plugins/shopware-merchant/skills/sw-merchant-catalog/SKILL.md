---
name: sw-merchant-catalog
description: >
  Shopware Katalog Überblick, Kataloge verwalten, Produktkatalog, Shopware Katalog-Bereich,
  Produktverwaltung Überblick, Kategorien Hersteller Eigenschaften, Produktstreams, Bewertungen,
  Medien verwalten, Shopware 6 Katalog-Kapitel, Katalogstruktur
---

# Shopware 6 – Kataloge (Überblick)

Der Bereich **Kataloge** ist das Herzstück der Produktverwaltung in Shopware 6. Hier werden alle produktbezogenen Daten angelegt und gepflegt.

## Enthaltene Bereiche

| Bereich | Pfad im Admin | Skill |
|---|---|---|
| Produkte | Kataloge > Produkte | `sw-merchant-catalog-products` |
| Kategorien | Kataloge > Kategorien | `sw-merchant-catalog-categories` |
| Hersteller | Kataloge > Hersteller | `sw-merchant-catalog-manufacturers` |
| Eigenschaften | Kataloge > Eigenschaften | `sw-merchant-catalog-properties` |
| Dynamische Produktgruppen | Kataloge > Dynamische Produktgruppen | `sw-merchant-catalog-product-streams` |
| Bewertungen | Kataloge > Bewertungen | `sw-merchant-catalog-reviews` |
| Medien | Inhalte > Medien | `sw-merchant-catalog-media` |

## Schnelleinstieg

- **Neues Produkt anlegen**: Kataloge > Produkte > „Produkt hinzufügen"
- **Kategorie anlegen**: Kataloge > Kategorien > Kontextmenü in der Baumstruktur
- **Eigenschaft anlegen** (für Filter/Varianten): Kataloge > Eigenschaften > „Eigenschaft hinzufügen"
- **Hersteller anlegen**: Kataloge > Hersteller > „Hersteller anlegen"
- **Produktgruppe anlegen**: Kataloge > Dynamische Produktgruppen > „Produktgruppe anlegen"

## Abhängigkeiten zwischen Bereichen

```
Eigenschaften ──→ Produkte (Filter + Varianten)
Hersteller ──→ Produkte (Zuordnung)
Kategorien ──→ Produkte (Navigation)
Dynamische Produktgruppen ──→ Kategorien / Cross-Selling / Erlebniswelten
Medien ──→ Produkte / Kategorien / Hersteller
```

## Quelle
https://docs.shopware.com/de/shopware-6-de/kataloge
