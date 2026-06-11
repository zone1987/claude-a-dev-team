# @shopware-ag/meteor-admin-sdk — Erschöpfende Referenz

Quelle: `packages/admin-sdk/src/` im Meteor-Monorepo.

## Installation & Initialisierung

```bash
npm install @shopware-ag/meteor-admin-sdk
```

### iFrame-App (Shopware App)

Eine iFrame-App ruft die SDK-Funktionen direkt auf — das SDK kommuniziert per `postMessage`
mit dem Admin-Parent-Fenster. Kein separater Init-Aufruf nötig; jeder `send`-Aufruf registriert
die App automatisch.

```js
import { location, notification, ui } from '@shopware-ag/meteor-admin-sdk';

// Höhe des iFrames automatisch anpassen
location.startAutoResizer();

// Menüeintrag hinzufügen
await ui.menu.addMenuItem({
  label: 'Mein Modul',
  locationId: 'my-plugin-main',
  parent: 'sw-extension',
});
```

### Plugin (Shopware Plugin, kein iFrame)

Plugins, die im selben Fenster wie der Admin laufen, können dieselben Funktionen nutzen.
`location.isIframe()` gibt `false` zurück; `location.is(id)` vergleicht die locationId
aus dem URL-Parameter `?locationId=...`.

---

## Namespace-Übersicht

| Import | Namespace | Beschreibung |
|---|---|---|
| `ui.menu` | `ui/menu` | Menüeinträge |
| `ui.mainModule` | `ui/main-module` | Hauptmodul-Registration |
| `ui.module.payment` | `ui/module/payment` | Zahlungs-Übersichtskarten |
| `ui.modal` | `ui/modal` | Modals öffnen/schließen/updaten |
| `ui.sidebar` | `ui/sidebar` | Seitenleisten |
| `ui.actionButton` | `ui/action-button` | Aktionsbuttons in Entity-Listen/-Detailseiten |
| `ui.tabs` | `ui/tabs` | Tabs an bestehenden Tab-Positionen hinzufügen |
| `ui.settings` | `ui/settings` | Einträge in Einstellungen |
| `ui.componentSection` | `ui/component-section` | Card/Div-Abschnitte in bestehende Seiten einfügen |
| `ui.mediaModal` | `ui/media-modal` | Media-Picker-Modal öffnen |
| `cms` | `ui/cms` | CMS-Elemente und -Blöcke registrieren |
| `notification` | `notification` | Benachrichtigungen |
| `toast` | `toast` | Toast-Nachrichten |
| `context` | `context` | Kontext-Daten (Sprache, Locale, User, …) |
| `location` | `location` | iFrame-Location-Hilfsmethoden |
| `window` | `window` | Redirect, Router-Push, Reload |
| `data` | `data` | Dataset-API (subscribe/get/update) + repository |
| `composables` | `data/composables` | Vue-Composables |
| `app.webhook` | `app/action` | Webhook-Actions ausführen |
| `iap` | `iap` | In-App-Purchase Checkout |
| `telemetry` | `telemetry` | Telemetrie-Events |
| `consent` | `consent` | Consent-Management |

---

## `ui.menu`

### `ui.menu.addMenuItem(options)`

Fügt einen Menüeintrag in die Shopware-Administration ein.

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `label` | `string` | ja | — | Anzeigetext |
| `locationId` | `string` | ja | — | ID der anzuzeigenden Location |
| `displaySearchBar` | `boolean` | nein | `true` | Suchleiste anzeigen |
| `displaySmartBar` | `boolean` | nein | `true` | Smart-Bar anzeigen |
| `parent` | `string` | nein | `'sw-extension'` | Übergeordneter Menüpunkt |
| `position` | `number` | nein | `110` | Sortierposition |

**Rückgabe:** `Promise<void>`

```js
await ui.menu.addMenuItem({
  label: 'Mein Plugin',
  locationId: 'my-plugin-main',
  parent: 'sw-catalogue',
  position: 50,
});
```

### `ui.menu.collapseMenu()`

Klappt das Seitenmenü ein. **Rückgabe:** `Promise<void>`

### `ui.menu.expandMenu()`

Klappt das Seitenmenü aus. **Rückgabe:** `Promise<void>`

---

## `ui.mainModule`

### `ui.mainModule.addMainModule(options)`

Registriert ein Hauptmodul (eigener Admin-Bereich mit LocationId).

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `heading` | `string` | ja | — | Titel des Moduls |
| `locationId` | `string` | ja | — | LocationId |
| `displaySearchBar` | `boolean` | nein | `true` | Suchleiste anzeigen |
| `displayLanguageSwitch` | `boolean` | nein | `false` | Sprachschalter anzeigen |

