# Was wird bei der Migration übernommen?

**Quelle**: https://docs.shopware.com/de/migration-de/Systemvoraussetzungen  
(Detailseite war zum Crawl-Zeitpunkt via category-Parameter erreichbar)

## Grundprinzip

Der **Migrationsassistent** (SwagMigrationAssistent) überträgt Daten aus dem Quellsystem
nach Shopware 6. Was genau migriert wird, hängt vom Quellsystem ab.

---

## Shopware 5 → Shopware 6

### Shopdaten (Standard, per Checkbox wählbar)

| Datentyp | Hinweise |
|---|---|
| Produkte | Inkl. Varianten, Eigenschaften, Preise |
| Kategorien | Kategoriehierarchie und Zuordnungen |
| Hersteller | Herstellerdaten |
| Kunden | Konten und persönliche Daten |
| Kundenadressen | Liefer- und Rechnungsadressen |
| Bestellungen | Bestellungen und Positionen |
| Medien | Bilder und Mediendateien (Download aus Quell-Shop) |
| Steuerregeln | Steuerklassen |
| Währungen | Währungskonfiguration |
| Sprachen | Sprachkonfiguration |

### Plugindaten (Drittanbieter)
Manche Drittanbieter-Erweiterungen stellen eigene Migrationsprofile bereit.
Diese erscheinen in der Datenauswahl mit dem Typ **„Plugindaten"**.

### Nicht migriert (typisch)
- Shop-Design / Theme (muss neu aufgebaut werden)
- Eigene Plugin-Konfigurationen (nur wenn Plugin Migrationsprofil anbietet)
- SEO-URLs (werden neu generiert)
- CMS-Seiten / Erlebniswelten (müssen neu erstellt werden)

---

## Shopware 6 → Shopware 6

Umfang analog zu SW5→SW6, da derselbe Migrationsassistent genutzt wird.
Einschränkung: Quell- und Zielsystem müssen **identische Shopware-Version** haben.

---

## Magento → Shopware 6

Siehe Magento-Wörterbuch (Begriff-Mapping Magento ↔ Shopware):
`docs.shopware.com/de/migration-de/magento`

Typische Daten: Produkte, Kategorien, Kunden, Bestellungen, Medien.

---

## Metadaten-Beschränkung (Shopware 5)

Bei der Migration aus Shopware 5 werden einige Metadaten **auf 255 Zeichen gekürzt**:

| Tabelle | Spalten |
|---|---|
| s_articles | description |
| s_categories | metadescription, metakeywords |

**Hinweis:** Längere Texte werden nach 255 Zeichen abgeschnitten. Inhalte vorher prüfen.

---

## Systemvoraussetzungen prüfen (Shopware 5)

Plugin **SwagMigrationAssistent** im SW5-Backend installieren:
1. Backend neu laden nach Installation und Aktivierung
2. Fragezeichen-Symbol in der Menüleiste anklicken
3. „Shopware 6 Update-Check" öffnen
4. **Tab „Voraussetzungen"**: zeigt erfüllte/nicht erfüllte Serveranforderungen
5. **Tab „Plugins"**: zeigt welche Plugins für SW6 verfügbar/konfigurierbar sind

---

*Quelle: https://docs.shopware.com/de/migration-de/Systemvoraussetzungen*
