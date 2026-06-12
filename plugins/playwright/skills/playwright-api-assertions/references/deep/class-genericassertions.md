# class-genericassertions — Playwright API Reference

`GenericAssertions` sind Jest-kompatible Assertion-Methoden fuer beliebige JavaScript-Werte. Sie **retrien nicht automatisch** (im Gegensatz zu `LocatorAssertions`). Geeignet fuer Daten, Primitive, Objekte, Promises und Funktionen.

Zugriff via `expect(value).*`.

Methoden-Anzahl: 27 Methoden + Properties `not`, `resolves`, `rejects`

---

## Properties

### not

```typescript
not: GenericAssertions
```

Invertiert die nachfolgende Assertion.

```typescript
expect(value).not.toBe(null);
expect(fn).not.toThrow();
```

---

### resolves

```typescript
resolves: GenericAssertions
```

Entpackt einen aufgeloesten Promise-Wert fuer nachfolgende Assertions. Schlaegt fehl, wenn der Promise abgelehnt wird.

```typescript
await expect(Promise.resolve(42)).resolves.toBe(42);
await expect(fetchUser()).resolves.toHaveProperty('name');
```

---

### rejects

```typescript
rejects: GenericAssertions
```

Entpackt den Ablehnungsgrund eines abgelehnten Promises fuer nachfolgende Assertions. Schlaegt fehl, wenn der Promise aufgeloest wird.

```typescript
await expect(Promise.reject(new Error('fail'))).rejects.toThrow('fail');
```

---

## Asymmetrische Matcher (Pattern-Matching fuer toEqual/toMatchObject)

### any()

```typescript
any(constructor: Function): AsymmetricMatcher
```

Matcht jede Instanz des angegebenen Konstruktors oder primitiven Typs.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `constructor` | `Function` | ja | — | Konstruktorfunktion z.B. `String`, `Number`, `Date` |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect({ id: 5, name: 'Test' }).toEqual({
  id: expect.any(Number),
  name: expect.any(String),
});
```

---

### anything()

```typescript
anything(): AsymmetricMatcher
```

Matcht jeden Wert ausser `null` und `undefined`.

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect({ value: 42 }).toEqual({ value: expect.anything() });
```

---

### arrayContaining()

```typescript
arrayContaining(expected: Array<unknown>): AsymmetricMatcher
```

Matcht ein Array, das alle erwarteten Elemente in beliebiger Reihenfolge enthaelt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `Array<unknown>` | ja | — | Teilmenge der erwarteten Elemente |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect([1, 2, 3, 4]).toEqual(expect.arrayContaining([2, 4]));
```

---

### arrayOf()

```typescript
arrayOf(constructor: Function): AsymmetricMatcher
```

Matcht ein Array, dessen alle Elemente Instanzen des angegebenen Typs sind.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `constructor` | `Function` | ja | — | Konstruktorfunktion fuer alle Elemente |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect([1, 2, 3]).toEqual(expect.arrayOf(Number));
```

---

### closeTo()

```typescript
closeTo(expected: number, numDigits?: number): AsymmetricMatcher
```

Matcht Gleitkommazahlen mit angegebener Dezimalstellengenauigkeit.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number` | ja | — | Erwarteter Wert |
| `numDigits` | `number` | nein | `2` | Anzahl Dezimalstellen fuer Vergleich |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect(0.1 + 0.2).toEqual(expect.closeTo(0.3, 5));
```

---

### objectContaining()

```typescript
objectContaining(expected: Record<string, unknown>): AsymmetricMatcher
```

Matcht ein Objekt, das alle erwarteten Eigenschaften enthaelt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `Record<string, unknown>` | ja | — | Teilmenge der erwarteten Eigenschaften |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect({ id: 1, name: 'Test', extra: true }).toEqual(
  expect.objectContaining({ id: 1, name: 'Test' })
);
```

---

### stringContaining()

```typescript
stringContaining(expected: string): AsymmetricMatcher
```

Matcht Strings, die den erwarteten Teilstring enthalten.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string` | ja | — | Gesuchter Teilstring |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect('Hallo Welt').toEqual(expect.stringContaining('Welt'));
```

---

### stringMatching()

```typescript
stringMatching(expected: string | RegExp): AsymmetricMatcher
```

Matcht Strings, die dem angegebenen Muster entsprechen.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string \| RegExp` | ja | — | Gesuchtes Muster oder Regex |

