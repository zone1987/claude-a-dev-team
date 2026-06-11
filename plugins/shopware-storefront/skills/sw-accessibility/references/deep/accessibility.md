# Shopware 6 Storefront Barrierefreiheit (vollständige Referenz)

Quellen: `guides/development/accessibility/index.md`, `storefront-accessibility.md`, `accessibility-checklist.md`

## Überblick

Shopware verpflichtet sich zur WCAG 2.1 Level AA und BITV 2.0. Barrierefreiheit betrifft sowohl den Core-Storefront als auch alle Custom Themes und Extensions.

- Rechtliche Compliance (EU Web Accessibility Directive)
- Bessere Usability für alle Nutzer
- Verbessertes SEO und Performance
- Zukunftssichere Storefront-Implementierungen

**Design-Referenz**: https://shopware.design/foundations/accessibility.html
**Blog**: https://www.shopware.com/en/news/accessible-online-store-by-2025/

## Shopware's Ansatz

- WCAG 2.1 AA und BITV 2.0 als Ziel
- Bootstrap 5 Basis mit eingebauten ARIA-Rollen
- Automatisierte E2E-Tests mit Playwright + axe Reporter
- Accessibility-Verbesserungen in Regular Minor Releases (kein "Big Bang Release")

## Feature Flag: ACCESSIBILITY_TWEAKS

Breaking a11y-Änderungen (HTML/Twig-Struktur, CSS) werden hinter dem Flag `ACCESSIBILITY_TWEAKS` eingeführt:

```dotenv
# .env oder .env.local
ACCESSIBILITY_TWEAKS=1
```

Nach Aktivierung Theme neu kompilieren:
```bash
bin/console theme:compile
```

### Versionsstrategie

| Shopware Version | Accessibility-Status |
|---|---|
| **6.7+** | Alle a11y-Verbesserungen als Standard (ACCESSIBILITY_TWEAKS wird Default) |
| **6.6+** | a11y-Features eingeführt (über ACCESSIBILITY_TWEAKS testen) |
| **Shopware 5** | Keine Accessibility-Unterstützung |

## Beispiel: Breaking-Change-Handling in Twig

Extension-Entwickler müssen beide Varianten unterstützen bis v6.7.0:

```twig
{# @deprecated tag:v6.7.0 - Die Liste wird zu `<ul>` und `<li>` für verbesserte Barrierefreiheit #}
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
    {# @deprecated tag:v6.7.0 - Verwende stattdessen `component_list_items_inner` mit `<li>` #}
    {% block component_list_items %}
      <div class="list-item"><a href="#">Item</a></div>
      <div class="list-item"><a href="#">Item</a></div>
      <div class="list-item"><a href="#">Item</a></div>
    {% endblock %}
  </div>
{% endif %}
```

Extension, die den Block überschreibt:

```twig
{% sw_extends '@Storefront/storefront/component/list.html.twig' %}

{# Neue Struktur bereits berücksichtigen: #}
{% block component_list_items_inner %}
  {{ parent() }}
  <li class="list-item"><a href="#">Mein Item</a></li>
{% endblock %}

{# Kann nach v6.7.0 entfernt werden: #}
{% block component_list_items %}
  {{ parent() }}
  <div class="list-item"><a href="#">Mein Item</a></div>
{% endblock %}
```

## Storefront Accessibility Checklist

### Semantisches HTML

```html
<!-- Gut: Native Elemente mit semantischer Bedeutung -->
<button onclick="...">Klicken</button>
<a href="/produkt">Produktseite</a>
<nav aria-label="Hauptnavigation">...</nav>
<main id="main-content">...</main>

<!-- Schlecht: divs ohne Semantik -->
<div onclick="...">Klicken</div>
```

- `<button>`, `<a>`, `<select>` statt `<div>` oder `<span>` für Aktionen
- Layout: `<nav>`, `<main>`, `<header>`, `<footer>`
- Formulare: `<label for="input-id">` + passende `id` — Placeholder reicht nicht!

### Dokument-Sprache

```html
<html lang="de">  <!-- oder 'en', 'fr', etc. -->
```

Screen Reader braucht dies für korrekte Aussprache.

### Barrierefreie Formulare

```html
<!-- Verknüpfte Labels -->
<label for="email">E-Mail-Adresse</label>
<input id="email" type="email" aria-describedby="email-hint email-error">
<p id="email-hint">Format: name@beispiel.de</p>
<p id="email-error" role="alert">Bitte gültige E-Mail eingeben.</p>
```

- `aria-describedby` für Hilfe- und Fehlermeldungen
- Fehler nicht nur durch Farbe (rot) — zusätzlich Icon oder Text
- `role="alert"` für dynamische Fehlermeldungen

### Fokus-Management

```js
// Focus nach Modal-Schließen zurückgeben
modalCloseButton.addEventListener('click', () => {
  modal.close();
  triggerButton.focus();
});

// Focus nach Fehler auf ersten Fehler setzen
const firstError = form.querySelector('[aria-invalid="true"]');
if (firstError) firstError.focus();
```