**Rückgabe:** `Promise<void>`

### `ui.mainModule.addSmartBarButton(options)`

Fügt einen Button in die SmartBar des Hauptmoduls ein.

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `locationId` | `string` | ja | — | LocationId |
| `buttonId` | `string` | ja | — | Eindeutige Button-ID |
| `label` | `string` | ja | — | Button-Text |
| `variant` | `'primary'\|'ghost'\|'danger'\|'ghost-danger'\|'contrast'\|'context'` | ja | — | Variante |
| `disabled` | `boolean` | nein | `false` | Deaktiviert |
| `onClickCallback` | `() => void` | ja | — | Click-Handler |

**Rückgabe:** `Promise<void>`

### `ui.mainModule.hideSmartBar(options)`

Versteckt die SmartBar für eine LocationId.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `locationId` | `string` | ja | LocationId |

**Rückgabe:** `Promise<void>`

---

## `ui.modal`

### `ui.modal.open(options)`

Öffnet ein Modal.

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `title` | `string` | nein | — | Titel |
| `locationId` | `string` | nein | — | LocationId für iFrame-Inhalt |
| `textContent` | `string` | nein | — | Textinhalt (wenn kein locationId) |
| `variant` | `'default'\|'small'\|'large'\|'full'` | nein | `'default'` | Größe |
| `showHeader` | `boolean` | nein | `true` | Header anzeigen |
| `showFooter` | `boolean` | nein | `true` | Footer anzeigen |
| `closable` | `boolean` | nein | `true` | Schließbar |
| `buttons` | `buttonProps[]` | nein | `[]` | Footer-Buttons |

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

**Rückgabe:** `Promise<void>`

```js
await ui.modal.open({
  title: 'Bestätigung',
  locationId: 'my-modal',
  variant: 'small',
  buttons: [
    { label: 'Abbrechen', method: () => ui.modal.close({ locationId: 'my-modal' }), variant: 'ghost' },
    { label: 'OK', method: () => doSomething(), variant: 'primary' },
  ],
});
```

### `ui.modal.close(options)`

Schließt ein Modal.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `locationId` | `string` | nein | LocationId des zu schließenden Modals |

**Rückgabe:** `Promise<void>`

### `ui.modal.update(options)`

Aktualisiert ein geöffnetes Modal.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `locationId` | `string` | ja | LocationId des Modals |
| `title` | `string` | nein | Neuer Titel |
| `showHeader` | `boolean` | nein | Header-Sichtbarkeit |
| `showFooter` | `boolean` | nein | Footer-Sichtbarkeit |
| `closable` | `boolean` | nein | Schließbarkeit |
| `buttons` | `buttonProps[]` | nein | Neue Buttons |

**Rückgabe:** `Promise<void>`

---

## `ui.sidebar`

### `ui.sidebar.add(options)`

Fügt eine Sidebar hinzu.

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `title` | `string` | ja | — | Titel |
| `locationId` | `string` | ja | — | LocationId |
| `icon` | `string` | ja | — | Icon-Name |
| `resizable` | `boolean` | nein | `false` | Größenänderung erlauben |

**Rückgabe:** `Promise<void>`

### `ui.sidebar.close(options)` / `ui.sidebar.remove(options)` / `ui.sidebar.setActive(options)`

Alle nehmen `{ locationId: string }`. **Rückgabe:** `Promise<void>`

---

## `ui.actionButton`

### `ui.actionButton.add(options)`

Fügt einen Aktionsbutton in Entity-Listen oder -Detailseiten ein.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | ja | Eindeutige ID |
| `entity` | `'product'\|'order'\|'category'\|'promotion'\|'customer'\|'media'` | ja | Entity-Typ |
| `view` | `'detail'\|'list'\|'item'` | ja | Anzeige in Detail-/Listen-/Item-Ansicht |
| `label` | `string` | ja | Beschriftung |
| `meteorIcon` | `string` | nein | Meteor-Icon-Name |
| `fileTypes` | `string[]` | nein | Nur bei Media: erlaubte Dateitypen |
| `callback` | `(entity: string, entityIdList: string[]) => void` | ja | Click-Handler |

**Rückgabe:** `Promise<void>`

```js
await ui.actionButton.add({
  name: 'my-export-button',
  entity: 'product',
  view: 'list',
  label: 'Exportieren',
  meteorIcon: 'solid-download',
  callback: (entity, ids) => console.log(entity, ids),
});
```

