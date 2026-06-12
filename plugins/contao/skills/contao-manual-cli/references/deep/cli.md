# Contao 5.x — Kommandozeilenbefehle (CLI)

Quellen:
- https://docs.contao.org/5.x/manual/de/cli/
- https://docs.contao.org/5.x/manual/de/cli/automator/
- https://docs.contao.org/5.x/manual/de/cli/datenbank-backups/
- https://docs.contao.org/5.x/manual/de/cli/crawl/
- https://docs.contao.org/5.x/manual/de/cli/maintenance-mode/
- https://docs.contao.org/5.x/manual/de/cli/migrate/
- https://docs.contao.org/5.x/manual/de/cli/resize-images/
- https://docs.contao.org/5.x/manual/de/cli/user/
- https://docs.contao.org/5.x/manual/de/cli/dca/

---

## Übersicht

Die Kommandozeile bietet zahlreiche Möglichkeiten zur Produktivitätssteigerung. Der Contao Manager stellt eine grafische Oberfläche für einige CLI-Funktionen bereit, deckt aber nur einen Bruchteil ab.

**Alle verfügbaren Befehle anzeigen:**
```bash
php vendor/bin/contao-console list
```

**Hilfe zu einem Befehl:**
```bash
php vendor/bin/contao-console <befehl> --help
```

---

## 1. contao:automator

Schnittstelle zur Contao-Klasse `Automator` für allgemeine Wartungsaufgaben.

**Syntax:**
```bash
php vendor/bin/contao-console contao:automator [<task>]
```

Ohne `<task>` erscheint eine interaktive Auswahl.

**Verfügbare Aufgaben:**

| Aufgabe | Funktion |
|---------|----------|
| `purgeSearchTables` | Suchindex löschen (`tl_search`, `tl_search_index`) |
| `purgeUndoTable` | Papierkorb leeren (`tl_undo`) — **nicht rückgängig machbar!** |
| `purgeVersionTable` | Versionsverlauf löschen (`tl_version`) |
| `purgeSystemLog` | Systemprotokoll löschen |
| `purgeImageCache` | Bildercache leeren (verarbeitete/skalierte Bilder) |
| `purgeScriptCache` | JavaScript und CSS-Cache leeren |
| `purgePageCache` | HTML-Seitencache leeren |
| `purgeSearchCache` | Suchergebniscache leeren |
| `purgeInternalCache` | Internen Contao-Cache leeren |
| `purgeTempFolder` | Temporären Ordner leeren (`system/tmp`) |
| `purgeRegistrations` | Nicht aktivierte Mitgliederregistrierungen löschen |
| `purgeOptInTokens` | Abgelaufene Double-Opt-In-Tokens löschen |
| `purgeXmlFiles` | XML-Dateien aus `generateXmlFiles` löschen |
| `generateSitemap` | `sitemap.xml` aus Seitenbaum erstellen |
| `generateXmlFiles` | XML-Dateien erstellen + Hook aufrufen |
| `generateSymlinks` | Symlinks zum Web-Verzeichnis erstellen |
| `generateInternalCache` | Internen Cache aufwärmen |

---

## 2. contao:backup (Datenbank-Backups)

Umfassendes Backup-System für Contao-Datenbanken. Backups werden standardmäßig in `var/backups/` gespeichert.

### contao:backup:create

```bash
php vendor/bin/contao-console contao:backup:create
```

Backup-Dateiname: `backup__20220126153243.sql.gz` (automatisch mit Zeitstempel).

**Benutzerdefinierter Name:**
```bash
php vendor/bin/contao-console contao:backup:create mein_backup__20220101000000.sql
```

**Optionen:**

| Option | Beschreibung |
|--------|-------------|
| `--ignore-tables` / `-i` | Kommagetrennte Tabellen ausschließen |
| `--format` | Ausgabeformat: `txt` oder `json` |

### contao:backup:list

```bash
php vendor/bin/contao-console contao:backup:list
```

Zeigt vorhandene Backups mit Erstellungsdatum und Größe.

