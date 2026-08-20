# playwright-api-locator

Erschoepfende API-Referenz fuer alle drei Klassen rund um Playwright-Locatoren.

## Enthaltene Klassen

- [API-LOCATOR-CLASS-LOCATOR.md](API-LOCATOR-CLASS-LOCATOR.md) — 57 Methoden
- [API-LOCATOR-CLASS-FRAMELOCATOR.md](API-LOCATOR-CLASS-FRAMELOCATOR.md) — 11 Methoden (incl. deprecated)
- [API-LOCATOR-CLASS-SELECTORS.md](API-LOCATOR-CLASS-SELECTORS.md) — 2 Methoden

## Manifest

| Klasse | Methoden/Properties | Fazit |
|---|---|---|
| Locator | 57 | Kernklasse fuer alle Element-Interaktionen; alle getBy*-Fabrikmethoden, Filterung, Komposition und Aktionen vollstaendig dokumentiert. |
| FrameLocator | 11 | Schmale Schnittstelle fuer iframe-Navigation; owner() und contentFrame() sind die modernen Alternativen zu den deprecated first/last/nth. |
| Selectors | 2 | Nur register() und setTestIdAttribute(); beide sind einmalig vor Seitenerstellung aufzurufen. |
