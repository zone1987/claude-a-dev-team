# Custom Product Template - Add View (add.vue)

**Dateipfad:** `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/add.vue`

## Zweck

Vue-Wrapper-Komponente zur Anzeige des Formulars zum Erstellen neuer Produkt-Templates im ResubmissionAppServer. Delegiert die komplette Formularlogik an die `custom-product-form.vue`-Komponente mit dem Modus `add`. Diese Komponente wird vom Backend (Symfony) als Twig-Template `customProduct/add.html.twig` gerendert und erhält URL-Parameter zur Shop-Identifikation weitergeleitet.

## Typ & Vererbung

**Typ:** Vue 3 Single-File Component (SFC)  
**Script Setup:** `<script setup>` Composition API  
**Imports:** 
- `CustomProductForm` von `./custom-product-form.vue` (lokale Komponente)
- Vue 3 Komponenten-Registration

## Props

| Prop | Typ | Default | Bedeutung |
|------|-----|---------|-----------|
| `urlParams` | `String` | - | Query-String mit Shop-Identifikation (z.B. `?shop=abc123&token=xyz`). Wird vom Backend mittels `ModuleActionService::buildParameters()` generiert und an das Twig-Template übergeben. Dient der Weitergabe an Sub-Komponenten und HTTP-Anfragen. |

## Template-Struktur

```vue
<MtCard class="custom-product-form">
  <CustomProductForm
    :urlParams="urlParams"
    mode="add"
  />
</MtCard>
```

Die Komponente erzeugt eine **einfache Wrapper-Struktur** ohne zusätzliche UI-Logik:
- `<MtCard>` aus Meteor Component Library als Container
- `<CustomProductForm>` als embedded Sub-Komponente mit zwei Props:
  - `:urlParams` - weitergeleitet von außen
  - `mode="add"` - feste Konstante zur Steuerung des Submitverhaltens in `custom-product-form.vue`

## Verhaltensfluss

1. **Mount:** Browser navigiert zu `/customProductTemplate/add?shop=...&token=...` (Symfony Route: `app_custom_product_template_add`, `CustomProductController::add()`)
2. **Render:** Twig rendert `customProduct/add.html.twig`, das den Vue-Mount-Point mit `urlParams` initialisiert
3. **Komponentenaufbau:** Vue instanziiert diese Komponente, übergeben Props werden gelesen
4. **Sub-Komponente:** `CustomProductForm` wird gerendert mit `mode="add"` → aktiviert später `submitAdd()`-Funktion statt `submitEdit()`
5. **User-Interaktion:** Formular wird ausgefüllt, Button "Speichern" gelöst `CustomProductForm::onSubmit()` aus
6. **HTTP POST:** `submitAdd()` sendet Daten an `/customProductTemplate/add` mit `urlParams` angehängt
7. **Redirect:** Nach erfolgreichem POST: `window.location.href = '/customProductTemplate' + props.urlParams` zurück zur Übersicht

## Integration mit Backend

**Related Controller:** `/src/Controller/CustomProductController.php`
- `GET /customProductTemplate/add` → `CustomProductController::add()` rendert Twig mit `urlParams`
- `POST /customProductTemplate/add` → Backend empfängt JSON-Daten via `CustomProductForm::submitAdd()`

**URL-Parameter-Fluss:**
```
UserRequest with shop token
    ↓
Symfony Route guards, injects ModuleAction
    ↓
ModuleActionService::buildParameters() → Query-String
    ↓
Twig renders with props: { urlParams }
    ↓
add.vue receives via prop
    ↓
CustomProductForm uses for HTTP calls
    ↓
Backend validates shop via token
```

## Verwandte Komponenten & Dateien

- **`custom-product-form.vue`** (`./custom-product-form.vue`) - Hauptformular-Logik, Template, State-Management
  - Props: `urlParams`, `mode`, `templateId` (unused in add), `template` (unused in add)
  - Events: keine direkten Events, HTTP-Redirect nach Submit
  - Sub-Komponenten: `CollapsibleSection`, `DaySelector`, `StartTimeSelector`, `DurationInput`, `UnitForm`

- **`edit.vue`** (`./edit.vue`) - Schwester-Komponente, identische Struktur, `mode="edit"`, empfängt zusätzlich `templateId` und `template` Props

- **Template-Twig:** `templates/customProduct/add.html.twig` - rendert dieses Vue-Komponenten-Wrapper

- **Backend-Controller:** `src/Controller/CustomProductController::add()`, `::addTemplate()` (POST-Handler)

## Besonderheiten & Fallstricke

1. **Prop als String, nicht Object:** `urlParams` ist String (z.B. `"?shop=abc&token=xyz"`), NICHT ein Objekt mit Eigenschaften. Dies ist bewusst zur einfachen String-Verkettung in HTTP-URLs: `/customProductTemplate/add${props.urlParams}`

2. **Keine State-Verwaltung in add.vue selbst:** Alle State ist in `custom-product-form.vue`. Die `add.vue`-Komponente ist nur ein dünner Wrapper ohne eigene Data/Methods. Dies ermöglicht Code-Reuse zwischen Add- und Edit-Modi.

3. **Mode-Konstante:** `mode="add"` ist hart codiert. Bei `mode="edit"` würde `CustomProductForm::onSubmit()` stattdessen `submitEdit()` aufrufen (siehe Zeile 605-609 in custom-product-form.vue).

