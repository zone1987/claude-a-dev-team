# Contao 5.x — Update und Migration

Quellen:
- https://docs.contao.org/5.x/manual/de/migration/
- https://docs.contao.org/5.x/manual/de/installation/contao-aktualisieren/
- https://docs.contao.org/5.x/manual/de/faq/

---

## Semantic Versioning

Contao folgt dem Semantic Versioning:

| Typ | Beschreibung | Beispiel |
|-----|-------------|---------|
| **Major** | Umfassende Neuversion | 4 → 5 |
| **Minor** | Meilenstein mit neuen Funktionen | 5.6 → 5.7 |
| **Bugfix** | Wartungsupdate | 5.7.0 → 5.7.1 |

### Long-Term-Support (LTS)

LTS-Versionen erhalten:
- 3 Jahre Bugfix-Support
- 1 Jahr Sicherheits-Support

---

## Contao aktualisieren (Minor/Bugfix)

### Via Contao Manager

**Bugfix-Update:**
1. Contao Manager öffnen
2. „Pakete aktualisieren" klicken
3. Nach Abschluss: Datenbanktabellen prüfen (Installtool oder `contao:migrate`)

**Minor-Update** (z.B. 5.6 → 5.7):
1. Contao Manager öffnen
2. Beim Contao Manager-Bundle auf Zahnrad-Icon klicken
3. Gewünschte Version eintragen (z.B. `5.7.*`)
4. „Änderungen anwenden" klicken
5. Datenbankmigrationen ausführen

### Via Kommandozeile

```bash
# Bugfix-Update
composer update

# Minor-Update: erst composer.json anpassen
# "contao/manager-bundle": "5.7.*"
composer update

# Datenbankmigrationen ausführen
vendor/bin/contao-console contao:migrate
```

### Lokale Updates ohne Cloud (bei Speicherlimitationen beim Hoster)

1. Update lokal auf eigenem Computer durchführen
2. `vendor/`, `composer.lock` auf den Server synchronisieren
3. Datenbankmigrationen via CLI auf Server ausführen

### Nach jedem Update

Immer Datenbanktabellen synchronisieren:
```bash
php vendor/bin/contao-console contao:migrate
```

Template-Dateien in `templates/` prüfen — können sich bei Updates ändern!

---

## Migration Contao 3.5 → 4.x

### Allgemeines Prinzip

**Major-Versionen können nicht übersprungen werden!**

Beispiel: Von 3.2.10 muss zunächst auf 3.5.40 aktualisiert werden, bevor 4.13.x möglich ist.

### Schritt-für-Schritt

1. **Datenbank-Backup erstellen** (vor allen Änderungen!)
2. **Frische Contao-4-Installation** auf dem Server anlegen
3. **Dateien kopieren** (in die neue Installation):
   - `files/` → `files/`
   - `templates/` → `templates/`
   - `system/config/localconfig.php` → `system/config/`
4. **Webserver** auf den `public/`-Unterordner der neuen Installation ausrichten
5. **Datenbankmigrationen** ausführen:
   ```bash
   php vendor/bin/contao-console contao:migrate
   ```
6. **Erweiterungen** prüfen: Gibt es für Contao 4 aktualisierte Versionen?

### Templates prüfen

Bei jeder Major-Version-Migration besonders wichtig: Überschriebene Templates in `templates/` auf Kompatibilität prüfen.

---

## Migration Contao 4.13 → 5.x

### Versionsanforderungen

**composer.json** anpassen:

```json
{
    "require": {
        "contao/manager-bundle": "5.0.*"
    }
}
```

Caret-Notation für Minor-Updates erlauben:
```json
"contao/manager-bundle": "^5.0"
```

### Composer-Scripts aktualisieren

Alt (Contao 4):
```json
"scripts": {
    "post-install-cmd": [
        "Contao\\ManagerBundle\\Composer\\ScriptHandler::initializeApplication"
    ]
}
```

Neu (Contao 5):
```json
"scripts": {
    "post-install-cmd": [
        "@php vendor/bin/contao-setup"
    ]
}
```

### Verzeichnisstruktur anpassen

Der `web/`-Ordner muss zu `public/` umbenannt werden:
```bash
mv web public
```

**Composer.json** anpassen (falls vorhanden):
```json
{
    "extra": {
        "public-dir": "public"
    }
}
```

Document Root im Webserver auf `public/` setzen.

### Ordner-Verlagerungen

| Alt | Neu |
|-----|-----|
| `app/config/` | `config/` |
| `app/Resources/contao/` | `contao/` |
| `app/Resources/public/` | `public/` |
| `app/Resources/translations/` | `translations/` |

### Entfernte Konfigurationen

