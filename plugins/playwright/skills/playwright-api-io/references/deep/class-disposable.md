# Playwright — class: Disposable

> **Manifest:** 1 Methode, 0 Properties, 0 Events.
> Erlaubt das Rueckgaengigmachen von Aktionen, die ein Disposable-Objekt zurueckgeben.
> Wird von verschiedenen Playwright-Methoden zurueckgegeben.

---

## Uebersicht

`Disposable` ist ein leichtgewichtiges Interface, das eine einzelne `dispose()`-
Methode bereitstellt, um eine zugehoerige Ressource oder Aktion zu widerrufen.
Es wird von Methoden zurueckgegeben, die eine reversible Aktion ausfuehren
(z.B. `page.addInitScript()`, `browserContext.addInitScript()`,
`tracing.group()`, `screencast.showActions()`, `screencast.showOverlay()`,
`screencast.start()`).

**Hinzugefuegt:** v1.59

---

## Methoden

### disposable.dispose()

Entfernt die zugehoerige Ressource oder macht die zugehoerige Aktion rueckgaengig.

**Signatur:**
```typescript
disposable.dispose(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
// Init-Script hinzufuegen und spaeter entfernen
const disposable = await page.addInitScript(() => {
  window.__testMode = true;
});
// ...
await disposable.dispose(); // Init-Script ist jetzt entfernt
```

---

## Rueckgabe-Kontext: Methoden die Disposable zurueckgeben

| Methode | Effekt beim Dispose |
|---------|---------------------|
| `page.addInitScript()` | Init-Script wird entfernt |
| `browserContext.addInitScript()` | Init-Script wird entfernt |
| `tracing.group()` | Trace-Gruppe wird geschlossen |
| `tracing.startHar()` | HAR-Aufzeichnung wird gestoppt |
| `screencast.showActions()` | Aktions-Annotierungen werden gestoppt |
| `screencast.showOverlay()` | Overlay wird entfernt |
| `screencast.start()` | Screencast-Aufnahme wird gestoppt |

---

## Using-Muster mit `await using` (TypeScript / ECMAScript)

Mit TypeScript und Symbol.asyncDispose kann das `Disposable`-Interface
sauber mit `await using` genutzt werden (sofern Playwright die
`Symbol.asyncDispose`-Schnittstelle implementiert):

```typescript
// Konzeptionelles Muster (TypeScript 5.2+)
{
  await using overlay = await page.screencast.showOverlay('<div>Loading...</div>');
  await performLongOperation();
  // overlay.dispose() wird automatisch am Ende des Blocks aufgerufen
}
```

---

## Typisches Nutzungsmuster

```javascript
// Visuellen Hint waehrend eines Test-Schritts anzeigen
async function withHint(page, label, fn) {
  const overlay = await page.screencast.showOverlay(
    `<div class="hint">${label}</div>`
  );
  try {
    await fn();
  } finally {
    await overlay.dispose();
  }
}

await withHint(page, 'Anmeldung', async () => {
  await page.fill('#email', 'test@example.com');
  await page.fill('#password', 'secret');
  await page.click('#login-button');
});
```

---

## Properties

Keine offentlichen Properties.

## Events

Keine Events.

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 1      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `Disposable` folgt dem Resource-Management-Pattern. Die Klasse ist
minimal gehalten — es gibt nur eine Methode. Wichtig ist es, `dispose()` im
`finally`-Block aufzurufen, um sicherzustellen, dass Ressourcen auch bei
Fehlern freigegeben werden. In TypeScript kann `await using` ab TS 5.2 als
elegante Alternative genutzt werden.

---

*Quelle: https://playwright.dev/docs/api/class-disposable*
