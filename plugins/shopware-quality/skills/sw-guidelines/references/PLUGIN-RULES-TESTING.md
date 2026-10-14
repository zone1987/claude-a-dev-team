# Plugin rules: Testing

## Contents

- [test-strategy: Every test level answers its own question, coverage is 100 percent, and one gate command decides whether work is finished](#test-strategy-every-test-level-answers-its-own-question-coverage-is-100-percent-and-one-gate-command-decides-whether-work-is-finished)
- [coverage-must-be-honest: A coverage number is only valid when it is measured, asserted and free of faked branches](#coverage-must-be-honest-a-coverage-number-is-only-valid-when-it-is-measured-asserted-and-free-of-faked-branches)
- [a-failing-test-is-classified-first: A failing test is classified as code, expectation, setup or environment before anything is changed](#a-failing-test-is-classified-first-a-failing-test-is-classified-as-code-expectation-setup-or-environment-before-anything-is-changed)
- [a-test-run-leaves-the-shop-unchanged: No test leaves a record that outlives it, and cleanup is verified by counting](#a-test-run-leaves-the-shop-unchanged-no-test-leaves-a-record-that-outlives-it-and-cleanup-is-verified-by-counting)
- [an-end-to-end-test-does-what-a-person-does: An end-to-end test does what a person does and never what a script could do instead](#an-end-to-end-test-does-what-a-person-does-an-end-to-end-test-does-what-a-person-does-and-never-what-a-script-could-do-instead)
- [end-to-end-tests-run-against-browserless: End-to-end tests connect to a browserless container and never install a browser](#end-to-end-tests-run-against-browserless-end-to-end-tests-connect-to-a-browserless-container-and-never-install-a-browser)
- [mutation-testing-comes-last: Mutation testing runs as the very last step on a stable suite, with every surviving mutant assessed](#mutation-testing-comes-last-mutation-testing-runs-as-the-very-last-step-on-a-stable-suite-with-every-surviving-mutant-assessed)
- [administration-tests-with-jest: The administration has its own pinned Jest setup, and every interactive element gets a test](#administration-tests-with-jest-the-administration-has-its-own-pinned-jest-setup-and-every-interactive-element-gets-a-test)
- [pest-is-rejected: Tests are written in PHPUnit and Pest is not adopted](#pest-is-rejected-tests-are-written-in-phpunit-and-pest-is-not-adopted)
- [five-phpunit-configs-not-one: The plugin carries five phpunit configurations and a sixth one for Infection in its own directory](#five-phpunit-configs-not-one-the-plugin-carries-five-phpunit-configurations-and-a-sixth-one-for-infection-in-its-own-directory)
- [coverage-thresholds-are-enforced-in-jest-and-read-in-php: Jest enforces the 100 percent threshold, the PHP figure is read and acted on](#coverage-thresholds-are-enforced-in-jest-and-read-in-php-jest-enforces-the-100-percent-threshold-the-php-figure-is-read-and-acted-on)
- [phpat-over-deptrac: Architecture rules run on phpat inside PHPStan and not on Deptrac](#phpat-over-deptrac-architecture-rules-run-on-phpat-inside-phpstan-and-not-on-deptrac)
- [rector-type-perfect-is-kept-although-abandoned: rector/type-perfect is kept although Composer reports it as abandoned](#rector-type-perfect-is-kept-although-abandoned-rectortype-perfect-is-kept-although-composer-reports-it-as-abandoned)
- [coverage-reports-are-ignored-and-mutation-baselines-are-committed: Coverage reports stay out of git and mutation baselines go in](#coverage-reports-are-ignored-and-mutation-baselines-are-committed-coverage-reports-stay-out-of-git-and-mutation-baselines-go-in)

## test-strategy: Every test level answers its own question, coverage is 100 percent, and one gate command decides whether work is finished

**Area:** testing **Status:** accepted

### Context

A plugin has logic in PHP, often logic in JavaScript, and integrations with the core. Each layer needs its own test strategy, and all of them must reach full coverage. The order of the checks must be fixed.

Typical situations that make the full standard necessary:

- A plugin that talks to an ERP must demonstrably work and must not merely be assumed to work. A coverage number is easy to reach with tests that assert nothing or with branches that never run.
- A plugin that is small, but deletes files and writes to the system configuration, has real consequences when it fails.
- A plugin that calculates prices which end up on invoices produces money, not cosmetics, when it is wrong. A wrong surcharge is a financial error.
- A plugin that arrives with no `tests/` directory, no PHPUnit, no PHPStan and no gate, and runs in several live shops on pages a shop earns its money on, needs the tooling before anything else. Defects such as a pagination fault that made products disappear, a recursive mode that never worked and a placeholder product that broke other plugins are arithmetic or wiring, which is exactly what a test suite is for.
- A plugin that touches the cart produces a wrong price when it fails, and the shopper pays it. A starting suite that rebuilds a template's arithmetic in PHP with `#[CoversNothing]` and asserts that its own reimplementation behaves proves nothing, because every calculation that matters lives in a Twig template where no PHP test can reach it.
- A plugin with a stale test setup (a `phpunit.xml` naming a suite for which no directory exists, Jest without a coverage threshold, Playwright specs that cannot run for lack of configuration, a gate made of ECS, Psalm and Rector) has to be brought up to the standard.
- The binding test standard also applies to small plugins. A plugin with three production files hooks into the timing of the core: it waits for a modal that is created asynchronously, decorates it, and must do the same on the second opening as on the first. Errors there arise during the course of events and not in the final state, so a check that only looks at the result does not see them. The temptation to leave out levels at that size is large, and it does not hold.
- A plugin with a user interface of its own (for example a configuration page in the administration) needs the end-to-end level for that interface.

Static analysis: PHPStan and Psalm overlap almost entirely. Shopware itself uses PHPStan and ships an extension that understands DAL specifics (`Criteria`, entity definitions, repository return types). No equivalent exists for Psalm. Running both means two baselines, two rule sets, contradictory generics reports and doubled gate runtime. Psalm's distinguishing feature, taint analysis, targets web input, while a plugin whose exposure is provider APIs is better served by error classification and webhook signature verification.

End-to-end: when the subject under test is mostly database state (which supplier was chosen, how groups were cut, whether a cost snapshot was frozen), a browser cannot observe it directly. But the customer-facing path (mixed cart, checkout, order confirmation, split shipment communication) is exactly what a browser test is for, and it is what breaks when a theme or template changes.

A reference plugin exists for what a plugin should look like: test-first on the domain, 100 % coverage with `#[CoversClass]` on every test, mutation testing to check the assertions rather than the line count, Playwright for what the shopper actually sees.

### Decision

#### Levels

Every level exists, and each answers a question the others cannot.

| Level | Tool | Question | Threshold | Content |
|---|---|---|---|---|
| PHPUnit unit | PHPUnit without a kernel, `tests/Unit` mirrors `src` | Does the logic hold without a kernel? Does the arithmetic hold? | Part of the 100 % | Pure, small classes, DTOs, services in isolation, cleaners, synchronizers, subscribers, handlers, tasks, domain logic test-first (sourcing, landed cost, availability, state machines, `Money` arithmetic) |
| PHPUnit integration | PHPUnit with a kernel (`TestBootstrapper` or `IntegrationTestBehaviour`, which resets the database) | Does it behave against a real kernel and a real database, with a faked external client where one exists? | Part of the same 100 % | Entity, DAL, event listeners, logic with dependencies, interplay with `SystemConfigService`, Store API and Admin API routes, file tests in a temporary directory and never in the real `var/log` |
| Architecture | phpat via PHPStan | Do dependencies and the folder structure hold? Do they point the right way? | Every rule green | Layer separation, boundaries, circular references. Typical rules: no dependency on other plugins, the framework layer depends on nothing else in the plugin, no internal core `Package` class in production code, no `Doctrine\DBAL` in production code |
| Jest (administration) | Jest | Does the administration behave? | 100 %, enforced by threshold | Vue components, forms, API calls |
| Jest (storefront) | Jest | Does the JavaScript behave (live price, visibility, validation, plugins, tracking, banner logic)? | 100 %, enforced by threshold | Storefront JavaScript plugins |
| Playwright end-to-end | Playwright against browserless | Does a person see and do the right thing? | Every flow the plugin touches | Administration configuration, storefront behavior, as a shopper or merchant would do it |
| Accessibility | axe inside the end-to-end suite | Does the user interface meet accessibility requirements? | No violation | Added where the plugin ships a dialog or other interface that must satisfy the BFSG |
| Contract tests | Against the external provider's test account | Does the real API still answer as recorded? | On request, every endpoint used | Only for plugins with an external API |
| Static analysis | PHPStan `max` | Is the code type safe? | Zero errors | |
| Style | php-cs-fixer | Is the style uniform? | Zero deviations | |
| Refactoring | Rector | Is the code current? | Dry run clean | |
| Mutation | Infection for PHP, Stryker for JavaScript bundles | Would a test notice a wrong line? | Every survivor documented, as close to 100 % as honest tests come | Runs last |

A level for which there is no subject is not written. A storefront that ships no JavaScript, only SCSS and Twig templates, has no storefront Jest setup. A test setup without a subject is not written, and the storefront is covered end to end instead.

An administration-only level can be omitted the same way where the plugin has no administration code.

#### Scenario layers for plugins with external providers and checkout flows

- **Unit:** domain logic test-first, no database, no container.
- **Integration (PHPUnit, extensive):** against the real DAL and a mock provider. This layer carries the weight of scenarios such as a mixed cart resulting in exactly one Shopware order with several fulfillment groups: cart composition, sourcing plan, fulfillment group formation, supplier order creation, idempotency, snapshot immutability, partial shipment and tracking aggregation, plus the Store API and Admin API routes.
- **End-to-end (Playwright, full):** the complete path in a real browser: mixed cart, checkout, order confirmation, storefront delivery information, and verification in the administration that supplier orders and fulfillment groups were created as expected.

External provider APIs are never contacted in any test layer. A mock provider or a sandbox only. Contract tests against a test account run on request only.

The same scenario appears at two layers, and that duplication is deliberate: the integration test asserts the data, the Playwright test asserts the experience. They fail for different reasons. Golden master tests for deterministic behavior (such as sourcing) live in the unit layer and run on every gate.

For a plugin whose arithmetic lives in a Twig template, the arithmetic must leave the template, because a template cannot be unit tested. That refactoring is a precondition for the strategy and not a side effect of it. A test that rebuilds the template's arithmetic is deleted, and its price matrices move into the test for the class that does the work (for example a threshold resolver), where they assert against the code that does the work. Playwright is the only level that covers the Twig template, and deliberately so: what matters about a template is what it renders, not how.

Where the plugin changes prices (for example discount tiers applied automatically), the PHPUnit integration level checks the cart processor against a real kernel: adding a product crosses a tier, removing it drops back, the discount line item carries the right amount and cannot be removed by the shopper.

> Earlier variant: one plugin first used a Playwright setup on `@shopware-ag/acceptance-test-suite` in a separate `playwright` DDEV service. That is superseded by running every end-to-end suite against browserless (see the browserless decision).

#### Coverage

- Coverage is 100 % of classes, methods and lines, measured by `composer coverage:all` for PHP (with a coverage driver such as pcov installed, reported to `var/coverage/`) and by Jest's `coverageThreshold` of 100 for statements, branches, functions and lines on every JavaScript side.
- The only exclusion in PHP is `src/Resources/config`, which is container configuration executed at boot. Where the core's own collections carry `@codeCoverageIgnore` because their generated methods belong to the framework, the plugin's DAL collections may carry it too. Nothing else is excluded.
- There is no `@codeCoverageIgnore` for "trivial" getters and no exemption for subscribers or structs. Container configuration is excluded only because it is executed at boot and never by a test. Every exemption is a judgement call about what is "important enough", and judgement calls multiply. A rule with no exceptions needs no arbiter.
- Dead code is deleted rather than covered. Reaching 100 % surfaces unreachable branches (for example an unreachable cache branch in a loader), which are removed and not propped up with a test.
- Every test names its subject with `#[CoversClass]`.
- PHP and JavaScript are tested against the same contract where both implement the same rules. JSON files under `tests/Fixtures/` are read by a PHPUnit test and a Jest spec, and both must produce the same result for every case. The configuration matrix covers every combination of option type, price type, selection mode, required flag and condition operator, and checks it on both sides.

#### Test data and tests first

- Fixtures originate exclusively from recorded real responses of the provider's test account, cleaned of credentials, tokens, hosts and personal data. No invented test data. Contract tests keep credentials in the local plugin configuration.
- A test run leaves the shop unchanged. Integration tests run in transactions, and end-to-end tests clean up after themselves.
- PHPUnit belongs to the shop project, never to the plugin. `phpunit/phpunit` is not in the plugin's `require-dev`. Every script calls `../../../vendor/bin/phpunit`. A version pinned in the plugin goes stale (one plugin sat on `^10.5` while the project ran 12.5), and the two can disagree about what a test means. The project's PHPUnit is the one the shop actually runs. Infection needs `phpUnit.customPath` pointing at the same path, because it cannot find PHPUnit beside its own `vendor/bin`.
- Test names state the rule, not the method. `testACartAtExactlyTheThresholdEarnsTheTier`, not `testCalculate`. The name is the documentation that survives a refactoring, and a suite of rule-shaped names reads as the specification of the class. `testAnOrderWithoutAnAddressIsNotSent`, `testTwoClosuresCostTwiceTheClosurePrice` and `testTheSecondPageContinuesWhereTheFirstStopped` are good names, `testCalculate` and `testPrepare` are not.
- Domain logic is written test-first: the test is written before the code and fails first.
- The implementation phase comes first with green static checks, and the test phase follows after the whole implementation. The toolchain, the rule checks of `CodingStyleTest` and the convention specs exist from the start. Done is measurable.
- Where rendering is concerned, behavior is measured over time with a `requestAnimationFrame` loop and not only by the end state.
- A test that cannot fail is not a test. Before a regression test is accepted, the defect is built back in once and the test is observed to fail.

#### The gate

- **The gate is one command and not a goal.** `composer gate` fixes first and then checks everything that is fast: Rector fix and php-cs-fixer fix, then PHPStan at level `max`, the style check, the Rector dry run, the linters for storefront and administration, the unit tests and, where it exists, Jest. Green means ready and mergeable, red means not finished, never "green except for".
- Two consecutive runs must leave the tree byte-identical.
- All checks run with `ddev exec -d <plugin directory> composer <script>`.
- **Coverage and mutation do not belong in the gate.** A gate slow enough to tempt anyone into skipping it protects nothing. Mutation takes minutes on a small plugin and hours on a large one. Coverage runs deliberately at the end of a task and before handover. Mutation runs when the suite shape has changed and as the last step, after the test suite changes shape and before a release.
- The tooling replaces older checkers: Psalm, ECS, phpcs and phpdocumentor are removed. The toolchain is PHPStan (with phpat, Strict Rules, Deprecation Rules, Symfony, PHPUnit and Type Perfect extensions), php-cs-fixer (`@PSR12`, `@Symfony`), Rector (the php83 set and Shopware 6.7) and Infection.
- Administration Jest runs through `npm run unit` and is part of the definition of done. It is not part of `composer gate` where that gate is PHP only, and the CI pipeline runs both.

> Earlier variant: one plugin's gate ran unit and integration tests and kept Playwright separate behind `composer test:e2e`, required before a release and whenever checkout, sourcing or storefront code changes, so that a red end-to-end run blocks a release and not every commit. Another earlier variant described the gate as checking "everything" including the end-to-end level.

#### Mutation testing

Mutation testing runs last, once everything else is green. Every surviving mutant is classified first. A missing test becomes a test that states the rule, dead or redundant code is removed, and an equivalent mutant is documented with its reason in the mutation baseline. Details are in the mutation decision.

#### CI portability

CI portability is a design constraint and not an afterthought. Every layer must run unchanged in a GitLab pipeline:

- No test invokes `ddev`. The composer scripts call `php` and `composer` directly. `ddev exec` is a local convenience placed in front of them and never a dependency of the test itself.
- No absolute paths and no hardcoded database URL. Configuration comes from environment variables (`DATABASE_URL`, `APP_ENV`, `APP_URL`).
- The pipeline provides Shopware through the official Docker image with the plugin mounted via a composer path repository, plus MySQL as a service. Playwright therefore has a real storefront and administration to drive.
- Pipeline stages are `lint`, `analyse`, `test`, `e2e` in that order. Fast stages fail first. The `e2e` stage runs on the main branch and on merge requests touching checkout, sourcing or storefront code.

### Consequences

- The tools are ready from the first day, and tests are written in a planned phase against stable code. The goal of 100 % brings unreachable branches and untestable designs to light, which is its purpose. Mutation results are only meaningful on a stable suite.
- Every place where an error can arise has its own level: single class, integrated, architectural, in the browser, end to end. A gap is visible.
- The gate is strict: red means the work is not finished, not that something is still to do.
- 100 % is the floor, not the goal. The number says every line ran, not that a test would fail if the line were wrong. Mutation testing measures that, which is why it is on the list.
- A test that reaches a line without asserting anything is worse than an uncovered line, because it reports safety that is not there. PHPStan catches the obvious cases (it rejected four tautological assertions while one suite was written).
- The test suite is often many times larger than the production code. That is the right ratio where the errors lie in the interplay with the timing of the core and not in reading one's own lines.
- The 100 percent threshold occasionally brings unreachable branches to light. The answer is to delete the branch, not to write a test that supports it.
- The axe check also reports theme defects. They are passed on and not silenced.
- The suite has more layers to maintain, and Playwright needs a running shop with fixtures. Test data setup becomes infrastructure and must be reproducible, otherwise the end-to-end layer decays into a flaky test nobody trusts. Playwright needing a running DDEV environment and a seeded shop is a heavier setup and is the price of testing a cart that changes prices.
- One static analyzer is enough to configure, correctness is verified precisely at the layer where it is observable, and the customer path is verified where it actually lives.

## coverage-must-be-honest: A coverage number is only valid when it is measured, asserted and free of faked branches

**Area:** testing **Status:** accepted

### Context

A coverage number says which lines were executed. It does not say whether what those lines do was checked. Full coverage is therefore compatible with unchecked behavior and with dead code. A hundred percent coverage is easy to reach when branches are faked and tests assert nothing.

### Decision

**100 percent is the lower bound, not the goal.** For the number to say anything at all, these rules apply:

- Required is 100 percent of classes, methods and lines.
- Only `src/Resources/config` is excluded. Everything else must be covered 100 percent.
- Dead branches are deleted, not tested. If an `if` never becomes true, the condition is an error.
- Every test has assertions. A test without `$this->assert*()` or `$this->expect*()` is not a test, even when it is green.
- Coverage is measured with `composer coverage:all`, over unit and integration tests together, on fully booted tests. The report lands in `var/coverage/all/`.
- A number is not asserted but measured. "100 percent" means a measurement run exists.
- **Every test class names its subject with `#[CoversClass]`.** A test that executes a class without naming it makes the report show checked code as unchecked, and the number then depends on the order of the test runs. Excluded are tests that do not check a single class but a rule across all files (for example `CodingStyleTest`, `BriefsAreCurrentTest` and `LayerTest`). They have no subject that could be named.
- **A tautological assertion is not a test.** It reaches the line and proves nothing.

```php
// Useless: the type is fixed statically, this can never fail.
static::assertInstanceOf(Plugin::class, new MyPlugin(true, __DIR__));

// Useful: this fails if someone removes the parent class.
static::assertTrue((new ReflectionClass(MyPlugin::class))->isSubclassOf(Plugin::class));
```

- **A coverage driver must be installed**, otherwise the run is green and measures nothing:

```bash
ddev exec php -m | grep -E 'pcov|xdebug'
```

- **Mutation tests are the touchstone of the number**, on both levels: Infection for PHP, Stryker for the storefront. Every survivor is classified, every unclassified one counts as unchecked. The baseline lies under `docs/mutation/`.

### Consequences

- The threshold brings unreachable branches, wrong assertions and untestable designs to light. That is not a disadvantage, it is the point.
- Coverage does not run in the gate but deliberately at the end of a task.
- Coverage is cheap to reach and worth little on its own. The expensive and useful part is the mutation tests.
- A survivor is not always a defect. Survivors that only concern the content of log contexts stay: a test on them would pin down the wording of an error message without securing behavior. The justification stands in the baseline.
- If the 100 percent threshold brings an unreachable branch to light, the branch is deleted, and no test is written that supports it.

## a-failing-test-is-classified-first: A failing test is classified as code, expectation, setup or environment before anything is changed

**Area:** testing **Status:** accepted

### Context

A failing test invites adjusting the assertion until it is green. The result is a suite that no longer says anything. Changing a test until it passes hides defects, and changing code until a wrong test passes creates new ones. Where code synchronizes orders and stock with another system, a bent test cannot be afforded, because the hidden defect becomes visible as wrong data in the other system.

The tests of a plugin often check against foreign behavior: the order in which the core fills its modal, the classes `FormCmsHandler` expects, the cleaning performed by the HtmlSanitizer. A reversed assertion writes a wrong assumption into the suite there.

### Decision

For every failing test this order applies, and the cause is named before anything is changed:

1. **Diagnosis.** What is the error? Timeout, wrong assertion, missing element or component, missing service, API error, a record left over from an earlier run, environment?
2. **Cause.** Is it the code (to be changed), the environment (to be checked) or the test itself (to be rewritten)? The classification is given with the evidence: what failed, then why, then the fix.
3. **Fix.** Only then is the problem addressed.

A failing test has exactly one of these causes:

| Cause | How to recognize it | What to do |
|---|---|---|
| The code is wrong (product defect) | the test names a rule the code breaks | change the code |
| The expectation is wrong (test defect) | the test asserts something the domain does not promise | change the expectation **after** it was refuted in the source text, and state the reason |
| The setup is wrong | the test does not reach what it wants to check | change the setup |
| The environment is wrong | container, browserless, build or test account misbehaves | fix the environment |

- **The second case is the dangerous one.** An assertion is only reversed once the source of the core has been read to confirm it was wrong. Not because it fails.
- A test is never weakened to become green: no assertion removed, no timeout raised, no case skipped or deleted.
- If it is unclear whether the test or the code is wrong, the rule the test name states decides, and the expected effect is determined from the requirement and not from the current behavior. A test is not adapted to fit the defect.
- **A test that cannot fail is not a test.** Before a regression test is accepted, the defect is built back in once and the test is observed to turn red.
- **When cleaning up, count, do not read.** A visual check in the administration misses exactly the one record that matters.
- **When the course of events is the issue, the course is measured.** A check on the end state misses every defect that at some point leads to the right state.
- The cause of every non-trivial error is stated in the commit message of the fix and, where it is a rule, in an ADR or in `CLAUDE.md`.

> Earlier variant: one earlier version said that if it is unclear whether test or code is wrong, the test is rewritten while the code is run for errors.

### Consequences

- Before every change to a test there is a classification. It costs a few minutes and prevents production code from being adapted to a wrong assumption.
- Red tests carry information, and errors are solved faster because nothing is guessed. A test that fails for the wrong reason does not become green by guessing.
- A mutant that cannot be killed is classified first: a hint of dead or redundant code is answered with a deletion, a missing rule with a test that states it, and an equivalent mutant with a documented reason.
- If two tools contradict each other, the setup is contradictory, and neither of the two is simply wrong. The answer is a narrowly bounded exception with a justification, not a loosened rule.

## a-test-run-leaves-the-shop-unchanged: No test leaves a record that outlives it, and cleanup is verified by counting

**Area:** testing **Status:** accepted

### Context

A test that creates data or files and does not clean up contaminates the following tests and runs. Or it runs twice in a row and breaks the second time. Examples: end-to-end tests that subscribe to the newsletter, where each subscription creates a recipient nobody removes unless the test does. One recipient per run never stands out. After two weeks of daily runs the administration shows a list in which real subscribers can no longer be told apart from test data. As soon as a test counts how many recipients exist, it measures the residue of its predecessors.

A plugin that deletes files makes this more critical: a test that hits the real `var/log` would be dangerous.

### Decision

**No test may leave a record that outlives it.** The shop has the same state before and after a test run.

This applies to newsletter recipients, configuration values, categories, content pages, files and everything else a test creates or changes.

- Data is created in `setUp` and deleted in `tearDown`, or by fixtures marked `once`.
- Integration tests run with `IntegrationTestBehaviour`, which resets the database.
- File tests work in a temporary directory (a helper class such as `TemporaryLogDirectory`), never in the real `var/log`.
- System configuration is reset after the test where a test changes it. Changed settings are reset to the previous value, not to an assumed default. The previous value is read before the change.
- **Every created record carries a recognizable prefix or ID** (for example a UUID in cookie names). Only then does the cleanup find it again, also after an aborted run.
- **Whatever was attached to the sales channel is detached first.** A record that something still points to cannot be deleted, and the deletion fails silently in that case.
- **Checking is done by counting, not by looking.** The number of records (shop data counted by SQL count, or visually with fixtures such as a `StorefrontPage` on a known product count setup) before and after two consecutive runs must be equal. A look into the administration misses exactly the one record that matters. In the end-to-end run, shop data is counted before and after the run. The run takes place once, not as a double run.
- **Every test runs in isolation.** No test may fail because the previous one did not clean up.
- **The clean-up rule is absolute.** A test run leaves the shop as it found it. There is one documented exception: cart rows, which are session artifacts no clean-up can see and which Shopware removes daily itself. Everything else is removed, and a report from the global teardown is treated as a defect in the earlier levels and not as the teardown doing its job.

### Consequences

- Tests can be repeated any number of times. Several runs side by side do not collide. A test run is equal to any other.
- A test that creates data is longer than one that only reads. The cleanup is part of the test and not an appendix.
- A silently failed cleanup is worse than none, because it feigns safety. Hence the counter check: it reveals what an executed but ineffective deletion hides.
- Recipients from a manual check are to be removed as well. Since the suite exists, this task no longer arises by hand.
- A check of a shop's real log files is never necessary and never allowed.

## an-end-to-end-test-does-what-a-person-does: An end-to-end test does what a person does and never what a script could do instead

**Area:** testing **Status:** accepted

### Context

A plugin is used by people who never read its code: the merchant who builds a configuration in the administration, and the shopper who fills it in on the product page and pays the displayed price. The defects that reach them lie between the parts: a drag in a structure tree that looks right and is not saved, a condition that hides a field in the browser and not on the server, a surcharge the buy box shows and the cart does not calculate. Typical defects reported from live shops could not have been seen from inside the code: products vanished between pages, a mode silently did nothing, an element was picked up by a third-party plugin as if it were a product.

Unit, integration and Jest tests prove that code calculates what it should. Every level below end-to-end answers a question about a part. A unit test proves the paging arithmetic, a Jest spec proves a component renders what it was handed. Neither shows whether a merchant finds the settings, can fill in the forms, or whether a customer sees the effect. The only question a merchant actually asks is: when I set this up and a shopper visits the page, is what they see correct?

An end-to-end test is the one level that can answer it, and it answers it only if it does what a person does. A browser check that jumps to an internal route or sets values by script proves the script and not the path a human takes. The moment a test reaches past the interface (writing the row the form would have written, posting the request the button would have sent, calling the method the click would have called) it stops testing the thing under test. It then proves that the database accepts a row, which nobody doubted, while the button it skipped may be missing, disabled, mislabelled, covered by another element or wired to nothing at all. A test that creates its subject through an API proves the API, not the screen a merchant or customer uses. A test that leaves data behind pollutes the shop and any external test account.

That is not hypothetical. An element carrying a data attribute was invisible to every level except a browser. A template override resolves through Shopware's per-request template hierarchy and cannot be integration tested at all (proven, and recorded in `CLAUDE.md`). A listing page renders through the CMS, the resolver, the processor and Twig together, and a fault can live in the arithmetic between those parts, where no single part is wrong.

Joint test sessions with the client in the Playwright browser, where the client wants to see and learn how Shopware and the connected external system are operated, showed the same: pages opened via typed addresses, results checked by database query and values read by script save time, but do not show the path a merchant takes and hide defects that only occur in the interface. Two defects of such a session only showed through normal operation: opening an order in the administration deleted a mapping, and the action menu in the dashboard closed during the automatic refresh.

### Decision

**An end-to-end test reproduces human behavior. It may only do what a shopper or a merchant would do, through the surface they would do it through.** A merchant does not write a script to simulate a button click. They click the button. That holds for every interaction, literally and by analogy.

| The test needs | It does | It must never |
|---|---|---|
| an object (interruptor, configurator with groups and options) to exist | fill in the administration form or build it in the administration and press save | write the row through the API or SQL, or write it through the API when it is the subject of the test |
| a setting changed | open the page, change the control, save | update the column directly |
| a new order of groups | drag the group in the structure tree | set `position` through the API |
| a listing checked | open the category page in the browser and read it | render the template or call the resolver |
| the next page | click the pagination control | request the URL with `?p=2` assembled by hand |
| a price checked | fill in the fields on the product page and read buy box, cart and order | call the calculator |
| a condition checked | choose the option that should show the field | render the template |
| something deleted | use the action the interface offers | delete the row |

- **Administration changes are made by clicking and typing**, not by `evaluate` scripts, API calls or direct SQL. No `evaluate` to set values, open dialogs, trigger buttons or change the address. Snapshots, screenshots and the console may be read.
- **Assertions are made against what the person sees:** the rendered page, the visible text, the element that is there or is not. Never against the database behind it, and never against a value read out of a component's internals. Behavior is checked and not CSS or every detail: conditionality and behavior under conditions. For example a value is saved and the core setting corresponds to it.
- **Setting a check up is not the same as carrying it out.** Products, categories, languages, plugins, sales channels and a sales channel assignment are scaffolding and may be created through the Admin API (`_action/sync`). Creating the 200 products a pagination test needs is scaffolding: a merchant would have them already. Only basic data that is not under test is set by API. **The thing being tested never may.** Where the subject of the test is the administration form itself, the form is filled in by hand, even where an API call would be shorter.
- **Navigate like a user:** open the normal start address and reach a page through the menu. No jumps to internal routes, no URL changes, and no deep addresses typed into the address bar.
- **Interact like a user:** click, type, select, scroll, press keys.
- **Every configuration a merchant can set is reachable from the interface, so every one of them is set through the interface.** A combination that can only be produced by writing to the database is a combination the suite does not cover, and that is recorded as a gap rather than faked.
- A setting saved in the administration is checked in the storefront, also with empty and invalid inputs.
- A finding becomes a test in the same change.
- Before a user interface counts as finished it is opened in a real browser, administration and storefront alike. Build first with `shopware-cli` for this extension only, otherwise the browser shows the previous bundle.
- **Two fixed tabs** stay open: tab 0 is the administration, tab 1 the storefront or the place of verification (and in sessions with an external system, tab 2 is that system). Switching is done by tab selection and not by navigating one tab back and forth.
- Credentials are read from `.env.local` and typed in directly, never printed in plain text.
- **Waiting is done the way a person waits**, for the thing to appear: a visible element, a response or a state, with web-first assertions. Never a fixed pause (a guess that is too long on a fast machine and too short on a slow one), no `networkidle` (the administration polls in the background), and no waiting for a message the administration does not show.
- Locators prefer roles, labels and text over test IDs, which at the same time checks accessibility.
- All data a test creates carries a prefix (for example `e2e-`) so it can be found, in the shop and in any external system. The cleanup removes every record with the prefix, also records the test did not know it had created. Two consecutive runs leave the shop and any external test account unchanged, counted before and after.
- Duration is accepted. A test of five minutes is not slow, it is exact.
- Joint test sessions: the administration, the storefront and the external system are operated the way a merchant does, through menus, tabs, search fields, links and buttons, with visible clicks and inputs in the browser. Every page is reached from the entry point of the application. Results are checked where a user sees them (synchronization log, run view, order view of the external system, storefront). REST calls from the page, SQL, console commands and scripts in the browser are used in the session only after consultation. The diagnosis of a code defect may use them, but is announced as such and kept apart from the operating flow. Each step is briefly explained.

### Consequences

- The suite is slower than one that posts its way to the same state. That is the price of the only level that can see what the others cannot, and it is paid deliberately.
- A test breaks when the interface changes (a renamed control, a moved button, a field that became a select). **That is the test working, not the test being brittle.** A merchant's habit breaks in exactly the same way, and the suite is the first to say so.
- Some failures will be in the test rather than in the plugin, because a human interaction has more steps than a direct write. Each is read as a report about the interface before it is read as a report about the test: a step that is hard to express is usually a step that is hard to perform.
- Tests are maintainable because they show what users do. Errors are close to the experience and not to test details. A green run says a person could do the task, and a test with data leaks is found on the second run.
- Broken menus and screens that only fail on the normal path are noticed before a merchant finds them.
- Test data is prefixed and removed afterwards, and a run leaves the shop as it found it, counted before and after two consecutive runs, never assumed. The levels beneath this one are described in the test strategy decision.
- Joint sessions take longer, but uncover operating defects and serve the client as training. If an interface is missing for a step, that is recorded as a finding instead of being done secretly via a detour.
- The rule complements the browser test rule, which likewise navigates, clicks and types like a user.

## end-to-end-tests-run-against-browserless: End-to-end tests connect to a browserless container and never install a browser

**Area:** testing **Status:** accepted

### Context

Installing a real browser into the development web container costs space (about 150 MB per project) and is lost with every image rebuild. The development environment (DDEV is the example here) provides a browserless add-on, the DDEV add-on `ddev-browserless`, that runs a Chromium in a container of its own and is addressed over a websocket. A single route for all plugins is better than two that drift apart. An earlier setup described starting the specs in a separate Playwright container whose configuration did not exist, so the specs could not run at all.

The add-on's own README is the authority on its variables, endpoints and commands. It is referenced and not copied, because a copy goes stale silently. The figures below were read from it at the time of writing and may have moved since.

Two properties decide how a suite has to be written.

**A browserless session has a lifetime, and it is short.** `BROWSERLESS_TIMEOUT` defaults to 120000 ms (two minutes), after which the browser is taken away mid-test. Playwright reports this as `Target page, context or browser has been closed`, which reads like a crashed page rather than like a deadline. The test timeout in `playwright.config.ts` does not help: the smaller of the two limits wins, and a 300 second test limit is simply never reached.

**The browser reaches the shop through the DDEV router**, not through `web` directly, so it is a genuine external client. It does not trust DDEV's mkcert certificate, and plain http is no way around that because the router sends HSTS.

### Decision

- **The suite connects to browserless at the dedicated Playwright endpoint** `ws://browserless:3000/chromium/playwright?token=...` and runs inside the web container. The token comes from the add-on's environment, never from the repository. `BROWSERLESS_TOKEN` is mandatory, and if it is missing the configuration says how browserless is started.
- **The browser is never installed locally**, and the suite never assumes one is present. Playwright uses the remote connection only. The separate Playwright container is not used, so that there is one way of running these tests rather than two that drift apart.
- **The configuration reads the shop's `.env.local`**, so that a fresh checkout needs no file of its own.
- **The session limit is raised for the project and not worked around in the tests.** `BROWSERLESS_TIMEOUT` is set to 900000 (900 seconds) through the add-on's own mechanism: `ddev dotenv set .ddev/.env.browserless --browserless-timeout 900000`, followed by `ddev restart`, because `ddev browserless restart` reuses the existing container and keeps the old value. Every change made to the add-on's configuration in the project is recorded in `browserless-changes.md` at the project root, with what was changed, why, and how to restore it after an add-on update.
- **A test still does not depend on a long session.** The limit is raised because a suite legitimately needs several minutes (for example 200 products across nine pages), not so that a badly written wait can sit there. A long test is not an error, and the time limit is generous. Tests stay short and independent, and the session limit decides and not the Playwright test timeout.
- **Never wait for `networkidle`.** The administration polls in the background and holds connections open, so the network is never idle and every such wait burns its full timeout (measured once: seven waits at 60 seconds each inside a session that lasted 120). Wait for what a person waits for: the spinner going, the row appearing, the notice becoming visible, the page changing.
- **Waiting for something that never appears is the same fault in a different shape.** Saving an entity may show no success notification. What tells a person it worked is, for example, the create page becoming the detail page. A test does not wait for a message the administration does not show.
- **`ignoreHTTPSErrors` is on**, because the browser is external to the shop, reaches it through the router and cannot be given DDEV's CA.
- The flow without JavaScript runs in the same suite, in a browser context with `javaScriptEnabled: false`.
- The command runs in the web container from the plugin's end-to-end folder:

```bash
ddev browserless on
ddev exec -d /var/www/html/shopware/custom/static-plugins/<Plugin>/tests/E2E \
    npx playwright test
```

- **Watching a run** is done through the add-on's debugger UI at `http://<project>.ddev.site:3000/debugger/?token=...`. Playwright's own UI mode is not available over browserless: it needs a browser to display itself in, and the browserless container has none to spare for that.

### Consequences

- There is no browser installation step in the setup. The environment is the same for all projects, the effort for a new shop stays small, and tests are quickly written.
- The suite needs `ddev browserless on` before it runs, and says so in the error when the token is missing rather than failing obscurely.
- A developer who has just checked the plugin out needs nothing beyond that, because the configuration falls back to the shop's own `.env.local` for credentials.
- A `browser closed` error most likely means the session limit was reached, not that a crash occurred. A test that dies at two minutes has a local timeout problem and not a code problem. A test that dies at a time limit is first treated as a problem of the test (see the decision on classifying failing tests).
- The session limit is project configuration and not plugin configuration, so it does not travel with the plugin. A plugin checked out into another project runs against whatever that project's browserless is set to, and a suite that suddenly dies at two minutes is this setting, which is why it is written down in `browserless-changes.md` and not only here.
- If the add-on changes its variables, its endpoints or its commands, this decision is wrong and the add-on's repository is right. An accepted ADR is not edited: a new one replaces it.

## mutation-testing-comes-last: Mutation testing runs as the very last step on a stable suite, with every surviving mutant assessed

**Area:** testing **Status:** accepted

### Context

Mutation tests measure whether the tests notice changes to the code. A measurement against code that is still changing says nothing. It also takes a long time: minutes on a small plugin, hours on a large one. A gate slow enough to tempt anyone into skipping it protects nothing, so mutation runs deliberately, after the test suite changes shape and before a release.

### Decision

- **Mutation runs last, after every other level is green**, on a stable suite. Whether it runs without an explicit request is stated in the plugin's `CLAUDE.md`. The default is on request.
- **The tool is Infection** (`composer infection` or `composer mutation`), with one thread and `--only-covering-test-cases`. Stryker is used for JavaScript bundles (administration and storefront).
- **`Resources/config` and `Migration` are excluded.**
- **The baseline lies under `docs/mutation/`** (for example `docs/mutation/<date>/README.md`). Reports are created under `var/infection/`.
- **Mutation is not part of `composer gate`.**
- **Surviving mutants are classified one by one.** A missing test becomes a test that states the rule. Dead or redundant code is removed. An equivalent mutant is documented with its reason in the mutation baseline.
- A running mutation pass is stopped when a new task arrives and restarted at the end. Where the suite shape has changed, mutation runs again.
- The first run sets the baseline, and thresholds follow from the measured figure. The result is as close to 100 percent as honest tests come.

### Consequences

- The measurement is meaningful because the code is stable. The gate stays fast.
- A later change to production code requires a new measurement.
- Results are only meaningful on a stable suite.

## administration-tests-with-jest: The administration has its own pinned Jest setup, and every interactive element gets a test

**Area:** administration **Status:** accepted

### Context

The plugin owner requires tests for all administration code. Shopware tests its own administration with Jest, but its testing guide states plainly that it "only applies to the Shopware-provided Administration! If you use unit tests in your plugin, you might need to write your own scripts for that."

Two further findings shaped this decision, both verified in the installation:

- The guide's example is outdated. It uses `createLocalVue` and `shallowMount`, which belong to Vue Test Utils 1 for Vue 2. Shopware 6.7 runs Vue 3.5.22 with `@vue/test-utils` 2.4.6, where `createLocalVue` no longer exists.
- Jest is declared in the core's `package.json` but not installed in `vendor/shopware/administration/.../node_modules`, because the asset build pulls production dependencies only. A plugin therefore cannot borrow the core's test runner and needs its own.

Another plugin in the same project already carries admin specs in the Vue 3 style: `mount` from `@vue/test-utils`, the component imported directly, `global.stubs` and `global.mocks`. That is the pattern worth continuing.

### Decision

The administration has its own Jest setup under `src/Resources/app/administration/`:

| File | Purpose |
|---|---|
| `package.json` | test dependencies and the `unit`, `unit:watch`, `unit:coverage` scripts |
| `jest.config.js` | jsdom environment, transforms for Twig and SCSS, the Shopware setup file |
| `babel.config.js` | `@babel/preset-env` targeting the running node |
| `test/_setup/shopware.js` | minimal stand-in for the global `Shopware` object |
| `test/_transformer/` | Twig templates become strings, stylesheets become empty modules |

Versions are pinned to exactly what the Shopware version in use declares (at the time of writing Shopware v6.7.14.0: Jest 30.2.0, `@vue/test-utils` 2.4.6, Vue 3.5.22), so the test environment matches the runtime. `@vue/vue3-jest` is deliberately absent: it requires babel-jest 29 while Shopware is on 30, and the plugin's components are `.js` files with Twig templates and not single-file components.

Tests live in `src/Resources/app/administration/test/`, grouped by subject and not beside the component. This keeps the shipped source free of test files.

**What is tested, and how:**

- *Module registration:* routes, navigation, ACL roles and search configuration are asserted against the registrations recorded by the Shopware mock.
- *Pages:* the options object is exercised directly. Computed properties are called with a prepared context, methods with mocked repositories. Mounting a page would drag in the entire administration component tree and test Shopware rather than the plugin.
- *Components with real markup:* mounted with `mount` and stubbed `mt-*` components.

**Coverage is exhaustive, not representative.** Every interactive element gets a test: every button, every filter, every entity selector, every toggle, every emitted event, every route transition, every error path. If a user can click it or a repository can fail on it, there is a test for it.

| Element | What the test asserts |
|---|---|
| Button | the handler runs, the right route or repository call follows, the disabled state matches the privilege |
| Filter | the criteria carry the expected filter, clearing it removes the filter, combinations work |
| Entity selector | the criteria and entity name are right, selection updates the model, clearing works |
| Toggle, input | the model updates, validation and the disabled state hold |
| Listing | columns, sorting, paging, the refresh action, the empty state |
| Error path | a rejected repository call produces a notification rather than an exception, and loading state resets |
| ACL | removing the privilege blocks the action |

The standard is that everything built is verified to work, not that a sample of it is.

Admin tests run through `npm run unit` and are part of the definition of done. They are not in `composer gate` where that gate is PHP only. The CI pipeline runs both. Where the gate includes Jest, the Jest threshold of 100 % is enforced as described in the test strategy decision.

### Consequences

- Admin logic is verifiable without a browser and without a running shop, tests run in under a second, and ACL mistakes surface immediately.
- The `Shopware` global mock has to grow with every new global the code touches. It is deliberately minimal. When a test fails on a missing global, extend the mock rather than working around it in the test.
- Testing the options object rather than a mounted component means template bindings are not covered. Those are verified by the Playwright end-to-end layer instead (see the test strategy decision).
- The pinned versions must be checked against Shopware's `package.json` on every upgrade, the same way the PHP toolchain is pinned.

## pest-is-rejected: Tests are written in PHPUnit and Pest is not adopted

**Area:** testing **Status:** accepted

### Context

Pest was evaluated twice and rejected twice. The argument for it is real: Pest unifies unit, integration, architecture and mutation testing under one syntax, which is exactly what this standard assembles by hand.

### Decision

Tests are written in PHPUnit. Pest is not adopted. Three things speak against it:

- **The architecture rules run on phpat, through PHPStan**, and therefore share PHPStan's type resolution. Pest's own architecture tests do not. Adopting them means trading a stronger tool for a weaker one.
- **Integration tests are built on Shopware's `TestBootstrapper` and `IntegrationTestBehaviour`**, both PHPUnit classes. Pest would wrap them, and every Shopware upgrade would mean checking whether the wrapper still fits.
- **Infection drives PHPUnit either way.** The syntax of the tests changes nothing there.

Shopware's own suite, the acceptance test suite and every reference plugin are PHPUnit.

**Revisit if** a plugin is ever extracted from the Shopware context entirely.

### Consequences

The gain that is given up is nicer unit-test syntax. The price that is avoided is two syntaxes in one codebase. A rejection is a record too, so the question is not argued again from scratch every year.

## five-phpunit-configs-not-one: The plugin carries five phpunit configurations and a sixth one for Infection in its own directory

**Area:** testing **Status:** accepted

### Context

A filtered run must never overwrite a full coverage report. Infection passes `--configuration` itself while looking only for a file literally named `phpunit.*` in the directory it is pointed at.

### Decision

- There are five phpunit configurations: unit, integration, and three coverage variants.
- A sixth one for Infection lives in `build/infection/`.
- Giving Infection a directory of its own keeps the plugin's configurations untouched.

### Consequences

A filtered run cannot destroy a full coverage report, and Infection finds its configuration without touching the others. The price is six configuration files instead of one.

## coverage-thresholds-are-enforced-in-jest-and-read-in-php: Jest enforces the 100 percent threshold, the PHP figure is read and acted on

**Area:** testing **Status:** accepted

### Context

PHPUnit's own threshold options are coarser than Jest's per-metric thresholds.

### Decision

- Jest fails the run below 100 %.
- The PHP figure is read and acted on rather than enforced by a flag.
- The asymmetry is practical, not principled. If PHPUnit gains a usable per-metric threshold, it is used.

### Consequences

The two sides are held to the same number by different mechanisms. The PHP side depends on the figure being read after a measuring run (see the coverage decision).

## phpat-over-deptrac: Architecture rules run on phpat inside PHPStan and not on Deptrac

**Area:** testing **Status:** accepted

### Context

Deptrac parses independently, knows less, and needs its own run, its own configuration and its own gate slot. The reference plugin migrated away from it.

### Decision

phpat runs inside PHPStan and shares its type resolution. Deptrac is not used.

### Consequences

One analysis, one configuration and one gate slot cover both types and architecture. phpat rules are written as PHPStan rules and are green or the gate is red.

## rector-type-perfect-is-kept-although-abandoned: rector/type-perfect is kept although Composer reports it as abandoned

**Area:** testing **Status:** accepted

### Context

Composer warns that the package is abandoned. The suggested replacement checks something else.

### Decision

`rector/type-perfect` stays in the toolchain. It is revisited when a rule actually breaks, not because of the warning.

### Consequences

The Composer warning is accepted knowingly. A breaking rule, not the warning, is the trigger for a new decision.

## coverage-reports-are-ignored-and-mutation-baselines-are-committed: Coverage reports stay out of git and mutation baselines go in

**Area:** testing **Status:** accepted

### Context

This looks inconsistent and is not.

**Coverage reports** are reproducible in seconds, change wholesale on every run and make every diff unreadable. Nothing is lost by regenerating them.

**Mutation baselines** cost hours per run. The figure's history answers a question nothing else can: "we were at 96 %, why are we at 71 %?" is unanswerable without the old run. That is worth a few kilobytes.

### Decision

**Coverage reports: ignored.**

**Mutation baselines: committed.** Committed are `docs/mutation/<date>/summary.json`, `infection.log` and a `README.md` with the table and the judgement on every survivor. Not committed is `infection.html`, which is large and says nothing the log does not.

**The line between them:** what is reproducible in seconds stays out. What costs hours and serves as a comparison point goes in.

The `.gitignore` reads:

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

### Built storefront assets: a release archive carries them, git does not.
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
tests/E2E/.env
tests/E2E/test-results/
tests/E2E/playwright-report/
tests/E2E/report.xml
tests/E2E/blob-report/
tests/E2E/.cache/

### Logs, except the mutation baselines below
*.log
!docs/mutation/**/*.log

### Mutation baselines ARE committed: a score costs hours and its history answers a
### question nothing else can. The verbose HTML report is not kept.
!docs/mutation/
docs/mutation/**/infection.html
```

### Consequences

Diffs stay readable, and the history of the mutation score survives a rerun. The baseline directory grows by a few kilobytes per run.
