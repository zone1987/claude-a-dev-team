# CustomProductEdit-Komponente (/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/edit.vue)

## Zweck

Vue 3 Single-File-Komponente für die Bearbeitung existierender Tourismus-Ticketing-Produkttemplates im ResubmissionAppServer. Sie dient als Wrapper/Einstiegspunkt, der den Bearbeitungsmodus in die universelle `CustomProductForm`-Komponente delegiert und die notwendigen Template-Daten (ID, komplettes OCTO-Produkt, Name) vom Backend bereitstellt.

## Typ & Vererbung

- **Vue 3 Composition API SFC** (Single-File Component)
- **Komponenten-Typ**: View Controller / Page Component
- **Template-Root**: `<CustomProductForm>` (child component)
- **Sprache**: JavaScript/TypeScript (keine explizite `.ts` Extension, aber mit `<script setup>`)

## Props

| Name | Typ | Default | Bedeutung |
|------|-----|---------|-----------|
| `urlParams` | `String` | `undefined` | Serialisierte URL-Parameter vom Backend (z.B. `?salesChannelId=...&locale=...`). Werden weitergegeben an `CustomProductForm` und dort verwendet für API-Calls und Links. |
| `templateId` | `String` | `undefined` | Eindeutige ID des zu bearbeitenden Produkttemplates. Wird in `CustomProductForm` bei `submitEdit()` genutzt. |
| `template` | `Object` | `undefined` | Komplettes Template-Objekt vom Backend mit Struktur: `{ id, name, octoProduct: { id, uuid, product: { options: [...] } } }`. Wird in `CustomProductForm` deserialisiert und reaktiv in das Formular-Modell konvertiert. |

## Render-Logik

```
<CustomProductForm
    :urlParams="urlParams"
    mode="edit"           <!-- Wichtig: setzt submitEdit() statt submitAdd() aktiv -->
    :templateId="templateId"
    :template="template"
/>
```

Die Komponente selbst hat **kein eigenes Template-UI**, nur Child-Komposition.

## Abhängigkeiten

- **Import**: `CustomProductForm` aus `./custom-product-form.vue` (sibling in gleichem Verzeichnis)
- **Keine direkten API-Calls**: alle Netzwerk-Operationen erfolgen in `CustomProductForm.onSubmit() → submitEdit()`

## Verwender & Kontext

- **Backend-Route** (PHP): `/customProductTemplate/{id}/edit` ([GET], `CustomProductController::edit()`)
  - Rendert die Twig-Template `customProduct/edit.html.twig`
  - Übergibt `urlParams`, `id`, `template` als Twig-Variablen
  - Diese werden im HTML als Vue-Props transpiliert

- **Verwandte Dateien** im Repository:
  - `custom-product-form.vue` (Core-Logik, Form-State, Submit-Handler)
  - `add.vue` (identische Struktur, aber `mode="add"`)
  - `CustomProductController.php` (Backend-Schnittstelle)
  - `components/CollapsibleSection.vue`, `DaySelector.vue`, `StartTimeSelector.vue`, `DurationInput.vue`, `UnitForm.vue` (Kind-Komponenten)

## Besonderheiten & Fallstricke

### 1. Minimale Eigenverantwortung
Diese Komponente ist intentional **sehr dünn** und nur ein Wrapper. Sie delegiert:
- Template-Rendering → `CustomProductForm`
- State-Management (reactives `form` Objekt) → `CustomProductForm`
- Validierung und Submit-Logik → `CustomProductForm` (`submitEdit()` vs. `submitAdd()`)

### 2. `mode="edit"` als kritischer Schalter
Der hardcodierte `mode="edit"` in der Template-Zeile ist essentiell. In `CustomProductForm.onSubmit()`:
```javascript
async function onSubmit() {
    if (props.mode === 'add') {
        await submitAdd()
    } else if (props.mode === 'edit') {
        await submitEdit()   // <-- Wird nur erreicht wenn mode="edit"
    }
}
```

### 3. Backend-Daten-Struktur
Das `template`-Prop muss folgende Struktur haben:
```javascript
{
    id: "product-123",
    name: "Guided Tour",
    octoProduct: {
        id: "octo-456",
        uuid: "abc123...",
        product: {
            options: [
                {
                    id: "opt-1",
                    title: "Standard",
                    availabilityWeekdays: { monday: true, ... },
                    availabilitySeasons: [ /* normalisierte Seasons */ ],
                    units: [ /* Unit-Objekte mit Preisen */ ],
                    ...
                }
            ]
        }
    }
}
```

Fehlende oder falsche Struktur führt zu Runtime-Fehlern in `CustomProductForm`'s `onMounted()` → `loadCurrency()`.

### 4. urlParams-Propagation
`urlParams` wird 1:1 in `CustomProductForm` weitergegeben und dort verwendet für:
- API-Endpoint-Konstruktion: `fetch('/customProductTemplate/edit' + (props.urlParams || ""), ...)`
- Navigations-Links: `<LinkButton :href="\`/customProductTemplate${urlParams || ''}\`" />`

Muss zur Backend-Route passen (z.B. `?salesChannelId=xyz`).

### 5. Preis-Normalisierung in `CustomProductForm`
Die `custom-product-form.vue` normalisiert Preise beim Laden (geteilt durch 100, von Cents zu EUR):
```javascript
const priceSource = Array.isArray(unit.pricingFrom) 
    ? (unit.pricingFrom[0] ?? {}) 
    : (unit.pricingFrom ?? {});
const pricingFrom = {
    original: Number(priceSource.original ?? 0) / 100,
    retail: Number(priceSource.retail ?? 0) / 100,
    net: Number(priceSource.net ?? 0) / 100,
    ...
};
```

Beim Submit werden Preise wieder umgekehrt (multipliziert mit 100). **Fallstrick**: Wenn `0,00 EUR` eingegeben wird, wird das zu `0` multipliziert und bleibt `0` — ist gültig, aber oft nicht beabsichtigt.

### 6. Keine lokalen State-Mutationen
`edit.vue` hat **kein eigenes reaktives State**, nur Props. Alle Mutations-Handler sitzen in `CustomProductForm`.

## Verwandte Dateien

- `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/custom-product-form.vue` (Core-Komponente)
- `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/src/Controller/CustomProductController.php` (Backend)
- `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/add.vue` (Pendant für Neuanlage)

## Session & Offline

Keine direkten Session-Abhängigkeiten erkennbar. Der Kontext wird über `ModuleAction` im Backend bereitgestellt (Shopware-App-SDK).

## Testsuite

Keine Unit-Tests für diese Komponente im Repo erkennbar. Validierung erfolgt implizit durch Backend-API-Validierung in `CustomProductController::editTemplate()`.
