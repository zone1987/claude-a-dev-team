---
name: sw-deptrac
description: >
  Architektur-/Schichten-Prüfung für Shopware-6-Plugins mit Deptrac: Layer definieren, erlaubte Abhängigkeiten,
  deptrac.yaml, Verstöße finden. Trigger: "Deptrac shopware", "deptrac.yaml", "Schichten plugin", "Layer dependency check",
  "architektur prüfung plugin". Shopware 6.7.
---

# Shopware 6 — Deptrac

Erzwingt Schichten-/Abhängigkeitsregeln (z.B. Core darf nicht auf Storefront zugreifen; Domänen entkoppelt).

```yaml
# deptrac.yaml
deptrac:
  paths: [./src]
  layers:
    - name: Core
      collectors: [{ type: directory, value: src/Core/.* }]
    - name: Storefront
      collectors: [{ type: directory, value: src/Storefront/.* }]
  ruleset:
    Storefront: [Core]
    Core: []        # Core darf NICHT auf Storefront
```

```bash
vendor/bin/deptrac analyse
```

Hält Plugin-interne Architektur sauber (Domänentrennung, keine Zyklen). Ergänzt PHPStan (`sw-phpstan`, Typen) und
ECS (`sw-ecs-cs-fixer`, Style). Im CI als Gate (`shopware-devops`).
