# Jest for a plugin's administration

**Everything the plugin adds to the administration is tested**: every component, function,
statement, method, button, page, dropdown, flow and mixin. The threshold enforces it — the
run fails below 100 %, so a gap cannot reach the branch quietly.

Shopware ships no plugin Jest setup. Every file below is the plugin's own, and versions are
pinned to what the target Shopware version declares so the test environment matches the
runtime.

## Where the files go

All under `src/Resources/app/administration/`:

```
src/Resources/app/administration/
├── jest.config.js
├── babel.config.js
├── package.json
├── test/
│   ├── _setup/shopware.js           the global Shopware stub
│   └── _transformer/
│       ├── twig.js                  strips Twig blocks from templates
│       └── style.js                 stylesheets carry no behaviour
└── src/
    ├── main.js                      registration; excluded from coverage
    ├── component/
    │   └── your-product-card/
    │       ├── index.js
    │       ├── index.spec.js        ← beside it
    │       ├── your-product-card.html.twig
    │       └── your-product-card.scss
    ├── module/
    │   └── your-supplier/
    │       ├── index.js
    │       ├── index.spec.js        ← the module registration is tested too
    │       ├── page/
    │       │   └── your-supplier-list/
    │       │       ├── index.js
    │       │       └── index.spec.js
    │       └── snippet/
    ├── extension/
    │   └── sw-product-detail-base/
    │       ├── index.js             an override of a core component
    │       └── index.spec.js
    ├── service/
    │   ├── your-api.service.js
    │   └── your-api.service.spec.js
    └── mixin/
        ├── your.mixin.js
        └── your.mixin.spec.js
```

## The rule for where a spec lives

**A spec sits beside the file it tests, in the same directory, named after it.** Never in a
mirrored `test/` tree.

| The file | Its spec |
|---|---|
| `component/your-card/index.js` | `component/your-card/index.spec.js` |
| `service/your-api.service.js` | `service/your-api.service.spec.js` |
| `mixin/your.mixin.js` | `mixin/your.mixin.spec.js` |
| `module/your-module/page/detail/index.js` | `module/your-module/page/detail/index.spec.js` |

Three reasons this is not arbitrary:

- **A missing spec is visible.** An `index.js` alone in a directory is obvious; a gap in a
  parallel tree is not.
- **Renaming a component moves its test with it.** In a mirrored tree the test is orphaned
  and nobody notices until coverage drops.
- **`jest.config.js` finds them without a second path**: `roots: ['<rootDir>/src']` plus
  `testMatch: ['**/*.spec.js']`.

**Every `.js` file under `src/` has one**, with a single exception: `main.js`, which is
registration executed by the administration and excluded from coverage. `collectCoverageFrom`
enforces exactly that:

```javascript
collectCoverageFrom: ['src/**/*.js', '!src/**/*.spec.js', '!src/main.js'],
```

Only `test/` — the setup and the transformers — sits outside `src/`, because it is test
infrastructure rather than plugin code, and it is not measured.

## package.json

```json
{
    "name": "your-plugin-administration",
    "version": "0.1.0",
    "private": true,
    "description": "Administration module of the YourPlugin plugin",
    "scripts": {
        "unit": "jest --config jest.config.js",
        "unit:watch": "jest --config jest.config.js --watch",
        "unit:coverage": "jest --config jest.config.js --coverage"
    },
    "devDependencies": {
        "@babel/core": "7.29.7",
        "@babel/preset-env": "7.29.5",
        "@vue/test-utils": "2.4.6",
        "babel-jest": "30.2.0",
        "jest": "30.2.0",
        "jest-environment-jsdom": "30.2.0",
        "vue": "3.5.22"
    }
}
```

Wire it into composer so one command runs everything:

```json
"test:admin": "npm --prefix src/Resources/app/administration run unit"
```

## jest.config.js

```javascript
module.exports = {
    rootDir: __dirname,
    testEnvironment: 'jsdom',
    roots: ['<rootDir>/src'],
    testMatch: ['**/*.spec.js'],
    moduleFileExtensions: ['js', 'json'],
    transform: {
        '^.+\\.js$': 'babel-jest',
        '^.+\\.(html|twig)$': '<rootDir>/test/_transformer/twig.js',
        '^.+\\.(css|scss)$': '<rootDir>/test/_transformer/style.js',
    },
    moduleNameMapper: {
        '^src/(.*)$': '<rootDir>/src/$1',
        // The full build carries the runtime template compiler, so a component that
        // assigns a template string renders instead of warning and staying empty.
        '^vue$': '<rootDir>/node_modules/vue/dist/vue.cjs.js',
    },
    setupFilesAfterEnv: ['<rootDir>/test/_setup/shopware.js'],
    collectCoverageFrom: ['src/**/*.js', '!src/**/*.spec.js', '!src/main.js'],
    coverageReporters: [
        'text',
        'text-summary',
        // html-spa defaults to lines, branches and functions only, so statements are
        // measured and enforced but never shown. Naming all four puts the column back.
        ['html-spa', { metricsToShow: ['statements', 'branches', 'functions', 'lines'] }],
        'json-summary',
    ],
    coverageDirectory: 'coverage',
    // 100 % everywhere, enforced rather than aspired to.
    coverageThreshold: {
        global: { statements: 100, branches: 100, functions: 100, lines: 100 },
    },
    clearMocks: true,
    restoreMocks: true,
};
```

