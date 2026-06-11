# StartTimeSelector (Vue 3 SFC)

**Pfad:** `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/components/StartTimeSelector.vue`

**Kategorie:** AppServer › Vue UI-Komponente (Custom-Product-Wizard)

---

## Zweck

Vue 3 Single File Component (SFC) zur Verwaltung von lokalen Startuhrzeit(en) im Custom-Product-Wizard (Tourismus-Ticketing / OCTO API Ventrata). Ermöglicht das Hinzufügen, Entfernen und sortierte Anzeige von Zeitangaben im Format `HH:MM`. Wird zweifach in der Eltern-Komponente `custom-product-form.vue` eingebunden:
1. Auf Options-Ebene: `option.availabilityLocalStartTimes`
2. Im Availability-Seasons-Detail: `season.startTimes`

---

## Typ & Struktur

- **Framework:** Vue 3 Composition API (`<script setup>`)
- **Registrierung:** Dynamische Import in `custom-product-form.vue` (Zeilen 191)
- **Component-Typ:** Presentational Component mit State-Management via `v-model` (2-way binding via `modelValue` + `update:modelValue`)
- **Template-Root-Element:** `<div class="custom-product-form-time">`

---

## Props

| Name | Typ | Default | Bedeutung |
|------|-----|---------|-----------|
| `modelValue` | `Array<string>` | `[]` | Array von Zeit-Strings im Format `"HH:MM"` (z.B. `["09:00", "14:30", "18:00"]`) |

---

## Events / Emit

| Name | Payload | Bedeutung |
|------|---------|-----------|
| `update:modelValue` | `Array<string>` | Emitted bei Änderung des Time-Arrays (add/remove) — treibt 2-way binding v-model |

---

## Reactive State

### Refs
- **`newTime`** (Type: `Ref<null | Date | string>`): Zwischenspeicher für die vom MtDatepicker-Component komende Zeiteingabe; wird nach erfolgreicher Ergänzung auf `null` zurückgesetzt.

### Computed Properties
- **`localValue`** (Type: `ComputedRef<Array<string>>`): Computed mit Getter/Setter:
  - **Getter:** Gibt `props.modelValue` unverändert zurück
  - **Setter:** Emittet `update:modelValue` mit dem neuen Wert — ermöglicht `v-model`-Semantik
  
- **`sortedTimes`** (Type: `ComputedRef<Array<string>>`): Gibt eine SORTIERTE Kopie von `localValue.value` zurück, sortiert numerisch nach Minuten seit Mitternacht:
  - Parse jedes Zeit-Strings `"HH:MM"` → `hours, minutes`
  - Numerischer Sort nach `hours * 60 + minutes`
  - Beispiel: `["18:00", "09:00", "14:30"]` wird zu `["09:00", "14:30", "18:00"]`

---

## Methoden

### `removeTime(timeIndex: number): void`
**Zweck:** Entfernt eine Zeit an Index `timeIndex` aus dem Array.

**Algorithmus:**
1. Erstelle Kopie von `localValue.value` (Spread: `[...localValue.value]`)
2. Splice: `updated.splice(timeIndex, 1)`
3. Setze `localValue.value = updated` (emittet `update:modelValue`)

**Seiteneffekte:** Emittet `update:modelValue` mit neuem Array.

**Aufrufer:** Template: Button mit `@click="removeTime(timeIndex)"` (Zeile 19).

---

### `addTime(): void`
**Zweck:** Fügt eine neue Zeit hinzu, wenn validierbar und nicht duplikat.

**Algorithmus:**
1. Guard: Wenn `!newTime.value` vorhanden → return ohne Aktion
2. Formatiere `newTime.value` via `formatTimeValue()` → `timeValue` (String `"HH:MM"`)
3. Guard: Wenn `timeValue` bereits in `localValue.value` vorhanden (`.includes()`) → return ohne Aktion (Duplikat-Schutz)
4. Spread-Add: `localValue.value = [...localValue.value, timeValue]`
5. Reset: `newTime.value = null` (Eingabefeld leeren)

**Seiteneffekte:** Emittet `update:modelValue` mit erweitertem Array.

**Aufrufer:** Template: Button `@click="addTime"` (Zeile 41).

---

### `formatTimeValue(value: Date | string): string`
**Zweck:** Normalisiert eine Zeit-Eingabe (Date-Objekt oder String) zu ISO-Format `"HH:MM"`.

**Algorithmus:**
- Wenn `value instanceof Date`:
  - Hole `hours = value.getHours()`, `minutes = value.getMinutes()`
  - Pad mit `padStart(2, '0')` → `"HH:MM"`
  - Return formatierter String
- Sonst: Return `value` unverändert (falls schon String)

