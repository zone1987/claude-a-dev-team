# Jest for a plugin's storefront JavaScript

Same rule as the administration — **everything the plugin ships is tested, 100 %, enforced
by the threshold** — but the setup differs in ways that cost hours if you assume otherwise.

## What is different from the administration

| | Administration | Storefront |
|---|---|---|
| What is tested | Vue components | plugin classes extending `Plugin` |
| Test helper | `@vue/test-utils` | none; plain DOM |
| Global to stub | `Shopware` | `window.PluginManager` |
| The hard part | the mixins | resolving `src/plugin-system/plugin.class` |
| Core precedent | plenty | **none for `matchMedia` or `Element.animate`** |

## Where the files go

```
src/Resources/app/storefront/
├── jest.config.js
├── babel.config.js
├── package.json
├── test/
│   ├── _mock/plugin.class.js        the Plugin base class double
│   └── _setup/storefront.js         PluginManager, animate, matchMedia
├── src/
│   ├── main.js                      registration; excluded from coverage
│   ├── plugin/
│   │   ├── free-shipping-progress.plugin.js
│   │   ├── free-shipping-progress.plugin.spec.js   ← beside it
│   │   ├── tier-display.plugin.js
│   │   └── tier-display.plugin.spec.js
│   ├── helper/
│   │   ├── currency.helper.js
│   │   └── currency.helper.spec.js
│   └── scss/                        not tested; no behaviour
└── dist/                            build artifact, git-ignored
```

## The rule for where a spec lives

**Beside the file it tests, in the same directory, named after it** — the same rule as the
administration, and for the same reasons: a missing spec is visible, a rename moves the
test with it, and `jest.config.js` needs no second path.

| The file | Its spec |
|---|---|
| `plugin/free-shipping-progress.plugin.js` | `plugin/free-shipping-progress.plugin.spec.js` |
| `helper/currency.helper.js` | `helper/currency.helper.spec.js` |

**Every `.js` under `src/` has one except `main.js`**, which is registration and excluded
from coverage. `scss/` holds no behaviour and is not measured. `dist/` is build output and
is git-ignored — never write a test against it.

## package.json

```json
{
    "name": "your-plugin-storefront",
    "version": "0.1.0",
    "private": true,
    "description": "Storefront JavaScript of the YourPlugin plugin",
    "scripts": {
        "unit": "jest --config jest.config.js",
        "unit:watch": "jest --config jest.config.js --watch",
        "unit:coverage": "jest --config jest.config.js --coverage"
    },
    "devDependencies": {
        "@babel/core": "7.29.7",
        "@babel/preset-env": "7.29.5",
        "babel-jest": "30.2.0",
        "jest": "30.2.0",
        "jest-environment-jsdom": "30.2.0"
    }
}
```

No `vue`, no `@vue/test-utils` — storefront plugins are plain classes.

## jest.config.js — and the ordering trap

```javascript
module.exports = {
    rootDir: __dirname,
    testEnvironment: 'jsdom',
    roots: ['<rootDir>/src'],
    testMatch: ['**/*.spec.js'],
    moduleFileExtensions: ['js', 'json'],
    transform: {
        '^.+\\.js$': 'babel-jest',
    },
    moduleNameMapper: {
        // THIS ENTRY MUST COME FIRST. moduleNameMapper is evaluated in order, and the
        // generic '^src/(.*)$' below would otherwise swallow it and look for the class
        // inside the plugin.
        '^src/plugin-system/plugin\\.class$': '<rootDir>/test/_mock/plugin.class.js',
        '^src/(.*)$': '<rootDir>/src/$1',
    },
    setupFilesAfterEnv: ['<rootDir>/test/_setup/storefront.js'],
    collectCoverageFrom: ['src/**/*.js', '!src/**/*.spec.js', '!src/main.js'],
    coverageReporters: [
        'text',
        'text-summary',
        ['html-spa', { metricsToShow: ['statements', 'branches', 'functions', 'lines'] }],
        'json-summary',
    ],
    coverageDirectory: 'coverage',
    coverageThreshold: {
        global: { statements: 100, branches: 100, functions: 100, lines: 100 },
    },
    clearMocks: true,
    restoreMocks: true,
};
```

## Resolving plugin.class — a local double, not a path into the core

A storefront plugin starts with:

```javascript
import Plugin from 'src/plugin-system/plugin.class';
```

Three ways to resolve it, and the recommendation is the third:

1. **Map into the shop's own storefront source.** A relative path across seven directory
   levels, which breaks the moment the plugin moves, and drags in `deepmerge`.
2. **Install the storefront bundle as a dev dependency.** Heavy, and version-coupled.
3. **A local test double.** No extra dependency, no fragile path. It has to grow if the
   plugin ever uses nested options or `data-*-config`, and that is an acceptable price.