---

## `ui.tabs`

### `ui.tabs(tabPositionId).addTabItem(options)`

Fügt einen Tab-Eintrag an einer bestehenden Tab-Position ein.

```js
const tabs = ui.tabs('sw-product-detail__tabs');
await tabs.addTabItem({
  label: 'Mein Tab',
  componentSectionId: 'my-tab-content',
});
```

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `label` | `string` | ja | Tab-Beschriftung |
| `componentSectionId` | `string` | ja | ID der ComponentSection für den Inhalt |

**Rückgabe:** `Promise<void>`

---

## `ui.settings`

### `ui.settings.addSettingsItem(options)`

Fügt einen Eintrag in den Systemeinstellungen hinzu.

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `label` | `string` | ja | — | Beschriftung |
| `locationId` | `string` | ja | — | LocationId |
| `icon` | `icons` (Meteor-Icon-Name) | ja | — | Icon |
| `tab` | `'shop'\|'system'\|'plugins'` | nein | `'plugins'` | Einstellungs-Tab |
| `displaySearchBar` | `boolean` | nein | `true` | Suchleiste |
| `displaySmartBar` | `boolean` | nein | `true` | SmartBar |

**Rückgabe:** `Promise<void>`

---

## `ui.componentSection`

### `ui.componentSection.add(options)`

Rendert eine Card oder ein Div an einer bestehenden Positions-ID.

```ts
// Card-Komponente
await ui.componentSection.add({
  component: 'card',
  positionId: 'sw-product-detail-base__before-price',
  props: {
    title: 'Meine Erweiterung',
    locationId: 'my-card-content',
  },
});

// Div-Komponente
await ui.componentSection.add({
  component: 'div',
  positionId: 'sw-product-detail-base__before-price',
  props: { locationId: 'my-div-content' },
});
```

**Rückgabe:** `Promise<void>`

---

## `ui.mediaModal`

### `ui.mediaModal.open(options)`

Öffnet den Media-Picker.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `initialFolderId` | `string` | nein | Startordner |
| `entityContext` | `string` | nein | Entity-Kontext |
| `allowMultiSelect` | `boolean` | nein | Mehrfachauswahl |
| `defaultTab` | `'upload'\|'library'` | nein | Standard-Tab |
| `fileAccept` | `string` | nein | MIME-Typen (z.B. `'image/png,image/jpeg'`) |
| `selectors` | `string[]` | nein | Zurückzugebende Properties |
| `callback` | `(mediaSelections: unknown[]) => void` | ja | Auswahl-Handler |

**Rückgabe:** `Promise<void>`

### `ui.mediaModal.openSaveMedia(options)`

Öffnet den Media-Speichern-Dialog.

| Name | Typ | Beschreibung |
|---|---|---|
| `initialFolderId` | `string` | Startordner |
| `initialFileName` | `string` | Vorgeschlagener Dateiname |
| `fileType` | `string` | Dateityp |
| `callback` | `(params: { fileName, folderId, mediaId? }) => void` | Callback |

**Rückgabe:** `Promise<void>`

---

## `cms`

### `cms.registerCmsElement(options)`

Registriert ein CMS-Element.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | ja | Technischer Name (mit Vendor-Präfix); generiert LocationIds `{name}-element`, `{name}-preview`, `{name}-config` |
| `label` | `string` | ja | Snippet-Key für die Anzeige |
| `defaultConfig` | `{ [key: string]: unknown }` | ja | Standard-Konfiguration |

**Rückgabe:** `Promise<void>`

### `cms.registerCmsBlock(options)`

Registriert einen CMS-Block.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | ja | Technischer Name |
| `label` | `string` | ja | Snippet-Key |
| `category` | `'commerce'\|'form'\|'image'\|'sidebar'\|'text-image'\|'text'\|'video'\|string` | nein | Kategorie |
| `slots` | `Array<{ element: string }>` | ja | Slot-Definitionen |
| `slotLayout` | `{ grid?: string }` | nein | CSS-Grid-Layout |
| `previewImage` | `string` | nein | Vorschaubild-URL (min. 350px breit) |

**Rückgabe:** `Promise<void>`

---

## `notification`

### `notification.dispatch(options)`

