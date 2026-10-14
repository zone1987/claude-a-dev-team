# Plugin rules: Resilience, privacy and security

## Contents

- [the-plugin-never-stops-the-shop: Nothing the plugin does or gets wrong may stop a shop, a page, the checkout, the administration, the scheduler or the worker](#the-plugin-never-stops-the-shop-nothing-the-plugin-does-or-gets-wrong-may-stop-a-shop-a-page-the-checkout-the-administration-the-scheduler-or-the-worker)
- [typed-errors-with-stable-codes: Errors are typed exceptions with stable codes and a category that decides retries](#typed-errors-with-stable-codes-errors-are-typed-exceptions-with-stable-codes-and-a-category-that-decides-retries)
- [no-blocking-external-call-in-the-checkout: No external provider call blocks the checkout](#no-blocking-external-call-in-the-checkout-no-external-provider-call-blocks-the-checkout)
- [failed-async-work-is-retried-then-dead-lettered: Failed sync pages are retried with a delay and then dead lettered](#failed-async-work-is-retried-then-dead-lettered-failed-sync-pages-are-retried-with-a-delay-and-then-dead-lettered)
- [privacy-by-design: Privacy is built in, not retrofitted](#privacy-by-design-privacy-is-built-in-not-retrofitted)
- [nothing-reaches-a-third-party-before-consent: Nothing reaches a third party before consent, and server side events need stored consent](#nothing-reaches-a-third-party-before-consent-nothing-reaches-a-third-party-before-consent-and-server-side-events-need-stored-consent)
- [log-channel-and-log-retention: A plugin writes to its own log channel at level info, and log rows and runs are pruned by age](#log-channel-and-log-retention-a-plugin-writes-to-its-own-log-channel-at-level-info-and-log-rows-and-runs-are-pruned-by-age)
- [acl-privileges: Roles grant no system config, risky actions have their own privilege and write in the system scope](#acl-privileges-roles-grant-no-system-config-risky-actions-have-their-own-privilege-and-write-in-the-system-scope)
- [security-policy-and-sbom: A disclosure policy in SECURITY.md and an SBOM for every release](#security-policy-and-sbom-a-disclosure-policy-in-securitymd-and-an-sbom-for-every-release)
- [a-receiver-checks-the-sender-before-the-body: A webhook receiver checks the sender before it reads the body](#a-receiver-checks-the-sender-before-the-body-a-webhook-receiver-checks-the-sender-before-it-reads-the-body)
- [development-never-touches-live: Development never touches live, and no task may overrule that](#development-never-touches-live-development-never-touches-live-and-no-task-may-overrule-that)
- [exported-settings-carry-no-secrets: Exported settings are portable, carry no secrets and delete nothing](#exported-settings-carry-no-secrets-exported-settings-are-portable-carry-no-secrets-and-delete-nothing)

## the-plugin-never-stops-the-shop: Nothing the plugin does or gets wrong may stop a shop, a page, the checkout, the administration, the scheduler or the worker

**Area:** core **Status:** accepted

### Context

The plugin hooks into the order flow, the administration and scheduled work, in shops with data, themes and extensions it has never seen. Missing data, API outages, malformed answers from external systems and overrides by third parties will occur somewhere. A plugin that takes down a checkout or an administration page does more harm than a delayed sync.

Many plugin features are not needed for selling (consent, tracking, a cleanup job, extra tiles in a listing). If such a plugin throws on a product page, in the checkout, when saving in the administration or in the worker, exactly the part of the shop that earns revenue stands still. A cleanup function that throws in the scheduler, when saving the configuration or on activation can stop the worker or the administration in the worst case. The owner has decided: errors are caught and logged, and the shop must never and nowhere crash.

A plugin that decorates services on the path every product listing takes (for example the paging processor and the CMS element resolver) is especially exposed. Both run on every listing page of every shop that has the plugin installed, and both are decorators, so an exception in either does not disable the plugin, it takes the page down.

What can go wrong is not hypothetical. Measured while writing the tests:

- `?p=abc` in the URL made `getInt('p')` throw `BadRequestException`. Any crawler reaches it.
- `getStock()`, `getSales()`, `getAutoIncrement()` and `getCalculatedMaxPurchase()` on a placeholder product were typed properties that were never written, so reading one was a fatal error instead of a null. Third-party plugins walk the listing and read exactly those. This is the defect that was reported from a live shop.
- A category whose `path` is empty, a sales channel without a navigation category, an interruptor whose categories were never loaded: each of them was a branch that could throw.

The plugin adds tiles to a listing. Nothing it does is worth a shopper losing the page.

### Decision

**The plugin is never the reason why a shop, a page, an administration page, the checkout, the scheduler or the worker stops working. Nothing the plugin does may cost a shopper their listing.** Every error is caught, logged and mitigated. Every entry point that Shopware calls catches `Throwable` and writes the error with context to the plugin's own log channel.

| Entry point | Behaviour on an error |
|---|---|
| Subscriber and listener | `catch (Throwable $exception)`, log, do nothing, the core flow, the page and the save operation continue unchanged |
| Response listener (script blocking) | deliver the response unchanged |
| Twig function | empty output |
| Blocking of a snippet in Twig | omit the snippet, never output it unblocked |
| Storefront controller | neutral answer (for example `excluded: false`, redirect without a cookie), stable error code in the response, never a stack trace |
| Admin API controller | stable error code in the response, never a stack trace (Shopware shows the error as a notice in the administration and the shop keeps running, so a controller that only serves the administration needs no neutral fallback) |
| Message handler | retry with back-off, then the dead letter queue, the error is logged. Where retrying is pointless, log the error and treat the message as done |
| Scheduled task handler | a failing item is logged and counted, the run goes on. Errors are logged and the scheduler keeps running |
| Command | a failing item is logged and counted, the run goes on, the exit code reports it |
| CMS resolver | element without data |
| `activate()` and `postUpdate()` | log the error, activation and update continue |
| Handler of a system config change | log the error, saving the configuration continues |
| Storefront JavaScript | every error is caught, a missing element is a no-op |
| Administration | every asynchronous call has error handling, resets its loading state and reports success or error through the `notification` mixin (`createNotificationSuccess`, `createNotificationError`) like the core |
| Paging processor decorator | leave the criteria exactly as the core built them, the listing renders without the plugin's additions |
| CMS element resolver decorator | leave the products exactly as they were loaded, the listing renders without the plugin's additions |

- Where an error leaves the choice between "deliver" and "omit", consent wins: a tracker is omitted on error and never loaded without consent.
- Within a storefront or checkout request no call to an external system is made. Sync work runs in the queue, in scheduled tasks or in commands.
- Logs go to the plugin's own channel. Examples of what was used: file `var/log/<channel>_<environment>.log` at level `warning` and higher with 14 rotated files, or `var/log/<channel>/<environment>.log`.
- A log context carries IDs, the exception class (`exception` => `$exception::class`) and the exception code (`code`). Never the exception object, never the exception message, never personal data, because the message of a database, validation or API error can quote the data it failed on. Where the error concerns a request, the context also carries identifiers such as the sales channel id.
- No empty catch block. A caught error is always logged (backend) or reported (administration). A fault that is swallowed is a fault nobody fixes, the catch exists to protect the shopper, not to hide the problem.
- A handler that must keep this behaviour is declared `final` so that the behaviour cannot be overridden. Examples of such entry points are the scheduled task handler `run()`, the system config change subscriber and the lifecycle methods.
- Every guarded call gets a test that forces the error and checks that nothing leaks outward, that the error is logged and that the caller still receives a usable result.
- The placeholder product used in listings is complete enough to be read by anyone. Every non-nullable property of `SalesChannelProductEntity` is filled, so no getter a third party might call can throw. A test (`FakeProductTest` in the source plugin) walks every public getter by reflection and asserts none of them throws.
- Values of the placeholder product are zero throughout (stock, sales, price, `auto_increment`). That is deliberate: `product.auto_increment` is a unique column MySQL fills itself and never hands out a zero (measured: real products run from 3 upwards), so nothing on a card can be mistaken for a real product by it.

### Consequences

Errors become log entries instead of outages, so the log has to be read. A broken or misconfigured plugin is invisible to the shopper and visible only in the log. For example an interruptor that stopped appearing looks like a configuration mistake until somebody opens the plugin's log directory. A failed sync shows up in the sync log and in the dead letter queue and is fixed there. A missing tracking event is a smaller damage than a stopped shop, and a stopped scheduler is the bigger damage than an invisible cleanup error, so the plugin accepts that its errors stay invisible until someone reads the log. The log is deliberately not linked in the administration module.

The price is one test per guarded call. Catching `Throwable` catches programming errors too, including ones a test would have caught. The unit suite is what keeps that from becoming a habit: the catch is the last line of defence, not the first.

Filling every property of the placeholder product means tracking `SalesChannelProductEntity` as Shopware changes it. A new non-nullable property in a future version reintroduces the fault, which is why the test walks the class by reflection rather than naming the getters.

## typed-errors-with-stable-codes: Errors are typed exceptions with stable codes and a category that decides retries

**Area:** core **Status:** accepted

### Context

Synchronisation errors are retried, logged and shown in the administration. That needs a stable code per kind of error and messages that never reveal personal data.

The engine must decide whether to retry, reschedule or give up, and the administration must show a reason without exposing response bodies that may contain personal data.

Retry handling, backoff, a circuit breaker on error rates and the definition of done for a provider plugin (specification chapters 61, 107, 108 and 183) all react to why a call failed. If providers report their own error codes, the middleware would need per-provider knowledge to decide whether to retry, which is exactly the provider-specific logic the specification forbids in the middleware. Cross-provider reporting and circuit breaking would also become impossible, since there would be no shared vocabulary to aggregate over.

Deriving the category automatically from HTTP status codes was considered. It works for transport failures but not for the interesting cases: a `400` may mean an invalid address, a discontinued product or a rejected order, and those have opposite retry semantics.

### Decision

Domain errors:

- One exception class (`ConnectorException` in the source plugin) is the only base of domain errors. Error codes start with a plugin specific prefix of the form `<VENDOR>_<PLUGIN>__`. Instances are created exclusively through static factory methods.
- Registry and contract errors: `unknownSyncType`, `unknownRegistryKey`, `duplicateRegistryKey`, `unknownSyncDependency`, `cyclicSyncDependency`, `invalidPayload`, `invalidCursor`, `readerPathMissing`, `readerTypeMismatch`.
- API errors are an `ApiException`, a subclass that carries the taxonomy `ApiErrorCategory`, which decides about retries. Persistence errors have their own subclass in the persistence area.
- Contracts declare `@throws ConnectorException`, which covers every subclass.
- Parameters carry IDs, keys and paths. Values from the external system or from customers never become part of a message.

API error taxonomy of a connector:

- `ApiErrorCategory` has the cases authentication, rate_limit, not_found, validation, server and network. `isRetryable()` is true for rate_limit, server and network.
- `ApiException` extends the base exception, carries the category, the HTTP status of the remote side and the normalised route (numeric segments become `{id}`, query strings are dropped), and is built exclusively through factory methods.
- Messages contain category, route and status. Credentials, tokens and response bodies are never part of a message.
- The HTTP status of the exception itself is 502, the status of the remote side is a separate field.

Error taxonomy of provider plugins (binding provider contract):

`ProviderErrorCategory` is a PHP enum with the nineteen values from specification chapter 107:

```text
AUTHENTICATION · AUTHORIZATION · RATE_LIMIT · NETWORK · TIMEOUT
PROVIDER_UNAVAILABLE · INVALID_REQUEST · INVALID_PRODUCT · OUT_OF_STOCK
PRICE_CHANGED · SHIPPING_UNAVAILABLE · ADDRESS_REJECTED · ORDER_REJECTED
DUPLICATE_ORDER · UNKNOWN_ORDER_STATE · WEBHOOK_INVALID · MAPPING_ERROR
DATA_QUALITY · INTERNAL
```

Every provider maps its API errors onto this enum, unmapped errors become `INTERNAL`. The enum is part of the provider contract (provider coupling) and its correct mapping is a release criterion (chapter 183).

Retry policy, backoff, circuit breaker input and review queue routing are decided from the category alone. The middleware never inspects provider-specific codes.

The original provider error (code, message, correlation ID) is preserved alongside the category for diagnostics, with secrets masked (chapter 76).

### Consequences

- Callers catch one base type, the retry logic reads the category of the API subclass.
- Retry decisions read a single enum. Log entries name the code, IDs and the failing route, which is enough to find the cause without personal data.
- Easier: one retry policy for all providers, circuit breaker and error reporting work across providers, adding a provider adds no branching to middleware error handling.
- Harder: provider authors must classify carefully. A lazy mapping to `INTERNAL` makes errors non-retryable and pushes them to manual review. This is deliberately the least convenient outcome, so that correct classification is the path of least resistance.
- `UNKNOWN_ORDER_STATE` and `DUPLICATE_ORDER` are special: neither may be retried blindly, since both may mean the supplier order already exists. They route to reconciliation (chapter 164) instead.

## no-blocking-external-call-in-the-checkout: No external provider call blocks the checkout

**Area:** checkout **Status:** accepted

### Context

Specification chapter 22.1 lists six moments at which availability could be checked, and 22.2 already recommends cached data everywhere except immediately before procurement. Chapter 124 sets checkout performance requirements.

A live supplier call inside the checkout couples the shop's conversion rate to a third party's uptime and latency. A supplier that answers in four seconds, or not at all, turns into an abandoned cart. Several suppliers in one cart multiply the exposure. Chapter 108 introduces a circuit breaker precisely because supplier APIs are expected to fail.

The counter-argument is data freshness: cached stock may be wrong, and the order is accepted for goods that cannot be procured. But chapter 22.3 concedes that without supplier stock reservation, no check, however fresh, can guarantee availability. A live call in the checkout buys a slightly better guess at a disproportionate cost.

### Decision

No provider API call blocks the checkout. Product detail page, add-to-cart, cart and checkout are served exclusively from cached data (caching strategy).

Fresh availability and the final sourcing decision happen asynchronously after the Shopware order is created, before the supplier order is placed (chapter 40). If the fresh check invalidates the plan, re-sourcing (chapter 44) selects another source. If none remains, the order enters manual review.

Shipping quotes follow the same rule: cached or rule based during checkout (chapter 89), live only in the asynchronous procurement step.

### Consequences

- Easier: checkout latency is independent of supplier APIs, a supplier outage never blocks a sale, and the performance requirements of chapter 124 are met by construction.
- Harder: an order may be accepted that cannot be fulfilled as planned. Re-sourcing, manual review and customer communication on final failure (chapter 22.3) are therefore not optional features. They are the price of this decision and belong in the MVP.
- Cache TTLs become a business parameter: the shorter the stock TTL, the rarer the post-order surprise, the higher the sync load. Defaults are in chapter 66.

## failed-async-work-is-retried-then-dead-lettered: Failed sync pages are retried with a delay and then dead lettered

**Area:** sync **Status:** accepted

### Context

The external system answers with rate limits, timeouts and server errors. A synchronisation must survive them without blocking a worker, and a programming error must stay visible instead of being retried forever.

### Decision

- Every handler catches `Throwable` and logs only IDs, exception class and code.
- A retryable API error (rate limit, server, network) enqueues the same page again with a `DelayStamp` of 60, then 120 seconds. The run stays open. The third failure ends the run as failed.
- A non-retryable API error (authentication, validation, not found) ends the run as failed without a dead letter, because the next scheduled run retries it anyway.
- Every other error ends the run as failed, and the handler throws `UnrecoverableMessageHandlingException`, so that Symfony moves the message straight to the failure transport. `messenger:failed:retry` processes it again, and the run is reopened if it is still the last run of its type.
- A failure writes the sync log line `enginePageFailed`, sets `last_error_code`, releases the lock and schedules the next run after the interval. The stored cursor is not advanced, so the next run repeats the failed page.
- No shop configuration is changed. The retry strategy of the core transport applies to errors outside the handler.

### Consequences

- Transient errors heal without operator intervention.
- Failures end up in `messenger:failed:show`, and the run is marked as failed.

## privacy-by-design: Privacy is built in, not retrofitted

**Area:** legal **Status:** accepted

### Context

A plugin decides which data a shop stores about its visitors and transmits to third parties. A mistake affects every visitor of every shop that uses the plugin. GDPR and TDDDG demand consent before every non-essential access to the end device, data minimisation, retention periods and understandable information about who receives which data and where it goes. A review of one plugin after step 10 found places where data was stored without consent or kept longer than necessary.

Log files and log entries can contain personal data, such as IP addresses, email addresses or order data in error messages. A defined retention period with subsequent deletion supports the principle of storage limitation under Art. 5(1)(e) GDPR.

A middleware transmits customer data to third parties. A supplier order carries the recipient's name, shipping address and, depending on the carrier, a phone number or email address. Specification chapter 75 limits this to what fulfilment actually requires and demands that logging minimises or masks personal data. Chapter 76 separately forbids logging credentials. Two GDPR obligations bear on this directly. Data minimisation (Art. 5(1)(c)) means a supplier receives only the fields it needs to ship the parcel, not the customer account and not payment details. Storage limitation (Art. 5(1)(e)) means diagnostic data that contains personal information cannot be kept indefinitely "just in case". Provider payload logging is where this becomes concrete: the most useful log for debugging a failed supplier order is exactly the one containing the customer's address.

Customers, orders and addresses are synchronised between Shopware and an external system and appear in sync logs. Personal data must be processed lawfully, minimised, protected and deleted when its purpose ends. The customer sync processes names, email addresses and addresses. The sync log is readable in the administration, can be exported and is kept for a configured time. The log writer masks known personal fields, but a field that never reaches the log needs no masking.

Sync log rows contain parameters, changes and raw data from the external system and from Shopware. Raw data of the order import and of the status write-back contains addresses, the recipient contact with its options and Base64 content of documents. An earlier masker of the engine knew only names, email, phone and street and left postcodes, cities, tax numbers, company names and the values of contact options readable. The import of legacy history had its own masker with different rules.

### Decision

Principles:

- **The plugin processes no personal data itself, where it can avoid it.** A plugin whose purpose is not personal data (for example a log cleanup) writes only file names and numbers into its log lines.
- **Safe defaults.** Optional processing is off by default. File cleanup is off by default with a retention period of 90 days. A period of less than one day deletes nothing (see the retention rule of the log retention decision).
- **No data is written into the plugin's logs that does not belong there.**
- **The operator remains responsible** for setting retention periods to match their own privacy policy and record of processing activities. Duties of the operator that the plugin cannot fulfil, such as the record of processing activities and the data processing agreement with the external system, are listed in the README.
- **Deleting log files and log entries after a fixed period is the purpose** of a cleanup plugin. The period is set by the operator.
- The plugin sets no cookies and loads nothing from third parties in the storefront unless that is its declared purpose and covered by consent.

Consent per field:

- Attribution data (click IDs, UTM parameters, landing page, referrer) is stored in the browser only if the service the field belongs to has consent. The landing page is stored without the query string.
- Server side events are sent only with the consent stored on the order. Before sending, the plugin checks whether consent has been withdrawn in the meantime.
- The plugin creates no identifiers of its own for trackers (no synthetic client IDs). If the browser identifier is missing, the event is sent without it or not at all.
- Advanced Consent Mode loads Google tags before consent. It takes effect only after the merchant has confirmed it explicitly. The confirmation cannot be transferred by a settings import.

Data minimisation and retention periods:

- The personal tracking fields on orders are emptied after 180 days (configurable from 30 to 730 days). The proof of consent, the send states and the refunds remain, they contain no identifiers.
- The consent log stores the IP address only shortened and only if the merchant switches that on. The user agent is stored as an HMAC with the kernel secret and cannot be reversed without the key. Retention is 3 years.
- Logs contain neither credentials nor personal data. A log processor strips the data of exceptions, and the plugin's API clients write no requests into the log.
- The list of unknown cookies contains only cookie names and no personal data. Its cleanup belongs to the scanner (step 11).
- A legal basis is defined per synchronised field. Contract performance (Art. 6(1)(b) GDPR) for orders, customers and addresses that are needed to fulfil the order, legal obligation (Art. 6(1)(c)) for data needed for invoices. Without one of the two nothing is synchronised.
- Only the fields the external system needs are stored or sent. Other personal data is not kept. Only the fields Shopware needs are read. Contact options are requested only to read the email fallback, newsletter, birthday and reviews are not read.
- Toward suppliers only fulfilment relevant fields are transmitted. Account data and payment details never leave the shop.
- The export of the sync log needs its own privilege, separate from viewing.
- A retention setting deletes log entries after a configured number of days. The default is finite.
- Uninstalling with removal deletes the logs (see the uninstall decision).
- Retention follows purpose: a payload log rotates hourly and keeps 48 files (two days, the shortest retention of any channel), while non-personal channels keep more.

Customer, review and promotion sync logs are minimised:

- Message keys are fixed strings such as `customer.skipped_guest`. They never contain data. Parameters carry only IDs, counts, reasons and error classes.
- The raw data snapshot of a customer log entry is a whitelist: `id`, `typeId`, `classId`, `externalId`, `referrerId`, `blocked`, `addressCount`. Names, email addresses, phone numbers and addresses are not part of it.
- The `changes` of a customer entry list field names with the value `changed`, never old or new values.
- Reviews log `id`, `targetId` and `isVisible`. Promotions log `id` and the number of codes. Redeemed codes are not logged.
- Errors are written to the plugin's channel and to the sync log, with the external ID, the exception class and the code. Exception messages are never logged, because they can carry data.
- A review stores the author's name as `externalUser`, because the storefront displays it.

One shared masker for every log row:

- `PersonalDataMasker` is the single masker of the plugin. It normalises the last segment of a key (after the last dot, lowercased, without underscores, hyphens and spaces).
- A key is personal if the normalised name is in the list (email, mail, first, last and full name, name1 to name4, phone, mobile, fax, street, house number, address lines, birthday, company, company name, contact person, postal code, zip, place, city, VAT number, VAT ID, tax number, IBAN, BIC, customer comment) or ends in one of the suffixes `email`, `firstname`, `lastname`, `fullname`, `responsiblename`, `phone`, `phoneno`, `phonenumber`, `street`, `housenumber` and `houseno`.
- In an options container (`options`, `addressOptions`, `contactOptions`) the `value` of each entry is personal, its type stays readable.
- Every value under a personal key is replaced by `***`, empty values stay empty. In any other text an email address is replaced by `***`.
- The rule applies to every row written by `SyncLogWriter` as long as `maskPersonalData` is on (default). `LegacyPersonalDataMasker` delegates to the same masker, so rows of the legacy history follow the same rules.
- The status write-back replaces the `content` of every document in its raw data with null before the row is written, regardless of the masking switch.

Masking of payloads in provider logs (masked, not merely truncated):

| Field kind | Result | Reason |
|---|---|---|
| Email | `a***@example.com` | domain stays readable for routing problems |
| Phone | `***1234` | last four digits identify the record without exposing the number |
| Name, company, street, birthday, VAT id, customer number | `A***` | first character only, enough to correlate |
| Country, postcode, city | unchanged | not personal on their own, needed for delivery restriction diagnosis |
| Credentials per chapter 76 | `***` | removed entirely, never masked |

`PayloadRedactor` implements this and is the only path by which a provider payload may be logged. Payload logging is off by default and switchable in the plugin configuration, so it is enabled deliberately for a diagnosis and switched off afterwards rather than running permanently.

Transparency:

- Every service in the cookie dialog and in the CMS cookie list states purpose, provider, privacy policy, cookies with storage duration, the transfer to third countries with the safeguard, and the legal basis.
- Legal basis for services with consent: Art. 6(1)(a) GDPR and Section 25(1) TDDDG. For technically necessary services: Art. 6(1)(f) GDPR and Section 25(2) no. 2 TDDDG.
- The third country statement is a translatable field on the service. Built-in services bring it along (for example "USA (EU-US Data Privacy Framework)"). Existing services receive it on installation and when saving the settings, but only if the field is empty and the merchant has not written the text themselves. A service that runs on the shop's own server (for example Matomo) has no statement.
- The consent ID and the cookies of the plugin are visible in the cookie settings.

### Consequences

Every new feature is checked against this list before the commit: consent, minimisation, retention, transparency, deletion together with the order. When a plugin is extended, each new data processing is checked against the list before it is finished. A new service without a third country statement appears without that line. The legal basis always appears. The statements do not replace the shop's privacy policy, they supplement it.

The operator has a tool to implement storage limitation for logs. The retention period does not replace a legal assessment.

A deletion request in Shopware leaves no readable personal data in logs. Masking and retention cost some detail when debugging, which IDs and codes make up for.

The administration shows which fields changed but not their values, which is enough to understand a run.

New fields of the external system with usual naming are masked without a code change. A harmless key that happens to match is masked as well. IDs, types and codes still identify the row.

Provider payload logging:

- Easier: logs can be shared with support without exposing customer data, and the retention period for personal data is short and enforced by rotation rather than by discipline.
- Harder: a masked log is less convenient to debug with. Where the exact value matters, the correlation id links the log entry to the order, and the order still holds the data.
- The masking list is key based and therefore incomplete by nature. A provider that names a field `recipientDesignation` is not covered. Every new provider mapping has to be checked against the list, and the list extended.
- Non-personal fields stay readable deliberately. Masking a country code would remove diagnostic value without protecting anyone.

## nothing-reaches-a-third-party-before-consent: Nothing reaches a third party before consent, and server side events need stored consent

**Area:** storefront **Status:** accepted

### Context

A meeting point is worth a map, and a map means tiles from a third party (for example OpenStreetMap, CyclOSM, the Humanitarian style, Esri). Every tile request carries the visitor's IP address to a service the shop does not control.

Under the GDPR that needs consent, and consent has two halves people routinely get wrong. The first is not loading anything beforehand. The second is Art. 7(3): withdrawing has to be as easy as giving.

A cookie that appears in no cookie setting cannot be withdrawn at all. One plugin registered no cookie provider at first, so the map's own cookie was invisible to the shop's cookie configuration, and the project guidelines claimed the opposite, which is how it stayed unnoticed.

On the server, the question is different: was the customer in agreement when placing the order? The browser can supply a consent state, but a value read from the request is read too early and asking afterwards is too late.

### Decision

**Nothing third party is built or requested before consent.** The map is built on the click, and not before. A page nobody consented on makes zero third-party requests, measured in the browser and not assumed.

**The answer is remembered in a cookie of the shop's own**, never in `localStorage` or anything else a cookie configuration cannot list.

**That cookie is declared.** A subscriber adds it to the comfort features group the core already keeps YouTube and Vimeo in, because an embedded third party is exactly what that group is for. It listens on `CookieGroupCollectEvent`, not on `CookieProviderInterface`, which is deprecated for 6.8.

**Withdrawing takes the map down at once.** The plugin listens for `CookieConfiguration_Update` rather than waiting for the next page load: a map still on screen after the visitor said no is not a withdrawal.

**Geocoding is exempt, and the reason is recorded here so nobody re-litigates it.** The geocoding service (Nominatim) is asked server side during the catalogue run, about a public business address, with no visitor involved. Nothing about a person is transmitted, so no consent is at stake.

Server side events:

- **The consent state is stored with the order on `CheckoutOrderPlacedEvent`** (entity `<prefix>_order_tracking`).
- **Stored:** consent ID, consent state per service, validity hash, timestamp.
- **Server events check this store** before an event is sent to a tracker.
- **Exclusion rules check order attributes** (sales channel source, customer group, IP range) and the order address.
- **Refund tracking uses the same consents** as the order.

### Consequences

Leaflet is bundled rather than fetched (42 KB under a BSD licence, compiled into the storefront build). Loading it from a CDN would itself be a third-party request before consent.

The placeholder has to hold the map's height, or the page jumps when a visitor agrees.

Every new tile service added later inherits this: it is a third party, so it waits for the same consent and is credited as its terms require.

The claim "zero requests before consent" is only worth what the measurement is worth. It is checked in a browser with the network panel, not inferred from the code.

Server side events are legally correct. Tracking without consent does not run, not even hours later.

## log-channel-and-log-retention: A plugin writes to its own log channel at level info, and log rows and runs are pruned by age

**Area:** log **Status:** accepted

### Context

Version 1.0.3 of one plugin had a log level `error` but wrote only messages of the levels info and debug. Therefore nothing was ever written. In addition, Shopware does not load the files under `Resources/config/packages/*.yaml` of a plugin by itself: `Bundle::buildDefaultConfig` is called only for the framework and for profiling.

Raw snapshots make a sync log large, and personal data must not be kept longer than necessary. The decision on personal data demands a finite default retention, but the configuration had shipped with zero days, which kept everything. Some merchants still want to keep the history forever.

Log rows from a legacy import have no run. Deleting an old run must not silently destroy log rows that retention has not yet reached.

### Decision

Log channel:

- **The plugin has its own Monolog channel.**
- **The file lives under `%kernel.logs_dir%/<channel>/<env>.log`**, as a rotating file with 14 files.
- **The level is `info`**, so that the line about deleted files arrives.
- **`build()` in the plugin class loads `Resources/config/{packages}/*.yaml` itself** through a `DelegatingLoader`.
- **The logger service is named `<channel>.logger`.**
- **The log lines contain only file names and numbers**, no personal data.

Retention of sync logs and runs:

- `logRetentionDays` defaults to 90 days in `config.xml` and in the config class when the key is missing.
- The scheduled task `<prefix>.log_retention` runs every 24 hours and deletes log rows older than `logRetentionDays` by `created_at`, as well as finished runs (succeeded, partial, failed, cancelled) that are older, by `started_at`.
- Zero days keeps everything and must be chosen explicitly. Running runs are never deleted.
- Deletion goes in blocks of 500 through the DAL.
- A command `<prefix>:log:prune [--days=N]` does the same on demand.

Link between log rows and runs:

- `<prefix>_sync_log.run_id` is nullable with `ON DELETE SET NULL`, the DAL side uses `SetNullOnDelete`.
- Retention deletes log rows by `created_at` and runs by `started_at`, both indexed. Zero days keeps everything.
- `<prefix>_sync_state.last_run_id` also uses SET NULL.

### Consequences

- Messages of the plugin are found in one place and do not mix with other channels. The plugin's log directory itself lies under `var/log` and is therefore covered by file cleanup: its rotated files age out after the configured period.
- Retention of runs and logs is independent of each other.
- Orphaned log rows are possible and expected. Log rows of deleted runs remain with an empty run link until they expire themselves.
- New installations keep three months of history. Existing installations keep their stored value, an update does not overwrite it.
- Legacy rows keep their original time and expire like all others, so an import of an older history is deleted on the next run of the task unless the merchant raises the value beforehand. The runbook points this out.

## acl-privileges: Roles grant no system config, risky actions have their own privilege and write in the system scope

**Area:** security **Status:** accepted

### Context

A module reads logs that can refer to customers and orders, and it can start syncs, change mappings and reset cursors. A consent log is evidence towards authorities, can become very large and contains shortened IP addresses. Reading in the administration makes sense for viewers, but a mass export should be granted deliberately.

A review of one plugin showed two weaknesses. The viewer role held `system_config:read` and the editor role `system_config:create` and `system_config:update` for every domain, only because the price rule map used the core system config API. Through `/api/_action/system-config` a viewer could read the external system password, the webhook token and the webhook signature key, and an editor could change any setting of the shop. At the same time no role held `<prefix>_sync_run:create` or `:update`, so the core write validator rejected every run that a user without the administrator flag started from the module (run now, retry, sync from a detail tab, legacy import).

### Decision

- The permission group (additional permissions) keeps the roles `viewer`, `editor`, `admin` and `log_export` with their dependencies (editor on viewer, admin on editor, log export on viewer).
- No role grants a `system_config` permission. The price rule map reads and writes only the key `additionalPriceRules` through its own routes: `GET /api/_action/<prefix>/price-rules` (viewer) and `POST /api/_action/<prefix>/price-rules` (editor). The save route validates every rule (positive price IDs, one rule UUID, type `normal` or `bulk`) and writes nothing else. The plugin configuration page stays with the core permission `system.plugin_maintain`, the dashboard shows its button only to users who hold it.
- The viewer reads the plugin entities and the core entities whose names the module displays: payment and shipping methods, state machines and states, customer groups, rules, taxes, units, delivery times, countries, salutations, sales channels and currencies.
- Routes that start or change the connector's bookkeeping (`sync/run`, `sync/reset-cursor`, `sync/retry-failed`, `entity/sync`, `legacy/import`) check their role through `_acl` and then call the runner, the order exporter and the legacy importer with a system context (`SystemSource`, system scope) that keeps currency, language chain and version of the request (`Controller/Administration/Support/SystemContext`). Runs, states and import runs are internal records of the connector. The role check of the route is the permission, the entity permissions of the runs are granted to nobody, so the generic DAL API cannot forge them.
- The detail tab routes of product, order, customer and category require `<prefix>.viewer`, the core route of the detail page keeps its own permission.
- Admin routes use `_acl` with these role keys (see `docs/extending/ADMIN.md`). The role labels live, as the core demands, under `sw-privileges.additional_permissions.<prefix>` and are registered from a JavaScript file.
- An integration test starts a run as an editor without the administrator flag and proves that the viewer receives the price rules but a 403 from the system config API.
- Export of the consent log has its own privilege `<prefix>_log:export`, registered in the administration as an additional permission (`additional_permissions`, key `<prefix>`, role `log_export`).
- The route `GET /api/_action/<prefix>/consent-log/export` requires `<prefix>_log:read` and `<prefix>_log:export`. Filters: consent ID, period, sales channel, kind of decision.
- The export is streamed: `StreamedResponse` with the core `RepositoryIterator` in blocks of 500, delimiter semicolon. Cells that begin with `=`, `+`, `-` or `@` get a leading apostrophe (protection against formulas in spreadsheet programs).
- One logic for list and export: `ConsentLogCriteriaBuilder` builds the search. The kind of decision (all accepted, all rejected, individual) follows the same rule as the statistics and is filtered null safe over JSON paths ("true or missing" instead of a negated comparison). The administration list builds the same filters with the admin criteria.

### Consequences

An operator can be restricted to read access, a separate person can hold the export right, and no plugin role exposes credentials or other shop settings. Code that writes connector records for a user action runs in the system scope after its route check, a new action route follows the same pattern.

The export needs little memory, even with large logs. Whoever may only read sees the list but not the export.

## security-policy-and-sbom: A disclosure policy in SECURITY.md and an SBOM for every release

**Area:** security **Status:** accepted

### Context

Regulation (EU) 2024/2847 (Cyber Resilience Act) requires manufacturers of products with digital elements to run a coordinated vulnerability disclosure policy (Art. 13(8)), to report actively exploited vulnerabilities (Art. 14) and to document the components of the product in a Software Bill of Materials. The regulation prescribes neither a file name nor a format. A plugin that processes credentials of an external system as well as order and customer data cannot treat the policy as optional.

### Decision

- `SECURITY.md` has the sections Report a vulnerability, Response times, Disclosure, Support period, Supported versions, Scope, Relationship to security.txt, Software Bill of Materials and Legal basis.
- It states where to report, what a report contains (affected version, description, steps to reproduce, impact), the response targets, the disclosure rule and the duty to report actively exploited vulnerabilities within the deadlines of Art. 14 to ENISA and the national CSIRT.
- The support period is tied to the end of Shopware security support for 6.6.
- The scope names what the plugin processes: credentials of the external system, API traffic, the sync log with masked personal data, the live write guard, the legacy import and the ACL of the administration.
- Fixed security vulnerabilities are documented in `CHANGELOG.md` under `Security` with the affected and the fixing version.
- The SBOM is generated per release with `composer CycloneDX:make-sbom --omit=dev --output-format=JSON --output-file=sbom.json`. It lists only runtime dependencies (Shopware is the environment, not a component), is attached to the release artefact and is not checked in (ignored by git). The README explains how it is generated.

### Consequences

Reporters and operators know the process, and every release carries the documents the CRA demands. `SECURITY.md` is updated whenever the scope changes.

## a-receiver-checks-the-sender-before-the-body: A webhook receiver checks the sender before it reads the body

**Area:** security **Status:** accepted

### Context

Subscriptions of the external system offer no headers of their own and no basic authentication. The Store API needs an access key header and a sales channel, and a storefront route runs through domain resolution, redirects and maintenance mode. The core health check shows that a route in the scope `api` can skip the bearer check with `auth_required` set to false. A caller outside the allow list must neither use up the rate limit nor make the plugin read and decode a body, and behind a reverse proxy the client address is only correct if Symfony trusts that proxy.

### Decision

- Route `POST /api/<prefix>/webhook/{token}`, name `api.<prefix>.webhook.receive`, scope `api`, `auth_required` false, controller `Controller\Webhook\WebhookController`, logic in `Service\Webhook\WebhookReceiver`.
- Checks in this order: feature switch (404), stated `Content-Length` above 256 KiB (413, before the body is read), IP allow list `webhookAllowedIps` with CIDR support (403), rate limit with a fixed window per client address with `webhookRateLimitPerMinute` (default 120, Symfony rate limiter on the pool `cache.rate_limiter`, 429), size of the body actually read (413), secret path token compared with `hash_equals` (401), signature key (401), a body without a readable event (400), storing with deduplication, enqueueing, 202.
- The client address is `Request::getClientIp()`. Behind a reverse proxy or load balancer the shop sets `TRUSTED_PROXIES` (and `TRUSTED_HEADERS` if needed), so that the address of the external system and not the address of the proxy is checked. `docs/WEBHOOKS.md` describes the setting.
- A call with more than 50 events is accepted with its first 50 events and logged as a warning with the offered and the accepted count. Polling covers the rest.
- The token consists of 32 random bytes as hex in `webhookToken`, is created on installation and update if it is empty, and is replaced by the administration route `POST /api/_action/<prefix>/webhook/token/regenerate` (privilege `<prefix>.editor`). The status route `GET /api/_action/<prefix>/webhook/status` needs `<prefix>.viewer` and shows the endpoint URL only to editors.
- Check of the signature key `webhookSignatureMode`: `plain` (default) compares the signature key in every event of the payload with `hash_equals`. `hmac_sha256` compares an HMAC SHA256 of the raw body in one of the headers `X-Signature`, a sender specific signature header or `X-Hub-Signature-256` (hex or Base64). The HMAC variant is prepared but untested. A missing stored signature key rejects every call.
- Rejections answer with an empty body and are logged only with the status. A storage error answers with 503 so that the sender can retry. The payload is never logged.
- The phpat rule `testTheWebhookReceiverDoesNotDependOnTheSyncTypes` keeps `Controller\Webhook` away from `Service\Sync` and `Service\Api`.

### Consequences

- The route works without a sales channel or a domain.
- A request body that is not valid JSON can be rejected with 400 by the core JSON request listener before the feature switch is read.
- The token has to be entered again in the external system after every regeneration.
- A shop behind a proxy without `TRUSTED_PROXIES` sees the proxy address: the allow list must then name the proxy, and all callers share one rate limit window.

## development-never-touches-live: Development never touches live, and no task may overrule that

**Area:** provider **Status:** accepted

### Context

A development or test shop that contains live credentials of an external system must never create contacts, orders or payments there. A booking is a real purchase. It consumes availability, it is invoiced, and it produces a ticket a guest will try to use.

Developers work from production database dumps. Such a dump carries every supplier row verbatim, including the live base URL, the live credential and `environment = live`. Running a test checkout on a laptop against that data sells real tickets.

Some suppliers make this sharper: with no `Octo-Env` header, staging and production are separate hosts with separate tokens, so an environment mix-up is a wrong URL rather than a wrong header, and the reference warns that it can "sell for real while you believe you are testing". A supplier setting is the wrong place to protect against this, because the dump contains the setting.

Two conditions have to hold at once before anything can go live, and a single resolver (`EnvironmentResolver::resolve()`) is the one place that decides it:

```
resolve(requested) = requested, but only if APP_ENV === 'prod' AND liveModeEnabled
                     otherwise: sandbox, always
```

Every supplier request in the plugin passes through it. The HTTP client's `send()` resolves the environment before it composes a URL, picks a credential or builds a header. One gate, and it already fails closed.

Measured in the shop on 17.09.2026 and not changed by that session:

| What | Value |
|---|---|
| `APP_ENV` (`shopware/.env`) | `dev` |
| `<plugin>.config.liveModeEnabled` | `false` |
| `<prefix>_supplier.environment`, all four rows | `sandbox` |

A host allowlist would be a false comfort here, and the measurement says why. Both suppliers carry the same base URL as their sandbox base URL and as their live one. The same host answers both, and which it is depends on the credential and the header, not on the address. A guard that inspects the URL would pass a live request through while reporting that it had checked. The environment, resolved once, is the fact worth guarding. The URL is not.

A session incident (16.09.2026): while establishing how supplier contact details reach the plugin, a probe script was written that called `/supplier` and `/whoami` on all three connections with their stored credentials, and then a second and a third one to work out which capability header widened the response. The measurements were correct and genuinely useful: they showed that one supplier answers `/supplier` where the reference says it does not, that another answers neither, and that the payload grows from 264 bytes to 64,823 with the content capability. That does not make the method acceptable. The merchant's instruction of 16.09.2026 was: "Never use the live API again." The reasons are not hypothetical:

- The keys in `.env.local` and in the supplier table are real credentials for real connections. The shop is a reseller of record, and the supplier sees the calls.
- "Sandbox" is not a safe word here. Two suppliers point at the same host as production, separated only by a key and an `Octo-Env` header. The environment guard exists precisely because that separation is one header wide.
- A read today is a write tomorrow. The same reflex that runs `GET /supplier` to check a field runs `POST /bookings` to check a response shape, and that one reaches a real booking system.
- Rate limits and quotas belong to the merchant, not to the session diagnosing something.

On 17.09.2026 the merchant extended this into a permanent, non-negotiable project safety invariant, instructed as absolute and never to be broken. It outranks every task, every TODO entry, every existing implementation, every test and every comment in the repository. Where anything in the project asks for the opposite, the project is wrong and this decision stands. It extends the ban on calling a supplier's live API: that one forbade the request, this one forbids reaching the state from which a request could be live at all.

A live request is not a read. It carries a real key, counts against a quota a merchant pays for, and a write reaches a real booking system: a reservation somebody is charged for, against capacity somebody else could have bought. There is no version of that which is undone afterwards by noticing it.

### Decision

Environment resolution:

- Live requests require two conditions at once: `APP_ENV` is `prod`, and live mode is enabled in the plugin configuration.
- When either is false, every request goes to the sandbox: the sandbox host, the sandbox credential, and `Octo-Env: test` where the provider supports it. The supplier's own `environment` column cannot override this. It is read only after both conditions hold.
- The resolver is the single place where the question is answered, and every provider call goes through it.
- The `Octo-Env` response header is compared against what was requested, and the result is stored on `<prefix>_api_operation` as `environment_requested` and `environment_applied`. A booking made in test mode carries `test_mode = true` regardless of what was asked for.

Write guard for connectors:

- Every POST, PUT and DELETE (login excepted) passes `WriteGuard::assertAllowed()` before every HTTP call, inside the client's `send()`. There is no second way.
- A write is allowed only if all of the following hold: `writesEnabled` is on, `allowedWriteHost` is set and matches the configured host, and the kernel environment is `prod` or `allowNonProductionWrites` is on.
- Everything else raises a `WriteBlockedException` with a reason (`writes_disabled`, `no_allowed_host`, `host_mismatch`, `non_production_environment`) and writes a warning to the plugin's log channel.
- All switches are off by default.

Rules for development sessions:

- **A development session never calls a supplier endpoint. There is no exception and no threshold.** Not with `curl`, not through a PHP probe, not through the plugin's own client, not "once to check a field name", not in sandbox, not with a read-only verb. Where autonomous work has been instructed, the question is not put to the merchant either, the answer is already no.
- Where an API fact is needed it comes from, in order: first the captured responses in `docs/` (the product payloads for all suppliers plus the captured supplier and whoami responses), second the references of the API skill, generated from the OpenAPI document and verifiable field by field through `FIELD-INDEX.json`, third, where neither answers it, build for the documented shape, record the assumption in CONTEXT.md and name it in the closing report.
- A gap in the references is closed by capturing a response the merchant runs themselves (as the supplier payload was, from a Postman window) and committing it to `docs/`.
- **`APP_ENV` stays `dev`.** It is never set to `prod` or `production`, not in `.env`, not in `.env.local`, not per command, not exported for a single invocation, and not "temporarily".
- **Suppliers stay in sandbox.** `<prefix>_supplier.environment` is never written to `live`, and `<plugin>.config.liveModeEnabled` is never switched on, including switching it on and back. A configuration set and reverted is a configuration that was live while it stood.
- **No provider endpoint is ever changed.** Only the sandbox and test endpoints the project already carries are used. A live, production or alternative base URL is never researched, never entered and never called. Where a task needs an endpoint the project does not already have as sandbox, that external interaction is not performed. It is built against mocks, stubs, fixtures or the captured payloads in `docs/`, and whatever remains is recorded as blocked by this invariant.
- **No live request, of any shape.** Not a booking, reservation, order or payment, not a connectivity, smoke, integration, end-to-end or manual check, not a single call "to see what it answers", not an automated test. Not once, not briefly, not to analyse behaviour.
- **No test may need a live endpoint to pass.** Tests run locally, against mocks and fixtures, or against the sandbox systems the project already provides. Live behaviour is proved with stubs: `EnvironmentResolverTest` does exactly that, asserting the `prod` plus live mode branch without any environment being `prod`. Testing the live mode itself is forbidden, testing the guard is required, and it costs no request.
- **Fail closed, on every uncertainty.** Where it is not plainly established that an endpoint, credential, environment or mode is sandbox, it is not used. Not tried, not probed, not inferred from a response, not assumed to be sandbox because it probably is. Only a configuration identified unambiguously as dev, sandbox or test is used for external communication. An unknown configuration is refused, never permitted by default.
- **Where code is touched near this, a guard is preferred over a convention.** An environment guard, an allowlist of endpoints explicitly permitted as sandbox, a refusal on `APP_ENV=prod`, a refusal on an endpoint recognised as live: each implemented fail closed, each tested locally with no real request. A guard that permits what it does not recognise is not a guard.
- **Live verification is outside the responsibility of an AI coding session, permanently.** Whatever can only be established against a live system is established by a person who has decided to do so, with the consequences in front of them. It is never arranged, prepared or triggered from a session.

### Consequences

- A production dump on a developer machine is harmless: it talks to the sandbox whatever it contains.
- A merchant cannot accidentally go live by flipping a supplier setting. Going live is a deliberate act in the plugin configuration, on a production system.
- Testing against the live environment is impossible by design. Where that is genuinely needed (a supplier's go-live review, for instance), it happens on the production system with live mode on and `Octo-Env: test`, which the API supports for exactly this purpose.
- The stored `environment_applied` answers the support question that otherwise costs a day: a booking confirmed here but absent from the supplier's system is usually a connection the supplier forced into test mode, not a bug.
- Read-only synchronisations of a connector run everywhere, writes need three deliberate settings. The decision of the guard is also available as `decide()` for the dashboard.
- The plugin's own runtime is untouched: the HTTP client calls suppliers because that is the product. This rule governs what a session does while developing it.
- `docs/` becomes the more valuable for it and stays the first place to look. Three supplier responses were added on 16.09.2026, and whatever is missing next is added the same way.
- Where a reference and reality disagree, reality is recorded rather than re-fetched. The `/supplier` finding is written into the case ADR with the numbers behind it, so no future session has a reason to call the endpoint again to satisfy the same doubt.
- Verification shifts to what it should have been: the integration suite against the real DAL, the captured payloads as fixtures, and a browser on the administration.
- A task whose completion would require a production request is not completed that far. What is safe is built, the external interaction is replaced by a mock, stub or test double, the remainder is recorded in `TODO.md` and `CONTEXT.md` as blocked by this invariant, and work continues with the next task. An unfinished task is always better than a production request, and a task marked done that reached a live system is worse than either.
- A badge on the ticket page rests on this: with `APP_ENV=dev` and live mode off, `resolve()` returns sandbox for every supplier, so every ticket in this shop is a sandbox ticket and wears the badge. That is not a defect to be tuned away. It is this invariant, shown on the page.
- This decision is never superseded by a TODO entry, an implementation requirement, a review comment or any other project instruction. A future decision that touches it changes nothing until this file says so.

## exported-settings-carry-no-secrets: Exported settings are portable, carry no secrets and delete nothing

**Area:** administration **Status:** accepted

### Context

In a tools tab all settings per sales channel and the registry (groups, services, cookies, custom scripts) are to be exported as JSON and imported again in another shop. IDs differ between shops, and so do languages and sales channels. The core import/export works with CSV profiles per entity and knows no plugin configuration.

The entities of the plugin are not versioned. A wrong change to settings, groups, services, cookies or custom scripts could until now only be undone through a manually exported state. The merchant wants automatic backups with a button to restore.

### Decision

Export and import:

- **Routes:** `GET /api/_action/<prefix>/settings/export` (ACL `system_config:read`, read group and service) and `POST /api/_action/<prefix>/settings/import` (ACL `system_config:update`, `system_config:create`, edit group and service). For new entries the DAL additionally checks with the rights of the user.
- **Format** `<prefix>-settings`, version 1. Groups and services are matched by technical name, cookies by service and name, scripts by name. Translations are keyed per locale code, not per language ID.
- **No secrets:** fields of type `password` from `config.xml` (through the core `ConfigurationService`) and runtime values (`ocdLastImportAt`, `ocdLastImportCount`, `translationQuotaExceededAt`) are neither exported nor imported.
- **Check first, then write:** `SettingsPayloadValidator` checks the whole file. On errors nothing is written (`SettingsTransferException`, 400). After that `SettingsImporter` writes groups, services with cookies, scripts and configuration in one database transaction.
- **Nothing is deleted** and the `system` flag is never imported. Unknown languages, sales channels and entries of the Open Cookie Database are skipped and reported as a notice.

Snapshots:

- A snapshot is the settings export (`SettingsExporter`) as JSON in the entity `<prefix>_settings_snapshot`, with checksum, summary, reason and user. API keys and passwords are never included, as with the export.
- Triggers are only changes by an admin user. A subscriber remembers per request that something changed and sends a message with a 15 second delay into the queue. A save with many single values thus yields one snapshot. If the state equals the last snapshot, none is created. Translations from DeepL, tasks and imports without a user trigger no snapshot.
- The last 20 snapshots are kept. The plugin deletes older ones when creating a new one.
- Restoring first saves the current state and then imports the snapshot through the `SettingsImporter`. The same check and the same rules apply as when importing a file.
- The list loads only time, reason, summary and user, not the content.

### Consequences

A setup can be moved from a test shop to the live shop without API keys ending up in files. A faulty import leaves no half state.

Restoring resets all contained values. What was newly created after the snapshot stays, because the import deletes nothing. This is stated in the hint of the card. The user is stored only as a reference. If the user is deleted, the snapshot remains without a user.
