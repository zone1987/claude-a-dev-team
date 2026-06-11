# Build System Migration: Webpack to Vite

Shopware 6.7 replaces Webpack with Vite for administration builds. This reference covers the migration steps for plugin developers.

---

## Overview

| Aspect | Shopware 6.6 (Webpack) | Shopware 6.7 (Vite) |
|---|---|---|
| Build tool | Webpack 5 | Vite 6 |
| Dev server | webpack-dev-server | Vite dev server |
| Config file | `build/webpack.config.js` | `vite.config.js` |
| Template engine | Twig (via custom loader) | Twig (via `TwigPlugin`) |
| Vue version | Vue 2.7 / Vue 3 compat | Vue 3.5 |
| HMR | Webpack HMR | Vite HMR (faster) |
| Port (dev) | `:8080` | `:5173` |

---

## Migration Steps

### Step 1: Remove Webpack Configuration

If your plugin has a custom `build/webpack.config.js`, it is no longer used. Remove it:

```bash
rm -f Resources/app/administration/build/webpack.config.js
```

### Step 2: Update package.json

```json
{
    "name": "my-plugin-administration",
    "version": "1.0.0",
    "private": true,
    "scripts": {
        "dev": "vite",
        "build": "vite build"
    },
    "devDependencies": {
        "@vitejs/plugin-vue": "^5.2.0",
        "vite": "^6.0.0"
    }
}
```

### Step 3: Create vite.config.js (Optional)

Most plugins do **not** need a custom Vite config. Shopware's build system handles plugin integration automatically.

Only create a `vite.config.js` if you need custom build behavior:

```javascript
import { defineConfig } from 'vite';

export default defineConfig({
    build: {
        // Custom build options if needed
    },
});
```

### Step 4: Update Import Paths

Vite uses native ES modules. Ensure your imports use proper paths:

```javascript
// BEFORE (Webpack-specific)
import template from './my-component.html.twig';
const { Component } = Shopware;

// AFTER (ESM-compatible)
import template from './my-component.html.twig';
const { Component } = Shopware;
```

Most imports remain the same. Watch for:
- **Dynamic imports**: `require()` is not supported. Use `import()` instead.
- **Glob imports**: `require.context()` must be replaced with `import.meta.glob()`.

```javascript
// BEFORE (Webpack)
const modules = require.context('./modules', true, /\.js$/);

// AFTER (Vite)
const modules = import.meta.glob('./modules/**/*.js', { eager: true });
```

### Step 5: Update Asset References

```javascript
// BEFORE (Webpack)
const imagePath = require('./assets/image.png');

// AFTER (Vite)
import imagePath from './assets/image.png';
// or for dynamic:
const imagePath = new URL('./assets/image.png', import.meta.url).href;
```

---

## Admin SDK Update

The Admin Extension SDK has been renamed and updated:

```bash
# Remove old package
npm remove @shopware-ag/admin-extension-sdk

# Install new package
npm install @shopware-ag/meteor-admin-sdk@^6.4.0
```

### Update All Imports

```javascript
// BEFORE
import { notification } from '@shopware-ag/admin-extension-sdk';
import { window as sdkWindow } from '@shopware-ag/admin-extension-sdk';
import type { Entity } from '@shopware-ag/admin-extension-sdk/es/data';

// AFTER
import { notification } from '@shopware-ag/meteor-admin-sdk';
import { window as sdkWindow } from '@shopware-ag/meteor-admin-sdk';
import type { Entity } from '@shopware-ag/meteor-admin-sdk/es/data';
```

### Package Versions (Shopware 6.7)

Key dependencies in the Shopware 6.7 administration:

```json
{
    "@shopware-ag/meteor-admin-sdk": "6.4.0",
    "@shopware-ag/meteor-component-library": "4.24.0",
    "@shopware-ag/meteor-icon-kit": "5.4.0",
    "vue": "3.5.22",
    "vue-router": "4.5.0",
    "vue-i18n": "10.0.8",
    "pinia": "2.3.1",
    "vite": "6.4.1"
}
```

---

## Build Commands

### Development (watch mode)

```bash
# From Shopware root
bin/watch-administration.sh

# Or via DDEV
ddev exec bin/watch-administration.sh

# Watcher URL
# Administration: http://localhost:5173
```

### Production Build

```bash
# From Shopware root
bin/build-administration.sh

# Or via DDEV
ddev exec bin/build-administration.sh
```

### Using shopware-cli (if available)

```bash
ddev exec shopware-cli project admin-build --only-extensions YourPluginName
```

---

## Troubleshooting

### Common Issues

**"require is not defined"**
Replace `require()` calls with `import` statements. Vite uses native ESM.

**"Cannot find module"**
Check that your import paths use the correct file extensions. Vite is stricter about path resolution than Webpack.

**Twig templates not loading**
Ensure `.html.twig` files are in the same directory as your component's `index.js`/`index.ts`. The Twig plugin handles template compilation.

**HMR not working**
Make sure your dev server port (`:5173`) is accessible. Check proxy configuration if running behind DDEV.
