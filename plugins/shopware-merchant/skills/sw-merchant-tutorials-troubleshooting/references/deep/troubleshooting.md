# Shopware 6 — Tutorials: Troubleshooting (vollständige Referenz)

---

## 1. Admin-Passwort zurücksetzen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/admin-passwort-zuruecksetzen  
**Ab Version:** 6.0.0

Via Konsole (SSH-Zugriff erforderlich):

```bash
bin/console user:change-password "admin"
```

`"admin"` ist Platzhalter für den tatsächlichen Benutzernamen.

---

## 2. Defekte Erweiterung entfernen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/erweiterung-entfernen  
**Ab Version:** 6.1.0.0

> **Wichtig:** Immer zuerst ein Backup der Datenbank und Dateien anlegen.

### Schritt 1: Funktionen deaktivieren (vor Entfernung)

- Zahlungserweiterungen: Zahlungsart deaktivieren
- Versanderweiterungen: Versandmethode deaktivieren
- Themes: Theme des Verkaufskanals auf Standard wechseln

### Schritt 2: Datenbankeintrag entfernen

**Nur deaktivieren** (behält Daten):
```sql
UPDATE plugin SET active = 0 WHERE name = 'ErweiterungsName';
```

**Komplett entfernen:**
```sql
DELETE FROM plugin WHERE name = 'ErweiterungsName';
```

### Schritt 3: Erweiterungsdateien entfernen

Dateien aus `custom/plugins/` im Shopware-Hauptverzeichnis löschen.

---

## 3. Debuggen

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/fehlermeldungen-debuggen  
**Ab Version:** 6.1.0.0

### Ereignis-Logs (erster Anlaufpunkt)

Einstellungen > System > Ereignis-Logs

- Nach "Failed" oder "Error"-Einträgen suchen
- Details über Kontextmenü (…) > "Details anzeigen"
- Besonders nützlich für: E-Mail-Versand, Versandmethoden, unvollständige Produktdaten

### Log-Dateien

Speicherort: `/var/log/`

| Modus | Log-Datei | Inhalt |
|-------|-----------|--------|
| Produktion | `prod.log` | Nur kritische Fehler |
| Entwicklung | `dev.log` | Alle Meldungen |

Erweiterungen schreiben ebenfalls in `/var/log/` (z. B. PayPal). Bei fehlenden Logs: Hersteller kontaktieren.

### Debug-Modus aktivieren

**Achtung:** Nur kurzzeitig aktivieren — zeigt sensible Daten und verbraucht deutlich mehr Ressourcen.

1. `.env` Datei öffnen (Root-Verzeichnis)
2. `APP_ENV=prod` → `APP_ENV=dev` ändern
3. Cache leeren: `php bin/console cache:clear`

### Troubleshooting-Checkliste

**Schritt 1 — Erweiterungen deaktivieren:**
- Theme auf Standard-Shopware-Theme setzen
- Alle Drittanbieter-Erweiterungen deaktivieren (manuell oder per SQL)
- Einzeln wieder aktivieren um Problemverursacher zu identifizieren
- Support-Ticket über Shopware Account erstellen

**SQL zum Deaktivieren aller Nicht-Shopware-Erweiterungen:**
```sql
CREATE TABLE plugin_tmp LIKE plugin;
INSERT INTO plugin_tmp SELECT * FROM plugin;
UPDATE plugin SET active = 0 WHERE (author <> 'shopware AG' AND author <> 'Shopware') OR (author IS NULL);
```

**Schritt 2 — Core-Dateien prüfen:**
- `file-checker.php` oder Extension "FroshTools" für Datei-Integritätsprüfung

**Schritt 3 — Community einbinden:**
- Forum: https://forum.shopware.com/
- Slack: https://slack.shopware.com/
- Stack Overflow: `[shopware]`-Tag
- GitHub: https://github.com/shopware/shopware/issues (erst suchen, dann erstellen)

---

## 4. SQL Tipps & Tricks

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/sql-tipps-tricks  
**Ab Version:** 6.7.0.0

> **Warnung:** Immer Backup anlegen. Auf Live-Shops nur nach Prüfung anwenden.

### Katalog-Operationen

