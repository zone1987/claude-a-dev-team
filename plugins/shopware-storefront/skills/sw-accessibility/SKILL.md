---
name: sw-accessibility
description: >
  Shopware 6 Storefront Barrierefreiheit (a11y): WCAG 2.1 AA, BITV 2.0, Feature-Flag
  ACCESSIBILITY_TWEAKS, Breaking-Changes-Handling, Checklist (ARIA, Fokus, Tastatur,
  Semantik, Farben, Modals, Skip Links). Automatisierte Tests (axe, Lighthouse, WAVE).
  Trigger: "accessibility shopware", "barrierefreiheit shopware", "wcag shopware",
  "ACCESSIBILITY_TWEAKS", "a11y storefront", "screen reader shopware", "aria shopware",
  "keyboard navigation shopware", "axe devtools shopware", "eu accessibility directive",
  "fokus management storefront", "accessible extension". Shopware 6.6+/6.7.
---

# Shopware 6 — Storefront Barrierefreiheit (a11y)

WCAG 2.1 AA + BITV 2.0. Bootstrap-5-Basis mit ARIA-Rollen.

## Feature-Flag ACCESSIBILITY_TWEAKS

```dotenv
# .env oder .env.local
ACCESSIBILITY_TWEAKS=1
```

Nach Aktivierung: `bin/console theme:compile` (Styling-Änderungen).

Breaking a11y-Changes sind hinter diesem Flag versteckt — sie werden in Minor Releases eingeführt, aber erst mit v6.7.0 zum Standard.

## Breaking-Change-Pattern in Twig

```twig
{# @deprecated tag:v6.7.0 - Wird zu <ul>/<li> für korrekte Semantik #}
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

Beim Erweitern: **beide Blöcke** anpassen bis v6.7.0.

## a11y-Checklist für Shopware-Extensions

| Bereich | Anforderung |
|---|---|
| Semantisches HTML | `<button>`, `<a>`, `<nav>`, `<main>`, `<label for="...">` statt `<div>` |
| Dokument-Sprache | `<html lang="de">` |
| Fokus-Management | Sichtbare Fokus-Indikatoren; `focus()` nach Modal-Schließen |
| Tastatur | Tab/Enter/Esc/Pfeiltasten; kein `onclick` auf nicht-fokussierbare Elemente |
| ARIA | Sparsam; `role="alert"`, `aria-expanded`, `aria-hidden`, `aria-live` |
| Bilder/Icons | `alt`-Texte; Icon-only Buttons mit `aria-label` |
| Farben | Kontrastverhältnis ≥ 4.5:1 (Text) — nicht nur Farbe als Info-Träger |
| Überschriften | Eine `<h1>`, korrekte Hierarchie `h2`→`h3`... |
| Skip Links | `<a href="#main-content" class="skip-link">Zum Inhalt springen</a>` |
| Modals | Fokus-Trap im Modal; Fokus-Rückgabe nach Schließen |
| Formulare | `<label>`, `aria-describedby` für Fehlermeldungen |
| `<title>` | Bei Seitenwechsel aktualisieren |

## Testing-Tools

- **Lighthouse** (Chrome DevTools): Accessibility Score
- **axe DevTools**: Detaillierte ARIA/Struktur-Analyse
- **WAVE (WebAIM)**: HTML-Struktur und ARIA-Fehler
- **NVDA** (Windows) / **VoiceOver** (Mac/iOS): Screen-Reader-Tests
- **Keyboard-Only**: Tab, Shift+Tab, Enter, Space, Esc

Vollständige Referenz + Changelog bekannter a11y-Fixes: `references/deep/accessibility.md`.
