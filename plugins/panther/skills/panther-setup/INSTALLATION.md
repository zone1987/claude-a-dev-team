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

- [INSTALLATION-DETAIL.md](INSTALLATION-DETAIL.md) — Vollstandige Treiber-Optionen, alle Env-Vars, Docker, GitHub Actions, GitLab CI, SSL
