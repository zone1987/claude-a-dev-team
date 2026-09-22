# Administration — ESLint, Prettier and Stylelint

**All three belong in the administration**, configured in
`src/Resources/app/administration/`. The administration is Vue code and needs ESLint more
than the storefront does: a mistake in a component's `.html.twig` otherwise shows up only
in the browser.

| File | Purpose |
|---|---|
| `eslint.config.js` | flat config, with `eslint-plugin-vue` |
| `.prettierrc.json` | formatting |
| `.prettierignore` | **`*.html.twig` above all** |
| `.stylelintrc.json` | SCSS |

## `.prettierrc.json`

```json
{
    "singleQuote": true,
    "tabWidth": 4,
    "printWidth": 125,
    "trailingComma": "all"
}
```

**Identical in administration and storefront**, deliberately: moving between the two
directories should not require switching conventions.

| Setting | Why this value |
|---|---|
| `singleQuote: true` | Shopware's own admin and storefront code uses single quotes |
| `tabWidth: 4` | four spaces, as in the plugin's PHP and in the core |
| `printWidth: 125` | the same limit as ESLint's `max-len` below |
| `trailingComma: "all"` | makes the diff of the next added line one line instead of two |

**`printWidth` and `max-len` must agree.** That is the most common misconfiguration:
Prettier wraps at 80, ESLint allows 120 — and then Prettier formats a line ESLint
complains about afterwards.

## `.prettierignore`

```
node_modules/
coverage/
*.html.twig
```

**`*.html.twig` is why the file exists.** A Twig template looks like HTML to Prettier but
is not: `{% block … %}`, `{{ … }}` and `{% if … %}` are unintelligible text nodes to it. It
formats them anyway — and in doing so spreads block directives over several lines, which
breaks Shopware's template inheritance.

## `eslint.config.js`

ESLint 9 flat config, complete:

```js
const js = require('@eslint/js');
const vue = require('eslint-plugin-vue');
const jest = require('eslint-plugin-jest');
const prettier = require('eslint-config-prettier');
const globals = require('globals');

/**
 * ESLint for the plugin's administration code.
 *
 * The core's own configuration is not reusable here: it pulls in four local rule packages,
 * a TypeScript programme and a Vite resolver, none of which exist inside a plugin. The
 * rules that matter without them are taken over, including the line length and the ban on
 * warning comments that the core enforces.
 */
module.exports = [
    {
        ignores: [
            'node_modules/**',
            'coverage/**',
        ],
    },

    js.configs.recommended,
    ...vue.configs['flat/recommended'],

    {
        files: ['src/**/*.js'],
        languageOptions: {
            ecmaVersion: 2022,
            sourceType: 'module',
            globals: {
                ...globals.browser,
                Shopware: 'readonly',
            },
        },
        rules: {
            'max-len': ['error', 125, { ignoreRegExpLiterals: true }],
            'comma-dangle': ['error', 'always-multiline'],
            'no-console': ['error', { allow: ['warn', 'error'] }],
            // A TODO that reaches a live shop is a TODO nobody will read.
            'no-warning-comments': ['error', { location: 'anywhere' }],
            'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
            eqeqeq: ['error', 'always'],
            'prefer-const': 'error',
            'no-var': 'error',
            curly: ['error', 'all'],
            'vue/multi-word-component-names': 'off',
            'vue/require-default-prop': 'error',
            'vue/require-prop-types': 'error',
            // A tag is always closed in full: `</mt-button>` rather than `/>`. Easier to
            // read, and it is what PhpStorm stops underlining.
            'vue/html-self-closing': ['error', {
                html: { void: 'never', normal: 'never', component: 'never' },
                svg: 'never',
                math: 'never',
            }],
        },
    },

    {
        files: ['src/**/*.spec.js'],
        languageOptions: {
            globals: {
                ...globals.jest,
                ...globals.node,
                Shopware: 'readonly',
            },
        },
        plugins: { jest },
        rules: {
            ...jest.configs.recommended.rules,
            // A spec that asserts nothing passes and proves nothing.
            'jest/expect-expect': 'error',
            'jest/no-disabled-tests': 'error',
            'jest/no-focused-tests': 'error',
            'jest/no-identical-title': 'error',
            'jest/valid-expect': 'error',
            'max-len': ['error', 125, { ignoreRegExpLiterals: true }],
        },
    },

    prettier,
];
```

### Why not the core's configuration

Shopware's own ESLint setup pulls in **four local rule packages, a TypeScript programme
and a Vite resolver** — none of which exist inside a plugin. What carries without them is
taken over: the line length and the ban on warning comments, both of which the core
enforces itself.

