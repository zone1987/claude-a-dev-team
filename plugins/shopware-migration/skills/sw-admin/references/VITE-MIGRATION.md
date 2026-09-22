# Shopware 6.7 — Webpack to Vite

6.7 replaces Webpack with Vite for the administration build. Webpack had become slow and, more to
the point, largely unmaintained — many of its maintainers moved on, and the loaders Shopware used
followed, which made it a security risk to stay on.

## Contents

- [What it means for extensions](#what-it-means-for-extensions)
- [Migrating a custom config](#migrating-a-custom-config)
- [How the build works](#how-the-build-works)
- [The Vite plugins](#the-vite-plugins)
- [HMR and performance](#hmr-and-performance)

## What it means for extensions

**Apps: nothing.** Their build is already decoupled from Shopware.

**Plugins: only if you extend the build.** A plugin without its own `webpack.config.js` needs no
change at all.

## Migrating a custom config

| Step | |
|---|---|
| 1 | create `vite.config.mts` in `YourApp/src/Resources/app/administration/src` — note the path: the Webpack config lived in `.../administration/build/` |
| 2 | delete the old `webpack.config.js` |
| 3 | remove every Webpack dependency from `package.json` |
| 4 | add the Vite dependencies |

```javascript
// old, Webpack
module.exports = () => {
    return {
        resolve: {
            alias: { '@example': 'src/example' },
        },
    };
};
```

```typescript
// new, Vite
import { defineConfig } from 'vite';

export default defineConfig({
    resolve: {
        alias: { '@example': 'src/example' },
    },
});
```

That is the simplest possible case; how much work a real migration is depends entirely on what the
Webpack config did.

## How the build works

The feature flag is **`ADMIN_VITE`**, which is what lets the setup be tested.

The table below describes the **core's own build internals** — what Shopware runs inside its
administration bundle. A plugin never invokes any of it. A plugin is built with `shopware-cli`,
inside the container, and with nothing else:

```bash
ddev exec shopware-cli project admin-build --only-extensions <PluginName>
ddev exec shopware-cli project admin-watch --only-extensions <PluginName>
```

| Piece | Detail |
|---|---|
| Bundle information | `Shopware\Core\Framework\Plugin\Command\BundleDumpCommand` writes `<shopwareRoot>/var/plugins.json`; standalone as `ddev exec bin/console bundle:dump`. `shopware-cli` triggers it for you — a plugin build never calls it by hand |
| Building everything (core) | the core's own `build:js:admin` script. Not the plugin path: a plugin uses `ddev exec shopware-cli project admin-build --only-extensions <PluginName>` |
| The core config | `<shopwareRoot>/src/Administration/Resources/app/administration/vite.config.mts` — **core only, not extensions** |
| Extension build | `.../administration/build/plugins.vite.ts` reads `var/plugins.json` and calls Vite's `build` per plugin, picking up each plugin's own `vite.config` from its entry path |
| Dev server | the core's own `watch:admin` script; `plugins.vite.ts` calls `createServer` per plugin. For a plugin: `ddev exec shopware-cli project admin-watch --only-extensions <PluginName>` |

**Vite needs a different module loading order than Webpack**, which is why some core files are
duplicated as `*.vite.ts` — the entry point, for instance, is
`.../administration/src/index.vite.ts`.

Assets are loaded through the `pentatrion_vite` Symfony bundle for the core, resolving files from the
`entrypoints.json` its counterpart `vite-plugin-symfony` generates. For bundles and plugins,
`application.ts` injects the entries per environment: a production build reads
`/api/_info/config`, while the dev server is served `sw-plugin-dev.json` by Shopware's own
`shopware-vite-plugin-serve-multiple-static`.

## The Vite plugins

Shopware's own plugins are all prefixed `shopware-vite-plugin-`:

| Plugin | What it does |
|---|---|
| `asset-path` | prepends `window.__sw__.assetPath` to the chunk path, which is what makes a cluster setup serving assets from S3 work |
| `static-assets` | copies static admin assets from `static` into the output directory |
| `serve-multiple-static` | serves the dev-mode entry information as `sw-plugin-dev.json` |
| `override-component` | finds every `*.override.vue`, imports it into the entry file and registers it through `Shopware.Component.registerOverrideComponent`, so overrides load as soon as the plugin script is injected |
| `twigjs` | transforms `*.html.twig` files so Vite can load them |

Imports of Vue itself change shape, since Vue is provided globally:

```javascript
// from
import { ref } from 'vue';

// to
const { ref } = window['Shopware']['Vue'];
```

## HMR and performance

**Vite only hot-reloads `*.vue` files.** Until everything is a single-file component, HMR reaches
only that far; once it is, the setup can tell a change in a plugin from a change in the core.

Vite builds the core administration in roughly 18 seconds — over 50 % faster than Webpack. Dev mode
is not directly comparable: the Vite dev server starts instantly and moves the cost to the first
request, where Webpack compiles ahead of time before the server is ready.

## Source

[developer.shopware.com/docs/guides/upgrades-migrations/administration/vite.html](https://developer.shopware.com/docs/guides/upgrades-migrations/administration/vite.html),
Shopware 6.7, retrieved 2026-08-21.
