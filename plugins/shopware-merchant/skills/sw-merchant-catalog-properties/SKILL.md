---
name: sw-merchant-catalog-properties
description: >
  Shopware Eigenschaften verwalten, Eigenschaft anlegen, Eigenschaftswerte, Eigenschaftsoptionen,
  Produktfilter Eigenschaften, Varianten Eigenschaften, Eigenschaftsgruppe, Farb-Eigenschaft,
  Bild-Eigenschaft, Dropdown-Eigenschaft, Text-Eigenschaft, Sortierung Eigenschaften,
  Ausprägungen anlegen, Eigenschaft bearbeiten, Shopware Eigenschaften Übersicht
---

# Shopware 6 – Eigenschaften

Eigenschaften werden unter **Kataloge > Eigenschaften** verwaltet. Sie dienen als filterbare
Produktinformationen (z. B. Größe, Farbe) und als Basis für Produktvarianten.

## Eigenschaft anlegen

1. Kataloge > Eigenschaften > **„Eigenschaft hinzufügen"**
2. Name eingeben (erscheint auf Produktdetailseite und in Filtern)
3. Optionale Felder: Beschreibung, Filterbarkeit, Anzeigetyp, Sortierung, Position
4. Ausprägungen (Werte) hinzufügen

## Anzeigetypen

| Typ | Darstellung im Filter |
|---|---|
| Text | Textuell |
| Farbe | HEX-Farbwert |
| Bild | Custom-Bild |
| Dropdown | Dropdown im Produkt, Text im Filter |

## Sortieroptionen

- **Alphanumerisch**: Standard a–z, 1–10
- **Benutzerdefiniert**: Manuelle Positionsreihenfolge

## Ausprägungen (Werte) anlegen

Jede Ausprägung benötigt: Name, Position (für benutzerdefinierte Sortierung).
Optional: Farb-HEX (bei Typ Farbe) oder Bild (bei Typ Bild).

> **Achtung**: Eigenschaft löschen entfernt sie von ALLEN zugewiesenen Produkten!

Siehe `references/deep/properties.md` für vollständige Details.

## Quelle
https://docs.shopware.com/de/shopware-6-de/produkte/eigenschaften
