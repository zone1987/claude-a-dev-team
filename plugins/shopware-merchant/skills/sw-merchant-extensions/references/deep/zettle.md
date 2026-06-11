# Zettle by PayPal – Point-of-Sale-Integration

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/zettle

## Überblick

**Zettle by PayPal** ermöglicht Kartenzahlungen am physischen Verkaufsort (POS) über ein
Chip-Card-Reader-Gerät für Smartphones und Tablets. Die Integration mit Shopware 6 läuft
als **eigener Verkaufskanal-Typ** und synchronisiert Produktdaten zwischen Online-Shop und POS.

**Wichtig**: Zettle ist eine **Komponente von PayPal** – keine eigenständige Extension.
Keine separate Installation nötig (kommt mit PayPal).

---

## Einrichtung

### Voraussetzungen
- PayPal Extension installiert und aktiv
- Zettle-Konto: https://zettle.com (separates Konto erforderlich)
- Zettle-Hardware (Kartenlesegerät)

### Setup-Wizard
1. **Verkaufskanäle** → Neuen Kanal hinzufügen → "Zettle" wählen
2. Setup-Wizard führt durch alle Konfigurationsschritte

---

## Konfiguration im Detail

### Schritt 1: Konto verknüpfen
1. API-Key aus dem **Zettle-Admin-Panel** generieren:
   - Zettle Portal: https://my.zettle.com/integrations
   - "Add integration" → API-Key kopieren
2. Im Shopware Admin: Zettle-Kanal → API-Key eintragen

### Schritt 2: Kanaleinstellungen
| Feld | Beschreibung |
|---|---|
| Kanalname | Interner Name (z. B. "Marktstand Berlin") |
| Shop-Domain | Domain, aus der Produktmedien geladen werden |

### Schritt 3: Produktsynchronisierung
Drei Optionen für die initiale Synchronisierung:

| Option | Beschreibung |
|---|---|
| **Nur Shopware-Produkte nutzen** | Zettle-Katalog wird durch Shopware-Produkte ersetzt |
| **Bestehenden Zettle-Katalog ersetzen** | Alle Zettle-Produkte werden durch Shopware-Produkte ersetzt |
| **Shopware-Produkte hinzufügen** | Shopware-Produkte werden zum bestehenden Zettle-Katalog hinzugefügt |

### Schritt 4: Preissynchronisierung
| Option | Beschreibung |
|---|---|
| Preise mit MwSt. synchronisieren | Bruttopreise an Zettle übermitteln |
| Preise ohne MwSt. synchronisieren | Nettopreise übermitteln (MwSt. in Zettle konfigurieren) |
| Preise in Zettle separat verwalten | Keine Preissynchronisierung |

---

## Laufende Verwaltung

Im Zettle-Verkaufskanal-Dashboard:

| Bereich | Inhalt |
|---|---|
| **Kontostatus** | Verbindungsstatus zu Zettle |
| **Synchronisationshistorie** | Protokoll aller Sync-Vorgänge |
| **Synchronisierte Produkte** | Liste der übertragenen Produkte |
| **Detaillierte Logs** | Technische Sync-Details und Fehler |

### Manuelle Synchronisierung
Jederzeit manuell anstoßen:
- Inventar synchronisieren
- Produktbilder synchronisieren
- Produktdetails synchronisieren

---

## Einschränkungen

| Einschränkung | Details |
|---|---|
| Custom Products | Konfigurierbare Produkte werden als Standard-Produkte ohne Optionen synchronisiert |
| Produktbeschreibungen | Maximal **1.024 Zeichen** (längere Texte werden abgeschnitten) |
| Varianten | Werden als separate Produkte in Zettle angelegt |
| Digitale Produkte | Nicht für POS geeignet |

---

## Anwendungsszenarien

- **Händler mit Online-Shop + Marktstand**: Gleicher Produktkatalog für beide Kanäle
- **Popup-Store**: Temporärer stationärer Verkauf mit Online-Shop-Produkten
- **Event-Verkauf**: Merchandise auf Veranstaltungen
- **Laden + Online**: Einheitliches Inventar-Management
