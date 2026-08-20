# playwright-api-assertions

Exhaustive API reference for all six Playwright assertion classes.

## Included classes

- [API-ASSERTIONS-CLASS-LOCATORASSERTIONS.md](API-ASSERTIONS-CLASS-LOCATORASSERTIONS.md) — 29 matchers + `not`
- [API-ASSERTIONS-CLASS-PAGEASSERTIONS.md](API-ASSERTIONS-CLASS-PAGEASSERTIONS.md) — 6 matchers + `not`
- [API-ASSERTIONS-CLASS-APIRESPONSEASSERTIONS.md](API-ASSERTIONS-CLASS-APIRESPONSEASSERTIONS.md) — 1 matcher + `not`
- [API-ASSERTIONS-CLASS-GENERICASSERTIONS.md](API-ASSERTIONS-CLASS-GENERICASSERTIONS.md) — 27 methods + `not`/`resolves`/`rejects`
- [API-ASSERTIONS-CLASS-SNAPSHOTASSERTIONS.md](API-ASSERTIONS-CLASS-SNAPSHOTASSERTIONS.md) — 2 methods
- [API-ASSERTIONS-CLASS-PLAYWRIGHTASSERTIONS.md](API-ASSERTIONS-CLASS-PLAYWRIGHTASSERTIONS.md) — 4 expect() overloads

## Manifest

| Class | Methods/Matchers | Conclusion |
|---|---|---|
| LocatorAssertions | 29 + `not` | Richest class; all matchers retry automatically until timeout; `not` inverts every matcher. |
| PageAssertions | 6 + `not` | Checks URL, title, screenshots and ARIA snapshots at page level. |
| APIResponseAssertions | 1 + `not` | Only `toBeOK()`; sufficient for HTTP status checking in API tests. |
| GenericAssertions | 27 + `not`/`resolves`/`rejects` | Jest-compatible matchers without auto-retry; covers primitives, objects, promises and functions. |
| SnapshotAssertions | 2 | `toMatchSnapshot` for strings/buffers with pixel tolerance; no auto-retry. |
| PlaywrightAssertions | 4 | expect() factory overloads; returns the matching assertion class depending on the argument type. |
