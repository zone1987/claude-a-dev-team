---
name: sw-merchant-catalog-product-streams
description: >
  Shopware dynamische Produktgruppen, Produktstream anlegen, dynamische Produktgruppe bearbeiten,
  Produktgruppe Bedingungen, Rule Builder Produkte, Produktfilter automatisch, Cross-Selling dynamisch,
  Kategorie dynamisch befüllen, Produktgruppe Vorschau, UND ODER Verknüpfung Produkte,
  Produktgruppe Shopware, Produktstream Shopware 6
---

# Shopware 6 – Dynamische Produktgruppen

Dynamische Produktgruppen werden unter **Kataloge > Dynamische Produktgruppen** verwaltet.
Sie gruppieren Produkte automatisch nach definierten Regeln.

## Produktgruppe anlegen

1. Kataloge > Dynamische Produktgruppen > **„Produktgruppe anlegen"**
2. Name und Beschreibung eingeben
3. Bedingungen definieren (Rule Builder)
4. Vorschau prüfen
5. Speichern

## Bedingungsoperatoren

| Operator | Bedeutung |
|---|---|
| Gleich | Exakter Wert |
| Ungleich | Nicht dieser Wert |
| Eins von | Einer der Werte |
| Keins von | Keiner der Werte |
| Alle von | Alle Werte müssen zutreffen |
| Alle außer | Alle außer diesen |

## Verknüpfungen

- **UND**: Alle Bedingungen müssen erfüllt sein
- **ODER**: Eine der Bedingungen reicht
- **Unterbedingungen**: Verschachtelung möglich

## Einsatzbereiche

- Kategorien (dynamisch befüllen statt manuell)
- Produktfeeds / Produktvergleiche
- Erlebniswelten (Produkt-Slider Commerce-Block)
- Cross-Selling auf Produktdetailseite

Siehe `references/deep/product-streams.md` für vollständige Regeloptionen.

## Quelle
https://docs.shopware.com/de/shopware-6-de/Kataloge/DynamischeProduktgruppen
