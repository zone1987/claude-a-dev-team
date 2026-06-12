# CollapsibleSection.vue

(/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/components/CollapsibleSection.vue)

## Zweck

Wiederverwendbare Vue-3-Komponentenfür eine Collapsible-Section in der Custom-Product-Verwaltung des AppServers. Sie stellt ein expandierbares/einklappbares Formular-Bereich mit optionalem Lösch-Button dar. Wird primär in den Custom-Product-Formularen verwendet, um komplexe Produktkonfigurationen übersichtlich zu strukturieren.

## Typ & Verwebung

- **Framework**: Vue 3 (Composition API mit `<script setup>`)
- **Komponenten-Typ**: SFC (Single File Component)
- **Abhängigkeiten**:
  - `@shopware-ag/meteor-component-library` (MtButton)
  - `vue-i18n` (useI18n für Internationalisierung)

## Props (Eingabe-Eigenschaften)

| Name | Typ | Default | Bedeutung |
|------|-----|---------|-----------|
| `title` | String | `''` | Anzeigetitel der Sektion. Falls leer, wird `'-'` als Fallback angezeigt. |
| `expanded` | Boolean | `false` | Steuert, ob die Sektion initial ausgeklappt ist. Zwei-Wege-Binding über `update:expanded`. |
| `removable` | Boolean | `false` | Zeigt optionalenLösch-Button nur wenn `true`. |

## Emits (Ereignisse)

| Event | Payload | Zweck |
|-------|---------|-------|
| `update:expanded` | Boolean | Wird emittiert, wenn Expand/Collapse-Button geklickt wird. Ermöglicht v-model-Binding: `v-model:expanded="myValue"`. |
| `remove` | (keine) | Wird emittiert, wenn der Lösch-Button geklickt wird. Parent muss die Sektion aus dem DOM entfernen. |

## Slots

| Name | Zweck |
|------|-------|
| Default (`<slot />`) | Beliebige Inhalte (üblicherweise Formular-Felder), die nur sichtbar sind wenn `expanded === true`. |

## Methoden

### `toggle()`

**Signatur**: `function toggle(): void`

**Zweck**: Toggled die `expanded`-Prop durch Emit des `update:expanded`-Events mit inversem Wert.

**Ablauf**:
1. Liest aktuellen `props.expanded`-Zustand
2. Emittiert `update:expanded` mit invertiertem Wert (`!props.expanded`)
3. Parent muss die Prop tatsächlich updaten (zwei-Wege-Binding über v-model)

**Aufrufer**: Expand/Collapse-Button im Header (`@click="toggle"`)

## Template-Struktur

### Wrapper
- `.custom-product-collapsible`: Root-Container mit CSS-Klasse für Styling

### Header (immer sichtbar)
- `.custom-product-collapsible-header`: Flex-Container mit Titel und Buttons
  - `.custom-product-collapsible-title`: Text `{{ title || '-' }}`
  - `.custom-product-collapsible-actions`: Flex-Container für Buttons
    - **Expand/Collapse-Button** (MtButton)
      - Größe: `small`, Variante: `secondary`
      - Label: Localized String (`t('template.form.collapse')` oder `t('template.form.expand')`)
      - Event: `@click="toggle"`
    - **Delete-Button** (bedingt)
      - Nur wenn `v-if="removable"` wahr
      - Größe: `small`, Variante: `secondary`
      - Label: Localized String (`t('template.form.delete')`)
      - Event: `@click="emit('remove')"`

### Content (bedingt)
- `.custom-product-collapsible-content`: Container für Slot, nur sichtbar wenn `v-if="expanded"`
  - `<slot />`: Standard-Slot für beliebige Child-Komponenten

## Internationalisierung (i18n)

Die Komponente nutzt `useI18n()` für drei Label-Strings:
- `template.form.collapse` - Button-Text zum Einklappen
- `template.form.expand` - Button-Text zum Ausklappen
- `template.form.delete` - Button-Text zum Löschen

Diese müssen in den i18n-Ressourcen (wahrscheinlich in einem globalen oder lokalen Locale-File) definiert sein.

## Besonderheiten & Fallstricke

1. **Zwei-Wege-Binding**: Das `expanded`-Prop ist "read-only" für die Komponente; sie emittiert nur das Event. Der Parent muss `v-model:expanded="state"` oder `@update:expanded="state = $event"` implementieren.

2. **Keine Default-Expansion für Removable**: Wenn `removable={true}` gesetzt ist, heißt das nicht, dass die Sektion initial expandiert ist. `expanded` bleibt `false` solange nicht explizit gesetzt.

3. **Slot-Sichtbarkeit**: Der Slot wird DOM-weit mit `v-if` nicht gerendert wenn `expanded === false`. Das reduziert DOM-Größe, aber auch Event-Listener in Kind-Komponenten sind inaktiv bis zur Expansion.

4. **CSS-Klassen für Styling**: Alle Elemente haben `.custom-product-collapsible-*`-Präfixe. Das Styling muss separat in einer SCSS/CSS-Datei definiert sein (nicht in der Komponente).

5. **MtButton als Meteor-UI-Komponente**: Die Buttons verwenden Shopware-interne Meteor-Component-Library. Falls diese nicht korrekt installiert oder registriert ist, wird die Komponente nicht rendern.

6. **Fehlende Default-Slot-Fallback**: Wenn kein Slot-Inhalt übergeben wird und `expanded === true`, wird ein leerer `.custom-product-collapsible-content`-div angezeigt (visuell leer aber nicht fehlerhaft).

## Bezüge

- **Parent-Komponente**: Wahrscheinlich in Custom-Product-Formularen (z.B. `CustomProductForm.vue` oder ähnlich) verwendet
- **Globale i18n**: Erwartet `vue-i18n` Setup auf App-Ebene mit Locale-Keys unter `template.form.*`
- **Styling**: Erwartet externe CSS-Datei mit `.custom-product-collapsible*`-Klassen (nicht in dieser Datei definiert)

## Komplexität & Reife

- **Komplexität**: Minimal (stateless, nur Props + Events)
- **Fehleranfälligkeit**: Sehr gering, typische Vue-3-Patterns
- **Testbarkeit**: Hoch (Pure-Komponente, leicht unit-testbar via Props/Events)
