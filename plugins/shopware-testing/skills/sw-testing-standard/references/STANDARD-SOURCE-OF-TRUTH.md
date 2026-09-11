# The source of truth is Shopware's own repository

**Before deciding how something is done, look at how Shopware does it.** Not the
documentation, not memory, not a blog post — the source, at the exact version the shop
runs.

```
https://github.com/shopware/shopware/tree/v<VERSION>
```

**The tag must match the installed version.** Developing against 6.7.14.0 means
`https://github.com/shopware/shopware/tree/v6.7.14.0`; moving to 6.7.19.2 means
`https://github.com/shopware/shopware/tree/v6.7.19.2`. A trunk link is worthless — it
describes code the shop does not run.

## Finding the version you are on

```bash
ddev exec bin/console --version
# Shopware 6.7.14.0 (env: dev, debug: true)
```

Or from the lock file, which is what actually determines behaviour:

```bash
python3 -c "
import json
d = json.load(open('composer.lock'))
for p in d['packages']:
    if p['name'].startswith('shopware/'):
        print(p['name'], p['version'])
"
```

## A local checkout beats the web

If a full checkout at the exact version is available, read that instead. It carries what
the installed `vendor/shopware/` is stripped of: tests, ADRs, upgrade guides, the
administration and storefront sources with their own test suites.

```
<project>/backup/shopware/          a full checkout at the installed version
<project>/shopware/vendor/shopware/ the stripped one composer installed
```

Prefer the checkout. Its `src/Core/…/Test/` directories answer questions the documentation
does not address at all.

## What to look up there, and why it matters

Every one of these decided something in this standard, and each was wrong when assumed:

| Question | Where the answer is |
|---|---|
| Does this rule compare against the cart total or the goods? | `src/Core/Checkout/Cart/Rule/*.php`, the `match()` method |
| What order does this constructor take its arguments in? | the class — `Price` takes **net before gross**, which reads backwards |
| Is this flag on by default? | `src/Core/Framework/Resources/config/packages/feature.yaml` |
| How does the core resolve a currency price? | `DeliveryCalculator::getCurrencyPrice()` — three steps, all necessary |
| What is this constant's value? | the class, never memory |
| How is this service tagged, at what priority? | `src/Core/Checkout/DependencyInjection/*.php` |
| Is this field nullable in this version? | the entity — it changes between versions |
| How does the core test this kind of class? | the `Test/` directory beside it |
| What does the admin's own Jest setup look like? | `src/Administration/Resources/app/administration/jest.config.js` |
| What does the storefront's? | `src/Storefront/Resources/app/storefront/jest.config.js` and `jest.init.js` |

## Two examples of what assuming costs

**`Price` takes net before gross.** Assuming the opposite produced a test that failed, was
"corrected" into failing differently, and cost three rounds before anyone opened the
constructor. Thirty seconds of reading would have settled it.

**The storefront builds with Webpack in 6.7, not Vite.** `package.json` lists both, which
invites the opposite conclusion. Plugin JavaScript goes through `webpack.config.js`; Vite
builds the core's Twig components and bundles. Reading the `scripts` block settles it.

## Also worth checking there

- **Upgrade guides**: `UPGRADE-6.8.md` at the tag, for what is about to break.
- **The core's own ADRs**: `adr/` — decisions with their reasoning, in the same shape this
  workspace uses.
- **Deprecations**: `grep -rn "@deprecated tag:v6.8" src/` at the tag tells you what to
  mirror in your own code.

## Mirror what the core writes

Whatever annotation or `extends` clause Shopware puts on a class of a given kind, put it
there too. Collections carry `@template`, `@extends EntityCollection<TElement>` and
`@codeCoverageIgnore`; `getExpectedClass()` returns `@return class-string<X>`; migrations
carry `@internal`. Before adding a class kind the plugin does not have yet, open the
corresponding core class and copy the structure.

The same for deprecations: whatever the core marks `@deprecated tag:v6.8.0 - …`, code that
uses or mirrors it carries the same marker, with the same target tag. That turns the next
major upgrade into a grep instead of a survey.
