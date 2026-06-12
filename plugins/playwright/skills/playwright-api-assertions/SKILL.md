---
name: playwright-api-assertions
description: >
  Vollstaendige Playwright API-Referenz fuer alle Assertion-Klassen: LocatorAssertions
  (alle toBe*/toHave*/toContain*-Matcher mit auto-retry), PageAssertions, APIResponseAssertions,
  GenericAssertions, SnapshotAssertions und PlaywrightAssertions (expect-Factory). Jeder
  Matcher mit vollstaendiger Signatur, allen Parametern und Beispiel. Playwright assertions
  class-locatorassertions class-pageassertions class-apiresponseassertions class-genericassertions
  class-snapshotassertions class-playwrightassertions expect matchers all.
triggers:
  - playwright assertions api
  - class-locatorassertions
  - class-pageassertions
  - class-apiresponseassertions
  - class-genericassertions
  - class-snapshotassertions
  - class-playwrightassertions
  - playwright expect api
  - locatorassertions methoden
  - playwright assertions vollstaendig
  - playwright assertions complete reference
  - playwright matchers api reference
  - toBeVisible api
  - toHaveText api
  - toHaveScreenshot api
  - toMatchSnapshot api
  - playwright assertions alle matcher
  - playwright expect factory
  - playwright assertions typescript
  - playwright assertions parameter
---

Erschoepfende API-Referenz fuer alle sechs Playwright-Assertion-Klassen.

## Enthaltene Klassen

- [references/deep/class-locatorassertions.md](references/deep/class-locatorassertions.md) — 29 Matcher + `not`
- [references/deep/class-pageassertions.md](references/deep/class-pageassertions.md) — 6 Matcher + `not`
- [references/deep/class-apiresponseassertions.md](references/deep/class-apiresponseassertions.md) — 1 Matcher + `not`
- [references/deep/class-genericassertions.md](references/deep/class-genericassertions.md) — 27 Methoden + `not`/`resolves`/`rejects`
- [references/deep/class-snapshotassertions.md](references/deep/class-snapshotassertions.md) — 2 Methoden
- [references/deep/class-playwrightassertions.md](references/deep/class-playwrightassertions.md) — 4 expect()-Ueberladungen

## Manifest

| Klasse | Methoden/Matcher | Fazit |
|---|---|---|
| LocatorAssertions | 29 + `not` | Reichhaltigste Klasse; alle Matcher retrien automatisch bis timeout; `not` invertiert jeden Matcher. |
| PageAssertions | 6 + `not` | Prueft URL, Titel, Screenshots und ARIA-Snapshots auf Seitenebene. |
| APIResponseAssertions | 1 + `not` | Nur `toBeOK()`; genuegt fuer HTTP-Statuspruefung in API-Tests. |
| GenericAssertions | 27 + `not`/`resolves`/`rejects` | Jest-kompatible Matcher ohne auto-retry; deckt Primitive, Objekte, Promises und Funktionen ab. |
| SnapshotAssertions | 2 | `toMatchSnapshot` fuer Strings/Buffer mit Pixel-Toleranz; kein auto-retry. |
| PlaywrightAssertions | 4 | expect()-Factory-Ueberladungen; gibt je nach Argument-Typ die passende Assertion-Klasse zurueck. |
