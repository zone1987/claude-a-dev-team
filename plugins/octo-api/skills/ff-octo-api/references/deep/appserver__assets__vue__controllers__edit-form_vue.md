# EditForm Vue Component (/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/edit-form.vue)

## Zweck
Vue 3 Single-File-Komponente für die Bearbeitung von Resubmission-Metadaten auf Order-Ebene in der Shopware-Verwaltungsapp. Wird in der Resubmission-Edit-Seite eingebunden und kommuniziert mit dem Backend-Endpoint POST `/resubmission/{id}/edit`, um Fälligkeitsdatum, Status, Notizen und zuständigen Benutzer zu speichern.

## Typ & Vererbung
- **Typ**: Vue 3 `<script setup>` Single-File-Component
- **Framework**: Vue 3 mit Composition API (Reactive + Ref)
- **UI-Library**: Shopware Meteor Component Library (@shopware-ag/meteor-component-library)
- **Internationalisierung**: vue-i18n (mit `useI18n()`)
- **Registrierung**: Wird über Symfony UX Vue (`vue_component('edit-form', {...})`) in Twig/edit.html.twig rendern
- **Props**: Drei erforderliche Props vom Twig-Template

## Props (defineProps)

| Name | Typ | Erforderlich | Quelle | Beschreibung |
|------|-----|-------------|--------|-------------|
| `urlParams` | String | Ja | Twig-Template | URL-Parameter für Shopware-Modul-Kontext (z.B. `?ids=X&ids=Y`); wird an API-Endpoints angehängt |
| `orderId` | String | Ja | Twig-Template | Die eindeutige Order-ID aus der Route `/resubmission/{id}/edit`; wird in editPost-Request verwendet |
| `order` | Object | Ja | Twig-Template | Die komplette Order-Entity vom Backend (Controller::edit); enthält Custom-Fields `resubmission_active`, `resubmission_date`, `resubmission_note`, `resubmission_user` |

## Reaktive Daten (reactive/ref)

### form (reactive)
```javascript
const form = reactive({
    active: props.order?.resubmission_active ?? false,        // Boolean, Default: false
    dueDate: props.order?.resubmission_date ?? null,          // ISO-Date-String oder null
    note: props.order?.resubmission_note ?? '',               // String, Default: '' (leerer String)
    user: props.order?.resubmission_user ?? null,             // String/UUID oder null
});
```
- **Zweck**: Bidirektionale Form-State mit v-model an MtSwitch, MtDatepicker, MtTextarea, MtSelect
- **Seiteneffekt**: Wird beim Komponenten-Mount mit Order-Custom-Fields initialisiert

### loading (ref)
```javascript
const loading = ref(false);
```
- **Typ**: Boolean Ref
- **Zweck**: Steuert `:loading`-Prop des Submit-Buttons und `:disabled`-Prop des Cancel-Buttons
- **Workflow**: Wird auf `true` gesetzt bei onSubmit-Beginn, auf `false` in finally-Block nach Redirect

### userOptions (ref)
```javascript
const userOptions = ref([]);
```
- **Typ**: Array von Objekten mit `{id, value, label}`
- **Initialisierung**: Leer beim Mount; wird asynchron durch `loadUsers()` gefüllt
- **Struktur nach loadUsers()**:
  ```javascript
  {
    id: user.id,                                    // UUID
    value: user.id,                                // UUID (duplicate für MtSelect-Kompatibilität)
    label: `${firstName} ${lastName}`.trim() || username   // Fallback auf username wenn kein Name
  }
  ```

## Lifecycle

### Komponenten-Mount (implizit durch <script setup>)
- `loadUsers()` wird direkt aufgerufen (Zeile 104)
- Async-Fetch ohne await-Blockierung; Fehler werden nur zu console.error geloggt

## Methoden

### loadUsers() — async
**Signatur**: `async function loadUsers(): Promise<void>`

