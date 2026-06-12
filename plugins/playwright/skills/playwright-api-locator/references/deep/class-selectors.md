# class-selectors — Playwright API Reference

Die `Selectors`-Klasse ermoeglicht das Registrieren eigener Selektor-Engines und das Konfigurieren des Test-ID-Attributs. Beide Methoden muessen **vor** der Erstellung von Seiten aufgerufen werden. Zugriff via `playwright.selectors` (globale Playwright-Instanz).

Methoden-Anzahl: 2

---

## register()

```typescript
register(
  name: string,
  script: Function | string | { path?: string; content?: string },
  options?: { contentScript?: boolean }
): Promise<void>
```

Registriert eine eigene Selektor-Engine. Nach der Registrierung kann der Selektor ueber das Praefix `name=myselector` in allen Methoden verwendet werden, die Selektoren akzeptieren.

**Wichtig:** Muss aufgerufen werden, bevor Seiten (`page`) erstellt werden.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string` | ja | — | Eindeutiger Bezeichner (nur `[a-zA-Z0-9_]`); wird als Praefix `name=...` genutzt |
| `script` | `Function \| string \| { path?: string; content?: string }` | ja | — | Evaluiert zu einer Selektor-Engine-Instanz; wird im Seitenkontext ausgefuehrt |
| `options.contentScript` | `boolean` | nein | `false` | Engine in isolierter JS-Umgebung ausfuehren (hat Zugriff auf DOM, aber nicht auf Frame-Scripts) |

**Rueckgabe:** `Promise<void>`

### Selektor-Engine API

Das Script muss ein Objekt mit folgenden Methoden zurueckgeben:

| Methode | Signatur | Beschreibung |
|---|---|---|
| `query` | `(root: Element, selector: string) => Element \| null` | Findet erstes passendes Element |
| `queryAll` | `(root: Element, selector: string) => Element[]` | Findet alle passenden Elemente |

```typescript
// Eigene Engine: findet Elemente ueber data-qa-Attribut
await playwright.selectors.register('qa', () => ({
  query(root, selector) {
    return root.querySelector(`[data-qa="${selector}"]`);
  },
  queryAll(root, selector) {
    return Array.from(root.querySelectorAll(`[data-qa="${selector}"]`));
  },
}));

// Verwendung
await page.locator('qa=submit-button').click();
```

Aus einer Datei laden:

```typescript
await playwright.selectors.register('myengine', {
  path: './my-selector-engine.js',
});
```

---

## setTestIdAttribute()

```typescript
setTestIdAttribute(attributeName: string): void
```

Setzt das HTML-Attribut, das von `getByTestId()` verwendet wird. Standard ist `data-testid`.

**Wichtig:** Muss vor der Erstellung von Seiten aufgerufen werden.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `attributeName` | `string` | ja | — | Name des Attributs, das als Test-ID interpretiert wird |

**Rueckgabe:** `void`

```typescript
// In playwright.config.ts oder einer globalen Setup-Datei:
import { selectors } from '@playwright/test';
selectors.setTestIdAttribute('data-cy');

// Anschliessend:
await page.getByTestId('login-form').fill('...'); // sucht nach data-cy="login-form"
```

---

## Methoden-Uebersicht

| Methode | Zweck |
|---|---|
| `register()` | Eigene Selektor-Engine registrieren |
| `setTestIdAttribute()` | Test-ID-Attributname konfigurieren |

---

Quelle: https://playwright.dev/docs/api/class-selectors
