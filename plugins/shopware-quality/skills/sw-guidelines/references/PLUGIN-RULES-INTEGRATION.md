# Plugin rules: External integrations

## Contents

- [api-client-on-symfony-http-client: The API client is built on the Symfony HttpClient and caches its access token per host and user](#api-client-on-symfony-http-client-the-api-client-is-built-on-the-symfony-httpclient-and-caches-its-access-token-per-host-and-user)
- [rate-limits-from-response-headers: Rate limits are read from the response headers and waits are injectable](#rate-limits-from-response-headers-rate-limits-are-read-from-the-response-headers-and-waits-are-injectable)
- [every-external-api-can-be-tested: Every external API can be tested directly in the configuration](#every-external-api-can-be-tested-every-external-api-can-be-tested-directly-in-the-configuration)
- [synced-records-keep-a-raw-snapshot: Synced records keep a raw snapshot and separate the remote status from the internal state](#synced-records-keep-a-raw-snapshot-synced-records-keep-a-raw-snapshot-and-separate-the-remote-status-from-the-internal-state)
- [webhooks-are-a-hint-polling-stays: Webhooks and notifications are only a hint, and polling stays as the floor](#webhooks-are-a-hint-polling-stays-webhooks-and-notifications-are-only-a-hint-and-polling-stays-as-the-floor)
- [a-dry-run-writes-nothing: A dry run writes nothing and keeps cursor and schedule unchanged](#a-dry-run-writes-nothing-a-dry-run-writes-nothing-and-keeps-cursor-and-schedule-unchanged)

## api-client-on-symfony-http-client: The API client is built on the Symfony HttpClient and caches its access token per host and user

**Area:** api **Status:** accepted

### Context

The plugin talks to a remote system over a REST API in many shops. It must not add a dependency beyond PHP and Shopware, and the transport must be replaceable in tests.

The remote system issues a bearer token with `expiresIn` and has no refresh token. A login per call would waste the rate limit and slow down every sync page.

### Decision

- The API client uses the container service `http_client` (`HttpClientInterface`). No Guzzle, no curl calls.
- The base URL is normalized by a `BaseUrl` class: https only, no credentials in the URL, host validated, path fixed to `/rest/`.
- Calls go through `send()`, which returns a response object (status, lower-case headers, raw body, decoded data). `get`, `post`, `put` and `delete` return the decoded array.
- Redirects are not followed, so a token never leaves the configured host.
- Time is read from the Symfony service `clock`, and waiting goes through a `SleeperInterface`, so the test phase can fake both.
- Non-idempotent calls (POST) are retried only after a rate limit response, never after a timeout or a server error.
- `POST /rest/login` sends the username and password as form parameters.
- The token is stored in the `cache.object` pool under `<prefix>_token_<sha256(host, username)>`, so every worker process shares it and two shops never mix tokens.
- The cache lifetime is `expiresIn` minus a safety margin of 300 seconds. A short lifetime is halved instead.
- A 401 response or a body containing the text "Unauthenticated" discards the token and logs in again, at most three times per call.
- The password and the token are never logged, never returned by the connection test and never part of an exception message.

### Consequences

Tests replace the HTTP client with a mock client and the sleeper with a fake. Endpoint calls are written once against the client and never touch HTTP details.

A password change invalidates a cached token only when it expires or a 401 occurs, which the re-login handles. The system configuration stores the password in plain text (Shopware does not encrypt configuration values), so database access equals access to the credentials.

## rate-limits-from-response-headers: Rate limits are read from the response headers and waits are injectable

**Area:** api **Status:** accepted

### Context

The remote system limits calls per day (global long period), per minute (global short period) and per route. When a limit is exceeded the server answers with 429, and a blind retry makes it worse.

### Decision

- A `RateLimitParser` reads `X-Plenty-Global-Long-Period-*`, `X-Plenty-Global-Short-Period-*` and `X-Plenty-Route-*` (`Limit`, `Calls-Left` or `Calls`, `Decay`) from every response. A `RateLimitTracker` remembers the last window per host and scope.
- Before every call the tracker waits until an exhausted window has expired. A wait longer than 90 seconds (for example with an exhausted daily window) is not waited out but raised as a rate limit error, so the engine can reschedule.
- A 429 response or a body containing "limit reached" is retried with exponential backoff (base 1 s, cap 30 s, `Retry-After` is honoured), bounded by the configured number of retries.
- Waiting happens exclusively through `SleeperInterface`. `RateLimitTracker::snapshot()` exposes the last seen limits for the dashboard and the connection test.

### Consequences

Syncs slow down by themselves instead of failing. The legacy connector discarded the result of its retry in the short period, this client returns the result of the retry.

## every-external-api-can-be-tested: Every external API can be tested directly in the configuration

**Area:** administration **Status:** accepted

### Context

API keys and tokens (a translation service, later a web analytics tool and several advertising platforms) are entered in the configuration. Whether a key is correct otherwise only shows when a translation or a server event fails.

A merchant also wants to know whether the URL and credentials of an integration work before saving them.

The connection test of the plugin configuration accepts unsaved values for URL, username and password so an operator can check them before saving. A missing value used to be filled in from the stored configuration. An editor could therefore send only a URL of their choice, and the plugin sent the stored password to that host. The access token cache is keyed by host and username, so even a typed but wrong password for the stored host and user could report success with the cached token.

### Decision

- **Backend contract:** a `ConnectionTesterInterface` with `getType()` and `test(array $values, ?string $salesChannelId): ConnectionTestResult` (success, snippet key of the message, details as placeholders). Implementations carry a service tag for connection testers, and a `ConnectionTesterRegistry` finds them by type.
- **Route:** `POST /api/_action/<plugin>/connection-test/{type}`, API scope, ACL `system_config:read`. Body `{ values: { short key: value }, salesChannelId }`. The unsaved form values are tested. Empty values (for example a password that was not typed again) fall back to the stored configuration.
- **Rule for the fall back:** when the request changes the URL or the username compared with the stored configuration, it must carry the password as well. Otherwise the route answers `success: false` with an error code meaning "connection password required" and calls nobody. The administration shows a hint to enter the password.
- **Fresh login for typed values:** a test with any typed value runs on a client created by `withSettings($settings, true)`, which logs in freshly and neither reads, writes nor forgets the token cache. A test of the stored configuration keeps using the cached token.
- **No secrets:** testers never return keys, passwords or tokens, never write them to the log and never echo them back.
- **Result shape of a concrete test route:** it accepts optional `url`, `username` and `password` in a `POST` action route with its own ACL permission (an editor permission of the plugin). It logs in, reads a cheap probe endpoint (for example the list of webstores) and returns the success flag, the list of webstores (ID and name) and the current rate limit windows. Errors answer with HTTP 200 and `success: false`, the error category, the plugin error code and the upstream status. The message and the response body of the remote system are never returned. The read-only probe means the write protection is not involved.
- **Administration:** a connection test button component is placed in `config.xml` as `<component name="...-connection-test-button">` with `<testerType>` and `<configKeys>` (comma list) directly below the fields. The button reads the values from the surrounding `sw-system-config` (its `actualConfigData`, and for an empty channel value the value of "All Sales Channels"), because the core does not offer neighbouring field values through provide/inject. Outside `sw-system-config` it takes the values through the prop `values`.
- **First implementation:** a tester for the translation service uses the plugin's API client (usage and target languages) with a configuration object that prefers the form values. Messages: success with plan, usage and number of target languages, otherwise key rejected, quota exhausted, too many requests, not reachable or not set up.
- **Web analytics tester:** a tester (type `matomo`, button in the matching configuration card for the URL and the site ID) checks whether the tracking script is served at the https address and queries `SitesManager.getSiteFromId` without a token. When the tool does not serve the site anonymously, the test reports "reachable, site cannot be checked". Its HTTP client is `NoPrivateNetworkHttpClient`, so the test cannot reach internal addresses.
- **No test button for public identifiers:** the IDs of Meta Pixel, Microsoft UET, Microsoft Clarity, TikTok Pixel and Pinterest Tag are public identifiers without credentials, and the vendors offer no API that checks an ID without a token. They are only checked for their format (invalid values show in the banner of the areas and in the overview).
- **Server API testers:** Measurement Protocol (validation endpoint, Google does not verify the secret there), Meta Conversions API (reads the pixel with the token), TikTok Events API (needs a test event code, sends a test event) and Pinterest Conversions API (reads the ad account).

### Consequences

Every later API gets its test with one class and one line in `config.xml`. The merchant sees immediately whether a key works. The administration shows an exact reason without additional requests.

The button depends on the data structure of `sw-system-config`. If the core changes it, the tests of the button show it.

The stored password only ever goes to the stored host for the stored user, and a typed password is really verified. Testing new credentials costs one login.

## synced-records-keep-a-raw-snapshot: Synced records keep a raw snapshot and separate the remote status from the internal state

**Area:** data **Status:** accepted

### Context

The OCTO specification documents 23 base fields on `Product`. The captured response of one supplier carries 56, of which 53 are filled on at least one product. Thirty-two of those appear in no documented schema at all:

`address`, `alert`, `bannerImageUrl`, `bannerImages`, `bookingTerms`, `brand`, `cancellationPolicy`, `categories`, `country`, `coverImageUrl`, `description`, `destination`, `exclusions`, `faqs`, `galleryImages`, `googlePlaceId`, `highlights`, `inclusions`, `keywords`, `latitude`, `location`, `logoUrl`, `longitude`, `pointToPoint`, `privacyTerms`, `redemptionInstructions`, `shortDescription`, `subtitle`, `tagline`, `title`, `usageInstructions`, `videoUrl`.

This is not a curiosity. It is almost everything a product page shows. `octo/content` does not explain it either, because that capability extends `Booking`, `Extra`, `Gift`, `Option` and `Order`, and does not name `Product` at all.

Options and units are the same: `meetingPoint`, `language`, `duration`, `itinerary`, `meetingPointDirections` and `coverImageUrl` are undocumented on the option, and `title`, `titlePlural`, `subtitle` and `deliveryMethods` are undocumented on the unit. A second supplier adds two of its own, `optionType` and `durationValue`.

A supplier that sends a field today can send another one tomorrow, and nothing in the specification will announce it. A mapper that reads only what it knows silently discards the rest, and the loss is invisible until someone asks where a description went.

`Booking.status` carries ten values: `ON_HOLD`, `CONFIRMED`, `CANCELLED`, `EXPIRED`, `REDEEMED`, `NO_SHOW`, `PENDING`, `REJECTED`, `REBOOKED`, `QUOTE`. That is what the supplier says about the booking, and it is authoritative about the supplier's own system.

It is not enough to run a shop on. Several situations the plugin must distinguish are invisible in it:

- A confirmation that failed after payment looks the same as one never attempted.
- A cancellation the supplier refused leaves the booking `CONFIRMED`, exactly like one nobody tried to cancel.
- A booking that is `PENDING` because `instantConfirmation` is false is normal operation, because the supplier confirms by hand. Two of 278 products of one supplier work this way. A booking that is `PENDING` because our confirm call never went out is a problem.
- A reservation being renewed, and how often it has been renewed already, has no remote representation at all.

Folding these into one column means either inventing values the API does not have, which makes the column lie about what the supplier said, or losing the distinction.

A legacy history stored JSON blobs per record and could not be filtered. Support must be able to answer what happened when and what the remote system actually returned.

### Decision

The product table carries a non-nullable `raw_snapshot` JSON column holding the provider response for that record verbatim, before any mapping. The column has a `JSON_VALID` check constraint.

Typed columns exist for every field we actually read. The snapshot is not a substitute for them. It is what survives when a field arrives that has no column yet.

Undocumented fields are read defensively: each one optional, none assumed present, none required to parse. A missing `title` falls back to `internalName`, and a missing `description` renders nothing.

The booking table has two columns.

`remote_status` holds the supplier's value verbatim, mapped through `BookingStatus` where it is recognised and stored as received where it is not.

`internal_state` holds the plugin's own view through `TicketBookingState`: reserving, reserved, confirming, confirmed, confirm failed, awaiting supplier confirmation, cancelling, cancel refused, cancelled, expired, needs review.

Neither is derived from the other. The remote status is written only from a provider response, and the internal state only from what the plugin did or decided.

Handling flags are read, never inferred: `cancellable`, `updatable` and `confirmable` come from the booking, and the storefront's cancel button follows `cancellable` rather than a status comparison.

The sync log table stores one row per event with level, entity name, IDs, action, a diff including deletions, the raw snapshot, the remote status unchanged and the internal state in a column of its own.

- JSON columns carry a `JSON_VALID` check.
- Personal data is masked before writing.
- Legacy history rows are imported with `legacy_imported` set and keep their time.

### Consequences

A field a supplier adds is never lost. When it turns out to matter, the column is added and backfilled from the snapshots already stored, without a re-sync of the whole catalogue.

The change review compares against the snapshot, so it can report a change in a field the plugin does not otherwise read.

The catalogue tables grow: one supplier's payload is 9.1 MB for 278 products, roughly 33 KB each. That is acceptable for a table read from a projection rather than scanned.

The snapshot is data, never instructions. It is never rendered unescaped and never evaluated.

A merchant reading a booking sees both: what the supplier thinks and where the plugin stands. When those disagree, that disagreement is the diagnosis.

The review queue keys on `internal_state`, so a `PENDING` booking under manual confirmation never reaches it while a failed confirmation always does.

A Shopware cancellation does not write `remote_status`. It cannot, because nothing was said to the supplier yet. That is why the merchant is asked before a Shopware cancellation reaches the provider.

Two columns must be kept consistent by the code that writes them, which is the cost. The gain is that neither has to carry a meaning it was not designed for.

The administration can filter and page the sync log by entity, ID, run and time. The remote status can change its vocabulary without touching the internal logic. Raw snapshots make the log table large, so retention matters.

## webhooks-are-a-hint-polling-stays: Webhooks and notifications are only a hint, and polling stays as the floor

**Area:** sync **Status:** accepted

### Context

The remote system can send webhook events. Its public documentation promises neither delivery, order, retries nor the list of events. A lost event, an outage of the receiver or a rotated signing key would leave data stale if the connector relied on webhooks alone. The merchant asked for webhooks as an optional feature.

OCTO offers two push mechanisms, and they overlap.

`octo/notifications` sends identifiers only (`uuid`, `productId`, `availabilityIds`) across three types. The payload is an instruction to re-read, never a source of truth.

`octo/webhooks` sends the serialized object plus a `diff[]` of what changed, across four events including `order_update`.

The reference is explicit about using both: *"Pick one per integration and stay with it: subscribing to both delivers the same change twice."*

One supplier has neither. Its entire API is nine operations, there is no `/webhooks` and no `/notifications/subscriptions`. Its catalogue can only be polled.

Neither mechanism has a signature scheme. Authentication is a shared secret the integrator sets as a request header.

### Decision

- Webhooks are off by default (`webhooksEnabled`). While they are off, the receiving route answers 404 and pending event rows are marked as ignored.
- A webhook never replaces a scheduled run. It only starts a run of the matching sync type earlier, with the remote IDs of the event, through `SyncRunnerInterface::start()` and the trigger `webhook`.
- The scheduled dispatch keeps running for every sync type. With `webhookReducePolling` active, a sync type that received a webhook within the last hour waits its interval times `webhookPollingFactor` (1 to 24, default 4) after its regular due time. Polling is never switched off and returns to the normal interval one hour after the last webhook.
- The engine reads the factors through the contract `WebhookPollingAdvisorInterface`. A failing advisor is logged, and the dispatch continues without factors.
- Webhook event rows are cleaned up together with the sync log, after `logRetentionDays`, but never later than 30 days, even when the log is kept forever.
- For the OCTO integration, the supplier column `sync_strategy` holds exactly one of `notifications`, `webhooks` or `polling`. The plugin implements all three, and a supplier uses one.
- Polling is the floor, not a fallback of last resort. It is the only option for a provider without push, and a scheduled task drives it per supplier at a configurable interval, dispatching one message per supplier into the queue.
- A notification is treated as an invalidation signal: the ids are read, the corresponding records are re-fetched from the API, and the payload itself is never written to the database. A webhook delivery, despite carrying the object, is treated the same way, because the reference calls the payload untrusted and says to verify by fetching.
- Webhook registration always sends the same `Octo-Capabilities` header on update as on create, because an update recalculates the stored capabilities and a missing header narrows them silently.
- The incoming endpoint compares the shared secret with `hash_equals` and is idempotent, because `retryOnError` means a delivery can arrive twice.
- A sync run table holds a row per run. A run in state `running` for a supplier blocks the next one for that supplier. The second is skipped and recorded as such.

### Consequences

- A shop without webhooks behaves exactly as before.
- A missed webhook is healed by the next scheduled run.
- Reduced polling only saves API calls when webhooks really arrive.
- No supplier receives duplicate events, because no supplier is subscribed twice.
- A provider without push works with the same code path as the others. What differs is the trigger, not the mapping.
- A shop behind a firewall, or one whose webhook endpoint is unreachable, can run entirely on polling without losing correctness, only timeliness.
- Because every channel ends in a fetch, a lost, duplicated or out-of-order delivery costs a request and nothing else.

## a-dry-run-writes-nothing: A dry run writes nothing and keeps cursor and schedule unchanged

**Area:** sync **Status:** accepted

### Context

- Finding F2: the sync run context had `dryRun` hard set to `false`, and there was no switch in the administration, in the API or in the command.
- A merchant could not check a sync type without writing data and moving the cursor.

### Decision

- The marker `src/Service/Registry/Contract/DryRunCapableInterface.php` is put on every sync type that honours `run->dryRun`.
- These are all master data types (through `AbstractMasterSyncType` and `MasterWriter`) and the types `ProductSyncType`, `PartialProductSyncType`, `ProductGarbageCollectionSyncType`, `ProductVariantValidationSyncType`, `ProductMediaSyncType`, `ProductUpdatedCatchUpSyncType`, `CustomerSyncType`, `ReviewSyncType`, `PromotionSyncType` and `PromotionInvalidationSyncType`.
- The order types (export, import, status, payment, gift cards) are excluded, because they write to the remote system or to Shopware without a check for a dry run. A dry run request for them is rejected with the error code `<PREFIX>__DRY_RUN_NOT_SUPPORTED`.
- A dry run always reads the full data set (`full`) and locks the type.
- It becomes `lastRunId`, so "Show last run" opens it.
- It leaves cursor, page, `finished`, `lastRunAt`, `nextRunAt` and `lastErrorCode` unchanged and never consumes the daily reset.
- The run carries the message `engineDryRun` and is called "Dry run" in the run list.
- The counters show what would happen (new, updated, unchanged).

### Consequences

- A new sync type implements the marker only after every write path has been checked.
- The administration offers "Run dry run" only for supported types, and `sync/types` reports `supportsDryRun` for this.
- The ownership proof of a run (`isCurrent`, `isOwnedBy`) checks `lastRunId`, so a dry run must set it.
