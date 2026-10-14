# Plugin rules: Data and plugin lifecycle

## Contents

- [uninstall-removes-plugin-data-only-when-asked: Uninstall removes plugin data only when asked and always keeps shop data](#uninstall-removes-plugin-data-only-when-asked-uninstall-removes-plugin-data-only-when-asked-and-always-keeps-shop-data)
- [migrations-are-additive-and-live-shops-decide: Migrations are additive and idempotent, and live shops decide what may change](#migrations-are-additive-and-live-shops-decide-migrations-are-additive-and-idempotent-and-live-shops-decide-what-may-change)
- [deleting-referenced-data-cleans-up: Deleting data that others reference cleans up every reference](#deleting-referenced-data-cleans-up-deleting-data-that-others-reference-cleans-up-every-reference)
- [default-data-in-the-lifecycle: Default data is created in the plugin lifecycle and large imports run in the message queue](#default-data-in-the-lifecycle-default-data-is-created-in-the-plugin-lifecycle-and-large-imports-run-in-the-message-queue)
- [configuration-sync-on-activation: Synchronization runs on activate and update, not on install](#configuration-sync-on-activation-synchronization-runs-on-activate-and-update-not-on-install)

## uninstall-removes-plugin-data-only-when-asked: Uninstall removes plugin data only when asked and always keeps shop data

**Area:** data **Status:** accepted

### Context

An uninstall that removes data by default destroys sync history the merchant may still need. An uninstall that leaves remnants behind or stops halfway leaves a shop in a state nobody can repair from the administration. The sync log contains personal data that must not outlive its purpose.

### Decision

- The flag `keepUserData` decides. When it is set, nothing is removed.
- Without the flag the plugin removes in a fixed order: its sync and log data, its mapping and configuration rows, then its own tables `<prefix>_*` with `DROP TABLE IF EXISTS` and the system config keys `<PluginName>.config.`.
- The logs are removed as well (see the ADR on personal data).
- Always kept, because they are shop data: legacy custom fields and custom field sets, document types, mail template types, number ranges, the tag and media in shop folders.
- Every step is guarded and logged with exception class and code. A failing step never stops the others.
- Raw SQL in the uninstall is a documented exception to the DAL ADR.

### Consequences

A clean uninstall leaves the shop as it was before, except for the data that belongs to the merchant. A reinstall finds the shared data again.

## migrations-are-additive-and-live-shops-decide: Migrations are additive and idempotent, and live shops decide what may change

**Area:** data **Status:** accepted

### Context

Migrations run on live shops in unknown states and can run again after a failed update. Live shops hold data that the sync and the operators created, so they decide what may change. A changed migration timestamp makes a migration run again, and a destructive schema change destroys data.

Merchants run a released version with objects they built by hand: for example configurators with groups, options, prices, visibility conditions, assignments to products and dynamic product groups, and orders whose line items carry the configuration as a payload. The next minor version changes the rule model, adds fields and corrects wrong prices. None of the existing data is ours to break.

A second case: a plugin runs in several live shops and an earlier decision drew the line between what a release may change and what it must leave alone, ruling out any migration in that release. Before the release was published, merchants asked for a tile that carries text only. Until then every tile reserved an image area: without an image it showed the placeholder icon, and the text box shared the tile with it. There was no way to say "no image here" other than removing the image, and that still left the placeholder. Saying so needs a switch, and a switch that survives a save needs a column. The release candidate tag existed, the release did not, so the change went into that release.

### Decision

- A published migration is never changed. A schema change gets a new migration. Existing migrations and their timestamps are never touched, because a changed timestamp makes every shop run the migration again.
- Schema changes are additive. Columns and tables are neither removed nor renamed in a minor or patch release.
- Tables are created with `CREATE TABLE IF NOT EXISTS`, utf8mb4, InnoDB and `DATETIME(3)` timestamps. Later changes check whether the column or index exists before adding it.
- Every migration is idempotent and can safely run again. JSON columns carry a `JSON_VALID` check.
- `updateDestructive()` stays empty, and a migration deletes nothing unless an ADR decides otherwise.
- Stored data keeps its meaning. A new enum value extends a list and never reinterprets an old value.
- Stored data stays valid. A visibility condition written by the earlier version (`{"operator": "AND", "conditions": [{"optionId": "...", "operator": "selected"}]}`) means the same in the new version. New operators extend the model and never reinterpret the old one.
- Order payloads are history. A configuration stored on an order line item is never recalculated or rewritten. Documents and mails show what is stored.
- Behaviour changes only where the behaviour was the defect, and then it is listed in the changelog under `Fixed`. Examples: two closures that cost as much as one, a drag and drop order that was not saved, a JavaScript validation that contradicted the server.
- A release may add exactly one migration, and it only adds. In the example above the migration adds `use_media TINYINT(1) NOT NULL DEFAULT 1` to the tile table. It checks that the column is missing before it adds it, so a second run changes nothing. It removes, renames and retypes nothing, and `updateDestructive()` is empty.
- The default of such a column keeps the old behaviour, so no live shop sees a difference. Every tile that exists when a shop updates keeps its image area exactly as before. Only a merchant who switches it off gets a text-only tile. The DAL default and the create page both say `true` for the same reason.
- Everything else the replaced decision said still holds:
  - the initial table migration is never touched, its timestamp least of all
  - DAL modernisation beyond the new column is metadata only
  - behaviour changes only where the behaviour was the defect, and the changelog names it
  - everything else is proven unchanged by the acceptance tests
  - a change that only tidies is not made
- A further schema change is its own migration and its own ADR, never a change to an existing migration.

### Consequences

An update never loses data, and running a migration again is safe. Removing a column needs its own ADR and a major version.

A merchant who relied on a defect notices the correction. The changelog says so, because a merchant whose prices change should know why.

If a destructive schema change becomes unavoidable later, it gets its own ADR and its own major version.

A shop updating to the release runs one migration. On a large table the `ALTER TABLE` is still cheap when the table holds only a handful of rows per shop.

Switching the image off leaves the assigned image in place. Switching it back on restores the tile as it was, and nothing is lost by trying the switch.

The two `dal:validate` findings the replaced decision recorded stay open for the same reason as before.

## deleting-referenced-data-cleans-up: Deleting data that others reference cleans up every reference

**Area:** data **Status:** accepted

### Context

The remote system reports deletions in a deletion log with a reference type and a value. The mapping table allows several Shopware records per remote ID: a main variant with attributes is at the same time the parent container and its first variant.

A rule points to an option by ID (for example "gas spring only for model 02"). When the option it points to was deleted, the rule stayed and pointed into nothing. The editor showed an empty field, and the dependent option never appeared in the shop again, because a condition on an unknown option counts as not fulfilled. The merchant only noticed this in the shop.

A check that rejects the deletion does not help: when saving, the administration sends the deletions first and the other changes afterwards. Even when the merchant adjusts the rule in the same save, the server still sees the old rule during the deletion and would reject what the merchant wanted.

### Decision

- Reference types of the deletion log: 1 category, 4 customer, 5 article, 13 variant. Other types are skipped with `deleted_reference_unsupported`.
- Category, customer and variant delete every Shopware record mapped to the reported ID (`findShopwareIdList`), each through the DAL repository, and explicitly remove every mapping row. An article deletes every product mapped with the article ID as parent ID.
- Unmapped values are skipped with `deleted_entity_not_mapped`.
- The delta filter is `updatedBetween` as a Unix timestamp. The default interval is one hour.
- When an option is deleted, the plugin removes it from every rule that points to it. This also applies when the option is deleted together with its group. The rest of a rule stays, a rule group without a condition is dropped, and a rule without a condition becomes "always visible".
- The editor does this immediately, when deleting in the form (`withoutOptions` in the condition model), so the merchant sees what changes before saving.
- The server does it after every deletion (`DeletedOptionRuleCleaner` on `EntityDeleteEvent`, cleanup in the success callback of the same transaction). So the rule also applies to deletions through the API, an import or another plugin. The pure part, freeing a condition from options, is `ConditionPruner` and has the same semantics as `withoutOptions` in JavaScript.
- Moving stays checked. If the merchant drags an option into the group its own rule points to, or an option that other rules point to into their group, the server rejects the save. There is no unambiguous correction the plugin could make itself.

### Consequences

- Entities are deleted as the legacy connector did, not deactivated, and no orphan of a shared variant ID remains. The product mapping must carry the article ID as parent ID for article deletions to work.
- A rule never points to an option that does not exist.
- Deleting is never blocked. The price: a rule can change silently through a deletion. In the editor this is visible before saving, through the API it is not.
- Integration tests (`StructureDeletionTest`) and Jest (`form-editor`, `condition-model`) pin both sides, and the E2E test "deleting the option a condition points to also removes it from that condition" pins the whole path in the browser.

## default-data-in-the-lifecycle: Default data is created in the plugin lifecycle and large imports run in the message queue

**Area:** core **Status:** accepted

### Context

After installation the plugin needs four default groups `required`, `statistical`, `comfort` and `marketing` with German and English texts. Seed data in a migration with hard coded binary IDs is forbidden by the project rules. During `postInstall` the DAL does not know the plugin's definitions yet, because the container is only rebuilt after activation. A repository for the plugin's own tables does not exist at that point.

The import of the Open Cookie Database loads several thousand entries over HTTP. Synchronously in `install` or `update` it would slow down the installation and let it abort on a network error.

### Decision

- A `DefaultGroupInstaller` creates the groups in `postInstall`, `activate` and `postUpdate`. It writes through the Doctrine `Connection` (like a migration), looks up each group by its `technical_name` and creates only what is missing. Existing groups and translations are never overwritten, so changes by the merchant are kept. IDs are created at runtime with `Uuid::randomBytes()`.
- Languages are resolved through the core repository `language.repository` (locales `de-DE` and `en-GB`). The system language always gets a translation, English if it is neither German nor English.
- The OCD import is only put into the message queue (`ImportOpenCookieDatabaseMessage`), in `activate` and in `postUpdate` of an active plugin. On a plain installation without activation nothing is dispatched, because the handler is only in the container with the active plugin.
- The regular import is a scheduled task with a seven day interval. It is a cheap delta import. `ScheduledTask` has an internal constructor, so there is a message of its own for the manual trigger.

### Consequences

The groups are there right after installation, even without a running worker. The installer is idempotent and can run again on every update. The OCD data appears only once the worker has processed the message. Until then the list of suggestions stays empty.

## configuration-sync-on-activation: Synchronization runs on activate and update, not on install

**Area:** core **Status:** accepted

### Context

The settings of the plugin and those of the core must match. The plugin has to act on install, activate and update for this. An inactive plugin has no services in the container, though. A call in `postInstall()` would run into nothing, because an installed but not yet activated plugin does not provide its services.

### Decision

- **Synchronization happens in `activate()` and `postUpdate()`, not in `postInstall()`.**
- **`activate()` runs after the container has been rebuilt.** The plugin's services exist there.
- **If the service is missing from the container, the call returns silently.** An update of an inactive plugin leaves the work to the next activation.
- **Two things happen on the call:** old keys from 1.0.x are taken over (`retentionDays` becomes `logFileRetentionDays` when the value is numeric and at least 1, `retentionDays` and `cleanupLogEntries` are deleted), and the core values are taken over. Seconds are **rounded up** to whole days, so the retention is never shortened.

### Consequences

After an activation the form shows the actual state of the core. A user who set the core value beforehand keeps it. Whoever installs the plugin and never activates it gets no synchronization, and that is correct, because the plugin then does nothing either.
