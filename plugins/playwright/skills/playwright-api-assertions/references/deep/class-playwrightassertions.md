# class-playwrightassertions — Playwright API Reference

`PlaywrightAssertions` ist die Factory-Klasse, die die `expect()`-Funktion bereitstellt. Sie ist ueberladen und gibt je nach Typ des uebergebenen Argument die passende Assertion-Klasse zurueck. Alle Ueberladungen implementieren "Web-First Assertions", die automatisch retrien bis die Bedingung zutrifft oder der Timeout ablaeuft.

Standard-Timeout: 5000 ms (konfigurierbar via `TestConfig.expect.timeout`).

Methoden-Anzahl: 4 Ueberladungen von `expect()`

---

## expect(response)

```typescript
expect(response: APIResponse): APIResponseAssertions
```

Erstellt Assertion-Utilities fuer ein `APIResponse`-Objekt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `response` | `APIResponse` | ja | — | Antwort-Objekt aus `request.get()`, `request.post()` etc. |

**Rueckgabe:** `APIResponseAssertions`

```typescript
import { test, expect } from '@playwright/test';

test('API-Endpunkt antwortet erfolgreich', async ({ request }) => {
  const response = await request.get('/api/health');
  await expect(response).toBeOK();
});
```

**Verfuegbare Assertions:** Alle Methoden von `APIResponseAssertions` — insbesondere `toBeOK()`.

---

## expect(value)

```typescript
expect(value: unknown): GenericAssertions
```

Erstellt Assertion-Utilities fuer beliebige JavaScript-Werte. Kein auto-retry.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `value` | `unknown` | ja | — | Zu pruefender Wert (Primitive, Objekte, Arrays, Promises, Funktionen) |

**Rueckgabe:** `GenericAssertions`

```typescript
expect(42).toBe(42);
expect([1, 2, 3]).toHaveLength(3);
expect(user).toMatchObject({ role: 'admin' });
await expect(Promise.resolve('ok')).resolves.toBe('ok');
expect(() => JSON.parse('{bad}')).toThrow(SyntaxError);
```

**Verfuegbare Assertions:** Alle Methoden von `GenericAssertions`.

---

## expect(locator)

```typescript
expect(locator: Locator): LocatorAssertions
```

Erstellt Assertion-Utilities fuer einen `Locator`. Alle Assertions retrien automatisch.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `locator` | `Locator` | ja | — | Playwright-Locator fuer das zu pruefende Element |

**Rueckgabe:** `LocatorAssertions`

```typescript
await expect(page.getByRole('button', { name: 'Senden' })).toBeEnabled();
await expect(page.locator('.success-message')).toBeVisible();
await expect(page.getByLabel('Name')).toHaveValue('Max');
await expect(page.getByRole('listitem')).toHaveCount(3);
```

**Verfuegbare Assertions:** Alle 29 Matcher von `LocatorAssertions` + `not`.

---

## expect(page)

```typescript
expect(page: Page): PageAssertions
```

Erstellt Assertion-Utilities fuer ein `Page`-Objekt. Alle Assertions retrien automatisch.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `page` | `Page` | ja | — | Playwright-Seiteninstanz |

**Rueckgabe:** `PageAssertions`

```typescript
await expect(page).toHaveURL('/dashboard');
await expect(page).toHaveTitle('Meine App');
await expect(page).toHaveScreenshot('baseline.png');
```

**Verfuegbare Assertions:** Alle 6 Matcher von `PageAssertions` + `not`.

---

## Rueckgabetypen nach Argument

| Argument-Typ | Rueckgabetyp | Auto-Retry |
|---|---|---|
| `APIResponse` | `APIResponseAssertions` | nein |
| beliebiger Wert | `GenericAssertions` | nein |
| `Locator` | `LocatorAssertions` | ja |
| `Page` | `PageAssertions` | ja |

---

## Soft Assertions

`expect.soft()` markiert fehlgeschlagene Assertions, bricht den Test aber nicht sofort ab. Alle Fehler werden am Testende gesammelt gemeldet.

```typescript
// Schlaegt fehl, fuehrt Test aber fort:
await expect.soft(page.locator('.title')).toHaveText('Erwarteter Titel');
await expect.soft(page.locator('.count')).toHaveText('5');
// Erst hier wird geworfen, wenn soft assertions fehlgeschlagen sind:
```

---

## expect.poll()

Fuehrt eine Funktion wiederholt aus und prueft das Ergebnis mit einem GenericAssertion-Matcher. Nuetzlich fuer Nicht-Playwright-Zustaende.

```typescript
await expect.poll(async () => {
  const response = await fetch('/api/status');
  return (await response.json()).state;
}, {
  intervals: [1000, 2000, 5000],
  timeout: 15_000,
}).toBe('complete');
```

---

## expect.toPass()

Fuehrt einen Block wiederholt aus, bis er ohne Fehler durchlaeuft.

```typescript
await expect(async () => {
  const items = await page.getByRole('listitem').all();
  expect(items.length).toBeGreaterThan(2);
}).toPass({ timeout: 10_000 });
```

---

## expect.extend()

Registriert eigene Matcher.

```typescript
expect.extend({
  async toBeLoggedIn(page: Page) {
    const isLoggedIn = await page.locator('.user-menu').isVisible();
    return {
      message: () => `Erwartet, dass Benutzer ${isLoggedIn ? '' : 'nicht '}eingeloggt ist`,
      pass: isLoggedIn,
    };
  },
});

// Verwendung:
await expect(page).toBeLoggedIn();
```

---

Quelle: https://playwright.dev/docs/api/class-playwrightassertions
