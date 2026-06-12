# Playwright — class: Clock

> **Manifest:** 7 Methoden, 0 Properties, 0 Events.
> Kontrolliert Zeit-APIs im Browser: Date, setTimeout, setInterval, requestAnimationFrame, performance.
> Gilt fuer den gesamten BrowserContext. Zugriff: `page.clock` oder `browserContext.clock`.

---

## Uebersicht

`Clock` ersetzt die nativen Browser-Zeit-APIs durch fake Implementierungen,
um deterministische Zeitsteuerung in Tests zu ermoeglichen. Betroffen sind:
`Date`, `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`,
`requestAnimationFrame`, `cancelAnimationFrame`, `requestIdleCallback`,
`cancelIdleCallback` und `performance`.

Wichtig: Die Clock-API wirkt auf den gesamten BrowserContext — alle Pages
und iframes.

---

## Methoden

### clock.fastForward(ticks)

Springt die Zeit vorwaerts, ohne alle Timer mehrfach auszuloesen.
Jeder faellige Timer wird hoechstens einmal gefeuert.

**Signatur:**
```typescript
clock.fastForward(ticks: number | string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `ticks` | `number \| string` | ja | — | Anzahl Millisekunden als Zahl oder als lesbarer String: `"08"` = 8s, `"01:00"` = 1min, `"02:34:10"` = 2h34m10s |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
// Numerisch
await page.clock.fastForward(1000);        // 1 Sekunde
await page.clock.fastForward(3600 * 1000); // 1 Stunde

// Lesbar
await page.clock.fastForward('30:00');     // 30 Minuten
await page.clock.fastForward('01:00:00'); // 1 Stunde
```

---

### clock.install(options?)

Installiert fake Zeit-Implementierungen. Muss vor der zu testenden
Seiten-Interaktion aufgerufen werden.

**Signatur:**
```typescript
clock.install(options?: {
  time?: number | string | Date;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.time` | `number \| string \| Date` | nein | aktuelles System-Datum | Startzeitpunkt der fake Uhr. Zahl = Unix-Timestamp (ms), String = ISO-Datum-String, Date-Objekt |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
// Mit festem Startpunkt (nuetzlich fuer reproduzierbare Tests)
await page.clock.install({ time: new Date('2024-01-15T10:00:00Z') });

// Ohne Option: aktuelles System-Datum
await page.clock.install();
```

---

### clock.pauseAt(time)

Springt zur angegebenen Zeit und pausiert die Uhr. Nach diesem Aufruf
werden keine Timer mehr gefeuert, bis `runFor()`, `fastForward()`,
`pauseAt()` oder `resume()` aufgerufen werden.

**Signatur:**
```typescript
clock.pauseAt(time: number | string | Date): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `time` | `number \| string \| Date` | ja | — | Zielzeitpunkt: Unix-Timestamp (ms), ISO-String oder Date-Objekt |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
// Einfrieren auf bestimmtes Datum
await page.clock.pauseAt(new Date('2020-02-02'));
await page.clock.pauseAt('2020-02-02');
await page.clock.pauseAt(1580601600000);

