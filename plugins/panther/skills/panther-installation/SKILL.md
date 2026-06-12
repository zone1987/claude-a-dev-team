---
name: panther-installation
description: >
  Symfony Panther installieren: composer require, WebDriver-Installation (BDI/ChromeDriver/
  GeckoDriver/Paketmanager), PHPUnit-Extension in phpunit.xml.dist registrieren, Anforderungen,
  Docker-Setup, Umgebungsvariablen fuer CI.
  Install Panther: composer, WebDriver setup, PHPUnit extension, requirements, Docker, CI env vars.
  Trigger: "panther installieren", "panther install", "panther setup", "chromedriver installieren",
  "geckodriver install", "bdi detect drivers", "panther phpunit extension", "panther docker",
  "panther ci setup", "panther anforderungen", "panther requirements", "dbrekelmans bdi",
  "panther github actions", "panther gitlab ci".
---

# Symfony Panther — Installation

```bash
composer require --dev symfony/panther
vendor/bin/bdi detect drivers   # empfohlen: automatische Treiber-Erkennung
```

## PHPUnit-Extension (Pflicht fur volle Funktionalitat)

```xml
<!-- phpunit.dist.xml (PHPUnit 10+) oder phpunit.xml.dist (alt) -->
<extensions>
    <bootstrap class="Symfony\Component\Panther\ServerExtension"/>
</extensions>
```

## Umgebungsvariablen (Kurzliste)

| Variable                   | Beschreibung                              | Default     |
|----------------------------|-------------------------------------------|-------------|
| `PANTHER_NO_HEADLESS`      | Browser sichtbar machen                   | —           |
| `PANTHER_WEB_SERVER_PORT`  | Port des integrierten PHP-Servers         | `9080`      |
| `PANTHER_ERROR_SCREENSHOT_DIR` | Screenshot-Pfad bei Testfehlern       | —           |
| `PANTHER_NO_SANDBOX`       | Sandbox deaktivieren (Docker/CI)          | —           |

## Vertiefung

- [references/deep/installation.md](references/deep/installation.md) — Vollstandige Treiber-Optionen, alle Env-Vars, Docker, GitHub Actions, GitLab CI, SSL
