# Playwright — class: Logger

> **Manifest:** 2 Methoden, 0 Properties, 0 Events.
> **DEPRECATED** — Playwright empfiehlt stattdessen `Tracing` zu verwenden.
> Interface zur Weiterleitung von Playwright-internen Logs an benutzerdefinierte Log-Handler.

---

## Uebersicht

`Logger` ist ein Interface (kein konkretes Objekt), das beim Erstellen des
Browsers in der `logger`-Option uebergeben werden kann. Es erlaubt das
Abfangen und Weiterleiten interner Playwright-Logs an eigene Log-Systeme.

**Deprecation-Hinweis:** "The logs pumped through this class are incomplete.
Please use tracing instead." — Playwright empfiehlt die Verwendung von
`context.tracing` fuer vollstaendige Diagnostik.

---

## Interface-Methoden

### logger.isEnabled(name, severity)

Prueft, ob der Logger-Sink an Logs eines bestimmten Loggers mit dem
angegebenen Schweregrad interessiert ist. Playwright ruft diese Methode
vor dem eigentlichen `log()`-Aufruf auf — gibt `false` zurueck, wird
`log()` nicht aufgerufen.

**Signatur:**
```typescript
logger.isEnabled(
  name: string,
  severity: 'verbose' | 'info' | 'warning' | 'error'
): boolean
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `name` | `string` | ja | — | Name des Loggers (z.B. `'api'`, `'browser'`, `'context'`) |
| `severity` | `'verbose' \| 'info' \| 'warning' \| 'error'` | ja | — | Schweregrad des Log-Eintrags |

**Rueckgabe:** `boolean` — `true` wenn der Logger diesen Eintrag verarbeiten soll

**Beispiel:**
```javascript
const myLogger = {
  isEnabled: (name, severity) => {
    // Nur API-Logs auf Error-Level
    return name === 'api' && severity === 'error';
  },
  log: (name, severity, message, args) => {
    console.error(`[${name}] ${message}`);
  }
};
```

---

### logger.log(name, severity, message, args, hints)

Verarbeitet einen Log-Eintrag. Wird nur aufgerufen, wenn `isEnabled()`
`true` zurueckgegeben hat.

**Signatur:**
```typescript
logger.log(
  name: string,
  severity: 'verbose' | 'info' | 'warning' | 'error',
  message: string | Error,
  args: Array<Object>,
  hints: {
    color?: string;
  }
): void
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `name` | `string` | ja | — | Logger-Name |
| `severity` | `'verbose' \| 'info' \| 'warning' \| 'error'` | ja | — | Schweregrad |
| `message` | `string \| Error` | ja | — | Log-Nachricht als String oder Error-Objekt |
| `args` | `Array<Object>` | ja | — | Argumente fuer String-Formatierung |
| `hints` | `Object` | nein | `{}` | Formatierungs-Hinweise |
| `hints.color` | `string` | nein | — | Bevorzugte Farbe fuer Display (z.B. `'red'`, `'green'`) |

**Rueckgabe:** `void` (synchron)

---

## Verwendung

Das Logger-Interface wird beim `chromium.launch()` / `chromium.connect()` /
`firefox.launch()` / `webkit.launch()` als Option uebergeben:

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch({
  logger: {
    isEnabled: (name, severity) => name === 'api',
    log: (name, severity, message, args) => {
      const formatted = typeof message === 'string'
        ? message
        : message.message;
      console.log(`[Playwright/${name}/${severity}] ${formatted}`);
    }
  }
});
```

### Alle Logs aufzeichnen

```javascript
const logs: string[] = [];

const browser = await chromium.launch({
  logger: {
    isEnabled: () => true,
    log: (name, severity, message) => {
      logs.push(`[${severity}][${name}] ${message}`);
    }
  }
});

// ... Test-Aktionen ...

// Bei Fehlschlag anzeigen
if (testFailed) {
  console.log(logs.join('\n'));
}
```

---

## Properties

Keine offentlichen Properties — rein Interface-basiert.

## Events

Keine Events.

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 2      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** Logger ist deprecated und sollte in neuem Code nicht mehr verwendet
werden. Fuer vollstaendige Diagnostik und Debug-Informationen bietet
`context.tracing` eine weit ueberlegene Alternative mit visueller
Aufbereitung im Trace Viewer. Falls doch Logger benoetigt wird: `isEnabled()`
als Gating-Funktion implementieren, um Performance-Overhead durch selektives
Logging zu minimieren.

---

*Quelle: https://playwright.dev/docs/api/class-logger*