Zeigt eine Benachrichtigung.

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `message` | `string` | ja | — | Text (HTML erlaubt, wird sanitiert) |
| `title` | `string` | ja | — | Titel |
| `growl` | `boolean` | nein | `true` | Als Growl anzeigen |
| `variant` | `'success'\|'info'\|'warning'\|'error'` | nein | — | Variante |
| `appearance` | `'system'\|'notification'` | nein | `'notification'` | Stil |
| `actions` | `Array<{ label, method?, route?, disabled? }>` | nein | `[]` | Aktions-Buttons |

**Rückgabe:** `Promise<void>`

```js
await notification.dispatch({
  title: 'Gespeichert',
  message: 'Daten wurden erfolgreich gespeichert.',
  variant: 'success',
});
```

---

## `toast`

### `toast.dispatch(options)`

Zeigt eine kurze Toast-Nachricht (max. 3 Wörter).

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `msg` | `string` | ja | Nachricht (max. 3 Wörter) |
| `type` | `'informal'\|'critical'\|'positive'` | ja | Typ |
| `dismissible` | `boolean` | ja | Manuell schließbar |
| `icon` | `string` | nein | Icon vor der Nachricht |
| `action` | `{ label: string, callback: () => void }` | nein | Aktionsbutton |

**Rückgabe:** `Promise<void>`

---

## `context`

### `context.getLanguage()`

**Rückgabe:** `Promise<{ systemLanguageId: string, languageId: string }>`

### `context.subscribeLanguage(callback)`

Abonniert Sprachänderungen. **Rückgabe:** Unsubscribe-Funktion.

### `context.getLocale()`

**Rückgabe:** `Promise<{ locale: string, fallbackLocale: string }>`

### `context.subscribeLocale(callback)`

Abonniert Locale-Änderungen.

### `context.getEnvironment()`

**Rückgabe:** `Promise<'development' | 'production' | 'testing'>`

### `context.getCurrency()`

**Rückgabe:** `Promise<{ systemCurrencyISOCode: string, systemCurrencyId: string }>`

### `context.getShopwareVersion()`

**Rückgabe:** `Promise<string>` (z.B. `'6.7.0.0'`)

### `context.compareIsShopwareVersion(operator, version)`

Vergleicht die aktuelle Shopware-Version.

```js
const isNewer = await context.compareIsShopwareVersion('>=', '6.6.0.0');
```

### `context.getUserInformation()`

**Rückgabe:** `Promise<{ id, email, firstName, lastName, username, admin, active, aclRoles, ... }>`

### `context.getUserTimezone()`

**Rückgabe:** `Promise<string>` (IANA-Timezone)

### `context.getAppInformation()`

**Rückgabe:** `Promise<{ name: string, version: string, type: 'app'|'plugin', privileges }>`

### `context.can(privilege)`

Prüft ACL-Privilege der Extension.

```js
const canWrite = await context.can('product:write');
```

**Rückgabe:** `Promise<boolean>`

### `context.getModuleInformation()`

**Rückgabe:** `Promise<{ modules: Array<{ displaySearchBar, heading, id, locationId }> }>`

### `context.getShopId()`

**Rückgabe:** `Promise<string | null>`

---

## `location`

### `location.is(locationId: string): boolean`

Prüft ob die aktuelle Location-ID mit der übergebenen übereinstimmt.

```js
if (location.is('sw-product-detail')) { /* … */ }
```

### `location.get(): string`

Gibt die aktuelle Location-ID zurück.

### `location.isIframe(): boolean`

Gibt `true` zurück wenn der Code in einem iFrame ausgeführt wird.

### `location.updateHeight(height?: number): Promise<void>`

Aktualisiert die iFrame-Höhe. Ohne Parameter: aktuelle `document.documentElement.offsetHeight`.

### `location.startAutoResizer(): void`

Startet einen `ResizeObserver` der die iFrame-Höhe automatisch aktualisiert.

> Hinweis: `body { overflow: hidden; }` im iFrame empfehlenswert um Scroll-Konflikte zu vermeiden.

### `location.stopAutoResizer(): void`

Stoppt den Auto-Resizer.

### `location.updateUrl(url: URL): Promise<void>`

Aktualisiert die angezeigte URL (Hash, Pathname, SearchParams) im Admin.

### `location.startAutoUrlUpdater(): void`

Startet einen 50ms-Intervall-Check der URL-Änderungen an den Admin sendet.

### `location.stopAutoUrlUpdater(): void`

Stoppt den URL-Updater.

### `location.MAIN_HIDDEN: string`

Konstante `'sw-main-hidden'` — LocationId für versteckte Hauptmodule.

---

## `window`

### `window.redirect(options)`

