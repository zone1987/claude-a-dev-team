# Shopware 6 plugin — ground rules

These nine rules override everything else. They hold in **every** plugin, they are not negotiable, and they are not
"cleaned up later" — a violation that is noticed is corrected immediately.

These are the rules of *our own* plugins, not the Shopware core's. Core conventions live in
[CODING-GUIDELINES.md](CODING-GUIDELINES.md); the plugin process built on top of these rules is in
[PLUGIN-WORKFLOW.md](PLUGIN-WORKFLOW.md).

Target environment: Shopware 6.7.x, PHP 8.3, DDEV, `shopware-cli`.

## Contents

- [1. Everything is English, except the README](#1-everything-is-english-except-the-readme)
- [2. No prose comments](#2-no-prose-comments)
- [3. No copyright headers in classes](#3-no-copyright-headers-in-classes)
- [4. Git: commit in a feature branch, never push, ask first](#4-git-commit-in-a-feature-branch-never-push-ask-first)
- [5. Foreign code is not touched](#5-foreign-code-is-not-touched)
- [6. Build only with shopware-cli](#6-build-only-with-shopware-cli)
- [7. Everything runs in DDEV](#7-everything-runs-in-ddev)
- [8. Credentials live in .env.local](#8-credentials-live-in-envlocal)
- [9. One task at a time](#9-one-task-at-a-time)
- [Placeholders](#placeholders)

---

## 1. Everything is English, except the README

| What | Language |
|---|---|
| Variables, parameters, functions, classes, types | **English** |
| File and directory names | **English** |
| Comments, DocBlocks | **English** |
| Test names (PHPUnit, Jest, Playwright) | **English** |
| Commit messages, branch names | **English** |
| ADRs, `CLAUDE.md`, `CONTEXT.md`, `UPGRADE-*.md`, `SECURITY.md`, `CHANGELOG.md` | **English** |
| `README.md` | **German** |
| Wiki | **German** |
| Admin snippets `de-DE.json` | German content, **English keys** |
| Conversation in the terminal | **German** |

**Why:** a German comment sits exactly where the reasoning for a decision sits. Whoever reads the code later without
German loses not a word but the knowledge behind it. `README.md` is the exception because it addresses the shop
operator, not the developer — and that operator is German-speaking here.

An ADR records this, e.g. `adr/YYYY-MM-DD-everything-is-written-in-english.md`.

---

## 2. No prose comments

Multi-line explanatory blocks telling background, trade-offs or decision history do not belong in the code — not even
when they are factually correct.

**Still allowed:**

| What | Example |
|---|---|
| Short one-liners for a non-obvious constraint | `// size excludes itself` |
| Terse doc comments on public API | `/** Returns the packet body. */` |
| `TODO`/`FIXME` with a concrete reference | `// TODO: replace once P-12 lands` |
| Directives a tool demands | `// eslint-disable-next-line …` |

**Where the knowledge goes instead:**

1. into an **ADR**, if it is a decision
2. into **`CONTEXT.md`**, if it is an interim state or a trap
3. into a **test name**, if it is a rule

A test named `it rejects a path containing ..` documents the rule better than ten lines of prose about it — and it
breaks when someone violates the rule. A comment never breaks.

---

## 3. No copyright headers in classes

No block of this kind, in any file:

```php
<?php
/*
 * @author <VENDOR-LABEL>
 * @copyright 2024 © <VENDOR-LABEL>
 * @license proprietary
 */
```

After removal the file starts directly with:

```php
<?php declare(strict_types=1);
```

**Why:** the statement already sits where it is maintained — in `LICENSE` and in `composer.json`. In the class it is a
copy nobody updates. Years go stale, a changed licence is corrected in one place and not in a hundred others, the
company name stays put when a project changes owner. A statement that sits in a hundred places and is maintained in
one is worse than none — it asserts something false with authority.

On top of that: the block displaces the first screenful of every file, where the namespace and the imports would
otherwise stand.

**Exception:** foreign code we include instead of writing. There the author's header stays untouched.

The rule is enforced by php-cs-fixer.

---

## 4. Git: commit in a feature branch, never push, ask first

**Three rules, in this order.**

**1. Before a project's first commit, ask.** At the start of the work, settle whether committing is wanted at all.
**A "no" holds for the whole project** — from then on the work stays in the working tree, and `git status` and
`git diff` are how the maintainer sees it. The question is asked once, not before every commit.

**2. Commits go into a feature branch and nowhere else.** Where committing has been agreed, it happens in the feature
branch only. Nothing is committed in `main`, `master`, `trunk` or a release branch — branch first, or leave the work
uncommitted and say so.

**3. Never `git push`.** Not once, not "just this branch", not after a green gate. The maintainer pushes after their
own review.

**Why the push is the absolute rule:** it is the only step here that can no longer be quietly taken back once someone
else has fetched the state. Everything else — commit, rebase, reset — stays locally repairable.

Within these rules the ordinary writing commands are available: `add`, `commit`, `branch`, `rm --cached`. Outside
them nothing is written.

---

## 5. Foreign code is not touched

| Place | Rule |
|---|---|
| `custom/static-plugins/<own plugin>` | this is where the work happens |
| `custom/static-plugins/<foreign plugin>` | read only |
| `custom/plugins/` | do not touch |
| `vendor/` | **never** touch |
| `.gitlab-ci.yml` | do not touch unless explicitly instructed |

A foreign plugin may be **read as a model**. Read, not changed.

---

## 6. Build only with `shopware-cli`

```bash
ddev exec shopware-cli project admin-build      --only-extensions <PLUGIN-NAME>
ddev exec shopware-cli project storefront-build --only-extensions <PLUGIN-NAME>
```

Never a `bin/` script, never a hand-rolled webpack command. `--only-extensions` limits the build to the one plugin;
without that switch every installed extension is rebuilt, which costs minutes and touches foreign artefacts.

---

## 7. Everything runs in DDEV

Every command runs in the container, not on the host:

```bash
ddev exec bash -c "cd /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME> && composer gate"
```

**Sole exception:** `composer changelog`. `git cliff` reads the git history, and the repository sits on the host.

---

## 8. Credentials live in `.env.local`

Admin credentials and API keys live in `shopware/.env.local`:

```
SHOPWARE_ADMIN_USERNAME=…
SHOPWARE_ADMIN_PASSWORD=…
SHOPWARE_ACCESS_KEY_ID=…
SHOPWARE_SECRET_ACCESS_KEY=…
```

They are read from there — not asked of the user, not guessed from the database, **never printed to the console**, and
never written into commits, `CONTEXT.md` or any other documentation.

---

## 9. One task at a time

Done means: committed, with a green gate. Not "the code runs".

The full ordering inside a task is in [PLUGIN-WORKFLOW.md](PLUGIN-WORKFLOW.md).

---

## Placeholders

Examples use placeholders in angle brackets. **They must be replaced with the real values when a plugin is created** —
a file still containing `<PLUGIN-NAME>` has been copied, not adopted.

| Placeholder | Meaning | Example |
|---|---|---|
| `<PLUGIN-NAME>` | plugin and directory name, PascalCase | `AcmeProductBadge` |
| `<PLUGIN-NAMESPACE>` | PHP namespace, usually the same as `<PLUGIN-NAME>` | `AcmeProductBadge` |
| `<PLUGIN-VENDOR>` | composer vendor, lower case | `acme` |
| `<PACKAGE-NAME>` | full composer name | `acme/product-badge` |
| `<NPM-NAME>` | npm name, kebab-case | `acme-product-badge` |
| `<TABLE-PREFIX>` | database table prefix | `acme_` |
| `<LOG-CHANNEL>` | monolog channel name, snake_case | `acme_product_badge` |
| `<COMPONENT-PREFIX>` | admin component prefix, kebab-case | `acme-product-badge` |
| `<VENDOR-LABEL>` | company name for `LICENSE` and `composer.json` | `Acme GmbH` |
| `<SHOPWARE-MINOR>` | Shopware minor version the plugin targets | `6.7` |
| `<SHOPWARE-NEXT>` | the next major version | `6.8` |
| `<TEST-PREFIX>` | prefix of all E2E test data | `Test-ACME` |
| `<PLUGIN-NAME-CAMEL>` | plugin name as lowerCamelCase, for the monolog handler | `acmeProductBadge` |
| `<VERSION>` | plugin version | `4.1.0` |
| `<VENDOR-HOMEPAGE>` | vendor website | `https://www.example.de` |
| `<YEAR-FROM>` / `<YEAR-TO>` | copyright span; end year = current year | `2021` / `2026` |
| `<SECURITY-EMAIL>` | email for security reports | `security@example.de` |
| `<Area>` | area in the package attribute | `Core`, `Storefront`, `Framework` |
| `<Domain>` | domain directory under `Core/Content/` | `ProductBadge` |
| `<datum>` | date of a mutation run, `YYYY-MM-DD` | `2026-09-22` |
| `<titel>` | ADR title, kebab-case | `test-strategy` |

The running example is `AcmeProductBadge` (`acme/product-badge`): a plugin that inserts notice tiles into a product
listing. Where an example needs a class, field or table name, it comes from there — and is replaced like any other
placeholder.
