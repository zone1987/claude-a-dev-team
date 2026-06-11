# Advanced Search – Hochleistungssuche für den Storefront

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/advanced-search  
**Plan**: Shopware Evolve (oder höher)  
**Technologie**: Elasticsearch (bis SW 6.4) / OpenSearch (ab SW 6.5.6.0)

## Überblick

**Advanced Search** bietet einfache Konfigurationsmöglichkeiten und aufgrund der
Elasticsearch/OpenSearch-Basis **hohe Performance** auch bei großen Produktkatalogen.
Ab Shopware 6.5 ist der Nachfolger **Advanced Search 2.0** zu nutzen.

---

## Versionen & Kompatibilität

| Shopware Version | Advanced Search Version | Suchmaschine |
|---|---|---|
| bis 6.4.20.2 | Advanced Search 1.x | Elasticsearch |
| 6.5.x | Advanced Search 2.0 | OpenSearch (ab 6.5.6.0) |
| 6.6+ | Advanced Search 2.0+ | OpenSearch |

---

## Voraussetzungen

- **Elasticsearch-Instanz** (für 1.x) oder **OpenSearch-Instanz** (für 2.0) zwingend erforderlich
- Environment-Variable setzen:
  ```
  SHOPWARE_ES_INDEXING_ENABLED=1
  ```
- Index erstellen:
  ```bash
  php bin/console es:index
  php bin/console messenger:consume
  # Optional:
  php bin/console es:create:alias
  ```

---

## Installation

1. **Erweiterungen > Meine Erweiterungen** im Admin
2. Im Shopware Account Tab einloggen (Lizenzverifizierung)
3. Advanced Search herunterladen und installieren
4. Aktivieren
5. Index neu aufbauen (siehe oben)

---

## Konfigurationsbereiche

### 1. Durchsuchbare Informationen (Searchable Information)

Festlegen, **welche Datenfelder** indexiert werden und mit welcher Priorität:

| Entität | Felder (Beispiele) |
|---|---|
| Produkte | Name, Beschreibung, EAN, Artikelnummer, Hersteller, Eigenschaften |
| Kategorien | Name, Beschreibung, Keywords |
| Hersteller | Name, Beschreibung |

Optionen pro Feld:
- **Teilübereinstimmung (Partial Match)**: Auch Teile des Suchbegriffs finden
- **Komposita (Compound Words)**: Zusammengesetzte Wörter (z. B. "Laufschuhe" findet "Lauf" + "Schuhe")
- **Priorität**: Höhere Zahl = wichtiger in der Suchreihenfolge

### 2. Vorschau (Preview)

- Suchfunktion **live testen** nach Verkaufskanal und Entitätstyp
- Zeigt Relevanzbewertungen der Treffer
- Ideal zum Prüfen von Konfigurationsänderungen vor dem Go-Live

### 3. Boostings

Gezielte Sichtbarkeitsanpassungen für bestimmte Inhalte:

| Typ | Beschreibung |
|---|---|
| Produkt-Boostings | Über dynamische Produktgruppen definieren |
| Kategorie-Boostings | Über benutzerdefinierte Regeln (Rule Builder) |
| Hersteller-Boostings | Über benutzerdefinierte Regeln |

### 4. Actions (Suchumleitungen)

Kunden **automatisch weiterleiten** bei bestimmten Suchbegriffen:
- Zu einer URL (extern oder intern)
- Zu einem bestimmten Produkt
- Zu einer bestimmten Kategorie

Beispiel: Suche nach "Sale" → automatische Weiterleitung zur Sale-Kategorie

### 5. Synonyme

Gleichwertige oder definierende Synonyme konfigurieren:

| Typ | Beispiel |
|---|---|
| Gleichwertig | "Hose" ↔ "Jeans" ↔ "Chino" |
| Definierend | "Smartphone" → "Handy, Mobiltelefon, Telefon" |

- Mehrere Sprachen werden unterstützt
- Erweitert die Suchabdeckung erheblich

---

## Index-Verwaltung

| Befehl | Beschreibung |
|---|---|
| `php bin/console es:index` | Index neu aufbauen |
| `php bin/console es:create:alias` | Alias neu setzen |
| `php bin/console es:admin:index` | Admin-Suchindex aktualisieren |
| `php bin/console messenger:consume` | Message-Queue abarbeiten |

> **Wichtig**: Bei neuen Produkten oder Preisänderungen muss kein manueller Rebuild erfolgen,
> wenn `SHOPWARE_ES_INDEXING_ENABLED=1` gesetzt ist – dies erfolgt automatisch.

---

## Unterschied zur Standard-Suche

| Feature | Standard-Suche | Advanced Search |
|---|---|---|
| Technologie | Datenbankbasiert (MySQL) | Elasticsearch/OpenSearch |
| Performance bei großem Katalog | Begrenzt | Sehr hoch |
| Konfigurierbare Felder | Nein | Ja |
| Synonyme | Nein | Ja |
| Boostings | Nein | Ja |
| Actions/Weiterleitungen | Nein | Ja |
| Partial Match | Begrenzt | Vollständig |
