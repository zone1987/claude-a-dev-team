# playwright-api-locator

Exhaustive API reference for all three classes surrounding Playwright locators.

## Included Classes

- [API-LOCATOR-CLASS-LOCATOR.md](API-LOCATOR-CLASS-LOCATOR.md) — 57 methods
- [API-LOCATOR-CLASS-FRAMELOCATOR.md](API-LOCATOR-CLASS-FRAMELOCATOR.md) — 11 methods (incl. deprecated)
- [API-LOCATOR-CLASS-SELECTORS.md](API-LOCATOR-CLASS-SELECTORS.md) — 2 methods

## Manifest

| Class | Methods/Properties | Conclusion |
|---|---|---|
| Locator | 57 | Core class for all element interactions; all getBy* factory methods, filtering, composition and actions fully documented. |
| FrameLocator | 11 | Narrow interface for iframe navigation; owner() and contentFrame() are the modern alternatives to the deprecated first/last/nth. |
| Selectors | 2 | Only register() and setTestIdAttribute(); both must be called once before page creation. |
