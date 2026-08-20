# class-apiresponseassertions — Playwright API Reference

`APIResponseAssertions` ist die Assertion-Klasse fuer `APIResponse`-Objekte aus Playwright-API-Tests. Sie bietet einen einzigen Matcher fuer HTTP-Statuspruefungen.

Zugriff via `expect(response).*`.

Matcher-Anzahl: 1 Matcher + Property `not`

---

## not

```typescript
not: APIResponseAssertions
```

Invertiert die nachfolgende Assertion.

```typescript
await expect(response).not.toBeOK();
```

---

## toBeOK()

```typescript
toBeOK(): Promise<void>
```

Prueft, ob der HTTP-Statuscode der Antwort im Erfolgsbereich `200..299` liegt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| — | — | — | — | Keine Parameter |

**Rueckgabe:** `Promise<void>`

```typescript
import { test, expect } from '@playwright/test';

test('API gibt Erfolgsantwort zurueck', async ({ request }) => {
  const response = await request.get('/api/products');
  await expect(response).toBeOK();
});

test('Geloeschte Ressource ist nicht mehr verfuegbar', async ({ request }) => {
  const response = await request.get('/api/products/geloescht');
  await expect(response).not.toBeOK();
  // Beispiel: Status 404 wuerde den Test bestehen lassen
});
```

---

## Praktische Hinweise

`toBeOK()` ist bewusst einfach gehalten. Fuer praezisere Statuspruefungen den Statuscode direkt pruefen:

```typescript
const response = await request.post('/api/orders', { data: payload });
await expect(response).toBeOK(); // Prueft nur 2xx

// Explizite Statuspruefung:
expect(response.status()).toBe(201);
expect(response.ok()).toBe(true);
```

---

## Matcher-Uebersicht (1 Matcher)

| Matcher | Prueft |
|---|---|
| `toBeOK` | HTTP-Statuscode im Bereich 200-299 |

---

Quelle: https://playwright.dev/docs/api/class-apiresponseassertions