**Rückgabe:** String im Format `"HH:MM"` (z.B. `"09:00"`, `"14:30"`).

**Aufrufer:** `addTime()` (Zeile 93).

**Besonderheit:** MtDatepicker mit `dateType="time"` gibt `Date`-Objekt zurück; Konversion nötig.

---

## Template-Struktur

### Hauptbereiche

#### 1. **Time-List-Anzeige** (Zeilen 2–28)
```html
<div class="custom-product-form-time">
  <div class="custom-product-time-list">
    <span>{{ t('template.form.localTimeHeader') }}</span>
    
    <!-- Sortierte Zeitenliste -->
    <div v-for="(time, timeIndex) in sortedTimes" :key="timeIndex">
      <span>{{ time }}</span>
      <MtButton @click="removeTime(timeIndex)">
        {{ t('template.form.delete') }}
      </MtButton>
    </div>
    
    <!-- Fallback wenn leer -->
    <div v-if="!localValue || localValue.length === 0">
      {{ t('template.form.noTimesDefined') || '-' }}
    </div>
  </div>
```

**Logik:**
- Iteriert über `sortedTimes` (automatisch sortiert)
- `:key="timeIndex"` (Index-basiert) — **Warnung:** Nicht ideal bei dynamischen Listen, aber akzeptabel da einfach numerisch
- Zeigt jeweils Zeit-String und Delete-Button (variant="secondary")
- Fallback-Text wenn Array leer

#### 2. **Input & Add-Button** (Zeilen 30–45)
```html
<div class="custom-product-time-add">
  <MtDatepicker
    v-model="newTime"
    dateType="time"
    placeholder="HH:MM"
    :textInput="true"
  />
  
  <MtButton type="button" variant="secondary" @click="addTime">
    {{ t('template.form.addTime') }}
  </MtButton>
</div>
```

**Verhalten:**
- MtDatepicker mit `dateType="time"` akzeptiert Zeit-Eingaben (HH:MM)
- `v-model="newTime"` bindet an Ref-State
- `:textInput="true"` ermöglicht manuelle Eingabe ohne Kalender-UI
- Add-Button triggert `addTime()` mit Validierung + Duplikat-Schutz

---

## Internationalisierung (i18n)

Die Komponente verwendet `useI18n()` (vue-i18n) für alle Textlabel:

| Key | Kontext |
|-----|---------|
| `template.form.localTimeHeader` | Überschrift der Zeit-Liste |
| `template.form.delete` | Delete-Button-Label |
| `template.form.addTime` | Add-Button-Label |
| `template.form.noTimesDefined` | Fallback-Text wenn leer |

Keine Hardcoded-Texte in der Komponente; alle sind parametrisiert.

---

## Abhängigkeiten & Imports

| Import | Quelle | Verwendung |
|--------|--------|-----------|
| `ref`, `computed` | `vue` (v3) | Reaktive State-Management |
| `MtButton` | `@shopware-ag/meteor-component-library` | Delete- & Add-Buttons |
| `MtDatepicker` | `@shopware-ag/meteor-component-library` | Zeit-Eingabe-Feld |
| `useI18n` | `vue-i18n` | Lokalisierung |

---

## Eltern-Komponente & Kontext

**Einbindung in** `/assets/vue/controllers/custom-product/custom-product-form.vue`:

1. **Import (Zeile 191):**
   ```javascript
   import StartTimeSelector from "./components/StartTimeSelector.vue";
   ```

2. **Verwendungen:**
   - **Zeile 50–52:** Option-Ebene
     ```vue
     <StartTimeSelector
       v-model="option.availabilityLocalStartTimes"
     />
     ```
   - **Zeile 85–87:** Season-Detailansicht (innerhalb nested Seasons-Loop)
     ```vue
     <StartTimeSelector
       v-model="season.startTimes"
     />
     ```

**Daten-Flow:**
- Eltern-Komponente managed Formular-State (reactive `form`-Objekt)
- StartTimeSelector ist ein **dumb/presentational** Component
- 2-way Binding via `v-model` synchronisiert Changes automatisch in Eltern-State
- Beim Submit (`submitAdd()` / `submitEdit()`) werden Arrays aus `form.options[i].availabilityLocalStartTimes` und `form.options[i].availabilitySeasons[j].startTimes` in JSON serialisiert

---

## Fallstricke & Besonderheiten

### 1. **MtDatepicker Time-Format**
- MtDatepicker mit `dateType="time"` gibt ein `Date`-Objekt zurück (lokale Mittags-Stunde + Minute)
- `formatTimeValue()` konvertiert via `getHours()` / `getMinutes()` → padded `"HH:MM"`
- **Falle:** Keine Typen-Prüfung; wenn Dateikonvention bricht, kann String reingeholt werden → fallback auf Identität