| Name | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `url` | `string` | ja | — | Ziel-URL |
| `newTab` | `boolean` | nein | `false` | In neuem Tab öffnen |

**Rückgabe:** `Promise<void>`

### `window.routerPush(options)`

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `name` | `string` | nein | Routen-Name |
| `path` | `string` | nein | Routen-Pfad |
| `params` | `Record<string, string>` | nein | Routen-Parameter |
| `replace` | `boolean` | nein | History-Replace statt Push |

**Rückgabe:** `Promise<void>`

### `window.reload()`

Lädt den Admin neu. **Rückgabe:** `Promise<void>`

### `window.getId()`

**Rückgabe:** `Promise<string>` — Eindeutige Fenster-ID.

### `window.getPath()`

**Rückgabe:** `Promise<string>` — Aktueller Router-Pfad.

---

## `data` — Dataset-API

### `data.get(options)`

Holt ein Dataset einmalig.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `id` | `string` | ja | Dataset-ID |
| `selectors` | `string[]` | nein | Nur bestimmte Properties zurückgeben |

**Rückgabe:** `Promise<unknown>`

### `data.subscribe(id, callback, options?)`

Abonniert ein Dataset. Callback wird bei jeder Änderung aufgerufen.

```js
const unsubscribe = data.subscribe('sw-product-detail', ({ data }) => {
  console.log(data);
}, { selectors: ['id', 'name'] });
```

**Rückgabe:** Unsubscribe-Funktion.

### `data.update(options)`

Aktualisiert ein Dataset.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `id` | `string` | ja | Dataset-ID |
| `data` | `unknown` | ja | Neue Daten |

**Rückgabe:** `Promise<unknown>`

---

## `data.repository`

Zugriff auf das Shopware-Repository-System über den Admin.

```js
import { data } from '@shopware-ag/meteor-admin-sdk';

const repo = data.repository('product');
```

### Repository-Methoden

| Methode | Signatur | Rückgabe |
|---|---|---|
| `search` | `(criteria, context?) => Promise<EntityCollection \| null>` | Suche nach Entities |
| `get` | `(id, context?, criteria?) => Promise<Entity \| null>` | Entity per ID laden |
| `save` | `(entity, context?) => Promise<void \| null>` | Entity speichern |
| `saveAll` | `(entities, context?) => Promise<unknown \| null>` | Mehrere Entities speichern |
| `delete` | `(entityId, context?) => Promise<void \| null>` | Entity löschen |
| `create` | `(context?, entityId?) => Promise<Entity \| null>` | Neue Entity erstellen |
| `clone` | `(entityId, context?, behavior?) => Promise<unknown \| null>` | Entity klonen |
| `hasChanges` | `(entity) => Promise<boolean \| null>` | Änderungen vorhanden? |

```js
const criteria = new data.Classes.Criteria(1, 25);
criteria.addFilter(data.Classes.Criteria.equals('active', true));
criteria.addSorting(data.Classes.Criteria.sort('name', 'ASC'));

const result = await repo.search(criteria);
```

---

## `Criteria`-Klasse

`data.Classes.Criteria` — Vollständige Suchkriterien für die DAL.

### Konstruktor

```ts
new Criteria(page?: number | null, limit?: number | null)
```

### Instanzmethoden (alle chainbar)

| Methode | Beschreibung |
|---|---|
| `setPage(page)` | Seite setzen |
| `setLimit(limit)` | Limit setzen |
| `setTerm(term)` | Suchbegriff |
| `setIds(ids[])` | ID-Filter |
| `setTitle(title)` | Debug-Titel für Netzwerk-Tab |
| `setTotalCountMode(mode)` | 0=keine, 1=exakt, 2=Pagination |
| `addFilter(filter)` | Filter hinzufügen |
| `addPostFilter(filter)` | Post-Filter |
| `addSorting(sorting)` | Sortierung |
| `addAssociation(path)` | Assoziation laden (dot-notation) |
| `getAssociation(path)` | Kriterium einer Assoziation |
| `addAggregation(agg)` | Aggregation |
| `addIncludes(include)` | Partial-Fields-Response |
| `addGrouping(field)` | Gruppierung |
| `addFields(...fields)` | Partielle Felder |
| `addQuery(filter, score, scoreField?)` | Scored Query |
| `resetSorting()` | Sortierungen zurücksetzen |

### Statische Filter-Methoden

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

### Statische Sortier-Methoden

```js
Criteria.sort('name', 'ASC', false)
Criteria.naturalSorting('name', 'ASC')
Criteria.countSorting('lineItems', 'DESC')
```

