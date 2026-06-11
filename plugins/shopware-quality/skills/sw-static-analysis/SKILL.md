---
name: sw-static-analysis
description: >
  Static-Analysis & Lint-Pipeline für Shopware-6-Plugins: Überblick ECS/PHP-CS-Fixer, PHPStan, Deptrac, Rector, ESLint,
  Stylelint, ludtwig — welche Befehle, wann. Trigger: "Static Analysis shopware", "lint plugin", "composer phpstan ecs",
  "Qualitätsprüfung shopware", "welche checks plugin", "CI checks shopware". Shopware 6.7.
---

# Shopware 6 — Static Analysis & Lint

Lint-/Analyse-Matrix (aus `AGENTS.md`/Core):

| Dateityp | Check | Fix |
|---|---|---|
| PHP (Style) | `composer ecs` | `composer ecs-fix` |
| PHP (Typen) | `composer phpstan` | manuell |
| PHP (Architektur) | Deptrac | manuell (`sw-deptrac`) |
| PHP (Upgrade/Codemod) | Rector | `rector process` (`sw-rector`) |
| JS/TS/Vue (Admin) | `composer eslint:admin` | `:fix` |
| JS/TS (Storefront) | `composer eslint:storefront` | `:fix` |
| SCSS | `composer stylelint` | `:fix` |
| Twig (Storefront) | `composer ludtwig:storefront` | `:fix` |

Im Plugin eigene Configs ablegen (`.php-cs-fixer`/ECS, `phpstan.neon`, `deptrac.yaml`, `rector.php`). Shopware-spezifische
PHPStan-Regeln: `sw-phpstan-shopware`. Detail je Tool: `sw-ecs-cs-fixer`, `sw-phpstan`, `sw-deptrac`, `sw-rector`.
Im CI als Gate ausführen (`shopware-devops`).
