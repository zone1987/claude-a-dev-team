# DurationInput-Komponente (`/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/components/DurationInput.vue`)

## Zweck

Vue 3 Composition-API-Komponente für die Eingabe von Zeitdauern im Ticketing-Kontext (Booking/Tourismus). 
Ermöglicht dem Nutzer, eine numerische Menge (z.B. 2) und eine Zeiteinheit (Minute, Stunde, Tag, Woche) 
separat auszuwählen. Wird verwendet für Stornierungsfristen (cancellationCutoff) und Aktivitätsdauern 
im Custom-Product-Formular des ResubmissionAppServer.

## Typ & Architektur

- **Typ**: Vue 3 Single-File-Component (SFC), `<script setup>` mit Composition API
- **Komponentenname**: `DurationInput` (automatisch vom Import-Pfad abgeleitet)
- **Registrierung**: Wird dynamisch in `custom-product-form.vue` importiert und verwendet
- **Abhängigkeiten**: 
  - Vue 3 `computed()` für reaktive Properties
  - `MtNumberField`, `MtSelect` aus Shopware Meteor Component Library (`@shopware-ag/meteor-component-library`)
  - `vue-i18n` für Übersetzungen (Zeiteinheit-Labels)

## Props (Eingabeparameter)

| Prop | Typ | Default | Beschreibung |
|------|-----|---------|-------------|
| `amount` | `Number \| String` | `null` | Numerische Menge (z.B. 2, 30). Keine Validierung auf Positivität. |
| `unit` | `String` | `null` | Zeiteinheit: `'minute'`, `'hour'`, `'day'`, `'week'`. |
| `amountLabel` | `String` | `''` | Label für das Mengen-Eingabefeld (über Parent via i18n) |
| `unitLabel` | `String` | `''` | Label für das Einheiten-Dropdown (über Parent via i18n) |

## Emits (Ereignisse)

| Event | Payload | Auslöser | Beschreibung |
|-------|---------|----------|-------------|
| `update:amount` | `value: Number \| String` | MtNumberField-Change | Wird emittiert wenn Benutzer die Menge ändert; Parent nutzt `v-model:amount` |
| `update:unit` | `value: String` | MtSelect-Change | Wird emittiert wenn Benutzer die Einheit ändert; Parent nutzt `v-model:unit` |

## Computed Properties

### `localAmount`
- **Getter**: Gibt `props.amount` zurück (Read-through proxy)
- **Setter**: Emittiert `update:amount` mit neuem Wert
- **Zweck**: Umsetzung von `v-model:amount` auf dem Eltern-Element; zweiweg-Bindung via computed Property

### `localUnit`
- **Getter**: Gibt `props.unit` zurück (Read-through proxy)
- **Setter**: Emittiert `update:unit` mit neuem Wert
- **Zweck**: Umsetzung von `v-model:unit` auf dem Eltern-Element; zweiweg-Bindung via computed Property

## Daten & Konstanten

### `timeUnitsOptions`
```javascript
const timeUnitsOptions = [
    { label: t('template.form.timeUnitMinute'), value: 'minute' },
    { label: t('template.form.timeUnitHour'), value: 'hour' },
    { label: t('template.form.timeUnitDays'), value: 'day' },
    { label: t('template.form.timeUnitWeeks'), value: 'week' },
];
```

- Statisches Array von Objekten für das MtSelect-Dropdown
- Labels werden via i18n übersetzt beim Component-Mount
- Values sind String-Konstanten ohne Validierung durch diese Komponente
- Reihenfolge: Minute → Stunde → Tag → Woche (logische Staffelung)

**Hinweis zu i18n-Keys**: 
- `template.form.timeUnitMinute` → z.B. "Minute"
- `template.form.timeUnitHour` → z.B. "Stunde"
- `template.form.timeUnitDays` → z.B. "Tage"
- `template.form.timeUnitWeeks` → z.B. "Wochen"

(Keys sind im ResubmissionAppServer unter `src/translations/` definiert)

## Template-Struktur

```html
<template>
    <div class="custom-product-duration">
        <!-- Wrapper für BEM-Klasse -->
        
        <div class="custom-product-duration-amount">
            <!-- Numerisches Input-Feld -->
            <MtNumberField
                :label="amountLabel"
                v-model="localAmount"
            />
        </div>

        <div class="custom-product-duration-unit">
            <!-- Dropdown für Zeiteinheit -->
            <MtSelect
                :label="unitLabel"
                :options="timeUnitsOptions"
                v-model="localUnit"
            />
        </div>
    </div>
</template>
```

- **CSS-Klassen**: BEM-Konvention (`custom-product-duration*`)
- **MtNumberField**: 
  - Nur numerische Eingabe (über Browser native `type="number"`)
  - Keine Min/Max-Constraints in dieser Komponente
  - Emittiert bei Änderung über `v-model="localAmount"`
- **MtSelect**:
  - Dropdown mit vordefiniertem `timeUnitsOptions`-Array
  - Emittiert bei Änderung über `v-model="localUnit"`
  - Required-Validierung auf Parent-Ebene (nicht hier)

## Verwendung & Aufrufer

**Direkt verwendet in**: 
- `assets/vue/controllers/custom-product/custom-product-form.vue` (3x)

**Kontexte**:
1. **Stornierungsfrist** (Zeile 36–41):
   ```vue
   <DurationInput
       v-model:amount="option.cancellationCutoffAmount"
       v-model:unit="option.cancellationCutoffUnit"
       :amount-label="t('template.form.optionCancellationCutoffAmount')"
       :unit-label="t('template.form.optionCancellationCutoffUnit')"
   />
   ```
   Bindet an `option.cancellationCutoffAmount/Unit` (z.B. "48 Stunden vor Buchung stornierbar")