### The rules worth explaining

**`no-warning-comments` with `location: 'anywhere'`** is the strictest rule here: **`TODO`
and `FIXME` in JavaScript are errors, not hints.** A TODO that reaches a live shop is one
nobody reads. What is to be done belongs in an issue or in `CONTEXT.md` — somewhere
a person reviews.

**`vue/html-self-closing` set to `'never'` everywhere** means `</mt-button>` rather than
`<mt-button />`. It reads more clearly where an element ends, and PhpStorm stops
underlining it.

**`vue/multi-word-component-names: 'off'`** — plugin components are prefixed anyway
(`acme-product-badge-list`), so the rule would only fire on generic helpers.

**The Jest block is separate** because a spec has different globals (`describe`, `it`,
`expect`, plus Node) than production code (browser plus `Shopware`). Without the split
ESLint either reports `describe is not defined` in specs or allows `describe` in
production code.

**`jest/expect-expect: 'error'`** is the JavaScript counterpart to PHPUnit's
`failOnRisky`: a spec that asserts nothing passes and proves nothing.

**`prettier` is the last entry in the array.** `eslint-config-prettier` switches off every
ESLint rule that collides with Prettier's formatting; as the final entry it overrides
everything before it. Placed earlier, the disabled rules come back.

## `.stylelintrc.json`

```json
{
    "extends": "stylelint-config-standard-scss",
    "ignoreFiles": [
        "node_modules/**",
        "coverage/**"
    ],
    "rules": {
        "color-hex-length": "long",
        "no-descending-specificity": null,
        "selector-class-pattern": null,
        "scss/dollar-variable-pattern": null,
        "custom-property-pattern": null,
        "max-nesting-depth": [3, {
            "ignore": ["blockless-at-rules", "pseudo-classes"]
        }],
        "scss/at-rule-no-unknown": true,
        "at-rule-no-unknown": null,
        "declaration-block-no-redundant-longhand-properties": null,
        "property-no-vendor-prefix": null,
        "scss/at-extend-no-missing-placeholder": true,
        "selector-no-qualifying-type": [true, {
            "ignore": ["attribute", "class"]
        }]
    }
}
```

**The same file goes in the storefront.** Each rule is explained in the storefront's
counterpart: `sw-theme` → `STOREFRONT-LINTING.md` in the `shopware-storefront` plugin.

## The scripts

```json
{
    "scripts": {
        "lint": "npm run lint:js && npm run lint:scss && npm run lint:format",
        "lint:js": "eslint --max-warnings 0 src",
        "lint:js:fix": "eslint --fix src",
        "lint:scss": "stylelint \"src/**/*.scss\"",
        "lint:scss:fix": "stylelint --fix \"src/**/*.scss\"",
        "lint:format": "prettier --check \"src/**/*.js\"",
        "lint:format:fix": "prettier --write \"src/**/*.js\""
    }
}
```

**The pattern runs throughout:** every checking task has a correcting one with the `:fix`
suffix — the same separation as the gate's `gate:fix` and `gate:check`.

**`--max-warnings 0`** turns every warning into an error. Without it warnings accumulate
until nobody looks.

**`prettier --check`** rather than `--write` in the checking variant: it reports what
would be formatted differently and changes nothing.

## In the gate

```json
{
    "scripts": {
        "lint:admin":     "npm --prefix src/Resources/app/administration run lint",
        "lint:admin-fix": "npm --prefix src/Resources/app/administration run lint:js:fix && npm --prefix src/Resources/app/administration run lint:format:fix",
        "gate:fix":       ["@rector:fix", "@cs-fix", "@lint:admin-fix"],
        "gate:check":     ["@phpstan", "@cs", "@rector", "@lint:admin", "@test:unit"]
    }
}
```

**The split follows the same logic as PHP:** what corrects goes in `gate:fix`, what checks
in `gate:check`. ESLint and Stylelint are the only npm tools fast enough to run on every
commit; Jest and Stryker stay out.

## The versions

```json
{
    "devDependencies": {
        "@eslint/js": "9.39.3",
        "eslint": "9.39.3",
        "eslint-config-prettier": "9.1.0",
        "eslint-plugin-jest": "28.14.0",
        "eslint-plugin-vue": "9.32.0",
        "globals": "15.15.0",
        "prettier": "3.6.2",
        "stylelint": "16.14.1",
        "stylelint-config-standard-scss": "14.0.0"
    }
}
```

**Pinned exactly, without `^`** — as with the PHP tooling. A new minor of ESLint adds
rules and turns the gate red without anybody having touched the code.
