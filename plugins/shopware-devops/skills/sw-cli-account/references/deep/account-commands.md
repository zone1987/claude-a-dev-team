# shopware-cli account — Vollständige Referenz

## account login

OIDC/OAuth2 Browser-basierter Login gegen Shopware Account.

```bash
shopware-cli account login
# → Öffnet Browser für OIDC-Flow
# → Token wird lokal gecached (~/.config/shopware-cli/ oder XDG_CONFIG_HOME)
```

Kein zusätzlicher Flag außer globalen (`--no-interaction`, `--verbose`).

Bei `--no-interaction`: Login schlägt fehl (benötigt Browser-Flow).
Für CI: `ACCOUNT_EMAIL` und `ACCOUNT_PASSWORD` Umgebungsvariablen setzen.

```bash
# CI-Login via Umgebungsvariablen
ACCOUNT_EMAIL=user@example.com ACCOUNT_PASSWORD=secret shopware-cli account login
```

## account logout

Lokalen Token-Cache invalidieren.

```bash
shopware-cli account logout
```

Keine Flags.

## account producer extension list

Alle eigenen Store-Extensions auflisten.

```bash
shopware-cli account producer extension list
shopware-cli account producer extension list --search "My"
```

| Flag | Beschreibung |
|------|--------------|
| `--search string` | Ergebnisse nach Name filtern |

**Ausgabe:**
- Extension-Name (technical)
- Anzeigename
- Status (aktiv/inaktiv)
- Aktuelle Version im Store

## account producer extension info pull

Store-Informationen aus Shopware Account in lokale Dateien ziehen.

```bash
shopware-cli account producer extension info pull path/to/MyPlugin
```

**Lädt herunter nach:**
- `.shopware-extension.yml` — Metadaten (Name, Beschreibungen, Kategorien, Einstellungen)
- `src/Resources/store/` — Store-Assets:
  - `icon.png` — Extension-Icon (256x256px)
  - `images/` — Store-Screenshots
  - `description_de.html`, `description_en.html` — Beschreibungen
  - `installation_manual_de.html`, `installation_manual_en.html` — Installationsanleitungen

Kein zusätzlicher Flag.

## account producer extension info push

Lokale Store-Infos aus `.shopware-extension.yml` und `src/Resources/store/` in Shopware Account hochladen.

```bash
shopware-cli account producer extension info push path/to/MyPlugin
# oder Zip-Datei
shopware-cli account producer extension info push MyPlugin-1.2.3.zip
```

**Aktualisiert:**
- Beschreibungen (alle Sprachen)
- Installationsanleitung
- Store-Screenshots
- Icon
- Kategorien
- Kompatibilitäts-Flags

Kein zusätzlicher Flag.

## account producer extension upload

Extension-Zip in Shopware Store hochladen und Code-Review triggern.

```bash
shopware-cli account producer extension upload MyPlugin-1.2.3.zip

# Ohne auf Code-Review warten
shopware-cli account producer extension upload MyPlugin-1.2.3.zip --skip-for-review-result
```

| Flag | Default | Beschreibung |
|------|---------|--------------|
| `--skip-for-review-result` | false | Nicht auf automatischen Code-Review warten (schnelleres CI) |

**Upload-Ablauf:**
1. Zip hochladen via Shopware Account API
2. Automatischen Code-Review triggern
3. (Standard) Auf Review-Ergebnis warten und ausgeben
4. Exit-Code != 0 wenn Code-Review Fehler meldet

**Code-Review prüft u.a.:**
- PHP-Syntax
- Verbotene Funktionen (`eval`, `exec`, etc.)
- Shopware-API-Nutzung
- Performance-Probleme
- Sicherheitsprobleme

---

## `.shopware-extension.yml` — Vollständiges Format

```yaml
store:
  # Store-Icon (256x256px PNG)
  icon: src/Resources/store/icon.png

  # Unterstützte Shopware-Sprachregionen
  localizations:
    - de_DE
    - en_GB

  # Store-Kategorien
  categories:
    - Storefront
    - Administration

  # Automatische Bugfix-Version-Kompatibilität
  automatic_bugfix_version_compatibility: true

  # Store-Texte pro Sprache
  info:
    de:
      name: "Mein Plugin"
      summary: "Kurze Beschreibung (max. 150 Zeichen)"
      description: "Lange Beschreibung im Markdown/HTML"
      installation_manual: "Installationsanleitung"
      highlights:
        - "Feature 1"
        - "Feature 2"
      features:
        - "Feature A"
      faq:
        - question: "Wie installiere ich das Plugin?"
          answer: "Über den Plugin Manager"
      tags:
        - "Shopware 6"
        - "Extension"
    en:
      name: "My Plugin"
      summary: "Short description"
      description: "Long description"
      installation_manual: "Installation instructions"

# Build-Konfiguration
build:
  # Dateien/Ordner vom Zip ausschließen
  zip:
    assets:
      enable: true
    pack:
      excludes:
        # Muster zum Ausschließen
        - "node_modules"
        - "src/Resources/app/*/node_modules"
        - ".git"
        - "*.test.*"
        - "phpunit.xml*"
        - "tests/"
```

---

## Typischer Store-Publishing-Workflow

```bash
# 1. Extension bauen und validieren
shopware-cli extension build path/to/MyPlugin
shopware-cli extension validate --full --store-compliance path/to/MyPlugin

# 2. Release-Zip erstellen
shopware-cli extension zip path/to/MyPlugin --use-git-tag-as-version --release

# 3. Store-Infos aktuell halten
shopware-cli account login
shopware-cli account producer extension info push path/to/MyPlugin

# 4. Extension hochladen
shopware-cli account producer extension upload MyPlugin-1.2.3.zip

# 5. Nach dem Upload: Status prüfen
shopware-cli account producer extension list --search MyPlugin
```

---

## CI-Pipeline für automatischen Store-Upload

```yaml
# GitHub Actions Beispiel
- name: Build and upload extension
  env:
    ACCOUNT_EMAIL: ${{ secrets.SHOPWARE_ACCOUNT_EMAIL }}
    ACCOUNT_PASSWORD: ${{ secrets.SHOPWARE_ACCOUNT_PASSWORD }}
  run: |
    shopware-cli account login
    shopware-cli extension build .
    shopware-cli extension validate --full --reporter github .
    shopware-cli extension zip . --use-git-tag-as-version --release
    ZIP=$(ls *.zip | head -1)
    shopware-cli account producer extension upload "$ZIP"
```
