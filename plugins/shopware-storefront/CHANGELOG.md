# Changelog

## [3.0.0] - 2026-08-26

### Added

- `sw-structure` skill: the Storefront's structure, generated from the Shopware source rather than
  written by hand. 21 reference files, ~14,500 lines.
  - All 2,206 Twig blocks with their nesting, per area (component, page, layout, CMS, utilities).
  - The 63 `sw_extends` edges and 203 `sw_include` targets with every call site.
  - Route to controller to page to template, both directions.
  - 33 page domains with their loaders, events and the getters each page exposes to Twig.
  - CMS: element type to administration component, resolver and template, with all 124
    configuration fields including source, type, default and entity binding.
  - JavaScript: 70 plugin registrations with selectors and options, 111 published events, every
    `data-*` attribute in the templates.
  - Design to code: CSS class to template, block and stylesheet.
  - Template variables: the 8 globals and their extension, controller hand-offs, `with` between
    templates, local assignments, and every Twig function and filter by extension.
  - Price calculation and the quantity selector chain.
  - JSON-LD and the analytics event system.
  - Header, footer and navigation, including the ESI mechanism and the flyout recursion.
  - The checkout: four pages, line item dispatch, every cart route, data layer events.
  - Modals and off-canvas panels.
  - Bootstrap 5.3.8: what it provides and what Shopware overrides.
  - 977 Bootstrap and 179 Shopware SCSS variables, 400 CSS custom properties, 27 functions, 84 mixins.
  - `theme.json`: keys, ordering, configuration fields, inheritance and compilation.
  - All 821 snippet keys with their text and the templates using them.
  - The cookie consent chain, from `CookieGroupCollectEvent` to `COOKIE_CONFIGURATION_UPDATE`.
  - The category sidebar and listing filters, including why the filter panel reads the listing slot.
  - The customer account: every page and its data, how orders are loaded, the cancellation
    transition, and why the edit-order screen shares the checkout confirm partials.
  - Forms: the seven field components, both validation layers, `formViolations`, the CMS form types,
    and the contact and revocation forms through to the Flow Builder mail.
  - The `prefers-*` media features against BFSG, including the 30 Shopware animations that carry no
    reduced-motion guard.
  - The project's CSS feature policy: `:has()` and container queries are not usable for layout.
- `shopware-storefront-lead` agent: orchestrates the plugin's skills, agents and commands, and drives
  the screen-design workflow. Delegates rather than editing.
- `shopware-structure-mapper` agent and `/sw-structure-map`: scan the project's own plugins, apps and
  theme plugins, and record which templates and blocks they override, including conflicts.
- `/sw-block-find`: look up a block, CSS class or data attribute and get its template, nesting,
  inheritance chain, stylesheet and JavaScript binding.
- Generator scripts under `scripts/`, each with a `--count` check against the source.
- `INVENTORY.json` covering 83 documentation pages.
- Accessibility (BFSG, WCAG 2.1 AA) recorded as binding in the skill and both agents.

### Changed

- `shopware-dev` (shopware-core) now carries a generated delegation table naming every Shopware
  plugin with its agent, skills and commands, plus the rules for tasks that span two domains.
- `shopware-storefront` agent points at `sw-structure` for structural lookups.

### Fixed

- Eight dead links across `sw-twig`, `sw-controller`, `sw-javascript` and `sw-theme`.


## 2.0.0 — 2026-08-20

Restructured from 39 skills into 5 domain skills. **Breaking:** every skill ID changed.

### Why

39 skills cost 17,804 characters of the skill listing budget — 223 % of the 8,000 available at a
200k context window, from this plugin alone. Claude Code truncates descriptions on overflow starting
with the least-used skills, so most of these silently stopped auto-activating.

### Changed

- **39 skills → 5**, grouped by domain. Listing cost 17,804 → 1,451 characters
  (223 % → 18 %).
- **No knowledge removed.** Every former `SKILL.md` body became a reference file; all reference
  files and bundled assets carried over, verified by content against a backup of the old layout
  (`scripts/verify-bundle.py`). 51 reference files and 7 bundled files remain.
- **References are flat siblings**, one level deep, with a table of contents in every file over
  100 lines that has more than two sections.
- **Descriptions rewritten** to the `<statement>. Use when <anchor>` pattern, under 200 characters,
  anchored on vocabulary specific to this domain rather than generic nouns.
- **`license` MIT**; author reduced to a GitHub handle.

Each former skill is now a file named after its topic inside the domain directory. The domain
`SKILL.md` maps them.

## 1.0.0

Initial release — 39 skills, one per documentation topic.
