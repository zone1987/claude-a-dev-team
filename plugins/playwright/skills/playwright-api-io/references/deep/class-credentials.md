# Playwright — class: Credentials (HTTPCredentials)

> **Manifest:** 0 Methoden, 2-4 Properties (Interface), 0 Events.
> Kein eigenstaendiges Klassenobjekt — `Credentials` / `HTTPCredentials` ist ein
> Konfigurations-Interface fuer HTTP-Basic-Authentifizierung in BrowserContext.

---

## Status

`Credentials` / `HTTPCredentials` ist kein eigenes Playwright-Klassenobjekt mit
Instanzmethoden, sondern ein Konfigurations-Interface, das als Option beim
Erstellen eines `BrowserContext` uebergeben wird.

Die Seite `https://playwright.dev/docs/api/class-credentials` existiert nicht in
den aktuellen Playwright-Docs. HTTP-Credentials sind als Interface-Typ in
`BrowserContext.newPage()` / `browser.newContext()` dokumentiert.

---

## HTTPCredentials Interface

```typescript
interface HTTPCredentials {
  username: string;
  password: string;
  origin?: string;
  send?: 'always' | 'unauthorized';
}
```

### Properties

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `username` | `string` | ja | — | HTTP Basic Auth Benutzername |
| `password` | `string` | ja | — | HTTP Basic Auth Passwort |
| `origin` | `string` | nein | — | Einschraenkung auf bestimmte Origin (z.B. `'https://example.com'`). Wenn angegeben, werden Credentials nur fuer diese Origin gesendet. |
| `send` | `'always' \| 'unauthorized'` | nein | `'unauthorized'` | `'always'`: Credentials bei jeder Anfrage senden. `'unauthorized'`: Nur bei HTTP 401-Antworten. |

---

## Verwendung

### Bei Context-Erstellung

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'admin',
    password: 'geheimpasswort'
  }
});
```

### Mit Origin-Einschraenkung

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'user',
    password: 'pass',
    origin: 'https://staging.example.com'
  }
});
```

### Immer senden (pre-emptive auth)

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'api-user',
    password: 'token123',
    send: 'always'
  }
});
```

---

## Deprecated: browserContext.setHTTPCredentials()

Die Methode `browserContext.setHTTPCredentials()` ist deprecated:

```javascript
// NICHT MEHR VERWENDEN:
await context.setHTTPCredentials({ username: 'user', password: 'pass' });

// Stattdessen: Neuen Context erstellen
const context = await browser.newContext({
  httpCredentials: { username: 'user', password: 'pass' }
});
```

**Hinweis:** Browser koennen Credentials nach erfolgreicher Authentifizierung
cachen. Daher empfiehlt Playwright, fuer jeden Test mit anderen Credentials einen
neuen BrowserContext zu erstellen.

---

## In playwright.config.ts

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    httpCredentials: {
      username: process.env.AUTH_USER!,
      password: process.env.AUTH_PASSWORD!
    }
  }
});
```

---

## Vollstaendiges Beispiel

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch();

// Kontext mit HTTP Basic Auth fuer alle Requests
const context = await browser.newContext({
  httpCredentials: {
    username: 'testuser',
    password: 's3cr3t',
    origin: 'https://protected.example.com',
    send: 'always'
  }
});

const page = await context.newPage();
await page.goto('https://protected.example.com/dashboard');
// Seite sollte ohne Login-Dialog laden

await context.close();
await browser.close();
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 0 (Interface, kein Klassenobjekt) |
| Properties | 4 (username, password, origin, send) |
| Events    | 0      |

**Fazit:** `HTTPCredentials` ist ein reines Konfigurations-Interface fuer
HTTP Basic Auth — keine Klasse mit Instanzmethoden. Die Konfiguration erfolgt
einmalig beim Erstellen des BrowserContext. Fuer fortgeschrittene Authentifizierung
(OAuth, Cookie-basiert, session storage) bietet Playwright die `storageState`-
Option als Alternative.

---

*Hinweis: https://playwright.dev/docs/api/class-credentials existiert nicht in
den aktuellen stabilen Playwright-Docs. Referenz: https://playwright.dev/docs/api/class-browser#browser-new-context*
