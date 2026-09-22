# Storefront — Stylelint, ESLint and Prettier

**Stylelint always. ESLint and Prettier as soon as there is JavaScript.**

A storefront that consists only of SCSS and Twig still needs Stylelint, because the gate
runs it. It needs no Jest, no ESLint and no Prettier — a test setup without a subject is
ballast that has to be maintained, whose dependencies go stale, and that reports
"0 tests" on every run.

**But the moment a `.js` file exists under `src/Resources/app/storefront/src/`, all of it
becomes mandatory.** Storefront code runs in every customer's browser.

## `.stylelintrc.json` — complete, with every rule explained

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

### Rules tightened

| Rule | Value | Why |
|---|---|---|
| `color-hex-length` | `"long"` | `#ffffff` rather than `#fff`. Searching a file for a colour otherwise finds half the occurrences |
| `scss/at-rule-no-unknown` | `true` | catches typos in `@include`, `@mixin`, `@extend` |
| `scss/at-extend-no-missing-placeholder` | `true` | see below |
| `selector-no-qualifying-type` | `[true, {ignore: [attribute, class]}]` | see below |
| `max-nesting-depth` | `[3, …]` | see below |

### Rules switched off (`null`)

| Rule | Why |
|---|---|
| `no-descending-specificity` | fires on every override of a core selector. A plugin overriding Shopware styles produces descending specificity by necessity |
| `selector-class-pattern` | Shopware's class names (`is--active`, `has--error`, `js-…`) match none of the standard patterns |
| `scss/dollar-variable-pattern` | likewise for core variable names (`$sw-color-brand-primary`) |
| `custom-property-pattern` | likewise for CSS custom properties |
| `at-rule-no-unknown` | replaced by the SCSS-aware variant above. The CSS one does not know `@mixin` or `@include` and reports every one |
| `declaration-block-no-redundant-longhand-properties` | setting `margin-top` and `margin-bottom` separately is often exactly right when overriding; the shorthand would also reset left and right |
| `property-no-vendor-prefix` | Shopware's storefront sets prefixes where browsers still need them |

**`at-rule-no-unknown: null` together with `scss/at-rule-no-unknown: true` is not a
contradiction** but the usual pair: the generic CSS rule is switched off and replaced by
the SCSS-aware one.

### `scss/at-extend-no-missing-placeholder`

```scss
// forbidden
.my-tile { @extend .card; }

// allowed
%card-base { /* … */ }
.my-tile { @extend %card-base; }
```

`@extend` on a real class pulls in **every** rule that class appears in — including the
core's, including ones added later. The result is selector lists that look different after
every Shopware update. A placeholder (`%name`) exists only where it is defined.

### `selector-no-qualifying-type`

```scss
// forbidden
div.product-box { /* … */ }

// allowed (ignore: class)
.product-box.is--active { /* … */ }

// allowed (ignore: attribute)
input[type="checkbox"] { /* … */ }
```

`div.product-box` binds the style to the element. When Shopware changes the `div` to an
`article`, the rule stops applying — silently. The exceptions for `attribute` and `class`
are needed because `input[type=…]` and state classes are legitimate patterns.

### `max-nesting-depth: 3`

```scss
// just allowed
.a { .b { .c { color: red; } } }

// too deep
.a { .b { .c { .d { color: red; } } } }
```

The exceptions `blockless-at-rules` and `pseudo-classes` keep `@media` and `&:hover` from
counting — otherwise the practical limit would be one.

**Why three:** every level of nesting raises specificity. What sits four levels deep can
only be overridden with `!important` — and in a plugin whose styles meet the shop's and
the theme's, that is the start of a specificity race nobody wins.

## `eslint.config.js` — only when there is JavaScript

The same configuration as the administration **minus Vue**:

