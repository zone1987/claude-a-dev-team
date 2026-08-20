# Suche in der Administration

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/suche-administration  
**AND/OR-Suche ab**: Shopware 6.4.19.0

## Überblick

Die Shopware-6-Administration enthält eine **zentrale Suchleiste** im oberen Bereich,
die alle aktivierten Entitäten durchsucht.

---

## Zugang & Bedienung

- **Position**: Obere Leiste der Administration, mittig
- **Öffnen per Tastenkürzel**: `Strg/Cmd + F`
- **Modul-Filter öffnen**: `#` eingeben → Dropdown zur Modulauswahl

---

## Modul-Filterung

Über ein **Dropdown in der Suchleiste** kann die Suche auf bestimmte Bereiche eingegrenzt werden:

| Modulkürzel | Durchsuchter Bereich |
|---|---|
| `#produkte` | Produktkatalog |
| `#bestellungen` | Bestellungen |
| `#kunden` | Kundenstammdaten |
| `#kategorien` | Kategoriebaum |
| `#medien` | Medienverwaltung |
| `#hersteller` | Herstellerliste |

---

## Sucheinstellungen personalisieren

Jeder Benutzer kann unter **Profil > Sucheinstellungen** individuell konfigurieren,
welche Entitäten in der Suche erscheinen sollen:

- **Alle auswählen**: Alle Entitäten aktivieren
- **Alle abwählen**: Alle Entitäten deaktivieren
- **Standard wiederherstellen**: Shopware-Default zurücksetzen

---

## Praktische Anwendungsfälle

| Szenario | Vorgehen |
|---|---|
| Kunde ruft mit Rechnungsnummer an | Rechnungsnummer in Suche eingeben → Bestellung direkt öffnen |
| Produkt nach Name-Fragment suchen | Teilbegriff eingeben → aus allen aktiven Modulen werden Treffer gezeigt |
| Produkt nach EAN/GTIN suchen | EAN/GTIN eingeben (Einstellung muss aktiviert sein) |

---

## Erweiterte AND/OR-Suche (ab 6.4.19.0)

Für komplexere Abfragen kann die AND/OR-Suchfunktion aktiviert werden.

### Voraussetzungen
- OpenSearch als Suchmaschine konfiguriert
- Environment-Variable in `.env`:
  ```
  SHOPWARE_ES_INDEXING_ENABLED=1
  ```
- Such-Index neu erstellen:
  ```bash
  php bin/console es:admin:index
  ```

### Verwendung
- **AND**: Alle Suchbegriffe müssen vorkommen
- **OR**: Mindestens ein Suchbegriff muss vorkommen
- Kombination über Suchoperatoren in der Eingabe

> **Hinweis**: Diese Funktion erfordert Server-Konfiguration und ist nicht im Standard-Setup
> ohne Elasticsearch/OpenSearch verfügbar.

---

## Zusammenhang mit Advanced Search

Die Standard-Admin-Suche ist von der **Advanced Search Extension** für die Storefront
zu unterscheiden. Die Admin-Suche betrifft nur das Backend.

→ Für Storefront-Suche: `../../../sw-merchant-extensions/references/deep/advanced-search.md`
