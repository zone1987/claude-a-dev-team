# Migrationsprozess: Shopware 5 → Shopware 6 (Schritt für Schritt)

**Quelle**: https://docs.shopware.com/de/migration-de/Migrationsprozess

---

## Schritt 1: Erweiterungen installieren

### Im Zielshop (Shopware 6)
- Erweiterung: **SwagMigrationAssistent** (aus Community Store)
- Dokumentation gilt ab Version **16.0.0** des Assistenten

### Im Quellshop (Shopware 5)
- Erweiterung: **SwagMigrationConnector**

> **Empfehlung:** Datenmigration vollständig abschließen, **bevor** Design/Styling begonnen wird.
> Der Prozess ist iterativ und kann System-Resets erfordern.

---

## Schritt 2: Integration im Quellshop anlegen (API-Zugang)

**Pfad im Quellshop (SW6):** Einstellungen > System > Integrationen > Integration anlegen

| Feld | Beschreibung | Hinweis |
|---|---|---|
| **Name (1)** | Eindeutiger Name (z.B. „Migration") | Zur Unterscheidung mehrerer Integrationen |
| **Administrator (2)** | Checkbox aktivieren | Gibt Vollzugriff auf Quellshop-Ressourcen |
| **Zugangs-ID (3)** | Automatisch generiert | **Notieren!** — Wird in Schritt 3 benötigt |
| **Sicherheitsschlüssel (4)** | Automatisch generiert | **Notieren!** — Wird in Schritt 3 benötigt |

Abschließen: Button **„Integration speichern"** klicken.

---

## Schritt 3: Migrationsverbindung herstellen

**Pfad im Zielshop:** Einstellungen > Erweiterungen > Migrations-Assistent

### 3.1 Initiale Verbindung
1. Button **„Initiale Verbindung anlegen"** anklicken
2. Profil wählen:
   - `Shopware 5.5` für SW5-Migration
   - `Shopware 6` für SW6-zu-SW6-Migration
3. **„Fortfahren"** anklicken

### 3.2 Verbindung konfigurieren

**Verbindungsfelder (alle Quellsysteme):**

| Feld | Inhalt |
|---|---|
| **Name** | Eindeutiger Verbindungsname (wichtig bei mehreren Quellshops) |
| **Profil** | Quellsystem-Typ (z.B. Shopware 5.5) |
| **Schnittstelle** | Verbindungstyp (s. unten) |

> ⚠️ **Warnung:** Keine Bindestriche im Verbindungsnamen verwenden!

### 3.3 Verbindungstypen (Shopware 5)

#### API-Methode
| Feld | Beschreibung |
|---|---|
| **API-Schlüssel** | Aus SW5-Benutzerverwaltung |
| **Benutzername** | Admin-Benutzer (Gruppe: local_admins) |
| **Shopdomain** | Mit SSL-Status |

#### Local-Methode (Direktzugriff auf DB)
| Feld | Beschreibung |
|---|---|
| **DB-Host** | `localhost` oder URL |
| **DB-Port** | Standard: `3306` |
| **DB-Benutzer** | Benutzer mit Admin-Rechten |
| **DB-Passwort** | Zugehöriges Passwort |
| **DB-Name** | Name der SW5-Datenbank |
| **Root Verzeichnis** | Absoluter Installationspfad |

#### Shopware 6-Profil (API ist einzige Option)
Zugangs-ID und Sicherheitsschlüssel aus Schritt 2 eintragen.

---

## Schritt 4: Migrationsdaten kontrollieren

### Übersicht-Seite
Nach der Verbindungskonfiguration erscheint die Migrationsübersicht mit:
- (1) Shopsystem / aktuelle Verbindung
- System-Profil und Schnittstellen-Typ
- Zeitpunkt der letzten Verbindungsprüfung
- Zeitpunkt der letzten Migration

**Aktionen:**
- Button **„Verbindung bearbeiten"** (2) — Änderungen vornehmen
- Kontextmenü (3) mit Optionen:
  - Neue Verbindung anlegen
  - Zugangsdaten löschen
  - Zu anderer Verbindung wechseln
  - **Prüfsumme zurücksetzen** (erzwingt komplette Neuübertragung aller Daten)

### Datenauswahl
Checkboxen für gewünschte Daten setzen. Angezeigt wird:
- Datentyp (Shopdaten vs. Plugindaten/Erweiterungsdaten)
- Anzahl zu migrierender Datensätze
- Information zu Drittanbieter-Erweiterungen

> Drittanbieter-Daten erscheinen mit Typ **„Plugindaten"** in der Liste.

### Datencheck
Automatische Überprüfung auf Zuordnungsfähigkeit:
- **Erfolgreiche Zuordnung:** Migration kann sofort starten
- **Manuelle Zuordnung erforderlich:** Korrekturen vornehmen, dann **„Fortfahren"** klicken
- Beispiel für Nacharbeit: Standard-Zahlungsart zuweisen
- Automatische Zuordnungen lassen sich kontrollieren und nachjustieren

### Historie
- Alle bisherigen Migrationsversuche einsehbar
- Kontextmenü: **„Details anzeigen"** oder **„Protokoll herunterladen"** (.txt-Datei)

---

## Schritt 5: Migration starten

Button **„Migration starten"** anklicken.

### 6 Migrationsphasen

#### Phase 1: Lesen der Daten
- Alle Datensätze aus dem Quellshop werden erfasst
- Für jeden Datensatz wird eine **Prüfsumme** generiert
- Bereits übertragene, unveränderte Daten werden **nicht erneut migriert**
- Prüfsummen zurücksetzen: Kontextmenü > „Prüfsumme zurücksetzen" (erzwingt Vollübertragung)

#### Phase 2: Fehlerbehebung (intelligente Pause)
- Problematische Datensätze werden identifiziert
- Korrekturen direkt in der Admin-Oberfläche möglich
- Kein Neustart erforderlich nach Korrekturen

#### Phase 3: Schreiben der Daten
Automatische Erstellung falls im Zielshop noch nicht vorhanden:
- Kundengruppen
- Kategorien
- Sprachen
- Währungen
- Verkaufskanäle

#### Phase 4: Download
- Mediendateien werden aus dem Quellshop heruntergeladen
- Ablage in der Medienverwaltung des Zielshops

#### Phase 5: Aufräumen
- Zwischengespeicherte Daten aus Tabelle `swag_migration_data` werden gelöscht

#### Phase 6: Indexierung
- Alle Shopware-Indexer werden neu angestoßen
- Gewährleistet Shopware-interne Datenintegrität

### Logbuch
- Fehler, Warnungen, Informationen nach der Migration
- Download-Link: **„Protokoll herunterladen"**
- Auch später über **Historie > Details** abrufbar

---

## Migration erneut durchführen

Die Migration kann **beliebig oft** wiederholt werden.

**Standard-Verhalten (mit Prüfsummen):**
- Geänderte Daten werden erneut migriert
- Unveränderte Daten werden übersprungen

**Vollständige Neuübertragung erzwingen:**
1. Migrationsübersicht aufrufen
2. Shopsystem-Bereich > Kontextmenü (1)
3. **„Prüfsumme zurücksetzen"** wählen
4. Alle Daten werden im Zielsystem **überschrieben**

---

## Shopware 5: Metadaten-Anpassung vor Migration

Einige Metadaten werden auf **varchar(255)** gekürzt:

| Tabelle | Spalten |
|---|---|
| s_articles | description |
| s_categories | metadescription, metakeywords |

> **Hinweis:** Texte über 255 Zeichen werden abgeschnitten. Vor der Migration prüfen!

---

*Quelle: https://docs.shopware.com/de/migration-de/Migrationsprozess | https://docs.shopware.com/de/migration-de/shopware6-Migrationsprozess*
