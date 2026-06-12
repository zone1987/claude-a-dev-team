# UnitForm.vue (/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/components/UnitForm.vue)

## Zweck

Einzelne Preisstufe (Unit) für eine Ticketart im Custom-Product-Editor des AppServers. Komponente wird vom Ventrata OCTO API verwendet, um Altersgruppen, Mengenrestriktionen und Preismodelle (Original/Retail/Netto) pro Tickettyp (ADULT, CHILD, SENIOR, FAMILY, etc.) zu verwalten. Jede Unit repräsentiert eine abrechenbare Kategorie mit eigenen Restriktionen und Preisen in einer definierten Währung.

## Typ & Vererbung

- **Typ**: Vue 3 Single-File Component (SFC)
- **Framework**: Vue 3 + `script setup` (Composition API)
- **UI-Bibliothek**: Shopware Meteor Component Library (MtSelect, MtNumberField)
- **Internationalisierung**: vue-i18n (`useI18n()`)
- **Kinder-Komponente**: Importiert `CollapsibleSection.vue` (kollabierbare Sektion mit Entfernen-Button)

## Props (Input)

| Prop | Typ | Standard | Bedeutung |
|------|-----|---------|-----------|
| `modelValue` | `Object` | erforderlich | Die Unit-Daten (type, restrictions, pricingFrom mit Währung) |
| `expanded` | `Boolean` | `false` | Steuert, ob die Sektion anfangs ausgeklappt ist |
| `currencyOptions` | `Array` | `[]` | Verfügbare Währungen als `[{label, value}, ...]` |

## Emits (Events)

| Event | Payload | Zweck |
|-------|---------|-------|
| `update:modelValue` | `value` | v-model-Update der Unit-Daten (when user modifies fields) |
| `update:expanded` | `boolean` | Parent antwortet auf Expansion/Collapse der Sektion |
| `remove` | - | Unit aus der Liste entfernen (gelöscht werden) |

## Computed Properties

### `unitTypeOptions`
- **Typ**: `Array<{label: string, value: string}>`
- **Wert**: Statische Liste der 9 Tickettypen:
  - ADULT (Erwachsener)
  - YOUTH (Jugendlicher)
  - CHILD (Kind)
  - INFANT (Säugling)
  - FAMILY (Familie/Kombi)
  - SENIOR (Senior)
  - STUDENT (Student)
  - MILITARY (Militär)
  - OTHER (Sonstiges)
- **Labels**: aus i18n-Schlüsseln `template.form.unitType.<TYPE>`
- **Zweck**: Dropdown-Optionen für Unit-Typ-Wahl

### `localValue` (Two-way Computed)
- **Getter**: Gibt `props.modelValue` zurück
- **Setter**: Emitted `update:modelValue` mit neuem Wert
- **Zweck**: Ermöglicht v-model-binding auf Parent-Komponente (zwei-Wege-Datenbindung)

### `unitTitle`
- **Typ**: `String`
- **Logik**: 
  - Wenn `localValue.value?.type` nicht gesetzt → leerer String
  - Sonst: Übersetzter Name des Typs aus `template.form.unitType.<TYPE>`
- **Zweck**: Titel der CollapsibleSection wird mit gewähltem Tickettyp angezeigt

## Template-Struktur

### Äußere Wrapper
- `<div class="custom-product-unit">` — Container mit Styling

### CollapsibleSection
- **Props**:
  - `:title="unitTitle"` — zeigt Unit-Typ an (z.B. "ADULT")
  - `:expanded="expanded"` — Kontrolle vom Parent (v-bind)
  - `:removable="true"` — Sektion kann gelöscht werden
- **Events**:
  - `@update:expanded` → durchgereiht an Parent
  - `@remove` → durchgereiht an Parent

### Inhalts-Felder (Three Sections)

#### 1. Unit-Typ-Auswahl
```vue
<MtSelect
  :label="t('template.form.unitType.label')"
  :options="unitTypeOptions"
  v-model="localValue.type"
/>
```
- Dropdown mit 9 Tickettypen
- v-model-gebunden an `localValue.type` (→ emitted as `update:modelValue`)