`test/_mock/plugin.class.js`:

```javascript
/**
 * Stand-in for the storefront's Plugin base class.
 *
 * Reproduces what a plugin under test actually relies on: the element, the merged
 * options, and init() being called by the constructor.
 */
export default class Plugin {
    constructor(el, options = {}, pluginName = null) {
        this.el = el;
        this.$emitter = { publish: jest.fn(), subscribe: jest.fn(), unsubscribe: jest.fn() };
        this._pluginName = pluginName;

        this.options = { ...(this.constructor.options ?? {}), ...options };

        this.init();
    }

    init() {}

    update() {}
}
```

## test/_setup/storefront.js — three globals jsdom lacks

```javascript
/**
 * The storefront's plugin registry. Without it, `new MyPlugin(el)` throws inside the base
 * class constructor before a single assertion runs.
 */
global.PluginManager = {
    register: jest.fn(),
    getPlugin: jest.fn(() => ({ get: jest.fn(() => []) })),
    getPluginInstances: jest.fn(() => []),
    getPluginInstanceFromElement: jest.fn(),
    initializePlugins: jest.fn(),
    initializePlugin: jest.fn(),
};

/**
 * jsdom implements neither of these, and the core has no precedent for stubbing them —
 * verified by grep over the storefront's own test directory.
 */
Element.prototype.animate = jest.fn(() => ({
    finished: Promise.resolve(),
    cancel: jest.fn(),
    finish: jest.fn(),
    pause: jest.fn(),
    play: jest.fn(),
}));

window.matchMedia = jest.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
}));
```

**`clearMocks: true` wipes the implementation, not just the calls.** After the first test,
`window.matchMedia()` returns `undefined` and the plugin throws on `.matches`. Every spec
that depends on it sets the return value itself:

```javascript
const givenReducedMotion = (prefersNoPreference) => {
    window.matchMedia.mockReturnValue({ matches: prefersNoPreference, addEventListener: jest.fn() });
};
```

This is the single most common way a storefront suite fails for reasons that look
unrelated to the test.

## Writing a spec

```javascript
import FreeShippingProgressPlugin from './free-shipping-progress.plugin';

describe('plugin/free-shipping-progress', () => {
    let el;

    beforeEach(() => {
        document.body.innerHTML = '<div class="progress-bar"></div>';
        el = document.querySelector('.progress-bar');
        window.matchMedia.mockReturnValue({ matches: true, addEventListener: jest.fn() });
    });

    it('animates the bar to the percentage it was given', () => {
        new FreeShippingProgressPlugin(el, { progress: 40 });

        expect(el.animate).toHaveBeenCalledWith(
            expect.objectContaining({ width: [0, '40%'] }),
            expect.objectContaining({ duration: 500 }),
        );
    });

    it('skips the animation when the visitor asked for reduced motion', () => {
        window.matchMedia.mockReturnValue({ matches: false, addEventListener: jest.fn() });

        new FreeShippingProgressPlugin(el, { progress: 40 });

        expect(el.animate).toHaveBeenCalledWith(
            expect.anything(),
            expect.objectContaining({ duration: 0 }),
        );
    });
});
```

## Dead code is deleted, not covered

Reaching 100 % occasionally surfaces a branch that cannot be true. A real example:

```javascript
_isMotionActive() {
    const mediaQueryList = window.matchMedia('(prefers-reduced-motion: no-preference)');

    return (mediaQueryList === true || mediaQueryList.matches === true);
}
```

`matchMedia` never returns the boolean `true`. The left operand is dead code, and the right
answer is to delete it — not to write a test that props it up. A test whose only purpose is
to cover a line is exactly what the mutation rules forbid.

## The build has to work before any of this matters

The storefront build is easy to break silently. Webpack refuses an extension-less relative
import in a fully specified module context:

```javascript
// Fails: "Can't resolve './plugin/my.plugin'"
PluginManager.register('MyPlugin', () => import('./plugin/my.plugin'), '[data-my-plugin]');

// Works
PluginManager.register('MyPlugin', () => import('./plugin/my.plugin.js'), '[data-my-plugin]');
```

The core writes its own imports without the extension, but resolves them through the
absolute `src/` alias, which behaves differently. A plugin's relative import needs the
`.js`.

Verify the build before trusting any storefront test:

```bash
ddev exec bash -c "cd /var/www/html/shopware && shopware-cli project storefront-build --only-extensions YourPlugin"
```

**Shopware 6.7 builds storefront plugins with Webpack, not Vite.** Vite is used for the
core's Twig components and bundles (`build:shopware`, `build:components`); plugin JavaScript
goes through `webpack.config.js`. Both are present in `package.json`, which invites the
wrong conclusion.