- `tabindex="0"` für custom Interactive Elements
- Fokus-Outline nicht entfernen ohne sichtbare Alternative
- Natürlichen Tab-Flow nicht mit `tabindex > 0` stören

### Tastatur-Zugänglichkeit

```js
// Keyboard-Unterstützung für custom Elements
element.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    element.click();
  }
});
```

- `Enter` und `Space` aktivieren Interactive Elements
- Custom Widgets: Arrow Keys + erwartete Keyboard-Patterns
- Kein `onclick` auf nicht-fokussierbare Elemente ohne Keyboard-Support

### ARIA

```html
<!-- Expandierbares Panel -->
<button aria-expanded="false" aria-controls="panel-id">Filter anzeigen</button>
<div id="panel-id" aria-hidden="true">...</div>

<!-- Live Region für dynamische Updates -->
<div aria-live="polite" id="cart-count">3 Artikel im Warenkorb</div>

<!-- Icon-Button mit Label -->
<button aria-label="Produkt löschen">
  <svg aria-hidden="true">...</svg>
</button>
```

ARIA nur wenn natives HTML nicht ausreicht. Bevorzuge native HTML-Elemente.

### Skip Links

```html
<!-- Erstes Element im body -->
<a href="#main-content" class="skip-link">Zum Hauptinhalt springen</a>

<!-- ... Navigation ... -->

<main id="main-content">
  <!-- Seiteninhalt -->
</main>
```

```scss
.skip-link {
  position: absolute;
  top: -100%;
  
  &:focus {
    top: 0; /* Sichtbar machen bei Tastaturnavigation */
  }
}
```

### Modals und Popovers

```js
// Fokus-Trap im Modal
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    // Fokus innerhalb des Modals halten
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
    triggerButton.focus(); // Fokus zurückgeben
  }
});
```

### Farben und Kontrast

- Kontrastverhältnis Text: ≥ 4.5:1 (normal) / ≥ 3:1 (groß, ≥18px oder 14px fett)
- Tool: https://webaim.org/resources/contrastchecker/
- Informationen nicht nur durch Farbe (Fehler: Farbe + Icon oder Text)

### Überschriften-Hierarchie

```html
<h1>Produktname</h1>       <!-- Nur eine h1 pro Seite -->
  <h2>Beschreibung</h2>
    <h3>Details</h3>
  <h2>Bewertungen</h2>
```

### Seitentitel

```js
// Bei SPA-Routenwechsel:
document.title = `${pageName} | ${shopName}`;
```

## Bekannte a11y-Verbesserungen (Iteration 1)

| Thema | Breaking | Version |
|---|---|---|
| Fehlende Semantik Formular-Adressen-Überschriften | Nein | v6.6.6.0 |
| Bild-Zoom Modal Tastatur-Zugänglichkeit | Nein | v6.6.6.0 |
| Fokussierte Slides im Karussell | Ja | v6.6.6.0 |
| Fokus springt nach Modal-Schließen auf Seitenanfang | Nein | v6.6.6.0 |
| Text bis 200% Zoom ohne Umbrüche | Ja | v6.6.6.0 |
| Paginierung hat keine Links | Ja | v6.6.6.0 |
| Menge-Selektor nicht beschriftet | Nein | v6.6.5.0 |
| ESC-Taste schließt Navigation-Flyout | Nein | v6.6.3.0 |
| "Produkt entfernen"-Button-Beschriftung | Nein | v6.6.3.0 |
| Fehlende alt-Texte Warenkorb-Produktbilder | Nein | v6.6.3.0 |
| Account-Login-Seite Überschriften | Nein | v6.6.2.0 |
| Distinctive Document Titles | Nein | v6.6.1.0 |
| Leeres `<nav>`-Element in Top-Bar | Ja | v6.6.1.0 |

## Testing-Workflow

### Automatisiert

```bash
# Lighthouse Accessibility Audit (Chrome DevTools → Lighthouse Tab)
# axe DevTools Browser-Extension installieren
# WAVE: https://wave.webaim.org/
```

### Manuell

1. **Keyboard-Only Navigation**: Tab, Shift+Tab, Enter, Space, Esc, Pfeiltasten
2. **Screen Reader**: NVDA (Windows), VoiceOver (Mac: Cmd+F5)
3. **Zoom 200%**: Kein horizontales Scrollen, keine überlappenden Inhalte
4. **Farb-Kontrast**: Alle Text/Hintergrund-Kombinationen prüfen

### Vor Store-Einreichung

- Extension mit aktiviertem `ACCESSIBILITY_TWEAKS`-Flag testen
- Lighthouse Accessibility Score prüfen
- Keyboard-only Test durchführen
- Shopware QA-Verifikation (ggf. Selbst-Zertifizierung)

## Bekannte offene Issues

GitHub: https://github.com/shopware/shopware/issues?q=state%3Aopen+label%3Aarea%2Faccessibility

Neue Issues melden: Bug Report + Label `area/accessibility`.