#### 2. Restriktions-Felder (`.custom-product-unit-restrictions`)
```vue
<MtNumberField :label="..." v-model="localValue.restrictions.minAge" />
<MtNumberField :label="..." v-model="localValue.restrictions.maxAge" />
<MtNumberField :label="..." v-model="localValue.restrictions.minQuantity" />
```
- **minAge**: Minimales Alter für diese Unit (z.B. Kinder < 18)
- **maxAge**: Maximales Alter (z.B. Senioren >= 60)
- **minQuantity**: Mindestmenge beim Kauf (z.B. mindestens 2 Stück)
- Alle sind Number-Inputs mit v-model
- I18n-Labels: `template.form.unit{MinAge|MaxAge|MinQuantity}`

#### 3. Preis-Felder (`.custom-product-unit-price`)
```vue
<MtNumberField :label="..." v-model="localValue.pricingFrom.original" />
<MtNumberField :label="..." v-model="localValue.pricingFrom.retail" />
<MtNumberField :label="..." v-model="localValue.pricingFrom.net" />
<MtSelect :label="..." :options="currencyOptions" v-model="localValue.pricingFrom.currency" />
```
- **original**: Katalog-/Originalpreis (z.B. 25,00)
- **retail**: Verkaufspreis für End-Kunden (z.B. 23,50)
- **net**: Netto-Betrag für Rechnungslegung (z.B. 19,75 bei 19% MwSt)
- **currency**: Währungs-Code (EUR, GBP, USD etc.) aus Parent-bereitgestellten Optionen
- **FALLSTRICK**: "0,00 EUR nie ok" — Preisvalidation müsste auf Parent-Ebene erfolgen

## Daten-Struktur (modelValue)

```typescript
{
  id?: string,  // Optional, wird von Parent generiert
  type: 'ADULT' | 'YOUTH' | 'CHILD' | 'INFANT' | 'FAMILY' | 'SENIOR' | 'STUDENT' | 'MILITARY' | 'OTHER',
  restrictions: {
    minAge?: number,
    maxAge?: number,
    minQuantity?: number,
  },
  pricingFrom: {
    original: number,      // EUR etc.
    retail: number,
    net: number,
    currency: string,      // z.B. "EUR", "GBP"
  },
}
```

## I18n-Schlüssel (Template)

| Schlüssel | Kontext |
|-----------|---------|
| `template.form.unitType.label` | Label für Typ-Dropdown |
| `template.form.unitType.ADULT` | Label für "ADULT" |
| `template.form.unitType.YOUTH` | Label für "YOUTH" |
| `template.form.unitType.CHILD` | Label für "CHILD" |
| `template.form.unitType.INFANT` | Label für "INFANT" |
| `template.form.unitType.FAMILY` | Label für "FAMILY" |
| `template.form.unitType.SENIOR` | Label für "SENIOR" |
| `template.form.unitType.STUDENT` | Label für "STUDENT" |
| `template.form.unitType.MILITARY` | Label für "MILITARY" |
| `template.form.unitType.OTHER` | Label für "OTHER" |
| `template.form.unitMinAge` | Label für Altersminimum |
| `template.form.unitMaxAge` | Label für Altersmaximum |
| `template.form.unitMinQuantity` | Label für Mindestmenge |
| `template.form.unitPriceOriginal` | Label für Original-Preis |
| `template.form.unitPriceRetail` | Label für Verkaufspreis |
| `template.form.unitPriceNet` | Label für Netto-Preis |
| `template.form.unitCurrency` | Label für Währungs-Dropdown |

## Abhängigkeiten & Importe

```javascript
import { computed } from 'vue';
import { MtNumberField, MtSelect } from "@shopware-ag/meteor-component-library";
import { useI18n } from "vue-i18n";
import CollapsibleSection from "./CollapsibleSection.vue";
```

- **Vue 3 Composition API**: `computed()` für Reactive Properties
- **Meteor Component Library**: Shopware-Standard UI Components (Inputs, Dropdowns)
- **vue-i18n**: Internationalisierung (Mehrsprachigkeit)
- **Lokale Abhängigkeit**: `./CollapsibleSection.vue` (kollabierbare Sektion)

## Aufrufer

