# Shopware 6 Storefront accessibility (full reference)

Sources: `guides/development/accessibility/index.md`, `storefront-accessibility.md`, `accessibility-checklist.md`

## Contents

- [Overview](#overview)
- [Shopware's approach](#shopwares-approach)
- [Feature Flag: ACCESSIBILITY_TWEAKS](#feature-flag-accessibility_tweaks)
- [Example: breaking-change handling in Twig](#example-breaking-change-handling-in-twig)
- [Storefront Accessibility Checklist](#storefront-accessibility-checklist)
- [Known a11y improvements (iteration 1)](#known-a11y-improvements-iteration-1)
- [Testing workflow](#testing-workflow)
- [Known open issues](#known-open-issues)

## Overview

Shopware commits to WCAG 2.1 Level AA and BITV 2.0. Accessibility concerns both the core Storefront and all custom themes and extensions.

- Legal compliance (EU Web Accessibility Directive)
- Better usability for all users
- Improved SEO and performance
- Future-proof Storefront implementations

**Design reference**: https://shopware.design/foundations/accessibility.html
**Blog**: https://www.shopware.com/en/news/accessible-online-store-by-2025/

## Shopware's approach

- WCAG 2.1 AA and BITV 2.0 as the goal
- Bootstrap 5 base with built-in ARIA roles
- Automated E2E tests with Playwright + axe reporter
- Accessibility improvements in regular minor releases (no "big bang release")

## Feature Flag: ACCESSIBILITY_TWEAKS

Breaking a11y changes (HTML/Twig structure, CSS) are introduced behind the `ACCESSIBILITY_TWEAKS` flag:

```dotenv
# .env or .env.local
ACCESSIBILITY_TWEAKS=1
```

Recompile the theme after activation:
```bash
bin/console theme:compile
```

### Version strategy

| Shopware version | Accessibility status |
|---|---|
| **6.7+** | All a11y improvements by default (ACCESSIBILITY_TWEAKS becomes the default) |
| **6.6+** | a11y features introduced (test via ACCESSIBILITY_TWEAKS) |
| **Shopware 5** | No accessibility support |

## Example: breaking-change handling in Twig

Extension developers must support both variants until v6.7.0:

```twig
{# @deprecated tag:v6.7.0 - The list becomes `<ul>` and `<li>` for improved accessibility #}
{% if feature('ACCESSIBILITY_TWEAKS') %}
  <ul class="sidebar-list">
    {% block component_list_items_inner %}
      <li class="list-item"><a href="#">Item</a></li>
      <li class="list-item"><a href="#">Item</a></li>
      <li class="list-item"><a href="#">Item</a></li>
    {% endblock %}
  </ul>
{% else %}
  <div class="sidebar-list">
    {# @deprecated tag:v6.7.0 - Use `component_list_items_inner` with `<li>` instead #}
    {% block component_list_items %}
      <div class="list-item"><a href="#">Item</a></div>
      <div class="list-item"><a href="#">Item</a></div>
      <div class="list-item"><a href="#">Item</a></div>
    {% endblock %}
  </div>
{% endif %}
```

An extension that overrides the block:

```twig
{% sw_extends '@Storefront/storefront/component/list.html.twig' %}

{# Already take the new structure into account: #}
{% block component_list_items_inner %}
  {{ parent() }}
  <li class="list-item"><a href="#">My item</a></li>
{% endblock %}

{# Can be removed after v6.7.0: #}
{% block component_list_items %}
  {{ parent() }}
  <div class="list-item"><a href="#">My item</a></div>
{% endblock %}
```

## Storefront accessibility checklist

### Semantic HTML

```html
<!-- Good: native elements with semantic meaning -->
<button onclick="...">Click</button>
<a href="/product">Product page</a>
<nav aria-label="Main navigation">...</nav>
<main id="main-content">...</main>

<!-- Bad: divs without semantics -->
<div onclick="...">Click</div>
```

- `<button>`, `<a>`, `<select>` instead of `<div>` or `<span>` for actions
- Layout: `<nav>`, `<main>`, `<header>`, `<footer>`
- Forms: `<label for="input-id">` + matching `id` — a placeholder is not enough!

### Document language

```html
<html lang="de">  <!-- or 'en', 'fr', etc. -->
```

Screen readers need this for correct pronunciation.

### Accessible forms

```html
<!-- Linked labels -->
<label for="email">Email address</label>
<input id="email" type="email" aria-describedby="email-hint email-error">
<p id="email-hint">Format: name@example.com</p>
<p id="email-error" role="alert">Please enter a valid email address.</p>
```

- `aria-describedby` for help and error messages
- Do not signal errors by color (red) alone — add an icon or text
- `role="alert"` for dynamic error messages

### Focus management

```js
// Return focus after closing a modal
modalCloseButton.addEventListener('click', () => {
  modal.close();
  triggerButton.focus();
});

// Move focus to the first error after a validation failure
const firstError = form.querySelector('[aria-invalid="true"]');
if (firstError) firstError.focus();
```

- `tabindex="0"` for custom interactive elements
- Do not remove the focus outline without a visible alternative
- Do not disturb the natural tab flow with `tabindex > 0`

### Keyboard accessibility

```js
// Keyboard support for custom elements
element.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    element.click();
  }
});
```

- `Enter` and `Space` activate interactive elements
- Custom widgets: arrow keys + expected keyboard patterns
- No `onclick` on non-focusable elements without keyboard support

### ARIA

```html
<!-- Expandable panel -->
<button aria-expanded="false" aria-controls="panel-id">Show filters</button>
<div id="panel-id" aria-hidden="true">...</div>

<!-- Live region for dynamic updates -->
<div aria-live="polite" id="cart-count">3 items in the cart</div>

<!-- Icon button with label -->
<button aria-label="Remove product">
  <svg aria-hidden="true">...</svg>
</button>
```

Use ARIA only when native HTML is not sufficient. Prefer native HTML elements.

### Skip Links

```html
<!-- First element in the body -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- ... Navigation ... -->

<main id="main-content">
  <!-- page content -->
</main>
```

```scss
.skip-link {
  position: absolute;
  top: -100%;
  
  &:focus {
    top: 0; /* make visible on keyboard navigation */
  }
}
```

### Modals and popovers

```js
// Focus trap inside the modal
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    // Keep focus within the modal
    const focusableElements = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    if (e.shiftKey && document.activeElement === firstElement) {
      e.preventDefault();
      lastElement.focus();
    } else if (!e.shiftKey && document.activeElement === lastElement) {
      e.preventDefault();
      firstElement.focus();
    }
  }
  if (e.key === 'Escape') {
    modal.close();
    triggerButton.focus(); // return focus
  }
});
```

### Colors and contrast

- Text contrast ratio: ≥ 4.5:1 (normal) / ≥ 3:1 (large, ≥18px or 14px bold)
- Tool: https://webaim.org/resources/contrastchecker/
- Do not convey information by color alone (error: color + icon or text)

### Heading hierarchy

```html
<h1>Product name</h1>      <!-- only one h1 per page -->
  <h2>Description</h2>
    <h3>Details</h3>
  <h2>Reviews</h2>
```

### Page title

```js
// On SPA route change:
document.title = `${pageName} | ${shopName}`;
```

## Known a11y improvements (iteration 1)

| Topic | Breaking | Version |
|---|---|---|
| Missing semantics in form address headings | No | v6.6.6.0 |
| Image zoom modal keyboard accessibility | No | v6.6.6.0 |
| Focused slides in the carousel | Yes | v6.6.6.0 |
| Focus jumps to the top of the page after closing a modal | No | v6.6.6.0 |
| Text up to 200% zoom without line breaks | Yes | v6.6.6.0 |
| Pagination has no links | Yes | v6.6.6.0 |
| Quantity selector not labelled | No | v6.6.5.0 |
| ESC key closes the navigation flyout | No | v6.6.3.0 |
| "Remove product" button label | No | v6.6.3.0 |
| Missing alt texts on cart product images | No | v6.6.3.0 |
| Account login page headings | No | v6.6.2.0 |
| Distinctive document titles | No | v6.6.1.0 |
| Empty `<nav>` element in the top bar | Yes | v6.6.1.0 |

## Testing workflow

### Automated

```bash
# Lighthouse accessibility audit (Chrome DevTools → Lighthouse tab)
# install the axe DevTools browser extension
# WAVE: https://wave.webaim.org/
```

### Manual

1. **Keyboard-only navigation**: Tab, Shift+Tab, Enter, Space, Esc, arrow keys
2. **Screen Reader**: NVDA (Windows), VoiceOver (Mac: Cmd+F5)
3. **Zoom 200%**: no horizontal scrolling, no overlapping content
4. **Color contrast**: check all text/background combinations

### Before store submission

- Test the extension with the `ACCESSIBILITY_TWEAKS` flag enabled
- Check the Lighthouse accessibility score
- Perform a keyboard-only test
- Shopware QA verification (self-certification where applicable)

## Known open issues

GitHub: https://github.com/shopware/shopware/issues?q=state%3Aopen+label%3Aarea%2Faccessibility

Report new issues: bug report + label `area/accessibility`.