Folgende Konfigurationen aus `config.yaml` entfernen (in Contao 5 nicht mehr unterstützt):
- `contao.prepend_locale`
- `contao.url_suffix`
- `contao.legacy_routing`
- `contao.encryption_key`

### Interne Stylesheets exportieren

**In Contao 5 entfällt der interne CSS-Editor.** Bestehende Stylesheets müssen migriert werden:

1. Alle internen Stylesheets im Backend exportieren
2. Als externe `.css`-Dateien speichern
3. In Seitenlayouts als externe Stylesheets einbinden

### Templates migrieren

**Alle Inhaltselemente** sind in Contao 5 neu implementiert mit **Twig-Templates**. Alte HTML5-Templates greifen nicht mehr automatisch.

**Migrations-Schritte:**
1. Vorhandene PHP-Templates in `templates/` identifizieren
2. Entsprechende Twig-Äquivalente erstellen
3. In Seitenlayouts überprüfen

### Migration starten

```bash
vendor/bin/contao-console contao:migrate
```

---

## Häufige Migrationsprobleme

### Datenbank-Server nicht im Strict Mode

Contao empfiehlt den MySQL Strict Mode. Aktivierung:
```sql
SET GLOBAL sql_mode = 'TRADITIONAL';
```

Oder in `my.cnf`:
```ini
sql_mode = TRADITIONAL
```

### web/ zu public/ umbenennen (FAQ)

Wenn noch in Contao-Version mit `web/`:
1. Ordner umbenennen: `mv web public`
2. Composer-Eintrag anpassen oder entfernen
3. Document Root im Webserver neu setzen
4. `composer install` ausführen

### Backend-Pfad ändern

In `config/config.yaml`:
```yaml
contao:
    backend:
        route_prefix: '/admin'
```

Cache leeren:
```bash
php vendor/bin/contao-console cache:clear --env=prod --no-warmup
php vendor/bin/contao-console cache:warmup --env=prod
```

### Anwendungs-Cache erneuern

```bash
vendor/bin/contao-console cache:clear --no-warmup
vendor/bin/contao-console cache:warmup
```

---

## FAQ — Häufige Fragen

### Allgemein

**Administrator-Passwort vergessen?**
- Mehrere Admin-Flags in `tl_user` zurücksetzen, dann im Install-Tool neuen Admin anlegen
- Via CLI: `php vendor/bin/contao-console contao:user:create --admin`

**Mehrere Webseiten verwalten?**
- Multidomain-Betrieb: Mehrere Website-Startseiten in einer Installation
- Mehrsprachig: Separate Startseiten pro Sprache

**Kommerzielle Nutzung?**
- Ja! Die LGPL erlaubt kommerzielle Projekte

**Debug-Modus aktivieren?**
- Backend: Käfer-Icon klicken
- Oder: `APP_ENV=dev` in `.env.local`

**Weiße Seite beim Bearbeiten?**
- Häufig von Browser-Extensions verursacht (z.B. LanguageTool)
- Lösung: Inkognito-Modus testen

### Template

**Template-Variablen anzeigen?**
- Dokumentation: „Template-Daten anzeigen"

**TinyMCE konfigurieren?**
- Eigene `config.js` unter `contao/config/tinymce.js` anlegen

**CSS-Klasse zu Überschriften hinzufügen?**
- Über `_headline` Twig-Komponente (nicht bei alten PHP-Templates)

### Konfiguration

**Backend-Pfad ändern?**
- `route_prefix` in `config.yaml` + Cache leeren

**E-Mail über Formulare?**
- SMTP in `parameters.yaml` oder `.env.local` konfigurieren

**URL-Präfix für Sprachen?**
- Im Startpunkt: URL-Präfix eintragen (z.B. `de`)

**HTML-Suffix `.html` hinzufügen?**
- Im Startpunkt: URL-Suffix eintragen

### Dateiverwaltung

**Bilder nicht sichtbar im Frontend?**
- Bildverzeichnis als „Öffentlich" markieren
- Alte `.htaccess`-Dateien prüfen

### Theme

**SCSS-Änderungen werden nicht übernommen?**
- Scriptcache leeren: System → Systemwartung → Daten bereinigen

### Contao Manager

**Manager hängt/reagiert nicht?**
- Datei `contao-manager/task.json` löschen

**Manager aktualisieren?**
- Automatisch im Hintergrund; oder neue `.phar` per FTP hochladen

**`.phar`-Datei umbenennen?**
- Möglich; in `config.yaml` anpassen:
  ```yaml
  contao_manager:
      manager_path: dein-name.phar.php
  ```
  Dann Cache leeren.

**Spezifische Contao-Version installieren?**
- Im Contao Manager: Experten-Modus verwenden, Version manuell eingeben