- **Parent**: `custom-product-form.vue` (Z. 128–136)
  ```vue
  <UnitForm
    v-for="(unit, unitIndex) in option.units"
    :key="unit.id ?? unitIndex"
    v-model="option.units[unitIndex]"
    :expanded="expandedUnitIndex[optionIndex] === unitIndex"
    :currency-options="currencyOptions"
    @update:expanded="toggleUnit(optionIndex, unitIndex)"
    @remove="removeUnit(optionIndex, unitIndex)"
  />
  ```
  - Wird in Schleife über `option.units` Array erzeugt
  - Parent stellt `currencyOptions` bereit
  - Parent antwortet auf Expand/Remove Events

## Besonderheiten & Fallstricke

1. **Two-way Binding über v-model**
   - UnitForm arbeitet mit lokalem Computed Property, das direkt auf Parent-Array zurückschreibt
   - Parent muss Array-Mutation korrekt handhaben (`option.units[unitIndex] = ...`)
   - Keine explizite Validierung in der Komponente!

2. **Statische Unit-Typ-Liste**
   - 9 vordefinierte Tickettypen (ADULT, CHILD, SENIOR, FAMILY, STUDENT, MILITARY, YOUTH, INFANT, OTHER)
   - Keine dynamische Erweiterung oder Custom-Typen möglich
   - Hard-coded in UnitForm, nicht konfigurierbar

3. **Preis in Dezimalform (Number)**
   - Felder sind `MtNumberField` (JavaScript `number` typ)
   - Keine explizite EUR-Formatierung (z.B. "€ 25,00")
   - Dezimaltrennzeichen hängt vom Locale/Browser ab
   - **FALLSTRICK**: "0,00 EUR nie ok" — keine min-value Validierung auf Komponenten-Ebene!

4. **Währungs-Optionen vom Parent**
   - `currencyOptions` muss Parent bereitstellen
   - Komponente macht keine API-Call zur Währungs-Liste
   - Format: `Array<{label: string, value: string}>` (z.B. `[{label: "EUR", value: "EUR"}, ...]`)

5. **Titel wird dynamisch aus Type berechnet**
   - `unitTitle` zeigt "ADULT", "CHILD" etc. (übersetzt) in der Sektion-Kopfzeile
   - Leerer String, wenn `type` nicht gesetzt → unbenannte Unit bis Typ gewählt

6. **Keine Seiteneffekte**
   - Keine API-Calls, keine Logging, keine Session-Änderungen
   - Reines Daten-Input/Output Component
   - Alle Events nach oben propagiert; Parent ist verantwortlich für Persistierung

7. **Fehlende Validierung**
   - minAge < maxAge Konsistenz wird nicht überprüft
   - Preis-Konsistenz (original >= retail >= net) wird nicht validiert
   - Currency-Format wird nicht überprüft
   - Parent muss alle Validierungen durchführen

## Verwandte Dateien (relativ)

- `../custom-product-form.vue` — Parent-Komponente, orchestriert Units pro Option
- `./CollapsibleSection.vue` — UI-Wrapper für kollabierbare Sektion
- `../../../shared/*` — Mögliche gemeinsame Utilities (nicht vorhanden in diesem Repo-Scan)
- `../../../../public/build/app.*.js` — Bundled Output (UnitForm ist enthalten)

## CSS-Klassen

- `.custom-product-unit` — Outermost Div
- `.custom-product-unit-field` — Single Input/Select Field (div Wrapper)
- `.custom-product-unit-restrictions` — Alters-/Mengen-Sektion
- `.custom-product-unit-price` — Preis-Sektion

## Zusammenfassung

UnitForm ist eine **einfache, präsentations-fokussierte** Komponente für die Editierung einer einzelnen Ticketpreis-Stufe im OCTO-API Custom-Product-Editor. Sie delegiert alle Geschäftslogik (Validierung, Persistierung, Regelwerk) an die Parent-Komponente `custom-product-form.vue`. Das Daten-Modell ist flach und direkt an Vue-Binding gebunden, was schnelle Änderungen ermöglicht, aber minimale Fehlerbehandlung auf Komponenten-Ebene bedeutet.
