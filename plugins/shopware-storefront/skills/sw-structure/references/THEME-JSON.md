<!-- distilled from shopware/storefront v6.7.13.1 — Resources/theme.json, Theme/ThemeCompiler.php, Theme/StorefrontPluginConfiguration/ -->

# Shopware Storefront — theme.json, loading and inheritance

`theme.json` is the contract between a theme and the compiler: which stylesheets and scripts belong
to it, which assets it ships, and what a shop owner may change in the administration. Everything
about a theme's appearance passes through this file.

## Contents

- [The file](#the-file)
- [The keys](#the-keys)
- [style, script and asset](#style-script-and-asset)
- [What @Plugins means](#what-plugins-means)
- [Configuration fields](#configuration-fields)
- [Field types](#field-types)
- [From a field to a stylesheet](#from-a-field-to-a-stylesheet)
- [Reading a value](#reading-a-value)
- [Inheritance](#inheritance)
- [How compilation works](#how-compilation-works)
- [Common mistakes](#common-mistakes)

## The file

The Storefront's own is `Resources/theme.json`; a theme plugin's lives at
`<plugin>/src/Resources/theme.json`. Its presence is what turns a plugin into a theme — there is no
other registration.

```
<theme-plugin>/src/Resources/
├── theme.json
├── app/storefront/src/       SCSS and JavaScript
├── app/storefront/dist/      compiled assets, committed
├── views/storefront/         template overrides
└── snippet/                  translations
```

## The keys

| Key | Type | Purpose |
|---|---|---|
| `name` | string | technical name, referenced when inheriting |
| `author` | string | shown in the administration |
| `description` | object | per-locale description, e.g. `{"en-GB": "…", "de-DE": "…"}` |
| `previewMedia` | string | path to the preview image in the theme list |
| `style` | array | SCSS entry points, in order |
| `script` | array | compiled JavaScript bundles |
| `asset` | array | directories copied to the public asset path |
| `config` | object | `fields` — everything editable in the administration |

`views` is **not** a key: template overrides are found by path convention
(`Resources/views/storefront/...`), not by declaration.

## style, script and asset

Order matters and is the whole mechanism:

```json
{
  "style": [
    "@Storefront",
    "app/storefront/src/scss/overrides.scss",
    "@Plugins",
    "app/storefront/src/scss/base.scss"
  ],
  "script": [
    "@Storefront",
    "@Plugins",
    "app/storefront/dist/storefront/js/my-theme/my-theme.js"
  ],
  "asset": [
    "@Storefront",
    "app/storefront/asset"
  ]
}
```

- **Before `@Storefront`** — variable overrides. This is the only place a `!default` variable can be
  changed, because the declaration must not have run yet.
- **After `@Storefront`** — rules that override compiled output.
- **Entries are compiled in the listed order**, and later files win at equal specificity.

An entry may also be an object, to pass a resolve path:

```json
{ "app/storefront/src/scss/base.scss": { "resolve": { "vendor": "app/storefront/vendor" } } }
```

That is how `~vendor/bootstrap/scss/bootstrap` resolves in the Storefront's own file.

## What @Plugins means

`@Plugins` is the placeholder for every **non-theme** plugin's storefront assets. Its position
decides whether your theme can override plugin styles:

- `@Plugins` **before** your SCSS — your rules win over plugin rules.
- `@Plugins` **after** your SCSS — plugin rules win over yours.

Omitting `@Plugins` entirely means no plugin styles are compiled at all, and every extension's
storefront styling disappears. That is almost never intended.

`@Storefront` is the same idea for the default theme's assets. Leaving it out gives an unstyled
shop — occasionally wanted for a theme built from scratch, but then Bootstrap is gone too.

## Configuration fields

```json
{
  "config": {
    "fields": {
      "sw-color-brand-primary": {
        "type": "color",
        "value": "#0042a0",
        "editable": true,
        "block": "themeColors",
        "order": 100
      }
    }
  }
}
```

| Property | Meaning |
|---|---|
| `type` | which control the administration renders |
| `value` | the default |
| `editable` | `false` hides it from the administration but keeps the SCSS variable |
| `block` | the tab it appears under |
| `section` | an optional group inside the tab |
| `order` | sort order within the block |
| `label` | per-locale label; defaults to the snippet key `sw-theme.<name>.label` |
| `helpText` | per-locale help text |
| `fullWidth` | render the control across the full width |
| `custom` | arbitrary data, not interpreted by the compiler |
| `scss` | `false` stops the value becoming an SCSS variable |

The Storefront ships **26 fields** in five blocks: `themeColors` (4), `statusColors` (4),
`typography` (4), `eCommerce` (9), `media` (5).

## Field types

| Type | Control | SCSS value |
|---|---|---|
| `color` | colour picker | the hex value |
| `text` | single-line input | the string |
| `fontFamily` | font selector | a font stack, e.g. `'Inter', sans-serif` |
| `media` | media selection | the asset URL |
| `checkbox` | checkbox | `true` / `false` |
| `number` | numeric input | the number |
| `select` | dropdown; needs `options` | the selected value |

A `select` carries its options in `custom.options`, each with `value` and per-locale `label`.

## From a field to a stylesheet

This is the chain a theme change actually travels:

```
theme.json field           sw-color-brand-primary: "#0042a0"
  -> the administration    the shop owner picks a colour
  -> theme_config          stored per sales channel
  -> compilation           $sw-color-brand-primary: #c81e1e;  injected before the SCSS
  -> skin/shopware/abstract/variables/_theme.scss    declares the !default
  -> skin/shopware/abstract/variables/_bootstrap.scss  $primary: $sw-color-brand-primary;
  -> Bootstrap             buttons, links, focus rings, badges, alerts
  -> --bs-primary          emitted as a CSS custom property
```

**Every field becomes an SCSS variable of the same name**, so `sw-color-brand-primary` is available
as `$sw-color-brand-primary`. That indirection is why changing one colour in the administration
restyles the whole shop: Shopware maps its own variables onto Bootstrap's, and Bootstrap derives
everything else from those.

## Reading a value

- **In SCSS** — `$sw-color-brand-primary`, injected before your files compile.
- **In Twig** — `theme_config('sw-color-brand-primary')`, and `theme_css_vars()` for the whole set
  as custom properties.
- **In CSS at runtime** — `var(--bs-primary)` for the Bootstrap-mapped ones.
- **In PHP** — the resolved configuration through `ResolvedConfigLoader`; rarely needed, since the
  values exist to reach the stylesheet.

## Inheritance

Two mechanisms that are often confused:

**Theme inheritance** (`"name"` in another theme's config) makes your theme build on a parent
theme's assets and configuration fields. Declare the parent's technical name; its `style`, `script`
and `config` are merged, and your entries win.

**Bundle inheritance** is what `@Storefront` and `@Plugins` do inside your own `style` array — not
theme inheritance, just an ordering placeholder.

**Template inheritance** is separate again and needs no declaration: a file at
`Resources/views/storefront/component/product/card/box-standard.html.twig` in your theme
automatically overrides the core file at the same path, and `{% sw_extends %}` inside it reaches the
original. Several plugins can extend the same template; Shopware's `sw_extends` supports that, where
Twig's own `extends` would not.

The resolution order for a template: the active theme, then themes it inherits from, then plugins by
priority, then the Storefront. The first match wins.

## How compilation works

```
bin/console theme:compile          all themes and sales channels
bin/console theme:compile --active-only
bin/console theme:change            assign a theme to a sales channel
bin/console theme:dump              write the resolved configuration for debugging
```

`ThemeCompiler` resolves the bundle names, collects the files from every `theme.json` in the
inheritance chain, injects the configuration as SCSS variables, compiles with `ScssPhpCompiler`, and
writes the result to a hashed path from `ThemePathBuilder`.

Compilation is **atomic**: the new output is written and only then swapped in, so a failed compile
leaves the running shop untouched. A theme change is not visible until a compile has run — this is
the reason a changed variable "does nothing" in production.

For development, the watcher (`bin/watch-storefront.sh`) recompiles on save; it does not replace a
real compile before deployment.

## Common mistakes

- **Overriding a variable after `@Storefront`.** A `!default` declaration has already run; your
  assignment is dead. Put variable overrides before it.
- **Dropping `@Plugins`.** Every extension's storefront styling disappears, usually noticed late.
- **Expecting a template change to need a declaration.** It does not — path convention is enough.
  Declaring template paths in `theme.json` does nothing.
- **Forgetting `theme:compile` after a change to `theme.json` or SCSS.** The dev watcher hides this
  until deployment.
- **Confusing `editable: false` with removing a field.** The field stays and keeps its SCSS
  variable; it is only hidden from the administration.
- **Hard-coding a value a shop owner should control.** If it is a colour, a font or a logo, make it
  a configuration field.
