# Shopware 6 — Deptrac

Enforces layer and dependency rules (for example: Core must not access Storefront; domains stay decoupled).

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
    Core: []        # Core must NOT access Storefront
```

```bash
vendor/bin/deptrac analyse
```

Keeps the plugin-internal architecture clean (domain separation, no cycles). Complements PHPStan (`sw-phpstan`, types) and
ECS (`sw-ecs-cs-fixer`, style). Use it as a gate in CI (`shopware-devops`).
