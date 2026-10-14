# Plugin rules: Administration and storefront

## Contents

- [nothing-in-the-administration-is-small: No component in the plugin's administration is rendered small, and everything sits inside the card frame](#nothing-in-the-administration-is-small-no-component-in-the-plugins-administration-is-rendered-small-and-everything-sits-inside-the-card-frame)
- [administration-built-from-core-components: The administration is built from core components, core icons and core services only](#administration-built-from-core-components-the-administration-is-built-from-core-components-core-icons-and-core-services-only)
- [every-listing-has-an-empty-state: Every entity listing shows a centered empty state](#every-listing-has-an-empty-state-every-entity-listing-shows-a-centered-empty-state)
- [minimal-storefront-overrides: The storefront is overridden as little as possible, templates only extend named blocks and render](#minimal-storefront-overrides-the-storefront-is-overridden-as-little-as-possible-templates-only-extend-named-blocks-and-render)
- [accessibility-and-semantic-markup: Storefront and administration output is accessible and uses semantic markup](#accessibility-and-semantic-markup-storefront-and-administration-output-is-accessible-and-uses-semantic-markup)
- [structured-data-only-where-the-page-shows-it: Structured data is emitted only where the page shows it](#structured-data-only-where-the-page-shows-it-structured-data-is-emitted-only-where-the-page-shows-it)
- [the-buyer-never-has-to-guess: The buyer never has to guess why something happens or what is missing](#the-buyer-never-has-to-guess-the-buyer-never-has-to-guess-why-something-happens-or-what-is-missing)
- [every-change-is-verified-in-the-browser: Every change is verified in a real browser, the way a person uses it, and an element counts as done only when a layout carries it](#every-change-is-verified-in-the-browser-every-change-is-verified-in-a-real-browser-the-way-a-person-uses-it-and-an-element-counts-as-done-only-when-a-layout-carries-it)

## nothing-in-the-administration-is-small: No component in the plugin's administration is rendered small, and everything sits inside the card frame

**Area:** administration **Status:** accepted

### Context

`mt-button` defaults to `size="small"`. A button that says nothing about its size is therefore **32 pixels tall with 12 pixel text**, while the other controls of a bar, such as `sw-language-switch` in the same smart bar, are 40 pixels tall with 14 pixel text.

Measured on a list page before this was settled, the "add" button stood at 32px against the language switch's 40px, and sat four pixels lower than the control it was aligned with. Nothing was wrong with either component. They simply belong to two different size scales, and the smaller one reads as an afterthought, as though the page were bolted onto the administration rather than part of it.

The core's own pages use `size="small"` 355 times, so following the core here would reproduce exactly the mismatch above. The plugin's surfaces sit inside Shopware's own settings area, directly beside core controls, and a merchant moving between them should not be able to tell which page a plugin wrote.

Tabs, notices and two-column card rows also stood at full width while individual cards are limited to 60rem.

### Decision

**No component in the plugin is rendered small.** Not `size="small"`, not `size="x-small"`, and not by leaving a size unset where the component defaults to one.

Every `mt-button` the plugin renders carries **`size="default"`**, explicitly, because the default of the component is not the default of the plugin. A component with no size property of its own (`mt-switch`, `mt-text-field`, `mt-number-field`) is left alone, because it already renders at the height the core's own forms use.

The rule governs what **the plugin** renders. A core component the plugin places but does not control (`sw-media-upload-v2` renders two small buttons of its own) is not overridden for this. Reaching into another component's markup to change its sizing is a bigger fault than the inconsistency it would fix. Sibling plugins of the same developer leave those alone too.

**One frame for everything.** The tabs and the content area of the module are limited to 60rem and centered, like the Meteor cards. Cards inside the frame use its full width. Notices, card rows and tables therefore sit on the same line.

### Consequences

A button added later inherits the wrong size unless somebody writes `size="default"` on it, and nothing in the toolchain says so: the page renders, every test passes, and the button is simply eight pixels short. A Jest test therefore reads every template off disk and asserts that every `mt-button` carries a size and that no component uses `small`. A list of known buttons would leave the next one out.

Pages are slightly taller than the core's equivalents. That is the trade being made, and it is deliberate: a merchant reads these pages next to `sw-settings-*`, not next to each other.

The rule is stated in the `CLAUDE.md` of each plugin that carries it, and recorded again in the plugin's own ADR so it survives a session that never reads the other one.

> Earlier variant: In a plugin for Shopware 6.6, the blanket rule "nothing small" was not adopted, because the 6.6 core itself uses small buttons and fields. There the size is not a rule (see administration-built-from-core-components).

## administration-built-from-core-components: The administration is built from core components, core icons and core services only

**Area:** administration **Status:** accepted

### Context

The 6.6 administration is Vue 3 with `@vue/compat` and Vuex. Components that the core does not use can change between minor versions or disappear, and a custom look makes the plugin feel foreign. The core itself uses small buttons and fields, so size is not a rule in 6.6.

An administration module for a cookie and tracking plugin has six tabs, a sales channel switch and a save button in the smart bar. Settings should inherit per sales channel as in the core. But `sw-system-config` always renders all cards of a domain and has no card filter. Several configuration files would change the keys (`<Plugin>.config.*`).

A second step adds the tabs "Services & cookies", "Logs & scanner" and "Tools" as well as a card in the order. It needs a two-level list (group, services), a detail page with a language switch, search types for the global search and the creation of services from the Open Cookie Database.

### Decision

**Core components and icons**

- Only components that the 6.6 core administration itself uses are allowed. The reference is `<shop>/vendor/shopware/administration/Resources/app/administration/src`, looked up before a component is used. `src/convention/components.spec.js` fails on any other tag.
- Icons come from the core icon set. The plugin ships no icon set of its own.
- Detail pages have no edit mode. Fields are editable on load, the page has a save and a cancel action, and the dirty state is shown.
- Snippet placeholders use single curly braces: `{name}`, never `{{name}}`.
- Snippet keys follow the core schema for modules, components and blocks.
- The empty state of every entity list is centered vertically and horizontally (see every-listing-has-an-empty-state).
- Never Pinia or `Shopware.Store`. In 6.6 the Vuex `Shopware.State` is used.

**System config module on core components**

- **Named cards:** Every card in `config.xml` carries a `<name>` (`consentBanner`, `consentMode`, `consentLog`, `openCookieDatabase`, `translation`). The earlier card "Consent" is split into three cards, the keys stay the same.
- **`<plugin>-system-config`** extends `sw-system-config` with `Component.extend` by the prop `cards` (filters by `card.name` in `readConfig`), follows the prop `salesChannelId`, always loads the values of "All sales channels" as well, reports the effective values (`effective-config-changed`) and offers `hasUnsavedChanges()` and `discardChanges()`. Inheritance, fields and saving remain entirely core.
- **Frame `<plugin>-index`:** `sw-page`, `sw-sales-channel-switch` (with the core's `abortChangeFunction` and `saveChangesFunction`), `sw-button-process`, `mt-tabs`, routes `<plugin>.index.<tab>`. Unsaved changes on a tab or page change are caught by `beforeRouteUpdate` and `beforeRouteLeave` with `sw-discard-changes-modal`.
- **Contract for the tabs** (`page/<plugin>-index/tab-contract.js`): Every tab receives the prop `salesChannelId`. A saving tab injects `<plugin>RegisterTab` and registers `{ save, isDirty, discard }`. The return value unregisters it again. `<plugin>OpenFirstRunAssistant` opens the setup assistant.
- **Setup assistant:** A modal, shown once, flagged by `<Plugin>.config.firstRunAssistantDone`. It writes only global values (All sales channels) and the placeholder keys `ga4MeasurementIds` and `gtmContainerIds` as lists.
- **Statistics:** `GET /api/_action/<plugin>/statistics` counts the decisions of the last 30 days in the consent log by DBAL aggregation, cached for 15 minutes in the object cache. Only services outside the group "required" are rated: all granted = "All accepted", none granted = "All rejected", otherwise "Individual". The DAL cannot aggregate JSON contents, hence DBAL.

**Services tab, detail page and order card on core building blocks**

- **List:** Groups as expandable sections with `mt-badge`, `mt-switch` and `sw-context-button`. `sw-tree` does not fit, because it brings moving and category logic. Filters use admin Criteria. "Translation missing" filters on the result of the state route.
- **Detail page** as its own route `<plugin>.detail` (`sw-page`, core `sw-language-switch`, `sw-language-info`, `sw-entity-multi-select` for sales channels). Saving uses the core repository.
- **Creating via the Sync API:** The dialog "Add service" (OCD search through the repository `<prefix>_ocd`, grouping by platform, the category determines the group and the consent mode types, the storage duration is parsed from the free text) and the group dialog write through the core Sync API, because they have to write translation rows per language.
- **Search types:** The module `<plugin>` carries the entity `<prefix>_service`. A second, invisible module `<plugin>-cookie` carries `<prefix>_cookie` and redirects to the service. Both are registered through the core `searchTypeService`, the weighting is in `search/default-search-configuration.js`.
- **Unknown cookies:** "Assign to suggestion" adds a service of the same platform or opens the dialog with the platform. "Choose service" and "Ignore" set the state. The scanner itself is delivered by step 11.
- **Order card:** `sw-order-detail` extends `orderCriteria` by the tracking association (only with read permission), `sw-order-detail-general` attaches the card with `{% parent %}`. It is read-only and disappears without data.
- **Tools:** The cards `openCookieDatabase` and `translation` come from `config.xml` through `<plugin>-system-config` (including the connection test). "Update now" calls `POST /api/_action/<plugin>/open-cookie-database/update` (ACL `system_config:update`), which schedules `ImportOpenCookieDatabaseMessage`. Legacy data import and debug session are disabled until step 12 and step 11 respectively. The path of the legacy route is the constant `LEGACY_IMPORT_DRY_RUN_PATH`.

### Consequences

The administration looks and behaves like core pages, and the switch to 6.7 is planned in the upgrade guide. The blanket rule "nothing small" is not adopted for 6.6, because the core does not follow it.

Every card from `config.xml` can be shown in exactly the tab it belongs in, without form logic of its own. New tabs register through the contract and get saving, channel switching and protection against data loss for free. The extension depends on the core methods `readConfig`, `loadCurrentSalesChannelConfig`, `getChangedConfigData` and the core data `actualConfigData` and `initialConfigData`. A core update checks this through the Jest and E2E tests.

All building blocks are core components and core services. Custom logic exists only where translation rows have to be written per language. The editor role may create new translation rows (`*_translation:create`), otherwise it could not fill a language for the first time.

## every-listing-has-an-empty-state: Every entity listing shows a centered empty state

**Area:** administration **Status:** accepted

### Context

The core `sw-empty-state` is positioned absolutely by default and centers only within a page content area. In cards and tabs it sticks to the top or collapses.

### Decision

- Every list of the module (runs, log lines, mappings, entries that cannot be assigned, price rules, entity log, legacy runs, synchronization types) renders the component `<plugin>-empty-state` when it has no rows and is not loading.
- The component wraps the core `sw-empty-state` (not absolute, automatic height) in a flex container with `align-items` and `justify-content` set to center and a minimum height, so that the state is centered vertically and horizontally in every container.
- Title and subline always explain why the list is empty and what fills it.

### Consequences

One component carries the rule, and a spec checks that grids are replaced by the empty state. New lists use it again.

## minimal-storefront-overrides: The storefront is overridden as little as possible, templates only extend named blocks and render

**Area:** storefront **Status:** accepted

### Context

Every overridden Twig file and every overridden JS plugin has to be checked on every Shopware update and can collide with themes or other plugins. Logic in Twig is unreachable for PHP tests. Earlier steps had replaced blocks of the core cookie bar and of the settings offcanvas and overridden the YouTube and Vimeo elements.

The risk is theme compatibility. A shop runs its own theme, often a heavily customized one. A plugin that replaces templates wholesale breaks on the next theme update, and a plugin that ships its own JavaScript competes with the theme's. Plugin compatibility is also asked for explicitly in the specification. Two specification chapters require storefront output, namely badges and labels on dropshipping products and the communication of split shipments to the customer (an order arriving in several parcels needs an honest delivery expectation).

There is also a business consideration: not every merchant wants dropshipping visible to customers at all. Whether the storefront reveals that an item ships from a third party is the merchant's decision, not the plugin's.

In one plugin, everything happens in `offcanvas-cart.html.twig`: finding the free shipping row in the shipping method's price matrix, comparing it against the cart, computing the remaining amount and the progress percentage. Twenty lines of `{% set %}`. No PHP test can reach any of it. The one test that exists, `tests/CalculationTest.php`, reimplements the same arithmetic in PHP and asserts that its own copy behaves. It carries `#[CoversNothing]` and earns the label. If the template were changed to divide where it subtracts, the test would stay green and the shop would show a wrong number. A later version adds discount tiers, which would double that untestable surface.

A connector plugin synchronizes data. The only storefront output that could belong to it is the warranty label (GARAN) and the manufacturer data that the product safety regulation requires. Shopware 6.6.10.26 renders the warranty label itself. The core fields `guaranteeMonths`, `guaranteeConfirmed`, the manufacturer name and `manufacturerNumber` are read in `storefront/Resources/views/storefront/component/buy-widget/buy-widget.html.twig` (block `buy_widget_garan_label`) and by `GaranLabelResolver` for line items, while the JavaScript plugin `GaranLabelToggle` is registered by the core storefront. Core 6.6.10.26 contains no storefront output for the manufacturer address or the data of the responsible person. The legacy connector produced no storefront output of its own. Its manufacturer and product additional fields are read by the theme of the shop. The decisions "templates only render", "only named blocks" and "the plugin builds nothing that Shopware 6.6 does not yet use" forbid a copy of the core label or a replacement for core output.

A tracking plugin needs `view_promotion` and `select_promotion` with a promotion name for each image, image slider and image gallery. The storefront code reads promotions from the attribute `data-<plugin>-promotion`. The obvious solution would be an override of the three element templates. The core in 6.7 knows no banner element. "Banner" is an image block there.

A previous decision foresaw a block override and `window.gtagActive = false` to replace the core Google Analytics. An override contradicts the rule of as few storefront overrides as possible, and `window.gtagActive` alone leaves the core inline script and the enhanced conversions block standing on the order confirmation page.

### Decision

**Integration happens through core data, core events, snippets and own JS plugins. Templates are extended only where there is no other way, and then only with `parent()`.**

| Place | Implementation |
|---|---|
| Cookie bar | no override. Core bar with its three equal buttons, different texts only through snippets |
| Settings | no override. Provider, purpose, privacy link and cookies are in the `description` of the core `CookieEntry` |
| YouTube, Vimeo | no override. Core mechanism `CmsGdprVideoElement` with the core cookies `youtube-video` and `vimeo-video` |
| Consent runtime | `layout/meta.html.twig`, one block, with `parent()` |
| Withdrawal button, own scripts | `base.html.twig`, one block, with `parent()` |
| Script blocking | server side during rendering, no template change |
| JavaScript | only own plugins (`<Prefix>Consent*`), no core plugin is overridden. Access to core internals only in the adapter |

Further rules:

- Templates use `sw_extends` and override only named core blocks, and the core output is always preserved with `parent()`. No core template is replaced as a whole and none is copied. Where a desired insertion point has no block, the display is adapted rather than the core template copied.
- The plugin's output lives in its own blocks with a prefix, so that a theme can adapt it without touching core blocks.
- Templates render and do not compute. A service builds a struct, and the template reads its properties. **A `{% set %}` that performs arithmetic is a defect.** The template may branch on what it is handed and format it, but it may not compute it.
- No core JavaScript plugin is overridden. The plugin adds its own storefront plugin only where needed. In a first version there is no custom JavaScript at all. Availability shown in the storefront comes from cached server-side data, so nothing needs to be fetched client side. Richer interactions (live availability, in-page shipment tracking) are deferred and, if added later, arrive as an opt-in JavaScript plugin and not as a change to the baseline.
- Icons come from the core icon set.
- Twig never reads a boolean configuration with `??`. It uses `config('X.config.y') is not same as(false)`. `CodingStyleTest` fails on `config(...) ??`.
- All customer-facing text comes from storefront snippets, so it is translatable and overridable without touching templates.
- Every storefront output is switchable off by configuration. The default for dropshipping-specific labelling is off.
- Delivery time display accounts for split shipments by showing the slowest group, not a per-item figure that would mislead.

**Calculations move into PHP.** A page subscriber computes a struct and puts it on the page, the template reads its properties and renders. Example split for a free shipping progress feature:

| Class | Answers |
|---|---|
| `FreeShippingThresholdResolver` | which row of the price matrix is the free shipping row, and at what amount |
| `DiscountTierCollection` | which tiers are configured, sorted and valid |
| `CartProgressCalculator` | how far to free shipping, which tier is active, which is next |
| `CartProgressSubscriber` | puts the result on the page |

**A plugin that only synchronizes data ships no storefront templates.**

- The plugin ships no storefront templates, no Twig extensions, no SCSS and no storefront JavaScript plugin.
- `src/Resources/app/storefront/src/main.js` stays a minimal entry point that exports a helper and registers nothing. The storefront toolchain (Jest, ESLint, Prettier, Stylelint) stays in place with thresholds of 100 % for code added later.
- The warranty label is rendered by the core from the synchronized fields. The synchronization only has to fill `guaranteeMonths`, `guaranteeConfirmed`, the manufacturer and `manufacturerNumber`.
- Manufacturer data for the product safety regulation is synchronized into the legacy additional fields of the manufacturer. A theme or project reads them. The plugin adds no template for it until the core renders such data.
- A storefront feature is added only if a later core line or a documented requirement leaves output uncovered, and then exclusively through named blocks.

**Promotion data hangs on the CMS element and reaches the storefront without a template override**

- **Admin:** `Component.override` of the core configurations `sw-cms-el-config-image`, `sw-cms-el-config-image-slider` and `sw-cms-el-config-image-gallery`. In each, exactly one block is extended with `{% parent %}` (`sw_cms_element_image_config_link`, `sw_cms_element_image_slider_config_tabs`, `sw_cms_element_image_gallery_config_tabs`) and supplemented by `<plugin>-cms-promotion-config`. The values live in the slot configuration under `<prefix>PromotionName` and `<prefix>CreativeName` (`{ source: 'static', value }`, translatable like every slot configuration). The chosen block of the slider and the gallery encloses both branches of the feature flag `v6.8.0.0`, so the extension survives 6.8.
- **Storefront without override:** All core blocks wrap every element with `data-cms-element-id="{{ element.id }}"`. `TrackingPageDataBuilder` collects the promotions of the CMS page (product, category and landing page) as `TrackingPromotion` in the page extension. The tracking JSON contains them as `promotions` per slot ID. `<Prefix>ConsentTrackingPlugin::_markPromotions()` sets the attribute `data-<plugin>-promotion` on the elements with that ID before the browser events start. An attribute that a custom template already sets stays unchanged.
- Without a promotion name no event is created. If `view_promotion` and `select_promotion` are switched off, nothing is output.

**Core analytics is suppressed through the render event, not through a template.** `CoreAnalyticsSuppressionSubscriber` listens to `StorefrontRenderEvent` with priority 1000, that is after the core loader (2000), and sets the parameter `storefrontAnalytics` to `null` as long as the plugin outputs Google tags in the channel. As a result the core renders neither `component/analytics.html.twig` nor `window.gtagActive`, does not register its `GoogleAnalytics` plugin and outputs no enhanced conversions data. The core loader itself is `@internal` and is not used. The core values are only read in step 12. This replaces the suppression decision of the earlier decision "core Google Analytics is replaced".

If a service description changes, the core asks again through the `cookie-config-hash`. That is intended: the information that was agreed to has changed. Automatic translations change texts only when the English source changes.

### Consequences

The plugin survives core updates and themes considerably more robustly, and themes keep working across updates. The rules are testable in PHP, and templates are checked for what they render. Translations follow the standard snippet mechanism.

Easier: merchants control visibility. Harder: block overrides can only extend where the core template defines a block.

For the cookie plugin: The imprint link in the bar is dropped (it is in the footer), "Reject all" in the offcanvas is dropped (saving without a selection has the same effect). "Accept all cookies" is shown by the core only with the setting `core.basicInformation.acceptAllCookies`. Core videos are only protected with "Confirmation required". Script blocking leaves their iframes unchanged. This decision replaces the corresponding parts of the earlier decisions on the consent runtime on the core bar and on own placeholders for embeds.

For the promotion mechanism: No storefront template is overridden, and themes with their own element templates keep working as long as the core block wraps the element. The three admin components are `@private` in the core. If Shopware changes the blocks, the extension has to follow (check point in `docs/UPGRADE-6.8.md`). Elements from app renderer blocks carry no element ID and get promotion events only if their template sets the attribute itself.

For core analytics: no template override. If an old plugin is responsible or Google is off, the core analytics stays unchanged.

For the arithmetic move: A file that is live in customer shops gets rewritten. The rendered markup must stay byte-identical for a shop with no tiers configured, and only the Playwright suite can prove that, which is why that suite is a precondition for the refactoring, not a follow-up. The threshold detection was never specified, only implemented. Moving it into PHP forces the rule into words: `calculation === 2`, `quantityEnd is null`, rule matches or is null, price gross and net both zero. Writing it down is likely to surface cases the template got wrong. Twig gains an indirection: a reader of the template no longer sees where the numbers come from, so the struct's property names have to carry that meaning on their own.

For the data-only plugin: It cannot collide with themes or break on template changes in the core. Pages stay as fast and cacheable as the core makes them, and the accessibility of the label remains the job of the core markup. Shops that want to show manufacturer data for product safety need a theme extension, which `docs/STOREFRONT.md` describes.

## accessibility-and-semantic-markup: Storefront and administration output is accessible and uses semantic markup

**Area:** storefront **Status:** accepted

### Context

In Germany the BFSG applies to online shops and is measured in practice against EN 301 549 and therefore against the WCAG success criteria. Plugin output that is not accessible makes the whole shop page non-conforming.

The BFSG has applied since June 2025 to online shops that sell to consumers in Germany. A dialog that traps the keyboard, or that confirms a sign-up in markup that no screen reader reads out, misses a legal requirement.

Shopware's pseudo modal already does most of this. Two gaps remain: The close button carries `aria-label="Close"` as a hard-wired English string, and the feedback of the form handler is markup without a live region. In addition the core returns focus with `el.focus()` without options, which scrolls the page.

### Decision

**Output rules**

- The output uses semantic HTML: headings in order, lists for lists, tables with header cells for tabular data, real links for navigation and real buttons for actions.
- Links are not recognizable by color alone. Focus is visible and managed, and it returns to the trigger after a dialog or offcanvas closes.
- The output reflows at a width of 320 CSS pixels without horizontal scrolling. Long values are wrapped.
- Every control and every image has an accessible name. Repeated controls in rows are named per row. A link that opens a new window says so.
- Status and error messages use the appropriate ARIA role so that assistive technology announces them.
- The administration follows the core components that carry accessible names, and custom controls receive labels.
- End-to-end tests find elements by role and label, which doubles as an accessibility check.

**A modal is operable without a mouse and without a screen. It meets WCAG 2.1 AA on the paths the plugin is responsible for.**

| Requirement | Met by | Secured by |
|---|---|---|
| announced as a dialog | core: `role="dialog"`, `aria-modal` | core |
| accessible name | title element moves into the header | template test |
| described by its own text | `aria-describedby` | template test |
| trigger announces the dialog | `aria-haspopup="dialog"` | Jest spec |
| Escape closes, focus trapped | Bootstrap modal | core |
| focus returns without scrolling | plugin, `preventScroll: true` | Jest spec |
| result is announced | `role="status"`, `aria-live="polite"` | Jest spec |
| close button in the shop language | override of `pseudo-modal.html.twig` | template test |
| no dead end in the nested dialog | `data-prev-url` | Jest spec |
| works without JavaScript | trigger stays a real link | E2E test |

**The template override translates only the close label.** It is checked after every Shopware update and is dropped as soon as the core translates it itself.

**The feedback is announced.** Without a live region, a screen reader user submits and learns nothing. A role that is already present is left untouched.

**An axe check runs in the end-to-end suite**, over the opened modal and over the modal after a successful sign-up, because the confirmation would otherwise never be checked.

### Consequences

Users of screen readers and keyboards get the same information and controls as everyone else.

The plugin overrides a core template that it would otherwise leave alone. That costs attention on every update and is the price for no screen reader user hearing an English word in every dialog.

The axe check also reports theme faults, such as contrast values, because the colors come from the theme. These are passed on, not silenced.

Automatic checks find about half of what matters. Whether the dialog name makes sense to someone who hears it remains a manual check on every markup change.

## structured-data-only-where-the-page-shows-it: Structured data is emitted only where the page shows it

**Area:** storefront **Status:** accepted

### Context

The standing instruction is that every element the plugin builds emits schema.org data wherever that is possible. Four elements can carry some: the FAQ accordion, the map, the itinerary and the nearby list.

Google treats structured data that contradicts the visible page as a violation rather than as a formatting slip. Two measurements made that concrete:

- Of 752 supplier entries under `faqs`, **61 are questions** and 559 are headed notes. Marking all of them up as an `FAQPage` would have put every ticket product at risk.
- Of 304 adopted tickets, **113 have a placed meeting point**. A `Place` without coordinates is worse than no `Place` at all.

### Decision

**Emit nothing rather than something wrong.** A product carrying only headed notes emits no `FAQPage`, and a meeting point without coordinates emits no `Place`. Both are verified in the browser in each direction rather than asserted.

**The switch is the core's own**, `feature('JSON_LD_DATA')`. A plugin that invented one would emit markup in a shop that had deliberately turned structured data off.

**The buy box emits nothing.** Checked in the browser first: the core's `json-ld-product` already emits a complete `Product` with `offers`, `image`, `brand` and `category`. A second `Offer` beside it would be two prices for one product.

**An address is cut at the first line break.** The supplier packs travel directions into the same field, and the second half is not an address. `AddressGeocoder` already cuts at the same place.

**A url from `seoUrl()` is already absolute.** Prefixing `schemeAndHttpHost` produced `https://hosthttps://host/...` on a live page.

**The rules live in a structure test**, `tests/Structure/StructuredDataStructureTest.php`, which reads every storefront template off disk and governs any that emits a `ld+json` block. An element written tomorrow is covered the moment it emits one, without anybody editing the test.

### Consequences

- Four types are emitted: `FAQPage` (questions only), `Place` with `GeoCoordinates`, `TouristTrip` with an `ItemList` of `TouristAttraction`, and an `ItemList` for the nearby element.
- A page may emit none of them and still be correct. That is the point.
- Both faults above were found in a browser and not by any test, which is why they are rules now rather than fixes.

## the-buyer-never-has-to-guess: The buyer never has to guess why something happens or what is missing

**Area:** storefront **Status:** accepted

### Context

Version 2.0.0 of a configurator locked the buy button when something was missing and colored the group red, but did not say what was wrong. A width outside the allowed range was reported only by the cart after submitting. A selection that hid a rule simply disappeared. With calculated values a number changes by itself, which looks like an error if nobody explains it.

Separately, a catalogue import of supplier "FAQ" entries showed that the premise was wrong. The task was written as "the supplier's FAQs, as a Bootstrap accordion with `FAQPage` JSON-LD". 283 of 325 tickets carry entries under `faqs`, 752 in total, and nothing but a read-only list in the administration read them. Measuring them before building anything showed:

| | |
|---|---|
| Entries ending in a question mark | **61** |
| Entries ending in a colon | **559** |
| Neither | 132 |
| With no answer at all | 30 |
| Whose answer carries markup | 309 |

The most common "question" in the catalogue is **"Please note:" (175 times)**, the second **"Schedule:" (125)**. Then "Itinerary:", "Locations:", "Meeting Point:", "Dress Code", "Opening Hours:".

These are not FAQs. They are headed sections of information, and genuinely useful ones: "Accessible car parking", "Bag size policy", "Lifts" tell a guest something they need. The supplier simply has one field for two different kinds of thing.

Per supplier: one sends 713 entries and answers all of them, the other sends 39 and answers 9. All 30 of the unanswered entries belong to the second.

### Decision

**Every field says what it accepts before it is filled in.** A number field shows its range ("200 mm to 1,500 mm") below the input, rendered on the server, so also without JavaScript.

**Every error stands in words at the field** ("At most 1,500 mm."), connected to the input through `aria-describedby`, **but only once the buyer has edited the field** or clicks the notice about missing entries. On first load nothing is red. A separate group notice is dropped, the fields name their errors themselves.

**The buy area says what is missing** ("3 entries still missing"), neutral at first, and a click leads the buyer to the first open field and makes the errors visible. Each missing entry is counted once.

**Automatic values explain themselves.** A calculated value shows why it has this value ("because width from 800 mm"), what the next step is ("From 800 mm: 2 pieces") and, as long as it is empty, what it is derived from ("Calculated automatically from 'Width'.").

**Nothing disappears silently.** A chosen option that hides a rule is deselected, and a notice names it.

**The price is broken down live**: base price, every surcharge, with the calculation for a price per unit with quantity ("2 x 24.50 EUR = 49.00 EUR"), and the total. This happens only with JavaScript. Without it, the buy box and the cart remain authoritative.

**A configurator can be shown as numbered steps** (`layoutMode: steps`) that show a check mark as soon as a group is complete. The list stays the default. The steps are the same markup with numbers and therefore also work without JavaScript.

**The cart reads like a table**: per group the label on top in gray, below it the value and, right aligned, the surcharge, in the font size of the delivery period.

**The merchant checks rules before the buyer sees them.** The detail page has a tab "Preview" that sends the unsaved configuration to `/api/_action/<plugin>/preview`, where the real evaluator, payload builder and validator answer. Notices in plain language mark rules that never or always apply, tiers that are never reached, and quantity sources that can be hidden.

**A heading is not a question: the element renders everything and marks up only the questions.** Both kinds belong on the page, only one of them may carry `FAQPage` markup.

**`FaqKind` decides by the question mark**, because that is the only signal the supplier gives, no field says which kind an entry is. A merchant who disagrees corrects the entry, and correcting it is what takes it over: `maintainedByShop` then keeps every sync off it.

**A product carrying nothing but headed notes emits no structured data at all.** Google treats a `Question` whose text is not one as a violation, and marking all 752 up would have put every ticket product at risk for the sake of 61 real questions.

**An entity, not a JSON column.** The texts have to be translatable and editable, and the DAL can translate neither a column nor a key inside one.

**The heading identifies an entry**, hashed lowercased and trimmed. The supplier sends no id on these, unlike an option, so a second sync run would otherwise add a second copy of all 722 of them. The catalogue carries "Please note:" and "Please Note:" as two spellings of one heading.

**An entry with no text never reaches the page**, and a text of spaces alone counts as none: an accordion row that opens onto nothing is worse than an absent one.

### Consequences

Every text a buyer sees exists as a snippet in de-DE and en-GB.

The storefront plugin grows. Every behavior is a method of its own, and the rule logic stays in `price-calculator.js` and `configuration-validator.js`, which keep the fixtures equal with PHP.

For the FAQ element:

- The storefront heading is **"Good to know"** (German "Gut zu wissen"), not "Frequently asked questions": 661 of the 722 stored entries are notes, and a heading has to describe what is under it.
- `AllowHtml` sits on the answer alone. 309 of 752 answers carry markup the supplier sent, and no heading in the catalogue carries any.
- An entry the supplier drops is deactivated, never deleted. A merchant may have translated it, and a heading that vanishes for one run must not throw that away.
- A backfill was required: 752 entries existed in `raw_snapshot` and only a read-only list read them. 722 were written, the 30 without an answer skipped.
- The same rule now governs every element: never emit what the page does not show (see structured-data-only-where-the-page-shows-it).

## every-change-is-verified-in-the-browser: Every change is verified in a real browser, the way a person uses it, and an element counts as done only when a layout carries it

**Area:** process **Status:** accepted

### Context

Unit tests, Jest and the matrix check whether the code calculates what it should. Whether the merchant and the buyer can cope with it, they do not see. An example from one release: The preview in the admin offered "Gas spring (135 degrees)" although a rule hides it for model 01. The server rejected the choice correctly and reported "no option chosen". Every test at code level was green, and the merchant faced an error message that contradicted their selection.

There was also a fault in the way of working: The preview was operated by script for checking (values set through the component instead of clicked). That way one cannot see what a person sees, and exactly this case would have been missed.

A plugin with full coverage on both halves, enforced by the test runners themselves, has never been enough. Every one of these shipped green:

- An options accordion that rendered nothing but its empty state. A Twig comment between `v-if` and `v-else` separated them, and a stubbed mount never compiles the real template. 58 specs passed.
- Leaflet's stylesheet resolving to nothing, so twelve map tiles lay scattered across a product page. `theme.json` listed a path the SCSS compiler cannot resolve, and **the build still succeeded**.
- A cart charging 140.20 EUR for a 107.68 EUR basket.
- Fare rows quoting 35.89 EUR where the guest pays 33.65 EUR.
- `slot.lockedHint` and `units.lockedHintNoSlot` standing on the page as raw keys.
- "Local time {zone}" verbatim, because Twig replaces `%name%` and not `{name}`.

None of them is a gap in coverage. Each is a thing a test cannot see: a template that is never compiled, a stylesheet that is never built, a snippet that is never resolved, a figure asserted in the state behind the screen rather than on it.

A second gap is specific to CMS work and easy to walk into. The merchant asked to see the "what is nearby" element in the storefront. The honest answer was that it was **nowhere**: built, verified in a browser on a temporary CMS block, merged, and the block deleted after the check. The overview map and the itinerary were in exactly the same state. **Three elements passed every test, had been verified in a browser, were merged, and were invisible to every guest.** A controller answers a route the moment it exists, and a subscriber runs as soon as its event fires. A CMS element does nothing at all until a layout carries it, and nothing in the codebase says whether one does. The verification step even makes it worse: a temporary block proves the element renders, and deleting it afterwards leaves the shop exactly as it was.

### Decision

**Every function, every flow and every change is checked with the Playwright browser MCP before completion, in the administration and in the storefront. A surface is opened in a real browser before it is called done, without exception.**

| Rule | Content |
|---|---|
| Two tabs | Tab 0 administration, tab 1 storefront, switched by tab selection |
| Like a person | click, type, select, drag, scroll through the visible interface |
| Never by script | no `evaluate` to set values, trigger buttons or address components |
| Reading is allowed | snapshot and screenshot to see what is displayed, console for errors |
| Both sides | a setting in the admin is checked in the storefront, and the other way round |
| Also empty input | forgotten fields, limit values, wrong values, rules that hide something |

A shop operator does not write a script to click a button. They click.

**Build first.** `admin-build` or `storefront-build` for the extension, then the page. Without the build the browser shows the previous bundle, so a check that skips it proves the old code works.

**Read the console.** Errors and warnings both.

**Assert the figure where it is rendered**, not in the state behind it. Every currency the shop carries, not one.

**The browser check does not replace a test.** Whatever the browser turns up becomes a test in the same change, at the fitting level, so the next regression is caught before anybody opens a browser again. The Playwright E2E suite later checks the flows automatically (see the decision that an end-to-end test does what a person does).

**A CMS element or block counts as done only when a layout in the shop carries it**, not when it renders on a block created to look at it. Placing it is part of the slice, not a follow-up.

**The placement is recorded where the rest of the state is.** TODO.md and CONTEXT.md name which layout carries which element, and in what order, so the next session can check rather than assume.

**Where a slice deliberately leaves an element unplaced**, because a merchant has to decide where it goes, that is written down as an open point. An unplaced element is a state, not an oversight, but only if somebody said so.

### Consequences

Every task takes longer, because it is finished only after a look into both interfaces, and the work finds things. Of the faults listed above, every single one was found by looking, several of them by the merchant, which is the expensive way. Contradictions between admin, storefront and server are noticed before the team finds them in the test shop.

A task counts as done only when `CONTEXT.md` says what was checked in the browser and with what result.

Some checks cannot be automated afterwards and stay manual: layout, whether a control lines up with the field it belongs to, whether two grays a shade apart read as a mistake. A convention test can assert that a rule exists in a stylesheet, only a browser can say whether the page looks right.

Where a fault is one a test *could* have caught, the test is written rather than the browser check repeated. `src/__conventions__/` exists for exactly this: SCSS is never compiled by Jest, so those specs assert the rules the browser proved were missing.

The test strategy describes the other levels.

A browser check on a temporary block proves the element works. It does not prove the shop shows it, and the two are separate questions.

- The ticket layout carries, in order: heading, gallery and buy box, map, itinerary, nearby, questions and notes, description.
- The overview map has a page and a navigation entry of its own (`/Karte/`), which is also what made the channel boundary visible: the same page renders 104 pins in the London shop and nothing in the New York one.