```sql
-- Alle Produkte löschen
DELETE FROM product;

-- Alle Eigenschaften löschen
DELETE FROM property_group;

-- Alle Kundendaten löschen (NUR vor Go-Live!)
DELETE FROM customer;

-- Alle Bestellungen löschen (NUR vor Go-Live!)
DELETE FROM `order`;
DELETE FROM `order_address`;
DELETE FROM `order_customer`;
DELETE FROM `order_delivery`;
DELETE FROM `order_delivery_position`;
DELETE FROM `order_line_item`;
DELETE FROM `order_tag`;
DELETE FROM `order_transaction`;
```

### System/Einstellungen

**Alle Nicht-Standard-Erweiterungen deaktivieren:**
```sql
CREATE TABLE plugin_tmp LIKE plugin;
INSERT INTO `plugin_tmp` SELECT * FROM `plugin`;
UPDATE `plugin` SET `active`= 0 WHERE (author <> 'shopware AG' AND author <> 'Shopware') OR (author IS NULL);
```

**Datenbankkollatierung prüfen (bei "Illegal mix of collations"):**
```sql
-- Einzelne Tabelle ändern
ALTER TABLE tabellenname CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Standard-Kundengruppe wiederherstellen:**
```sql
INSERT INTO `customer_group` (`id`, `display_gross`, `registration_active`, `created_at`, `updated_at`) VALUES
(UNHEX('CFBD5018D38D41D8ADCA10D94FC8BDD6'), 1, 0, '2021-01-01 00:00:00.00', NULL);
```

---

## 5. Fehlerbehebung im Migrationsprozess

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/hinweise-fuer-die-migration  
**Ab Version:** 6.7.0.0

### Wichtige Tabellen für die Fehleranalyse

| Tabelle | Verwendung |
|---------|-----------|
| `swag_migration_logging` | Logs mit Filter nach Fehlertyp und Entität |
| `swag_migration_mapping` | Zuordnungen zwischen Quell- und Zieldaten |
| `swag_migration_media_file` | Mediendateien-Migration |
| `swag_migration_data` | Rohdaten der Migration |

### Performance bei großen Datenmengen

Lokale Datenbankverbindung nutzen (im Migrations-Assistenten unter Verbindung bearbeiten) — reduziert Systemlast bei Millionen von Datensätzen.

### Fehler "Keine Verbindung hergestellt"

"Es konnte keine Verbindung zum angegebenen Server hergestellt werden" → Domain-Eingabe prüfen, Migrations-Erweiterung aktualisieren.

### Indexierungsprobleme

Wenn Produkte/Kategorien nach Migration nicht vollständig erscheinen:

**Voraussetzungen für vollständige Indexierung:**
- Mindestens 2 GB Server-RAM
- Keine lang laufenden Prozesse durch Server beendet
- Message Queue zurücksetzen

**Queue-Reset (SQL):**
```sql
DELETE FROM dead_message;
DELETE FROM enqueue;
DELETE FROM message_queue_stats;
TRUNCATE TABLE increment;
```

**Re-Indexierung:**
```bash
bin/console dal:refresh:index --use-queue
```

### Bereits migrierte Elemente erneut migrieren

Checksummen in `swag_migration_mapping` zurücksetzen:
```sql
UPDATE swag_migration_mapping 
SET checksum = null 
WHERE entity = "newsletter_recipient"
```

---

## 6. HTML Sanitizer

**Quelle:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/html-sanitizer  
**Ab Version:** 6.5.3.0  
**Gilt für:** Self-hosted (nicht Cloud)

### Funktion

Entfernt automatisch potenziell gefährlichen HTML-Code (XSS-Schutz). Betrifft alle Texteingaben im Admin (z. B. Produktbeschreibungen).

### HTML-Tags whitelisten

Datei anlegen/erweitern: `config/packages/z-shopware.yaml`:

```yaml
shopware:
    html_sanitizer:
        sets:
            -   name: basic
                tags: [ "img" ]
                attributes: [ "src", "alt", "style" ]
                options:
                    - key: HTML.Trusted
                      value: true
                    - key: CSS.Trusted
                      value: true
```

Nach Änderungen: Cache leeren.

### Sanitizer deaktivieren (nicht empfohlen)

```yaml
shopware:
    html_sanitizer:
        enabled: false
```

**Risiken:** XSS-Angriffe, Datenverletzungen, Compliance-Probleme, Reputationsschäden.

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/troubleshooting — Stand: 2026-06*
