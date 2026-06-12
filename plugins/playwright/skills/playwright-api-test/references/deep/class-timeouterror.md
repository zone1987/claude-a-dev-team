# class-timeouterror — Playwright TimeoutError Reference

`TimeoutError` is a subclass of the native JavaScript `Error` that Playwright throws when an
operation exceeds its configured timeout. It can be caught and type-narrowed using
`instanceof playwright.errors.TimeoutError`.

---

## Class Hierarchy

```
Error
  └── TimeoutError
```

`TimeoutError` inherits all standard `Error` properties:

| Property | Type | Description |
|----------|------|-------------|
| `message` | `string` | Description of which operation timed out and after how many ms |
| `name` | `string` | Always `"TimeoutError"` |
| `stack` | `string` | Stack trace from the throw site |

No additional custom properties are documented.

---

## When it is Thrown

`TimeoutError` is thrown by any operation that has a configurable `timeout` option, including:

| Operation | Default Timeout |
|-----------|----------------|
| `locator.waitFor()` | `actionTimeout` (0 = no limit) |
| `page.waitForSelector()` | `actionTimeout` |
| `page.waitForLoadState()` | `navigationTimeout` |
| `page.goto()` | `navigationTimeout` |
| `browserType.launch()` | 30 000 ms |
| `expect(locator).toBeVisible()` | `expect.timeout` (5 000 ms) |
| `expect.poll()` | `expect.timeout` |
| `expect.toPass()` | configurable |

---

## Import

```ts
import { errors } from '@playwright/test';
const { TimeoutError } = errors;
```

or from the core package:

```ts
import playwright from 'playwright';
const { TimeoutError } = playwright.errors;
```

---

## Usage Examples

### Catching a timeout

```ts
import { errors } from '@playwright/test';

test('handle optional banner', async ({ page }) => {
  try {
    await page.locator('.cookie-banner').waitFor({ timeout: 2_000 });
    await page.locator('.cookie-banner button').click();
  } catch (e) {
    if (!(e instanceof errors.TimeoutError)) throw e;
    // Banner did not appear; continue
  }
});
```

### Distinguishing timeout from other errors

```ts
import { errors } from '@playwright/test';

test('graceful timeout handling', async ({ page }) => {
  await page.goto('/slow-page').catch(e => {
    if (e instanceof errors.TimeoutError) {
      test.info().annotations.push({ type: 'slow', description: 'Navigation timed out' });
    } else {
      throw e;
    }
  });
});
```

### In a reporter

```ts
onTestEnd(test, result) {
  for (const err of result.errors) {
    if (err.message?.includes('TimeoutError')) {
      metrics.increment('timeout_failures', { project: test.parent.project()?.name });
    }
  }
}
```

---

## Manifest

| Category | Count |
|----------|-------|
| Custom properties | 0 (inherits `message`, `name`, `stack` from `Error`) |
| Custom methods | 0 |

**Fazit:** `TimeoutError` ist ein reiner Typ-Marker ohne eigene Properties. Sein Hauptzweck
ist `instanceof`-Pruefung, um Timeouts von anderen Fehlern zu unterscheiden und gezielt
abzufangen, ohne alle Fehler zu verschlucken.

---

Source: https://playwright.dev/docs/api/class-timeouterror