// Typischer Einsatz: Seite laden, dann auf bestimmte Zeit einfrieren
await page.clock.install({ time: new Date('2024-01-01') });
await page.goto('https://example.com');
await page.clock.pauseAt(new Date('2024-01-15T09:00:00'));
// Jetzt ist die Seite eingefroren — ideal fuer Screenshot-Tests
```

---

### clock.resume()

Setzt die fake Uhr fort. Zeit laeuft wieder, Timer werden normal gefeuert.

**Signatur:**
```typescript
clock.resume(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.clock.pauseAt(new Date('2024-01-15'));
// ... Assertions ...
await page.clock.resume(); // Zeit laeuft weiter
```

---

### clock.runFor(ticks)

Laesst die Zeit um `ticks` vorlaufen und feuert dabei ALLE faelligen Timer
(im Gegensatz zu `fastForward()`, das Timer nur einmal ausloest).

**Signatur:**
```typescript
clock.runFor(ticks: number | string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `ticks` | `number \| string` | ja | — | Millisekunden als Zahl oder lesbarer String (gleiche Formate wie `fastForward`) |

**Rueckgabe:** `Promise<void>`

**Unterschied zu `fastForward()`:**
- `runFor()`: Feuert *alle* Timer, die im Zeitfenster faellig werden (inkl. rekursiver Timer).
- `fastForward()`: Feuert jeden Timer hoechstens *einmal*.

**Beispiel:**
```javascript
// Alle Timer in den naechsten 5 Sekunden ausfuehren
await page.clock.runFor(5000);
await page.clock.runFor('05:00'); // 5 Minuten
```

---

### clock.setFixedTime(time)

Setzt `Date.now()` und `new Date()` auf einen festen Wert. Timer laufen
weiterhin normal — nur die zurueckgegebene Zeit ist eingefroren.

**Signatur:**
```typescript
clock.setFixedTime(time: number | string | Date): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `time` | `number \| string \| Date` | ja | — | Fester Zeitwert fuer alle Date-Aufrufe |

**Rueckgabe:** `Promise<void>`

**Hinweis:** Keine vorherige `install()`-Aufruf noetig — `setFixedTime()` kann
direkt genutzt werden ohne andere Time-APIs zu beeinflussen.

**Beispiel:**
```javascript
// Datum einfrieren fuer "Heute ist 2024-12-31"-Tests
await page.clock.setFixedTime(new Date('2024-12-31'));
await page.goto('https://example.com');
// Date.now() und new Date() geben jetzt immer 2024-12-31 zurueck
```

---

### clock.setSystemTime(time)

Setzt die Systemzeit, ohne Timer auszuloesen. Dient dazu, das Verhalten
der Seite bei Zeitsprungen zu testen.

**Signatur:**
```typescript
clock.setSystemTime(time: number | string | Date): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `time` | `number \| string \| Date` | ja | — | Neue Systemzeit |

**Rueckgabe:** `Promise<void>`

**Unterschied zu `setFixedTime()`:**
- `setFixedTime()`: Zeit bleibt eingefroren.
- `setSystemTime()`: Zeit wird gesetzt, laeuft dann aber normal weiter.

**Beispiel:**
```javascript
// Systemzeit setzen ohne Auswirkung auf Timer
await page.clock.setSystemTime(new Date('2023-06-01'));
```

---

## Typische Anwendungsmuster

### Muster 1: Bestimmtes Datum testen (Date-Only)

```javascript
// Nur Date.now() faelschen, Timer nicht beeinflussen
await page.clock.setFixedTime(new Date('2024-12-31T23:59:59'));
await page.goto('https://myapp.com/countdown');
await expect(page.getByText('1 Sekunde bis Neujahr')).toBeVisible();
```

### Muster 2: Timer-Verhalten testen

```javascript
await page.clock.install();
await page.goto('https://myapp.com/auto-refresh');
// Seite aktualisiert sich alle 30 Sekunden
await page.clock.runFor(30000);
await expect(page.getByText('Aktualisiert')).toBeVisible();
```

### Muster 3: Spezifisches Datum einfrieren + Screenshot

```javascript
await page.clock.install({ time: new Date('2024-01-01') });
await page.goto('https://myapp.com/dashboard');
await page.clock.pauseAt(new Date('2024-06-15T14:30:00'));
await page.screenshot({ path: 'dashboard-juni.png' });
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 7      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `setFixedTime()` ist die schnellste Option fuer einfache Datumstests.
`install()` + `pauseAt()` + `resume()` ermaoglicht praezise Kontrolle ueber
Timer-Verhalten. `runFor()` vs. `fastForward()` unterscheiden sich im
Umgang mit rekursiven Timern — bei Polling-Logik `runFor()` bevorzugen.

---

*Quelle: https://playwright.dev/docs/api/class-clock*
