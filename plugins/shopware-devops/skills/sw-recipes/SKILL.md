---
name: sw-recipes
description: >
  Symfony Flex Recipes für Shopware — Repository-Struktur, manifest.json-Format
  (alle Keys), wie Recipes genutzt und erstellt werden, verfügbare Shopware-Packages.
  Trigger: "shopware recipes", "symfony flex shopware", "recipe manifest.json",
  "flex endpoint shopware", "composer recipes", "shopware/core recipe",
  "shopware/paas-meta recipe", "recipe erstellen", "flex recipe keys".
---

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

- [references/deep/recipes-manifest.md](references/deep/recipes-manifest.md) — Alle Keys mit Vollbeispielen und Shopware-Besonderheiten
- [references/deep/recipes-packages.md](references/deep/recipes-packages.md) — Alle verfügbaren Recipe-Packages mit Versionen
