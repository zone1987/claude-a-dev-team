# The decisions behind this standard

Each of these was argued, and each is written down so it is not re-argued from scratch. A
decision that no longer holds gets replaced by a new one that says why — it is not quietly
reversed.

## PHPUnit belongs to the project, never to the plugin

`phpunit/phpunit` is **not** in the plugin's `require-dev`. Scripts call
`../../../vendor/bin/phpunit`.

A plugin that pins its own version pins a version that goes stale — one plugin here sat on
`^10.5` while the project ran 12.5. Worse, the two can disagree about what a test means.
The project's PHPUnit is the one the shop actually runs.

**Consequence:** Infection needs `phpUnit.customPath` pointing at the same path, because it
cannot find PHPUnit beside its own `vendor/bin`.

## Pest was evaluated twice and rejected twice

The argument for it is real: Pest unifies unit, integration, architecture and mutation
testing under one syntax, which is exactly what this standard assembles by hand.

Against it, three things:

- **The architecture rules run on phpat, through PHPStan**, and therefore share PHPStan's
  type resolution. Pest's own architecture tests do not; adopting them means trading a
  stronger tool for a weaker one.
- **Integration tests are built on Shopware's `TestBootstrapper` and
  `IntegrationTestBehaviour`**, both PHPUnit classes. Pest would wrap them, and every
  Shopware upgrade would mean checking whether the wrapper still fits.
- **Infection drives PHPUnit either way.** The syntax of the tests changes nothing there.

The gain would be nicer unit-test syntax at the price of two syntaxes in one codebase.
Shopware's own suite, the acceptance test suite and every reference plugin are PHPUnit.

**Revisit if** a plugin is ever extracted from the Shopware context entirely.

## Coverage reports are not committed; mutation baselines are

This looks inconsistent and is not.

**Coverage reports: ignored.** Reproducible in seconds, change wholesale on every run, and
make every diff unreadable. Nothing is lost by regenerating them.

**Mutation baselines: committed.** A mutation run costs hours. The figure's *history*
answers a question nothing else can — "we were at 96 %, why are we at 71 %?" is
unanswerable without the old run. That is worth a few kilobytes.

Committed: `docs/mutation/<date>/summary.json`, `infection.log`, and a `README.md` with the
table and the judgement on every survivor. Not committed: `infection.html`, which is large
and says nothing the log does not.

```gitignore
### IDE
.idea
.vscode

### Composer
composer.lock
**/vendor

### Node
package-lock.json
**/node_modules

### Built storefront assets — a release archive carries them, git does not.
### Build with: shopware-cli project storefront-build --only-extensions YourPlugin
src/Resources/app/storefront/dist/

### Tool caches and generated reports.
### Reproducible in seconds, and they change wholesale on every run.
var/
.php-cs-fixer.cache
.phpunit.cache
.phpunit.result.cache

### Jest coverage, same reasoning
src/Resources/app/*/coverage/

### Playwright output
tests/Acceptance/.env
tests/Acceptance/test-results/
tests/Acceptance/playwright-report/
tests/Acceptance/report.xml
tests/Acceptance/blob-report/
tests/Acceptance/.cache/

### Logs, except the mutation baselines below
*.log
!docs/mutation/**/*.log

### Mutation baselines ARE committed — a score costs hours and its history answers a
### question nothing else can. The verbose HTML report is not kept.
!docs/mutation/
docs/mutation/**/infection.html
```

**The line between them:** what is reproducible in seconds stays out; what costs hours and
serves as a comparison point goes in.

## Built assets are not committed either

`src/Resources/app/storefront/dist/` is a build artifact. What ships in a release archive
is built; what lives in git is source.

**The consequence has to be written down where someone will read it**, because it is easy
to get wrong: a release archive built without
`shopware-cli project storefront-build --only-extensions <Plugin>` carries no JavaScript at
all, and the plugin silently does nothing.

One plugin here had three stale files under `dist/`, two of them hash-named leftovers, and
the build had been **failing for months** over a missing `.js` in one import. Those stale
files were the only JavaScript it had been shipping. Committed build output hides a broken
build.

## Five phpunit configs, not one

Unit, integration, and three coverage variants. Plus a sixth for Infection, in
`build/infection/`.

A filtered run must never overwrite a full coverage report, and Infection passes
`--configuration` itself while looking only for a file literally named `phpunit.*` in the
directory it is pointed at. Giving it a directory of its own keeps the plugin's configs
untouched.

## Coverage thresholds are enforced in Jest, read in PHP

Jest fails the run below 100 %. PHPUnit's own threshold options are coarser, so the PHP
figure is read and acted on rather than enforced by a flag.

The asymmetry is practical, not principled. If PHPUnit gains a usable per-metric threshold,
use it.

## 100 % coverage, no exemptions

No `@codeCoverageIgnore` for "trivial" getters, no exemption for subscribers or structs.
Only `src/Resources/config` is excluded, because container configuration is executed at
boot and never by a test.

Every exemption is a judgement call about what is "important enough", and judgement calls
multiply. A rule with no exceptions needs no arbiter.

## Mutation testing is not in the gate

It takes minutes on a small plugin and hours on a large one. A gate slow enough to tempt
anyone into skipping it protects nothing.

It runs deliberately: after the test suite changes shape, before a release.

## phpat over Deptrac

phpat runs inside PHPStan and shares its type resolution. Deptrac parses independently,
knows less, and needs its own run, config and gate slot. The reference plugin migrated away
from it.

## Versions are pinned exactly

`"phpstan/phpstan": "2.2.8"`, not `"^2.2"`. A gate that passes today and fails tomorrow
because a patch release changed a rule is a gate nobody trusts. Upgrades are deliberate
acts with the diff read.

## `rector/type-perfect` is kept although abandoned

Composer warns about it. It is kept because the suggested replacement checks something
else. Revisit when a rule actually breaks, not because of the warning.

## Test names state rules

`testACartAtExactlyTheThresholdEarnsTheTier`, not `testCalculate`. The name is the
documentation that survives a refactoring, and a suite of rule-shaped names reads as the
specification of the class.

## The clean-up rule is absolute

**A test run leaves the shop as it found it.** One documented exception: cart rows, which
are session artifacts no clean-up can see and which Shopware removes daily itself.

Everything else is removed, and a report from the global teardown is treated as a defect in
the earlier levels rather than as the teardown doing its job.
→ [STANDARD-CLEANUP.md](STANDARD-CLEANUP.md)

## Git is the plugin owner's

No tooling and no assistant runs a git command that writes — not `commit`, not `add`, not
`branch`, not `rm --cached`. Work is left in the working tree; `git status` and `git diff`
is how the owner sees it.

This is stricter than it looks: `git rm --cached` to untrack a directory is a git write,
even though nothing is deleted from disk. Change the `.gitignore`, say what remains to be
done, and leave it.

## Read the source before deciding

`https://github.com/shopware/shopware/tree/v<VERSION>`, at the installed version.
→ [STANDARD-SOURCE-OF-TRUTH.md](STANDARD-SOURCE-OF-TRUTH.md)
