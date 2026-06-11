# Shopware 6 — Backup & Update-Vorbereitung: Vollständige Referenz

## Backup: Pflichtschritt vor jedem Update

> **KRITISCH:** Shopware erstellt kein automatisches Backup. Ohne Backup kein sicheres Rollback möglich.

### Was muss gesichert werden?

| Komponente | Inhalt | Methode |
|---|---|---|
| Datenbank | Alle Shop-Daten | mysqldump / Hosting-Panel |
| public/media/ | Hochgeladene Bilder, Dokumente | rsync / Hosting-Backup |
| config/ | Konfigurationsdateien | rsync / Git |
| .env | Umgebungsvariablen | rsync (separat, nicht in Git!) |
| var/log/ | Logs (optional) | rsync |

### Nicht sichern müssen (regenerierbar)

| Verzeichnis | Grund |
|---|---|
| var/cache/ | Wird bei Update geleert |
| vendor/ | Via `composer install` wiederherstellbar |
| node_modules/ | Via `npm install` wiederherstellbar |

---

## Backup-Methoden

### Methode 1: Datenbank-Backup via mysqldump

```bash
# Vollständiges Backup
mysqldump -u db_user -p db_name > shopware-backup-$(date +%Y%m%d-%H%M%S).sql

# Mit Kompression (empfohlen bei großen Datenbanken)
mysqldump -u db_user -p db_name | gzip > shopware-backup-$(date +%Y%m%d).sql.gz

# Mit Single-Transaction (kein Table-Lock bei InnoDB)
mysqldump -u db_user -p --single-transaction db_name > shopware-backup.sql
```

### Methode 2: shopware-cli Dump (sauberere Alternative)

```bash
# Clean Dump (ohne Cart-Session-Daten, Logs)
shopware-cli project dump \
  --clean \
  --host localhost \
  --username db_user \
  --password db_pass \
  --output shopware-backup-$(date +%Y%m%d).sql \
  db_name

# Mit Anonymisierung (DSGVO für externe Staging-Umgebungen)
shopware-cli project dump \
  --clean \
  --anonymize \
  --host localhost \
  --username db_user \
  --password db_pass \
  --output shopware-backup-anon.sql \
  db_name
```

### Methode 3: Hosting-Panel (für Shared Hosting)
Die meisten Hosting-Anbieter bieten in ihrem Control Panel (cPanel, Plesk, Hetzner) automatische oder manuelle Backup-Funktionen:
- cPanel: Backups > Full Backup / Partial Backup
- Plesk: Websites & Domains > Backup Manager
- Hetzner: Server Backups (automatisch, kostenpflichtig)

### Methode 4: Dateien-Backup via rsync

```bash
# Gesamtes Shop-Verzeichnis sichern
rsync -avz --exclude='vendor/' --exclude='var/cache/' --exclude='node_modules/' \
  /pfad/zum/shop/ \
  /pfad/zum/backup/shopware-$(date +%Y%m%d)/

# Remote-Backup auf anderen Server
rsync -avz --exclude='vendor/' \
  /pfad/zum/shop/ \
  backup-user@backup-server:/backups/shopware/$(date +%Y%m%d)/
```

---

## Backup-Strategie für Updates

### Empfohlene Vorgehensweise

1. **3-2-1-Regel:**
   - 3 Kopien der Daten
   - 2 verschiedene Medien (lokal + Cloud/Remote)
   - 1 Kopie extern (anderer Standort)

2. **Zeitpunkt:**
   - Backup direkt vor dem Update (nicht Stunden vorher)
   - Shop in Wartungsmodus versetzen → Backup → Update

3. **Verifikation:**
   - Backup-Datei auf Integrität prüfen
   - Test-Wiederherstellung auf Staging-Umgebung

### Backup-Checkliste vor Update

- [ ] Datenbank gesichert (lokale Kopie)
- [ ] Datenbank-Backup auf externem Speicher vorhanden
- [ ] public/media/ gesichert
- [ ] config/ + .env gesichert
- [ ] Backup-Integrität geprüft (Dateigröße plausibel)
- [ ] Shopware-Version notiert (für Rollback)
- [ ] Composer-Version in composer.lock notiert