### contao:backup:restore

```bash
# Neuestes Backup wiederherstellen
php vendor/bin/contao-console contao:backup:restore

# Spezifisches Backup wiederherstellen
php vendor/bin/contao-console contao:backup:restore backup__20220126153243.sql.gz
```

### Automatisierte Backups

**Cronjob (täglich 23:10 Uhr):**
```cron
10 23 * * * /pfad/zum/system/vendor/bin/contao-console contao:backup:create
```

### Konfiguration

```yaml
# config/config.yaml
contao:
    backup:
        # Tabellen die nicht gesichert werden (z.B. Logs, Crawl-Daten)
        ignore_tables:
            - tl_crawl_queue
            - tl_log
            - tl_search
            - tl_search_index
            - tl_search_term
        # Maximale Anzahl aufzubewahrender Backups
        keep_max: 5
        # Aufbewahrungsintervalle (ältestes Backup pro Intervall behalten)
        keep_intervals:
            - '1D'   # 1 Tag
            - '7D'   # 7 Tage
            - '14D'  # 14 Tage
            - '1M'   # 1 Monat
```

**Zeitbezeichner:**
- `Y` Jahre, `M` Monate, `D` Tage, `W` Wochen
- `T`-Präfix für: `H` Stunden, `M` Minuten, `S` Sekunden
- Kombinierbar: `1Y2MT5H`

**Hinweis:** `keep_max` sollte mindestens um 1 größer sein als Anzahl der `keep_intervals`.

---

## 3. contao:crawl

HTTP-Crawler basierend auf der Escargot-Bibliothek. Crawlt systematisch alle URLs.

**Syntax:**
```bash
php vendor/bin/contao-console contao:crawl [options] [<job>]
```

Das optionale `job`-Argument ermöglicht das Fortsetzen unterbrochener Crawling-Prozesse.

### Subscriber

| Subscriber | Funktion |
|------------|---------|
| `search-index` | Suchindex aktualisieren (nur bei aktivierter Suche) |
| `broken-link-checker` | Fehlerhafte Links prüfen |

### Optionen

| Option | Beschreibung |
|--------|-------------|
| `--subscribers` / `-s` | Kommagetrennte Liste aktivierter Subscriber |
| `--concurrency` / `-c` | Anzahl gleichzeitiger Anfragen (Standard: 5) |
| `--delay` | Verzögerung zwischen Anfragen (in Mikrosekunden) |
| `--max-requests` | Maximale Anfragen pro Durchlauf |
| `--max-depth` | Crawl-Tiefe (Standard: 3) |
| `--enable-debug-csv` | CSV-Datei aktivieren (als `crawl_debug_log.csv`) |
| `--debug-csv-path` | Eigenen CSV-Pfad angeben |

### Beispiele

```bash
# Nur Suchindex aktualisieren
vendor/bin/contao-console contao:crawl -s search-index

# 10 gleichzeitige Requests, max. 2 Ebenen tief
vendor/bin/contao-console contao:crawl --concurrency=10 --max-depth=2

# Debug-CSV erstellen
vendor/bin/contao-console contao:crawl --enable-debug-csv
```

### Voraussetzungen

Domain muss im Startpunkt konfiguriert sein. Für CLI ohne HTTP-Kontext:
```yaml
# config/parameters.yaml
parameters:
    router.request_context.host: 'example.org'
    router.request_context.scheme: 'https'
```

---

## 4. contao:maintenance-mode

Versetzt die gesamte Installation (Back- und Frontend) in den Wartungsmodus.

**Syntax:**
```bash
php vendor/bin/contao-console contao:maintenance-mode [options] [<state>]
```

**States:**

| State | Beschreibung |
|-------|-------------|
| `enable` / `on` | Wartungsmodus aktivieren |
| `disable` / `off` | Wartungsmodus deaktivieren |

**Optionen:**

