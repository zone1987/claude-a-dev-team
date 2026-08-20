# playwright-api-assertions

Erschoepfende API-Referenz fuer alle sechs Playwright-Assertion-Klassen.

## Enthaltene Klassen

- [API-ASSERTIONS-CLASS-LOCATORASSERTIONS.md](API-ASSERTIONS-CLASS-LOCATORASSERTIONS.md) — 29 Matcher + `not`
- [API-ASSERTIONS-CLASS-PAGEASSERTIONS.md](API-ASSERTIONS-CLASS-PAGEASSERTIONS.md) — 6 Matcher + `not`
- [API-ASSERTIONS-CLASS-APIRESPONSEASSERTIONS.md](API-ASSERTIONS-CLASS-APIRESPONSEASSERTIONS.md) — 1 Matcher + `not`
- [API-ASSERTIONS-CLASS-GENERICASSERTIONS.md](API-ASSERTIONS-CLASS-GENERICASSERTIONS.md) — 27 Methoden + `not`/`resolves`/`rejects`
- [API-ASSERTIONS-CLASS-SNAPSHOTASSERTIONS.md](API-ASSERTIONS-CLASS-SNAPSHOTASSERTIONS.md) — 2 Methoden
- [API-ASSERTIONS-CLASS-PLAYWRIGHTASSERTIONS.md](API-ASSERTIONS-CLASS-PLAYWRIGHTASSERTIONS.md) — 4 expect()-Ueberladungen

## Manifest

| Klasse | Methoden/Matcher | Fazit |
|---|---|---|
| LocatorAssertions | 29 + `not` | Reichhaltigste Klasse; alle Matcher retrien automatisch bis timeout; `not` invertiert jeden Matcher. |
| PageAssertions | 6 + `not` | Prueft URL, Titel, Screenshots und ARIA-Snapshots auf Seitenebene. |
| APIResponseAssertions | 1 + `not` | Nur `toBeOK()`; genuegt fuer HTTP-Statuspruefung in API-Tests. |
| GenericAssertions | 27 + `not`/`resolves`/`rejects` | Jest-kompatible Matcher ohne auto-retry; deckt Primitive, Objekte, Promises und Funktionen ab. |
| SnapshotAssertions | 2 | `toMatchSnapshot` fuer Strings/Buffer mit Pixel-Toleranz; kein auto-retry. |
| PlaywrightAssertions | 4 | expect()-Factory-Ueberladungen; gibt je nach Argument-Typ die passende Assertion-Klasse zurueck. |
