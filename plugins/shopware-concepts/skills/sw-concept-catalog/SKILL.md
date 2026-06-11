---
name: sw-concept-catalog
description: >
  Shopware Produktkatalog: Products (Varianten, Properties, Options), Categories (Tree, SEO, CMS),
  Sales Channels (Domains, Navigation, Sichtbarkeit). Trigger: "Produktkatalog", "wie funktionieren Produkte",
  "Shopware Varianten", "Properties vs Options", "Kategoriebaum", "Sales Channel Konzept",
  "product variants shopware", "category tree shopware", "sales channel shopware",
  "Dynamic Product Groups", "product visibility", "wie ist der Produktkatalog aufgebaut",
  "Shopware catalog concept", "Produkteigenschaften".
---

# Shopware Produktkatalog — Konzept

Vollständige Konzept-Doku: `references/deep/catalog.md`

## Kurzüberblick

### Produkte

- **Selbst-referenzierendes Entity** — Parent-Produkt + Kind-Varianten (Inheritance)
- **Properties** — nicht-variantenbestimmend (Herkunft, Waschhinweis)
- **Options** — variantenbestimmend (Größe, Farbe)
- **Configurator** — Store API liefert alle Variantenoptionen für die Auswahl im Frontend

### Kategorien

- **Baumstruktur** — `parentId`, `path`, `level` für Breadcrumbs und Navigation
- **Typen**: `page`, `folder`, `link`
- **CMS-Layout-Vererbung** — fehlt `cmsPageId`, wird vom Parent übernommen
- **Dynamic Product Groups** — Stream-basierte Zuweisung statt manueller Produkt-Zuweisung
- **SEO** — URL-Templates und per-Sales-Channel-Domain-Routing

### Sales Channels

- **Ein-Shopware-Instanz, mehrere Stores** — Sprache, Währung, Zahlungsarten pro Channel
- **Domains** — je Domain: Sprache + Währung + Snippet-Set (getrennte Subdomains empfohlen)
- **Navigation Roots** — `navigation`, `footer`, `service` Category-Einstiegspunkte
- **Product Visibility** — Produkte müssen je Sales Channel sichtbar geschaltet sein

Technische Umsetzung: `shopware-core`, `shopware-data` (Dev-Plugins)