---

## Erweiterungen: Kompatibilitätsprüfung

### Vor dem Update prüfen

**Methode 1: Admin-Panel**
- Einstellungen > System > Shopware-Update
- Zeigt Kompatibilitätsstatus aller Erweiterungen

**Methode 2: Shopware Store**
- store.shopware.com > Mein Account > Lizenzen
- Kompatibilitätsfilter nach Ziel-Shopware-Version

**Methode 3: shopware-cli**
```bash
shopware-cli project upgrade-check
```

### Drei Kompatibilitätsstatus

| Status | Bedeutung | Aktion vor Update |
|---|---|---|
| Bereits kompatibel | Aktuelle Version läuft mit neuer SW-Version | Nichts tun |
| Mit neuer SW-Version kompatibel | Neue Extension-Version nach SW-Update verfügbar | Nach Update aktualisieren |
| Nicht kompatibel | Keine kompatible Version geplant | Deaktivieren/löschen VOR Update |

### Erweiterungen beim Major-Update (6.4→6.5 oder 6.5→6.6)

**ALLE Extensions müssen deaktiviert werden:**

1. **Theme auf Standard setzen:**
   Admin > Einstellungen > Design > Theme > Storefront Theme aktivieren

2. **Theme-Extension deaktivieren:**
   Admin > Erweiterungen > Meine Erweiterungen > Theme deaktivieren

3. **Alle weiteren Extensions deaktivieren:**
   Admin > Erweiterungen > Meine Erweiterungen > alle deaktivieren

4. **Update durchführen**

5. **Nach Update:**
   - Extensions im Store auf kompatible Versionen aktualisieren
   - Extensions wieder aktivieren
   - Theme neu aktivieren

---

## Systemvoraussetzungen vor dem Update prüfen

### Admin-Systemcheck
Admin > Einstellungen > System > Shopware-Update > Systemvoraussetzungen

Grüne Indikatoren = OK
Rote Indikatoren = Muss behoben werden

### Manuelle CLI-Überprüfung

```bash
# PHP-Version prüfen
php -v

# PHP-Extensions prüfen
php -m | grep -E 'curl|json|zip|gd|pdo|intl|mbstring|openssl|ctype|dom'

# MySQL/MariaDB-Version prüfen
mysql --version

# Node.js-Version prüfen
node --version

# Composer-Version prüfen
composer --version

# Freier Festplattenplatz
df -h /pfad/zum/shop
```

### Typische PHP-Extensions die Shopware benötigt

| Extension | Zweck |
|---|---|
| curl | HTTP-Anfragen |
| json | JSON-Verarbeitung |
| zip | Archiv-Handling |
| gd / imagick | Bildverarbeitung |
| pdo_mysql | Datenbank |
| intl | Internationalisierung |
| mbstring | Multi-Byte-Strings |
| openssl | SSL/TLS |
| ctype | Zeichentyp-Prüfungen |
| dom | DOM-Manipulation |
| simplexml | XML-Parsing |
| sodium | Verschlüsselung |
| xml | XML-Verarbeitung |
| xmlreader | XML-Streaming |
| xmlwriter | XML-Erstellung |

---

## Screenshots: Update-Prozess

![Admin Update Start](../assets/update-admin-start.png)
*Admin-Panel: Einstellungen > System > Shopware-Update — Systemvoraussetzungen prüfen*

![Admin Update Version](../assets/update-admin-version.png)
*Verfügbare Update-Versionen werden angezeigt*

![Erweiterungen deaktivieren](../assets/update-erweiterungen-deaktivieren.png)
*Erweiterungen-Kompatibilitätsstatus und Deaktivierungsoptionen*

![Admin Update Finish](../assets/update-admin-finish.png)
*Erfolgreicher Abschluss des Updates*

![Browser Changelog](../assets/update-browser-changelog.png)
*Browser-Installer: Download des Shopware-Installers aus dem Changelog*

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/update-guides/shopware-aktualisieren-updaten*