| Option | Beschreibung |
|--------|-------------|
| `--template` | Alternatives Twig-Template (Standard: `@ContaoCore/Error/service_unavailable.html.twig`) |
| `--templateVars` | Zusätzliche Template-Variablen als JSON |

**Manuell deaktivieren:** Datei `var/maintenance.html` löschen.

---

## 5. contao:migrate

Führt Datenbankmigrationen durch — nach Neuinstallationen, Contao-Updates oder Erweiterungsinstallationen.

Umfasst:
- Update-Skripte
- Registrierte Migrationen von Erweiterungen
- Legacy-Dateien
- Datenbankschema-Updates

**Syntax:**
```bash
php vendor/bin/contao-console contao:migrate [options]
```

**Optionen:**

| Option | Beschreibung |
|--------|-------------|
| `--with-deletes` | Migrationen mit `DROP`-Befehlen ausführen |
| `--schema-only` | Nur Datenbankschema migrieren (keine Update-Skripte) |
| `--migrations-only` | Nur Migrationen, keine Tabellenaktualisierungen |
| `--dry-run` | Anstehende Änderungen anzeigen ohne Ausführung |
| `--no-interaction` | Bestätigungsfragen automatisch mit „Ja" beantworten |
| `--no-backup` | Standardmäßiges Datenbank-Backup deaktivieren |

---

## 6. contao:resize-images

Erstellt fehlende, verzögert erzeugte Bilder.

**Syntax:**
```bash
php vendor/bin/contao-console contao:resize-images [options]
```

**Optionen:**

| Option | Beschreibung |
|--------|-------------|
| `--concurrent` | Gleichzeitige Prozesse oder CPU-Begrenzung. Wert < 0.5 = max. 50% CPU |
| `--time-limit` | Zeitlimit in Sekunden |
| `--image` | Spezifisches Bild (ohne `assets/images`-Präfix, z.B. `1/foobar-f6eac395d.jpg`) |
| `--no-sub-process` | Keine Unterprozesse (Vorsicht: extremer Speicherverbrauch möglich) |
| `--preserve-missing` | Latente Bildreferenzen auf nicht existierende Bilder behalten |

**Beispiel für Hosting mit CPU-Begrenzung:**
```bash
php vendor/bin/contao-console contao:resize-images --concurrent=0.3 --time-limit=300
```

---

## 7. contao:user

Verwaltung von Backend-Benutzern.

### contao:user:list

```bash
php vendor/bin/contao-console contao:user:list [options]
```

| Option | Beschreibung |
|--------|-------------|
| `--admins` | Nur Administratoren anzeigen |
| `--column` | Anzuzeigende Spalten (mehrfach verwendbar) |
| `--format` | Ausgabeformat: `txt` oder `json` |

### contao:user:create

```bash
php vendor/bin/contao-console contao:user:create [options]
```

Interaktive Abfrage aller Angaben wenn ohne Optionen ausgeführt.

| Option | Beschreibung |
|--------|-------------|
| `--username` | Benutzername |
| `--name` | Vollständiger Name |
| `--email` | E-Mail-Adresse |
| `--password` | Passwort |
| `--admin` | Als Administrator anlegen |
| `--groups` | Gruppen-IDs (kommagetrennt) |
| `--change-password` | Passwortänderung beim ersten Login erzwingen |

### contao:user:password

```bash
php vendor/bin/contao-console contao:user:password <benutzername>
```

⚠️ **Sicherheit**: Passwort nicht direkt als Argument übergeben — wird in Bash-History gespeichert!

---

## 8. debug:dca

Entwicklungstool zur Analyse von Data Container Array (DCA) Konfigurationen.

**Syntax:**
```bash
php vendor/bin/contao-console debug:dca <container>
```

**Beispiel:**
```bash
php vendor/bin/contao-console debug:dca tl_page
```

Gibt die **finale, zusammengesetzte** Konfiguration des Containers aus — nach allen Modifikationen durch Anwendung und Erweiterungen.

Nützlich um zu verstehen, welche Felder, Callbacks und Konfigurationen aktiv sind.
