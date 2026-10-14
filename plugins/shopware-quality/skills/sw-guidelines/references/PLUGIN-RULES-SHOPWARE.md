# Plugin rules: Using Shopware

## Contents

- [shopware-first-and-the-core-is-read: Use everything Shopware provides, build your own only where the core offers no way, and read the core source instead of remembering it](#shopware-first-and-the-core-is-read-use-everything-shopware-provides-build-your-own-only-where-the-core-offers-no-way-and-read-the-core-source-instead-of-remembering-it)
- [nothing-internal-from-shopware: No code that Shopware marks as internal is used, not in production code and not in tests](#nothing-internal-from-shopware-no-code-that-shopware-marks-as-internal-is-used-not-in-production-code-and-not-in-tests)
- [the-plugin-stands-alone: The plugin depends on PHP, Shopware and Symfony only, references no other plugin, copies no third-party code and ships no styling](#the-plugin-stands-alone-the-plugin-depends-on-php-shopware-and-symfony-only-references-no-other-plugin-copies-no-third-party-code-and-ships-no-styling)
- [the-plugin-is-generic: The plugin is generic and runs in any shop](#the-plugin-is-generic-the-plugin-is-generic-and-runs-in-any-shop)
- [only-what-the-supported-core-uses: The plugin builds nothing that the supported Shopware line does not use itself yet](#only-what-the-supported-core-uses-the-plugin-builds-nothing-that-the-supported-shopware-line-does-not-use-itself-yet)
- [data-access-only-through-the-dal: Data is accessed only through the DAL, SQL only in a few named places, and sync writes go through the DAL so core invalidation runs](#data-access-only-through-the-dal-data-is-accessed-only-through-the-dal-sql-only-in-a-few-named-places-and-sync-writes-go-through-the-dal-so-core-invalidation-runs)
- [state-transitions-through-api-routes: A state transition goes through an API route, never through the repository](#state-transitions-through-api-routes-a-state-transition-goes-through-an-api-route-never-through-the-repository)
- [configuration-in-system-config: Configuration lives in the system configuration with sales channel scope](#configuration-in-system-config-configuration-lives-in-the-system-configuration-with-sales-channel-scope)
- [performance-and-caching: Performance is never traded, pages stay fast and cacheable, and caches are invalidated explicitly and precisely](#performance-and-caching-performance-is-never-traded-pages-stay-fast-and-cacheable-and-caches-are-invalidated-explicitly-and-precisely)
- [parallel-run-and-legacy-migration: The plugin runs in parallel to the old plugins, parity is the acceptance criterion, and the legacy import is idempotent and reuses the settings import](#parallel-run-and-legacy-migration-the-plugin-runs-in-parallel-to-the-old-plugins-parity-is-the-acceptance-criterion-and-the-legacy-import-is-idempotent-and-reuses-the-settings-import)

## shopware-first-and-the-core-is-read: Use everything Shopware provides, build your own only where the core offers no way, and read the core source instead of remembering it

**Area:** core **Status:** accepted

### Context

Everything a plugin builds itself has to be maintained, tested and checked at every Shopware update. Whoever rebuilds core functions ends up with code that is worse than the core and deviates from it. Earlier plugins built things Shopware already can: their own Ajax interception instead of storefront events, their own snippet synchronisation, their own cookie providers instead of `CookieGroupCollectEvent`, and a custom deletion of database log entries although the core task `log_entry.cleanup` does the same.

Remembering the core API is tempting, but the memory is often wrong, and a wrong assumption about a field, an event or a fallback costs hours. A plugin often hooks into core flows at several points, for example by passing a trigger on to `AjaxModal`, relying on `FormCmsHandler` for submission, on `PseudoModalUtil` for the title and on the privacy partial for legal texts. Each of these interventions rests on an assumption about core behavior. A wrong assumption does not show up as an error message but as something that almost works.

For end-to-end tests, `@shopware-ag/acceptance-test-suite` ships its own sales channel, page objects, test data services and automatic cleanup. Much of this could also be built by hand, with the same result and permanent maintenance cost.

### Decision

**What Shopware offers is used. Something of our own is built only if there is really no other way.**

Before every new class, template and JS plugin, the core (`<shop>/vendor/shopware`) is checked for an existing solution: classes and services, DAL and entities, events and hooks, Twig templates and blocks, storefront JS plugins and helpers, administration components (`mt-*`, `sw-*`), SystemConfig, scheduled tasks, message queue, rate limiter, cache and cache invalidation, snippets, ACL. Reused are the DAL, the system configuration, the message queue, scheduled tasks, the ACL, the Flow Builder, cache invalidation and the administration components. A small plugin typically uses `SystemConfigService`, `ScheduledTask` and `ScheduledTaskHandler`, `SystemConfigChangedEvent`, Monolog and the Symfony Finder and Filesystem components.

If something of our own must be built after all, the reason is recorded in an ADR.

**The core is read, not remembered.** Before it is decided how something is done, it is looked up how the core does it. Not the documentation, not memory, but the source code, in the version the shop actually runs.

```bash
ddev exec bin/console --version
```

The source lives locally under `vendor/shopware/`. It is the yardstick, not a branch on GitHub: a link to `trunk` describes code the shop does not run. Where a link is needed, it points at the tag of the installed version, `https://github.com/shopware/shopware/tree/v<VERSION>` (for example `v6.7.14.0`), and the tag matches the installed version exactly.

- Facts about the core are checked in the vendor source of the installed version (for example 6.6) and never assumed from another version. A rule or convention from a newer line is only adopted after it has been checked against the installed core and found there.
- Before a Shopware class is used, the core source (`vendor/shopware/*`) is read.
- Assumptions about return values, constants or field names are backed by evidence, never guessed.
- The source is mentioned in code review (line, case, reason).
- The checked fact and its location go into `CONTEXT.md`, and into an ADR where it is a rule.
- The procedure is faster than the alternative: a wrong assumption costs hours, reading the source costs minutes.
- In the administration only components are allowed that the installed core itself uses (see the ADR on the administration).

**What to look up in particular:**

- the order of constructor arguments
- whether a field is nullable in this version
- the default values of feature flags
- when an event is fired, not only that it is
- how the core tests its own class of this kind

**What was looked up in the source is recorded as such**, with file and line. A claim without evidence is a guess, however certain it sounds.

**What was measured is recorded with the measurement.** A timing statement without a number is a guess, and only a stated number can be refuted later.

**Before an end-to-end test gets custom code, it is checked whether the acceptance suite can already do it.** The check goes in this order:

1. Search `node_modules/@shopware-ag/acceptance-test-suite/dist/index.d.ts` for the term. The type file is readable and complete.
2. The fixtures under `FixtureTypes`.
3. The page objects under `StorefrontPageObjects` and `AdminPageObjects`.
4. `dist/index.mjs`, if the type file does not reveal how something works.

Custom code is written only when the check found nothing, and it then carries a short comment saying what was searched for and why it did not fit.

Four fixed rules follow:

**The page comes from `StorefrontPage`, never from `page`.** Only the former knows the address of the test channel and makes sure its theme is compiled. Without a compiled theme the storefront delivers no JavaScript.

**Navigation goes through `ShopCustomer.goesTo()` with a page object of the suite**, not through self-assembled addresses.

**Test data comes from the `TestDataService`.** It registers every record for cleanup. What it cannot do is added to it instead of replaced, and whatever is created past the cleanup is removed by the test itself.

**A deviation from the suite is justified.** The suite makes assumptions about the environment, for example English labels in the master data. If an assumption does not hold, the affected fixture is overridden, with the reason in a comment. Real shop data is not changed for this.

### Consequences

Less custom code and behavior that fits the shop. The plugin follows core behavior and profits from its fixes, and it stays smaller and easier to maintain. In return it depends more closely on core structures, and a change there shows up in the integration and end-to-end tests. A small plugin can consist of just a task, a synchroniser, a subscriber and a file cleaner.

A decision takes longer, because a look into foreign code lies between question and answer. In return, drafts contain statements that can be verified instead of statements that merely sound plausible. The price is reading before writing.

At a Shopware update the source is read again. Every intervention that exists only because of a core behavior belongs, with its condition, into the `UPGRADE` files.

Before writing an end-to-end test there is a search of a few minutes that regularly saves hours. If a fixture of the suite fails, the first question is which assumption it makes about the environment, not how to replace it. The own sales channel of the suite makes the tests independent of whatever else is installed in the respective shop, which matches the claim that the plugin runs in every shop.

## nothing-internal-from-shopware: No code that Shopware marks as internal is used, not in production code and not in tests

**Area:** core **Status:** accepted

### Context

The Shopware core marks a lot with `@internal`, among others the attribute `Shopware\Core\Framework\Log\Package`, the `TaskRunner` and the method `Context::createDefaultContext`. Such classes may change or disappear in any release without counting as a break. A plugin that uses them is coupled to the Shopware version and breaks at a core update. It runs in live shops and has to survive every patch release of its Shopware line.

The `Package` attribute is such an internal marker. Its `PackageString` type lists only the core's own domain names (`inventory`, `checkout`, `framework`, and so on), so a plugin that uses its own area name has to be excused from static analysis, and the ignore block in `phpstan.neon` existed for exactly that. The attribute is read at runtime only narrowly: `PackageService` consults it for controllers and exceptions, to label traces and error reports, and a plugin that ships neither is not affected.

PhpStorm reports every use of internal classes, also in tests, and the rule that every PhpStorm inspection is resolved applies to `src` and `tests`.

### Decision

- **No `@internal` API of the core is used, neither in production code nor in tests.** This is the newest and strictest form of the rule. Where one would genuinely be the only way, there is no exception: the plugin builds a small class of its own instead.
- Only the public, documented extension points are used: the DAL, the Store API, the Admin API, events, Twig blocks, the API for administration modules, the storefront plugin system, the message queue and scheduled tasks.
- Classes and methods marked `@internal` are not referenced, even if that is shorter to write. A migration of a plugin from a newer line applies the same rule, a new use of a deprecated core element is listed in `docs/DEPRECATIONS.md` in the same commit.
- **The plugin ships its own attribute `<Plugin>\Framework\Log\Package`**, in `src/Framework/Log/Package.php`, instead of the internal core attribute, and every class carries `#[Package('<Plugin>.<Area>')]` from it. It behaves like the one of the core, only without the restriction of allowed names, which is the sole reason for the copy.
- **A phpat rule enforces this for production code.** The build gate fails as soon as a class depends on `Shopware\Core\Framework\Log`. The rule selects the core attribute by regular expression, so that the test itself does not name the internal class. The rule file is maintained together with the architecture tests.
- php-cs-fixer orders the attribute first among the attributes. Every class imports it from the plugin's own `Framework\Log` namespace.
- **Tests use public paths:**
  - `SystemConfigChangedEvent` is created as a PHPUnit stub instead of being constructed.
  - `Context::createCLIContext` is used instead of the internal `createDefaultContext`.
  - Repositories come through `DefinitionInstanceRegistry` instead of string service IDs, which PhpStorm cannot resolve.
  - Parity tests against the internal core attribute `Package` are dropped.
- **A command invokes a core task through the public console command `scheduled-task:run-single`**, not through the internal `TaskRunner`.
- **Migrations and the uninstallation use the public building blocks of Shopware.** An own database trait is not built, and `TableHelper` stays off limits because it is internal. A previous own `DatabaseTrait` was built on the Doctrine schema manager, whose methods `listTableColumns()` and `listTableForeignKeys()` are deprecated for DBAL 5 and thus for Shopware 6.8, so it was exactly what it should avoid: code that breaks at the next update. The maintainer decided: we do what Shopware does.

| Need | Building block |
|---|---|
| Column exists? | `Shopware\Core\Framework\Migration\ColumnExistsTrait` |
| Create a column | `AddColumnTrait` or `ALTER TABLE` as in the core migrations |
| Inheritance column | `InheritanceUpdaterTrait::updateInheritance()` |
| Remove a column, foreign key, table, index | `MigrationStep::dropColumnIfExists()`, `dropForeignKeyIfExists()`, `dropTableIfExists()`, `indexExists()` |
| Uninstallation | `DROP TABLE IF EXISTS` and `ALTER TABLE ... DROP COLUMN` behind `columnExists()` |

- **The plugin targets a defined Shopware line only**, for example 6.7. `composer.json` sets `conflict` to `<6.7 || >=6.8` for core, storefront and administration, and PHP from 8.3. The code uses no deprecated API, so it runs unchanged on the next line.
- **A cookie provider is extended through the public event**, not by decorating `CookieProviderInterface` (deprecated since 6.7, removed in 6.8). `CookieGroupCollectEvent` is the public extension point for cookie registration.
- **Before a new dependency is added, the core is read**, not guessed.

> Earlier variant: older versions of this rule excluded tests, kept a parity test (`PackageTest`) asserting that the own `Package` attribute equals the core attribute in constant, method signature, attribute target and parent class lookup (`$tryParentClass`) so that a divergence would fail the gate, and a named exception allowed reading the payloads of `WriteCommand`s in a write validator (limited to `WriteSnapshotLoader` and listed in `UPGRADE-6.8.md`). Some versions placed the attribute in `src/Core/Framework/Log/Package.php` to mirror the core layout `Core/Framework`.

### Consequences

The plugin and its tests stay runnable at core updates within the targeted line and are not bound to a patch version. A move to the next line is a deliberate task with its own check. A test that used to build an internal type now needs a stub or a public access.

One more class exists in the plugin that replicates a core behavior, and a second `Package` attribute exists in the codebase. Reading a class, one has to notice which is imported, and the namespace makes it plain. In return there is no exception in static analysis and no dependency that may change in a patch version. Core tools that read their own attribute do not see ours, which is accepted. The core reads its attribute only for controllers and exceptions via the `PackageService`, so this has no effect for a plugin that ships neither. If the plugin ever gains one, this decision is revisited rather than worked around.

If Shopware changes its own `Package`, ours does not follow automatically, which is accepted. Because the substitute is a copy of a documented behavior and not a use of the internal class, this causes no break.

If Shopware changes its migration traits, the migrations follow automatically. `ColumnExistsTrait` throws in 6.7 for a missing table, so migrations only query tables that an earlier migration created.

Code that used to read internal structures, such as a write validator, is the class most likely to break at an update. Integration tests write through the real DAL, so a changed payload shape shows up there first.

## the-plugin-stands-alone: The plugin depends on PHP, Shopware and Symfony only, references no other plugin, copies no third-party code and ships no styling

**Area:** core **Status:** accepted

### Context

Plugins can call each other in Shopware. A plugin that requires another one is tied to it, and updating, deactivating and uninstalling become complicated. The plugin is installed in many shops with different themes and extensions. A dependency on another plugin, a theme, a vendor service or a library makes installation, updates and removal dependent on something the plugin does not control. A default or a text that is bound to one shop or theme is wrong in every other shop.

A reference to another plugin in code, configuration, documents or tests binds the plugin to something other shops do not have and reveals internal project history.

A shop often already brings everything a feature needs: a newsletter form in its own plugin, its design in the theme, a hook point in its `base.html.twig`. Reusing all that is the shortest path and yields a plugin that cannot be installed anywhere else: without these neighbors it renders an unstyled form or nothing.

There are third-party connectors and example plugins. They are proprietary or carry licenses with conditions, and copying from them would expose the plugin and its customers to license claims. An old connector that the plugin replaces is such a case.

### Decision

**The plugin depends on Shopware and on nothing else.**

- `composer.json` requires `php` (from 8.3) and the Shopware packages through `conflict` ranges. No other plugin, no third-party library, no vendor service. Development tools appear only in `require-dev`.
- Direct dependencies are only the Shopware core and Symfony.
- No class of another plugin is imported, and none is probed with `class_exists` or similar. Whether an old plugin is active is read exclusively by a `LegacyPluginDetector` from the core plugin repository. Foreign classes are never imported.
- **No `conflict` in `composer.json` towards the old plugins.** They must be able to run in parallel for a migration (see the ADR on parallel run).
- No file names another plugin, a plugin path or a Composer vendor other than the plugin's own. Payment integrations and similar are recognised through their public interfaces or technical identifiers defined by Shopware, never through the name of a third-party plugin.
- The only exception is data of a legacy connector that has to stay compatible. Its technical identifiers appear only in `src/Service/Legacy` and `src/Service/Installer` with their tests and fixtures. Everywhere else it is called "the legacy connector".
- The plugin names no other development plugins and no local paths, except the old plugins of a migration.
- No theme dependency. No default, text or template is bound to a shop or theme. Shop specific content is configuration or data that the operator enters.
- No license server, no phone home, no plan limits. Credentials of an external system are entered in the plugin configuration.
- **No styling in the plugin.** It sets a dedicated class such as `newsletter-modal-dialog` on its modal and assigns its own class names for its markup. The look is the responsibility of the theme. A theme that styles none of it still gets a usable modal, because the core design then applies. It then does not look like the shop, which is the right failure.

| Allowed | Not allowed |
|---|---|
| Extending and including `@Storefront/...` templates | Including templates of other plugins |
| Using core services and routes | Referencing PHP classes of other plugins |
| Own templates, snippets, JavaScript | SCSS, CSS, inline styles |

- **Enforced, not just written down.** A phpat rule allows dependencies only on the plugin itself, Shopware, Symfony, PHP and the plugin's own Composer packages: the plugin namespace must not depend on other namespaces that belong to sibling plugins. The rule file is maintained together with the architecture tests (`tests/Architecture/LayerTest.php` or phpat). A template test checks that no Twig file uses a foreign namespace and that no stylesheet lies in the plugin. `CodingStyleTest` fails on foreign plugin names and foreign vendors.

**Third-party plugins, the old connector and the example plugins of an external system are only read to learn which functions are expected.**

- No code, identifier, template, snippet text, config key, table name and no database layout is copied from them.
- Everything is derived from the documentation of the external system, from Shopware and from the plugin's own design.
- Exception: identifiers that must stay identical for data continuity when switching from the old connector (names and IDs of custom fields, old table names that the import reads, technical names of document types and mail templates, names of flow events). They appear only in `src/Service/Legacy` and `src/Service/Installer`.
- The license of this plugin stays `proprietary`.

### Consequences

The plugin installs, works and can be removed again without other plugins suffering. It can be installed, run and uninstalled in every shop of its Shopware line without side effects on other plugins. Shopware updates are independent. It can be read, shipped and tested without knowing anything else in a shop. Needs that would pull in a library are solved with the platform or with small classes of its own.

The origin of every part of the code can be named. The scope of functions is measured against behavior, not against similarity of implementation.

The newsletter form can exist twice in one shop, in the plugin and in a shop owned plugin. The double maintenance is the price of this rule. The two forms will drift apart, a change to the shop owned box does not reach this plugin by itself and has to be carried over if it applies to the modal as well. Styling the modal requires work in two repositories: markup in the plugin, look in the theme.

## the-plugin-is-generic: The plugin is generic and runs in any shop

**Area:** core **Status:** accepted

### Context

The plugin was first built for a single shop. Values of that shop in code, tests or documents would be wrong or even harmful in every other shop.

### Decision

- No shop names, domains, absolute local paths, local database values, sales channel IDs, theme names or counts in code, tests, fixtures, configuration or documents.
- Paths in documents use the generic form, for example `<shop>/vendor/shopware/administration/Resources/app/administration/src`. A ddev command is only an example setup.
- Behavior that depends on the shop is configuration or is detected at runtime (for example by looking up an ID by name first and keeping an existing one).
- Built in defaults that serve compatibility with the legacy connector are constants in `src/Service/Installer`, and the installer keeps every ID the shop already has.
- `CodingStyleTest` fails on absolute local paths and development hosts.

### Consequences

A second shop needs no code change. Shop specific knowledge stays in the shop and in `CONTEXT.md`, which is excluded from the checks.

## only-what-the-supported-core-uses: The plugin builds nothing that the supported Shopware line does not use itself yet

**Area:** core **Status:** accepted

### Context

The client formulated the rule like this: no functions are created that Shopware itself does not use yet. Functions and conventions of later Shopware lines (for example field descriptions on DAL fields, which come with 6.7) tempt a plugin to build its own substitute. Such a substitute has to be maintained, deviates from the real feature and has to be removed at the upgrade.

### Decision

- The plugin builds no own substitute, no polyfill and no backport of a Shopware feature that exists only in a later line.
- A rule or convention from a newer Shopware line is adopted only after it has been checked against the installed 6.6 core and found there.
- The plugin uses only what the 6.6 core itself uses. This covers PHP APIs, DAL features, events, Twig blocks and storefront mechanisms as well as administration components and icons (see the ADR on the administration).
- Where a later line brings a feature, the switch is listed in `docs/UPGRADE-6.7.md` and carried out when the plugin moves to that line.

### Consequences

The plugin stays small and close to the core, and nothing has to be removed at the upgrade. Some conveniences of newer lines are missing in 6.6 until then.

## data-access-only-through-the-dal: Data is accessed only through the DAL, SQL only in a few named places, and sync writes go through the DAL so core invalidation runs

**Area:** data **Status:** accepted

### Context

Raw SQL bypasses entity events, inheritance, translations, versioning, write protection and the cache invalidation and indexing attached to them. A synchronisation that writes products and orders must trigger the same consequences as an edit in the administration. The core invalidates cached pages and starts indexers as a consequence of DAL writes, and writes that bypass the DAL leave stale pages and stale indexes.

Two persistence routes exist in a Shopware plugin: the Data Abstraction Layer with `EntityDefinition` classes, or plain Doctrine DBAL tables managed by the plugin itself. One plugin specification listed roughly 23 entities, stated explicitly that custom fields alone are insufficient, and required entity extensions on `product` and `order`, so that its data is reachable as `product.extensions.<name>` and `order.extensions.<name>`.

DBAL is faster to write for a single table and faster at runtime for bulk operations. But everything the specification asks for beyond raw storage is DAL infrastructure: Admin API endpoints, `Criteria` searches with filters and aggregations, ACL roles, entity extensions on core entities, versioning, the administration data grids. Choosing DBAL means reimplementing each of those by hand. This decision is effectively irreversible, because the 23 entities and every consumer of them would have to be rewritten.

The sync writes products, stock, prices and categories to Shopware.

### Decision

- Reading and writing go through `EntityRepository` with `Criteria`, or for external clients through the Store API and the Admin API.
- All entities are `EntityDefinition` classes in the Shopware DAL, following core conventions verified against `vendor/shopware/core`:
  - classic `defineFields()`, no attribute based field definitions
  - an `ENTITY_NAME` constant as the single source of truth for the table name, the collection alias and foreign key names
  - the `ApiAware` flag on every field that may be exposed
  - `SearchRanking` on meaningful text fields
  - a short, plugin specific table prefix
- Entity extensions on `product` and `order` connect the plugin data to core entities.
- `Doctrine\DBAL\Connection` is used only in `src/Migration`, in the plugin class (uninstallation), in `src/Service/Installer` and in `src/Service/Legacy`, where legacy tables are read in bulk for the import.
- A phpat rule forbids `Connection` everywhere else. The rule file is maintained together with the architecture tests.
- Complex reads are expressed as `Criteria` plus associations and are tested in integration tests against a real kernel.
- Where a hot path later proves too slow through the DAL, an isolated DBAL query is permissible, but as a measured exception with a note in the ADR, never as the default.
- Every sync write goes through the DAL, so the core indexers run and the core cache invalidation applies.
- No own cache invalidation is added for core entities, because the core takes care of it.
- The invalidation of product pages through the core event `InvalidateProductCache` applies only if plugin data appears on cached pages. If that is the case, the plugin fires this event after writing for the affected product IDs. Today no plugin data is rendered into cached pages.
- Mass writes are split into chunks, so that a request does not hold a huge payload.

### Consequences

Plugin data is cached, indexed and invalidated consistently with the core data. The named exceptions are the places where SQL is the better tool (schema changes, one time imports, removal).

Admin API, ACL, Criteria, administration grids and entity extensions all work without extra code, and the plugin behaves like core code to other plugins. More boilerplate is needed per entity (definition, entity, collection, plus translation aggregates where needed), and DAL bulk writes need the sync API for large imports.

The table prefix is short, which keeps composite names such as `<prefix>_supplier_order_line_item` well inside the MySQL limit of 64 characters for identifiers once translation and foreign key suffixes are appended.

A synchronised change is visible in the storefront without manually clearing the cache. The sync inherits the cost of core indexing, which is why heavy runs belong in the queue.

## state-transitions-through-api-routes: A state transition goes through an API route, never through the repository

**Area:** core **Status:** accepted

### Context

The administration writes through `repositoryFactory` by default, and that is right for an ordinary entity save: a form edits fields, the DAL validates them, no rule is at stake. Three pages went further and wrote a decided state the same way:

- a review task detail page set `status`, `resolvedBy` and `resolvedAt`
- a supplier return detail page set the status and the matching timestamp
- both webhook event pages set `status = 'received'` and cleared `lastError`

Each had a rule behind it. `ReviewQueue::decide()` refuses a task that is already final, `ReturnService::advance()` refuses a transition the state machine forbids, and `WebhookEventStatus::allowsRetry()` says which events may be retried. None of those rules ran: the browser checked an equivalent in JavaScript and then wrote the row directly. A request built by hand walked past all three.

Two of them were worse than a missing guard. The review task took `resolvedBy` from the session and a test recorded `null` as acceptable, so the record of who decided was whatever the client chose to send. The webhook retry set the status and raised "The event was queued for processing again" without dispatching a message at all. The handler never ran, and the merchant was told something that was not true.

### Decision

**A write that carries a rule goes through an API route in `src/Controller/Api/`.** The controller calls the service that already owns the rule, and the administration talks to it through an `ApiService` in the module's `service/` directory.

- The route declares `_acl`, so the permission is enforced by Shopware rather than by the page hiding a button.
- The client sends only what it knows: an id, and a target where there is a choice. Never a timestamp, never a user id, never a status the server can derive.
- A refused write answers 409, a malformed one 400, and the page reloads either way.
- `repositoryFactory` stays the right tool for an ordinary entity save with no rule attached.

### Consequences

- Three controllers exist: `ReviewTaskController`, `SupplierReturnController` and `WebhookEventController`. A fourth is needed the moment another page writes a state.
- The guards are testable where they live. `ReturnServiceTest` keeps the promise about timestamps that six Jest tests used to duplicate.
- The administration carries slightly more indirection: a service file, a registration, an injection. That is the price of the rule being enforced once rather than twice.
- `RETRYABLE_STATES` and `ALLOWED_TRANSITIONS` stay in the pages, but only to decide what to offer. They are no longer what makes a write safe.

## configuration-in-system-config: Configuration lives in the system configuration with sales channel scope

**Area:** api **Status:** accepted

### Context

Merchants enter credentials and settings in the plugin configuration. Several values (client, referrer, prices, order options) differ per sales channel.

### Decision

- All settings are keys of the plugin's own domain (`<PluginName>.config.`), defined in `config.xml` (texts for de-DE and en-GB, no shop specific defaults).
- `ConnectorConfig` is the only reader. It offers one method per key, typed defaults and group objects (`ConnectionSettings`, `WriteSettings`, `ClientSettings`, `ProductSettings`, `OrderSettings`, `SyncSettings`, `LogSettings`). Key names exist once in `ConfigKeys`.
- Reads take an optional sales channel ID and inherit from the global value. Connection, write protection, sync and log settings are read globally.
- Switches to enable a type and schedules are not configuration. They live in the sync state table.
- Lists are comma separated text, additional price rules are a JSON list, invalid values fall back to defaults and never throw.

### Consequences

A new setting is an XML field, a constant and a method. Other classes never use magic key strings.

## performance-and-caching: Performance is never traded, pages stay fast and cacheable, and caches are invalidated explicitly and precisely

**Area:** core **Status:** accepted

### Context

Anything a plugin adds to a storefront page multiplies with listings and traffic. One query per product box turns a listing of 48 products into 48 additional queries, and visitor specific HTML breaks the HTTP cache. A tracking plugin quickly costs speed through extra requests, uncacheable HTML and JavaScript on every visit, and the counterweight is its benefit.

Lookups for mappings, languages, currencies and clients run thousands of times per sync page. They must be fast and must never deliver data that was changed in the administration or by another process. Every sync page writes several sync log rows and updates its run. A subscriber used to invalidate a cache tag for each of these writes although nothing caches log rows or runs: the administration reads them on every request through the DAL.

The HTTP cache of Shopware stores product pages and CMS pages with tags for the core entities: product, category, CMS page. When one of these entities changes, the core empties exactly the affected pages. It does not know the entities of a plugin. If a merchant changes a surcharge, a rule, a translation or an assignment, the buyer sees the old configurator until the entry expires (default two hours) or someone empties the whole cache. The cart always recalculates, but then the price in the buy box differs from the price in the cart. Emptying the whole cache on every change makes every page render again in a live shop, including pages without a configurator.

The realtime checkout calls of one plugin make the checkout depend entirely on cached data, which turns the cache from an optimisation into load bearing infrastructure. The plugin specification lists the cache candidates and suggests TTL defaults:

```text
Catalog          24 h
Price            15 min
Stock             5 min
Shipping Quote    5 min
Availability      2 min
```

The specification also states that the TTL must be configurable per provider, because suppliers differ widely in how fast their stock moves and how tolerant their rate limits are.

Two placements were considered. Storing cached values on the DAL entities themselves makes everything visible in the administration and queryable via `Criteria`, but every cache read becomes a database round trip, which is the opposite of what a checkout path needs. A dedicated cache pool keeps reads fast and lets tag based invalidation react to webhooks.

### Decision

**Pages stay fast and cacheable:**

- No additional request per page view for normal visitors. The output is rendered on the server.
- No call to an external system in a storefront request.
- Data for a page full of entries is loaded in one batch per page and attached as an extension, never per entry.
- Only the associations that are needed are added to a `Criteria`.
- Nothing visitor specific in cached HTML. The output of the plugin depends only on the entity, the sales channel and the language. User and cart come from AJAX or cookies.
- Heavy work runs only in the console, in the message queue or as a scheduled task (translation, import, consent log cleanup, server events), never in a storefront request.
- A consent runtime is inlined, and the script is below 3 KB minified.
- Channel configuration is cached with cache tags and invalidated on save (including the HTTP cache).
- A consent log is written only through `sendBeacon` when the user decides, not on every page view.
- A script blocking rewrite runs once per cache entry, with a fast pre check before parsing.

**Per request state and explicit invalidation:**

- The mapping store, the language and currency lookups and the sync settings hold per request memory only. They implement `ResetInterface` and are tagged with `kernel.reset`, so workers start every message empty.
- `CacheInvalidationSubscriber` listens to `EntityWrittenContainerEvent`. Mapping writes reset the mapping store (not if the write comes from a sync, because the store updates itself) and invalidate the tags `<prefix>-mapping` and `<prefix>-mapping-<entity_name>`. Writes of the other low volume plugin entities (sync state, unassignable rows, media queue, webhook events) invalidate `<prefix>-<entity>`. Writes of the sync log and sync run entities invalidate nothing. Writes of language, locale, currency and sales channel reset their lookups. Tags go through the public core `CacheInvalidator`.
- Every persistent cache added later tags its entries with the names from `CacheTags` and is invalidated without further code. A cache for log rows or runs would need its own invalidation and a change to this decision.
- The live option lists of the administration are kept in the browser only for 60 seconds and expire.
- `ConnectionConfigSubscriber` discards the cached access token of the old URL and old user name through `TokenStore::forget()` before a credential key changes, and the token of the new pair after the change. The connection test with typed values neither reads nor writes the token cache.
- Core entities written by syncs rely on the core invalidation, because every write goes through the DAL.

**A change to a configurator empties only the pages that show one:**

- Every page that can show a configurator carries a plugin specific tag, set through `CacheTagCollector`:
  - on every product page (in a pagelet loaded subscriber), even if no configurator is assigned to the product yet, so that a new assignment reaches the page
  - on every inquiry element of a CMS page (in the element resolver), even before a configurator is chosen
- Every write and delete of one of the seven plugin entities invalidates exactly this tag (a cache invalidation subscriber in `src/Subscriber/`): configurator, group, option, their three translations and the assignment. The list of entities is a constant on the plugin class, the same one the uninstallation uses, and a test checks every event from it.
- The invalidation is forced, not queued (`invalidate([TAG], true)`). Queued tags are awaited by Shopware until the scheduled task processes them, and until then the merchant would still see the old state after saving.
- A failure while invalidating does not abort the save. It is logged in the plugin's log channel with the exception, and the pages then update when their entry expires.
- The same approach is used in other plugins that tag listing pages.

**Caching of external provider data:**

- A Symfony cache pool with its own namespace holds availability, prices, stock, shipping quotes and catalog data.
- TTL defaults follow the table above and are overridable per supplier in the administration.
- Cache entries carry tags (`supplier-<id>`, `offer-<id>`, `product-<id>`), so a webhook event invalidates precisely what changed rather than flushing broadly.
- Every cached value stores the timestamp it was fetched at, so staleness is a property of the data and stale data policies can be applied consistently.
- Authoritative state stays in the DAL. The cache is derived and may be dropped at any time without data loss.

### Consequences

- The plugin costs visitors no speed, and performance audits do not fail because of it. It changes the number of queries per page at most by a constant, which an integration test proves where the plugin adds storefront data.
- No stale mapping survives a change in the administration. A sync page causes no cache invalidation for its log rows and its run. A change of credentials costs a new login.
- A change to the configurator is visible in the shop immediately after saving. All product pages and pages with an inquiry element are emptied, not only those of the changed configurator. This is deliberately coarse: which products a configurator reaches through dynamic product groups cannot be determined cheaply at save time. Pages without a configurator relation, such as categories and the home page, stay in the cache.
- Cart, checkout, mails and documents need no tag: they do not land in the HTTP cache and read the stored snapshot.
- `CacheTagCollector` and `CacheInvalidator` are public classes. Only their constructors are `@internal`, and the plugin does not build them itself.
- The test configuration of Shopware turns off the delayed invalidation (`delay_enabled: false`). Whether `force` is set is therefore proven by the unit test, and the integration tests prove the wiring through a tagged entry in `cache.object`.
- Checkout reads are fast and independent of supplier APIs, invalidation is precise, and the cache can be cleared wholesale without consequence.
- Cached values are not visible in the administration by default. The supplier detail view must therefore expose "last fetched at" and a manual refresh, otherwise support cannot tell stale data from wrong data.
- Cache misses fall back to the last known value in the DAL rather than to a live provider call. A live call in a request path would reintroduce exactly what the decision on realtime checkout calls forbids.

## parallel-run-and-legacy-migration: The plugin runs in parallel to the old plugins, parity is the acceptance criterion, and the legacy import is idempotent and reuses the settings import

**Area:** core **Status:** accepted

### Context

A plugin replaces several old plugins. The data takeover reads the tables and settings of the old plugins, and the merchant checks the result before switching over. This only works if all plugins can be installed and active at the same time. A comparison of all identifiers showed that the only hard collision was a `conflict` in `composer.json`. In behavior, duplicate Google entries in the banner, doubly loaded GTM, contradicting consent updates and doubly counted purchases are at risk.

What the old plugins can do together, the new plugin must do.

Shops that use the old plugins or the Google Analytics of Shopware should be able to take over their data without manual work. The plugin already has a checked settings import (JSON from the export) that writes groups, services, cookies and settings transactionally and does not create cookies twice.

The import can be started again after the old connector has kept running, after a failed batch or after a changed mapping rule. A second run must not duplicate anything and must never overwrite what the new plugin has written in the meantime.

The old connector kept a connection row with a JSON configuration. The new plugin keeps its settings in the system config with sales channel scope. The old row also contains an encrypted password, an access token and license data. Its product mapping profile decided which of the three article names of the external system became the product name, and shops that took the name from `name2` would get different product names after the switch if only the profile were archived.

### Decision

**Parallel operation:**

- **No `conflict`** towards the old plugins in `composer.json`.
- **Unique prefixes** for every identifier (tables, administration modules, components, snippets, routes, Twig functions, CSS classes, data attributes, JS plugins, globals, config domain, commands, log channel), in the forms snake case, kebab case, camel case, `<Prefix>` for JS globals and `data-<prefix>-` for data attributes. Names of the old plugins (their own prefixes and `cookie-list`) are never used. Before every new naming it is checked against the old plugins.
- **`LegacyPluginDetector`** reads from the core plugin repository whether an old plugin is active. Foreign classes are never imported.
- **One responsibility per sales channel** (`trackingResponsibility`): as long as the old plugin is responsible, the new plugin outputs no GTM, no gtag, no ecommerce events and no server events. After switching, the reverse applies.
- **Bridge for consent:** if the visitor grants or revokes a Google service, the new plugin also sets or deletes the cookies the old plugins listen to (`google-analytics-enabled`, `google-ads-enabled` and the tag manager cookie).
- **No duplicates in the banner:** a Google entry that the old plugin has already registered in a core group is not created twice. A complementary decision on legacy Google cookies shared between plugins covers sharing cookies instead of duplicates and switching off the old plugin's scripts.
- **Script blocking** leaves the script IDs of the old plugin untouched as long as it is responsible.
- The administration overview shows a migration hint with the recommended order.

**Parity is the acceptance criterion:**

- The parity list is in section 2 of `TODO.md` with 25 features in total.
- From the first old plugin (W1 to W18): everything except W11 (external CMP adapters, dropped by the user).
- From the second old plugin (F1 to F10): everything.
- **Every line of the list is an acceptance criterion.** It is verified in the browser, not in code.
- At the end of the implementation, every line is green or documents why not.

**Legacy import reuses the settings import:**

- Every source (`LegacySourceInterface`, tag `<prefix>.legacy_source`) reads the old data directly from the database and converts it into the format of the settings export. Writing happens exclusively through the existing `SettingsImporter`. There is no second write path.
- The dry run converts and checks with the `SettingsPayloadValidator` but writes nothing. It shows a report with counts and every hint. The takeover starts only afterwards, through a dedicated button or the `import-legacy` console command without `--dry-run`.
- Existing data of the plugin always wins: settings are only filled if they are empty. An existing service keeps its values and only receives missing cookies. An old service belongs to the service that already knows most of its cookies, so Google services, for example, are not created twice.
- Data protection comes first: the consent mode always starts with Basic, and consent mode types that were pre allowed in the old plugin are not taken over. Both are noted in the report for review. The tracking responsibility is not switched.
- Free text is cleaned up: lifetimes are split into value and unit (unclear statements become session, with a hint), groups of the same name are merged, the option "refresh" is dropped, and `is_cmp` becomes consent mode types via the category of the Open Cookie Database. Missing translations are added afterwards by DeepL in the background.
- The report delivers codes with parameters. The administration translates them through snippets, the console shows English texts.

**Idempotent import of connector data, existing data wins:**

- Every written row gets a deterministic ID derived from a fixed prefix, the kind and the old key (`LegacyIds::of`). Mappings use the old table plus the complete identity of the row, history rows use the old history ID, sync states use the sync type.
- Before writing, a batch checks which of its IDs exist. Existing rows are counted as unchanged and never updated.
- A sync state row is the only exception. A row that exists but has no cursor, no last run and no run ID (an untouched default) is filled with the old cursor. Every state that has already run stays untouched.
- System config keys are written only if the current value is empty (null, empty string, zero, false or empty list), so settings entered in the new plugin take precedence.
- A dry run takes the same path and computes the number of created and unchanged rows without writing a row, a config value or a log note.
- Incomplete rows (missing IDs) are skipped and logged, never half written.

**Legacy settings and the product name source become system config, credentials stay behind:**

- The connection host becomes the `url` (always `https`), the user name becomes `username`. The password and the access token are never read by the import, so they cannot end up in logs or in the config.
- A pure converter turns the JSON configuration into system config keys of the plugin: price IDs, additional price rules, barcode, warehouse, product layout, switches for properties and variations, the external system's ID per client, referrer and default flag (stored per sales channel), the order status groups, the order import status and the referrers, the discount handling and the default campaign number.
- A sales channel that no longer exists is skipped and logged. No value, ID or name of a shop is hard coded in the plugin.
- License data, the main client ID, the switches of the migration aid and the document keys have no counterpart. They are reported in the log as not migrated with the message key `legacySettingSkipped` and the reason.
- The old mapping profile as a whole has no counterpart, because its job is taken over by the mapper registries. Its mapping and configuration are archived once as a note row (`legacyMappingProfileArchived`), so the merchant can compare the actual behavior.
- The active system default profile of the target `product` sets `productNameField` from `mapping.mainTranslation.name.key` (`name` or `name1` becomes `name`, `name2` and `name3` stay, a dotted path counts by its last segment). The value is written only globally and only while the setting is empty or still the default `name`, a different choice of the merchant is kept. Other keys of the profile are not interpreted.

### Consequences

The migration can happen step by step and reversibly per sales channel. When the old plugins are deactivated, the bridge paths no longer run and cost nothing. They are removed in a later major version.

The plugin is not finished until it can do everything both predecessors could. It does not replace, it does not degrade.

The takeover can be repeated as often as wished, and a second run creates nothing twice. Running the import twice changes nothing in the second run. New sources are just another class with the tag. The old tables and settings stay unchanged until the old plugin is uninstalled.

A dry run is a faithful prediction of the first real run, except for collisions with unique keys, which only show up at write time. Corrections to old data after the first import are not taken over. They require a manual change in the new plugin.

The merchant enters the password again and tests the connection. This step is part of the runbook. Nothing of the old license or of plan limits is taken over. Products keep the name source they had with the old connector.

The conversion is covered per rule by a unit test, so a changed old shape makes a test fail instead of writing a wrong value.
