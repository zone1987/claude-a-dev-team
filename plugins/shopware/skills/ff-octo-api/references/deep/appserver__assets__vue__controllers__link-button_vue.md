# LinkButton Vue-Komponente (/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/link-button.vue)

## Zweck

Wrapper-Komponente für Meteor Design System Button (`mt-button`), die als Hyperlink (`<a>`) fungiert. Konvertiert eine Schaltfläche zur Navigation via href-Attribut, ohne dass JS-Navigation oder Router-Links nötig sind. Typischerweise für Kontextnavigation in Listen (order-table.vue, template-table.vue) und Detail-Ansichten im AppServer eingesetzt.

## Typ & Struktur

- **Komponente**: Vue 3 Single File Component (SFC)
- **Framework**: Composition API mit `<script setup>`
- **Abhängigkeiten**: `@shopware-ag/meteor-component-library` (MtButton)
- **Template-Struktur**: 
  - Root: `<a :href="href">` (Native HTML-Link)
  - Child: `<mt-button>` (Shopware Meteor Design System Button)

## Properties (defineProps)

### Erforderliche Props

| Prop | Typ | Default | Bedeutung |
|------|-----|---------|-----------|
| `href` | String | **erforderlich** | Ziel-URL für den Link (wird auf `<a href>` gemappt) |
| `text` | String | **erforderlich** | Button-Text/Label (wird als Slot-Inhalt an mt-button übergeben) |

### Optionale Props – Styling & Verhalten

| Prop | Typ | Default | Bedeutung |
|------|-----|---------|-----------|
| `variant` | String | `'primary'` | Button-Variante (z.B. primary, secondary, danger) |
| `actionVariant` | String | `'secondary'` | Action-Variante für Hover/aktiven Zustand |
| `size` | String | `'small'` | Größe des Buttons (small, medium, large) |
| `disabled` | Boolean | `false` | Button-Status deaktiviert (UI-Klasse, blockiert aber nicht den Link) |
| `square` | Boolean | `false` | Quadratische Button-Form (nur Icon-Buttons) |
| `block` | Boolean | `false` | Block-Level Button (volle Breite des Containers) |
| `isLoading` | Boolean | `false` | Loading-Spinner anzeigen (z.B. während Datenladung) |
| `ghost` | Boolean | `false` | Ghost-Style: transparenter Hintergrund |
| `showFrontIcon` | Boolean | `false` | Icon vor dem Text anzeigen |
| `showBackIcon` | Boolean | `false` | Icon nach dem Text anzeigen |
| `iconFront` | Object | `null` | Front-Icon-Objekt (Struktur: abhängig von Meteor-Icon-API) |
| `iconBack` | Object | `null` | Back-Icon-Objekt (Struktur: abhängig von Meteor-Icon-API) |

## Template-Struktur

```vue
<a :href="href">
    <mt-button
        :variant="variant"
        :action-variant="actionVariant"
        :size="size"
        :disabled="disabled"
        :square="square"
        :block="block"
        :is-loading="isLoading"
        :ghost="ghost"
        :show-front-icon="showFrontIcon"
        :show-back-icon="showBackIcon"
        :icon-front="iconFront"
        :icon-back="iconBack"
    >
        {{ text }}
    </mt-button>
</a>
```

## Besonderheiten & Fallstricke

1. **Semantisch als Link, nicht als Button**: Die Komponente ist ein `<a>`-Element mit Style-Eigenschaften eines `<button>`. Dies hat Auswirkungen auf:
   - **Keyboard-Navigation**: Links werden mit Tab navigiert (nicht als Button-Reihenfolge)
   - **Screenreader**: Werden als "Link" angesagt, nicht als "Button"
   - **Standard-Verhalten**: Beim Klick wird Standard-Link-Verhalten ausgelöst (neue URL, History)

2. **disabled-Prop hat keine Auswirkung auf Navigation**: Das `disabled`-Prop wird nur auf `mt-button` übergeben und deaktiviert optisch die UI, blockiert aber nicht das Hyperlink-Verhalten. Für echte Deaktivierung müsste die href-Navigation mit CSS (`pointer-events: none`) oder JS verhindert werden.

3. **Kein Click-Handler oder Event-Emitting**: Die Komponente gibt keine Events aus und hat keine Hooks. Sie delegiert vollständig an HTML-Link-Verhalten.

4. **Icon-Struktur nicht definiert**: Das Format von `iconFront` und `iconBack` hängt von der `MtButton`-Komponente der Meteor-Library ab (wahrscheinlich Icon-Objekt mit `name` und `size`, aber nicht dokumentiert in dieser Datei).

## Einsätze & Aufrufer

- **order-table.vue**: `import LinkButton from "./link-button.vue"` – Navigation zu Order-Details
- **custom-product/template-table.vue**: `import LinkButton from "../link-button.vue"` – Navigation zu Produkteditoren oder Vorschau
- Typischerweise für Kontextnavigation in Tabellenzeilen (Spalte mit Action-Links)

## Verwandte Dateien

- `/assets/vue/controllers/order-table.vue` – Aufrufer (Order-Tabelle)
- `/assets/vue/controllers/custom-product/template-table.vue` – Aufrufer (Produkt-Tabelle)
- `@shopware-ag/meteor-component-library` – MtButton-Komponente (externe Dependency)

## Besonderheiten für AppServer-Kontext

- **Tourismus/Ticketing-Booking**: Wird für Navigationslinks in Order- und Produkt-Management-Listen verwendet
- **Keine Session/Cart-Abhängigkeit**: Reine Präsentationskomponente, keine State-Verwaltung
- **Keine Event-Dispatcher**: Nicht mit Symfony-Events oder FfOctoApi-Domain-Events verbunden
- **Meteor Design System**: Konsistent mit Shopware Admin UI Design Language
