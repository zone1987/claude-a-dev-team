# TemplateTable Vue3-Komponente

**Pfad:** `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer/assets/vue/controllers/custom-product/template-table.vue`

## Zweck

Verwaltungsinterface für Custom-Product-Templates im ResubmissionAppServer. Darstellt eine paginierbare, sortierbare Tabelle aller verfügbaren Templates mit editierbaren Einträgen. Dient als Übersichtansicht mit Links zum Hinzufügen und Bearbeiten von einzelnen Templates.

## Typ & Komponente

**Vue 3 Single-File Component (SFC)** mit `<script setup>` Composition API.

- **Framework:** Vue 3 + TypeScript-ready
- **UI-Library:** Shopware Meteor Component Library (`@shopware-ag/meteor-component-library`)
- **Internationalisierung:** vue-i18n
- **Props:** `urlParams` (optional String, für Query-Parameter-Durchreichen)
- **Registrierung:** Importbar als `./template-table.vue`, erwartet keine globale Registrierung

## Komponenten-Struktur

### Props

```javascript
urlParams: String (optional)
```
Query-Parameter-String (z.B. `?locale=de_DE`), wird an allen Links weitergegeben (Bearbeitungs- und Erstellungs-Links).

### Reactive State (Refs)

| Property | Typ | Default | Zweck |
|----------|-----|---------|-------|
| `dataSource` | `ref<Array>` | `[]` | Gefüllte Template-Einträge vom Server |
| `paginationLimit` | `ref<number>` | `10` | Items pro Seite |
| `currentPage` | `ref<number>` | `1` | Aktuelle Seite (1-indexed) |
| `sortBy` | `ref<Object>` | `{ property: "", direction: "" }` | Aktuelle Sortiereinstellung (Property + direction) |

### Computed Properties

**`totalItems`** → `number`
- Extrahiert `total` aus erstem Element von `dataSource` (falls vorhanden und als Zahl parsebar)
- Fallback: Länge des lokalen Arrays
- **Algorithmus:** Prüft `firstTemplate.total`, validiert mit `Number.isNaN()`, gibt sonst `dataSource.length` zurück
- **Seiteneffekt:** Keine
- **Zweck:** Bestimmt Gesamtzahl für Pagination-Component

**`columns`** → `Array<{label, property, position, sortable}>`
- Definiert Spalten-Schema für `mt-data-table`
- Spalten:
  1. **Name** (property: "name", sortierbar)
  2. **Aktionen** (property: "actions", nicht sortierbar)
- Labels über `t("template.columns.*")`
- Position: name=200, actions=1200 (für Rendering-Order)

**`paginationOptions`** → `number[]` = `[5, 10, 25, 50]`
- Verfügbare Seitengröße-Optionen für Dropdown

### Methoden

#### `async loadTemplates(): Promise<void>`

**Signatur:** `async function loadTemplates()`

**Zweck:** Lädt Template-Liste vom Server basierend auf aktuellem Pagination-, Sort- und URL-Param-Status.

**Algorithmus:**
1. Erstellt `URLSearchParams` mit:
   - `sortBy`: aktueller Sortstatus als JSON-String
   - `page`: `currentPage.value` (1-indexed)
   - `limit`: `paginationLimit.value`
2. Sendet POST-Request an `/customProductTemplate${urlParams || ''}`
3. Erwartet JSON-Response mit `{ data: Array }`
4. Setzt `dataSource.value = result.data`

**Request-Details:**
- **Methode:** POST
- **Content-Type:** `application/x-www-form-urlencoded`
- **Body:** URLSearchParams-formatiert
- **URL-Konstruktion:** Dynamisch aus `props.urlParams`

**Exceptions/Error-Handling:** Try-catch mit `console.error()`, kein Throwback (stille Fehlerbehandlung)

**Seiteneffekte:**
- Mutiert `dataSource.value`
- HTTP-Request mit Pagination/Sort-Zustand
- Logging bei Fehler