### 2. **Duplikat-Schutz**
- `addTime()` prüft via `.includes(timeValue)` vor dem Push
- **Effekt:** Identische Zeiten können nicht doppelt eingegeben werden
- **Edge-Case:** "09:00" und "09:00:00" würden als unterschiedlich behandelt (String-Gleichheit)

### 3. **Sortierung in sortedTimes**
- **Keine Mutation** des Original-Arrays: `[...localValue.value].sort(...)`
- **Numerische Sortierung:** `aH * 60 + aM` (Minuten seit Mitternacht)
- **Reihenfolge:** Aufsteigend (morgens → abends)
- **Rendering-Effekt:** Unabhängig von Eingabe-Reihenfolge immer sortiert angezeigt

### 4. **Index-basierte Keys**
```vue
<div v-for="(time, timeIndex) in sortedTimes" :key="timeIndex">
```
- `:key="timeIndex"` ist **Index-basiert**
- **Problem:** Bei Remove/Reorder können Komponenten-States verlorengehen
- **Hier aber akzeptabel:** StartTimeSelector ist stateless, nur visuelle Anzeige
- **Besser wäre:** `:key="time"` (Zeit-String als Identifier)

### 5. **Array-Formatierung für Submit**
- Beim Speichern erwartet Backend Array von Strings: `["09:00", "14:30", ...]`
- Die sortierte Anzeige ändert nicht die tatsächliche Reihenfolge im state
- **Vorsicht:** `sortedTimes` ist Computed für UI; Speicherung erfolgt mit Original-Array-Reihenfolge (aber nach Add vom User sortiert eingegeben)

### 6. **Keine Validierung auf Grenzen**
- Keine Prüfung auf minimale/maximale Anzahl Zeiten
- Keine Prüfung auf zirkuläre oder ungültige Zeitbereiche
- Delegation auf Backend oder Parent-Komponente

---

## CSS-Klassen (BEM-konvention)

```
.custom-product-form-time
├── .custom-product-time-list
│   ├── .custom-product-time-item
│   │   ├── .custom-product-time-label
│   │   └── (Button: MtButton)
│   └── (Fallback: "keine Zeiten")
└── .custom-product-time-add
    ├── (MtDatepicker)
    └── (MtButton)
```

Keine inline-Styles; reine class-basierte Styling (SCSS extern).

---

## Performance & Reaktivität

- **Computed Properties:** `sortedTimes` wird nur neu berechnet bei Änderung von `localValue`
- **No Deep Watchers:** Keine expliziten Watchers; Vue verwaltet Dependencies automatisch
- **Vermiedene Probleme:**
  - Keine Filter/Map mit Side-Effects
  - Keine DOM-Mutation via Refs (nur via reaktive Daten)
  - Keine Circular-Watchers

---

## Testing-Hinweise (falls Unit-Test nötig)

**Zu testende Szenarien:**
1. `removeTime(0)` → entfernt exakte Index-Position
2. `addTime()` mit gültiger Zeit → emittet `update:modelValue` mit neuem Array
3. `addTime()` mit Duplikat → no emit, silent ignore
4. `addTime()` mit `null` newTime → no emit
5. `sortedTimes` Computed → Korrekte numerische Sortierung (09:00, 14:30, 18:00)
6. `formatTimeValue(Date)` → Korrekte `"HH:MM"`-Formatierung
7. `formatTimeValue(string)` → Passthrough unverändert

---

## Bezüge & Verwandte Dateien

**Im selben Ordner:**
- `DaySelector.vue` — Wochentag-Selector (ähnliches Muster: v-model, Array-Handling)
- `DurationInput.vue` — Multi-Props Input (amount + unit)
- `CollapsibleSection.vue` — Accordion-Wrapper
- `UnitForm.vue` — Komplexer Unit-Editor

**Eltern-Komponente:**
- `custom-product-form.vue` — Master-Formular (Context: Optionen, Saisonen, Units)

**Backend-Integration:**
- POST `/customProductTemplate/add` + `/customProductTemplate/edit` (via ElternSubmit)
- Array `availabilityLocalStartTimes[]` + `season.startTimes[]` werden JSON-serialisiert

**OCTO API Kontext:**
- Ventrata Ticketing System (Tourism)
- Availability-Management: Wochentage + Saisonen + Zeiten-Slots
- Custom-Product-Wizard für Shop-spezifische Ticketoptionen

---

## Changelog & Versionierung

- **Keine Versionsinformation** in der Datei selbst
- **Repository:** ResubmissionAppServer (Shopware 6.7 + OCTO Ventrata Integration)
- **Stabilität:** Production-ready (2-way v-model, i18n, MtComponent-Usage)

---

**Dokumentiert:** 2026-06-11