4. **Keine Error-Handling in add.vue:** Fehler werden entweder in `CustomProductForm` abgefangen (z.B. `loadCurrency()` try-catch, Zeile 564) oder als unkontrollierte Fehler geworfen. HTTP-Fehler beim POST führen direkt zu Page-Redirect ohne Nutzerbenachrichtigung.

5. **Shop-Token-Abhängigkeit:** Ohne `urlParams` mit gültigem Token funktionieren HTTP-Anfragen vom Backend fehlgeschlagen. Dies ist ein Sicherheitsmechanismus des ResubmissionAppServer.

6. **Template Property unused:** In `custom-product-form.vue` gibt es ein `template` Prop (Zeile 206-209), das in `add.vue` nicht gesetzt wird. Stattdessen wird `template` standardmäßig auf `{}` initialisiert. Dies ist korrekt, da beim Erstellen kein bestehendes Template geladen wird.

7. **Currency-Loading:** `CustomProductForm::loadCurrency()` wird bei `onMounted` aufgerufen (Zeile 650-652). POST-Anfrage erfolgt zu `/customProductTemplate/currency${props.urlParams}`. Fallback auf `['EUR', 'GBP']` wenn Fetch fehlschlägt.

8. **Preis-Conversion:** Preise werden in Cent gespeichert (Multiplikation mit 100 bei Submit, Zeile 367-369). Frontend zeigt EUR-Werte (Division durch 100 beim Load).

## Typen & Signaturen

### Komponenten-Definition
```typescript
interface Props {
  urlParams: string;
}

// Impliziert von custom-product-form.vue:
interface CustomProductFormProps {
  urlParams: string;
  mode: 'add' | 'edit';
  templateId?: string;
  template?: CustomProductTemplate;
}
```

### CustomProductTemplate (aus custom-product-form.vue Zeile 206-209)
```typescript
type CustomProductTemplate = {
  name?: string;
  octoProduct?: {
    id: string;
    uuid: string;
    product: {
      options: CustomProductOption[];
    };
  };
}
```

## HTTP-Schnittstellenverträge

### GET /customProductTemplate/add
**Symfony Route:** `app_custom_product_template_add`  
**Handler:** `CustomProductController::add(ModuleAction $module)`  
**Response:** HTML mit embedded Vue app, Props: `{ urlParams }`

### POST /customProductTemplate/add
**Symfony Route:** wird nicht explizit in add.vue definiert, Handler abhängig von Backend**  
**Request Body (URL-encoded):**
```
name=<string>&options=<JSON-array>
```

**Options JSON Schema:** Array mit Strukturen:
```javascript
{
  id: null | string,
  default: boolean,
  internalName: string,
  title: string,
  cancellationCutoffAmount: null | number,
  cancellationCutoffUnit: null | string,
  durationAmount: null | number,
  durationUnit: null | string,
  availabilityLocalStartTimes: string[],
  availabilityWeekdays: { monday: bool, tuesday: bool, ... },
  availabilitySeasons: SeasonObject[],
  units: UnitObject[]
}
```

**Response:** Redirect zu `/customProductTemplate${urlParams}` (301/302)

## Code-Duplikate & Refactoring-Potenzial

- **add.vue vs. edit.vue:** Identische Struktur, unterscheiden sich nur in `mode="add"` vs. `mode="edit"`. Könnten in eine gemeinsame Wrapper-Komponente mit `mode` Prop zusammengefasst werden.

- **prepareOptionsForSubmit() Duplikat:** Logik zur Preis-Konvertierung (÷100 im Load, ×100 im Submit) ist verteilt. Könnte in Utility-Funktion ausgelagert werden.

- **createWeekdaysState():** Wird 4× aufgerufen (Zeile 214, 261, 339, 343). Ist korrekt, aber zeigt Bedarf für robuste Default-Handling bei Wochentagen.

## Test-Relevanz

Diese Komponente ist typischerweise nicht direkt getestet (zu dünn). Tests sollten auf `custom-product-form.vue` fokussieren:
- Unit Tests für State-Transformationen (Preis, Wochentage)
- Integration Tests für HTTP-Anfragen (Currency-Load, Submit)
- E2E Tests für kompletten Workflow (Route → Form → Submit → Redirect)

## Sicherheit & Validierung

1. **CSRF:** Nicht explizit sichtbar; Symfony-Token wird vermutlich vom Framework injiziert
2. **Authentifizierung:** Über `ModuleAction` aus Shopware SDK, Token in `urlParams`
3. **Input-Validierung:** Minimal im Frontend (nur `start/end` Datumscheck in `addSeason`, Zeile 445). Hauptvalidation erfolgt auf Backend.
4. **XSS-Schutz:** Vue 3 interpoliert standardmäßig escaped; keine `v-html` verwendet in dieser Komponente

## Bekannte Abhängigkeiten

- **Vue 3.x** (vue, vue-i18n)
- **Meteor Component Library** (@shopware-ag/meteor-component-library): MtCard, MtButton, MtTextField, etc.
- **Shopware ResubmissionAppServer** Backend (CustomProductController)
- **OCTO API Integration** (indirekt über Backend Admin API Client)

