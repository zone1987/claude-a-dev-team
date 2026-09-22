# Shopware 6 — deprecation handling

Shopware announces breaking changes with `@deprecated tag:v6.x` notices and major feature
flags.

## Finding them: PHPStan, in the gate

**`phpstan/phpstan-deprecation-rules` is the only reliable mechanism.** It reports every
call to something marked `@deprecated` — at the line it stands on, on every
`composer gate`.

The alternatives do not suffice:

| Route | Why it is not enough |
|---|---|
| Symfony's deprecation helper in the tests | reports only what a test actually executes, and `SYMFONY_DEPRECATIONS_HELPER=weak` dampens it anyway |
| Reading Shopware's own `UPGRADE-*.md` | names the changes, not the places in your code |
| Noticing at update time | too late: by then it is a fatal in production |

The extension is registered by `phpstan/extension-installer`, so it needs no entry in
`phpstan.neon`. → `shopware-quality` → `sw-analysis` → `PHPSTAN.md`

For the data layer there is a second check:

```bash
ddev exec bin/console dal:validate
```

It validates the entity definitions against the schema and reports deprecated field types
and flags.

## Writing them down: `UPGRADE-<next>.md`

**One file per upcoming major version**, in the plugin root — `UPGRADE-6.8.md` while the
plugin runs on 6.7.

**Why not `DEPRECATIONS.md`:** the name says what has to be done, not merely what is
obsolete. It also matches what Shopware itself uses, so the file can point at its
counterpart:

```markdown
See also: https://github.com/shopware/shopware/blob/trunk/UPGRADE-6.8.md
```

### What goes in, per finding

1. **What is deprecated** — class, method, signature, fully qualified
2. **Where the plugin uses it** — file and line
3. **What replaces it** — the new call
4. **When it disappears** — the version from the `@deprecated` tag

```markdown
### `EntitySearchResult::sortByIdArray()`

`@deprecated tag:v6.8.0` — removed in 6.8.

**Used in:** `src/Core/Content/Product/Cms/MyResolver.php:100`

**Replacement:** … the concrete new call
```

Add a section for everything that carries **no** deprecation tag but is still pending —
administration components with no Meteor counterpart in the current version, for instance.

### When it is written

**As soon as a finding appears, not collected at the end.** The finding is in the gate, so
it is known; not writing it down means finding it again next time.

## What is not done

**No code for the next major version.** While the `conflict` block in `composer.json`
excludes it, that would be code the shop is not allowed to run — and the Rector set stays
on the released version for the same reason.
→ `shopware-quality` → `sw-analysis` → `RECTOR.md`

**`UPGRADE-<next>.md` describes what will have to be done. It is not an implementation.**

## Resolving them

- Use the recommended successor API; where one is offered, apply the Rector rule.
- Activate new behaviour for testing through `Feature::isActive('v6.x.0.0')`
  (`shopware-core` → `sw-plugin` → `FEATURE-FLAGS.md`).
- **Never pin a test to a deprecated path.** A test that asserts the old behaviour keeps
  the old behaviour alive.
- **Never rely on `@internal`.** That is also why a plugin carries its own `#[Package]`
  attribute rather than the core's.
  → `shopware-core` → `sw-plugin` → `PLUGIN-PACKAGE-ATTRIBUTE.md`

Version-specific list: [OVERVIEW.md](OVERVIEW.md) and Shopware's own `UPGRADE-6.x.md`.