**Zweck**: Lädt die Liste aller Benutzer vom Backend-Endpoint `/resubmission/users` und populates das `userOptions`-Ref für die MtSelect-Komponente.

**Implementierung**:
1. POST-Fetch zu `/resubmission/users{urlParams}`
2. Antwortkörper muss JSON mit Array unter `result.data` sein
3. Jedes User-Objekt hat Struktur:
   ```
   {
     id: string,
     attributes: {
       firstName?: string,
       lastName?: string,
       username: string
     }
   }
   ```
4. Transformation zu Select-Options (id, value, label)
5. Label-Logik:
   - Falls `firstName || lastName` vorhanden: `"${firstName} ${lastName}".trim()`
   - Fallback: `username`

**Seiteneffekt**: 
- Setzt `userOptions.value`
- Console.error bei Fehler (keine Error-Propagation)

**Exceptions**: Fangen alle Fetch-Fehler ab (keine Rethrow); nur Konsolenlogging

**Aufrufer**: Wird beim Komponenten-Mount aufgerufen (Zeile 104, vor Template-Render)

**Request-Format**:
```
POST /resubmission/users
Content-Type: application/json (bei Fetch)
Body: (leer oder ggf. urlParams)
```

### onSubmit() — async
**Signatur**: `async function onSubmit(): Promise<void>`

**Zweck**: Speichert die geänderten Resubmission-Felder via POST an `/resubmission/{orderId}/edit` und leitet danach auf `/resubmission` um.

**Implementierung**:
1. Setzt `loading.value = true`
2. Erstellt URLSearchParams mit:
   - `active`: form.active (Boolean → String 'true'/'false')
   - `date`: form.dueDate (ISO-String oder null)
   - `note`: form.note (Text)
   - `user`: form.user (User-ID oder null)
3. POST-Fetch zu `/resubmission/{orderId}/edit{urlParams}`
   - Content-Type: `application/x-www-form-urlencoded;charset=UTF-8`
   - Body: URLSearchParams
4. Im `finally`-Block (wird immer ausgeführt):
   - `loading.value = false`
   - `window.location.href = '/resubmission' + urlParams` (Hard-Redirect, keine Vue-Router)

**Seiteneffekte**:
- HTTP POST mit URL-enkodiertem Body
- Hard-Redirect via window.location (lädt Seite neu)
- Speichert Daten im Shopware-Order-Custom-Field (Backend)

**Exceptions**: Keine Try-Catch; Fetch-Fehler würden unbehandelt bleiben (Bug: sollte Error-Handling haben)

**Aufrufer**: Click-Handler auf Primary-Button (Zeile 39, `@click="onSubmit"`)

**Backend-Entsprechung**: `ResubmissionController::editPost(ModuleAction, string, Request)` 
- Liest `request->request->get('active')`, `.get('date')`, `.get('note')`, `.get('user')`
- Ruft `adminClient->setOrderCustomField($id, {...})` auf
- Returniert 200 OK

### onCancel() — sync
**Signatur**: `function onCancel(): void`

**Zweck**: Hard-Redirect auf die Order-Übersichtsliste (Resubmission-Index) ohne Speicherung.

**Implementierung**:
```javascript
const url = '/resubmission' + props.urlParams;
window.location.href = url;
```

**Seiteneffekte**: Hard-Redirect via window.location

**Aufrufer**: Click-Handler auf Secondary-Button (Zeile 30, `@click="onCancel"`)

## Template-Struktur