**Aufrufer:** 
- `onMounted` (Komponenten-Lifecycle)
- `handleSortChange()` (nach Sort-Änderung)
- `handleLimitChange()` (nach Limit-Änderung)
- `handlePageChange()` (nach Seite-Änderung)

#### `handleSortChange(property: string, direction: string): void`

**Signatur:** `(property, direction) => void`

**Zweck:** Event-Handler für Sortierspalten-Klick. Aktualisiert Sortstatus und lädt Daten neu.

**Algorithmus:**
1. Aktualisiert `sortBy.value` mit neuer Property und Direction
2. Ruft `loadTemplates()` auf

**Seiteneffekte:**
- Mutiert `sortBy.value`
- Triggeriert HTTP-Request via `loadTemplates()`

**Event:** Gebunden an `@sortChange` der `mt-data-table`

#### `handleLimitChange(newLimit: number): void`

**Signatur:** `(newLimit) => void`

**Zweck:** Event-Handler für Pagination-Limit-Dropdown. Setzt neues Limit, resettet auf Seite 1, lädt neu.

**Algorithmus:**
1. Setzt `paginationLimit.value = newLimit`
2. Resettet `currentPage.value = 1`
3. Ruft `loadTemplates()` auf

**Seiteneffekte:**
- Mutiert `paginationLimit.value` und `currentPage.value`
- Triggeriert HTTP-Request

**Event:** Gebunden an `@pagination-limit-change`

#### `handlePageChange(newPage: number): void`

**Signatur:** `(newPage) => void`

**Zweck:** Event-Handler für Pagination-Navigation (Seiten-Nummern). Aktualisiert Seite und lädt Daten.

**Algorithmus:**
1. Setzt `currentPage.value = newPage`
2. Ruft `loadTemplates()` auf

**Seiteneffekte:**
- Mutiert `currentPage.value`
- Triggeriert HTTP-Request

**Event:** Gebunden an `@pagination-current-page-change`

### Lifecycle Hooks

**`onMounted()`**
- Ruft `loadTemplates()` auf beim Komponenten-Mount
- Populiert Tabelle mit initialen Daten

## Template / UI-Struktur

### Hauptkomponente: `<mt-data-table>`

**Props:**
| Prop | Wert | Zweck |
|------|------|-------|
| `class` | `"template-table"` | CSS-Klasse |
| `:columns` | `columns` (computed) | Spalten-Definition |
| `:data-source` | `dataSource` (ref) | Tabellenzeilen |
| `:pagination-limit` | `paginationLimit` | Aktuelle Seitengröße |
| `:current-page` | `currentPage` | Aktuelle Seite |
| `:pagination-total-items` | `totalItems` | Gesamtzahl für Pagination |
| `:paginationOptions` | `[5,10,25,50]` | Verfügbare Limits |
| `:disable-search` | `true` | Suche deaktiviert |
| `layout` | `"full"` | Vollbreiten-Layout |
| `disable-edit` | `-` | Inline-Bearbeitung deaktiviert |
| `disable-delete` | `-` | Löschen deaktiviert |
| `disable-settings-table` | `-` | Tabellen-Einstellungen deaktiviert |
| `:title` | `t('template.title')` | Tabel-Titel (i18n) |
| `:subtitle` | `t('template.subtitle')` | Tabel-Untertitel (i18n) |

**Event-Listener:**
- `@pagination-limit-change="handleLimitChange"`
- `@pagination-current-page-change="handlePageChange"`
- `@sortChange="handleSortChange"`

### Slots

#### `#toolbar`
Enthält "Add Template"-Button:
```vue
<LinkButton
    :href="`/customProductTemplate/add${urlParams || ''}`"
    :text="t('template.button.add')"
/>
```
- Navigiert zu Erstellungsseite
- Hängt `urlParams` an (z.B. zur Locale-Persistierung)

#### `#column-name="{ data }"`
Rendert Template-Name oder Fallback:
```vue
{{ data?.name || "–" }}
```
- **Seiteneffekt:** Keine
- **Fallback:** Em-Dash bei fehlendem Name

