<!-- distilled from shopware/storefront v6.7.13.1 — section/cms-section-sidebar, element/cms-element-sidebar-filter, layout/sidebar/, component/listing/ -->

# Shopware Storefront — the category sidebar and listing filters

The sidebar is not one component. It is a CMS **section layout** that happens to hold blocks, and
the filter panel inside it reads its data from a different slot than the one it sits in. Both facts
explain most of the surprises when adapting it.

## Contents

- [The sidebar is a section layout](#the-sidebar-is-a-section-layout)
- [What goes in the sidebar](#what-goes-in-the-sidebar)
- [The category navigation](#the-category-navigation)
- [The filter panel reads another slot](#the-filter-panel-reads-another-slot)
- [Where the filter data comes from](#where-the-filter-data-comes-from)
- [The filter types](#the-filter-types)
- [How a filter reaches the URL](#how-a-filter-reaches-the-url)
- [Off-canvas on small screens](#off-canvas-on-small-screens)
- [Adding your own filter](#adding-your-own-filter)
- [Rules for rebuilding the sidebar](#rules-for-rebuilding-the-sidebar)

## The sidebar is a section layout

A CMS page is built from **sections**, and a section has a layout. `cms-section-sidebar.html.twig`
is the two-column one:

```twig
<div class="cms-section-sidebar {{ sectionMobileBehaviorClass }} {{ layout }}">
  <div class="row">
    <div class="cms-section-sidebar-sidebar-content col-lg-4 col-xl-3">   {# sidebar #}
    <div class="cms-section-sidebar-main-content col-lg-8 col-xl-9">      {# main #}
```

Blocks: `page_content_section_sidebar`, `page_content_section_sidebar_row`,
`section_sidebar_content`, `section_sidebar_content_block`, `section_main_content`,
`section_main_content_block`.

Three consequences:

- **The column widths are Bootstrap classes in the template**, not configuration. Changing the ratio
  means overriding `section_sidebar_content` and `section_main_content` together — they must add up
  to 12.
- **The switch to a single column happens at `lg` (992px)**, because the classes are `col-lg-*`.
- **`sectionMobileBehaviorClass`** comes from the section's configuration in the administration and
  decides whether the sidebar is shown above, below or hidden on mobile. Removing the class from
  your override removes the editor's control over it.

`block.sectionPosition` tells a block whether it sits in the `sidebar` or the `main` column — the
same block template renders in both, and this is how it knows which one it is in.

## What goes in the sidebar

Whatever the editor puts there. In a category layout it is typically:

- **`cms-block-sidebar-filter`** → `cms-element-sidebar-filter` — the filter panel.
- **`cms-block-category-navigation`** → `cms-element-category-navigation` — the category tree.
- Any other block: text, image, product slider.

The sidebar has no fixed content, so a theme cannot assume the filter is there. Guard against its
absence when styling.

## The category navigation

`layout/sidebar/category-navigation.html.twig`, included by the CMS element of the same name.

```twig
{% set navigationMaxDepth = context.salesChannel.navigationCategoryDepth %}
{% set activeId = shopware.navigation.id %}
{% set activePath = shopware.navigation.pathIdList %}
```

Unlike the main navigation's flyout, **the depth comes from the sales channel** rather than a
template constant, so a channel configured for two levels renders two.

It recurses through `navigationTree` and marks the active branch from `activePath` — the same
globals the header navigation uses, so both stay in step.

Blocks: `layout_navigation_categories`, `layout_navigation_categories_list`,
`layout_navigation_categories_list_entry`. Classes: `.category-navigation`, `.level-{n}`,
`.category-navigation-entry`, `.category-navigation-link`. Styles live in
`skin/shopware/component/_category-navigation.scss`.

## The filter panel reads another slot

This is the part that surprises people. `cms-element-sidebar-filter.html.twig` has **no data
resolver of its own**. It reaches into the listing slot:

```twig
{% if cmsPage is defined %}
    {% set config = element.fieldConfig.elements %}
    {% set slot = cmsPage.getFirstElementOfType('product-listing') %}
    {% set listing = slot.data.listing %}
    {% set sidebar = block.sectionPosition == 'sidebar' %}
{% endif %}
```

So:

- **The filter panel only works on a page that also has a product listing.** Put it on a page
  without one and it renders nothing — `listing.aggregations` is empty and the whole element is
  skipped.
- **`getFirstElementOfType('product-listing')`** means the *first* listing wins. A page with two
  listings filters only the first.
- **Outside a CMS page**, `listing` and `sidebar` must be set by whoever includes the template.

The element renders nothing at all when `listing.aggregations.elements|length == 0` — no
aggregations, no filters, which is correct behaviour and not a bug to work around.

## Where the filter data comes from

```
ProductListingRoute
  -> the criteria are built, including the aggregations for each filter
  -> ProductListingCriteriaEvent          add or change aggregations here
  -> the search runs
  -> ProductListingResultEvent            add or change the result here
  -> ProductListingCmsElementResolver     attaches it as slot.data.listing
  -> listing.aggregations                 what the filter panel renders
  -> listing.currentFilters               what is currently applied
```

An **aggregation** is what makes a filter possible: it is the list of available values with their
counts. A filter with no aggregation has nothing to offer, which is why adding a filter always means
adding an aggregation first, in `ProductListingCriteriaEvent`.

## The filter types

`component/listing/filter-panel.html.twig` renders them; each is its own template:

| Template | Filter | Registered as |
|---|---|---|
| `filter/filter-boolean.html.twig` | a yes/no toggle, e.g. free shipping | `[data-filter-boolean]` |
| `filter/filter-range.html.twig` | min/max, e.g. price | `[data-filter-range]` |
| `filter/filter-multi-select.html.twig` | a checkbox list | `[data-filter-multi-select]` |
| `filter/filter-multi-select-list-item.html.twig` | one entry of that list | — |
| `filter/filter-property-select.html.twig` | properties; extends multi-select | `[data-filter-property-select]` |
| `filter/filter-rating-select.html.twig` | star rating; extends multi-select | `[data-filter-rating-select]` |
| `filter/filter-rating-select-item.html.twig` | one rating row | — |

`filter-property-select` and `filter-rating-select` **`sw_extends` `filter-multi-select`**, so a
change to the multi-select template reaches all three. That is usually what you want, and
occasionally the reason a change appears in more places than expected.

On the JavaScript side every filter plugin extends `FilterBasePlugin`, and `ListingPlugin`
(`[data-listing]`) coordinates them: it collects each filter's value, requests the new result and
replaces the listing markup.

## How a filter reaches the URL

1. The visitor changes a control; the filter plugin reports its value to `ListingPlugin`.
2. `ListingPlugin` builds a query string — `?p=1&properties=<id>|<id>&min-price=10`.
3. It requests the listing route and replaces the markup, then re-runs `PluginManager`.
4. The URL is updated through the History API, so the filtered listing is linkable and the back
   button works.
5. `Listing/afterRenderResponse` is published after the replacement — subscribe to it for anything
   that must run on the new markup.

Because the markup is replaced, **any JavaScript bound to a filter or product must be a registered
plugin**, not a one-off listener attached on page load.

## Off-canvas on small screens

The panel is shown inline in the sidebar on large screens and as an off-canvas below them. The
button carries `data-off-canvas-filter="true"` and `aria-haspopup="dialog"`;
`offcanvas-filter.plugin.js` moves the existing panel into an off-canvas rather than rendering a
second copy.

That is why there is one `#filter-panel-wrapper`: it is the same DOM node in both modes. A theme
that duplicates the panel for mobile ends up with two, and the filters stop agreeing with each
other.

## Adding your own filter

Four steps, in this order:

1. **Add the aggregation** in a `ProductListingCriteriaEvent` subscriber, so values and counts
   exist.
2. **Apply the filter** from the request in the same subscriber — read your parameter and add the
   criteria filter.
3. **Render the control** by overriding `filter-panel.html.twig` and including your own template.
   Extend an existing filter template when the shape matches; `filter-multi-select` covers most
   cases.
4. **Register a JavaScript plugin** extending `FilterBasePlugin`, implementing `getValues()`,
   `getLabels()` and `reset()`, so `ListingPlugin` can collect and reset it with the others.

Skipping step 4 gives a control that looks right and never filters anything.

## Rules for rebuilding the sidebar

- **Keep the column classes adding up to 12**, and change both columns together.
- **Keep `sectionMobileBehaviorClass`**, or the editor loses control of the mobile behaviour.
- **Do not assume the filter is present** — the sidebar's content is editor-configured.
- **Keep one `#filter-panel-wrapper`.** Inline and off-canvas are the same node.
- **Keep the `data-filter-*` attributes** and the `data-listing` wrapper, or filtering stops
  silently.
- **Expect markup replacement.** Bind behaviour through a plugin, and use
  `Listing/afterRenderResponse` for work after a filter run.
- **Check the category navigation depth** against the sales channel setting before changing the
  template.
- **Verify keyboard and screen reader use** in both modes — the off-canvas is a dialogue and needs
  focus handling, which BFSG requires.