```html
<template>
  <mt-card>
    <!-- 1. Active Toggle -->
    <MtSwitch v-model="form.active" :label="t('resubmission.form.active')" />
    
    <!-- 2. Due Date Picker -->
    <MtDatepicker v-model="form.dueDate" :label="t('resubmission.form.dueDate')" />
    
    <!-- 3. Note Textarea -->
    <MtTextarea
      v-model="form.note"
      :label="t('resubmission.form.note')"
      :placeholder="t('resubmission.form.notePlaceholder')"
    />
    
    <!-- 4. User Dropdown -->
    <MtSelect
      :label="t('resubmission.form.user')"
      v-model="form.user"
      :options="userOptions"
    />
    
    <!-- 5. Action Buttons -->
    <div class="form-actions">
      <MtButton variant="secondary" type="button" @click="onCancel" :disabled="loading">
        {{ t('resubmission.form.cancel') }}
      </MtButton>
      <MtButton variant="primary" type="button" @click="onSubmit" :loading="loading">
        {{ t('resubmission.form.save') }}
      </MtButton>
    </div>
  </mt-card>
</template>
```

**Komponenten**:
- `<mt-card>`: Shopware-Kartenelement (Wrapper)
- `<MtSwitch>`: Toggle für `form.active`
- `<MtDatepicker>`: Datumswähler für `form.dueDate`
- `<MtTextarea>`: Mehrzeiliges Textfeld für `form.note`
- `<MtSelect>`: Dropdown mit `userOptions` für `form.user`
- `<MtButton>`: Zwei Action-Buttons (Cancel/Submit)

**Internationalisierung (i18n-Keys)**:
- `resubmission.form.active`
- `resubmission.form.dueDate`
- `resubmission.form.note`
- `resubmission.form.notePlaceholder`
- `resubmission.form.user`
- `resubmission.form.cancel`
- `resubmission.form.save`

## Imports & Dependencies

```javascript
import { reactive, ref } from 'vue';                        // Vue 3 Composition API
import { useI18n } from "vue-i18n";                         // i18n für Mehrsprachigkeit
import { 
  MtButton, 
  MtSwitch, 
  MtTextarea, 
  MtDatepicker, 
  MtCard, 
  MtSelect 
} from "@shopware-ag/meteor-component-library";             // Shopware UI-Komponenten
```

**Abhängigkeiten**:
- **Vue 3**: Für `reactive()` und `ref()`
- **vue-i18n**: Für `useI18n()` und `t()` (Translation-Helper)
- **@shopware-ag/meteor-component-library**: Shopware-UI-Komponenten

## Besonderheiten & Fallstricke

### 1. Hard-Redirect bei Submit & Cancel
- Beide Funktionen nutzen `window.location.href` für Full-Page-Redirect
- **Konsequenz**: Der Vue-Router wird umgangen; Komponenten-State wird nicht beibehalten
- **Fallstrick**: Falls Submit fehlschlägt (400/500), wird trotzdem umgeleitet (weil Redirect im finally-Block ist)
  - **Bug**: Sollte nur bei erfolgreichem Status (200) umleitenoder Error-Behandlung implementieren

### 2. loadUsers() wird nicht awaitet
```javascript
loadUsers();  // Zeile 104 — async, aber nicht await
```
- **Konsequenz**: MtSelect rendert zunächst mit leerem `userOptions.value`
- **Fallstrick**: Race-Condition, wenn API-Response verzögert kommt
- **Vermutlich beabsichtigt**: MtSelect ist optional (nicht erforderlich); laden im Hintergrund ist OK

### 3. URLSearchParams für Form-Encoding
```javascript
const body = new URLSearchParams({ active: form.active, date: form.dueDate, note: form.note, user: form.user });
```
- **Achtung**: Booleans und null-Werte werden als Strings konvertiert
  - `true` → `"true"`, `false` → `"false"`, `null` → `"null"` (Strings!)
- **Backend-Handling** (ResubmissionController::editPost):
  ```php
  $activeRaw = $request->request->get('active');  // String "true" oder "false" oder "null"
  $active = filter_var($activeRaw, FILTER_VALIDATE_BOOL, FILTER_NULL_ON_FAILURE);  // Konvertierung
  ```
  - `filter_var($activeRaw, FILTER_VALIDATE_BOOL, FILTER_NULL_ON_FAILURE)` konvertiert "true"/"false"/null korrekt

