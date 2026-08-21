# class-genericassertions — Playwright API Reference

`GenericAssertions` are Jest-compatible assertion methods for arbitrary JavaScript values. They **do not retry automatically** (unlike `LocatorAssertions`). Suitable for data, primitives, objects, promises and functions.

Accessed via `expect(value).*`.

Method count: 27 methods + properties `not`, `resolves`, `rejects`

---

## Contents

- [Properties](#properties)
- [Asymmetric matchers (pattern matching for toEqual/toMatchObject)](#asymmetric-matchers-pattern-matching-for-toequaltomatchobject)
- [Direct assertion methods](#direct-assertion-methods)
- [Method overview (27 methods)](#method-overview-27-methods)

## Properties

### not

```typescript
not: GenericAssertions
```

Inverts the following assertion.

```typescript
expect(value).not.toBe(null);
expect(fn).not.toThrow();
```

---

### resolves

```typescript
resolves: GenericAssertions
```

Unwraps a resolved promise value for the following assertions. Fails if the promise is rejected.

```typescript
await expect(Promise.resolve(42)).resolves.toBe(42);
await expect(fetchUser()).resolves.toHaveProperty('name');
```

---

### rejects

```typescript
rejects: GenericAssertions
```

Unwraps the rejection reason of a rejected promise for the following assertions. Fails if the promise is resolved.

```typescript
await expect(Promise.reject(new Error('fail'))).rejects.toThrow('fail');
```

---

## Asymmetric matchers (pattern matching for toEqual/toMatchObject)

### any()

```typescript
any(constructor: Function): AsymmetricMatcher
```

Matches any instance of the given constructor or primitive type.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `constructor` | `Function` | yes | — | Constructor function e.g. `String`, `Number`, `Date` |

**Returns:** `AsymmetricMatcher`

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

Matches any value except `null` and `undefined`.

**Returns:** `AsymmetricMatcher`

```typescript
expect({ value: 42 }).toEqual({ value: expect.anything() });
```

---

### arrayContaining()

```typescript
arrayContaining(expected: Array<unknown>): AsymmetricMatcher
```

Matches an array that contains all expected elements in any order.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `Array<unknown>` | yes | — | Subset of the expected elements |

**Returns:** `AsymmetricMatcher`

```typescript
expect([1, 2, 3, 4]).toEqual(expect.arrayContaining([2, 4]));
```

---

### arrayOf()

```typescript
arrayOf(constructor: Function): AsymmetricMatcher
```

Matches an array whose elements are all instances of the given type.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `constructor` | `Function` | yes | — | Constructor function for all elements |

**Returns:** `AsymmetricMatcher`

```typescript
expect([1, 2, 3]).toEqual(expect.arrayOf(Number));
```

---

### closeTo()

```typescript
closeTo(expected: number, numDigits?: number): AsymmetricMatcher
```

Matches floating-point numbers with the given decimal precision.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number` | yes | — | Expected value |
| `numDigits` | `number` | no | `2` | Number of decimal places for the comparison |

**Returns:** `AsymmetricMatcher`

```typescript
expect(0.1 + 0.2).toEqual(expect.closeTo(0.3, 5));
```

---

### objectContaining()

```typescript
objectContaining(expected: Record<string, unknown>): AsymmetricMatcher
```

Matches an object that contains all expected properties.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `Record<string, unknown>` | yes | — | Subset of the expected properties |

**Returns:** `AsymmetricMatcher`

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

Matches strings that contain the expected substring.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string` | yes | — | Substring to look for |

**Returns:** `AsymmetricMatcher`

```typescript
expect('Hallo Welt').toEqual(expect.stringContaining('Welt'));
```

---

### stringMatching()

```typescript
stringMatching(expected: string | RegExp): AsymmetricMatcher
```

Matches strings that match the given pattern.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string \| RegExp` | yes | — | Pattern or regex to look for |

**Returns:** `AsymmetricMatcher`

```typescript
expect('user@example.com').toEqual(expect.stringMatching(/@example\.com$/));
```

---

## Direct assertion methods

### toBe()

```typescript
toBe(expected: unknown): void
```

Checks strict equality via `Object.is()` (like `===`).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `unknown` | yes | — | Expected value (reference comparison) |

```typescript
expect(42).toBe(42);
expect(obj).toBe(obj); // same reference
```

---

### toBeCloseTo()

```typescript
toBeCloseTo(expected: number, numDigits?: number): void
```

Checks floating-point numbers with the given decimal precision.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number` | yes | — | Expected value |
| `numDigits` | `number` | no | `2` | Number of decimal places |

```typescript
expect(0.1 + 0.2).toBeCloseTo(0.3, 5);
```

---

### toBeDefined()

```typescript
toBeDefined(): void
```

Checks that the value is not `undefined`.

```typescript
expect(someVar).toBeDefined();
```

---

### toBeFalsy()

```typescript
toBeFalsy(): void
```

Checks that the value is falsy (`false`, `0`, `''`, `null`, `undefined`, `NaN`).

```typescript
expect(0).toBeFalsy();
expect('').toBeFalsy();
```

---

### toBeGreaterThan()

```typescript
toBeGreaterThan(expected: number | bigint): void
```

Checks `value > expected`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number \| bigint` | yes | — | Comparison value |

```typescript
expect(count).toBeGreaterThan(0);
```

---

### toBeGreaterThanOrEqual()

```typescript
toBeGreaterThanOrEqual(expected: number | bigint): void
```

Checks `value >= expected`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number \| bigint` | yes | — | Comparison value |

```typescript
expect(items.length).toBeGreaterThanOrEqual(1);
```

---

### toBeInstanceOf()

```typescript
toBeInstanceOf(expected: Function): void
```

Checks `value instanceof expected`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `Function` | yes | — | Constructor function |

```typescript
expect(new Date()).toBeInstanceOf(Date);
```

---

### toBeLessThan()

```typescript
toBeLessThan(expected: number | bigint): void
```

Checks `value < expected`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number \| bigint` | yes | — | Comparison value |

```typescript
expect(responseTime).toBeLessThan(500);
```

---

### toBeLessThanOrEqual()

```typescript
toBeLessThanOrEqual(expected: number | bigint): void
```

Checks `value <= expected`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number \| bigint` | yes | — | Comparison value |

```typescript
expect(retries).toBeLessThanOrEqual(3);
```

---

### toBeNaN()

```typescript
toBeNaN(): void
```

Checks whether the value is `NaN`.

```typescript
expect(NaN).toBeNaN();
expect(parseInt('abc', 10)).toBeNaN();
```

---

### toBeNull()

```typescript
toBeNull(): void
```

Checks whether the value is `null`.

```typescript
expect(result).toBeNull();
```

---

### toBeTruthy()

```typescript
toBeTruthy(): void
```

Checks that the value is truthy (anything except `false`, `0`, `''`, `null`, `undefined`, `NaN`).

```typescript
expect('hello').toBeTruthy();
expect(1).toBeTruthy();
```

---

### toBeUndefined()

```typescript
toBeUndefined(): void
```

Checks whether the value is `undefined`.

```typescript
expect(obj.missingProp).toBeUndefined();
```

---

### toContain() — string

```typescript
toContain(expected: string): void
```

Checks whether the string contains the expected substring (case-sensitive).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string` | yes | — | Substring to look for |

```typescript
expect('Hallo Welt').toContain('Welt');
```

---

### toContain() — Array/Set

```typescript
toContain(expected: unknown): void
```

Checks whether an array or set contains the element (reference comparison).

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `unknown` | yes | — | Element to look for |

```typescript
expect([1, 2, 3]).toContain(2);
```

---

### toContainEqual()

```typescript
toContainEqual(expected: unknown): void
```

Checks whether an array or set contains an element that matches `expected` by deep equality.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `unknown` | yes | — | Expected element (deep comparison) |

```typescript
expect(users).toContainEqual({ id: 1, name: 'Max' });
```

---

### toEqual()

```typescript
toEqual(expected: unknown): void
```

Checks deep equality; supports asymmetric matchers.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `unknown` | yes | — | Expected value (deep comparison) |

```typescript
expect({ a: 1, b: { c: 2 } }).toEqual({ a: 1, b: { c: 2 } });
```

---

### toHaveLength()

```typescript
toHaveLength(expected: number): void
```

Checks the `.length` property of the value.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `number` | yes | — | Expected length |

```typescript
expect([1, 2, 3]).toHaveLength(3);
expect('Hallo').toHaveLength(5);
```

---

### toHaveProperty()

```typescript
toHaveProperty(keyPath: string, expected?: unknown): void
```

Checks whether a property exists at the given path; optionally with a value comparison.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `keyPath` | `string` | yes | — | Property path with dot or bracket notation |
| `expected` | `unknown` | no | — | Expected value |

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

Checks whether a string matches the given regex or substring.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `RegExp \| string` | yes | — | Regex or substring |

```typescript
expect('test@example.com').toMatch(/@example\.com$/);
```

---

### toMatchObject()

```typescript
toMatchObject(expected: Record<string, unknown> | Array<unknown>): void
```

Checks deep equality; allows additional properties in the actual object.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `Record<string, unknown> \| Array<unknown>` | yes | — | Expected (partial) structure |

```typescript
expect(response).toMatchObject({ status: 'ok', data: { count: 5 } });
```

---

### toStrictEqual()

```typescript
toStrictEqual(expected: unknown): void
```

Like `toEqual`, but stricter: it also checks types and distinguishes `undefined` properties.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `unknown` | yes | — | Expected value (strict comparison) |

```typescript
expect({ a: undefined }).toStrictEqual({ a: undefined });
```

---

### toThrow()

```typescript
toThrow(expected?: string | RegExp | Error | { message?: string | RegExp }): void
```

Checks whether a function throws an error; optionally matching the error message or the type.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | `string \| RegExp \| Error \| { message?: string \| RegExp }` | no | — | Expected error message, regex, instance or object |

```typescript
expect(() => JSON.parse('invalid')).toThrow(SyntaxError);
expect(() => riskyFn()).toThrow('Unerwarteter Fehler');
```

---

### toThrowError()

```typescript
toThrowError(expected?: string | RegExp | Error | { message?: string | RegExp }): void
```

Alias for `toThrow()`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `expected` | — | no | — | Identical to `toThrow()` |

```typescript
expect(() => riskyFn()).toThrowError(/nicht gefunden/);
```

---

## Method overview (27 methods)

| Category | Methods |
|---|---|
| Asymmetric | `any`, `anything`, `arrayContaining`, `arrayOf`, `closeTo`, `objectContaining`, `stringContaining`, `stringMatching` |
| Equality | `toBe`, `toEqual`, `toStrictEqual` |
| Truthiness | `toBeTruthy`, `toBeFalsy`, `toBeDefined`, `toBeUndefined`, `toBeNull`, `toBeNaN` |
| Comparison (numbers) | `toBeGreaterThan`, `toBeGreaterThanOrEqual`, `toBeLessThan`, `toBeLessThanOrEqual`, `toBeCloseTo` |
| Type | `toBeInstanceOf` |
| String/Array | `toContain`, `toContainEqual`, `toMatch`, `toMatchObject`, `toHaveLength`, `toHaveProperty` |
| Error handling | `toThrow`, `toThrowError` |

---

Source: https://playwright.dev/docs/api/class-genericassertions