```js
const js = require('@eslint/js');
const jest = require('eslint-plugin-jest');
const prettier = require('eslint-config-prettier');
const globals = require('globals');

// Same rules as the administration, minus Vue: a storefront plugin is a plain class.
module.exports = [
    {
        ignores: [
            'node_modules/**',
            'coverage/**',
        ],
    },

    js.configs.recommended,

    {
        files: ['src/**/*.js'],
        languageOptions: {
            ecmaVersion: 2022,
            sourceType: 'module',
            globals: {
                ...globals.browser,
                PluginBaseClass: 'readonly',
                PluginManager: 'readonly',
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
        },
    },

    {
        files: ['src/**/*.spec.js'],
        languageOptions: {
            globals: {
                ...globals.jest,
                ...globals.node,
                PluginBaseClass: 'readonly',
                PluginManager: 'readonly',
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

**The two differences to the administration:**

1. no `eslint-plugin-vue`, no `vue/*` rules
2. different globals: `PluginBaseClass` and `PluginManager` instead of `Shopware`

Everything else — including `no-warning-comments`, the separate Jest block and `prettier`
as the final entry — is identical and explained in the administration's counterpart:
`sw-build` → `ADMIN-LINTING.md` in the `shopware-admin` plugin.

## `.prettierrc.json`

```json
{
    "singleQuote": true,
    "tabWidth": 4,
    "printWidth": 125,
    "trailingComma": "all"
}
```

**Byte-identical to the administration's.** `printWidth` must match ESLint's `max-len`.

**No `.prettierignore` is needed** where the Twig templates live under
`src/Resources/views/` rather than in the storefront app directory and the lint scripts
only cover `src/**/*.js`.

## `package.json`

**With JavaScript:**

```json
{
    "name": "{npm-name}-storefront",
    "private": true,
    "scripts": {
        "unit": "jest --config jest.config.js",
        "unit:watch": "jest --config jest.config.js --watch",
        "unit:coverage": "jest --config jest.config.js --coverage",
        "lint": "npm run lint:js && npm run lint:scss && npm run lint:format",
        "lint:js": "eslint --max-warnings 0 src",
        "lint:js:fix": "eslint --fix src",
        "lint:scss": "stylelint \"src/**/*.scss\"",
        "lint:scss:fix": "stylelint --fix \"src/**/*.scss\"",
        "lint:format": "prettier --check \"src/**/*.js\"",
        "lint:format:fix": "prettier --write \"src/**/*.js\""
    },
    "devDependencies": {
        "@babel/core": "7.29.7",
        "@babel/preset-env": "7.29.5",
        "@eslint/js": "9.39.3",
        "babel-jest": "30.2.0",
        "eslint": "9.39.3",
        "eslint-config-prettier": "9.1.0",
        "eslint-plugin-jest": "28.14.0",
        "globals": "15.15.0",
        "jest": "30.2.0",
        "jest-environment-jsdom": "30.2.0",
        "prettier": "3.6.2",
        "stylelint": "16.14.1",
        "stylelint-config-standard-scss": "14.0.0"
    }
}
```

A library that ends up in the browser goes under `dependencies`, not `devDependencies`.

**Without JavaScript — still required, because the gate reaches for it:**

```json
{
    "name": "{npm-name}-storefront",
    "private": true,
    "scripts": {
        "lint": "npm run lint:scss",
        "lint:scss": "stylelint \"src/**/*.scss\"",
        "lint:scss:fix": "stylelint --fix \"src/**/*.scss\""
    },
    "devDependencies": {
        "stylelint": "16.14.1",
        "stylelint-config-standard-scss": "14.0.0"
    }
}
```

## In the gate

```json
{
    "scripts": {
        "lint:scss":     "npm --prefix src/Resources/app/storefront run lint:scss",
        "lint:scss-fix": "npm --prefix src/Resources/app/storefront run lint:scss:fix",
        "gate:check":    ["@phpstan", "@cs", "@rector", "@lint:scss", "@test:unit"]
    }
}
```

**Stylelint and ESLint are the only npm tools that run in the gate.** Jest and Stryker
stay out because they take considerably longer; both linters are fast enough for every
commit.

Where the storefront has JavaScript, `lint` replaces `lint:scss` and covers all three
tools at once.