**Rueckgabe:** `AsymmetricMatcher`

```typescript
expect('user@example.com').toEqual(expect.stringMatching(/@example\.com$/));
```

---

## Direkte Assertion-Methoden

### toBe()

```typescript
toBe(expected: unknown): void
```

Prueft strikte Gleichheit via `Object.is()` (wie `===`).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `unknown` | ja | — | Erwarteter Wert (Referenzvergleich) |

```typescript
expect(42).toBe(42);
expect(obj).toBe(obj); // gleiche Referenz
```

---

### toBeCloseTo()

```typescript
toBeCloseTo(expected: number, numDigits?: number): void
```

Prueft Gleitkommazahlen mit angegebener Dezimalstellengenauigkeit.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number` | ja | — | Erwarteter Wert |
| `numDigits` | `number` | nein | `2` | Anzahl Dezimalstellen |

```typescript
expect(0.1 + 0.2).toBeCloseTo(0.3, 5);
```

---

### toBeDefined()

```typescript
toBeDefined(): void
```

Prueft, dass der Wert nicht `undefined` ist.

```typescript
expect(someVar).toBeDefined();
```

---

### toBeFalsy()

```typescript
toBeFalsy(): void
```

Prueft, dass der Wert falsy ist (`false`, `0`, `''`, `null`, `undefined`, `NaN`).

```typescript
expect(0).toBeFalsy();
expect('').toBeFalsy();
```

---

### toBeGreaterThan()

```typescript
toBeGreaterThan(expected: number | bigint): void
```

Prueft `value > expected`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number \| bigint` | ja | — | Vergleichswert |

```typescript
expect(count).toBeGreaterThan(0);
```

---

### toBeGreaterThanOrEqual()

```typescript
toBeGreaterThanOrEqual(expected: number | bigint): void
```

Prueft `value >= expected`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number \| bigint` | ja | — | Vergleichswert |

```typescript
expect(items.length).toBeGreaterThanOrEqual(1);
```

---

### toBeInstanceOf()

```typescript
toBeInstanceOf(expected: Function): void
```

Prueft `value instanceof expected`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `Function` | ja | — | Konstruktorfunktion |

```typescript
expect(new Date()).toBeInstanceOf(Date);
```

---

### toBeLessThan()

```typescript
toBeLessThan(expected: number | bigint): void
```

Prueft `value < expected`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number \| bigint` | ja | — | Vergleichswert |

```typescript
expect(responseTime).toBeLessThan(500);
```

---

### toBeLessThanOrEqual()

```typescript
toBeLessThanOrEqual(expected: number | bigint): void
```

Prueft `value <= expected`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number \| bigint` | ja | — | Vergleichswert |

```typescript
expect(retries).toBeLessThanOrEqual(3);
```

---

### toBeNaN()

```typescript
toBeNaN(): void
```

Prueft, ob der Wert `NaN` ist.

```typescript
expect(NaN).toBeNaN();
expect(parseInt('abc', 10)).toBeNaN();
```

---

### toBeNull()

```typescript
toBeNull(): void
```

Prueft, ob der Wert `null` ist.

```typescript
expect(result).toBeNull();
```

---

### toBeTruthy()

```typescript
toBeTruthy(): void
```

Prueft, dass der Wert truthy ist (alles ausser `false`, `0`, `''`, `null`, `undefined`, `NaN`).

```typescript
expect('hello').toBeTruthy();
expect(1).toBeTruthy();
```

---

### toBeUndefined()

```typescript
toBeUndefined(): void
```

Prueft, ob der Wert `undefined` ist.

```typescript
expect(obj.missingProp).toBeUndefined();
```

---

### toContain() — String

```typescript
toContain(expected: string): void
```

Prueft, ob der String den erwarteten Teilstring enthaelt (case-sensitive).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string` | ja | — | Gesuchter Teilstring |

```typescript
expect('Hallo Welt').toContain('Welt');
```

---

### toContain() — Array/Set

```typescript
toContain(expected: unknown): void
```

Prueft, ob Array oder Set das Element enthaelt (Referenzvergleich).

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `unknown` | ja | — | Gesuchtes Element |

```typescript
expect([1, 2, 3]).toContain(2);
```

---

### toContainEqual()

```typescript
toContainEqual(expected: unknown): void
```

Prueft, ob Array oder Set ein Element enthaelt, das via tiefer Gleichheit `expected` entspricht.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `unknown` | ja | — | Erwartetes Element (tiefer Vergleich) |

