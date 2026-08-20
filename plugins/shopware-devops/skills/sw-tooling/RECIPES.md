# Symfony Flex Recipes für Shopware

Recipes automatisieren die Konfiguration beim `composer require`. Das offizielle
Shopware-Flex-Repository ergänzt den Symfony-Standard-Server um Shopware-spezifische
Packages.

```json
// composer.json
"extra": {
    "symfony": {
        "endpoint": ["https://raw.githubusercontent.com/shopware/recipes/flex/main/index.json"]
    }
}
```

```bash
composer require shopware/core          # installiert + wendet Recipe an
composer recipes                        # alle angewandten Recipes zeigen
composer recipes:update shopware/core   # Recipe re-applyen (nach Update)
```

## Manifest-Keys (Kurzübersicht)

| Key | Zweck |
|-----|-------|
| `copy-from-recipe` | Dateien aus Recipe-Dir ins Projekt kopieren |
| `bundles` | Bundles in `config/bundles.php` registrieren |
| `env` | `.env`-Einträge hinzufügen (`%generate(secret)%`) |
| `gitignore` | `.gitignore`-Zeilen anhängen |
| `container` | Container-Parameter / `env(...)`-Defaults setzen |
| `docker-compose` | Services in `docker-compose.yml` injizieren |
| `makefile` | Makefile-Targets einfügen |
| `aliases` | `composer require`-Kurzaliase (`paas`, `fastly`) |
| `conflict` | Inkompatible Paket-Versionen deklarieren |
| `composer-scripts` | `composer.json`-Scripts registrieren |

## Vertiefung

- [RECIPES-MANIFEST.md](RECIPES-MANIFEST.md) — Alle Keys mit Vollbeispielen und Shopware-Besonderheiten
- [RECIPES-PACKAGES.md](RECIPES-PACKAGES.md) — Alle verfügbaren Recipe-Packages mit Versionen
