# Shopware 6 — Static analysis and linting

**One command covers all of it: `composer gate`.** It runs the fixers and then every
check, so nobody has to remember the list.

```
gate  =  gate:fix         →  gate:check
         ├─ rector:fix        ├─ phpstan
         └─ cs-fix            ├─ cs
                              ├─ rector
                              ├─ lint:scss
                              └─ test:unit
```

**`gate:fix` changes files. `gate:check` changes nothing and only reports.** That split is
the point: a tool that corrects and judges at the same time cannot fail — it repairs the
violation and reports success, and then nobody is checking anything.

## The matrix

| Subject | Tool | Check | Fix |
|---|---|---|---|
| PHP style | php-cs-fixer | `composer cs` | `composer cs-fix` |
| PHP types | PHPStan, level `max` | `composer phpstan` | by hand |
| PHP architecture | **phpat, run by PHPStan** | part of `composer phpstan` | by hand |
| PHP modernisation | Rector | `composer rector` | `composer rector:fix` |
| SCSS | Stylelint | `composer lint:scss` | `composer lint:scss-fix` |
| Admin JS | ESLint + Prettier | `npm --prefix …/administration run lint` | `lint:js:fix`, `lint:format:fix` |
| Storefront JS | ESLint + Prettier | `npm --prefix …/storefront run lint` | same |

**Not ECS.** Shopware's core uses ECS internally; a plugin follows the core's published
`.php-cs-fixer.dist.php` instead, because that is the file it can adopt directly.
→ [ECS-CS-FIXER.md](ECS-CS-FIXER.md)

**Not Deptrac.** Architecture rules run through **phpat**, as PHPStan rules: phpat needs
the type graph PHPStan builds anyway, so the check costs almost nothing and runs on every
`composer gate`. A separate Deptrac pass would build that graph a second time.
→ `shopware-testing` → `sw-testing-standard` → `STANDARD-ARCHITECTURE.md`

## Why the order is what it is

**Inside `gate:fix`: Rector first, then php-cs-fixer.** Rector rewrites code — it adds type
declarations, puts `#[Override]` on methods, inverts conditions into early returns. What it
produces is syntactically correct but unformatted. php-cs-fixer tidies that up. The other
way round is pointless: format first, then have it rewritten, and the formatting is gone.

**Inside `gate:check`: PHPStan first.** It finds the most real defects and takes the
longest. Running it first means a failure surfaces early, not after three faster checks
reported green.

**`cs` and `rector` run as dry runs.** They prove the fix pass was complete. If `gate:fix`
has just run and `gate:check` still finds something, one tool is producing output the
other wants to change — **oscillation**, which is resolved rather than ignored. The usual
cause is the DocBlock rules: eleven Rector rules and seven php-cs-fixer rules have to stay
disabled, and disabling them in only one tool makes the other delete the tags on every run.

**Proving stability — two runs must leave the same tree:**

```bash
ddev exec bash -c "cd /var/www/html/shopware/custom/static-plugins/{PluginName} && \
    find src tests -name '*.php' | sort | xargs shasum | shasum"
```

Run it before and after `composer gate`: the checksum has to be identical.

## What the gate does not contain, and why

| Not in the gate | Why |
|---|---|
| `test:integration` | needs a database and a kernel; too slow for every commit |
| `test:admin` (Jest) | needs an installed npm tree |
| End-to-end (Playwright) | needs a running shop and the browserless container |
| `infection` / `mutation:admin` | run last, when no task is open |
| `coverage:*` | pcov slows every run; the figure is measured deliberately, not in passing |

These run before the commit of a finished task, not on every intermediate state.

## The configuration files

Each lives in the plugin root, and each has a reference of its own:

| File | Reference |
|---|---|
| `phpstan.neon` | [PHPSTAN.md](PHPSTAN.md) — `level: max`, no `ignoreErrors` |
| `.php-cs-fixer.dist.php` | [ECS-CS-FIXER.md](ECS-CS-FIXER.md) — including the seven rules that must stay off |
| `rector.php` | [RECTOR.md](RECTOR.md) — including the twelve skip rules |
| `.stylelintrc.json` | `shopware-storefront` → `sw-theme` → `STOREFRONT-LINTING.md` |
| `eslint.config.js`, `.prettierrc.json` | `shopware-admin` → `sw-build` → `ADMIN-LINTING.md` |

Shopware-specific PHPStan rules: [PHPSTAN-SHOPWARE.md](PHPSTAN-SHOPWARE.md).

**In CI the gate is the gate** — the same command, not a reassembled list that drifts from
what runs locally.
