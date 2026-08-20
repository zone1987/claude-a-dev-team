# Shopware Produktkatalog — Konzept

Vollständige Konzept-Doku: `CATALOG-DETAIL.md`

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