**The `vue` mapping is not optional.** The default export is the runtime-only build; a
component that assigns `template` renders nothing and warns, and the test fails with an
empty wrapper for no visible reason.

**`main.js` is excluded from coverage** because it is registration, executed by the
administration and not by a test.

## babel.config.js

```javascript
module.exports = {
    presets: [
        ['@babel/preset-env', { targets: { node: 'current' } }],
    ],
};
```

## The transformers

`test/_transformer/twig.js` — a component imports its template and assigns it to the
`template` option. The Twig block directives exist so third parties can override parts of
the markup; they carry no meaning when rendering:

```javascript
module.exports = {
    process(sourceText) {
        const template = sourceText
            .replace(/\{%\s*block\s+[\w.]+\s*%\}/g, '')
            .replace(/\{%\s*endblock\s*%\}/g, '');

        return { code: `module.exports = ${JSON.stringify(template)};` };
    },
};
```

`test/_transformer/style.js`:

```javascript
module.exports = {
    process() {
        return { code: 'module.exports = {};' };
    },
};
```

## test/_setup/shopware.js — the global stub

A plugin's admin code runs inside the administration, where `Shopware` is a global. Under
Jest it is not. The stub records registrations so they can be asserted, and supplies the
mixins a page declares.

Its shape:

```javascript
const notifications = [];

// Vue binds mixin methods to the instance, which loses a jest.fn's identity, so calls
// are collected in an array instead.
const MIXINS = {
    listing: {
        data() {
            return {
                page: 1, limit: 25, term: null, total: 0,
                naturalSorting: false, freshSearchTerm: false,
                // A component test has no router; the mixin's route branch is exercised
                // by the core's own spec, not by ours.
                disableRouteParams: true,
            };
        },
        computed: {
            currentSortBy() { return this.freshSearchTerm ? null : this.sortBy; },
            maxPage() { return Math.ceil(this.total / this.limit); },
        },
        created() { this.getList(); },
        methods: {
            onPageChange({ page = 1, limit = 25 }) {
                this.page = page; this.limit = limit;
                return this.getList();
            },
            onSearch(term) { this.term = term || null; this.page = 1; return this.getList(); },
            // … onSortColumn, onRefresh, and the rest the templates bind to
        },
    },
    notification: {
        methods: {
            createNotificationError(config) { notifications.push({ type: 'error', ...config }); },
            createNotificationSuccess(config) { notifications.push({ type: 'success', ...config }); },
            // …
        },
    },
};

global.Shopware = {
    Component: { register: …, override: …, build: …, getComponentRegistry: … },
    Mixin: { getByName: (name) => MIXINS[name] },
    Service: (name) => services[name],
    Data: { Criteria: …, Classes: … },
    Classes: { ShopwareError },
    Application: { getContainer: … },
    Context: { api: {} },
    Utils: { format: { currency: … }, createId: … },
    Filter: { getByName: … },
    Module: { register: … },
    // get() only. The administration's own Store.register takes a factory function and
    // is not worth reproducing: a component test registers nothing.
    Store: { get: (name) => (name === 'error' ? errorStore : { api: {} }) },
};

// The stub resets itself, so no spec has to remember to.
beforeEach(() => {
    notifications.length = 0;
    errorStore.resetApiErrors();
});

global.ShopwareError = ShopwareError;
global.__shopwareNotifications = notifications;
global.__shopwareTestRegistry = { components, services };
```

**Read notifications through `global.__shopwareNotifications`**, the array itself:

```javascript
expect(global.__shopwareNotifications).toContainEqual(
    expect.objectContaining({ type: 'error' }),
);
```

Mirror the real `listing.mixin.js` closely enough that a mounted page does not throw on
its first binding. `AgDropshippersCompanion`'s version runs to 444 lines, and that is the
realistic size once a plugin has list pages — the sketch above names the keys, not their
bodies.

## Writing a spec

```javascript
import { mount } from '@vue/test-utils';
import YourCard from './index';

describe('component/your-card', () => {
    const createWrapper = (props = {}) => mount(YourCard, {
        props: { productId: 'a-product', ...props },
        global: {
            stubs: {
                // Meteor components get real templates, so slots render and a click
                // reaches the handler under test.
                'mt-card': { template: '<div><slot /></div>' },
                'mt-banner': { template: '<div><slot /></div>' },
                'sw-data-grid': { template: '<div><slot /></div>', props: ['dataSource'] },
            },
        },
    });

    it('asks for the offers of the product it was given', async () => { … });

    it('raises an error notification when the request fails', async () => {
        …
        expect(global.__shopwareNotifications).toContainEqual(
            expect.objectContaining({ type: 'error' }),
        );
    });
});
```

**Test names are sentences that state the rule**, not `test('renders')`. The name is the
documentation that survives.

## Running it

```bash
npm --prefix src/Resources/app/administration run unit
npm --prefix src/Resources/app/administration run unit:coverage
```
