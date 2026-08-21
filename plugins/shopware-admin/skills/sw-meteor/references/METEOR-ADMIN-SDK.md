# @shopware-ag/meteor-admin-sdk — Exhaustive reference

Source: `packages/admin-sdk/src/` in the Meteor monorepo.

## Contents

- [Installation & initialization](#installation-initialization)
- [Namespace overview](#namespace-overview)
- [`ui.menu`](#uimenu)
- [`ui.mainModule`](#uimainmodule)
- [`ui.modal`](#uimodal)
- [`ui.sidebar`](#uisidebar)
- [`ui.actionButton`](#uiactionbutton)
- [`ui.tabs`](#uitabs)
- [`ui.settings`](#uisettings)
- [`ui.componentSection`](#uicomponentsection)
- [`ui.mediaModal`](#uimediamodal)
- [`cms`](#cms)
- [`notification`](#notification)
- [`toast`](#toast)
- [`context`](#context)
- [`location`](#location)
- [`window`](#window)
- [`data` — dataset API](#data-dataset-api)
- [`data.repository`](#datarepository)
- [`Criteria` class](#criteria-class)
- [`composables`](#composables)
- [`app.webhook`](#appwebhook)
- [`iap`](#iap)
- [`telemetry`](#telemetry)
- [`consent`](#consent)
- [`EntitySchema` namespace](#entityschema-namespace)

## Installation & initialization

```bash
npm install @shopware-ag/meteor-admin-sdk
```

### iFrame app (Shopware app)

An iFrame app calls the SDK functions directly — the SDK communicates via `postMessage`
with the admin parent window. No separate init call needed; every `send` call registers
the app automatically.

```js
import { location, notification, ui } from '@shopware-ag/meteor-admin-sdk';

// adjust the iFrame height automatically
location.startAutoResizer();

// add a menu item
await ui.menu.addMenuItem({
  label: 'My module',
  locationId: 'my-plugin-main',
  parent: 'sw-extension',
});
```

### Plugin (Shopware plugin, no iFrame)

Plugins that run in the same window as the admin can use the same functions.
`location.isIframe()` returns `false`; `location.is(id)` compares the locationId
from the URL parameter `?locationId=...`.

---

## Namespace overview

| Import | Namespace | Description |
|---|---|---|
| `ui.menu` | `ui/menu` | Menu items |
| `ui.mainModule` | `ui/main-module` | Main module registration |
| `ui.module.payment` | `ui/module/payment` | Payment overview cards |
| `ui.modal` | `ui/modal` | Open/close/update modals |
| `ui.sidebar` | `ui/sidebar` | Sidebars |
| `ui.actionButton` | `ui/action-button` | Action buttons in entity lists/detail pages |
| `ui.tabs` | `ui/tabs` | Add tabs at existing tab positions |
| `ui.settings` | `ui/settings` | Entries in the settings |
| `ui.componentSection` | `ui/component-section` | Insert card/div sections into existing pages |
| `ui.mediaModal` | `ui/media-modal` | Open the media picker modal |
| `cms` | `ui/cms` | Register CMS elements and blocks |
| `notification` | `notification` | Notifications |
| `toast` | `toast` | Toast messages |
| `context` | `context` | Context data (language, locale, user, …) |
| `location` | `location` | iFrame location helper methods |
| `window` | `window` | Redirect, router push, reload |
| `data` | `data` | Dataset API (subscribe/get/update) + repository |
| `composables` | `data/composables` | Vue composables |
| `app.webhook` | `app/action` | Execute webhook actions |
| `iap` | `iap` | In-app purchase checkout |
| `telemetry` | `telemetry` | Telemetry events |
| `consent` | `consent` | Consent management |

---

## `ui.menu`

### `ui.menu.addMenuItem(options)`

Inserts a menu item into the Shopware Administration.

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `label` | `string` | yes | — | Display text |
| `locationId` | `string` | yes | — | ID of the location to display |
| `displaySearchBar` | `boolean` | no | `true` | Show the search bar |
| `displaySmartBar` | `boolean` | no | `true` | Show the smart bar |
| `parent` | `string` | no | `'sw-extension'` | Parent menu entry |
| `position` | `number` | no | `110` | Sort position |

**Returns:** `Promise<void>`

```js
await ui.menu.addMenuItem({
  label: 'My plugin',
  locationId: 'my-plugin-main',
  parent: 'sw-catalogue',
  position: 50,
});
```

### `ui.menu.collapseMenu()`

Collapses the side menu. **Returns:** `Promise<void>`

### `ui.menu.expandMenu()`

Expands the side menu. **Returns:** `Promise<void>`

---

## `ui.mainModule`

### `ui.mainModule.addMainModule(options)`

Registers a main module (a dedicated admin area with a locationId).

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `heading` | `string` | yes | — | Title of the module |
| `locationId` | `string` | yes | — | LocationId |
| `displaySearchBar` | `boolean` | no | `true` | Show the search bar |
| `displayLanguageSwitch` | `boolean` | no | `false` | Show the language switch |

**Returns:** `Promise<void>`

### `ui.mainModule.addSmartBarButton(options)`

Inserts a button into the SmartBar of the main module.

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `locationId` | `string` | yes | — | LocationId |
| `buttonId` | `string` | yes | — | Unique button ID |
| `label` | `string` | yes | — | Button text |
| `variant` | `'primary'\|'ghost'\|'danger'\|'ghost-danger'\|'contrast'\|'context'` | yes | — | Variant |
| `disabled` | `boolean` | no | `false` | Disabled |
| `onClickCallback` | `() => void` | yes | — | Click handler |

**Returns:** `Promise<void>`

### `ui.mainModule.hideSmartBar(options)`

Hides the SmartBar for a locationId.

| Name | Type | Required | Description |
|---|---|---|---|
| `locationId` | `string` | yes | LocationId |

**Returns:** `Promise<void>`

---

## `ui.modal`

### `ui.modal.open(options)`

Opens a modal.

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `title` | `string` | no | — | Title |
| `locationId` | `string` | no | — | LocationId for the iFrame content |
| `textContent` | `string` | no | — | Text content (when no locationId is given) |
| `variant` | `'default'\|'small'\|'large'\|'full'` | no | `'default'` | Size |
| `showHeader` | `boolean` | no | `true` | Show the header |
| `showFooter` | `boolean` | no | `true` | Show the footer |
| `closable` | `boolean` | no | `true` | Closable |
| `buttons` | `buttonProps[]` | no | `[]` | Footer buttons |

**buttonProps:**

```ts
{
  method: () => void,
  label: string,
  variant?: 'primary'|'ghost'|'danger'|'ghost-danger'|'contrast'|'context',
  size?: 'x-small'|'small'|'large',
  square?: boolean,
}
```

**Returns:** `Promise<void>`

```js
await ui.modal.open({
  title: 'Confirmation',
  locationId: 'my-modal',
  variant: 'small',
  buttons: [
    { label: 'Cancel', method: () => ui.modal.close({ locationId: 'my-modal' }), variant: 'ghost' },
    { label: 'OK', method: () => doSomething(), variant: 'primary' },
  ],
});
```

### `ui.modal.close(options)`

Closes a modal.

| Name | Type | Required | Description |
|---|---|---|---|
| `locationId` | `string` | no | LocationId of the modal to close |

**Returns:** `Promise<void>`

### `ui.modal.update(options)`

Updates an open modal.

| Name | Type | Required | Description |
|---|---|---|---|
| `locationId` | `string` | yes | LocationId of the modal |
| `title` | `string` | no | New title |
| `showHeader` | `boolean` | no | Header visibility |
| `showFooter` | `boolean` | no | Footer visibility |
| `closable` | `boolean` | no | Closability |
| `buttons` | `buttonProps[]` | no | New buttons |

**Returns:** `Promise<void>`

---

## `ui.sidebar`

### `ui.sidebar.add(options)`

Adds a sidebar.

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `title` | `string` | yes | — | Title |
| `locationId` | `string` | yes | — | LocationId |
| `icon` | `string` | yes | — | Icon name |
| `resizable` | `boolean` | no | `false` | Allow resizing |

**Returns:** `Promise<void>`

### `ui.sidebar.close(options)` / `ui.sidebar.remove(options)` / `ui.sidebar.setActive(options)`

All take `{ locationId: string }`. **Returns:** `Promise<void>`

---

## `ui.actionButton`

### `ui.actionButton.add(options)`

Inserts an action button into entity lists or detail pages.

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Unique ID |
| `entity` | `'product'\|'order'\|'category'\|'promotion'\|'customer'\|'media'` | yes | Entity type |
| `view` | `'detail'\|'list'\|'item'` | yes | Display in detail/list/item view |
| `label` | `string` | yes | Caption |
| `meteorIcon` | `string` | no | Meteor icon name |
| `fileTypes` | `string[]` | no | Media only: allowed file types |
| `callback` | `(entity: string, entityIdList: string[]) => void` | yes | Click handler |

**Returns:** `Promise<void>`

```js
await ui.actionButton.add({
  name: 'my-export-button',
  entity: 'product',
  view: 'list',
  label: 'Export',
  meteorIcon: 'solid-download',
  callback: (entity, ids) => console.log(entity, ids),
});
```

---

## `ui.tabs`

### `ui.tabs(tabPositionId).addTabItem(options)`

Inserts a tab item at an existing tab position.

```js
const tabs = ui.tabs('sw-product-detail__tabs');
await tabs.addTabItem({
  label: 'My tab',
  componentSectionId: 'my-tab-content',
});
```

| Name | Type | Required | Description |
|---|---|---|---|
| `label` | `string` | yes | Tab caption |
| `componentSectionId` | `string` | yes | ID of the component section for the content |

**Returns:** `Promise<void>`

---

## `ui.settings`

### `ui.settings.addSettingsItem(options)`

Adds an entry to the system settings.

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `label` | `string` | yes | — | Caption |
| `locationId` | `string` | yes | — | LocationId |
| `icon` | `icons` (Meteor icon name) | yes | — | Icon |
| `tab` | `'shop'\|'system'\|'plugins'` | no | `'plugins'` | Settings tab |
| `displaySearchBar` | `boolean` | no | `true` | Search bar |
| `displaySmartBar` | `boolean` | no | `true` | SmartBar |

**Returns:** `Promise<void>`

---

## `ui.componentSection`

### `ui.componentSection.add(options)`

Renders a card or a div at an existing position ID.

```ts
// card component
await ui.componentSection.add({
  component: 'card',
  positionId: 'sw-product-detail-base__before-price',
  props: {
    title: 'My extension',
    locationId: 'my-card-content',
  },
});

// div component
await ui.componentSection.add({
  component: 'div',
  positionId: 'sw-product-detail-base__before-price',
  props: { locationId: 'my-div-content' },
});
```

**Returns:** `Promise<void>`

---

## `ui.mediaModal`

### `ui.mediaModal.open(options)`

Opens the media picker.

| Name | Type | Required | Description |
|---|---|---|---|
| `initialFolderId` | `string` | no | Start folder |
| `entityContext` | `string` | no | Entity context |
| `allowMultiSelect` | `boolean` | no | Multi-selection |
| `defaultTab` | `'upload'\|'library'` | no | Default tab |
| `fileAccept` | `string` | no | MIME types (e.g. `'image/png,image/jpeg'`) |
| `selectors` | `string[]` | no | Properties to return |
| `callback` | `(mediaSelections: unknown[]) => void` | yes | Selection handler |

**Returns:** `Promise<void>`

### `ui.mediaModal.openSaveMedia(options)`

Opens the save-media dialog.

| Name | Type | Description |
|---|---|---|
| `initialFolderId` | `string` | Start folder |
| `initialFileName` | `string` | Suggested file name |
| `fileType` | `string` | File type |
| `callback` | `(params: { fileName, folderId, mediaId? }) => void` | Callback |

**Returns:** `Promise<void>`

---

## `cms`

### `cms.registerCmsElement(options)`

Registers a CMS element.

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Technical name (with vendor prefix); generates the locationIds `{name}-element`, `{name}-preview`, `{name}-config` |
| `label` | `string` | yes | Snippet key for the display |
| `defaultConfig` | `{ [key: string]: unknown }` | yes | Default configuration |

**Returns:** `Promise<void>`

### `cms.registerCmsBlock(options)`

Registers a CMS block.

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Technical name |
| `label` | `string` | yes | Snippet key |
| `category` | `'commerce'\|'form'\|'image'\|'sidebar'\|'text-image'\|'text'\|'video'\|string` | no | Category |
| `slots` | `Array<{ element: string }>` | yes | Slot definitions |
| `slotLayout` | `{ grid?: string }` | no | CSS grid layout |
| `previewImage` | `string` | no | Preview image URL (at least 350px wide) |

**Returns:** `Promise<void>`

---

## `notification`

### `notification.dispatch(options)`

Shows a notification.

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `message` | `string` | yes | — | Text (HTML allowed, is sanitized) |
| `title` | `string` | yes | — | Title |
| `growl` | `boolean` | no | `true` | Show as a growl |
| `variant` | `'success'\|'info'\|'warning'\|'error'` | no | — | Variant |
| `appearance` | `'system'\|'notification'` | no | `'notification'` | Style |
| `actions` | `Array<{ label, method?, route?, disabled? }>` | no | `[]` | Action buttons |

**Returns:** `Promise<void>`

```js
await notification.dispatch({
  title: 'Saved',
  message: 'The data was saved successfully.',
  variant: 'success',
});
```

---

## `toast`

### `toast.dispatch(options)`

Shows a short toast message (max. 3 words).

| Name | Type | Required | Description |
|---|---|---|---|
| `msg` | `string` | yes | Message (max. 3 words) |
| `type` | `'informal'\|'critical'\|'positive'` | yes | Type |
| `dismissible` | `boolean` | yes | Manually closable |
| `icon` | `string` | no | Icon in front of the message |
| `action` | `{ label: string, callback: () => void }` | no | Action button |

**Returns:** `Promise<void>`

---

## `context`

### `context.getLanguage()`

**Returns:** `Promise<{ systemLanguageId: string, languageId: string }>`

### `context.subscribeLanguage(callback)`

Subscribes to language changes. **Returns:** unsubscribe function.

### `context.getLocale()`

**Returns:** `Promise<{ locale: string, fallbackLocale: string }>`

### `context.subscribeLocale(callback)`

Subscribes to locale changes.

### `context.getEnvironment()`

**Returns:** `Promise<'development' | 'production' | 'testing'>`

### `context.getCurrency()`

**Returns:** `Promise<{ systemCurrencyISOCode: string, systemCurrencyId: string }>`

### `context.getShopwareVersion()`

**Returns:** `Promise<string>` (e.g. `'6.7.0.0'`)

### `context.compareIsShopwareVersion(operator, version)`

Compares the current Shopware version.

```js
const isNewer = await context.compareIsShopwareVersion('>=', '6.6.0.0');
```

### `context.getUserInformation()`

**Returns:** `Promise<{ id, email, firstName, lastName, username, admin, active, aclRoles, ... }>`

### `context.getUserTimezone()`

**Returns:** `Promise<string>` (IANA timezone)

### `context.getAppInformation()`

**Returns:** `Promise<{ name: string, version: string, type: 'app'|'plugin', privileges }>`

### `context.can(privilege)`

Checks an ACL privilege of the extension.

```js
const canWrite = await context.can('product:write');
```

**Returns:** `Promise<boolean>`

### `context.getModuleInformation()`

**Returns:** `Promise<{ modules: Array<{ displaySearchBar, heading, id, locationId }> }>`

### `context.getShopId()`

**Returns:** `Promise<string | null>`

---

## `location`

### `location.is(locationId: string): boolean`

Checks whether the current location ID matches the given one.

```js
if (location.is('sw-product-detail')) { /* … */ }
```

### `location.get(): string`

Returns the current location ID.

### `location.isIframe(): boolean`

Returns `true` when the code is executed inside an iFrame.

### `location.updateHeight(height?: number): Promise<void>`

Updates the iFrame height. Without a parameter: the current `document.documentElement.offsetHeight`.

### `location.startAutoResizer(): void`

Starts a `ResizeObserver` that updates the iFrame height automatically.

> Note: `body { overflow: hidden; }` inside the iFrame is recommended to avoid scroll conflicts.

### `location.stopAutoResizer(): void`

Stops the auto resizer.

### `location.updateUrl(url: URL): Promise<void>`

Updates the displayed URL (hash, pathname, search params) in the admin.

### `location.startAutoUrlUpdater(): void`

Starts a 50ms interval check that sends URL changes to the admin.

### `location.stopAutoUrlUpdater(): void`

Stops the URL updater.

### `location.MAIN_HIDDEN: string`

Constant `'sw-main-hidden'` — locationId for hidden main modules.

---

## `window`

### `window.redirect(options)`

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | `string` | yes | — | Target URL |
| `newTab` | `boolean` | no | `false` | Open in a new tab |

**Returns:** `Promise<void>`

### `window.routerPush(options)`

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | no | Route name |
| `path` | `string` | no | Route path |
| `params` | `Record<string, string>` | no | Route parameters |
| `replace` | `boolean` | no | History replace instead of push |

**Returns:** `Promise<void>`

### `window.reload()`

Reloads the admin. **Returns:** `Promise<void>`

### `window.getId()`

**Returns:** `Promise<string>` — unique window ID.

### `window.getPath()`

**Returns:** `Promise<string>` — current router path.

---

## `data` — dataset API

### `data.get(options)`

Fetches a dataset once.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Dataset ID |
| `selectors` | `string[]` | no | Return only certain properties |

**Returns:** `Promise<unknown>`

### `data.subscribe(id, callback, options?)`

Subscribes to a dataset. The callback is invoked on every change.

```js
const unsubscribe = data.subscribe('sw-product-detail', ({ data }) => {
  console.log(data);
}, { selectors: ['id', 'name'] });
```

**Returns:** unsubscribe function.

### `data.update(options)`

Updates a dataset.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | yes | Dataset ID |
| `data` | `unknown` | yes | New data |

**Returns:** `Promise<unknown>`

---

## `data.repository`

Access to the Shopware repository system through the admin.

```js
import { data } from '@shopware-ag/meteor-admin-sdk';

const repo = data.repository('product');
```

### Repository methods

| Method | Signature | Returns |
|---|---|---|
| `search` | `(criteria, context?) => Promise<EntityCollection \| null>` | Search for entities |
| `get` | `(id, context?, criteria?) => Promise<Entity \| null>` | Load an entity by ID |
| `save` | `(entity, context?) => Promise<void \| null>` | Save an entity |
| `saveAll` | `(entities, context?) => Promise<unknown \| null>` | Save multiple entities |
| `delete` | `(entityId, context?) => Promise<void \| null>` | Delete an entity |
| `create` | `(context?, entityId?) => Promise<Entity \| null>` | Create a new entity |
| `clone` | `(entityId, context?, behavior?) => Promise<unknown \| null>` | Clone an entity |
| `hasChanges` | `(entity) => Promise<boolean \| null>` | Are there changes? |

```js
const criteria = new data.Classes.Criteria(1, 25);
criteria.addFilter(data.Classes.Criteria.equals('active', true));
criteria.addSorting(data.Classes.Criteria.sort('name', 'ASC'));

const result = await repo.search(criteria);
```

---

## `Criteria` class

`data.Classes.Criteria` — complete search criteria for the DAL.

### Constructor

```ts
new Criteria(page?: number | null, limit?: number | null)
```

### Instance methods (all chainable)

| Method | Description |
|---|---|
| `setPage(page)` | Set the page |
| `setLimit(limit)` | Set the limit |
| `setTerm(term)` | Search term |
| `setIds(ids[])` | ID filter |
| `setTitle(title)` | Debug title for the network tab |
| `setTotalCountMode(mode)` | 0=none, 1=exact, 2=pagination |
| `addFilter(filter)` | Add a filter |
| `addPostFilter(filter)` | Post filter |
| `addSorting(sorting)` | Sorting |
| `addAssociation(path)` | Load an association (dot notation) |
| `getAssociation(path)` | Criteria of an association |
| `addAggregation(agg)` | Aggregation |
| `addIncludes(include)` | Partial fields response |
| `addGrouping(field)` | Grouping |
| `addFields(...fields)` | Partial fields |
| `addQuery(filter, score, scoreField?)` | Scored query |
| `resetSorting()` | Reset the sortings |

### Static filter methods

```js
Criteria.equals('field', value)
Criteria.equalsAny('field', [v1, v2])
Criteria.contains('field', 'substring')
Criteria.prefix('field', 'prefix')
Criteria.suffix('field', 'suffix')
Criteria.range('field', { gte: '100', lte: '200' })
Criteria.not('and', [Criteria.equals('active', false)])
Criteria.multi('or', [filter1, filter2])
```

### Static sorting methods

```js
Criteria.sort('name', 'ASC', false)
Criteria.naturalSorting('name', 'ASC')
Criteria.countSorting('lineItems', 'DESC')
```

### Static aggregation methods

```js
Criteria.avg('avg-price', 'price')
Criteria.count('count-products', 'id')
Criteria.max('max-price', 'price')
Criteria.min('min-price', 'price')
Criteria.sum('sum-price', 'price')
Criteria.stats('price-stats', 'price')
Criteria.terms('product-categories', 'categoryIds', 5, null, null)
Criteria.histogram('sales-per-month', 'createdAt', 'month', null, null, 'UTC')
Criteria.filter('filtered-agg', [filter], aggregation)
Criteria.entityAggregation('categories-agg', 'categoryIds', 'category')
```

---

## `composables`

Vue 3 composables for reactive data access.

### `composables.useRepository(entityNameRef, repositoryFactoryRef?)`

Reactive wrapper around `getRepository`. Updates when the refs change.

```ts
import { composables } from '@shopware-ag/meteor-admin-sdk';
import { ref } from 'vue';

const entityName = ref('product');
const repo = composables.useRepository(entityName);

// repo.value.search(criteria)
```

**Returns:** `ComputedRef<SDKRepository<EntityName>>`

### `composables.getRepository(entityName, repositoryFactory?)`

Non-reactive version. Returns a repository object directly.

```ts
const repo = composables.getRepository('product');
const entity = await repo.get('entity-id');
```

### `composables.useSharedState(key, initialValue)`

Persistent, reactive, cross-window state (IndexedDB + BroadcastChannel).

```ts
const state = composables.useSharedState('my-plugin-state', { count: 0 });
// state.value.count = 1  →  is persisted & synchronized automatically
```

**Returns:** `{ value: UnwrapRef<T> }`

### `composables.useDataset(id, options?)`

Reactive access to an admin dataset.

```ts
const { data, isReady, ready } = composables.useDataset('sw-product-detail', {
  selectors: ['id', 'name', 'price'],
});

await ready;
// data.value contains the product data
```

**Returns:** `{ data: Ref<T | null>, isReady: Ref<boolean>, ready: Promise<void> }`

---

## `app.webhook`

### `app.webhook.actionExecute(options)`

Executes a webhook action (for Shopware apps).

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | `string` | yes | Webhook URL |
| `entityIds` | `string[]` | yes | Affected entity IDs |
| `entity` | `string` | yes | Entity type |

**Returns:** `Promise<void>`

---

## `iap`

### `iap.purchase(options)`

Opens the in-app purchase checkout.

| Name | Type | Required | Description |
|---|---|---|---|
| `identifier` | `string` | yes | IAP identifier |

**Returns:** `Promise<unknown>`

---

## `telemetry`

### `telemetry.dispatch(options)`

Sends a telemetry event. The `source` (extension name) is injected automatically.

| Name | Type | Required | Description |
|---|---|---|---|
| `event` | `string` | yes | Event name |
| `data` | `Record<string, unknown>` | no | Event data |

**Returns:** `Promise<void>`

### `telemetry.trackPageView(properties)`

Sends a `page_viewed` event with standardized properties:

```ts
{ sw_route_from_href, sw_route_from_name, sw_route_to_href, sw_route_to_name, sw_route_to_query?, ...custom }
```

### `telemetry.trackLinkVisited(properties)`

Sends a `link_visited` event:

```ts
{ sw_link_href, sw_link_type: 'internal'|'external', ...custom }
```

---

## `consent`

### `consent.status(options)`

Queries the current consent status.

| Name | Type | Required | Description |
|---|---|---|---|
| `consent` | `string` | yes | Consent name |

**Returns:** `Promise<Consent>` with the properties:
- `name: string`
- `status: 'unset' | 'declined' | 'revoked' | 'accepted'`
- `updatedAt: string | null`
- `acceptedRevision: string | null`
- `lastRevision: string | null`
- `isAccepted: boolean` (getter)
- `isStale: boolean` (getter — accepted but the revision is outdated)

### `consent.request(options)`

Requests consent and waits for the response.

| Name | Type | Required | Description |
|---|---|---|---|
| `consent` | `string` | yes | Consent name |
| `requestMessage` | `string` | no | Message to the user |
| `privacyLink` | `string` | no | Link to the privacy policy |

**Returns:** `{ requestPromise: Promise<Consent>, abort: (reason?) => void }`

```js
const { requestPromise, abort } = consent.request({
  consent: 'my-analytics-consent',
  requestMessage: 'We need your consent.',
});

const result = await requestPromise;
if (result.isAccepted) { /* enable tracking */ }
```

---

## `EntitySchema` namespace

Allows extending the entity types in TypeScript:

```ts
declare global {
  namespace EntitySchema {
    interface Entities {
      'my_custom_entity': {
        id: string;
        name: string;
        active: boolean;
      };
    }
  }
}

// Then type-safe:
const repo = data.repository('my_custom_entity');
const entity = await repo.get('some-id');
entity?.name; // TypeScript knows the type
```