```typescript
expect(users).toContainEqual({ id: 1, name: 'Max' });
```

---

### toEqual()

```typescript
toEqual(expected: unknown): void
```

Prueft tiefe Gleichheit; unterstuetzt asymmetrische Matcher.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `unknown` | ja | — | Erwarteter Wert (tiefer Vergleich) |

```typescript
expect({ a: 1, b: { c: 2 } }).toEqual({ a: 1, b: { c: 2 } });
```

---

### toHaveLength()

```typescript
toHaveLength(expected: number): void
```

Prueft die `.length`-Eigenschaft des Werts.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `number` | ja | — | Erwartete Laenge |

```typescript
expect([1, 2, 3]).toHaveLength(3);
expect('Hallo').toHaveLength(5);
```

---

### toHaveProperty()

```typescript
toHaveProperty(keyPath: string, expected?: unknown): void
```

Prueft, ob eine Eigenschaft am angegebenen Pfad existiert; optional mit Wertvergleich.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `keyPath` | `string` | ja | — | Eigenschaftspfad mit Punkt- oder Klammer-Notation |
| `expected` | `unknown` | nein | — | Erwarteter Wert |

```typescript
expect(obj).toHaveProperty('user.name');
expect(obj).toHaveProperty('user.age', 30);
expect(arr).toHaveProperty('[0].id', 1);
```

---

### toMatch()

```typescript
toMatch(expected: RegExp | string): void
```

Prueft, ob ein String dem angegebenen Regex oder Teilstring entspricht.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `RegExp \| string` | ja | — | Regex oder Teilstring |

```typescript
expect('test@example.com').toMatch(/@example\.com$/);
```

---

### toMatchObject()

```typescript
toMatchObject(expected: Record<string, unknown> | Array<unknown>): void
```

Prueft tiefe Gleichheit; erlaubt zusaetzliche Eigenschaften im tatsaechlichen Objekt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `Record<string, unknown> \| Array<unknown>` | ja | — | Erwartete (Teil-)Struktur |

```typescript
expect(response).toMatchObject({ status: 'ok', data: { count: 5 } });
```

---

### toStrictEqual()

```typescript
toStrictEqual(expected: unknown): void
```

Wie `toEqual`, aber strikter: prueft auch Typen und unterscheidet `undefined`-Eigenschaften.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `unknown` | ja | — | Erwarteter Wert (strikter Vergleich) |

```typescript
expect({ a: undefined }).toStrictEqual({ a: undefined });
```

---

### toThrow()

```typescript
toThrow(expected?: string | RegExp | Error | { message?: string | RegExp }): void
```

Prueft, ob eine Funktion einen Fehler wirft; optional mit Uebereinstimmung der Fehlermeldung oder des Typs.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Error \| { message?: string \| RegExp }` | nein | — | Erwartete Fehlermeldung, Regex, Instanz oder Objekt |

```typescript
expect(() => JSON.parse('invalid')).toThrow(SyntaxError);
expect(() => riskyFn()).toThrow('Unerwarteter Fehler');
```

---

### toThrowError()

```typescript
toThrowError(expected?: string | RegExp | Error | { message?: string | RegExp }): void
```

Alias fuer `toThrow()`.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | — | nein | — | Identisch mit `toThrow()` |

```typescript
expect(() => riskyFn()).toThrowError(/nicht gefunden/);
```

---

## Methoden-Uebersicht (27 Methoden)

| Kategorie | Methoden |
|---|---|
| Asymmetrisch | `any`, `anything`, `arrayContaining`, `arrayOf`, `closeTo`, `objectContaining`, `stringContaining`, `stringMatching` |
| Gleichheit | `toBe`, `toEqual`, `toStrictEqual` |
| Wahrheitswerte | `toBeTruthy`, `toBeFalsy`, `toBeDefined`, `toBeUndefined`, `toBeNull`, `toBeNaN` |
| Vergleich (Zahlen) | `toBeGreaterThan`, `toBeGreaterThanOrEqual`, `toBeLessThan`, `toBeLessThanOrEqual`, `toBeCloseTo` |
| Typ | `toBeInstanceOf` |
| String/Array | `toContain`, `toContainEqual`, `toMatch`, `toMatchObject`, `toHaveLength`, `toHaveProperty` |
| Fehlerbehandlung | `toThrow`, `toThrowError` |

---

Quelle: https://playwright.dev/docs/api/class-genericassertions
