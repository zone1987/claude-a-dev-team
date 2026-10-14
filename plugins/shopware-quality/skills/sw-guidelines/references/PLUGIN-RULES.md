# Plugin rule book

The binding decisions for every Shopware plugin of ours: 84 cross-cutting decisions, merged from the ADRs of nine plugins, each decision once. Each is a `## <slug>: <sentence>` section with Context, Decision and Consequences. The text is English, a plugin's own ADRs are German.

**Precedence.** The rule book wins over older wording in the other `PLUGIN-*` references. Inside a plugin its own accepted ADRs add domain decisions and may tighten a rule but never loosen it.

**How a plugin uses it.** The plugin's `adr/` directory holds German ADRs. The rule book is the English source that the plugin's cross-cutting ADRs follow. Domain decisions stay in the plugin. Load it before writing or reviewing plugin code.

## Contents

- [Code](#code) (13)
- [Shopware](#shopware) (10)
- [User interface](#user-interface) (8)
- [Resilience and security](#resilience-and-security) (12)
- [Integration](#integration) (6)
- [Data](#data) (5)
- [Testing](#testing) (14)
- [Process, documentation and repository](#process-documentation-and-repository) (15)

## Code

Chapter file: [PLUGIN-RULES-CODE.md](PLUGIN-RULES-CODE.md).

| Decision | Area |
|---|---|
| [Prose comments are not written in any file type](PLUGIN-RULES-CODE.md#no-prose-comments-prose-comments-are-not-written-in-any-file-type) | core |
| [DocBlocks carry complete tags and nothing but tags, and no tool strips them](PLUGIN-RULES-CODE.md#complete-docblock-tags-docblocks-carry-complete-tags-and-nothing-but-tags-and-no-tool-strips-them) | core |
| [@throws names every exception PhpStorm reports and is never guessed](PLUGIN-RULES-CODE.md#throws-where-known-throws-names-every-exception-phpstorm-reports-and-is-never-guessed) | core |
| [Classes and functions are imported, test classes use self::, and readonly is declared where possible](PLUGIN-RULES-CODE.md#classes-and-functions-are-imported-classes-and-functions-are-imported-test-classes-use-self-and-readonly-is-declared-where-possible) | core |
| [Every PhpStorm inspection is resolved](PLUGIN-RULES-CODE.md#every-phpstorm-inspection-is-resolved-every-phpstorm-inspection-is-resolved) | core |
| [PHP and Shopware code conventions](PLUGIN-RULES-CODE.md#php-conventions-php-and-shopware-code-conventions) | core |
| [Classes live where their kind belongs, names are derived, and the structure is technical, not DDD](PLUGIN-RULES-CODE.md#technical-folder-structure-classes-live-where-their-kind-belongs-names-are-derived-and-the-structure-is-technical-not-ddd) | core |
| [Services, routes and bundle configuration are registered explicitly in PHP](PLUGIN-RULES-CODE.md#services-registered-explicitly-in-php-services-routes-and-bundle-configuration-are-registered-explicitly-in-php) | core |
| [Layers are enforced by architecture rules, and transport, format and meaning are separate layers](PLUGIN-RULES-CODE.md#layers-enforced-by-architecture-rules-layers-are-enforced-by-architecture-rules-and-transport-format-and-meaning-are-separate-layers) | core |
| [Extension goes through tagged registries and narrow interfaces](PLUGIN-RULES-CODE.md#extension-through-tagged-registries-extension-goes-through-tagged-registries-and-narrow-interfaces) | core |
| [Events let project code change data](PLUGIN-RULES-CODE.md#events-let-project-code-change-data-events-let-project-code-change-data) | core |
| [Typed readers hold each field path exactly once](PLUGIN-RULES-CODE.md#typed-readers-hold-each-field-path-once-typed-readers-hold-each-field-path-exactly-once) | core |
| [Money is integer minor units, and net prices are stored unrounded like the core](PLUGIN-RULES-CODE.md#money-handling-money-is-integer-minor-units-and-net-prices-are-stored-unrounded-like-the-core) | data |

## Shopware

Chapter file: [PLUGIN-RULES-SHOPWARE.md](PLUGIN-RULES-SHOPWARE.md).

| Decision | Area |
|---|---|
| [Use everything Shopware provides, build your own only where the core offers no way, and read the core source instead of remembering it](PLUGIN-RULES-SHOPWARE.md#shopware-first-and-the-core-is-read-use-everything-shopware-provides-build-your-own-only-where-the-core-offers-no-way-and-read-the-core-source-instead-of-remembering-it) | core |
| [No code that Shopware marks as internal is used, not in production code and not in tests](PLUGIN-RULES-SHOPWARE.md#nothing-internal-from-shopware-no-code-that-shopware-marks-as-internal-is-used-not-in-production-code-and-not-in-tests) | core |
| [The plugin depends on PHP, Shopware and Symfony only, references no other plugin, copies no third-party code and ships no styling](PLUGIN-RULES-SHOPWARE.md#the-plugin-stands-alone-the-plugin-depends-on-php-shopware-and-symfony-only-references-no-other-plugin-copies-no-third-party-code-and-ships-no-styling) | core |
| [The plugin is generic and runs in any shop](PLUGIN-RULES-SHOPWARE.md#the-plugin-is-generic-the-plugin-is-generic-and-runs-in-any-shop) | core |
| [The plugin builds nothing that the supported Shopware line does not use itself yet](PLUGIN-RULES-SHOPWARE.md#only-what-the-supported-core-uses-the-plugin-builds-nothing-that-the-supported-shopware-line-does-not-use-itself-yet) | core |
| [Data is accessed only through the DAL, SQL only in a few named places, and sync writes go through the DAL so core invalidation runs](PLUGIN-RULES-SHOPWARE.md#data-access-only-through-the-dal-data-is-accessed-only-through-the-dal-sql-only-in-a-few-named-places-and-sync-writes-go-through-the-dal-so-core-invalidation-runs) | data |
| [A state transition goes through an API route, never through the repository](PLUGIN-RULES-SHOPWARE.md#state-transitions-through-api-routes-a-state-transition-goes-through-an-api-route-never-through-the-repository) | core |
| [Configuration lives in the system configuration with sales channel scope](PLUGIN-RULES-SHOPWARE.md#configuration-in-system-config-configuration-lives-in-the-system-configuration-with-sales-channel-scope) | api |
| [Performance is never traded, pages stay fast and cacheable, and caches are invalidated explicitly and precisely](PLUGIN-RULES-SHOPWARE.md#performance-and-caching-performance-is-never-traded-pages-stay-fast-and-cacheable-and-caches-are-invalidated-explicitly-and-precisely) | core |
| [The plugin runs in parallel to the old plugins, parity is the acceptance criterion, and the legacy import is idempotent and reuses the settings import](PLUGIN-RULES-SHOPWARE.md#parallel-run-and-legacy-migration-the-plugin-runs-in-parallel-to-the-old-plugins-parity-is-the-acceptance-criterion-and-the-legacy-import-is-idempotent-and-reuses-the-settings-import) | core |

## User interface

Chapter file: [PLUGIN-RULES-UI.md](PLUGIN-RULES-UI.md).

| Decision | Area |
|---|---|
| [No component in the plugin's administration is rendered small, and everything sits inside the card frame](PLUGIN-RULES-UI.md#nothing-in-the-administration-is-small-no-component-in-the-plugins-administration-is-rendered-small-and-everything-sits-inside-the-card-frame) | administration |
| [The administration is built from core components, core icons and core services only](PLUGIN-RULES-UI.md#administration-built-from-core-components-the-administration-is-built-from-core-components-core-icons-and-core-services-only) | administration |
| [Every entity listing shows a centered empty state](PLUGIN-RULES-UI.md#every-listing-has-an-empty-state-every-entity-listing-shows-a-centered-empty-state) | administration |
| [The storefront is overridden as little as possible, templates only extend named blocks and render](PLUGIN-RULES-UI.md#minimal-storefront-overrides-the-storefront-is-overridden-as-little-as-possible-templates-only-extend-named-blocks-and-render) | storefront |
| [Storefront and administration output is accessible and uses semantic markup](PLUGIN-RULES-UI.md#accessibility-and-semantic-markup-storefront-and-administration-output-is-accessible-and-uses-semantic-markup) | storefront |
| [Structured data is emitted only where the page shows it](PLUGIN-RULES-UI.md#structured-data-only-where-the-page-shows-it-structured-data-is-emitted-only-where-the-page-shows-it) | storefront |
| [The buyer never has to guess why something happens or what is missing](PLUGIN-RULES-UI.md#the-buyer-never-has-to-guess-the-buyer-never-has-to-guess-why-something-happens-or-what-is-missing) | storefront |
| [Every change is verified in a real browser, the way a person uses it, and an element counts as done only when a layout carries it](PLUGIN-RULES-UI.md#every-change-is-verified-in-the-browser-every-change-is-verified-in-a-real-browser-the-way-a-person-uses-it-and-an-element-counts-as-done-only-when-a-layout-carries-it) | process |

## Resilience and security

Chapter file: [PLUGIN-RULES-RESILIENCE-SECURITY.md](PLUGIN-RULES-RESILIENCE-SECURITY.md).

| Decision | Area |
|---|---|
| [Nothing the plugin does or gets wrong may stop a shop, a page, the checkout, the administration, the scheduler or the worker](PLUGIN-RULES-RESILIENCE-SECURITY.md#the-plugin-never-stops-the-shop-nothing-the-plugin-does-or-gets-wrong-may-stop-a-shop-a-page-the-checkout-the-administration-the-scheduler-or-the-worker) | core |
| [Errors are typed exceptions with stable codes and a category that decides retries](PLUGIN-RULES-RESILIENCE-SECURITY.md#typed-errors-with-stable-codes-errors-are-typed-exceptions-with-stable-codes-and-a-category-that-decides-retries) | core |
| [No external provider call blocks the checkout](PLUGIN-RULES-RESILIENCE-SECURITY.md#no-blocking-external-call-in-the-checkout-no-external-provider-call-blocks-the-checkout) | checkout |
| [Failed sync pages are retried with a delay and then dead lettered](PLUGIN-RULES-RESILIENCE-SECURITY.md#failed-async-work-is-retried-then-dead-lettered-failed-sync-pages-are-retried-with-a-delay-and-then-dead-lettered) | sync |
| [Privacy is built in, not retrofitted](PLUGIN-RULES-RESILIENCE-SECURITY.md#privacy-by-design-privacy-is-built-in-not-retrofitted) | legal |
| [Nothing reaches a third party before consent, and server side events need stored consent](PLUGIN-RULES-RESILIENCE-SECURITY.md#nothing-reaches-a-third-party-before-consent-nothing-reaches-a-third-party-before-consent-and-server-side-events-need-stored-consent) | storefront |
| [A plugin writes to its own log channel at level info, and log rows and runs are pruned by age](PLUGIN-RULES-RESILIENCE-SECURITY.md#log-channel-and-log-retention-a-plugin-writes-to-its-own-log-channel-at-level-info-and-log-rows-and-runs-are-pruned-by-age) | log |
| [Roles grant no system config, risky actions have their own privilege and write in the system scope](PLUGIN-RULES-RESILIENCE-SECURITY.md#acl-privileges-roles-grant-no-system-config-risky-actions-have-their-own-privilege-and-write-in-the-system-scope) | security |
| [A disclosure policy in SECURITY.md and an SBOM for every release](PLUGIN-RULES-RESILIENCE-SECURITY.md#security-policy-and-sbom-a-disclosure-policy-in-securitymd-and-an-sbom-for-every-release) | security |
| [A webhook receiver checks the sender before it reads the body](PLUGIN-RULES-RESILIENCE-SECURITY.md#a-receiver-checks-the-sender-before-the-body-a-webhook-receiver-checks-the-sender-before-it-reads-the-body) | security |
| [Development never touches live, and no task may overrule that](PLUGIN-RULES-RESILIENCE-SECURITY.md#development-never-touches-live-development-never-touches-live-and-no-task-may-overrule-that) | provider |
| [Exported settings are portable, carry no secrets and delete nothing](PLUGIN-RULES-RESILIENCE-SECURITY.md#exported-settings-carry-no-secrets-exported-settings-are-portable-carry-no-secrets-and-delete-nothing) | administration |

## Integration

Chapter file: [PLUGIN-RULES-INTEGRATION.md](PLUGIN-RULES-INTEGRATION.md).

| Decision | Area |
|---|---|
| [The API client is built on the Symfony HttpClient and caches its access token per host and user](PLUGIN-RULES-INTEGRATION.md#api-client-on-symfony-http-client-the-api-client-is-built-on-the-symfony-httpclient-and-caches-its-access-token-per-host-and-user) | api |
| [Rate limits are read from the response headers and waits are injectable](PLUGIN-RULES-INTEGRATION.md#rate-limits-from-response-headers-rate-limits-are-read-from-the-response-headers-and-waits-are-injectable) | api |
| [Every external API can be tested directly in the configuration](PLUGIN-RULES-INTEGRATION.md#every-external-api-can-be-tested-every-external-api-can-be-tested-directly-in-the-configuration) | administration |
| [Synced records keep a raw snapshot and separate the remote status from the internal state](PLUGIN-RULES-INTEGRATION.md#synced-records-keep-a-raw-snapshot-synced-records-keep-a-raw-snapshot-and-separate-the-remote-status-from-the-internal-state) | data |
| [Webhooks and notifications are only a hint, and polling stays as the floor](PLUGIN-RULES-INTEGRATION.md#webhooks-are-a-hint-polling-stays-webhooks-and-notifications-are-only-a-hint-and-polling-stays-as-the-floor) | sync |
| [A dry run writes nothing and keeps cursor and schedule unchanged](PLUGIN-RULES-INTEGRATION.md#a-dry-run-writes-nothing-a-dry-run-writes-nothing-and-keeps-cursor-and-schedule-unchanged) | sync |

## Data

Chapter file: [PLUGIN-RULES-DATA.md](PLUGIN-RULES-DATA.md).

| Decision | Area |
|---|---|
| [Uninstall removes plugin data only when asked and always keeps shop data](PLUGIN-RULES-DATA.md#uninstall-removes-plugin-data-only-when-asked-uninstall-removes-plugin-data-only-when-asked-and-always-keeps-shop-data) | data |
| [Migrations are additive and idempotent, and live shops decide what may change](PLUGIN-RULES-DATA.md#migrations-are-additive-and-live-shops-decide-migrations-are-additive-and-idempotent-and-live-shops-decide-what-may-change) | data |
| [Deleting data that others reference cleans up every reference](PLUGIN-RULES-DATA.md#deleting-referenced-data-cleans-up-deleting-data-that-others-reference-cleans-up-every-reference) | data |
| [Default data is created in the plugin lifecycle and large imports run in the message queue](PLUGIN-RULES-DATA.md#default-data-in-the-lifecycle-default-data-is-created-in-the-plugin-lifecycle-and-large-imports-run-in-the-message-queue) | core |
| [Synchronization runs on activate and update, not on install](PLUGIN-RULES-DATA.md#configuration-sync-on-activation-synchronization-runs-on-activate-and-update-not-on-install) | core |

## Testing

Chapter file: [PLUGIN-RULES-TESTING.md](PLUGIN-RULES-TESTING.md).

| Decision | Area |
|---|---|
| [Every test level answers its own question, coverage is 100 percent, and one gate command decides whether work is finished](PLUGIN-RULES-TESTING.md#test-strategy-every-test-level-answers-its-own-question-coverage-is-100-percent-and-one-gate-command-decides-whether-work-is-finished) | testing |
| [A coverage number is only valid when it is measured, asserted and free of faked branches](PLUGIN-RULES-TESTING.md#coverage-must-be-honest-a-coverage-number-is-only-valid-when-it-is-measured-asserted-and-free-of-faked-branches) | testing |
| [A failing test is classified as code, expectation, setup or environment before anything is changed](PLUGIN-RULES-TESTING.md#a-failing-test-is-classified-first-a-failing-test-is-classified-as-code-expectation-setup-or-environment-before-anything-is-changed) | testing |
| [No test leaves a record that outlives it, and cleanup is verified by counting](PLUGIN-RULES-TESTING.md#a-test-run-leaves-the-shop-unchanged-no-test-leaves-a-record-that-outlives-it-and-cleanup-is-verified-by-counting) | testing |
| [An end-to-end test does what a person does and never what a script could do instead](PLUGIN-RULES-TESTING.md#an-end-to-end-test-does-what-a-person-does-an-end-to-end-test-does-what-a-person-does-and-never-what-a-script-could-do-instead) | testing |
| [End-to-end tests connect to a browserless container and never install a browser](PLUGIN-RULES-TESTING.md#end-to-end-tests-run-against-browserless-end-to-end-tests-connect-to-a-browserless-container-and-never-install-a-browser) | testing |
| [Mutation testing runs as the very last step on a stable suite, with every surviving mutant assessed](PLUGIN-RULES-TESTING.md#mutation-testing-comes-last-mutation-testing-runs-as-the-very-last-step-on-a-stable-suite-with-every-surviving-mutant-assessed) | testing |
| [The administration has its own pinned Jest setup, and every interactive element gets a test](PLUGIN-RULES-TESTING.md#administration-tests-with-jest-the-administration-has-its-own-pinned-jest-setup-and-every-interactive-element-gets-a-test) | administration |
| [Tests are written in PHPUnit and Pest is not adopted](PLUGIN-RULES-TESTING.md#pest-is-rejected-tests-are-written-in-phpunit-and-pest-is-not-adopted) | testing |
| [The plugin carries five phpunit configurations and a sixth one for Infection in its own directory](PLUGIN-RULES-TESTING.md#five-phpunit-configs-not-one-the-plugin-carries-five-phpunit-configurations-and-a-sixth-one-for-infection-in-its-own-directory) | testing |
| [Jest enforces the 100 percent threshold, the PHP figure is read and acted on](PLUGIN-RULES-TESTING.md#coverage-thresholds-are-enforced-in-jest-and-read-in-php-jest-enforces-the-100-percent-threshold-the-php-figure-is-read-and-acted-on) | testing |
| [Architecture rules run on phpat inside PHPStan and not on Deptrac](PLUGIN-RULES-TESTING.md#phpat-over-deptrac-architecture-rules-run-on-phpat-inside-phpstan-and-not-on-deptrac) | testing |
| [rector/type-perfect is kept although Composer reports it as abandoned](PLUGIN-RULES-TESTING.md#rector-type-perfect-is-kept-although-abandoned-rectortype-perfect-is-kept-although-composer-reports-it-as-abandoned) | testing |
| [Coverage reports stay out of git and mutation baselines go in](PLUGIN-RULES-TESTING.md#coverage-reports-are-ignored-and-mutation-baselines-are-committed-coverage-reports-stay-out-of-git-and-mutation-baselines-go-in) | testing |

## Process, documentation and repository

Chapter file: [PLUGIN-RULES-PROCESS.md](PLUGIN-RULES-PROCESS.md).

| Decision | Area |
|---|---|
| [Code, identifiers, file names, comments and commits are English, and every Markdown file of a plugin is German](PLUGIN-RULES-PROCESS.md#language-code-english-markdown-german-code-identifiers-file-names-comments-and-commits-are-english-and-every-markdown-file-of-a-plugin-is-german) | documentation |
| [No text a person reads contains semicolons or dashes, and a test checks it](PLUGIN-RULES-PROCESS.md#no-semicolons-or-dashes-in-texts-no-text-a-person-reads-contains-semicolons-or-dashes-and-a-test-checks-it) | documentation |
| [Assets are built with shopware-cli and nothing else](PLUGIN-RULES-PROCESS.md#assets-built-with-shopware-cli-assets-are-built-with-shopware-cli-and-nothing-else) | devops |
| [CI pipeline with staged checks, tag-driven release and an enforced version match](PLUGIN-RULES-PROCESS.md#ci-pipeline-ci-pipeline-with-staged-checks-tag-driven-release-and-an-enforced-version-match) | devops |
| [The changelog is written in German from a git-cliff draft, and an upgrade guide is maintained](PLUGIN-RULES-PROCESS.md#changelog-and-upgrade-guide-the-changelog-is-written-in-german-from-a-git-cliff-draft-and-an-upgrade-guide-is-maintained) | documentation |
| [Work happens on content-named feature branches in grouped Conventional Commits, merged by the owner and never pushed](PLUGIN-RULES-PROCESS.md#git-workflow-work-happens-on-content-named-feature-branches-in-grouped-conventional-commits-merged-by-the-owner-and-never-pushed) | process |
| [Every decision is an ADR, and the ADR folder with its index is the rule book](PLUGIN-RULES-PROCESS.md#every-decision-is-an-adr-every-decision-is-an-adr-and-the-adr-folder-with-its-index-is-the-rule-book) | process |
| [Knowledge lives in ADRs, CLAUDE.md and a local, unversioned CONTEXT.md](PLUGIN-RULES-PROCESS.md#knowledge-in-adrs-claude-md-and-context-md-knowledge-lives-in-adrs-claudemd-and-a-local-unversioned-contextmd) | process |
| [A new request is routed to its record before it is followed](PLUGIN-RULES-PROCESS.md#a-new-request-is-recorded-before-it-is-followed-a-new-request-is-routed-to-its-record-before-it-is-followed) | process |
| [One task at a time with a measurable definition of done, features first, tests next, mutation testing last](PLUGIN-RULES-PROCESS.md#one-task-at-a-time-one-task-at-a-time-with-a-measurable-definition-of-done-features-first-tests-next-mutation-testing-last) | process |
| [The model is chosen per task, Opus work stays in the main session, and delegated agents own disjoint files](PLUGIN-RULES-PROCESS.md#model-choice-and-subagents-the-model-is-chosen-per-task-opus-work-stays-in-the-main-session-and-delegated-agents-own-disjoint-files) | process |
| [The licence is proprietary and is checked by hand at the start of every piece of work](PLUGIN-RULES-PROCESS.md#licence-is-proprietary-the-licence-is-proprietary-and-is-checked-by-hand-at-the-start-of-every-piece-of-work) | legal |
| [Every image is licence-free, documented, and marked when a machine made it](PLUGIN-RULES-PROCESS.md#images-are-licence-free-every-image-is-licence-free-documented-and-marked-when-a-machine-made-it) | documentation |
| [A margin is measured before it is assumed](PLUGIN-RULES-PROCESS.md#measure-before-assuming-a-margin-is-measured-before-it-is-assumed) | statistics |
| [Built assets are not committed and a release archive is built with the storefront build](PLUGIN-RULES-PROCESS.md#built-assets-are-not-committed-built-assets-are-not-committed-and-a-release-archive-is-built-with-the-storefront-build) | devops |