2. **Aktivitätsdauer** – auf Option-Level (Zeile 43–48):
   ```vue
   <DurationInput
       v-model:amount="option.durationAmount"
       v-model:unit="option.durationUnit"
       :amount-label="t('template.form.optionDurationAmount')"
       :unit-label="t('template.form.optionDurationUnit')"
   />
   ```
   Bindet an `option.durationAmount/Unit` (z.B. "2 Stunden Aktivitätsdauer")

3. **Aktivitätsdauer – auf Saison-Level** (Zeile 79–84):
   ```vue
   <DurationInput
       v-model:amount="season.durationAmount"
       v-model:unit="season.durationUnit"
       :amount-label="t('template.form.optionDurationAmount')"
       :unit-label="t('template.form.optionDurationUnit')"
   />
   ```
   Bindet an `season.durationAmount/Unit` (saisonal unterschiedliche Dauern)

**Form-Struktur** (Parent):
- `form.options[].cancellationCutoffAmount/Unit` → Stornierungsfrist pro Option
- `form.options[].durationAmount/Unit` → Standard-Aktivitätsdauer pro Option
- `form.options[].availabilitySeasons[].durationAmount/Unit` → Saisonale Dauervarianten

## Besonderheiten & Fallstricke

### 1. Keine Validierung auf Komponentenebene
- **Keine Min/Max-Checks**: DurationInput akzeptiert jede Zahl (auch 0, negativ, dezimal).
  Validierung obliegt dem Parent oder dem Server.
- **Keine Unit-Validierung**: Akzeptiert jeden String, prüft nicht gegen `timeUnitsOptions`-Values.

### 2. i18n ist vorausgesetzt
- Component nutzt `useI18n()` via Vue-i18n Plugin.
- Wenn Plugin nicht registriert, wirft Fehler bei Mount.
- Parent muss sicherstellen, dass alle 4 i18n-Keys (`template.form.timeUnitMinute`, `-Hour`, `-Days`, `-Weeks`) 
  in der aktiven Sprache vorhanden sind.

### 3. Null-Handling
- Props defaulten auf `null`; UI zeigt leere Felder.
- Computed Properties geben `null` durch wenn nicht gesetzt.
- Parent verantwortlich für Konvertierung in falsche Typen (z.B. String→Number bei Serialisierung).

### 4. Keine Abhängigkeit zwischen amount und unit
- Komponente ändert nicht automatisch unit wenn amount gesetzt wird (z.B. "zu viele Minuten" → automatisch in Stunden konvertieren).
- Dies ist eine bewusste Entkopplung; Parent kann optional Logik für Konvertierung implementieren.

### 5. Meteor Component Library muss verfügbar sein
- MtNumberField und MtSelect sind externe Dependencies.
- Wenn `@shopware-ag/meteor-component-library` nicht installiert, Build-Fehler.

## I18n-Keys (vom Parent oder Child erwartet)

| Key | Beispiel-Wert (DE) |
|-----|------------------|
| `template.form.timeUnitMinute` | "Minute" |
| `template.form.timeUnitHour` | "Stunde" |
| `template.form.timeUnitDays` | "Tage" |
| `template.form.timeUnitWeeks` | "Wochen" |
| `template.form.optionCancellationCutoffAmount` | "Stornierungsfrist (Menge)" |
| `template.form.optionCancellationCutoffUnit` | "Stornierungsfrist (Einheit)" |
| `template.form.optionDurationAmount` | "Dauer (Menge)" |
| `template.form.optionDurationUnit` | "Dauer (Einheit)" |

(Labels 4–8 werden vom Parent als Props übergeben)

## Verwandte Dateien & Struktur

```
ResubmissionAppServer/
├── assets/vue/controllers/custom-product/
│   ├── components/
│   │   ├── DurationInput.vue ← DIESE DATEI
│   │   ├── DaySelector.vue (ähnliches Pattern, wählt Wochentage)
│   │   ├── StartTimeSelector.vue (wählt Startzeiten)
│   │   ├── CollapsibleSection.vue (Container für Optionen/Saisons)
│   │   └── UnitForm.vue (?)
│   ├── custom-product-form.vue ← HAUPTFORM (importiert DurationInput 3x)
│   ├── add.vue (Routing zu new Form)
│   ├── edit.vue (Routing zu existing Form)
│   └── template-table.vue (Tabellenansicht der Custom Products)
├── src/translations/
│   └── de.json (i18n-Wörterbuch mit timeUnit* Keys)
└── ...
```

## Code-Stil & Moderne Patterns

- **Vue 3 Composition API** (nicht Options API)
- **Reactivity via `computed()`** statt `watch()` (deklarativ, nicht imperativ)
- **v-model:prop** Syntax (Vue 3.4+) für zweiweg-Binding in Child-Props
- **Keine Scoped Slots** oder komplexe generics
- **Einfach & fokussiert**: Eine Komponente = eine Aufgabe (Duration input)

## Test-Umfang (falls vorhanden)

Keine Tests in dieser Repository-Kopie sichtbar. Bei Unit-Tests würden Tests folgende Szenarien abdecken:
- Props werden korrekt gelesen und in computed Properties widergespiegelt
- Emits funktionieren bei Input-Änderung
- i18n-Keys werden korrekt aufgelöst
- `timeUnitsOptions` Array hat alle 4 erwarteten Einheiten

---

**Zusammenfassung**: Leichte, fokussierte Vue 3-Komponente für Zeitdauer-Eingaben im Ticketing-Kontext. 
Keine serverseitige Logik, keine Validierung – nur UI-Binding. Parent trägt Verantwortung für Typkonvertierung, 
Validierung und Serialisierung in API-Requests.
