# DaySelector (Vue 3 Komponent) (/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/components/DaySelector.vue)

## Zweck
Stellt eine UI-Komponente für die Wochentagsauswahl bereit. Die Komponente wird im Custom-Product-Kontext des AppServers verwendet, um Verfügbarkeitsangaben oder Buchungszeiträume auf Wochentags-Basis zu filtern oder zu konfigurieren. Sie ist essenziell für Tourismus-Ticketing-Szenarien (z.B. „diese Tour läuft täglich, außer Montags"), wo Geschäftsregeln tagespezifische Einschränkungen definieren.

## Typ & Struktur
- **Framework**: Vue 3 mit `<script setup>` Syntax
- **Registrierung**: Importiert als Komponente in Parent-Komponenten des Custom-Product-Controllers
- **Dependencies**:
  - `MtCheckbox` (Shopware Meteor Component Library) – Checkbox-Komponente mit Shopware-Design
  - `vue@3.x` (computed, defineProps, defineEmits)
  - `vue-i18n@9.x` (useI18n Hook für Mehrsprachigkeit)

## Props
| Name | Typ | Erforderlich | Default | Bedeutung |
|------|-----|--------------|---------|-----------|
| `modelValue` | `Object` | Ja | — | Zwei-Wege-Bindung mit Parent. Erwartet Objekt mit Keys `'monday'` bis `'sunday'`, Werte sind `boolean`. z.B. `{ monday: true, tuesday: false, ... }` |

## Emits
| Event | Payload | Zweck |
|-------|---------|-------|
| `update:modelValue` | `Object` | Vue 3 Standard-Event für `v-model`-Update. Parent wird benachrichtigt, wenn Benutzer Checkboxen ändert. |

## Konstanten
**weekdays** (Array, lokal, Zeile 33–41):
```javascript
[
    {label: t('template.form.weekday.monday'), value: 'monday'},
    {label: t('template.form.weekday.tuesday'), value: 'tuesday'},
    {label: t('template.form.weekday.wednesday'), value: 'wednesday'},
    {label: t('template.form.weekday.thursday'), value: 'thursday'},
    {label: t('template.form.weekday.friday'), value: 'friday'},
    {label: t('template.form.weekday.saturday'), value: 'saturday'},
    {label: t('template.form.weekday.sunday'), value: 'sunday'},
]
```
- Startkonstante für die Wochentags-Liste (Montag bis Sonntag)
- `label`: Übersetzter Text aus i18n-Keys `template.form.weekday.*` (z.B. „Montag", „Monday" je nach Locale)
- `value`: Englischer Bezeichner, dient als Key im `modelValue`-Objekt
- Wird **nicht reaktiv** aktualisiert nach Locale-Wechsel (Fallstrick! siehe unten)

## Computed Properties
**localValue** (Zeile 43–46):
- **Getter**: Rückgabe von `props.modelValue` (Read-Through)
- **Setter**: Emittiert `update:modelValue`-Event mit neuer Value
- **Zweck**: Ermöglicht `v-model`-Syntax auf `modelValue` in Parent-Templates
- **Nutzung**: Nicht explizit im Template verwendet, da v-bind direkt auf `modelValue` erfolgt; ist aber Standard-Pattern für Custom Components mit `v-model`

## Template-Struktur
```html
<div class="custom-product-daySelector">
    <span>{{ t('template.form.weekdays') }}</span>
    
    <div class="custom-product-daySelector-list">
        <MtCheckbox
            v-for="weekday in weekdays"
            :key="weekday.value"
            v-model="modelValue[weekday.value]"
            :label="weekday.label"
        />
    </div>
</div>
```

- **Outer Div** (`custom-product-daySelector`): Styling-Container
- **Span**: Übersetzt Label „Wochentage" (i18n-Key: `template.form.weekdays`)
- **Inner Div** (`custom-product-daySelector-list`): Layout-Container für Checkbox-Liste
- **v-for Loop**: Erzeugt 7 Checkboxen (eine pro Wochentag)
  - `:key="weekday.value"`: Eindeutige ID (z.B. `'monday'`, `'tuesday'`)
  - `v-model="modelValue[weekday.value]"`: Zwei-Wege-Bindung zu Parent-Objekt (z.B. `modelValue.monday`)
  - `:label="weekday.label"`: Übersetzter Wochentagsname
- **MtCheckbox**: Shopware-Standard-Checkbox mit Built-in-Validation, Accessibility, Styling

## Abhängigkeiten & Imports
1. **MtCheckbox** aus `@shopware-ag/meteor-component-library`
   - Shopware Admin-UI Komponente
   - Nutzt internes Design-System
2. **computed** aus `'vue'`
   - Vue 3 Reactivity API
3. **useI18n** aus `'vue-i18n'`
   - Internationale Übersetzungen
   - Gibt `t(key)`-Funktion zurück

## Seiteneffekte & Lifecycle
- **Keine Seiteneffekte**: Komponente ist pure presentational (UI-only)
- **Keine HTTP-Calls, DB-Zugriffe, Events, Logging**
- **Keine Lifecycle-Hooks**: Keine mounted/unmounted/watch
- **i18n-Fallstrick**: `weekdays`-Array wird **einmalig** beim Component-Setup berechnet; Locale-Wechsel zur Laufzeit aktualisiert Labels **nicht** (da weekdays nicht reaktiv ist). Wenn Parent die Locale ändert, muss Parent auch Neurender triggern oder Komponente re-mounten.

## Besonderheiten & Fallstricke

### 1. **Reaktivitätsproblem bei Locale-Wechsel**
Die `weekdays`-Konstante wird einmalig beim Setup berechnet. Wenn die Shopware Admin-UI die Sprache wechselt (z.B. von de-DE zu en-US), werden die `weekday.label`-Werte **nicht** aktualisiert, da sie nicht in einer `ref()` oder `computed()` sind. 
- **Symptom**: Nach Locale-Wechsel zeigen Checkboxen alte Labels
- **Lösung**: `weekdays` als `computed` umschreiben:
  ```javascript
  const weekdays = computed(() => [
    {label: t('template.form.weekday.monday'), value: 'monday'},
    // ... rest
  ]);
  ```

### 2. **modelValue-Objekt muss korrekte Keys haben**
Parent muss `modelValue` als Objekt mit exakt den Keys `'monday'` bis `'sunday'` übergeben, und zwar **alle 7**, auch wenn nur ein Subset relevant ist. Fehlende Keys → undefined → Checkbox-State ist unbestimmt.
- **Symptom**: Checkbox springt nach Click zurück in Aus-Position
- **Lösung**: Parent initialisiert `modelValue` vollständig:
  ```javascript
  {
    monday: false,
    tuesday: false,
    // ... alle 7 Wochentage
    sunday: false
  }
  ```

### 3. **Keine initiale Validierung**
Die Komponente validiert **nicht**, ob `modelValue` ein Objekt ist. Wenn Parent versehentlich `null`, `undefined`, oder String übergibt, stürzt v-model ab.
- **Fallstrick**: Props-Default ist nicht definiert, da `required: true`; aber bei Props-Validierungsfehler wird Konsolen-Warning geloggt, aber Component rendern versucht

### 4. **Keine indirekte Parent-Benachrichtigung**
Änderung einer einzelnen Checkbox emittiert das gesamte `modelValue`-Objekt (mit allen 7 Keys), nicht nur geänderten Key. Parent-Watchers reagieren auf das ganze Objekt.

## Integrationspunkte & Aufrufer
- **Parent-Komponente**: Vermutlich `CustomProductForm` oder ähnlich im Custom-Product-Controller
- **Nutzung**: 
  ```vue
  <DaySelector v-model="productFormData.availableDays" />
  ```
- **Cross-Component-Vertrag**: Parent muss `productFormData.availableDays` als persistenter reaktiver State führen und bei Save/Submit an Backend senden (z.B. in `custom_product_days`-Tabelle oder JSON im `custom_fields`)

## i18n-Keys (Abhängigkeiten)
Diese Keys **müssen** in Shopware-Locale-Dateien definiert sein:
- `template.form.weekdays` – Überschrift/Label (z.B. „Wochentage")
- `template.form.weekday.monday` – Montag
- `template.form.weekday.tuesday` – Dienstag
- `template.form.weekday.wednesday` – Mittwoch
- `template.form.weekday.thursday` – Donnerstag
- `template.form.weekday.friday` – Freitag
- `template.form.weekday.saturday` – Samstag
- `template.form.weekday.sunday` – Sonntag

Wenn Keys fehlen, zeigen Checkboxen leere Labels (fallback zu Key-String selbst in vue-i18n).

## CSS-Klassen
- `.custom-product-daySelector` – Outer Container (keine Inline-Styles, nur Klasse)
- `.custom-product-daySelector-list` – List Container (Flexbox o.ä. für Checkbox-Layout)

Styles müssen extern (wahrscheinlich in `assets/css/controllers/custom-product.css` oder `.scss`) definiert sein; in dieser Komponente keine `<style>`-Sektion.

## Technische Schulden & Verbesserungen
1. **weekdays sollte computed sein** (siehe Fallstrick 1)
2. **Props-Validierung** sollte hinzugefügt werden:
   ```javascript
   const props = defineProps({
     modelValue: {
       type: Object,
       required: true,
       validator: (value) => {
         const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
         return days.every(day => day in value && typeof value[day] === 'boolean');
       }
     }
   });
   ```
3. **KeyError-Handling**: Falls `modelValue` fehlende Keys hat, sollte Default-Value (false) verwendet werden:
   ```javascript
   :v-model="modelValue[weekday.value] ?? false"
   ```

## Verwandte Dateien (relativ zum AppServer)
- `assets/vue/controllers/custom-product/index.js` – Komponenten-Registrierung
- `assets/vue/controllers/custom-product/*.vue` – Parent-Komponenten (CustomProductForm, etc.)
- `assets/css/controllers/custom-product.css` o.ä. – Styling für `.custom-product-daySelector`
- `src/Entity/CustomProduct.php` o.ä. – Backend-Entity mit `days` oder `availableDays` Property

## Deployment-Kontext (FfOctoApi Ökosystem)
Diese Komponente ist Teil des **Resubmission AppServer** (Tourismus-Ticketing), nicht des Shopware-6.7-Plugins selbst. Sie wird für die Admin-UI des Custom-Product-Verwaltungs-Bereichs genutzt, um Verfügbarkeitsregeln auf Wochentags-Basis zu definieren. Die Daten werden über das FfOctoApi-Backend (Ventrata OCTO) mit Shopware-Produkten synchronisiert.