### Statische Aggregations-Methoden

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

Vue 3 Composables für reaktiven Datenzugriff.

### `composables.useRepository(entityNameRef, repositoryFactoryRef?)`

Reaktiver Wrapper um `getRepository`. Aktualisiert bei Ref-Änderungen.

```ts
import { composables } from '@shopware-ag/meteor-admin-sdk';
import { ref } from 'vue';

const entityName = ref('product');
const repo = composables.useRepository(entityName);

// repo.value.search(criteria)
```

**Rückgabe:** `ComputedRef<SDKRepository<EntityName>>`

### `composables.getRepository(entityName, repositoryFactory?)`

Nicht-reaktive Version. Gibt direkt ein Repository-Objekt zurück.

```ts
const repo = composables.getRepository('product');
const entity = await repo.get('entity-id');
```

### `composables.useSharedState(key, initialValue)`

Persistenter, reaktiver, fensterübergreifender State (IndexedDB + BroadcastChannel).

```ts
const state = composables.useSharedState('my-plugin-state', { count: 0 });
// state.value.count = 1  →  wird automatisch persistiert & synchronisiert
```

**Rückgabe:** `{ value: UnwrapRef<T> }`

### `composables.useDataset(id, options?)`

Reaktiver Zugriff auf ein Admin-Dataset.

```ts
const { data, isReady, ready } = composables.useDataset('sw-product-detail', {
  selectors: ['id', 'name', 'price'],
});

await ready;
// data.value enthält die Produkt-Daten
```

**Rückgabe:** `{ data: Ref<T | null>, isReady: Ref<boolean>, ready: Promise<void> }`

---

## `app.webhook`

### `app.webhook.actionExecute(options)`

Führt eine Webhook-Action aus (für Shopware Apps).

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `url` | `string` | ja | Webhook-URL |
| `entityIds` | `string[]` | ja | Betroffene Entity-IDs |
| `entity` | `string` | ja | Entity-Typ |

**Rückgabe:** `Promise<void>`

---

## `iap`

### `iap.purchase(options)`

Öffnet den In-App-Purchase Checkout.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `identifier` | `string` | ja | IAP-Identifier |

**Rückgabe:** `Promise<unknown>`

---

## `telemetry`

### `telemetry.dispatch(options)`

Sendet ein Telemetrie-Event. Die `source` (Extension-Name) wird automatisch injiziert.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `event` | `string` | ja | Event-Name |
| `data` | `Record<string, unknown>` | nein | Event-Daten |

**Rückgabe:** `Promise<void>`

### `telemetry.trackPageView(properties)`

Sendet ein `page_viewed`-Event mit standardisierten Properties:

```ts
{ sw_route_from_href, sw_route_from_name, sw_route_to_href, sw_route_to_name, sw_route_to_query?, ...custom }
```

### `telemetry.trackLinkVisited(properties)`

Sendet ein `link_visited`-Event:

```ts
{ sw_link_href, sw_link_type: 'internal'|'external', ...custom }
```

---

## `consent`

### `consent.status(options)`

Fragt den aktuellen Consent-Status ab.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `consent` | `string` | ja | Consent-Name |

**Rückgabe:** `Promise<Consent>` mit Properties:
- `name: string`
- `status: 'unset' | 'declined' | 'revoked' | 'accepted'`
- `updatedAt: string | null`
- `acceptedRevision: string | null`
- `lastRevision: string | null`
- `isAccepted: boolean` (getter)
- `isStale: boolean` (getter — accepted aber veraltete Revision)

### `consent.request(options)`

Fordert Consent an und wartet auf die Antwort.

| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `consent` | `string` | ja | Consent-Name |
| `requestMessage` | `string` | nein | Nachricht an den Nutzer |
| `privacyLink` | `string` | nein | Link zur Datenschutzerklärung |

**Rückgabe:** `{ requestPromise: Promise<Consent>, abort: (reason?) => void }`

```js
const { requestPromise, abort } = consent.request({
  consent: 'my-analytics-consent',
  requestMessage: 'Wir benötigen Ihre Zustimmung.',
});

const result = await requestPromise;
if (result.isAccepted) { /* Tracking aktivieren */ }
```

---

## `EntitySchema`-Namespace

Ermöglicht das Erweitern der Entity-Typen in TypeScript:

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

// Dann typsicher:
const repo = data.repository('my_custom_entity');
const entity = await repo.get('some-id');
entity?.name; // TypeScript kennt den Typ
```
