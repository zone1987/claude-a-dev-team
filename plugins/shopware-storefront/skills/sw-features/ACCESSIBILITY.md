# Shopware 6 — Storefront accessibility (a11y)

WCAG 2.1 AA + BITV 2.0. Bootstrap 5 base with ARIA roles.

## Feature flag ACCESSIBILITY_TWEAKS

```dotenv
# .env or .env.local
ACCESSIBILITY_TWEAKS=1
```

After activation: `bin/console theme:compile` (styling changes).

Breaking a11y changes are hidden behind this flag — they are introduced in minor releases, but only become the default with v6.7.0.

## Breaking-change pattern in Twig

```twig
{# @deprecated tag:v6.7.0 - Becomes <ul>/<li> for correct semantics #}
{% if feature('ACCESSIBILITY_TWEAKS') %}
  <ul class="sidebar-list">
    {% block component_list_items_inner %}
      <li class="list-item"><a href="#">Item</a></li>
    {% endblock %}
  </ul>
{% else %}
  <div class="sidebar-list">
    {% block component_list_items %}
      <div class="list-item"><a href="#">Item</a></div>
    {% endblock %}
  </div>
{% endif %}
```

When extending: adjust **both blocks** until v6.7.0.

## a11y checklist for Shopware extensions

| Area | Requirement |
|---|---|
| Semantic HTML | `<button>`, `<a>`, `<nav>`, `<main>`, `<label for="...">` instead of `<div>` |
| Document language | `<html lang="de">` |
| Focus management | Visible focus indicators; `focus()` after closing a modal |
| Keyboard | Tab/Enter/Esc/arrow keys; no `onclick` on non-focusable elements |
| ARIA | Sparingly; `role="alert"`, `aria-expanded`, `aria-hidden`, `aria-live` |
| Images/icons | `alt` texts; icon-only buttons with `aria-label` |
| Colors | Contrast ratio ≥ 4.5:1 (text) — color must not be the only carrier of information |
| Headings | One `<h1>`, correct hierarchy `h2`→`h3`... |
| Skip links | `<a href="#main-content" class="skip-link">Skip to content</a>` |
| Modals | Focus trap inside the modal; return focus after closing |
| Forms | `<label>`, `aria-describedby` for error messages |
| `<title>` | Update on page change |

## Testing tools

- **Lighthouse** (Chrome DevTools): accessibility score
- **axe DevTools**: detailed ARIA/structure analysis
- **WAVE (WebAIM)**: HTML structure and ARIA errors
- **NVDA** (Windows) / **VoiceOver** (Mac/iOS): screen reader tests
- **Keyboard-only**: Tab, Shift+Tab, Enter, Space, Esc

Full reference + changelog of known a11y fixes: `ACCESSIBILITY-DETAIL.md`.