#### `#column-actions="{ data }"`
Rendert Edit-Button:
```vue
<LinkButton
    :href="`/customProductTemplate/${data.id}/edit${urlParams || ''}`"
    :text="t('template.button.edit')"
/>
```
- Navigiert zu Bearbeitungsseite mit Template-ID
- Hängt `urlParams` an

## Abhängigkeiten & Importe

| Import | Quelle | Zweck |
|--------|--------|-------|
| `MtDataTable` | `@shopware-ag/meteor-component-library` | Shopware Meteor Tabellen-Component |
| `LinkButton` | `../link-button.vue` | Lokale Button-Komponente (Navigation) |
| `computed, ref, onMounted` | `vue` | Vue 3 Composition API |
| `useI18n` | `vue-i18n` | Internationalisierungs-Hook |

## Besonderheiten & Fallstricke

### 1. **Total-Berechnung via erstem Element**
   - `totalItems` versucht, `firstTemplate.total` zu extrahieren
   - **Annahme:** Server gibt in jedem Response-Item ein `total`-Feld zurück (Metadaten)
   - **Fallback:** Lokale Array-Länge
   - **Risiko:** Wenn `total` nicht vorhanden, wird nur lokale Seite gezählt (falsche Pagination möglich)

### 2. **Stilles Error-Handling**
   - `loadTemplates()` fehlerhafte Requests loggen nur zu Console, keine UI-Feedback
   - **Empfehlung:** Error-Toast oder Fehler-State hinzufügen

### 3. **URLSearchParams + Content-Type Mismatch**
   - Body wird als `URLSearchParams` gesendet, aber Header setzt `application/x-www-form-urlencoded`
   - ✓ Korrekt, wenn Backend dieses Format erwartet
   - Backend muss `sortBy` als JSON-String parsen

### 4. **Sort-Struktur**
   - `sortBy = { property: "", direction: "" }`
   - Initial mit leeren Strings (keine Default-Sortierung)
   - **Impact:** Erste Abfrage könnte unsortiert sein

### 5. **Page-Reset auf Limit-Change**
   - Limit-Wechsel setzt automatisch zu Seite 1
   - ✓ Standard UX-Pattern, verhindert "out of bounds"-Fehler

### 6. **Keine Typisierung**
   - Props, State, Methoden ohne TypeScript-Annotationen
   - DataSource-Struktur implicit erwartet (`data.id`, `data.name`)
   - **Fragil:** Keine Compile-Zeit-Sicherheit

### 7. **URL-Konstruktion mit optionalen Params**
   - `urlParams || ''` überall wiederholt (Code-Duplikat möglich)
   - **Refactor-Kandidat:** In Computed Property auslagern

### 8. **LinkButton-Abhängigkeit**
   - Setzt voraus, dass `/customProductTemplate/add` und `/customProductTemplate/{id}/edit` Routen existieren
   - **Contract:** Backend muss diese Routes bereitstellen

## Verwandte Dateien

- `../link-button.vue` — Button-Komponente mit href-Navigation
- `/customProductTemplate` — Backend-Endpoint für Template-Liste (POST)
- `/customProductTemplate/{id}/edit` — Backend-Route für Edit-Seite
- `/customProductTemplate/add` — Backend-Route für Create-Seite
- Lokalisierung: `template.columns.*`, `template.button.*`, `template.title`, `template.subtitle` in i18n-Konfiguration

## Integration im FfOctoApi-Kontext

Diese Komponente ist Teil des **ResubmissionAppServer** und verwaltet Custom-Product-Templates. Keine direkte Abhängigkeit zu Ventrata OCTO API erkennbar, aber Templates könnten mit OCTO-Produkt-Definitionen verknüpft sein (Cross-Repo-Vertrag AppServer ↔ FfOctoApi).

**Potential Verknüpfung:**
- Templates für Ticketing-Produkte generieren
- Preisanpassungen / Variantenmanagement
- Session-Persistierung von Template-Auswahl (nicht implementiert)
