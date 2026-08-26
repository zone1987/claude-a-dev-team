<!-- distilled from shopware/storefront and shopware/core v6.7.13.1 — Content/Cookie/, Framework/Cookie/, layout/cookie/, plugin/cookie/ -->

# Shopware Storefront — the cookie consent banner

How a cookie reaches the consent dialogue, from the PHP that declares it to the JavaScript that acts
on the visitor's choice. Anything setting a cookie or loading a third-party script has to enter
through this chain — that is what makes consent enforceable rather than decorative.

## Contents

- [The chain end to end](#the-chain-end-to-end)
- [Where groups and cookies are declared](#where-groups-and-cookies-are-declared)
- [The default groups](#the-default-groups)
- [Adding your own cookie: the current way](#adding-your-own-cookie-the-current-way)
- [The structs](#the-structs)
- [Adding a whole group](#adding-a-whole-group)
- [Apps declare cookies in the manifest](#apps-declare-cookies-in-the-manifest)
- [The deprecated CookieProvider](#the-deprecated-cookieprovider)
- [Routes and templates](#routes-and-templates)
- [The JavaScript side](#the-javascript-side)
- [Reacting to a consent change](#reacting-to-a-consent-change)
- [Which cookies are actually set](#which-cookies-are-actually-set)
- [The two banner modes](#the-two-banner-modes)
- [Rules for a third-party integration](#rules-for-a-third-party-integration)

## The chain end to end

```
PHP: a listener on CookieGroupCollectEvent
  adds a CookieEntry to a CookieGroup in the CookieGroupCollection
    -> CookieController renders the group tree
    -> layout/cookie/cookie-configuration.html.twig  the off-canvas dialogue
         one checkbox per entry, carrying data-cookie and data-cookie-value
    -> the visitor accepts or declines
    -> cookie-configuration.plugin.js writes the accepted cookies,
       removes the declined ones, stores 'cookie-preference' and a config hash
    -> it publishes COOKIE_CONFIGURATION_UPDATE with { <cookie>: true|false }
    -> your JavaScript subscribes and switches its behaviour
```

Every step is extensible, and the first one is where a new cookie enters.

## Where groups and cookies are declared

`core/Content/Cookie/`:

| File | Role |
|---|---|
| `Event/CookieGroupCollectEvent.php` | the extension point — carries the collection and the sales channel context |
| `Service/CookieProvider.php` | builds the default groups and dispatches the event |
| `Struct/CookieGroup.php` | one group |
| `Struct/CookieGroupCollection.php` | all groups |
| `Struct/CookieEntry.php` | one cookie |
| `Struct/CookieEntryCollection.php` | the cookies of a group |

Core listeners that use the event, and are the models to copy:

- `core/Checkout/Customer/Cookie/WishlistCookieCollectListener.php` — conditional on a system config
- `core/System/SalesChannel/Cookie/AnalyticsCookieCollectListener.php` — Google Analytics
- `storefront/Framework/Captcha/CaptchaCookieCollectListener.php` — captcha
- `core/Framework/App/Cookie/AppCookieCollectListener.php` — cookies declared by apps

## The default groups

Four, identified by their snippet name constants on `CookieProvider`:

| Group | Constant | Contains |
|---|---|---|
| Required | `SNIPPET_NAME_COOKIE_GROUP_REQUIRED` | session, `timezone`, `cookie-preference`, `cookie-config-hash` |
| Statistical | `SNIPPET_NAME_COOKIE_GROUP_STATISTICAL` | analytics, filled by listeners |
| Comfort features | `SNIPPET_NAME_COOKIE_GROUP_COMFORT_FEATURES` | `youtube-video`, `vimeo-video`, wishlist |
| Marketing | `SNIPPET_NAME_COOKIE_GROUP_MARKETING` | filled by listeners |

**Required cookies have no checkbox** — they are shown but cannot be declined, because the shop
cannot function without them. Putting a tracking cookie there is the one mistake with legal
consequences.

The session cookie's name is injected at runtime, since it depends on the PHP configuration.

## Adding your own cookie: the current way

Subscribe to `CookieGroupCollectEvent` and add an entry to an existing group:

```php
use Shopware\Core\Content\Cookie\Event\CookieGroupCollectEvent;
use Shopware\Core\Content\Cookie\Service\CookieProvider;
use Shopware\Core\Content\Cookie\Struct\CookieEntry;
use Shopware\Core\Content\Cookie\Struct\CookieEntryCollection;

class MyCookieCollectListener
{
    public function __invoke(CookieGroupCollectEvent $event): void
    {
        // Only offer it where it applies — the event carries the sales channel context.
        $salesChannelId = $event->getSalesChannelContext()->getSalesChannelId();
        if (!$this->systemConfigService->getBool('MyPlugin.config.active', $salesChannelId)) {
            return;
        }

        $group = $event->cookieGroupCollection->get(CookieProvider::SNIPPET_NAME_COOKIE_GROUP_MARKETING);
        if (!$group) {
            return;
        }

        $entries = $group->getEntries();
        if ($entries === null) {
            $entries = new CookieEntryCollection();
            $group->setEntries($entries);
        }

        $entry = new CookieEntry('my-tracking-cookie');
        $entry->name = 'myPlugin.cookieName';          // snippet key
        $entry->description = 'myPlugin.cookieDesc';   // snippet key
        $entry->value = '1';
        $entry->expiration = '30';                     // days
        $entries->add($entry);
    }
}
```

Register it with the `kernel.event_listener` tag for `CookieGroupCollectEvent`.

Three things that are easy to get wrong:

- **Always guard against a missing group.** A group can be absent when another extension removed it.
- **`name` and `description` are snippet keys**, not text. Define them in your snippet file, or the
  dialogue shows the raw key.
- **Check the sales channel.** A multi-channel shop may want the cookie in one channel only.

## The structs

**`CookieEntry`** — constructor takes the cookie name; the rest are public properties:

| Property | Meaning |
|---|---|
| `cookie` | the cookie name, and the key in the consent payload |
| `name` | snippet key for the label |
| `description` | snippet key for the description |
| `value` | the value written on acceptance |
| `expiration` | lifetime in days |

**`CookieGroup`** — constructed with a technical name; carries `name`, `description` and an
`entries` collection. A group may itself be a cookie, but then it must not have children: the
dialogue cannot render both a parent checkbox and child checkboxes meaningfully.

## Adding a whole group

```php
$group = new CookieGroup('my-group');
$group->name = 'myPlugin.groupName';
$group->description = 'myPlugin.groupDesc';
$group->setEntries($entries);
$event->cookieGroupCollection->add($group);
```

Prefer an existing group. A visitor faced with eight groups accepts all of them without reading, and
a new group needs its own justification under GDPR.

## Apps declare cookies in the manifest

An app does not write PHP; it declares cookies in `manifest.xml`, and
`AppCookieCollectListener` turns them into entries. That is why an app's cookies appear in the
dialogue without any code in the project.

## The deprecated CookieProvider

`storefront/Framework/Cookie/CookieProviderInterface.php` and its `CookieProvider` /
`AppCookieProvider` decorators are the **old** mechanism: a service returning a nested array,
extended by decoration.

**Deprecated, removed in 6.8** — use `CookieGroupCollectEvent`. Existing decorations still work
until then, and its array schema is what the templates historically rendered, which is why the
group tree still looks array-shaped in Twig.

## Routes and templates

| Route | Path | Returns |
|---|---|---|
| `frontend.cookie.offcanvas` | `/cookie/offcanvas` | the configuration dialogue |
| `frontend.cookie.permission` | `/cookie/permission` | the small banner |
| `frontend.cookie.consent.offcanvas` | `/cookie/consent-offcanvas` | the consent panel for a blocked feature |
| `frontend.cookie.groups` | `/cookie/groups` | the group tree, for custom front ends |

Templates in `layout/cookie/`:

| Template | Renders |
|---|---|
| `cookie-permission.html.twig` | the bar shown until a choice is made |
| `cookie-configuration.html.twig` | the off-canvas dialogue; extends `utilities/offcanvas.html.twig` |
| `cookie-configuration-group.html.twig` | one group |
| `cookie-configuration-parent.html.twig` | a group's own checkbox |
| `cookie-configuration-child.html.twig` | one cookie's checkbox, with `data-cookie` and `data-cookie-value` |
| `cookie-consent-offcanvas.html.twig` | the panel offering consent for a blocked feature |

**`data-cookie` on the checkbox is the join** between the PHP declaration and the JavaScript that
writes the cookie. Keep it when restyling.

## The JavaScript side

`src/plugin/cookie/`:

- **`cookie-permission.plugin.js`** (`[data-cookie-permission]`) — the bar; shows until
  `cookie-preference` exists.
- **`cookie-configuration.plugin.js`** (`[data-cookie-permission]`) — the dialogue: reads the
  checkboxes, writes and removes cookies, stores the preference, publishes the update.

Selectors it depends on:

| Option | Default |
|---|---|
| `cookiePreference` | `cookie-preference` |
| `cookieSelector` | `[data-cookie]` |
| `buttonOpenSelector` | `.js-cookie-configuration-button button` |
| `buttonSubmitSelector` | `.js-offcanvas-cookie-submit` |
| `buttonAcceptAllSelector` | `.js-offcanvas-cookie-accept-all` |
| `globalButtonAcceptAllSelector` | `.js-cookie-accept-all-button` |
| `globalButtonPermissionSelector` | `.js-cookie-permission-button` |
| `parentInputSelector` | `.offcanvas-cookie-parent-input` |

`cookie-config-hash` records which configuration the visitor consented to. When the available
cookies change, the hash no longer matches and consent is asked again — so adding a cookie
correctly re-prompts existing visitors, which is the legally required behaviour and not a bug.

## Reacting to a consent change

```javascript
import { COOKIE_CONFIGURATION_UPDATE } from 'src/plugin/cookie/cookie-configuration.plugin';
import CookieStorageHelper from 'src/helper/storage/cookie-storage.helper';

// on load
if (CookieStorageHelper.getItem('my-tracking-cookie')) {
    this._activate();
}

// and on every change, without a reload
document.$emitter.subscribe(COOKIE_CONFIGURATION_UPDATE, (event) => {
    const updated = event.detail;                    // { 'my-tracking-cookie': true|false }
    if (updated['my-tracking-cookie'] === true)  this._activate();
    if (updated['my-tracking-cookie'] === false) this._deactivate();
});
```

`event.detail` contains **only the cookies that changed**, so check for the key before reading it.
Both checks are needed: the load check covers a returning visitor, the subscription covers a change
in the current session.

`window.useDefaultCookieConsent` tells you whether the built-in consent is active at all; a shop
using a third-party consent tool sets it false, and `main.js` then skips registering the cookie
plugins.

## Which cookies are actually set

The dialogue does not set cookies by itself except its own bookkeeping. On submit,
`cookie-configuration.plugin.js`:

- **writes** the accepted entries' `cookie` name with their `value` and `expiration`;
- **removes** the declined ones, including their `.` -prefixed domain variants;
- **stores** `cookie-preference` and `cookie-config-hash`;
- **publishes** `COOKIE_CONFIGURATION_UPDATE`.

A cookie your integration sets itself is **not** removed by declining — you must remove it in your
own handler. That is the most common compliance defect in a custom integration.

## The two banner modes

- **Default consent** (`core.basicInformation.useDefaultCookieConsent`) — the built-in bar and
  dialogue. `window.useDefaultCookieConsent` reflects it.
- **Third-party tool** — the setting is off, the core plugins do not register, and the external tool
  owns the decision. Your integration must then read that tool's state, not
  `COOKIE_CONFIGURATION_UPDATE`.

Support both if you ship a plugin for other shops: check `window.useDefaultCookieConsent` and fall
back accordingly.

## Rules for a third-party integration

1. **Declare the cookie** through `CookieGroupCollectEvent`, in Statistical or Marketing — never in
   Required.
2. **Load nothing before consent.** Injecting a tag manager or pixel on page load and "waiting" to
   send data still sets the vendor's cookies.
3. **Check on load and subscribe to changes**, so consent takes effect without a reload.
4. **Remove your own cookies on withdrawal**, including domain variants.
5. **Use snippet keys** for the label and description, and translate them.
6. **Keep `data-cookie` and the `js-` classes** when restyling the dialogue.
7. **Expect a re-prompt** after adding a cookie — the config hash changes by design.
