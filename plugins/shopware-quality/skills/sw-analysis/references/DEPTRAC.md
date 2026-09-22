# Shopware 6 — Deptrac (superseded)

> **Architecture rules run through phpat, not Deptrac.** phpat executes inside PHPStan and
> shares its type resolution, so the check costs almost nothing and runs on every
> `composer gate`. Deptrac parses independently, knows less, and needs its own run, its own
> configuration and its own place in the gate.
>
> → `shopware-testing` → `sw-testing-standard` → `STANDARD-ARCHITECTURE.md`
>
> What follows describes Deptrac for reading projects that still use it. **Do not set it up
> in a new plugin.**

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