### 4. Order-Custom-Fields Struktur
- Das Backend erwartet Custom-Fields mit Präfix `resubmission_`:
  - `resubmission_active` (Boolean)
  - `resubmission_date` (ISO-Date)
  - `resubmission_note` (String)
  - `resubmission_user` (User-ID/UUID)
- Diese müssen in Shopware bereits als Custom-Fields definiert sein (Migrations/Entity-Definition)

### 5. Fehlerbehandlung
- **loadUsers()**: Fehler werden nur geloggt (console.error); keine UI-Benachrichtigung
- **onSubmit()**: Keine Fehlerbehandlung; Fetch-Fehler würde unabgefangen bleiben
  - **Verbesserungspotenzial**: Try-Catch mit User-Feedback hinzufügen

### 6. Opener-Vertrag mit Backend
Die Komponente erwartet, dass der Backend-Controller folgende Endpoints bereitstellt:
- **GET** `/resubmission/{id}/edit` → Liefert Order mit Custom-Fields (in ResubmissionController::edit())
- **POST** `/resubmission/{id}/edit` → Speichert Custom-Fields (in ResubmissionController::editPost())
- **POST** `/resubmission/users` → Liefert User-Liste (in ResubmissionController::getUsers())

### 7. Module-Action-Kontext
- `urlParams` wird vom Backend-Controller via `ModuleActionService::buildParameters($module)` erzeugt
- Enthält Shopware-Modul-Identifikation (z.B. App-ID, Shop-ID)
- Wird an jeden API-Request angehängt → Ermöglicht Backend, Kontext zu rekonstruieren

## Verwandte Dateien (Pfade relativ zum Projekt)

- **Backend-Controller**: `src/Controller/ResubmissionController.php`
  - Methode: `edit()` (GET, Zeile 69)
  - Methode: `editPost()` (POST, Zeile 97)
  - Methode: `getUsers()` (POST, Zeile 269)
  
- **Twig-Template**: `templates/resubmission/edit.html.twig`
  - Rendert Komponente mit Props
  
- **Service**: `src/Service/AdminApiClient.php`
  - Methode: `getOrder($id)` (wird von ResubmissionController::edit() aufgerufen)
  - Methode: `setOrderCustomField($id, $fields)` (wird von ResubmissionController::editPost() aufgerufen)
  - Methode: `getUsers($filter)` (wird von ResubmissionController::getUsers() aufgerufen)

- **Internationalisierungsdatei**: `assets/vue/i18n/messages.js`
  - Enthält Übersetzungen für i18n-Keys `resubmission.form.*`

- **Verwandte Komponenten**:
  - `assets/vue/controllers/order-table.vue` — Tabelle mit Order-Liste (Listing)
  - `assets/vue/controllers/link-button.vue` — Link zu dieser Edit-Komponente

## Testfallbeispiele (keine Tests in der Datei, aber empfohlen)

- **loadUsers()**: Mock API, Test auf leere Liste, Test auf User mit/ohne Vornamen/Nachnamen
- **onSubmit()**: Mock Fetch, Test auf Redirect mit urlParams, Test auf loading-Flag-Wechsel
- **onCancel()**: Direkt-Test auf window.location.href-Änderung
- **Form-Binding**: v-model-Zwei-Wege-Bindung für alle vier Felder
- **i18n**: Verifizierung, dass alle i18n-Keys existieren

## Zusammenfassung der Datenflüsse

```
[edit.html.twig: props übergeben]
            ↓
[edit-form.vue: Component Mount]
            ↓
[loadUsers() → POST /resubmission/users → userOptions.value gefüllt]
            ↓
[Template rendert mit geladenem userOptions]
            ↓
[User interagiert mit Form]
            ↓
[onSubmit() oder onCancel()]
            ├─→ onSubmit(): POST /resubmission/{orderId}/edit → Redirect /resubmission
            └─→ onCancel(): Redirect /resubmission (ohne speichern)
            ↓
[Hard-Page-Redirect via window.location.href]
```

