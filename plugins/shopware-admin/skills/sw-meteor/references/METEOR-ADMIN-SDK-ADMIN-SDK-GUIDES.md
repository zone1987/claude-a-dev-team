# Meteor Admin SDK — Concepts, Guides & Setup

Source: Official documentation `docs/admin-sdk/` in the Meteor monorepo.

> API reference (methods, parameters, types): see `admin-sdk.md`.
> This document covers concepts, installation, architecture, migration and development tools.

---

## Contents

- [Overview — What is the Meteor Admin SDK?](#overview-what-is-the-meteor-admin-sdk)
- [Extension types: Apps vs. Plugins](#extension-types-apps-vs-plugins)
- [Installation — Apps (complete walkthrough)](#installation-apps-complete-walkthrough)
- [Installation — Plugins (complete walkthrough, Shopware 6.7+)](#installation-plugins-complete-walkthrough-shopware-67)
- [Without npm (CDN)](#without-npm-cdn)
- [Architecture — postMessage communication](#architecture-postmessage-communication)
- [Locations and iFrames](#locations-and-iframes)
- [Positions vs. Locations](#positions-vs-locations)
- [Component Sections](#component-sections)
- [Data Selectors](#data-selectors)
- [TypeScript entity types](#typescript-entity-types)
- [Translations in the extension](#translations-in-the-extension)
- [Migrating existing admin plugins](#migrating-existing-admin-plugins)
- [Permissions in apps (manifest.xml)](#permissions-in-apps-manifestxml)
- [URL persistence on page reload](#url-persistence-on-page-reload)

## Overview — What is the Meteor Admin SDK?

The `@shopware-ag/meteor-admin-sdk` is an npm library for building Shopware Administration UI extensions.

**Areas of application:**
- Custom Administration modules with their own pages
- UI extensions (notifications, modals, tabs, sidebars)
- Access to and modification of entity data through the admin data layer
- Entity-driven workflows and admin integrations

**Advantages:**
- Stable, backwards-compatible API — reduces effort on Shopware updates
- No deep knowledge of the admin internals required
- Full TypeScript with auto-completion
- Lightweight, tree-shakable (only what is imported ends up in the bundle)

---

## Extension types: Apps vs. Plugins

### Apps

Apps run on their own external server and communicate through a defined API.

**Recommended because:**
- They work in Shopware Cloud **and** self-hosted, including SaaS
- Frontend and backend are fully decoupled from the Shopware code
- A dedicated domain per app is required (CORS security)

```
app-one.my-company.com   ✓
app-two.my-company.com   ✓
my-company.com/app-one   ✗  (same domain → not allowed)
```

> For local development: `localhost` or a tunneling service (ngrok). If Shopware runs in Docker, set `registrationUrl` to `host.docker.internal:PORT`; `base-app-url`, on the other hand, with `localhost`.

### Plugins

Plugins run directly inside the Shopware instance. Full access to the PHP codebase, but limited to **self-hosted**.

---

## Installation — Apps (complete walkthrough)

### 1. Set up app server + frontend

```bash
# Scaffold an example app with the App Server SDK
npx tiged shopware/app-sdk-js/examples/node-hono demo-app
cd demo-app
npm install

# Meteor Admin SDK + Vite for the admin frontend
npm install @shopware-ag/meteor-admin-sdk
npm install vue
npm install -D vite
```

### 2. Create the admin frontend (`meteor-app/`)

**`demo-app/meteor-app/index.html`:**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Example App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

**`demo-app/meteor-app/src/main.js`:**

```js
import { notification } from "@shopware-ag/meteor-admin-sdk";

notification.dispatch({
  title: "Meteor Admin SDK installed",
  message: "Your app is connected successfully",
});
```

### 3. Mount Vite on the app server

In `demo-app/index.ts`, configure the HTTP server so that `/admin` requests are forwarded to Vite:

```ts
import { readFileSync } from "node:fs";
import { createServer } from "node:http";
import { getRequestListener } from "@hono/node-server";

const PORT = 3000;

async function startServer() {
  const honoListener = getRequestListener(app.fetch);
  const { createServer: createViteServer } = await import("vite");

  const httpServer = createServer();

  const vite = await createViteServer({
    root: "./meteor-app",
    base: "/admin/",
    appType: "custom",
    server: { middlewareMode: true, hmr: { server: httpServer } },
  });

  httpServer.on("request", (req, res) => {
    if (req.url?.startsWith("/admin")) {
      vite.middlewares(req, res, async () => {
        let html = readFileSync("./meteor-app/index.html", "utf-8");
        html = await vite.transformIndexHtml(req.url, html);
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(html);
      });
      return;
    }
    honoListener(req, res);
  });

  httpServer.listen(PORT, () => {
    console.log(`App server: http://localhost:${PORT}`);
    console.log(`Admin frontend: http://localhost:${PORT}/admin/`);
  });
}

void startServer();
```

### 4. Register `manifest.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/platform/trunk/src/Core/Framework/App/Manifest/Schema/manifest-1.0.xsd">
  <meta>
    <name>MyExampleApp</name>
    <label>MyExampleApp</label>
    <description>My first example app</description>
    <author>Developer</author>
    <copyright>(c) Developer</copyright>
    <version>1.0.0</version>
    <license>MIT</license>
  </meta>
  <setup>
    <!-- host.docker.internal when Shopware runs in Docker -->
    <registrationUrl>http://host.docker.internal:3000/app/register</registrationUrl>
    <secret>S3cr3tf0re$t</secret>
  </setup>
  <admin>
    <!-- base-app-url is loaded by the browser → localhost works -->
    <base-app-url>http://localhost:3000/admin/</base-app-url>
  </admin>
</manifest>
```

Name and secret must match the app server:

```ts
configureAppServer(app, {
  appName: "MyExampleApp",
  appSecret: "S3cr3tf0re$t",
  shopRepository: new BetterSqlite3Repository("shop.db"),
});
```

### 5. Start and install the app

```bash
npm start
# Admin frontend available at http://localhost:3000/admin/

# Install in Shopware (inside the Docker container if applicable):
bin/console app:install --activate MyExampleApp
bin/console cache:clear
```

---

## Installation — Plugins (complete walkthrough, Shopware 6.7+)

### 1. Create the entry point folder

```
custom/plugins/yourPluginName/src/Resources/app/meteor-app
```

> Shopware < 6.7: path `administration` instead of `meteor-app`

### 2. Install the SDK

```bash
cd custom/plugins/yourPluginName/src/Resources/app/meteor-app
npm install @shopware-ag/meteor-admin-sdk
```

### 3. Create the entry files

**`index.html`** (Shopware loads this file as a hidden iFrame):

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Your extension</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

> Shopware < 6.7: omit `<script type="module">` — it is injected automatically.

**`src/main.js`:**

```js
import { notification } from "@shopware-ag/meteor-admin-sdk";

notification.dispatch({
  title: "Hello from your plugin",
  message: "Meteor Admin SDK is working",
});
```

### 4. Install the plugin

```bash
bin/console plugin:install --activate yourPluginName
bin/console cache:clear
```

### 5. Start the admin watcher

Shopware takes care of the bundling — no separate Vite setup needed:

```bash
composer watch:admin
```

---

## Without npm (CDN)

For prototypes or very small setups, the SDK can be loaded directly via a `<script>` tag:

```html
<script src="https://unpkg.com/@shopware-ag/meteor-admin-sdk/cdn"></script>
```

The SDK is globally available as `sw`:

```html
<script src="https://unpkg.com/@shopware-ag/meteor-admin-sdk/cdn"></script>
<script>
  sw.notification.dispatch({
    title: 'Hello',
    message: 'Meteor Admin SDK is working',
  });
</script>
```

Apps using the CDN still require: an app server, an HTML file to serve, and `manifest.xml`.

---

## Architecture — postMessage communication

*(Diagram in the upstream docs: postMessage communication between app and admin.)*

### Hybrid model

Apps (in iFrames) and plugins (in the same window) use **the same SDK**. Every method works both in iFrames and in the same window.

### Flow of an SDK call

1. The extension calls `context.getLanguage()`
2. The SDK sends a JSON message via `channel.send()` using `postMessage`:

```js
{
  _type: 'contextLanguage',
  _data: {},
  _callbackId: 'aRand0mGeneratedUniqueId'
}
```

3. The Administration reacts via `handle('contextLanguage', () => { ... })` and sends back:

```js
{
  _type: 'contextLanguage',
  _response: { languageId: '...', systemLanguageId: '...' },
  _callbackId: 'aRand0mGeneratedUniqueId'
}
```

4. The SDK resolves the original promise → the extension receives the data

### Methods in messages

Because JSON does not support functions, methods are converted into information objects:

```js
{ __type__: '__function__', id: 'theUniqueFunctionId' }
```

The method is stored in a `methodRegistry`. The receiver then calls back via `send('__function__', { args, id })`.

---

## Locations and iFrames

**Locations** define where extension code is executed. Every location runs in its own iFrame — all of them execute the same JavaScript code, so you must branch via `location.is()`.

```js
import { location, ui } from '@shopware-ag/meteor-admin-sdk';

// Registration: in the hidden main iFrame
if (location.is(location.MAIN_HIDDEN)) {
  ui.componentSection.add({
    component: 'card',
    positionId: 'sw-product-properties__before',
    props: {
      title: 'Hello from plugin',
      locationId: 'my-app-card-before-properties'
    }
  });
}

// Render content: in the visible iFrame
if (location.is('my-app-card-before-properties')) {
  document.body.innerHTML = '<h1>Custom content here</h1>';
}
```

### Managing the iFrame height

```js
location.updateHeight(750);           // fixed height
location.startAutoResizer();          // automatically on content changes
```

Avoid scrollbars: set `overflow: hidden` on `body` inside the iFrame.

---

## Positions vs. Locations

- **Position**: Where UI can be injected (identified by `positionId`)
- **Location**: Where extension code runs and renders content (identified by `locationId`)

### Discovering positions with Vue DevTools

*(Screenshot in the upstream docs: the Meteor Admin SDK DevTools panel.)*

**Prerequisites:**
- Vue DevTools (version 6+, beta channel)
- A running Shopware instance in watch mode (`composer watch:admin`)

**Workflow:**
1. Open the Shopware Administration
2. Open browser DevTools → Vue tab → "Shopware Extension API" plugin
3. A list of all extension points for the current page appears
4. Click an extension point → the area in the Administration is highlighted
5. Read the `positionId` from the details

---

## Component Sections

Component sections allow injecting UI components into predefined extension points.

*(Screenshot in the upstream docs: a component section rendered in the admin.)*

```js
import { ui, location } from '@shopware-ag/meteor-admin-sdk';

if (location.is(location.MAIN_HIDDEN)) {
  ui.componentSection.add({
    positionId: 'sw-manufacturer-card-custom-fields__before',
    component: 'card',
    props: {
      title: 'Hello from plugin',
      subtitle: 'I am before the properties card',
      locationId: 'my-app-card-before-properties'
    }
  });
}

if (location.is('my-app-card-before-properties')) {
  document.body.innerHTML = '<h1>Hello World</h1>';
}
```

---

## Data Selectors

Selectors allow requesting only certain properties from admin datasets.

### Syntax

| Segment | Syntax | Description |
|:---|:---|:---|
| Property | `name` | Named property on the root object |
| Nested | `a.b` | Descend into a nested object |
| Array index | `[N]` | Element by zero-based index |
| Wildcard | `*` | All elements of an array |

### Examples

```js
data.get({
  id: 'sw-product-detail__product',
  selectors: ['name', 'manufacturer.name'],
}).then((product) => console.log(product));
// { name: "My Product", manufacturer: { name: "My Manufacturer" } }

// Wildcard
data.get({
  id: 'sw-product-detail__product',
  selectors: ['variants.*.name'],
}).then((product) => console.log(product));
// { variants: [{ name: "First Variant" }, { name: "Second Variant" }] }
```

Multiple selectors on the same parent are merged:

```js
selectors: ['manufacturer.id', 'manufacturer.name']
// → { manufacturer: { id: "...", name: "..." } }
```

### Discovering datasets

Available datasets can be inspected in Vue DevTools → "Shopware Extension API".

---

## TypeScript entity types

### Option 1: Generated types from Shopware (recommended)

```bash
npm install @shopware-ag/entity-schema-types@5.0.0
```

Version correspondence (Shopware without the leading `6.`):
- Shopware 6.5.0.0 → `@shopware-ag/entity-schema-types@5.0.0`
- Shopware 6.6.3.1 → `@shopware-ag/entity-schema-types@6.3.1`
- Shopware 6.7.x.x → accordingly `7.x.x`

**`global.d.ts`:**

```ts
import '@shopware-ag/entity-schema-types';
```

### Option 2: Fallback `any` (simplest option)

```ts
// global.d.ts
declare namespace EntitySchema {
  interface Entities {
    [entityName: string]: any;
  }
}
```

### Option 3: Define your own entity types

```ts
// global.d.ts
declare namespace EntitySchema {
  interface Entities {
    product_manufacturer: product_manufacturer;
    media: media;
  }

  interface product_manufacturer {
    id: string;
    versionId: string;
    mediaId?: string;
    link?: string;
    name: string;
    description?: string;
    customFields?: unknown;
    media?: Entity<'media'>;
    translations: EntityCollection<'product_manufacturer_translation'>;
    createdAt: string;
    updatedAt?: string;
    translated?: { name?: string; description?: string; customFields?: unknown };
  }
}
```

---

## Translations in the extension

### Snippet files for the native admin UI

For text in **native UI components** (e.g. card titles in `componentSection.add`), snippet files are used:

```
<app-root>/Resources/app/administration/snippet/en-GB.json
<app-root>/Resources/app/administration/snippet/de-DE.json
```

**`en-GB.json`:**

```json
{
  "my-app-name": {
    "example-card": {
      "title": "My app",
      "subtitle": "This is my app"
    }
  }
}
```

**Usage via snippet key:**

```js
ui.componentSection.add({
  component: 'card',
  positionId: 'sw-manufacturer-card-custom-fields__before',
  props: {
    title: 'my-app-name.example-card.title',
    subtitle: 'my-app-name.example-card.subtitle',
    locationId: 'my-app-card'
  }
});
```

On language changes the matching snippet file is used automatically.

### Translations in your own iFrame UI

Inside your own iFrame you can use any frontend framework (e.g. `vue-i18n`). To synchronize the current admin language:

```js
import { context } from '@shopware-ag/meteor-admin-sdk';

context.subscribeLanguage(({ languageId }) => {
  // switch the i18n locale
});
```

---

## Migrating existing admin plugins

### Stepwise migration possible

The SDK can be used alongside the existing Twig plugin system. Both approaches work in parallel:

```js
// Existing extension functionality
Shopware.Component.override('sw-dashboard-index', {
  methods: {
    async createdComponent() {
      // use the Meteor Admin SDK at the same time
      await sw.notification.dispatch({
        title: 'Hello from the plugin',
        message: 'Combining old and new approach',
      });
      this.$super('createdComponent');
    }
  }
});
```

### Locations with Vue components (without an iFrame)

Instead of rendering an iFrame, a regular Vue component can be bound into a location:

```js
import { ui, location } from '@shopware-ag/meteor-admin-sdk';

if (!location.isIframe()) {
  const myLocationId = 'my-example-location-id';

  // create a tab
  ui.tabs('sw-product-detail').addTabItem({
    label: 'Example tab',
    componentSectionId: 'example-product-detail-tab-content'
  });

  // insert a card with a location into the tab content
  ui.componentSection.add({
    component: 'card',
    positionId: 'example-product-detail-tab-content',
    props: {
      title: 'Component section example',
      locationId: myLocationId
    }
  });

  // register the Vue component in the plugin system
  Shopware.Component.register('your-component-name', {
    // your component
  });

  // assign the component to the location
  Shopware.State.commit('sdkLocation/addLocation', {
    locationId: myLocationId,
    componentName: 'your-component-name'
  });
}
```

`location.isIframe()` returns `false` when the code runs in the plugin context (not an iFrame).

---

## Permissions in apps (manifest.xml)

For repository operations, permissions must be declared in the manifest:

```xml
<permissions>
  <create>product</create>
  <read>product</read>
  <update>product</update>
  <delete>product</delete>
</permissions>
```

> After changing the permissions: increase the app version and update the app.

### Client-side privilege check (base options)

```ts
notification.dispatch({
  title: 'Report ready',
  message: 'Your report is ready',
  privileges: ['product:read'],  // the action is skipped if the privilege is missing
});
```

**Important**: This is only a UI-side check. Server-side authorization is still required.

---

## URL persistence on page reload

For modules with their own router, the current URL can be sent to the admin so that the correct state is restored after a reload:

```ts
// once
location.updateUrl(new URL(window.location.href));

// automatically on URL changes
location.startAutoUrlUpdater();
```

Available from Shopware 6.6.8.0.
